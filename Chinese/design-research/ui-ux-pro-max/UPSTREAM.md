# Upstream provenance and portable use

- Project: UI/UX Pro Max Skill
- Author and copyright holder: Next Level Builder
- Repository: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Fixed revision: `6ae86f61f520d6ca229d2f40e070410638c908c5`
- Upstream package: `.claude/skills/ui-ux-pro-max/`
- Repository version: 2.15.0 (upstream `skill.json`)
- Imported: 2026-11-14
- License: [MIT](LICENSE), copied verbatim from the repository root, including the original copyright notice.

## Included files and changes

The complete upstream package is included: its entry, references, local research datasets, Python scripts, and bundled test files. The root `LICENSE` was added because it covers this extracted package. This provenance file is an additional distribution document.

Only `SKILL.md` was adapted: its plugin-specific `${CLAUDE_PLUGIN_ROOT}/.claude/skills/ui-ux-pro-max` command prefix was replaced with `<resolved-skill-directory>`, accompanied by instructions to resolve the loaded entry's actual directory. The reference to a missing repository README for Python installation was replaced by an explicit prerequisite note. No search logic, data, or design rules were changed. All other upstream package files retain their original bytes.

The pinned package contains ordinary files, not symlinks. Data resolution already uses each script's own location. No external repository directories are needed for local search or non-persisted design-system recommendations. Some upstream maintenance/regression tests may expect the original repository; retaining those files does not claim that the entire upstream suite runs from this extracted package.

## Running research after moving the package

Resolve this package's current directory from the loaded `SKILL.md` and invoke its `scripts/search.py` by absolute path. For example, replace the placeholder before execution:

```text
python "<resolved-skill-directory>/scripts/search.py" "keyboard focus modal" --domain ux --json
python "<resolved-skill-directory>/scripts/search.py" "analytics dashboard minimal" --design-system --json
```

The runtime needs Python 3 and its standard library. It reads the included datasets locally and does not require a network service or third-party Python installation. In this design cluster, results are research recommendations. The selected implementation lead and global-style capability decide what to adopt. Do not invoke `--persist` or `--force` merely to gather references; any product writes remain governed by the user's task and the target project's token ownership.

## Asset boundaries

The package includes upstream font-license metadata, icon metadata, and dataset provenance records. It does not include font binaries, unrelated `ui-styling` material, the repository CLI, or the entire repository. No font files are required for these local searches. If later implementing a recommendation that downloads fonts or other assets, follow the asset's own license; the package MIT notice does not relicense third-party assets.

The same original-language package and documented portability adaptation are used byte-for-byte in both cluster editions. File provenance hashes and actual import checks are retained in the authoring record; they are not runtime dependencies.
