# Kraken — limited white-and-purple reference

Case ID: `kraken`. Status: `document_reviewed_product_unverified`. Review date: 2026-11-14.

## Surface and evidence

An unspecified white-background website with purple emphasis; concrete source pages are not listed. The repository summary mentions a dark trading UI, but this document does not establish that scope.

The following relationships and values are third-party descriptions or claimed extractions, not independent measurements of the current site. Adaptation paragraphs are this project's proposals. Find the exact upstream path, fixed revision, original-file hash and byte size in the `kraken` row of the [metadata record](../catalog/catalog-02.csv).

## Useful visual relationships

- Source primary purple `#7132f5` sits on white with ink `#101114` and cool gray `#686b82`. Purple variants are assigned to filled, outlined and subtle controls.
- A filled candidate has 13px 16px padding and 12px radius; outlined controls keep purple text/border on white. The white-button description instead uses 10px radius, creating a source inconsistency.
- Success badges use a translucent green background with dark green `#026b3f` text, separated from purple action emphasis. Display and body have distinct type roles; the source lists 48px/700 display and 16px/400 body.

## Transfer into the target product

Use as a narrow comparison for action and badge roles when the requested direction calls for purple or the user names Kraken. Keep status and action semantics separate, and map to existing tokens. If the target brand is not purple, borrow the role distinction rather than importing the hue.

Define the target's filled, outlined and subtle button hierarchy with coherent geometry, then verify visible states and actual content. For a generic dense trading dashboard, use the established dashboard/list methods; this card lacks task structure and trading interaction evidence.

## Evidence limits and completion needs

The short document's responsive section is only a breakpoint list, with no actual reflow rules. A general rule says all buttons use 12px although the white-button candidate says 10px. Neither is a verified universal requirement. Font resources, keyboard/focus, loading/error behavior and accessible combinations require target-product decisions and checks.

When implementing, complete keyboard, focus, loading, error and narrow-screen behavior for the actual content, and check real contrast. Case values are not library-wide Token defaults or an accessibility pass.

## Pinned sources

[VoltAgent source analysis](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/kraken/DESIGN.md). Source locators: [Inspired scope and palette](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/kraken/DESIGN.md#L1) · [Type hierarchy](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/kraken/DESIGN.md#L34) · [White-button geometry](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/kraken/DESIGN.md#L77) · [Rules and breakpoint-only coverage](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/kraken/DESIGN.md#L103). Source documentation is covered by the package's [MIT LICENSE](../../LICENSE); fonts and brand assets are not supplied.
