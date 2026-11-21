"""Validate paired editions and build immutable, reproducible release archives.

Use --record-sync only after reviewing both languages. It records a new paired
baseline without building archives. Ordinary runs require that exact baseline.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath, PureWindowsPath
from urllib.parse import unquote, urlsplit

import yaml


VERSION = "0.5.0"
EDITIONS = ("English", "Chinese")
EXCLUDED_DIRECTORIES = {".venv", "__pycache__"}
HAN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
FIXED_ZIP_DATE = (2026, 11, 14, 0, 0, 0)


class ReleaseError(Exception):
    """An actionable release validation failure."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def inventory(folder: Path) -> dict[str, bytes]:
    if not folder.is_dir():
        raise ReleaseError(f"Missing edition directory: {folder.name}")
    result = {}
    for directory, directories, files in os.walk(folder, followlinks=False):
        directories[:] = sorted(set(directories) - EXCLUDED_DIRECTORIES)
        for name in directories + files:
            path = Path(directory) / name
            if path.is_symlink():
                raise ReleaseError(f"Replace symbolic links with portable files: {path.relative_to(folder)}")
        for name in sorted(files):
            path = Path(directory) / name
            if path.suffix in {".pyc", ".pyo"}:
                continue
            result[path.relative_to(folder).as_posix()] = path.read_bytes()
    if not result:
        raise ReleaseError(f"Empty edition directory: {folder.name}")
    return dict(sorted(result.items()))


def without_fences(text: str) -> str:
    """Remove fenced code examples before checking Markdown resource links."""
    output = []
    marker = ""
    length = 0
    for line in text.splitlines():
        fence = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            if fence and fence.group(1)[0] == marker and len(fence.group(1)) >= length:
                marker = ""
            continue
        if fence:
            marker, length = fence.group(1)[0], len(fence.group(1))
        else:
            output.append(line)
    return "\n".join(output)


def markdown_targets(text: str) -> list[str]:
    text = without_fences(text)
    targets = re.findall(r"\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)(?:\s+[^)]+)?\)", text)
    targets += re.findall(r"^\s*\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", text, flags=re.MULTILINE)
    return [target[1:-1] if target.startswith("<") else target for target in targets]


def check_link(edition_root: Path, relative: str, target: str) -> None:
    if target.startswith(("#", "//")):
        return
    if re.match(r"^(?:https?|mailto|tel):", target, flags=re.IGNORECASE):
        return
    target_path = unquote(urlsplit(target).path).replace("\\", "/")
    if not target_path:
        return
    windows_path = PureWindowsPath(target_path)
    if PurePosixPath(target_path).is_absolute() or windows_path.drive or urlsplit(target).scheme:
        raise ReleaseError(f"{edition_root.name}/{relative}: nonportable link {target!r}")
    resolved = (edition_root / relative).parent.joinpath(target_path).resolve()
    if not resolved.is_relative_to(edition_root.resolve()):
        raise ReleaseError(f"{edition_root.name}/{relative}: link leaves the edition: {target!r}")
    if not resolved.exists():
        raise ReleaseError(f"{edition_root.name}/{relative}: missing linked resource {target!r}")


def frontmatter(data: bytes, label: str) -> dict:
    text = data.decode("utf-8-sig")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ReleaseError(f"{label}: missing YAML frontmatter")
    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
        value = yaml.safe_load("\n".join(lines[1:end]))
    except (StopIteration, yaml.YAMLError) as error:
        raise ReleaseError(f"{label}: invalid YAML frontmatter") from error
    if not isinstance(value, dict):
        raise ReleaseError(f"{label}: frontmatter must be a mapping")
    name, description = value.get("name"), value.get("description")
    if not isinstance(name, str) or len(name) > 64 or not NAME.fullmatch(name):
        raise ReleaseError(f"{label}: invalid skill name")
    if not isinstance(description, str) or not description.strip():
        raise ReleaseError(f"{label}: missing skill description")
    if value.get("metadata") is not None and not isinstance(value["metadata"], dict):
        raise ReleaseError(f"{label}: metadata must be a mapping")
    return value


