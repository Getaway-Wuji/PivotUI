# Async Feedback and Recovery

Read for requests, autosave, remote switches, filters, undo, or bulk actions. These are implementation recommendations; adapt to the target system's actual API.

## Minimum Complete Lifecycle

`idle/edited → pending → confirmed | recoverable-error | outcome-unknown`.

Local validation failure returns to editing without an invalid request. Enter confirmed only after the business response confirms success. A timeout or lost connection can mean outcome-unknown; it does not always mean the server did nothing.

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| Valid submission | edited → pending | Show progress in place; preserve content and action context | Duplicate guard; unrelated actions may continue |
| Confirmed success | pending → confirmed | Explain what was saved; brief success motion is optional | Update saved baseline; stay, close, or navigate as the task requires |
| Confirmed failure | pending → recoverable-error | Explain cause, affected object, and next step | Preserve input, selection, and failed objects; allow correction/retry |
| Timeout/disconnection with uncertain result | pending → outcome-unknown | Explain that outcome is unconfirmed; do not announce undo | Query status/reconcile through refresh; retry only when repetition is safe |
| User leaves or stops waiting | waiting → detached/cancel-requested | Distinguish stopping the wait from cancelling the business action | Cancellation needs server evidence; keep later outcomes traceable as appropriate |

Disabling a front-end button addresses only some duplicate input; the handler must also guard running state. Use idempotency/task identifiers supported by the backend for payment, creation, deletion, or batches. Retry in place must not accidentally create a second transaction. Do not amplify failure through unbounded automatic retries.

## Make Waiting and Outcomes Understandable

- Do not delay short requests to play a loader. For longer tasks show real stages or available progress; without a measurable total, use indeterminate progress instead of invented percentages.
- Initial loading may use a skeleton resembling the actual region. During refresh, normally preserve existing data and mark it as updating rather than clearing the page after each input.
- Lightweight success may use a success indicator, Toast, or status bar. Never use Toast for errors. Keep field errors inline; use Alert for persistent sync/network failures, associated with the affected region. Follow [overlay selection](../sub-skills/floating-components/SKILL.md); extending error-Toast duration cannot bypass its restriction.
- Keep low-interruption repeated-save/autosave feedback in a stable location. Do not pull focus away each time.

## Races and Drafts

| Problem | Invariant | Possible handling |
| --- | --- | --- |
| A is entered, then B, but A responds last | Displayed results correspond to the currently applied query | Cancel cancellable requests and reject stale responses by request ID/current query; cancellation alone does not prove a response cannot arrive |
| Editing continues while saving | Success confirms only the submitted version | Attach submitted snapshot/version; later changes stay unsaved; do not overwrite newer drafts with older returned values |
| Another person updates during editing | Neither person's changes are silently overwritten | Use actual API version conflicts to offer reload, comparison, or resubmission |
| Component unmounts or entity changes | Previous entity's result does not update the new entity | Bind entity key and request identity; clean up listeners/animations/timers; retain an outcome entry if needed |

Debouncing merges queries; it does not order server work. Use the project's delay or a locally adjustable value, allow immediate explicit submission, and account for input-method composition.

## Optimistic Updates, Undo, and Partial Failure

Use optimistic updates when reliable restoration is possible, conflicts are explainable, and error cost is acceptable. Record previous value and object identity. A rollback must undo only its own operation, not overwrite later successful changes. Prefer confirmation before high-impact or uncertain operations.

Specify whether undo cancels a delayed send or performs a compensating operation after submission. Match the UI deadline to the actual undo window; remove or explain expired actions. Reversing animation is not undo, and countdown completion does not prove server success.

Track successful, failed, unprocessed, and unknown results per item in bulk operations. Do not show only overall failure then rerun successful items; retry the safely repeatable subset. After deleting the current row, move focus to a sensible adjacent row or table entry and announce the actual result.

## Representative Walkthrough

Failed save in an editing Drawer: open and focus → submit valid draft → show saving and prevent duplicates → simulate failure response → keep Drawer open, input intact, and error readable → correct or retry → confirm success → close/return focus as appropriate. Also cover continued editing before completion and timeout after actual server submission. A timed checkmark animation cannot stand in for these branches.
