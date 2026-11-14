# Sources and adoption boundaries

Research date: 2026-11-14. This package contains original synthesized guidance and small illustrative snippets, not copies of third-party tutorials, UI kits, or product code.

## User-supplied material

Eight Chinese teaching images introduce percentage sizing, media queries, rem, Flex, Grid, viewport units, rpx, and framework grids. They are a conceptual starting point. No image shows a product's desktop/tablet/mobile sequence, live interaction, or measured layout transition. Original images and detailed intake stay in the authoring archive, outside this distribution.

Adopt the distinction between sizing, layout and conditional rules. Do not adopt the slides' root font reduction, sample breakpoints, fixed column counts, pure viewport font size or a blanket ranking of Grid over Flex. No original-image watermark, color or typography becomes a target-product preference. The rpx topic remains conditional on a supported platform; this release does not claim to have verified a mini-program implementation.

## Core implementation reference: Tailwind

The user selected [Tailwind CSS](https://tailwindcss.com/) as the central technical reference. Official documents were read for implementation semantics; the website was not audited across viewport sizes. The [Tailwind guide](tailwind.md) maps these facts to the module without requiring Tailwind in non-Tailwind projects.

- [Responsive design](https://tailwindcss.com/docs/responsive-design): base styles, viewport variants, ranges and container queries.
- [Theme variables](https://tailwindcss.com/docs/theme): configuration and shared variable scope.
- [States and capabilities](https://tailwindcss.com/docs/hover-focus-and-other-states): keyboard focus and pointer/hover conditions.
- [Upgrade guide](https://tailwindcss.com/docs/upgrade-guide): version and compatibility boundaries.
- [Source detection](https://tailwindcss.com/docs/detecting-classes-in-source-files): complete discoverable class names.
- [v3 screen configuration](https://v3.tailwindcss.com/docs/screens) and [official container-query plugin](https://github.com/tailwindlabs/tailwindcss-container-queries): legacy project adaptation.

The current documentation identifies v4.3 and the v3 archive v3.4.17; these are observed documentation labels, not assumptions about a user's installed dependency. Recheck relevant behavior when targeting another version.

## Supporting primary documentation

- [MDN container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries): ancestor containment and component-local space.
- [MDN overflow-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap): breaking otherwise unbreakable text.
- [W3C media queries](https://www.w3.org/TR/mediaqueries-4/#mf-interaction): input capabilities, including hybrid inputs.
- [W3C viewport units](https://www.w3.org/TR/css-values-4/#viewport-relative-lengths): small/large/dynamic viewports and keyboard limitations.
- [W3C reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) and [target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html): scoped accessibility checks and exceptions, not certification.

Content priority, state continuity, task-preserving region patterns, the four-part decision record, and integration checks are module design synthesis. They are not attributed as verbatim Tailwind or screenshot instructions. Document reading establishes neither successful compilation of example snippets nor a product's real-device behavior.
