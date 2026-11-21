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
SHARED_DOC_PATHS = {
    "FOUNDATIONS.md": "design-system/FOUNDATIONS.md",
    "ORCHESTRATION.md": "design-system/ORCHESTRATION.md",
    "README.md": "README.md",
    "THIRD_PARTY_NOTICES.md": "THIRD_PARTY_NOTICES.md",
}

# Read-only routing hints for unmodified upstream external packages so metadata
# filtering works before reading bodies without altering upstream SKILL.md bytes.
BUILTIN_HINTS: dict[str, dict[str, tuple[str, ...]]] = {
    "design-taste-frontend": {
        "requires": ("node>=22", "chromium-browser"),
        "tags": ("website", "marketing", "landing", "portfolio", "redesign"),
    },
    "ui-ux-pro-max": {
        "requires": ("python3",),
        "tags": ("research", "palette", "typography", "charts", "ux"),
    },
    "gpt-taste": {
        "exclude_scopes": ("dashboard", "business-tool", "admin"),
        "tags": ("marketing", "expressive", "gsap", "hero", "opt-in"),
    },
    "high-end-visual-design": {
        "tags": ("soft", "polished", "luxury", "opt-in"),
    },
    "minimalist-ui": {
        "tags": ("minimal", "editorial", "monochrome", "opt-in"),
    },
    "industrial-brutalist-ui": {
        "tags": ("brutalist", "industrial", "swiss", "opt-in"),
    },
    "imagegen-frontend-web": {
        "requires": ("image-generation-tool",),
        "tags": ("image", "mockup", "website", "concept"),
    },
    "imagegen-frontend-mobile": {
        "requires": ("image-generation-tool",),
        "tags": ("image", "mockup", "mobile", "app", "concept"),
    },
    "brandkit": {
        "requires": ("image-generation-tool",),
        "tags": ("brand", "logo", "moodboard", "image"),
    },
    "image-to-code": {
        "requires": ("image-generation-tool", "coding-agent"),
        "tags": ("image", "concept", "frontend", "code"),
    },
    "stitch-design-taste": {
        "requires": ("google-stitch",),
        "tags": ("stitch", "design-md", "opt-in"),
    },
    "design-taste-frontend-v1": {
        "tags": ("legacy", "opt-in"),
    },
    "design-taste-frontend-v2-experimental": {
        "exclude_scopes": ("dashboard", "data-table", "business-tool"),
        "tags": ("legacy", "experimental", "opt-in"),
    },
    "redesign-existing-projects": {
        "tags": ("legacy", "redesign", "audit", "opt-in"),
    },
}

SYNONYM_GROUPS: tuple[frozenset[str], ...] = (
    frozenset({"弹窗", "弹框", "对话框", "浮层", "提示框", "抽屉", "气泡", "modal", "drawer", "dialog", "toast", "tooltip", "alert", "popconfirm", "overlay", "floating"}),
    frozenset({"表格", "数据表", "列表", "分页", "筛选", "批量", "table", "list", "data-list", "pagination", "filter", "bulk"}),
    frozenset({"看板", "仪表盘", "仪表板", "概览", "图表", "指标", "监控", "dashboard", "chart", "kpi", "analytics", "monitoring"}),
    frozenset({"主题", "配色", "颜色", "暗黑", "深色", "浅色", "字体", "排版", "风格", "设计变量", "token", "tokens", "theme", "color", "palette", "typography", "style", "dark", "light"}),
    frozenset({"导航", "侧边栏", "侧栏", "顶栏", "菜单", "面包屑", "框架", "壳子", "shell", "sidebar", "navigation", "nav", "breadcrumb", "header"}),
    frozenset({"响应式", "移动端", "手机", "窄屏", "自适应", "适配", "溢出", "断点", "触控", "responsive", "mobile", "narrow", "overflow", "breakpoint", "touch", "reflow"}),
    frozenset({"表单", "表单页", "设置", "设置页", "编辑", "编辑页", "新建", "向导", "输入框", "校验", "验证", "提交", "草稿", "form", "settings", "wizard", "edit", "create", "input", "validation", "submit", "draft"}),
    frozenset({"详情", "详情页", "记录", "实体", "核查", "属性", "时间线", "detail", "record", "entity", "inspection", "timeline"}),
    frozenset({"按钮", "点击", "加载态", "button", "press", "loading", "pending"}),
    frozenset({"组件", "控件", "组件库", "变体", "component", "components", "primitive", "variant"}),
    frozenset({"交互", "动效", "动画", "焦点", "键盘", "反馈", "恢复", "interaction", "animation", "motion", "focus", "keyboard", "feedback", "recovery"}),
    frozenset({"官网", "落地页", "宣传页", "营销页", "营销", "作品集", "公开网站", "marketing", "landing", "website", "portfolio", "hero"}),
    frozenset({"生图", "图像", "图片", "概念图", "品牌板", "视觉板", "image", "imagegen", "brandkit", "mockup"}),
    frozenset({"研究", "参考", "案例", "对标", "调研", "竞品", "research", "reference", "case", "benchmark"}),
)

