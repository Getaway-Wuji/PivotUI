"""Read-only, progressively loaded design skills over MCP stdio."""
from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
import hashlib
import json
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
from typing import Any

import yaml
from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import ToolAnnotations


MAX_HEADER_CHARS = 16_384
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_PAGE_CHARS = 12_000
TEXT_SUFFIXES = frozenset({
    ".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".css",
    ".html", ".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx", ".py", ".svg", ".csv",
})
ALIASES = {
    "taste-skill": "design-taste-frontend",
    "dashboard-skill": "dashboard-design",
    "interaction-skill": "interaction-design",
    "floating-component-skill": "floating-components",
    "global-style-skill": "global-style-skill",
}


class SkillError(Exception):
    def __init__(self, code: str, message: str, **details: Any):
        super().__init__(message)
        self.payload = {"code": code, "message": message, **details}


@dataclass(frozen=True)
class Entry:
    id: str
    name: str
    description: str
    manifest: Path
    package: Path
    category: str = ""
    allow_implicit_invocation: bool = True

    def metadata(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "allow_implicit_invocation": self.allow_implicit_invocation,
            "aliases": [key for key, value in ALIASES.items() if value == self.name and key != self.name],
        }


def read_header(path: Path) -> tuple[str, str, bool]:
    """Read only YAML frontmatter; never read the skill body for discovery."""
    with path.open("r", encoding="utf-8-sig") as stream:
        if stream.readline(MAX_HEADER_CHARS + 1).strip() != "---":
            raise SkillError("invalid_metadata", "SKILL.md needs YAML frontmatter.")
        lines: list[str] = []
        size = 0
        while True:
            line = stream.readline(MAX_HEADER_CHARS + 1)
            size += len(line)
            if size > MAX_HEADER_CHARS or not line:
                raise SkillError("invalid_metadata", "Frontmatter is incomplete or exceeds its size limit.")
            if line.strip() == "---":
                break
            lines.append(line)
    try:
        data = yaml.safe_load("".join(lines))
    except yaml.YAMLError:
        raise SkillError("invalid_metadata", "Frontmatter is not valid YAML.") from None
    if not isinstance(data, dict):
        raise SkillError("invalid_metadata", "Frontmatter must be a mapping.")
    name, description = data.get("name"), data.get("description")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", name):
        raise SkillError("invalid_metadata", "Skill name must use lowercase letters, digits and hyphens.")
    if not isinstance(description, str) or not description.strip() or len(description) > 2048:
        raise SkillError("invalid_metadata", "Skill description must contain 1–2048 characters.")
    implicit = data.get("disable-model-invocation") is not True
    policy_file = path.parent / "agents/openai.yaml"
    if policy_file.is_file():
        if not policy_file.resolve().is_relative_to(path.parent.resolve()):
            raise SkillError("outside_package", "Invocation policy leaves its skill package.")
        with policy_file.open("r", encoding="utf-8-sig") as stream:
            policy_text = stream.read(MAX_HEADER_CHARS + 1)
        if len(policy_text) > MAX_HEADER_CHARS:
            raise SkillError("invalid_metadata", "Invocation policy exceeds its size limit.")
        try:
            config = yaml.safe_load(policy_text)
        except yaml.YAMLError:
            raise SkillError("invalid_metadata", "Invocation policy is not valid YAML.") from None
        if isinstance(config, dict) and isinstance(config.get("policy"), dict):
            implicit = implicit and config["policy"].get("allow_implicit_invocation") is not False
    return name, description.strip(), implicit


