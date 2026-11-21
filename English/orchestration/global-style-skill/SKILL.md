---
name: global-style-skill
description: Select or compare a product's visual direction and generate, organize, or validate its design tokens. Use for style exploration, requested visual changes, new themes, brand migrations, or cross-region consistency. Skip local behavior fixes covered by the existing theme.
metadata:
  version: 1.1.3
  tags: [theme, tokens, color, palette, typography, style, dark, light, contrast]
---

# Global Style and Design Tokens

Handle the current product's visual direction, design tokens, and consistent use of them. When called by the orchestrator, receive the scope and design evidence, return usable results, and let the orchestrator consolidate them. Apply the same rules when used independently. Recommend visual treatments within the requested scope; page owners decide composition and business semantics. Do not implement pages or components, or load other business skills.

## Establish the inputs

Read the task type, current theme source, established brand, reference purpose, allowed change scope, and output format from the request and target project. Prefer the target project's design conventions. Read this series' shared conventions and module records only when present in the target project. Work independently without those files; do not search for this skill's original authoring directory.

Distinguish direction advice, generation, local extension, migration, and validation only. If tokens are complete and the user only wants an interaction fix, return the source and "no change needed"; do not rebuild the theme for every request. A requested style comparison or visual change still belongs here even with complete tokens. Advice-only work returns recommendations without writing tokens or page code. Supply reasoned provisional values for ordinary missing details, labeling them as candidates. Ask only about material conflicts that cannot reasonably be inferred.

An established theme does not by itself prove that affected pages and components use it correctly. This module can contribute validation at delivery without selecting a new direction or regenerating values. Reuse adequate validation already completed by the implementer.

## Choose the visual evidence

- For a new project, use audience, page purpose, and references to choose a direction before assigning values. Without references, provide a clearly provisional starting point; do not present your choices as user preferences.
- For faithful reproduction, use the specified design as the visual authority. For integration into an existing product, map reference roles to its theme. Resolve conflicting mandatory requirements before delivery; do not silently replace colors or shapes at the end.
- Use verifiable source design or code values directly. Mark colors, fonts, and dimensions estimated from screenshots as estimates. Exploring candidates does not authorize replacing the current theme.

## Select a direction when needed

For open style choices or comparisons, read [selection rules](references/style-selection.md). Use the [style index](references/styles/index.md) to find relevant candidates, then read only their cards. These are combinable reference attributes, not 40 required templates or additional skills. Established visuals and scoped fixes skip this library unless the user requests reconsideration. Reuse directions already resolved by a compatible lead rather than conducting a second selection pass.

Choose and briefly explain a provisional direction when the task is clear or the user delegates the choice. Offer 2–3 concrete alternatives and ask the user to choose only when materially different directions remain equally plausible and the user's preference cannot be inferred; keep dependent visual changes pending while continuing independent work. Explicit references and current instructions take priority. The selection rules describe handoff, combination limits, evidence boundaries, and optional research without making other skills mandatory.

For requested case analysis/comparison or source verification, or a concrete case-evidence gap, use `design-reference-research` when available, following the selection guide's evidence rules. For specific visual borrowing, inspect supplied material or reuse adequate inspected evidence, researching only remaining source gaps unless research is explicitly requested. A name used only to describe atmosphere with a sufficiently supported direction does not require case research; record the intended mood without claiming observed product details. Research metadata and selected cases supplement this same decision; they do not start another theme workflow. Keep source observations, recommendations and synthetic examples distinct, and map adopted traits to the existing token source. Ordinary local repairs skip research. If that module is absent, inspect supplied evidence directly and disclose remaining gaps; this skill remains independently usable.

## Generate and consolidate

Find the editable source of truth and its generated outputs first. Reuse existing CSS custom properties, theme objects, or component-library configuration. When values are generated, edit the upstream source rather than maintaining two independently editable copies.

Add only what the current task needs:

| Category | Roles to express |
| --- | --- |
| Color | Primary color, backgrounds and surfaces, text hierarchy, borders, interaction states; business statuses and chart colors when needed |
| Typography | Font families and fallbacks, size scale, weight, line height, and numeric styles when needed |
| Spacing | Purposeful spacing scale, container margins, and component padding |
| Shape | Radius scale and strokes; shadows and stacking levels where justified |

Produce usable values, units, semantic names, and references, rather than descriptions such as "refined gray" or "moderate radius." Follow the project's naming and format. Check duplicate names, invalid values, missing references, and reference cycles. Match colors and fonts to actual backgrounds, languages, and available resources. Do not claim an unloaded font is active.

Express local differences as explicitly named component or region variants. Marketing headlines and dense dashboard tables can differ; pages must not silently redefine the same global token. For shared changes, list the purpose, old value, new value, reason, and affected scope. The orchestrator coordinates other regions; this module edits only the authorized scope.

## Validate actual output

Compare specified files or interfaces with the adopted design decisions and authoritative source. Check actual color, typography, spacing, and radius references for unintended overrides, missing variants, or invalid references. Classify local colors before changing them: a conflicting shared semantic role needs reconciliation; an intentional region variant needs an explicit scope; illustration or decorative constants may remain local. A literal value, including a fixed icon size, is not automatically an error.

When implementation adds several regions or changes shared theme values, verify representative affected consumers as well as the source:

- Select pages or shared components that cover distinct uses of the affected shared values. Include the relevant visible states, such as focus, selected, error, or disabled, rather than checking only defaults.
- Inspect actual foreground/background combinations and theme inheritance. Where present and affected, include image or transparent backgrounds and overlays rendered through a Portal or outside the theme container.
- Name the person or agent integrating findings; this can be the same implementer. Reuse still-valid evidence, and expand checks only for uncovered or changed uses. This does not require another reviewer, a new theme, or a full-site pass through every state.
- Record the inspected consumers, states and conditions, results or fix locations, and unverified scope in the existing project notes or requested output. Source-file checks alone do not verify rendered consumption.

For validation-only requests, return locatable findings, evidence, and proposed fixes. For correction requests, apply theme changes within scope. When Python 3.11+ is available, you can run [check_tokens.py](scripts/check_tokens.py) on CSS or JSON token files (`python scripts/check_tokens.py <file> [--pair --fg:--bg]`) to deterministically verify duplicate definitions, undefined `var()` references, reference cycles, and opaque hex/rgb WCAG contrast ratios; static token checks supplement rather than replace rendered-page inspection. Check contrast and other visual issues against actual combinations rather than variable names alone. Treat a user-selected new direction as a change, rather than mechanically restoring the old conventions.

## Return results

Deliver requested direction advice, token files, or changes in the project's existing format. For style decisions, state concrete traits, region boundaries, evidence and adopted/provisional status, plus any unresolved choice; the selection guide gives the lightweight handoff. Briefly record the task type, authoritative source location, changes and scope, affected regions, findings, and checks actually performed. Use target-project-relative paths. For candidate exploration, return candidates and recommendations without claiming they were applied.

The orchestrator can pass these results directly to page and component modules without regenerating values. Keep enough context for later chats, but do not write the product's brand back into the skill library. Distinguish file validation from runtime, rendering, or visual checks that were not performed.

Source: Shared UI Design Foundations 0.2 and this series' layered orchestration agreement. This file includes the required methods and has no mandatory dependency on another project or skill.
