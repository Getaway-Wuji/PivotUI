# Handoff and verification

Read when coordinating a responsive change or checking results. Reuse the current task record; a small local fix needs only the relevant decisions.

## Contract with the lead

| Input / output | Content |
| --- | --- |
| Receive | Region and user goal; visual direction and token source; components; target devices, browser range and input expectations; existing breakpoints; reference purpose; allowed changes |
| Propose before layout | Conditions and priorities; retained content; rearrangement; continuing operations; observed versus supplemental decisions |
| Coordinate during implementation | Component variants and affected callers to `component-system`; touch, keyboard, focus, hover and state transitions to `interaction-design`; one integrator per region |
| Return afterward | Changed files/regions, chosen conditions, preserved state and access paths, verification evidence, remaining limitations, and any shared changes needing consolidation |

The page lead owns business priorities; responsive work translates them into usable arrangements. Keep shared token proposals with the orchestrator/global style owner. Do not silently create another breakpoint or token source. When using the module independently, perform these roles within the permitted scope and use the [portable conventions](foundations.md) as needed. Missing specialists do not block ordinary work.

For discovery, resolve the actual `responsive-design` entry. With the cluster MCP, catalog metadata before loading the entry and selected linked resources; without it, read the declared file location. A listed candidate is not proof of availability. This package needs no mandatory dependency on the rest of the cluster or additional registration format.

## Check an actual interface

Choose checks for the affected region, not a fixed list of every device:

1. Cover agreed target widths and heights. For every implemented layout transition, inspect just below, at, and just above its actual threshold, plus a representative width within each resulting layout. If behavior depends on a container, vary that container independently of viewport width.
2. Try realistic long headings, translated labels, URLs, numbers, empty/missing values, and relevant loading/error states. Verify text enlargement and browser zoom where supported. Preserve meaningful source/reading/focus order after stacking.
3. Check both accidental page overflow and intended local scrolling. Confirm full values, essential columns, chart meanings and moved controls remain reachable. Inspect fixed/sticky regions at short heights and after content expands.
4. Complete key operations with keyboard and available pointing input: open/close navigation, filter, inspect details, select rows, open/close overlays, submit and recover from errors as applicable. Resize while a panel is open or a form/selection is active; verify retained state and a valid focus location.
5. Record actual environment, viewport/container dimensions, threshold, content/state, action and observed result. Capture relevant evidence, report failures and fix within scope, then repeat only affected checks.

When CSS `order`, Grid placement, breakpoint hiding or alternate navigation copies change a region, walk Tab and Shift+Tab through it in the layouts before and after the transition. Compare the focus path with meaningful reading order, visual grouping and task sequence; check that hidden copies cannot receive focus or appear as duplicate controls in accessibility navigation. Cross the breakpoint while focus is in the affected region and confirm that it remains on a visible, usable element or moves to an appropriate destination. A Modal focus test does not cover surrounding navigation. Geometric order need not match DOM order position for position; fix misleading or unusable sequences without requiring DOM rearrangement as the only solution. Unchanged regions do not acquire a site-wide review requirement.

For a reflow accessibility check, WCAG 2.2 SC 1.4.10 uses 320 CSS pixels for vertically scrolling content (for example, a 1280-CSS-pixel starting width at 400% zoom). Necessary two-dimensional regions have exceptions; that does not exempt their surrounding page or remove content access obligations. Treat this as a test condition, not a design breakpoint or a full accessibility certification. [Reflow explanation](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).

## Report evidence accurately

| Evidence | What it establishes | What it does not establish |
| --- | --- | --- |
| Rule review / scenario walkthrough | Whether instructions guide the required decisions and handoff | Rendered behavior or browser compatibility |
| Build / generated CSS inspection | Syntax and generated rule availability for that toolchain | Usable layout or successful interaction |
| Browser viewport checks | Observed rendering and exercised interactions at recorded settings | Physical touch accuracy, device keyboard or real mobile browser chrome |
| Browser touch emulation | The emulated events/settings actually exercised | Real-device ergonomics or OS/browser behavior |
| Real device checks | Recorded device, OS/browser, orientation and actual operations | Every other device and browser |

When only authoring a skill, inspect rules, links and representative behavior decisions; do not claim browser or device validation. When no runnable page is provided, mark intended widths and interaction checks as planned. If implementation is requested and a runnable target exists, inspect it rather than stopping at a checklist.

## Representative authoring checks

Use three task families to exercise the module: a public-site layout with only a desktop reference; a business table/chart with comparison and bulk operations; a local overflow repair in a narrow container with long content. Evaluate whether the skill keeps scope, visual inheritance, task reachability, evidence boundaries and a concrete integration owner. Use independent requests rather than checking only for the presence of prescribed phrases. Store executed outcomes in authoring records, not as runtime dependencies.
