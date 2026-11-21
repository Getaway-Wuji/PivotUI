"""Install or manage a complete PivotUI edition and a discoverable local Agent Skill.

Requires Python 3.11+ and a complete repository checkout. Uses only the standard
library; never edits project instructions, MCP settings, or other skills.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
MANAGED_BY = "pivotui-installer-v1"
MANIFEST = ".pivotui-install.json"
EXCLUDED = {".git", ".venv", "__pycache__", "node_modules"}
EDITIONS = {"en": "English", "zh": "Chinese"}
AGENTS = ("codex", "claude-code", "dsh", "cursor", "antigravity", "gemini", "windsurf", "opencode", "generic")
MANAGED_LIB_NAME = re.compile(r"^(English|Chinese)-[a-f0-9]{16}$")


class InstallError(Exception):
    """An installation cannot proceed without risking existing files."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def inventory(root: Path) -> dict[str, str]:
    if root.is_symlink() or not root.is_dir():
        raise InstallError(f"Expected a real edition directory: {root}")
    files = {}
    for directory, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = sorted(set(dirs) - EXCLUDED)
        for name in dirs + names:
            path = Path(directory) / name
            if path.is_symlink():
                raise InstallError(f"Symbolic links are not copied: {path}")
        for name in sorted(names):
            path = Path(directory) / name
            if path.suffix in {".pyc", ".pyo"}:
                continue
            files[path.relative_to(root).as_posix()] = digest(path.read_bytes())
    return dict(sorted(files.items()))


def source_inventory(edition: str) -> tuple[dict[str, str], str]:
    baseline = json.loads((ROOT / "language-sync.json").read_text(encoding="utf-8"))
    if not isinstance(baseline, dict) or not isinstance(baseline.get("files"), dict) or not isinstance(baseline.get("cluster_version"), str):
        raise InstallError("Invalid release baseline; use a complete, unmodified checkout.")
    expected = {}
    for name, pair in baseline["files"].items():
        if not isinstance(name, str) or not isinstance(pair, dict) or not isinstance(pair.get(edition), str):
            raise InstallError("Invalid file hashes in the release baseline.")
        expected[name] = pair[edition]
    actual = inventory(ROOT / edition)
    if actual != expected:
        raise InstallError("The edition differs from its release baseline. Use a complete, unmodified checkout.")
    return actual, baseline["cluster_version"]


def default_skills_dir(agent: str, project: Path | None = None) -> Path:
    if agent == "generic":
        raise InstallError("--agent generic requires --skills-dir pointing to the host's skill directory.")
    if project is not None:
        if agent == "claude-code":
            return project / ".claude" / "skills"
        if agent == "antigravity":
            return project / ".agent" / "skills"
        if agent == "gemini":
            return project / ".gemini" / "skills"
        if agent == "windsurf":
            return project / ".windsurf" / "skills"
        if agent == "opencode":
            return project / ".opencode" / "skills"
        return project / ".agents" / "skills"
    home = Path.home()
    if agent == "codex":
        return Path(os.environ.get("CODEX_HOME") or home / ".codex") / "skills"
    if agent == "claude-code":
        return Path(os.environ.get("CLAUDE_CONFIG_DIR") or home / ".claude") / "skills"
    if agent == "dsh":
        return Path(os.environ.get("DSH_AGENTS_HOME") or home / ".agents") / "skills"
    if agent == "antigravity":
        return home / ".gemini" / "antigravity" / "skills"
    if agent == "gemini":
        return home / ".gemini" / "skills"
    if agent == "windsurf":
        return home / ".codeium" / "windsurf" / "skills"
    if agent == "opencode":
        return home / ".config" / "opencode" / "skills"
    return home / ".agents" / "skills"


def check_entry(target: Path) -> dict[str, bytes] | None:
    if target.is_symlink():
        raise InstallError(f"Refusing to replace a linked skill directory: {target}")
    if not target.exists():
        return None
    if not target.is_dir():
        raise InstallError(f"The skill destination is not a directory: {target}")
    marker = target / MANIFEST
    entry = target / "SKILL.md"
    if marker.is_symlink() or entry.is_symlink() or not marker.is_file() or not entry.is_file():
        raise InstallError(f"Existing pivotui is not managed by this installer: {target}")
    old = {"SKILL.md": entry.read_bytes(), MANIFEST: marker.read_bytes()}
    try:
        metadata = json.loads(old[MANIFEST])
    except (ValueError, UnicodeDecodeError) as error:
        raise InstallError(f"Invalid installation manifest: {marker}") from error
    if not isinstance(metadata, dict) or metadata.get("managed_by") != MANAGED_BY:
        raise InstallError(f"Existing pivotui is not managed by this installer: {target}")
    if metadata.get("entry_sha256") != digest(old["SKILL.md"]):
        raise InstallError(f"The installed SKILL.md was edited; preserve your edits before reinstalling: {entry}")
    return old


