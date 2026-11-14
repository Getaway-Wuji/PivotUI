# Input capabilities, height, and overflow

Read for local repairs or when layout changes alter access to controls. Width and input capability are independent: a narrow desktop window can use a keyboard/mouse, and a large screen can be touch-enabled.

## Keep operations available

Keep meaningful actions exposed through an explicit control and visible keyboard focus. Hover may add preview or emphasis but cannot be the sole way to reveal required information or activate an operation. `hover`/`pointer` describe the primary input; `any-hover`/`any-pointer` consider available inputs. Mixed devices may have both coarse and fine pointers. Do not infer keyboard availability or remove keyboard access from these queries. [Input-feature semantics](https://www.w3.org/TR/mediaqueries-4/#mf-interaction).

Use existing touch targets and spacing or purposefully enlarge the hit area where inaccurate pointing is likely. Keep adjacent targets distinguishable and prevent transparent hit regions overlapping. For projects checking WCAG 2.2 AA, SC 2.5.8 specifies a 24-by-24 CSS-pixel target or its stated exceptions, including spacing; this is not a universal recommended button size. [Target-size criterion](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

On responsive disclosure, distinguish persistent selected/open state from incidental hover. Preserve a valid focus destination when the current control disappears at a transition. Keep inactive duplicated controls out of focus and accessibility navigation. Coordinate Modal/Drawer focus management, Escape behavior, and return focus with the existing interaction owner. Do not replace labels with unexplained icons solely to save width.

## Diagnose overflow at its source

1. Reproduce the issue with actual content and the failing viewport or container. Determine whether overflow belongs to the page, a component, or an intended scroll region.
2. Inspect the first element exceeding its available size and its ancestor sizing chain: fixed/minimum width, flex/grid automatic minimum, `white-space`, long strings, media dimensions, padding plus width, `100vw`, transforms, or positioned decoration. Compare bounds and scroll dimensions; intentionally off-canvas/hidden elements may be false positives.
3. Fix the smallest responsible scope. Often a flex/grid item needs `min-width: 0` / `min-inline-size: 0`, a flexible track needs `minmax(0, 1fr)`, or a child needs wrapping or its own bounded scroll. Trace nested ancestors instead of adding a random breakpoint.
4. Wrap ordinary content. Apply `overflow-wrap: anywhere` selectively to unbreakable references; avoid blanket `word-break: break-all` that harms normal reading. Constrain media and preserve its aspect ratio. [Wrapping behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap).
5. For content whose meaning depends on width, use a local scroll region with a clear name/instruction when needed. Verify horizontal access by pointer, touch, and keyboard; add focusability if the target browser needs it, rather than making every wrapper a tab stop. Keep focus outlines and open menus from being clipped by the new scroll boundary.
6. Recheck the failing case, adjacent layout states, content completeness, and main operation. An absence of body overflow alone is not success.

Use clipping only for intentionally decorative overflow whose crop does not remove meaning, focus or hit targets. Do not apply `overflow-x: hidden` to the whole site as a repair. A deliberate Modal body scroll lock is a different behavior; it must be released reliably.

## Viewport height and content growth

Treat height as well as width: landscape orientation, browser controls, zoom, expanded errors and the on-screen keyboard can leave little usable content space. `svh` represents the small viewport, `lvh` the large viewport, and `dvh` the dynamic viewport; choose based on whether stable fit or tracking changing browser UI serves the task. Dynamic units are not a universal fix for the virtual keyboard, which may overlay content without changing them. [Viewport-unit definitions and caveats](https://www.w3.org/TR/css-values-4/#viewport-relative-lengths).

Prefer content-driven height or a suitable minimum height over a rigid full-height box when content can grow. Keep a scroll path to focused fields and submit actions. Test the project's actual browser/keyboard behavior; safe-area insets address device/UI edges, not every keyboard occlusion. Add fallbacks for the supported browser range and retain user zoom. Do not set restrictive viewport zoom flags to make a layout appear stable.