def is_text_resource(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name.upper() in {"LICENSE", "NOTICE", "COPYING", "AUTHORS"}


def read_text(path: Path) -> str:
    """Bounded read of one selected UTF-8 text file."""
    if not is_text_resource(path):
        raise SkillError("unsupported_file", "Only supported text resources can be read.")
    try:
        with path.open("rb") as stream:
            raw = stream.read(MAX_FILE_BYTES + 1)
    except OSError:
        raise SkillError("unreadable_file", "The selected text resource is not readable.") from None
    if len(raw) > MAX_FILE_BYTES:
        raise SkillError("file_too_large", "The selected file exceeds the 2 MiB file limit.")
    try:
        return raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise SkillError("invalid_encoding", "Text resources must use UTF-8 encoding.") from None


class SkillLibrary:
    def __init__(self, roots: list[Path]):
        self.roots = list(dict.fromkeys(root.expanduser().resolve() for root in roots))

    def discover(self) -> tuple[list[Entry], list[dict[str, str]]]:
        entries: list[Entry] = []
        warnings: list[dict[str, str]] = []
        seen: dict[Path, int] = {}
        for number, root in enumerate(self.roots):
            root_id = f"root{number}"
            if not root.is_dir():
                warnings.append({"id": root_id, "code": "missing_root"})
                continue
            if (root / "SKILL.md").is_file():
                top_entries = [root / "SKILL.md"]
            else:
                top_entries = list(root.glob("*/SKILL.md"))
                for category in root.iterdir():
                    if not category.is_dir() or category.name.startswith(".") or category.name in {"design-system", "mcp", "references", "assets", "scripts"}:
                        continue
                    if not (category / "SKILL.md").is_file():
                        top_entries.extend(category.glob("*/SKILL.md"))
            candidates = list(top_entries)
            for top_entry in top_entries:
                sub_skills = top_entry.parent / "sub-skills"
                if sub_skills.is_dir():
                    candidates.extend(sub_skills.rglob("SKILL.md"))
            for lexical in sorted(set(candidates)):
                relative = lexical.relative_to(root).as_posix()
                entry_id = f"{root_id}:{relative}"
                try:
                    manifest = lexical.resolve(strict=True)
                    if not manifest.is_relative_to(root) or not manifest.is_file():
                        raise SkillError("outside_root", "Skill entry leaves its configured root.")
                    package = manifest.parent
                    for parent in manifest.parents:
                        if not parent.is_relative_to(root):
                            break
                        parent_manifest = parent / "SKILL.md"
                        if parent_manifest.is_file() and parent_manifest.resolve().is_relative_to(root):
                            package = parent
                    package_parts = package.relative_to(root).parts
                    category = package_parts[0] if len(package_parts) > 1 else ""
                    if manifest in seen:
                        index = seen[manifest]
                        previous = entries[index]
                        # Keep one catalog identity, but do not let an earlier
                        # leaf root hide shared resources authorized by another
                        # configured root containing the complete package.
                        if previous.package.is_relative_to(package):
                            entries[index] = replace(previous, package=package, category=category or previous.category)
                        continue
                    name, description, implicit = read_header(manifest)
                    seen[manifest] = len(entries)
                    entries.append(Entry(entry_id, name, description, manifest, package, category, implicit))
                except (SkillError, OSError, UnicodeError) as exc:
                    warnings.append({"id": entry_id, "code": exc.payload["code"] if isinstance(exc, SkillError) else "unreadable_metadata"})
        return entries, warnings

    def catalog(self, query: str = "") -> dict[str, Any]:
        entries, warnings = self.discover()
        terms = query.casefold().split()
        result = []
        for entry in entries:
            meta = entry.metadata()
            haystack = " ".join([entry.name, entry.description, entry.category, *meta["aliases"]]).casefold()
            if all(term in haystack for term in terms):
                result.append(meta)
        return {"skills": result, "count": len(result), "warnings": warnings}

    def resolve_entry(self, skill_id: str) -> Entry:
        entries, _ = self.discover()
        explicit = [entry for entry in entries if entry.id == skill_id]
        if explicit:
            return explicit[0]
        canonical = ALIASES.get(skill_id, skill_id)
        matches = [entry for entry in entries if entry.name == canonical or entry.name == skill_id]
        if not matches:
            raise SkillError("skill_not_found", "No available skill matches this id, name or alias.", requested=skill_id)
        if len(matches) > 1:
            raise SkillError("ambiguous_skill", "Several skills match. Select an exact catalog id.", candidates=[entry.metadata() for entry in matches])
        return matches[0]

    @staticmethod
    def resource_path(entry: Entry, resource: str) -> Path:
        normalized = resource.replace("\\", "/")
        windows = PureWindowsPath(resource)
        if not resource or PurePosixPath(normalized).is_absolute() or windows.drive or windows.root or ":" in resource:
            raise SkillError("invalid_resource_path", "Use a file path relative to the selected skill entry.")
        try:
            path = (entry.manifest.parent / normalized).resolve(strict=True)
        except (OSError, RuntimeError):
            raise SkillError("resource_not_found", "The resource does not exist.") from None
        if not path.is_relative_to(entry.package.resolve()):
            raise SkillError("outside_package", "The resource must remain inside the selected skill package.")
        if not path.is_file():
            raise SkillError("resource_not_found", "The selected resource is not a file.")
        return path

    @staticmethod
    def page(entry: Entry, resource: str, content: str, offset: int, limit: int) -> dict[str, Any]:
        if offset < 0 or offset > len(content) or not 1 <= limit <= MAX_PAGE_CHARS:
            raise SkillError("invalid_page", f"Use offset 0–total_chars and limit 1–{MAX_PAGE_CHARS}.")
        end = min(offset + limit, len(content))
        return {
            "skill": entry.metadata(), "path": resource,
            "content": content[offset:end], "offset": offset, "end_offset": end,
            "total_chars": len(content), "truncated": end < len(content),
            "next_offset": end if end < len(content) else None,
            "revision": hashlib.sha256(content.encode("utf-8")).hexdigest(),
        }

    def load(self, skill_id: str) -> dict[str, Any]:
        entry = self.resolve_entry(skill_id)
        content = read_text(self.resource_path(entry, "SKILL.md"))
        result = self.page(entry, "SKILL.md", content, 0, MAX_PAGE_CHARS)
        resources: list[str] = []
        for target in re.findall(r"\]\(([^\n)]+)\)", content):
            target = target.strip().strip("<>").split("#", 1)[0]
            if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            try:
                path = self.resource_path(entry, target)
                if is_text_resource(path) and target not in resources:
                    resources.append(target)
            except SkillError:
                continue
        result["linked_resources"] = resources
        return result

    def read(self, skill_id: str, resource: str, offset: int = 0, limit: int = MAX_PAGE_CHARS) -> dict[str, Any]:
        entry = self.resolve_entry(skill_id)
        path = self.resource_path(entry, resource)
        return self.page(entry, resource, read_text(path), offset, limit)


def create_server(library: SkillLibrary) -> MCPServer:
    server = MCPServer(
        "design-skill-cluster", version="1.0.0",
        instructions="Discover metadata, then load only selected skills and necessary linked files. These read-only tools supply instructions; the host AI performs the user task. Do not preload the catalog's bodies.",
    )

    def call(method: Any, *args: Any) -> dict[str, Any]:
        try:
            return method(*args)
        except SkillError as exc:
            raise ToolError(json.dumps(exc.payload, ensure_ascii=False)) from None

    readonly = ToolAnnotations(read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False)

    @server.tool(annotations=readonly)
    def catalog_skills(query: str = "") -> dict[str, Any]:
        """Discover skill names, descriptions, aliases and ids; never returns skill bodies. Optional query filters metadata."""
        return call(library.catalog, query)

    @server.tool(annotations=readonly)
    def load_skill(skill_id: str) -> dict[str, Any]:
        """Load one selected SKILL.md and its linked filenames. Resolve ambiguity with a catalog id. Continue truncated text with read_skill_file."""
        return call(library.load, skill_id)

    @server.tool(annotations=readonly)
    def read_skill_file(skill_id: str, path: str, offset: int = 0, limit: int = MAX_PAGE_CHARS) -> dict[str, Any]:
        """Read one UTF-8 file relative to a selected skill, within its package. Follow next_offset for pagination; compare revision across pages."""
        return call(library.read, skill_id, path, offset, limit)

    return server


def default_skill_roots(server_file: Path) -> list[Path]:
    """Use one complete language distribution, independent of the working directory."""
    base = server_file.resolve().parents[2]
    # A release can be extracted under any directory name. The repository's
    # shared server defaults to English; a packaged server stays in its release.
    distribution = base / "English" if (base / "English").is_dir() else base
    return [distribution]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, action="append", help="Skill directory or parent library; repeat to include external libraries.")
    args = parser.parse_args()
    roots = args.skill_root or default_skill_roots(Path(__file__))
    create_server(SkillLibrary(roots)).run(transport="stdio")


if __name__ == "__main__":
    main()
