# `@getaway-wuji/pivotui` — Lightweight CLI Launcher

A tiny (< 10 KB), zero-dependency npm CLI package that installs the complete **PivotUI** Skill cluster without forcing users to memorize long GitHub Release URLs or download both language editions.

## Usage (once published to npm)

```sh
# Interactive mode (prompts for Agent and language)
npx @getaway-wuji/pivotui

# Direct project install (downloads ONLY the Chinese single-language release tarball)
npx @getaway-wuji/pivotui --agent codex --language zh

# Global install + prune older versions
npx @getaway-wuji/pivotui --agent claude-code --language en --global --prune

# Inspect status or uninstall cleanly
npx @getaway-wuji/pivotui --agent codex --status
npx @getaway-wuji/pivotui --agent codex --uninstall --prune
```

## Security model

1. Fetches `NPX-CHECKSUMS-v<version>.sha256` from the pinned GitHub Release.
2. Downloads only `pivotui-installer-<lang>-v<version>.tgz` (~29 MB) and verifies its exact SHA-256 digest before execution.
3. Delegates installation to the verified bundled `bin/pivotui.mjs`, which independently checks all installed files against `language-sync.json`.

## Publishing to npm

```sh
cd cli
npm publish --access public
```