def remove_staging(path: Path, parent: Path) -> None:
    resolved = path.resolve()
    if path.is_symlink() or resolved.parent != parent.resolve() or not path.name.startswith(".pivotui-stage-"):
        raise InstallError(f"Refusing to clean an unexpected staging path: {path}")
    shutil.rmtree(resolved)


def prune_unused_libraries(library_parent: Path, keep_library: Path | None) -> list[str]:
    if library_parent.is_symlink() or not library_parent.is_dir():
        return []
    real_parent = library_parent.resolve()
    keep_real = keep_library.resolve() if keep_library and keep_library.exists() else None
    removed: list[str] = []
    for item in sorted(real_parent.iterdir()):
        if item.is_symlink() or not item.is_dir():
            continue
        if not MANAGED_LIB_NAME.match(item.name):
            continue
        resolved = item.resolve()
        if resolved.parent != real_parent:
            continue
        if keep_real is not None and resolved == keep_real:
            continue
        shutil.rmtree(resolved)
        removed.append(item.name)
    return removed


def install_library(source: Path, destination: Path, expected: dict[str, str]) -> None:
    if destination.exists():
        if inventory(destination) != expected:
            raise InstallError(f"Installed library was modified: {destination}. Choose another --install-dir.")
        return
    parent = destination.parent
    parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".pivotui-stage-", dir=parent))
    try:
        for relative in expected:
            output = staging / relative
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / relative, output)
        if inventory(staging) != expected:
            raise InstallError("Source changed while copying; rerun from an unmodified checkout.")
        if destination.exists():
            if inventory(destination) != expected:
                raise InstallError(f"Another install created conflicting files: {destination}")
        else:
            staging.rename(destination)
    finally:
        if staging.exists():
            remove_staging(staging, parent)


