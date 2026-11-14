# Choose changes from content

Read when planning layout transitions or choosing a CSS mechanism. Begin with the task, then choose a mechanism that preserves it; the eight supplied teaching images are technique prompts rather than a menu of mutually exclusive solutions.

## A useful decision record

| Field | Establish |
| --- | --- |
| Condition | Which content fails, at what measured viewport/container space or input condition? |
| Retain | Information, relationships, and operations essential to this task |
| Rearrange | Wrap, stack, reduce columns, relocate, disclose, or allow bounded scrolling |
| Continue | Where the next action lives, how users discover it, and which state persists |
| Evidence | Observed reference, measured behavior, or supplemental design; verification still needed |

For example: when a filter bar can no longer fit readable labels and usable controls, keep search and active-filter feedback visible, wrap controls or offer an explicitly named filter panel, and preserve values and results when it opens/closes. This is a proposed method, not an observation from the reference images.

## Choose a mechanism

| Mechanism | Good fit | Decision that it does not make for you |
| --- | --- | --- |
| Percentage / flexible width | Sharing available space; bounded page gutters | Maximum readable line length, minimum usable child size, or what should stack |
| Flex with wrapping or direction changes | A row/column of controls, navigation items, metadata | Wrapping is not automatic; inspect intrinsic minimum sizes and action labels |
| Grid | Aligned rows/columns, card collections, main/detail regions | Fixed column counts need a content-fit strategy; Grid is not universally better than Flex |
| Viewport media query | Page shell, navigation, or regions whose available space follows the viewport | A wide viewport can still contain a narrow component |
| Container size query | A reusable card, toolbar, or panel in different slots | Needs a suitable ancestor container and supported browser/runtime; query its descendants |
| `rem` / `em` | Font-relative sizing and coherent component proportions | Does not automatically make a layout responsive; shrinking root text scales away usability |
| Viewport units / bounded fluid values | Space genuinely related to viewport size | Pure `vw` text and fixed viewport-height content can fail zoom, long copy, or browser UI |
| Framework grid/utilities | Expressing the chosen layout in the existing stack | Class names, breakpoints, and plugin support vary with framework/version |
| Platform units such as `rpx` | A runtime that explicitly supports them | Not standard browser CSS; inspect that platform's current rules before implementation |

Prefer intrinsic wrapping/fluid sizing when they solve the problem without a transition. Combine methods when they solve different dimensions. Do not introduce JavaScript resize logic for behavior already expressed clearly in CSS; use runtime measurement only for needs such as a chart's resize API.

## Locate transitions

Use existing project conventions first, including container and component variants. With no established threshold, resize using realistic long labels, languages, data volumes, and zoom. Locate the point where the current arrangement fails, identify its cause, then switch before the failure. Record the rationale and the scope. Do not adopt the teaching slides' 600/1024 values or Tailwind defaults as device requirements.

Unprefixed narrow layouts plus minimum-width enhancements often simplify new work; preserve a sound existing approach in local repairs. Avoid media-query gaps such as one range ending at 600px and another starting at 601px: fractional viewport widths exist. Use a base plus minimum-width override, or complementary range syntax supported by the project.

Use available content width, including gutters and sidebars, when estimating columns. Bound reading lines and media width on large displays without stretching every region to fill space. A heading may change size within the adopted type scale, but important text must remain readable when enlarged. Keep a single meaningful content order; CSS `order`, grid placement, and duplicated desktop/mobile controls must not create misleading focus order or duplicate active form IDs.

## Small implementation patterns

These declarations illustrate mechanics, not product tokens. Reuse actual project values and selectors; check browser support before adopting them.

```css
/* Allow a nested layout item to shrink; wrap only text that may break. */
.content-slot { min-inline-size: 0; }
.long-reference { overflow-wrap: anywhere; }
.media { max-inline-size: 100%; block-size: auto; }

/* Illustrative 16rem card minimum and 1rem gap, not library defaults. */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: 1rem;
}
```

Use `minmax(0, 1fr)` for a flexible track that should be allowed below its content's automatic minimum, together with an explicit content wrapping/scroll strategy. A zero minimum alone does not repair an unbreakable child. Choose a meaningful minimum for comparison-heavy charts/tables and a local scroll alternative rather than squeezing them illegibly.
