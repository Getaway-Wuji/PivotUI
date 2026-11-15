#!/usr/bin/env node

// Dependency-free installer. The library belongs to this package, never cwd.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { createHash, randomUUID } from 'node:crypto';
import { fileURLToPath } from 'node:url';

const ROOT = fs.realpathSync(path.join(path.dirname(fileURLToPath(import.meta.url)), '..'));
const EDITIONS = { en: 'English', zh: 'Chinese' };
const AGENTS = new Set(['codex', 'claude-code', 'dsh', 'cursor', 'generic']);
const EXCLUDED = new Set(['.git', '.venv', '__pycache__', 'node_modules']);
const MANAGED_BY = 'pivotui-installer-v1';
const MANIFEST = '.pivotui-install.json';
// npm omits this nested ignore file even when it is in the files allowlist.
// Keep the exact bytes as a runtime resource; the release baseline verifies them.
const NPM_PRESERVED_FILE = 'mcp/skill-cluster/.gitignore';

class InstallError extends Error {}

const digest = data => createHash('sha256').update(data).digest('hex');
const posix = value => value.split(path.sep).join('/');
const isRecord = value => value !== null && typeof value === 'object' && !Array.isArray(value);

function statOrNull(filename) {
  try { return fs.lstatSync(filename); }
  catch (error) { if (error.code === 'ENOENT') return null; throw error; }
}

function canonical(filename) {
  let expanded = filename;
  if (filename === '~') expanded = os.homedir();
  else if (/^~[\\/]/.test(filename)) expanded = path.join(os.homedir(), filename.slice(2));
  let existing = path.resolve(expanded);
  const tail = [];
  while (!statOrNull(existing)) {
    const parent = path.dirname(existing);
    if (parent === existing) throw new InstallError(`Cannot resolve path: ${filename}`);
    tail.unshift(path.basename(existing));
    existing = parent;
  }
  return path.join(fs.realpathSync(existing), ...tail);
}

function within(child, parent) {
  const relative = path.relative(parent, child);
  return relative === '' || (!path.isAbsolute(relative) && relative !== '..' && !relative.startsWith(`..${path.sep}`));
}

function inventory(directory) {
  const rootStat = statOrNull(directory);
  if (!rootStat || rootStat.isSymbolicLink() || !rootStat.isDirectory()) {
    throw new InstallError(`Expected a real edition directory: ${directory}`);
  }
  const result = {};
  function visit(current) {
    for (const item of fs.readdirSync(current, { withFileTypes: true }).sort((a, b) => a.name < b.name ? -1 : a.name > b.name ? 1 : 0)) {
      const absolute = path.join(current, item.name);
      if (item.isDirectory() && EXCLUDED.has(item.name)) continue;
      if (item.isSymbolicLink()) throw new InstallError(`Symbolic links are not copied: ${absolute}`);
      if (item.isDirectory()) visit(absolute);
      else if (item.isFile()) {
        if (/\.py[co]$/.test(item.name)) continue;
        result[posix(path.relative(directory, absolute))] = digest(fs.readFileSync(absolute));
      } else throw new InstallError(`Unsupported file type: ${absolute}`);
    }
  }
  visit(directory);
  return Object.fromEntries(Object.entries(result).sort(([a], [b]) => a < b ? -1 : a > b ? 1 : 0));
}

function sameHashes(left, right) {
  return Object.keys(left).length === Object.keys(right).length && Object.entries(left).every(([name, hash]) => right[name] === hash);
}

