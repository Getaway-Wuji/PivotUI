"""Build portable manual-install ZIPs using the same Node project installer.

Maintainer tool: requires Node.js and the Python dependencies of release.py.
End users can extract and copy the resulting files without either runtime.
"""

from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import tempfile

import release


ROOT = Path(__file__).resolve().parents[1]
PACKAGING_REVISION = 2


def project_files(edition: str, language: str) -> dict[str, bytes]:
    temp_parent = Path(tempfile.gettempdir()).resolve()
    staging = Path(tempfile.mkdtemp(prefix="pivotui-project-build-", dir=temp_parent)).resolve()
    try:
        subprocess.run(
            ["node", str(ROOT / "bin" / "pivotui.mjs"), "--agent", "codex",
             "--language", language, "--project", str(staging)],
            check=True, capture_output=True, text=True, encoding="utf-8",
        )
        entry_dir = staging / ".agents" / "skills" / "pivotui"
        manifest = json.loads((entry_dir / ".pivotui-install.json").read_text(encoding="utf-8"))
        library_ref = Path(manifest["library"])
        if library_ref.is_absolute():
            raise release.ReleaseError("Project manifest contains an absolute library path")
        library = (entry_dir / library_ref).resolve()
        if not library.is_relative_to(staging / ".pivotui" / "libraries"):
            raise release.ReleaseError("The installed library escaped the portable project layout")
        if (staging / ".claude" / "skills" / "pivotui" / library_ref).resolve() != library:
            raise release.ReleaseError("The entry cannot be copied into the documented Claude Code layout")
        if release.inventory(library) != release.inventory(ROOT / edition):
            raise release.ReleaseError(f"{edition}: installed project resources differ from the edition")
        guide = (ROOT / "scripts" / "install-resources" / edition / "manual.txt").read_text(encoding="utf-8")
        (staging / "INSTALL.md").write_text(guide.replace("{{LIBRARY_NAME}}", library.name), encoding="utf-8", newline="\n")
        files = release.inventory(staging)
        for relative, data in files.items():
            if str(staging).encode("utf-8") in data or staging.as_posix().encode("utf-8") in data:
                raise release.ReleaseError(f"Build-machine path in project archive: {relative}")
            if relative.endswith(".md"):
                for target in release.markdown_targets(data.decode("utf-8-sig")):
                    release.check_link(staging, relative, target)
        return files
    finally:
        # Delete only this builder's temporary directory, never an arbitrary target.
        if staging.parent != temp_parent or not staging.name.startswith("pivotui-project-build-") or staging.is_symlink():
            raise release.ReleaseError("Unexpected staging directory; refusing cleanup")
        shutil.rmtree(staging)


def main() -> None:
    editions = {name: release.inventory(ROOT / name) for name in release.EDITIONS}
    release.check_structure(ROOT, editions)
    release.check_baseline(ROOT / "language-sync.json", release.sync_manifest(editions))
    pending = {}
    for edition, language in (("English", "en"), ("Chinese", "zh")):
        files = project_files(edition, language)
        archive_root = f"PivotUI-{edition}"
        data = release.archive_bytes(archive_root, files)
        release.verify_archive(data, archive_root, files)
        name = f"PivotUI-{edition}-project-v{release.VERSION}-r{PACKAGING_REVISION}.zip"
        pending[ROOT / "dist" / name] = data
        print(f"Verified {name}: {len(files)} files, relative entry paths, unchanged edition resources.")
    checksums = "".join(f"{release.digest(data)}  {path.name}\n" for path, data in pending.items())
    pending[ROOT / "dist" / f"PROJECT-CHECKSUMS-v{release.VERSION}-r{PACKAGING_REVISION}.sha256"] = checksums.encode("utf-8")
    for path, data in pending.items():
        if path.exists() and path.read_bytes() != data:
            raise release.ReleaseError(f"Refusing to replace a different published project archive: {path.name}")
    release.unchanged_sources(ROOT, editions)
    (ROOT / "dist").mkdir(exist_ok=True)
    for path, data in pending.items():
        if not path.exists():
            with path.open("xb") as handle:
                handle.write(data)
        if path.read_bytes() != data:
            raise release.ReleaseError(f"Written archive differs from validated bytes: {path.name}")
        print(path.name)


if __name__ == "__main__":
    main()
