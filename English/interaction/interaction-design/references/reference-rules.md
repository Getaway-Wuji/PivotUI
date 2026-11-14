# Rules Distilled from the Initial References

Research date: 2026-11-14. Source: 34 static PNGs supplied by the user. R identifiers correspond to per-image research records; this file works independently of originals and the research directory. **This set provides no actual observation of continuous interaction, keyboard behavior, async requests, or performance.**

## Evidence Summary

| Reference group | Facts visible in images | Author descriptions inside images; not runtime-verified |
| --- | --- | --- |
| R01, R05, R11: navigation and docks | Current-item background, floating icons, labels/location markers | Following pill, adjacent-item magnification, returning to current on pointer leave |
| R02, R08–R10, R12, R15: local enhancements | Card edges, view indicator, buttons/pills, local color inversion; R15 has no preview | Spotlight, magnetism, cursor label, widening, circular spread, hover image following |
| R03–R04, R26, R28: expansion and exit | Overlapping cards, menu icon, bottom panel; R04 shows only Calendar page | In-place expansion, command-panel shortcut, icon-to-cross transform, Drawer pause |
| R13–R14, R22–R23: values | Stops, track fill, value bubble, bar readout, metric numbers | Snapping, pointer coordination, shared timing, decelerating numbers |
| R17–R21: press and result | Pill button, left-positioned switch thumb, ripple-colored block, heart, success check | Springback, stretching, spread, particles, circle-then-check; no particles visible in R20 |
| R24–R25, R27: content state | Skeleton blocks, card front, stacked edges | Equal-size replacement, flip, removing front card |
| R06, R16: visual context | Color/style samples, dark page, moon icon | Specific visual recipes and circular theme transition |
| R07, R29–R34: presentation narrative | Product imagery/text, image strips, fan, curved surface, wall, ribbon, depth arrangements | Sticky scroll narrative, opposing strips, flip, cylinder drag, ring-wall switching, twisted ring, tunnel |

## Reusable Behavior Chains

**The entire table below consists of editorial distillation and proposed additions.** It adopts described intent and adds input, state authority, and recovery; do not mark the whole chain as observed. React Bits names are search candidates, not claims of exact equivalence or execution.

| Pattern and applicability | Trigger | State change | User feedback | Exit or recovery | Candidates to inspect |
| --- | --- | --- | --- | --- | --- |
| Current-item marker: navigation/radio selection | Click selects; hover/focus can explore temporarily | Separate current from hover/focus | Marker follows actual current item; temporary item may be lightly emphasized | Leave/blur restores current; without current, clear temporary state | Pill Nav, Rubber Segment; identify navigation versus radio semantics first |
| Local emphasis: a few clear entry points | Pointer enters/approaches; keyboard focus has equivalent cue | Local brightness, edge, or slight movement | Stable text, focus, and hit area | Restore on leave; touch/reduced motion retain ordinary entry | Glare Hover, Magnet, Specular Button |
| Press feedback: immediate input acknowledgment | Press followed by valid activation | pressed → resting; separate business state | Press feel or local ripple, optionally from input point | Clear on release/cancel; do not wait for effect completion to execute | Click Spark, Sling Button; existing controls may supply ripple |
| Binary setting | Click/Space | checked changes; remote pending separate | Position, name, and semantics express state | Reverse toggle; restore/explain remote failure under policy | Squish Switch, Spring Check |
| Value control | Drag, arrows, direct input | One actual value updates track, thumb, readout | Consistent units, steps, and associated output | Define preview/commit, cancellation, and boundary values | Wake Slider, Scrub Field, Comet Dial |
| Outcome confirmation | Actual action succeeds/fails | pending → confirmed/error | Readable result alongside graphics | Continue after success; preserve content/retry after failure | Status Mark can represent outcomes; Swipe Toast only lightweight success/information; errors inline/Alert; animation cannot create success |
| Data waiting | Request starts before content is ready | loading → content/empty/error | Appropriate placeholder dimensions; refresh can preserve old data | Stop waiting on arrival; provide recovery after failure | Lattice Loader is only a waiting-visual candidate; reuse project skeleton components |
| Menu/Drawer/detail expansion | Visible entry or already-supported shortcut | closed → open; determine modality | Identifiable heading, expanded state, focus | Visible close, applicable Esc, draft protection, sensible focus return | Branched Menu, Staggered Menu are candidates only; inspect semantics/focus first |
| Flipping/stacked content | Explicit switch or next/previous; drag is an enhancement | Displayed item changes; preserve identity | Current face/item is clear and readable | Return is possible; hidden face unfocusable; deletion needs separate recovery | Flip Card, Stack |
| Supplementary preview | hover/focus or explicit preview entry | Previewed object changes | Supplementary image in stable position, without obscuring target or intercepting clicks | Clear on blur/exit; original item remains openable if resource fails | Image Trail is only a visual candidate; ordinary preview may reuse existing overlay |
| Theme switch | User switches theme | Actual theme value remains immediately consistent | Icon/name agree; spread is optional | Switch directly without motion support or with reduced motion; rapid switching settles on final state | Prefer existing theme mechanism; no forced component pairing |
| Image strips/spatial display | Page lead first chooses presentation scope; then scroll/switch/drag | Current work or presentation form changes | Identity and reading order remain traceable | Normal scroll exit, pause, ordinary grid/list, static fallback | Circular Carousel, Circular Gallery, Dome Gallery, Infinite Menu; performance evaluation required |

## Adoption Boundaries

- Overlay selection follows the user's later explicit [applicability/exclusion table](../sub-skills/floating-components/SKILL.md). Older Drawer, command-panel, or success examples do not fit every task and do not justify simple-form Drawers.
- Glass, orange/purple colors, radii, shadows, and motion values are local source recipes. This skill inherits target-product tokens and establishes no new global brand.
- Author-provided overshoot, angles, dimensions, delays, and keyframe percentages were not runtime-verified here. In particular, a Drawer pause in a demo loop must not become mandatory waiting after every user action.
- High-frequency business operations prioritize clear state and reliable recovery; low-risk favorites may use brief celebration. The page lead owns complex spatial-gallery layout/content; this module adds input, stopping, fallback, and performance constraints.
- New references may establish dynamic evidence. Update specific stages under the [evidence rules](evidence.md); one animation does not verify keyboard, requests, or all devices.