def readme_origins(files: dict[str, bytes], edition: str) -> dict[str, str]:
    """Read provenance from the user-facing README table, not directory names."""
    if "README.md" not in files:
        raise ReleaseError(f"{edition}: missing README.md source table")
    origins = {}
    labels = {"internal": "internal", "external": "external", "内源": "internal", "外源": "external"}
    for line in without_fences(files["README.md"].decode("utf-8-sig")).splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        skill = re.fullmatch(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`", cells[0])
        origin = labels.get(cells[1].casefold())
        if not skill or origin is None:
            continue
        name = skill.group(1)
        if name in origins and origins[name] != origin:
            raise ReleaseError(f"{edition}/README.md: conflicting origins for {name}")
        origins[name] = origin
    if not origins:
        raise ReleaseError(f"{edition}/README.md: no skill origin rows found")
    return origins


def package_origins(files: dict[str, bytes], origins: dict[str, str], edition: str) -> dict[str, str]:
    """Classify flat or function-grouped packages by declared identities."""
    packages = {}
    names = set()
    for relative, data in files.items():
        path = PurePosixPath(relative)
        if len(path.parts) not in {2, 3} or path.name != "SKILL.md":
            continue
        if any((parent / "SKILL.md").as_posix() in files for parent in path.parent.parents if parent != PurePosixPath(".")):
            continue
        name = frontmatter(data, f"{edition}/{relative}")["name"]
        if name not in origins:
            raise ReleaseError(f"{edition}/{relative}: declare {name} and its origin in README.md")
        if name in names:
            raise ReleaseError(f"{edition}: duplicate top-level skill identity {name}")
        names.add(name)
        packages[path.parent.as_posix()] = origins[name]
    return packages


def owning_package(relative: str, packages: dict[str, str]) -> str | None:
    matches = [package for package in packages if relative.startswith(package + "/")]
    return max(matches, key=len) if matches else None


def check_structure(root: Path, editions: dict[str, dict[str, bytes]]) -> None:
    english, chinese = (editions[name] for name in EDITIONS)
    if english.keys() != chinese.keys():
        missing_english = sorted(chinese.keys() - english.keys())
        missing_chinese = sorted(english.keys() - chinese.keys())
        raise ReleaseError(
            "Edition file inventories differ. "
            f"Missing in English: {missing_english}; missing in Chinese: {missing_chinese}"
        )
    origins = {edition: readme_origins(editions[edition], edition) for edition in EDITIONS}
    if origins["English"] != origins["Chinese"]:
        raise ReleaseError("The English and Chinese README skill origin tables differ")
    packages = {
        edition: package_origins(editions[edition], origins[edition], edition)
        for edition in EDITIONS
    }
    if packages["English"] != packages["Chinese"]:
        raise ReleaseError("Package origins differ between editions")
    manifests = {}
    for edition in EDITIONS:
        for relative, data in editions[edition].items():
            label = f"{edition}/{relative}"
            path = PurePosixPath(relative)
            try:
                text = data.decode("utf-8-sig")
            except UnicodeDecodeError:
                if path.suffix in {".md", ".yaml", ".yml", ".json", ".toml", ".txt", ".py"}:
                    raise ReleaseError(f"{label}: expected UTF-8 text")
                continue
            normalized = re.sub(r"\\+", "/", text).casefold()
            if packages[edition].get(owning_package(relative, packages[edition])) != "external" and re.search(r"(?:^|[\s(\"'`])(?:[a-z]:/users/|/users/|/home/)(?!your-|example|user(?:/|\b))[^/\s\"'`]+/", normalized):
                raise ReleaseError(f"{label}: contains a personal build-machine path")
            owner = owning_package(relative, packages[edition])
            upstream = packages[edition].get(owner) == "external"
            if edition == "English" and not upstream and path.suffix != ".py" and HAN.search(text):
                raise ReleaseError(f"{label}: untranslated Han characters in authored English content")
            if path.suffix == ".md":
                for target in markdown_targets(text):
                    check_link(root / edition, relative, target)
            if path.name == "SKILL.md":
                if owner is None:
                    raise ReleaseError(f"{label}: skill entry must belong to a declared package")
                value = frontmatter(data, label)
                manifests[(edition, relative)] = value
                if not upstream and value["name"] != path.parent.name:
                    raise ReleaseError(f"{label}: skill name must match its directory")
            elif path.suffix in {".yaml", ".yml"}:
                try:
                    yaml.safe_load(text)
                except yaml.YAMLError as error:
                    raise ReleaseError(f"{label}: invalid YAML") from error
    for relative in english:
        if packages["English"].get(owning_package(relative, packages["English"])) == "external":
            if english[relative] != chinese[relative]:
                raise ReleaseError(f"{relative}: upstream originals must be identical in both editions")
        if PurePosixPath(relative).name != "SKILL.md":
            continue
        left, right = (manifests[(edition, relative)] for edition in EDITIONS)
        left_identity = (left["name"], left.get("version"), (left.get("metadata") or {}).get("version"))
        right_identity = (right["name"], right.get("version"), (right.get("metadata") or {}).get("version"))
        if left_identity != right_identity:
            raise ReleaseError(f"{relative}: skill name or version differs between languages")
    if not manifests:
        raise ReleaseError("The editions contain no SKILL.md entrypoints")


