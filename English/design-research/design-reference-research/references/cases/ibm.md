# IBM — enterprise marketing with flat boundaries

Case ID: `ibm`. Status: `document_reviewed_product_unverified`. Review date: 2026-11-14.

## Surface and evidence

IBM home, software/product and consulting marketing pages plus a community subdomain listed as a stylistic exception. The document references Carbon but is not a complete official Carbon specification.

The following relationships and values are third-party descriptions or claimed extractions, not independent measurements of the current site. Adaptation paragraphs are this project's proposals. Find the exact upstream path, fixed revision, original-file hash and byte size in the `ibm` row of the [metadata record](../catalog/catalog-02.csv).

## Useful visual relationships

- White canvas `#ffffff`, gray surface `#f4f4f4` and border `#e0e0e0` create bands and tiles. The source's feature-card primitive uses no radius and 24px padding; a new shadow is not required for every group.
- The analysis pairs IBM Blue `#0f62fe` with ink `#161616` and muted text `#525252`. The blue has an action role; content hierarchy is carried heavily by type and alignment.
- Source display text reaches 76px at weight 300, while body is 16px/400 and emphasized small text is 14px/600. Large light text and compact stronger emphasis serve different reading tasks.

## Transfer into the target product

For an enterprise marketing or editorial product page, compare flat bands and aligned content tiles before adding individually floating cards. A consistent boundary can group related content with fewer decorative layers. Map these roles into the established brand; square corners are an optional direction, not a universal enterprise requirement.

For a business application, the flat surface relationship may transfer, but use the existing component library and page methods for real tables, menus and form flows. Inspect first-party component documentation when the task specifically needs Carbon behavior.

## Evidence limits and completion needs

Known Gaps says actual product data tables, charts and menus were not extracted from the marketing pages, and the full dark theme was not captured. The responsive table and prose disagree about column-change boundaries and approximately 32px versus 42px mobile headings. These are unresolved source claims, not verified responsive rules. Keep community-subdomain styling separate.

When implementing, complete keyboard, focus, loading, error and narrow-screen behavior for the actual content, and check real contrast. Case values are not library-wide Token defaults or an accessibility pass.

## Pinned sources

[VoltAgent source analysis](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/ibm/DESIGN.md). Source locators: [Values and type](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/ibm/DESIGN.md#L6) · [Source-page scope](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/ibm/DESIGN.md#L284) · [Responsive disagreement](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/ibm/DESIGN.md#L510) · [Known gaps](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/ibm/DESIGN.md#L545). Source documentation is covered by the package's [MIT LICENSE](../../LICENSE); fonts and brand assets are not supplied.