function sourceInventory(edition) {
  const baseline = JSON.parse(fs.readFileSync(path.join(ROOT, 'language-sync.json'), 'utf8'));
  if (!isRecord(baseline) || !isRecord(baseline.files) || typeof baseline.cluster_version !== 'string') {
    throw new InstallError('Invalid release baseline; use a complete, unmodified package.');
  }
  const expected = {};
  for (const [name, pair] of Object.entries(baseline.files)) {
    if (!isRecord(pair) || typeof pair[edition] !== 'string' || !/^[a-f0-9]{64}$/.test(pair[edition])) {
      throw new InstallError('Invalid file hashes in the release baseline.');
    }
    expected[name] = pair[edition];
  }
  const actual = inventory(path.join(ROOT, edition));
  const sourceOverrides = {};
  if (!Object.hasOwn(actual, NPM_PRESERVED_FILE)) {
    const preserved = path.join(ROOT, 'bin', 'npm-resources', 'gitignore.txt');
    const stat = statOrNull(preserved);
    if (!stat || stat.isSymbolicLink() || !stat.isFile()) throw new InstallError('Missing npm preservation resource; use a complete, unmodified package.');
    actual[NPM_PRESERVED_FILE] = digest(fs.readFileSync(preserved));
    sourceOverrides[NPM_PRESERVED_FILE] = preserved;
  }
  if (!sameHashes(actual, expected)) {
    throw new InstallError('The edition differs from its release baseline. Use a complete, unmodified package.');
  }
  return { hashes: actual, version: baseline.cluster_version, sourceOverrides };
}

function pythonFingerprint(hashes) {
  // Match json.dumps(hashes, sort_keys=True, ensure_ascii=True) in install.py.
  const ascii = text => JSON.stringify(text).replace(/[\u007f-\uffff]/g, char => `\\u${char.charCodeAt(0).toString(16).padStart(4, '0')}`);
  const names = Object.keys(hashes).sort((a, b) => {
    const left = Array.from(a, c => c.codePointAt(0));
    const right = Array.from(b, c => c.codePointAt(0));
    for (let index = 0; index < Math.min(left.length, right.length); index++) {
      if (left[index] !== right[index]) return left[index] - right[index];
    }
    return left.length - right.length;
  });
  return digest(`{${names.map(name => `${ascii(name)}: ${ascii(hashes[name])}`).join(', ')}}`).slice(0, 16);
}

function defaultSkillsDir(agent, project, global) {
  if (agent === 'generic') throw new InstallError('--agent generic requires --skills-dir pointing to the host\'s skill directory.');
  if (!global) return path.join(project, agent === 'claude-code' ? '.claude' : '.agents', 'skills');
  if (agent === 'codex') return path.join(process.env.CODEX_HOME || path.join(os.homedir(), '.codex'), 'skills');
  if (agent === 'claude-code') return path.join(process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), '.claude'), 'skills');
  if (agent === 'dsh') return path.join(process.env.DSH_AGENTS_HOME || path.join(os.homedir(), '.agents'), 'skills');
  return path.join(os.homedir(), '.agents', 'skills');
}

function checkEntry(target) {
  const targetStat = statOrNull(target);
  if (!targetStat) return null;
  if (targetStat.isSymbolicLink() || !targetStat.isDirectory()) throw new InstallError(`Refusing to replace a linked or non-directory skill destination: ${target}`);
  const files = {};
  for (const name of ['SKILL.md', MANIFEST]) {
    const filename = path.join(target, name);
    const stat = statOrNull(filename);
    if (!stat || stat.isSymbolicLink() || !stat.isFile()) throw new InstallError(`Existing pivotui is not managed by this installer: ${target}`);
    files[name] = fs.readFileSync(filename);
  }
  let metadata;
  try { metadata = JSON.parse(files[MANIFEST].toString('utf8')); }
  catch { throw new InstallError(`Invalid installation manifest: ${path.join(target, MANIFEST)}`); }
  if (!isRecord(metadata) || metadata.managed_by !== MANAGED_BY) throw new InstallError(`Existing pivotui is not managed by this installer: ${target}`);
  if (metadata.entry_sha256 !== digest(files['SKILL.md'])) throw new InstallError(`The installed SKILL.md was edited; preserve your edits before reinstalling: ${path.join(target, 'SKILL.md')}`);
  return files;
}

function sameFiles(left, right) {
  if (left === null || right === null) return left === right;
  return Object.keys(left).length === Object.keys(right).length && Object.entries(left).every(([name, data]) => Buffer.isBuffer(right[name]) && data.equals(right[name]));
}

function removeStaging(staging, parent) {
  const stat = statOrNull(staging);
  if (!stat) return;
  const resolved = fs.realpathSync(staging);
  if (stat.isSymbolicLink() || path.dirname(resolved) !== fs.realpathSync(parent) || !path.basename(staging).startsWith('.pivotui-stage-')) {
    throw new InstallError(`Refusing to clean an unexpected staging path: ${staging}`);
  }
  fs.rmSync(resolved, { recursive: true });
}

