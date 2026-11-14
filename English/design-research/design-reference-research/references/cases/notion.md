# Notion — marketing grouping and pricing

Case ID: `notion`. Status: `document_reviewed_product_unverified`. Review date: 2026-11-14.

## Surface and evidence

Homepage, enterprise, product AI, product agents, startups and pricing. This is a marketing/pricing analysis, not a specification of the workspace editor or database views.

The following relationships and values are third-party descriptions or claimed extractions, not independent measurements of the current site. Adaptation paragraphs are this project's proposals. Find the exact upstream path, fixed revision, original-file hash and byte size in the `notion` row of the [metadata record](../catalog/catalog-03.csv).

## Useful visual relationships

- The source describes a dark navy hero with product imagery, then lighter feature/pricing areas. Pastel feature groups can separate product stories without changing the whole page theme.
- It distinguishes primary-action purple `#5645d4` from ordinary-link blue `#0075de`; neutral canvas `#ffffff`, surface `#f6f5f4` and hairline `#e5e3df` support reading. Pastel candidates include peach `#ffe8d4` and mint `#d9f3e1`.
- Typography lists 80px/600 hero display, 16px/400 body and 14px/500 action text. The four pricing tiers pair concise offer cards with a separate comparison structure rather than putting every fact into a card.

## Transfer into the target product

For a feature-rich SaaS marketing page, group stories by the decision they help make. Use a small number of scoped surface tints and retain one consistent action hierarchy. For pricing, distinguish the quick plan-selection summary from detailed feature comparisons, preserving factual definitions and available plans.

If the target already has one link/action color, this reference is a comparison candidate rather than permission to introduce two new brand colors. For Chinese pricing copy, test tier names, billing explanations and feature labels at narrow widths; preserve complete information when tables reflow.

## Evidence limits and completion needs

The source explicitly says transition timing was not extracted: 150–200ms is its recommendation. Successful form-validation states were not captured. Its responsive table and summary disagree about feature-card column counts in a phone interval. Adopt explicit target-product behavior and test it; do not silently present either sentence as observed fact.

When implementing, complete keyboard, focus, loading, error and narrow-screen behavior for the actual content, and check real contrast. Case values are not library-wide Token defaults or an accessibility pass.

## Pinned sources

[VoltAgent source analysis](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/notion/DESIGN.md). Source locators: [Values and roles](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/notion/DESIGN.md#L6) · [Source-page scope](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/notion/DESIGN.md#L467) · [Responsive disagreement](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/notion/DESIGN.md#L781) · [Known gaps and timing](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/notion/DESIGN.md#L816). Source documentation is covered by the package's [MIT LICENSE](../../LICENSE); fonts and brand assets are not supplied.
