# Verification and handoff

Read when implementing or reviewing a shell. Choose checks relevant to the change and record the actual environment and outcomes.

## Runtime checks

| Check | Exercise | Passing evidence |
| --- | --- | --- |
| Location | Open a list, deep detail/edit link, and browser Back/Forward | Content, active ancestor, expanded path, breadcrumb and title agree; direct entry has a valid return |
| Return state | Filter a list, scroll, open a record, edit/cancel, return | Agreed filter/page/selection/scroll survive; focus returns by stable identity or a documented fallback |
| Long labels | Long translated navigation names, page title, breadcrumb | Labels and actions remain reachable; text does not push content outside its region |
| Keyboard | Tab/Shift+Tab, Enter/Space disclosures, content entry | Visible focus follows meaningful order; disclosure and navigation are distinct; hidden entries cannot receive focus |
| Collapse | Collapse/expand groups and sidebar, including while focus is inside | No hidden focus, lost route, or inaccessible destination; current remains distinct from hover/focus |
| Narrow and short | Relevant widths, around the transition, and reduced height | Navigation is available, controls fit, last items are reachable; resizing preserves work and resolves temporary navigation correctly |
| Scroll and layers | Scroll main and long sidebar independently; reach first/last actions | Header/sidebar remain as intended; no competing page scroll or obscured focus; local overflow is contained |
| Contrast | Inspect rendered foreground/background pairs, including muted, selected and hover text | Record measured ratios; normal text at least 4.5:1, large text at least 3:1 under WCAG AA; focus and controls remain distinguishable |

Use the product's accessibility target when stricter. The contrast thresholds follow [WCAG contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). Check actual backgrounds rather than token names alone.

For a specification-only task, review the decisions and executable acceptance criteria; do not report browser checks as passed. Distinguish automated behavior checks, visual inspection, real-device testing, and assistive-technology testing.

## Handoff

A compact record is enough:
- Chosen composition and conditions; persistent versus route-specific regions.
- Route matching, breadcrumb/title/action metadata and return contract.
- Content width/inset, scroll owners, fixed/sticky layers, narrow-screen transition.
- Reused component/token source and the one implementation owner per region.
- Reference evidence, estimates and supplemental choices.
- Changed files, actual checks, unresolved issues and unrun environments.

Page owners consume the agreed content and action slots; they should not recreate the shell or wrap its main scroller in another full-height page scroller. Specialists return scoped requirements or fixes to the named owner. Keep original research and demo evidence in authoring records, outside a standalone skill package.
