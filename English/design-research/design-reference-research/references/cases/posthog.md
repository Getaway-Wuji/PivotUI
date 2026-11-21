# PostHog — warm cream documentation and analytics cards

Case ID: `posthog`. Status: `document_reviewed_product_unverified`. Review date: 2026-11-21.

## Surface and evidence

Developer-tools marketing, documentation chrome, and analytics card presentation (`PostHog-design-analysis`). It captures surface contrast, doc typography, and semantic pill colors rather than verified live product query builders or session-replay players.

The following relationships and values are third-party descriptions or claimed extractions, not independent measurements of the live product. Adaptation paragraphs are this project's proposals. See the `posthog` row in [catalog-03.csv](../catalog/catalog-03.csv) for the pinned revision, source path, hash, and byte size.

## Useful visual relationships

- Separates white content cards (`#ffffff`) and doc surfaces (`#fcfcfa`) from a warm cream canvas (`#eeefe9`, soft `#e5e7e0`) using crisp olive hairlines (`#bfc1b7`, `#dcdfd2`) and tight `4px–6px` radii, avoiding heavy drop shadows.
- Uses warm olive-charcoal text hierarchy (`#23251d` headings, `#4d4f46` body, `#6c6e63` muted) paired with a single amber CTA (`#f7a501` with dark `#23251d` ink) and accessible soft-tinted semantic status pairs (blue `#2c84e0`/`#dceaf6`, red `#cd4239`/`#f7d6d3`, green `#2c8c66`/`#d9eddf`, purple `#7c44a6`/`#e7d8ee`).
- Keeps display headings restrained (`36px`/`24px`) relative to `14px–16px` body and `14px` code, supporting dense documentation and analytical workspaces cleanly.

## Transfer into the target product

When a product analytics tool, internal console, or documentation hub wants a warm, approachable light theme instead of sterile white or dark-tech chrome, borrow the cream-canvas + white-card + thin-border surface ladder and the paired soft/strong semantic status tokens. Keep brand illustrations optional and strictly scoped so they never obscure tables, filters, or form actions.

## Evidence limits and completion needs

Document review covers public site, docs, and static analytics-card styling; live funnel builders, multi-filter tables, keyboard shortcuts, and mobile navigation drawers remain unverified. Always validate muted text (`#6c6e63` / `#9b9c92`) contrast against `#eeefe9` and `#ffffff` in real usage, and ensure status cues combine text/icons with color.

## Pinned sources

[VoltAgent source analysis](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/posthog/DESIGN.md). Source locators: [Palette and semantic accents](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/posthog/DESIGN.md#L7) · [Typography scale](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/posthog/DESIGN.md#L38). Source documentation is covered by the package's [MIT LICENSE](../../LICENSE); fonts and brand assets are not supplied.
