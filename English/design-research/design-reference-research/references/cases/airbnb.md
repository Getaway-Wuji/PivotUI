# Airbnb — marketplace search and detail decisions

Case ID: `airbnb`. Status: `document_reviewed_product_unverified`. Review date: 2026-11-14.

## Surface and evidence

Consumer marketplace browsing/search, property cards, property details and booking area, date selection and forms. This is the most task-relevant initial case for consumer marketplace layouts, but no live booking flow was independently tested.

The following relationships and values are third-party descriptions or claimed extractions, not independent measurements of the current site. Adaptation paragraphs are this project's proposals. Find the exact upstream path, fixed revision, original-file hash and byte size in the `airbnb` row of the [metadata record](../catalog/catalog-01.csv).

## Useful visual relationships

- Photography is a primary comparison surface, paired with compact title, price and contextual information. The source separates the detailed reading area from an adjacent booking/action region rather than distributing booking controls throughout the description.
- It lists primary `#ff385c`, ink `#222222`, muted text `#6a6a6a`, white canvas and soft surface `#f7f7f7`. The useful distinction is action emphasis against mostly neutral comparison content.
- Title roles include 16px/600 and 16px/500 beside 16px body and 14px smaller text. Its primary-button primitive lists a 48px height with 14px 24px padding. These are source candidates, not a guarantee of every content/font combination fitting.

## Transfer into the target product

For marketplace search, decide which fields change the user's result set and keep that search scope understandable. Pair images with enough comparable information to make the next choice; do not hide price meaning or key constraints to preserve a clean card.

For a detail page, keep reading and the primary decision adjacent on wide layouts. A narrow-layout action area can be a candidate, but define its information, scrolling, focus and safe-area behavior in the target project. The existing form/interaction owner must design validation, asynchronous price changes, loading and recovery. Test realistic Chinese names, prices and date labels.

## Evidence limits and completion needs

Known Gaps says precise hover extraction was unreliable, loading was not observed and full input-error styling was not captured; maps and other details also remain incomplete. The source includes a no-hover policy that is not adopted here. Its introductory radius description differs from the rounded-token table, so select a coherent target radius rather than copying the inconsistency. Documented breakpoint and touch assertions are not runtime checks.

When implementing, complete keyboard, focus, loading, error and narrow-screen behavior for the actual content, and check real contrast. Case values are not library-wide Token defaults or an accessibility pass.

## Pinned sources

[VoltAgent source analysis](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/airbnb/DESIGN.md). Source locators: [Values and primitives](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/airbnb/DESIGN.md#L6) · [Marketplace and booking layout](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/airbnb/DESIGN.md#L420) · [Responsive candidates](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/airbnb/DESIGN.md#L518) · [Known gaps](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/airbnb/DESIGN.md#L539). Source documentation is covered by the package's [MIT LICENSE](../../LICENSE); fonts and brand assets are not supplied.
