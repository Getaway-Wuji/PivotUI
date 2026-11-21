#!/usr/bin/env node
/**
 * Thin zero-dependency PivotUI CLI bootstrap (< 10 KB).
 *
 * Downloads ONLY the requested single-language PivotUI release tarball from
 * GitHub Releases, verifies its SHA-256 digest against NPX-CHECKSUMS, extracts
 * it into a temporary cache, and runs the bundled verified bin/pivotui.mjs.
 *
 * When published to npm as @getaway-wuji/pivotui, users simply run:
 *   npx @getaway-wuji/pivotui --agent codex --language zh
 */

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import readline from 'node:readline/promises';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';

const DEFAULT_REPO = process.env.PIVOTUI_REPO || 'Getaway-Wuji/PivotUI';
const DEFAULT_VERSION = '0.5.0';
const VALID_AGENTS = ['codex', 'claude-code', 'dsh', 'cursor', 'antigravity', 'gemini', 'windsurf', 'opencode', 'generic'];

export function buildReleaseUrls(version, language, repo = DEFAULT_REPO) {
  const tag = version.startsWith('v') ? version : `v${version}`;
  const cleanVer = tag.slice(1);
  const langSuffix = language === 'zh' ? 'zh' : 'en';
  const base = `https://github.com/${repo}/releases/download/${tag}`;
  const assetName = `pivotui-installer-${langSuffix}-v${cleanVer}.tgz`;
  const checksumName = `NPX-CHECKSUMS-v${cleanVer}.sha256`;
  return {
    tag,
    assetName,
    checksumName,
    assetUrl: `${base}/${assetName}`,
    checksumUrl: `${base}/${checksumName}`,
  };
}

export function parseChecksumFile(text, assetName) {
  for (const line of text.splitlines ? text.splitlines() : text.split(/\r?\n/)) {
    const match = line.trim().match(/^([a-f0-9]{64})\s+\*?(.+)$/i);
    if (match && match[2].trim() === assetName) {
      return match[1].toLowerCase();
    }
  }
  return null;
}

export function sha256Buffer(buf) {
  return createHash('sha256').update(buf).digest('hex');
}

function parseFlags(argv) {
  const result = { version: DEFAULT_VERSION, language: null, agent: null, passthrough: [], help: false, printUrls: false };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--help' || arg === '-h') {
      result.help = true;
      return result;
    }
    if (arg === '--version-tag') {
      result.version = argv[++i] || DEFAULT_VERSION;
      continue;
    }
    if (arg === '--print-urls') {
      result.printUrls = true;
      continue;
    }
    if (arg === '--language') {
      result.language = argv[++i] || null;
      result.passthrough.push(arg, result.language || '');
      continue;
    }
    if (arg === '--agent') {
      result.agent = argv[++i] || null;
      result.passthrough.push(arg, result.agent || '');
      continue;
    }
    result.passthrough.push(arg);
  }
  return result;
}

async function promptMissing(parsed) {
  if (!process.stdin.isTTY) {
    if (!parsed.language) {
      parsed.language = 'en';
      parsed.passthrough.push('--language', 'en');
    }
    return parsed;
  }
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  try {
    if (!parsed.agent) {
      const answer = (await rl.question(`Select Agent (${VALID_AGENTS.join('/')} ) [codex]: `)).trim() || 'codex';
      parsed.agent = answer;
      parsed.passthrough.push('--agent', answer);
    }
    if (!parsed.language) {
      const answer = (await rl.question('Select edition language (zh/en) [zh]: ')).trim() || 'zh';
      parsed.language = answer;
      parsed.passthrough.push('--language', answer);
    }
  } finally {
    rl.close();
  }
  return parsed;
}

async function downloadBuffer(url) {
  const res = await fetch(url, { redirect: 'follow', headers: { 'User-Agent': 'pivotui-cli' } });
  if (!res.ok) throw new Error(`HTTP ${res.status} fetching ${url}`);
  return Buffer.from(await res.arrayBuffer());
}

async function main() {
  const parsed = parseFlags(process.argv.slice(2));
  if (parsed.help) {
    console.log(`PivotUI lightweight CLI launcher (v${DEFAULT_VERSION})

Usage:
  npx @getaway-wuji/pivotui --agent <codex|claude-code|dsh|cursor|antigravity|gemini|windsurf|opencode|generic> --language <zh|en> [options]

Extra launcher options:
  --version-tag <ver>  Release version to install (default: ${DEFAULT_VERSION})
  --print-urls         Print resolved single-language release URLs without downloading

All other options (--global, --project, --skills-dir, --install-dir, --status, --prune, --uninstall, --dry-run) are forwarded to PivotUI's verified installer.`);
    return;
  }

  if (parsed.printUrls) {
    const urls = buildReleaseUrls(parsed.version, parsed.language || 'en');
    console.log(JSON.stringify(urls, null, 2));
    return;
  }

  await promptMissing(parsed);
  if (!parsed.agent) {
    throw new Error(`--agent is required in non-interactive mode (${VALID_AGENTS.join(', ')}).`);
  }
  if (!['en', 'zh'].includes(parsed.language)) {
    throw new Error('--language must be en or zh.');
  }

  const urls = buildReleaseUrls(parsed.version, parsed.language);
  const cacheDir = path.join(os.tmpdir(), 'pivotui-cli-cache', urls.tag);
  fs.mkdirSync(cacheDir, { recursive: true });
  const tarballPath = path.join(cacheDir, urls.assetName);

  console.log(`Fetching checksums: ${urls.checksumUrl}`);
  const checksumText = (await downloadBuffer(urls.checksumUrl)).toString('utf8');
  const expectedSha = parseChecksumFile(checksumText, urls.assetName);
  if (!expectedSha) {
    throw new Error(`Checksum entry not found for ${urls.assetName} in ${urls.checksumName}`);
  }

  let needDownload = true;
  if (fs.existsSync(tarballPath)) {
    if (sha256Buffer(fs.readFileSync(tarballPath)) === expectedSha) {
      needDownload = false;
      console.log(`Using verified cached tarball: ${tarballPath}`);
    }
  }
  if (needDownload) {
    console.log(`Downloading ${urls.assetName} (single-language complete cluster)...`);
    const data = await downloadBuffer(urls.assetUrl);
    const actualSha = sha256Buffer(data);
    if (actualSha !== expectedSha) {
      throw new Error(`SHA-256 mismatch for ${urls.assetName}: expected ${expectedSha}, got ${actualSha}`);
    }
    fs.writeFileSync(tarballPath, data);
    console.log(`SHA-256 verified: ${actualSha.slice(0, 16)}...`);
  }

  const npxCmd = process.platform === 'win32' ? 'npx.cmd' : 'npx';
  const child = spawnSync(
    npxCmd,
    ['--yes', '--offline', `--package=${tarballPath}`, 'pivotui', ...parsed.passthrough],
    { stdio: 'inherit' },
  );
  if (child.error) throw child.error;
  process.exitCode = child.status ?? 1;
}

if (import.meta.url === `file://${process.argv[1].replace(/\\/g, '/')}` || process.argv[1]?.endsWith('pivotui-cli.mjs')) {
  main().catch((err) => {
    console.error(`PivotUI CLI error: ${err.message}`);
    process.exitCode = 1;
  });
}
