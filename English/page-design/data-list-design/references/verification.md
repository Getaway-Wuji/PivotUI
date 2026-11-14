# Verification and handoff

Choose checks for the delivered scope. A design specification can provide an executable acceptance plan, but cannot claim browser results. For an implementation, exercise meaningful flows with realistic synthetic records and record viewport, browser, actions and outcomes. Keep authoring demos and raw evidence outside the distributed skill.

| Check | Exercise and observable result |
| --- | --- |
| Long content | Long mixed-language names/IDs, missing values, large numbers; full values and actions remain reachable without overlap |
| Query states | Apply multiple filters, reset, no matches and failed/denied load; correct state, retained inputs and recovery path |
| Columns/views | Hide/reset columns and switch relevant views; identity/detail route survives, permissions are respected, persistence matches the contract |
| Selection scope | Select a page, change page, explicitly select all matches if supported, exclude one, change filters; labels and affected IDs agree |
| Partial failure | Submit mixed outcomes; persistent reasons, correct counts, no success reapplication, only retryable failures retried |
| Detail return | Leave a filtered later page at a known scroll/focus anchor; return by UI and browser Back; query/page/size/order and useful position recover |
| Changed data | Delete/deny the origin record or empty the last page; valid fallback and clear explanation, no phantom selection |
| Keyboard | Complete filters, selection, settings, confirmation and detail return; visible logical focus, no trap outside a true modal, focus survives removed controls |
| Actual contrast | Inspect computed foregrounds and effective backgrounds for labels, values, links, status and selected/error states; use WCAG AA text targets (4.5:1 normal, 3:1 qualifying large text) and record measured pairs |
| Narrow fields | At relevant small widths and zoom, reach every required field and action with labels; local scrolling/disclosure works without page-wide clipping |
| Export | Verify the file/job contents match named scope, fields and permissions; no synthetic completion represented as real remote work |

Contrast criteria reference: [WCAG contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). Computed checks alone do not establish all accessibility: visually inspect overlap, focus visibility, disabled/status contexts and actual rendering. Record untested assistive technology, physical devices, backend behavior or performance as untested.

For handoff, return the list-region owner, inherited token/component sources, query/selection/job/return contracts, supplemental decisions, changed files and actual results. Explain shared component or token proposals without silently expanding their scope. In this authoring workspace the module record is `design-system/modules/data-list-design.md`; in other projects use their own record convention. That workspace path is not a runtime dependency.
