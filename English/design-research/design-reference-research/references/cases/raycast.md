# Raycast — dark command-palette surface ladder

Case ID: `raycast`. Status: `document_reviewed_product_unverified`. Review date: 2026-11-21.

## Surface and evidence

Marketing surfaces modeled on command-palette chrome and extension-store cards (`Raycast-design-analysis`). Full-bleed product screenshots show command-palette and AI chat aesthetics, not verified desktop-app keyboard trees or web accessibility behavior.

The following relationships and values are third-party descriptions or claimed extractions, not independent measurements of the live product. Adaptation paragraphs are this project's proposals. See the `raycast` row in [catalog-03.csv](../catalog/catalog-03.csv) for the pinned revision, source path, hash, and byte size.

## Useful visual relationships

- Uses a disciplined near-black surface ladder (`#07080a` canvas → `#0d0d0d` surface → `#101111` elevated → `#121212` card) separated by `1px` hairlines (`#242728`, `rgba(255,255,255,0.08–0.16)`) and tight `6px–10px` radii instead of glowing borders or heavy blur.
- Keeps chrome monochrome with a high-contrast white primary action pill (`#ffffff` / `#000000` ink), reserving four crisp semantic/category accents (`#57c1ff` blue, `#ff6161` red, `#59d499` green, `#ffc533` yellow) paired with 15% opacity soft backdrops for badges and category icons.
- Applies compact heading steps (`24px`, `22px`, `20px`, `18px`) above `14px–16px` body text, fitting command palettes, quick-switchers, and dark utility panels well.

## Transfer into the target product

For dark command menus, developer workspaces, or keyboard-first utility panels, borrow the subtle surface-elevation ladder, 1px hairline separation, and 15%-alpha tinted semantic badge pairing. Map colors into the product's existing dark theme tokens, keep visible keyboard focus rings distinct from `#242728` borders, and verify contrast for muted gray text (`#9c9c9d` / `#6a6b6c`) before using it for functional labels.

## Evidence limits and completion needs

The upstream analysis targets marketing surfaces scaled from product chrome (note: line 4 of the upstream file contains a stray non-standard YAML key; treat only inspected visual descriptions as reference data). Real command-menu keyboard navigation, IME composition, focus restoration, and light-theme equivalents must be completed via `navigation-interaction` and `global-style-skill`.

## Pinned sources

[VoltAgent source analysis](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/raycast/DESIGN.md). Source locators: [Dark surface ladder and accents](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/raycast/DESIGN.md#L8) · [Typography scale](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/raycast/DESIGN.md#L41). Source documentation is covered by the package's [MIT LICENSE](../../LICENSE); fonts and brand assets are not supplied.