function installLibrary(source, destination, hashes, sourceOverrides) {
  if (statOrNull(destination)) {
    if (!sameHashes(inventory(destination), hashes)) throw new InstallError(`Installed library was modified: ${destination}. Choose another --install-dir.`);
    return;
  }
  const parent = path.dirname(destination);
  fs.mkdirSync(parent, { recursive: true });
  const staging = fs.mkdtempSync(path.join(parent, '.pivotui-stage-'));
  try {
    for (const relative of Object.keys(hashes)) {
      const input = sourceOverrides[relative] ?? path.join(source, relative);
      const inputStat = fs.lstatSync(input);
      if (inputStat.isSymbolicLink() || !inputStat.isFile()) throw new InstallError(`Source file changed while copying: ${input}`);
      const output = path.join(staging, relative);
      fs.mkdirSync(path.dirname(output), { recursive: true });
      fs.copyFileSync(input, output);
    }
    if (!sameHashes(inventory(staging), hashes)) throw new InstallError('Source changed while copying; retry with an unmodified package.');
    if (statOrNull(destination)) {
      if (!sameHashes(inventory(destination), hashes)) throw new InstallError(`Another install created conflicting files: ${destination}`);
    } else fs.renameSync(staging, destination);
  } finally { removeStaging(staging, parent); }
}

function writeAtomic(filename, content) {
  const temporary = path.join(path.dirname(filename), `.pivotui-write-${randomUUID()}`);
  try {
    fs.writeFileSync(temporary, content, { flag: 'wx' });
    fs.renameSync(temporary, filename);
  } finally {
    if (statOrNull(temporary)) fs.unlinkSync(temporary);
  }
}

function withEntryLock(skillsDir, action) {
  fs.mkdirSync(skillsDir, { recursive: true });
  const filename = path.join(skillsDir, '.pivotui-install.lock');
  const owner = `${process.pid}:${randomUUID()}\n`;
  try { fs.writeFileSync(filename, owner, { flag: 'wx', mode: 0o600 }); }
  catch (error) {
    if (error.code === 'EEXIST') throw new InstallError(`An install lock already exists: ${filename}. Wait for the other installer; remove a stale lock only after it has stopped.`);
    throw error;
  }
  try { return action(); }
  finally {
    const stat = statOrNull(filename);
    if (stat && !stat.isSymbolicLink() && stat.isFile() && fs.readFileSync(filename, 'utf8') === owner) fs.unlinkSync(filename);
  }
}

function installEntry(target, files, old) {
  if (!sameFiles(checkEntry(target), old)) throw new InstallError('The entry changed during installation; rerun after other edits finish.');
  if (old === null) fs.mkdirSync(target);
  const changed = [];
  try {
    for (const [name, data] of Object.entries(files)) {
      const filename = path.join(target, name);
      if (!statOrNull(filename) || !fs.readFileSync(filename).equals(data)) {
        writeAtomic(filename, data);
        changed.push(name);
      }
    }
  } catch (error) {
    for (const name of changed.reverse()) {
      if (old !== null) writeAtomic(path.join(target, name), old[name]);
      else fs.unlinkSync(path.join(target, name));
    }
    if (old === null && fs.readdirSync(target).length === 0) fs.rmdirSync(target);
    throw error;
  }
}

function usage() {
  console.log(`Install the complete PivotUI library and one native Agent Skill. No Python needed.

Usage: pivotui --agent <codex|claude-code|dsh|cursor|generic> [options]

  --language <en|zh>     Library language (default: en)
  --project <directory> Project to install into (default: current directory)
  --global              Install for this user instead of a project
  --skills-dir <path>   Override the host's skills directory; required for generic
  --install-dir <path>  Override library storage (default: <project>/.pivotui)
  --dry-run             Validate and show destinations without writing
  --help                Show this help

Relative paths are resolved from the current directory. --global cannot be
combined with --project. Global library storage defaults to ~/.pivotui.`);
}

