"""Build verified single-language and deduplicated bilingual npm installer tarballs.

Produces three complete-cluster tarballs (keeping all 23 packages / 27 entries):
- pivotui-installer-zh-v<VER>.tgz  : Chinese-only (~29 MB; zero English files)
- pivotui-installer-en-v<VER>.tgz  : English-only (~29 MB; zero Chinese files)
- pivotui-installer-v<VER>.tgz     : Deduplicated bilingual (~29 MB; shared external
                                     and identical files stored once instead of twice)

Maintainer tool: requires Node.js/npm and release.py dependencies (PyYAML).
"""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile

import release


ROOT = Path(__file__).resolve().parents[1]
NPM = shutil.which("npm.cmd") or shutil.which("npm")
NPM_PRESERVED_FILE = "mcp/skill-cluster/.gitignore"


def _copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def _stage_common(staging: Path, editions: list[str], extra_files: list[str]) -> None:
    for rel in ("LICENSE", "THIRD_PARTY_NOTICES.md", "language-sync.json"):
        _copy_file(ROOT / rel, staging / rel)
    shutil.copytree(ROOT / "bin", staging / "bin")
    for edition in editions:
        shutil.copytree(ROOT / "scripts" / "install-resources" / edition, staging / "scripts" / "install-resources" / edition)
    pkg = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    pkg["version"] = release.VERSION
    pkg["files"] = [
        "bin/",
        *[f"{ed}/" for ed in editions],
        "language-sync.json",
        "scripts/install-resources/",
        *extra_files,
    ]
    (staging / "package.json").write_text(json.dumps(pkg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _pack_variant(variant: str, editions_data: dict[str, dict[str, bytes]], baseline: dict) -> bytes:
    if not NPM:
        raise release.ReleaseError("npm is required to build installer tarballs.")
    temp_parent = Path(tempfile.gettempdir()).resolve()
    staging = Path(tempfile.mkdtemp(prefix=f"pivotui-npm-{variant}-", dir=temp_parent)).resolve()
    pack_out = Path(tempfile.mkdtemp(prefix=f"pivotui-pack-{variant}-", dir=temp_parent)).resolve()
    try:
        if variant == "en":
            _stage_common(staging, ["English"], [])
            for rel, data in editions_data["English"].items():
                dst = staging / "English" / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(data)
        elif variant == "zh":
            _stage_common(staging, ["Chinese"], [])
            for rel, data in editions_data["Chinese"].items():
                dst = staging / "Chinese" / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(data)
        elif variant == "universal":
            _stage_common(staging, ["English", "Chinese"], [])
            for rel, data in editions_data["English"].items():
                dst = staging / "English" / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(data)
            files_map = baseline["files"]
            zh_unique = 0
            zh_deduped = 0
            for rel, data in editions_data["Chinese"].items():
                if files_map[rel]["Chinese"] == files_map[rel]["English"]:
                    zh_deduped += 1
                    continue
                zh_unique += 1
                dst = staging / "Chinese" / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(data)
            dedup_meta = {
                "deduplicated_edition": "Chinese",
                "shared_source": "English",
                "deduplicated_files": zh_deduped,
                "unique_files": zh_unique,
            }
            (staging / "bin" / "npm-resources" / "dedup-edition.json").write_text(
                json.dumps(dedup_meta, indent=2) + "\n", encoding="utf-8"
            )
        else:
            raise release.ReleaseError(f"Unknown npm variant: {variant}")

        result = subprocess.run(
            [NPM, "pack", "--json", "--pack-destination", str(pack_out)],
            cwd=staging,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
            timeout=240,
        )
        info = json.loads(result.stdout)
        tarball = pack_out / info[0]["filename"]
        raw = tarball.read_bytes()
        _verify_tarball(tarball, variant, baseline)
        return raw
    finally:
        for path in (staging, pack_out):
            if path.parent != temp_parent or path.is_symlink():
                raise release.ReleaseError(f"Refusing unexpected cleanup path: {path}")
            shutil.rmtree(path)


def _verify_tarball(tarball: Path, variant: str, baseline: dict) -> None:
    files_map = baseline["files"]
    with tarfile.open(tarball, "r:gz") as bundle:
        members = {m.name: bundle.extractfile(m).read() for m in bundle.getmembers() if m.isfile()}
    if "package/bin/pivotui.mjs" not in members or "package/language-sync.json" not in members:
        raise release.ReleaseError(f"{variant}: tarball missing installer or baseline")
    for name in members:
        if "/__pycache__/" in name or "/.venv/" in name or name.startswith("package/assets/"):
            raise release.ReleaseError(f"{variant}: unwanted file leaked into tarball: {name}")

    def check_edition_complete(edition: str, allow_dedup_from: str | None = None) -> None:
        prefix = f"package/{edition}/"
        for rel, pair in files_map.items():
            expected_hash = pair[edition]
            key = prefix + rel
            if key in members:
                if release.digest(members[key]) != expected_hash:
                    raise release.ReleaseError(f"{variant}: hash mismatch for {key}")
                continue
            if allow_dedup_from and pair[edition] == pair[allow_dedup_from]:
                shared_key = f"package/{allow_dedup_from}/{rel}"
                if shared_key in members and release.digest(members[shared_key]) == expected_hash:
                    continue
            if rel == NPM_PRESERVED_FILE:
                fallback = members.get("package/bin/npm-resources/gitignore.txt")
                if fallback is not None and release.digest(fallback) == expected_hash:
                    continue
            raise release.ReleaseError(f"{variant}: missing required file {edition}/{rel}")

    if variant == "en":
        if any(name.startswith("package/Chinese/") for name in members):
            raise release.ReleaseError("en: Chinese files leaked into English-only tarball")
        check_edition_complete("English")
    elif variant == "zh":
        if any(name.startswith("package/English/") for name in members):
            raise release.ReleaseError("zh: English files leaked into Chinese-only tarball")
        check_edition_complete("Chinese")
    elif variant == "universal":
        if "package/bin/npm-resources/dedup-edition.json" not in members:
            raise release.ReleaseError("universal: missing dedup-edition.json manifest")
        check_edition_complete("English")
        check_edition_complete("Chinese", allow_dedup_from="English")


def main() -> None:
    editions = {name: release.inventory(ROOT / name) for name in release.EDITIONS}
    release.check_structure(ROOT, editions)
    baseline = release.sync_manifest(editions)
    release.check_baseline(ROOT / "language-sync.json", baseline)

    variants = (
        ("universal", f"pivotui-installer-v{release.VERSION}.tgz"),
        ("zh", f"pivotui-installer-zh-v{release.VERSION}.tgz"),
        ("en", f"pivotui-installer-en-v{release.VERSION}.tgz"),
    )
    pending: dict[Path, bytes] = {}
    for variant, filename in variants:
        data = _pack_variant(variant, editions, baseline)
        pending[ROOT / "dist" / filename] = data
        print(f"Verified {filename}: {len(data) / (1024 * 1024):.2f} MB")

    checksum_text = "".join(f"{release.digest(data)}  {path.name}\n" for path, data in pending.items())
    pending[ROOT / "dist" / f"NPX-CHECKSUMS-v{release.VERSION}.sha256"] = checksum_text.encode("utf-8")

    for path, data in pending.items():
        if path.exists() and path.read_bytes() != data:
            raise release.ReleaseError(f"Refusing to overwrite different published tarball: {path.name}")
    release.unchanged_sources(ROOT, editions)
    (ROOT / "dist").mkdir(exist_ok=True)
    for path, data in pending.items():
        if not path.exists():
            with path.open("xb") as handle:
                handle.write(data)
        if path.read_bytes() != data:
            raise release.ReleaseError(f"Written file differs from verified bytes: {path.name}")
    print(f"Published {len(variants)} verified npm installer tarballs + checksums in dist/.")


if __name__ == "__main__":
    main()