CJK_SYNONYM_TOKENS: tuple[str, ...] = tuple(
    sorted(
        {token for group in SYNONYM_GROUPS for token in group if len(token) >= 2 and any("\u4e00" <= ch <= "\u9fff" for ch in token)},
        key=len,
        reverse=True,
    )
)


class SkillError(Exception):
    def __init__(self, code: str, message: str, **details: Any):
        super().__init__(message)
        self.payload = {"code": code, "message": message, **details}


@dataclass(frozen=True)
class HeaderData:
    name: str
    description: str
    allow_implicit_invocation: bool
    version: str = ""
    aliases: tuple[str, ...] = ()
    tags: tuple[str, ...] = ()
    requires: tuple[str, ...] = ()
    exclude_scopes: tuple[str, ...] = ()


@dataclass(frozen=True)
class Entry:
    id: str
    name: str
    description: str
    manifest: Path
    package: Path
    category: str = ""
    allow_implicit_invocation: bool = True
    version: str = ""
    extra_aliases: tuple[str, ...] = ()
    tags: tuple[str, ...] = ()
    requires: tuple[str, ...] = ()
    exclude_scopes: tuple[str, ...] = ()

    def all_aliases(self) -> list[str]:
        combined = [key for key, value in ALIASES.items() if value == self.name and key != self.name]
        for alias in self.extra_aliases:
            if alias != self.name and alias not in combined:
                combined.append(alias)
        return combined

    def metadata(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "allow_implicit_invocation": self.allow_implicit_invocation,
            "aliases": self.all_aliases(),
            "version": self.version,
            "tags": list(self.tags),
            "requires": list(self.requires),
            "exclude_scopes": list(self.exclude_scopes),
        }


def _string_tuple(value: Any) -> tuple[str, ...]:
    if isinstance(value, str):
        stripped = value.strip()
        return (stripped,) if stripped else ()
    if isinstance(value, list):
        items: list[str] = []
        for item in value:
            if isinstance(item, str) and item.strip() and item.strip() not in items:
                items.append(item.strip())
        return tuple(items)
    return ()


def _merge_tuples(*groups: tuple[str, ...]) -> tuple[str, ...]:
    merged: list[str] = []
    for group in groups:
        for item in group:
            if item and item not in merged:
                merged.append(item)
    return tuple(merged)


def read_header_data(path: Path) -> HeaderData:
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
    meta = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
    raw_version = meta.get("version") if meta.get("version") is not None else data.get("version")
    version = str(raw_version).strip() if raw_version is not None else ""
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
    hints = BUILTIN_HINTS.get(name, {})
    aliases = _merge_tuples(_string_tuple(meta.get("aliases")), _string_tuple(data.get("aliases")))
    tags = _merge_tuples(_string_tuple(meta.get("tags")), _string_tuple(data.get("tags")), hints.get("tags", ()))
    requires = _merge_tuples(_string_tuple(meta.get("requires")), _string_tuple(data.get("requires")), hints.get("requires", ()))
    exclude_scopes = _merge_tuples(
        _string_tuple(meta.get("exclude_scopes")),
        _string_tuple(data.get("exclude_scopes")),
        hints.get("exclude_scopes", ()),
    )
    return HeaderData(
        name=name,
        description=description.strip(),
        allow_implicit_invocation=implicit,
        version=version,
        aliases=aliases,
        tags=tags,
        requires=requires,
        exclude_scopes=exclude_scopes,
    )


def read_header(path: Path) -> tuple[str, str, bool]:
    """Backward-compatible wrapper returning (name, description, allow_implicit_invocation)."""
    header = read_header_data(path)
    return header.name, header.description, header.allow_implicit_invocation


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