function parseArgs(argv) {
  const options = { language: 'en', global: false, dryRun: false };
  const valueFlags = new Map([['--agent', 'agent'], ['--language', 'language'], ['--project', 'project'], ['--skills-dir', 'skillsDir'], ['--install-dir', 'installDir']]);
  const seen = new Set();
  for (let index = 0; index < argv.length; index++) {
    const flag = argv[index];
    if (flag === '--help' || flag === '-h') return { help: true };
    if (seen.has(flag)) throw new InstallError(`Option supplied more than once: ${flag}`);
    seen.add(flag);
    if (flag === '--global') options.global = true;
    else if (flag === '--dry-run') options.dryRun = true;
    else if (valueFlags.has(flag)) {
      const value = argv[++index];
      if (!value || value.startsWith('--')) throw new InstallError(`Missing value for ${flag}`);
      options[valueFlags.get(flag)] = value;
    } else throw new InstallError(`Unknown option: ${flag}. Use --help.`);
  }
  if (!AGENTS.has(options.agent)) throw new InstallError('--agent is required; choose codex, claude-code, dsh, cursor, or generic.');
  if (!Object.hasOwn(EDITIONS, options.language)) throw new InstallError('--language must be en or zh.');
  if (options.global && options.project !== undefined) throw new InstallError('--global and --project cannot be used together.');
  if (options.agent === 'generic' && options.skillsDir === undefined) throw new InstallError('--agent generic requires --skills-dir pointing to the host\'s skill directory.');
  return options;
}

function main() {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) { usage(); return; }
  const project = canonical(options.project ?? process.cwd());
  const edition = EDITIONS[options.language];
  const { hashes, version, sourceOverrides } = sourceInventory(edition);
  const store = canonical(options.installDir ?? path.join(options.global ? os.homedir() : project, '.pivotui'));
  const libraryParent = canonical(path.join(store, 'libraries'));
  const library = path.join(libraryParent, `${edition}-${pythonFingerprint(hashes)}`);
  const skillsDir = canonical(options.skillsDir ?? defaultSkillsDir(options.agent, project, options.global));
  const target = path.join(skillsDir, 'pivotui');
  const sourceRoots = Object.values(EDITIONS).map(name => fs.realpathSync(path.join(ROOT, name)));
  if (sourceRoots.some(root => within(target, root) || within(library, root)) || within(target, library) || within(library, target)) {
    throw new InstallError('Source editions, installed library, and skill entry must not overlap.');
  }
  const old = checkEntry(target);
  if (statOrNull(library) && !sameHashes(inventory(library), hashes)) throw new InstallError(`Installed library was modified: ${library}. Choose another --install-dir.`);
  const relative = path.relative(target, library);
  if (!options.global && path.isAbsolute(relative)) throw new InstallError('Project entry and library must be on the same drive so relative resource paths remain portable.');
  const reference = posix(relative);
  const template = fs.readFileSync(path.join(ROOT, 'scripts', 'install-resources', edition, 'entry.txt'), 'utf8');
  const entry = Buffer.from(template.replaceAll('{{EDITION_ROOT}}', reference), 'utf8');
  const metadata = {
    managed_by: MANAGED_BY,
    edition,
    cluster_version: version,
    scope: options.global ? 'global' : 'project',
    library: reference,
    entry_sha256: digest(entry),
  };
  const files = { 'SKILL.md': entry, [MANIFEST]: Buffer.from(`${JSON.stringify(metadata, null, 2)}\n`, 'utf8') };
  console.log(`Library: ${library}\nAgent Skill: ${path.join(target, 'SKILL.md')}`);
  if (options.dryRun) { console.log(`Dry run: ${Object.keys(hashes).length} edition files verified; no files written.`); return; }
  withEntryLock(skillsDir, () => {
    if (!sameFiles(checkEntry(target), old)) throw new InstallError('The entry changed while waiting to install; rerun after other edits finish.');
    installLibrary(path.join(ROOT, edition), library, hashes, sourceOverrides);
    installEntry(target, files, old);
    if (!sameHashes(inventory(library), hashes) || !sameFiles(checkEntry(target), files)) throw new InstallError('Post-install verification failed.');
  });
  console.log(`Installed PivotUI ${version} (${edition}): ${Object.keys(hashes).length} files verified.`);
  console.log('Start a new Agent session and select the pivotui skill. No MCP setup is required.');
}

try { main(); }
catch (error) { console.error(`Installation failed: ${error.message}`); process.exitCode = 1; }
