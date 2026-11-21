# Sentry — dual-polarity violet developer-tool surfaces

Case ID: `sentry`. Status: `document_reviewed_product_unverified`. Review date: 2026-11-21.

## Surface and evidence

Marketing pages, pricing surfaces, and developer-tool presentation framed as an inspired analysis (`Sentri-Inspired-design-analysis`). It does not establish live Sentry issue-tracker tables, triage workflows, or backend alert rules.

The following relationships and values are third-party descriptions or claimed extractions, not independent measurements of the live product. Adaptation paragraphs are this project's proposals. See the `sentry` row in [catalog-03.csv](../catalog/catalog-03.csv) for the pinned revision, source path, hash, and byte size.

## Useful visual relationships

- Combines deep violet-midnight dark surfaces (`#150f23`, `#1f1633`, hairline `#362d59`) with crisp white pricing/documentation bands (`#ffffff`, hairlines `#cfcfdb` / `#e5e7eb`), keeping primary dark-violet action buttons (`#150f23` with `#ffffff` text) readable across polarities.
- Reserves high-energy accents (`#c2ef4e` lime, `#fa7faa` pink, `#6a5fc1` violet) for highlights and badges while keeping UI body copy in neutral Rubik / system sans (`16px`) and code snippets in monospaced Monaco/Menlo (`16px`).
- Lists an explicit blue focus ring (`#9dc1f5`) and crisp 6–12px radii across buttons and cards.

## Transfer into the target product

For a technical monitoring or developer-platform product needing both dark hero/console regions and high-density light pricing/config tables, borrow the polarity discipline: keep dark surfaces quiet and neutral-violet rather than neon-saturated, and let status/severity semantics in operational tables follow the product's own accessible status tokens rather than decorative lime/pink accents.

## Evidence limits and completion needs

The source is explicitly an inspired interpretation covering public developer marketing and pricing. It does not specify real issue-list filtering, keyboard shortcuts, alert escalation workflows, or dark/light theme toggling in production dashboards. Custom display fonts are not bundled. Verify actual foreground/background contrast on any light/dark surfaces and complete keyboard, loading, and narrow-screen behavior locally.

## Pinned sources

[VoltAgent source analysis](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/sentry/DESIGN.md). Source locators: [Palette and typography](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/sentry/DESIGN.md#L6) · [Button tokens](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/sentry/DESIGN.md#L146). Source documentation is covered by the package's [MIT LICENSE](../../LICENSE); fonts and brand assets are not supplied.