def _without_fences(text: str) -> str:
    output: list[str] = []
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


def _expand_query_terms(query: str) -> list[set[str]]:
    raw_terms = [part for part in re.split(r"[\s,，、/]+", query.casefold()) if part]
    expanded: list[set[str]] = []
    for term in raw_terms:
        matches: set[str] = {term}
        matched_group = False
        for group in SYNONYM_GROUPS:
            if term in group:
                matches.update(group)
                matched_group = True
        if not matched_group and any("\u4e00" <= ch <= "\u9fff" for ch in term):
            sub_tokens = [tok for tok in CJK_SYNONYM_TOKENS if tok in term]
            if sub_tokens:
                # Decompose CJK compounds like "移动端表格" into independent intent terms.
                seen_groups: list[frozenset[str]] = []
                for tok in sub_tokens:
                    for group in SYNONYM_GROUPS:
                        if tok in group and group not in seen_groups:
                            seen_groups.append(group)
                            expanded.append(set(group) | {tok})
                continue
        expanded.append(matches)
    return expanded


def _file_signature(path: Path) -> tuple[int, int, int] | None:
    try:
        st = path.stat()
    except OSError:
        return None
    return (st.st_mtime_ns, st.st_size, st.st_ctime_ns)


class SkillLibrary:
    def __init__(self, roots: list[Path]):
        self.roots = list(dict.fromkeys(root.expanduser().resolve() for root in roots))
        self._header_cache: dict[Path, tuple[tuple[int, int, int] | None, tuple[int, int, int] | None, HeaderData]] = {}

    def _cached_header(self, manifest: Path) -> HeaderData:
        policy_file = manifest.parent / "agents/openai.yaml"
        m_sig = _file_signature(manifest)
        p_sig = _file_signature(policy_file) if policy_file.is_file() else None
        cached = self._header_cache.get(manifest)
        if cached is not None and cached[0] == m_sig and cached[1] == p_sig:
            return cached[2]
        header = read_header_data(manifest)
        self._header_cache[manifest] = (m_sig, p_sig, header)
        return header

    def discover(self) -> tuple[list[Entry], list[dict[str, str]]]:
        entries: list[Entry] = []
        warnings: list[dict[str, str]] = []
        seen: dict[Path, int] = {}
        live_manifests: set[Path] = set()
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
                    live_manifests.add(manifest)
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
                    header = self._cached_header(manifest)
                    seen[manifest] = len(entries)
                    entries.append(
                        Entry(
                            id=entry_id,
                            name=header.name,
                            description=header.description,
                            manifest=manifest,
                            package=package,
                            category=category,
                            allow_implicit_invocation=header.allow_implicit_invocation,
                            version=header.version,
                            extra_aliases=header.aliases,
                            tags=header.tags,
                            requires=header.requires,
                            exclude_scopes=header.exclude_scopes,
                        )
                    )
                except (SkillError, OSError, UnicodeError) as exc:
                    warnings.append({"id": entry_id, "code": exc.payload["code"] if isinstance(exc, SkillError) else "unreadable_metadata"})
        # Drop stale cache entries for deleted skills.
        for stale in set(self._header_cache) - live_manifests:
            self._header_cache.pop(stale, None)
        return entries, warnings

    def catalog(self, query: str = "") -> dict[str, Any]:
        entries, warnings = self.discover()
        term_groups = _expand_query_terms(query)
        result = []
        for entry in entries:
            meta = entry.metadata()
            haystack = " ".join([
                entry.name,
                entry.description,
                entry.category,
                entry.version,
                *meta["aliases"],
                *meta["tags"],
                *meta["requires"],
                *meta["exclude_scopes"],
            ]).casefold()
            if all(any(candidate in haystack for candidate in group) for group in term_groups):
                result.append(meta)
        return {"skills": result, "count": len(result), "warnings": warnings}

    def resolve_entry(self, skill_id: str) -> Entry:
        entries, _ = self.discover()
        explicit = [entry for entry in entries if entry.id == skill_id]
        if explicit:
            return explicit[0]
        canonical = ALIASES.get(skill_id, skill_id)
        matches = [
            entry
            for entry in entries
            if entry.name == canonical or entry.name == skill_id or skill_id in entry.extra_aliases
        ]
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
        for token in re.findall(r"`([^`\n]{2,200})`", _without_fences(content)):
            candidate = token.strip().split("#", 1)[0]
            if not candidate or " " in candidate or candidate in {"SKILL.md"} or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", candidate):
                continue
            if "/" not in candidate and "." not in candidate and candidate.upper() not in {"LICENSE", "NOTICE", "COPYING", "AUTHORS"}:
                continue
            try:
                path = self.resource_path(entry, candidate)
                if is_text_resource(path) and candidate not in resources:
                    resources.append(candidate)
            except SkillError:
                continue
        result["linked_resources"] = resources
        return result

    def read(self, skill_id: str, resource: str, offset: int = 0, limit: int = MAX_PAGE_CHARS) -> dict[str, Any]:
        entry = self.resolve_entry(skill_id)
        path = self.resource_path(entry, resource)
        return self.page(entry, resource, read_text(path), offset, limit)

    def shared_doc_path(self, doc_name: str) -> Path:
        relative = SHARED_DOC_PATHS.get(doc_name)
        if relative is None:
            raise SkillError("resource_not_found", "Unknown shared cluster document.", requested=doc_name)
        for root in self.roots:
            if not root.is_dir():
                continue
            candidate = root / relative
            try:
                resolved = candidate.resolve(strict=True)
            except (OSError, RuntimeError):
                continue
            if resolved.is_relative_to(root) and resolved.is_file():
                return resolved
        raise SkillError("resource_not_found", "The requested shared cluster document is not present in the configured roots.", requested=doc_name)

    def list_shared_docs(self) -> list[str]:
        available: list[str] = []
        for doc_name in SHARED_DOC_PATHS:
            try:
                self.shared_doc_path(doc_name)
                available.append(doc_name)
            except SkillError:
                continue
        return available

    def read_shared_doc(self, doc_name: str) -> str:
        return read_text(self.shared_doc_path(doc_name))