def write_atomic(path: Path, content: bytes) -> None:
    fd, temp_name = tempfile.mkstemp(prefix=".pivotui-write-", dir=path.parent)
    temporary = Path(temp_name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


@contextmanager
def entry_lock(skills_dir: Path):
    skills_dir.mkdir(parents=True, exist_ok=True)
    path = skills_dir / ".pivotui-install.lock"
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as error:
        raise InstallError(f"An install lock already exists: {path}. Wait for the other installer; remove a stale lock only after it has stopped.") from error
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(f"{os.getpid()}\n")
        yield
    finally:
        path.unlink()


def install_entry(target: Path, files: dict[str, bytes], old: dict[str, bytes] | None) -> None:
    if check_entry(target) != old:
        raise InstallError("The entry changed during installation; rerun after other edits finish.")
    target.mkdir(parents=True, exist_ok=True)
    try:
        for name, data in files.items():
            if not (target / name).exists() or (target / name).read_bytes() != data:
                write_atomic(target / name, data)
    except OSError:
        for name in files:
            if old is not None:
                write_atomic(target / name, old[name])
            elif (target / name).exists():
                (target / name).unlink()
        raise


def uninstall_entry(target: Path, old: dict[str, bytes]) -> None:
    if check_entry(target) != old:
        raise InstallError("The entry changed before uninstall; rerun after other edits finish.")
    for name in ("SKILL.md", MANIFEST):
        file_path = target / name
        if file_path.exists():
            file_path.unlink()
    if target.exists() and not any(target.iterdir()):
        target.rmdir()


def show_status(target: Path, library_parent: Path) -> None:
    existing = check_entry(target)
    if existing is None:
        print(f"Status: not installed at {target}")
        return
    metadata = json.loads(existing[MANIFEST].decode("utf-8"))
    raw_lib = Path(metadata["library"])
    resolved_lib = raw_lib if raw_lib.is_absolute() else (target / raw_lib).resolve()
    print("Status: installed")
    print(f"Version: {metadata.get('cluster_version', 'unknown')}")
    print(f"Edition: {metadata.get('edition', 'unknown')}")
    print(f"Agent Skill: {target / 'SKILL.md'}")
    print(f"Library: {resolved_lib} ({'present' if resolved_lib.is_dir() else 'MISSING'})")
    if library_parent.is_dir():
        libs = sorted(p.name for p in library_parent.iterdir() if p.is_dir() and MANAGED_LIB_NAME.match(p.name))
        if len(libs) > 1:
            print(f"Stored libraries ({len(libs)}): {', '.join(libs)} (use --prune to remove unused older versions)")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", required=True, choices=AGENTS)
    parser.add_argument("--language", choices=EDITIONS, default="en", help="Edition to install (default: en)")
    parser.add_argument("--project", type=Path, help="Install into a project directory instead of user home")
    parser.add_argument("--skills-dir", type=Path, help="Override the host's skills directory; required for generic")
    parser.add_argument("--install-dir", type=Path, help="Override full library storage (default: ~/.pivotui or <project>/.pivotui)")
    parser.add_argument("--prune", action="store_true", help="Remove unused older managed libraries after install or uninstall")
    parser.add_argument("--status", action="store_true", help="Inspect current installation without writing files")
    parser.add_argument("--uninstall", action="store_true", help="Safely remove the managed pivotui skill entry")
    parser.add_argument("--dry-run", action="store_true", help="Validate and show destinations without writing")
    args = parser.parse_args(argv)
    try:
        if args.status and args.uninstall:
            raise InstallError("--status and --uninstall cannot be used together.")
        project = args.project.expanduser().resolve() if args.project is not None else None
        store = (args.install_dir if args.install_dir is not None else ((project or Path.home()) / ".pivotui")).expanduser().resolve()
        library_parent = store / "libraries"
        skills_dir = (args.skills_dir if args.skills_dir is not None else default_skills_dir(args.agent, project)).expanduser().resolve()
        target = skills_dir / "pivotui"

        if args.status:
            show_status(target, library_parent)
            return 0

        if args.uninstall:
            old = check_entry(target)
            if old is None:
                print(f"Nothing to uninstall: {target} does not exist.")
                return 0
            if args.dry_run:
                print(f"Dry run: would remove managed entry at {target}{' and prune libraries' if args.prune else ''}.")
                return 0
            with entry_lock(skills_dir):
                uninstall_entry(target, old)
                if args.prune:
                    removed = prune_unused_libraries(library_parent, None)
                    if removed:
                        print(f"Pruned libraries: {', '.join(removed)}")
            print(f"Uninstalled PivotUI entry from {target}.")
            return 0

        edition = EDITIONS[args.language]
        hashes, version = source_inventory(edition)
        fingerprint = digest(json.dumps(hashes, sort_keys=True).encode("utf-8"))[:16]
        library = library_parent / f"{edition}-{fingerprint}"
        source = ROOT / edition
        source_roots = [(ROOT / name).resolve() for name in EDITIONS.values()]
        if any(target.is_relative_to(root) or library.is_relative_to(root) for root in source_roots) or library.is_relative_to(target) or target.is_relative_to(library):
            raise InstallError("Source edition, installed library, and skill entry must not overlap.")
        old = check_entry(target)
        if library.exists() and inventory(library) != hashes:
            raise InstallError(f"Installed library was modified: {library}. Choose another --install-dir.")
        reference = os.path.relpath(library, target).replace("\\", "/") if project is not None else library.as_posix()
        template = (ROOT / "scripts" / "install-resources" / edition / "entry.txt").read_text(encoding="utf-8")
        entry = template.replace("{{EDITION_ROOT}}", reference).encode("utf-8")
        metadata = {
            "managed_by": MANAGED_BY,
            "edition": edition,
            "cluster_version": version,
            "scope": "project" if project is not None else "global",
            "library": reference,
            "entry_sha256": digest(entry),
        }
        files = {"SKILL.md": entry, MANIFEST: (json.dumps(metadata, indent=2, ensure_ascii=False) + "\n").encode("utf-8")}
        print(f"Library: {library}")
        print(f"Agent Skill: {target / 'SKILL.md'}")
        if args.dry_run:
            print(f"Dry run: {len(hashes)} edition files verified; no files written.")
            return 0
        with entry_lock(skills_dir):
            if check_entry(target) != old:
                raise InstallError("The entry changed while waiting to install; rerun after other edits finish.")
            install_library(source, library, hashes)
            install_entry(target, files, old)
            if inventory(library) != hashes or check_entry(target) != files:
                raise InstallError("Post-install verification failed.")
            if args.prune:
                removed = prune_unused_libraries(library_parent, library)
                if removed:
                    print(f"Pruned older libraries: {', '.join(removed)}")
        print(f"Installed PivotUI {version} ({edition}): {len(hashes)} files verified.")
        print("Start a new Agent session and select the pivotui skill. No MCP setup is required.")
        return 0
    except (InstallError, OSError, ValueError, KeyError) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
