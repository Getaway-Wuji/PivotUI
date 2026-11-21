"""Deterministic static validator for CSS custom properties and JSON design tokens.

Zero external dependencies (Python 3.11+ stdlib only). Checks:
- Duplicate token definitions inside the same CSS selector scope
- Undefined var(--token) / {token.ref} references
- Circular token references
- WCAG 2.1 contrast ratios for explicit --pair fg:bg checks (and hex/rgb color pairs)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any


COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)
DECL_RE = re.compile(r"(--[a-zA-Z0-9_-]+)\s*:\s*([^;{}]+?)\s*(?:;|$)")
VAR_RE = re.compile(r"var\(\s*(--[a-zA-Z0-9_-]+)\s*(?:,\s*([^)]+))?\)")
JSON_REF_RE = re.compile(r"\{([a-zA-Z0-9_.-]+)\}")
HEX_RE = re.compile(r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
RGB_RE = re.compile(r"^rgba?\(\s*(\d{1,3})\s*[, ]\s*(\d{1,3})\s*[, ]\s*(\d{1,3})(?:\s*[,/]\s*([0-9.]+%?))?\s*\)$")


def strip_comments(text: str) -> str:
    return COMMENT_RE.sub("", text)


def parse_css_scopes(text: str) -> list[tuple[str, list[tuple[str, str]]]]:
    """Extract (selector, [(name, value), ...]) pairs from top-level CSS blocks."""
    cleaned = strip_comments(text)
    scopes: list[tuple[str, list[tuple[str, str]]]] = []
    idx = 0
    n = len(cleaned)
    while idx < n:
        brace = cleaned.find("{", idx)
        if brace == -1:
            break
        selector = " ".join(cleaned[idx:brace].split())
        depth = 1
        pos = brace + 1
        while pos < n and depth > 0:
            if cleaned[pos] == "{":
                depth += 1
            elif cleaned[pos] == "}":
                depth -= 1
            pos += 1
        body = cleaned[brace + 1 : pos - 1]
        if selector.startswith("@media") or selector.startswith("@supports") or selector.startswith("@layer"):
            for sub_sel, decls in parse_css_scopes(body):
                scopes.append((f"{selector} > {sub_sel}", decls))
        else:
            decls = [(m.group(1), m.group(2).strip()) for m in DECL_RE.finditer(body)]
            if decls:
                scopes.append((selector or "<root>", decls))
        idx = pos
    return scopes


def flatten_json_tokens(data: Any, prefix: str = "") -> dict[str, str]:
    result: dict[str, str] = {}
    if isinstance(data, dict):
        if "$value" in data and prefix:
            result[prefix] = str(data["$value"]).strip()
            return result
        if "value" in data and len(data) <= 3 and prefix and not isinstance(data["value"], dict):
            result[prefix] = str(data["value"]).strip()
            return result
        for key, value in data.items():
            if key.startswith("$"):
                continue
            next_prefix = f"{prefix}.{key}" if prefix else key
            result.update(flatten_json_tokens(value, next_prefix))
    elif prefix and isinstance(data, (str, int, float)):
        result[prefix] = str(data).strip()
    return result


def parse_color(value: str) -> tuple[int, int, int] | None:
    raw = value.strip()
    m = HEX_RE.match(raw)
    if m:
        digits = m.group(1)
        if len(digits) == 3:
            return tuple(int(c * 2, 16) for c in digits)  # type: ignore[return-value]
        if len(digits) == 6:
            return (int(digits[0:2], 16), int(digits[2:4], 16), int(digits[4:6], 16))
        if len(digits) == 8 and digits[6:8].lower() == "ff":
            return (int(digits[0:2], 16), int(digits[2:4], 16), int(digits[4:6], 16))
        return None
    m = RGB_RE.match(raw)
    if m:
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if all(0 <= c <= 255 for c in (r, g, b)):
            alpha = m.group(4)
            if alpha is None or alpha in {"1", "1.0", "100%"}:
                return (r, g, b)
    return None


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    def channel(c: int) -> float:
        s = c / 255.0
        return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4

    r, g, b = rgb
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast_ratio(fg: tuple[int, int, int], bg: tuple[int, int, int]) -> float:
    l1 = relative_luminance(fg)
    l2 = relative_luminance(bg)
    lighter, darker = max(l1, l2), min(l1, l2)
    return round((lighter + 0.05) / (darker + 0.05), 3)


def resolve_value(name: str, mapping: dict[str, str], seen: list[str] | None = None) -> tuple[str | None, list[str] | None]:
    seen = list(seen or [])
    if name in seen:
        return None, seen + [name]
    if name not in mapping:
        return None, None
    seen.append(name)
    value = mapping[name]
    var_match = VAR_RE.fullmatch(value)
    if var_match:
        target = var_match.group(1)
        if target in mapping:
            return resolve_value(target, mapping, seen)
        fallback = var_match.group(2)
        return (fallback.strip(), None) if fallback else (None, None)
    json_match = JSON_REF_RE.fullmatch(value)
    if json_match:
        target = json_match.group(1)
        return resolve_value(target, mapping, seen)
    return value, None


def validate_files(paths: list[Path], pairs: list[str], min_ratio: float = 4.5) -> dict[str, Any]:
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    merged_tokens: dict[str, str] = {}
    css_scopes_all: list[tuple[str, str, dict[str, str]]] = []
    json_tokens_all: list[tuple[str, dict[str, str]]] = []

    for path in paths:
        label = path.as_posix()
        text = path.read_text(encoding="utf-8-sig")
        if path.suffix.lower() == ".json":
            data = json.loads(text)
            tokens = flatten_json_tokens(data)
            json_tokens_all.append((label, tokens))
            merged_tokens.update(tokens)
        else:
            scopes = parse_css_scopes(text)
            for selector, decls in scopes:
                seen_in_scope: dict[str, str] = {}
                for name, value in decls:
                    if name in seen_in_scope:
                        errors.append({
                            "code": "duplicate_token",
                            "file": label,
                            "scope": selector,
                            "token": name,
                            "message": f"Duplicate token {name} in scope {selector!r}.",
                        })
                    seen_in_scope[name] = value
                css_scopes_all.append((label, selector, seen_in_scope))
                if selector in {":root", "@theme", "html"} or not merged_tokens:
                    merged_tokens.update(seen_in_scope)
                else:
                    for k, v in seen_in_scope.items():
                        merged_tokens.setdefault(k, v)

    all_defined = set(merged_tokens)
    for _, _, scope_map in css_scopes_all:
        all_defined.update(scope_map)

    for label, selector, scope_map in css_scopes_all:
        effective = {**merged_tokens, **scope_map}
        for name, value in scope_map.items():
            for match in VAR_RE.finditer(value):
                ref = match.group(1)
                fallback = match.group(2)
                if ref not in effective and ref not in all_defined:
                    bucket = warnings if fallback else errors
                    bucket.append({
                        "code": "missing_reference",
                        "file": label,
                        "scope": selector,
                        "token": name,
                        "reference": ref,
                        "message": f"{name} references undefined token {ref}" + (" (has fallback)." if fallback else "."),
                    })
            _, cycle = resolve_value(name, effective)
            if cycle:
                errors.append({
                    "code": "reference_cycle",
                    "file": label,
                    "scope": selector,
                    "token": name,
                    "cycle": cycle,
                    "message": f"Circular reference detected: {' -> '.join(cycle)}.",
                })

    for label, tokens in json_tokens_all:
        for name, value in tokens.items():
            for match in JSON_REF_RE.finditer(value):
                ref = match.group(1)
                if ref not in merged_tokens:
                    errors.append({
                        "code": "missing_reference",
                        "file": label,
                        "scope": "json",
                        "token": name,
                        "reference": ref,
                        "message": f"{name} references undefined token {{{ref}}}.",
                    })
            _, cycle = resolve_value(name, merged_tokens)
            if cycle:
                errors.append({
                    "code": "reference_cycle",
                    "file": label,
                    "scope": "json",
                    "token": name,
                    "cycle": cycle,
                    "message": f"Circular reference detected: {' -> '.join(cycle)}.",
                })

    contrast_results: list[dict[str, Any]] = []
    for pair in pairs:
        if ":" not in pair:
            errors.append({"code": "invalid_pair", "pair": pair, "message": f"Use --pair fg:bg format, got {pair!r}."})
            continue
        fg_name, bg_name = [part.strip() for part in pair.split(":", 1)]
        fg_raw, _ = resolve_value(fg_name, merged_tokens)
        bg_raw, _ = resolve_value(bg_name, merged_tokens)
        fg_rgb = parse_color(fg_raw) if fg_raw else parse_color(fg_name)
        bg_rgb = parse_color(bg_raw) if bg_raw else parse_color(bg_name)
        if not fg_rgb or not bg_rgb:
            warnings.append({
                "code": "unparseable_color_pair",
                "pair": pair,
                "message": f"Could not resolve opaque hex/rgb colors for {fg_name} ({fg_raw}) on {bg_name} ({bg_raw}).",
            })
            continue
        ratio = contrast_ratio(fg_rgb, bg_rgb)
        passed = ratio >= min_ratio
        entry = {
            "foreground": fg_name,
            "background": bg_name,
            "ratio": ratio,
            "min_ratio": min_ratio,
            "passed": passed,
        }
        contrast_results.append(entry)
        if not passed:
            errors.append({
                "code": "low_contrast",
                **entry,
                "message": f"Contrast {ratio}:1 for {fg_name} on {bg_name} is below {min_ratio}:1.",
            })

    return {
        "files": [p.as_posix() for p in paths],
        "token_count": len(all_defined),
        "errors": errors,
        "warnings": warnings,
        "contrast": contrast_results,
        "ok": len(errors) == 0,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate CSS/JSON design tokens for duplicates, missing refs, cycles, and WCAG contrast.")
    parser.add_argument("files", nargs="+", type=Path, help="CSS or JSON token files to validate.")
    parser.add_argument("--pair", action="append", default=[], help="Check foreground:background token or color contrast (repeatable).")
    parser.add_argument("--min-ratio", type=float, default=4.5, help="Minimum WCAG contrast ratio for --pair checks (default: 4.5).")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Emit structured JSON output.")
    args = parser.parse_args(argv)

    missing = [p for p in args.files if not p.is_file()]
    if missing:
        print(f"Token file not found: {', '.join(str(p) for p in missing)}", file=sys.stderr)
        return 2

    report = validate_files(args.files, args.pair, args.min_ratio)
    if args.as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        status = "PASS" if report["ok"] else "FAIL"
        print(f"[{status}] Checked {len(report['files'])} file(s), {report['token_count']} token(s): {len(report['errors'])} error(s), {len(report['warnings'])} warning(s).")
        for item in report["contrast"]:
            mark = "OK" if item["passed"] else "FAIL"
            print(f"  contrast [{mark}] {item['foreground']} on {item['background']} = {item['ratio']}:1 (min {item['min_ratio']}:1)")
        for item in report["errors"]:
            print(f"  error [{item['code']}] {item['message']}")
        for item in report["warnings"]:
            print(f"  warn  [{item['code']}] {item['message']}")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