def sync_manifest(editions: dict[str, dict[str, bytes]]) -> dict:
    return {
        "schema_version": 1,
        "cluster_version": VERSION,
        "source_language": "English",
        "files": {
            relative: {edition: digest(editions[edition][relative]) for edition in EDITIONS}
            for relative in editions["English"]
        },
    }


def check_baseline(path: Path, expected: dict) -> None:
    if not path.is_file():
        raise ReleaseError("Missing language-sync.json. Review both editions, then run --record-sync.")
    try:
        actual = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ReleaseError("language-sync.json is not valid UTF-8 JSON") from error
    if actual == expected:
        return
    old_files = actual.get("files", {}) if isinstance(actual, dict) else {}
    if not isinstance(old_files, dict):
        old_files = {}
    changed = [name for name in sorted(set(old_files) | set(expected["files"])) if old_files.get(name) != expected["files"].get(name)]
    details = ", ".join(changed) if changed else "manifest metadata"
    raise ReleaseError(f"Language-sync baseline drift: {details}. Review both languages before --record-sync.")


def archive_bytes(edition: str, files: dict[str, bytes]) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative, data in files.items():
            info = zipfile.ZipInfo(f"{edition}/{relative}", date_time=FIXED_ZIP_DATE)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data, compresslevel=9)
    return output.getvalue()


def verify_archive(data: bytes, edition: str, files: dict[str, bytes]) -> None:
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        expected = [f"{edition}/{relative}" for relative in files]
        if archive.namelist() != expected:
            raise ReleaseError(f"{edition}: archive file inventory does not match source")
        if archive.testzip() is not None:
            raise ReleaseError(f"{edition}: archive integrity check failed")
        for relative, source in files.items():
            if archive.read(f"{edition}/{relative}") != source:
                raise ReleaseError(f"{edition}/{relative}: archive bytes differ from source")


def unchanged_sources(root: Path, editions: dict[str, dict[str, bytes]]) -> None:
    for edition in EDITIONS:
        if inventory(root / edition) != editions[edition]:
            raise ReleaseError(f"{edition} changed during validation; rerun after edits finish")


def write_release(root: Path, editions: dict[str, dict[str, bytes]]) -> list[Path]:
    pending = {}
    for edition in EDITIONS:
        data = archive_bytes(edition, editions[edition])
        verify_archive(data, edition, editions[edition])
        destination = root / "dist" / f"PivotUI-{edition}-v{VERSION}.zip"
        pending[destination] = data
    checksum_path = root / "dist" / f"CHECKSUMS-v{VERSION}.sha256"
    pending[checksum_path] = "".join(f"{digest(data)}  {path.name}\n" for path, data in pending.items()).encode("utf-8")
    # Preflight every output so one immutable-file conflict cannot leave a partial release.
    for path, data in pending.items():
        if path.exists() and path.read_bytes() != data:
            raise ReleaseError(f"Refusing to overwrite a different published version: {path.name}. Use a new release version.")
    unchanged_sources(root, editions)
    (root / "dist").mkdir(exist_ok=True)
    for path, data in pending.items():
        if not path.exists():
            with path.open("xb") as handle:
                handle.write(data)
    for edition in EDITIONS:
        path = root / "dist" / f"PivotUI-{edition}-v{VERSION}.zip"
        verify_archive(path.read_bytes(), edition, editions[edition])
    return list(pending)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Cluster repository root")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--record-sync", action="store_true", help="Record a reviewed bilingual baseline; do not build")
    mode.add_argument("--check-only", action="store_true", help="Validate structure and existing baseline; do not build")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        editions = {edition: inventory(root / edition) for edition in EDITIONS}
        check_structure(root, editions)
        expected = sync_manifest(editions)
        baseline = root / "language-sync.json"
        if args.record_sync:
            unchanged_sources(root, editions)
            baseline.write_text(json.dumps(expected, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"Recorded reviewed language baseline: {len(expected['files'])} paired files.")
            return 0
        check_baseline(baseline, expected)
        unchanged_sources(root, editions)
        if args.check_only:
            print(f"Validated {len(expected['files'])} paired files against the reviewed language baseline.")
            return 0
        for path in write_release(root, editions):
            print(f"Verified release output: {path.name}")
        return 0
    except (ReleaseError, OSError, UnicodeDecodeError) as error:
        print(f"Release validation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