def create_server(library: SkillLibrary) -> MCPServer:
    server = MCPServer(
        "design-skill-cluster", version="1.1.0",
        instructions=(
            "Discover metadata (including category, version, tags, requires, exclude_scopes and allow_implicit_invocation), "
            "then load only selected skills and necessary linked files. Shared cluster guides are available as read-only MCP resources "
            "under pivotui://docs/. These read-only tools supply instructions; the host AI performs the user task. Do not preload the catalog's bodies."
        ),
    )

    def call(method: Any, *args: Any) -> dict[str, Any]:
        try:
            return method(*args)
        except SkillError as exc:
            raise ToolError(json.dumps(exc.payload, ensure_ascii=False)) from None

    readonly = ToolAnnotations(read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False)

    @server.tool(annotations=readonly)
    def catalog_skills(query: str = "") -> dict[str, Any]:
        """Discover skill names, descriptions, versions, tags, prerequisites, exclusions, aliases and ids; never returns skill bodies. Optional query supports bilingual UI intent filtering."""
        return call(library.catalog, query)

    @server.tool(annotations=readonly)
    def load_skill(skill_id: str) -> dict[str, Any]:
        """Load one selected SKILL.md and its linked filenames. Resolve ambiguity with a catalog id. Continue truncated text with read_skill_file."""
        return call(library.load, skill_id)

    @server.tool(annotations=readonly)
    def read_skill_file(skill_id: str, path: str, offset: int = 0, limit: int = MAX_PAGE_CHARS) -> dict[str, Any]:
        """Read one UTF-8 file relative to a selected skill, within its package. Follow next_offset for pagination; compare revision across pages."""
        return call(library.read, skill_id, path, offset, limit)

    def register_shared_doc(doc_name: str, description: str) -> None:
        @server.resource(f"pivotui://docs/{doc_name}", name=doc_name, description=description, mime_type="text/markdown")
        def _read_doc() -> str:
            try:
                return library.read_shared_doc(doc_name)
            except SkillError as exc:
                raise ToolError(json.dumps(exc.payload, ensure_ascii=False)) from None

    register_shared_doc("FOUNDATIONS.md", "Shared interface design foundations for the selected edition.")
    register_shared_doc("ORCHESTRATION.md", "Cluster orchestration agreement for authored and external skills.")
    register_shared_doc("README.md", "Edition skill inventory, origins, versions, and usage overview.")
    register_shared_doc("THIRD_PARTY_NOTICES.md", "Upstream licenses, attributions, and bundled asset notices.")

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
