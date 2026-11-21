---
name: form-interaction
description: Handle states and feedback during input, selection, validation, filtering, and submission; protect drafts and define error location, async saving, and continuation after failure.
metadata:
  version: 1.1.0
  tags: [form, input, validation, submit, draft, filter, select]
---

# Form Interaction

This is an on-demand submodule of `interaction-design`. Inherit the scope, tokens, evidence labels, and optional project conventions established by the [root entry](../../SKILL.md). Do not reload it when these agreements are available. When entering directly without them, read only “Scope and Existing Decisions.”

Own fields, selection controls, filters, validation, and input flows. Do not rearrange the page or change business validation rules. Button states belong to [button interaction](../button-interaction/SKILL.md). These are design and implementation recommendations; behavior not established by screenshots remains a proposed addition.

## Field and Submission Behavior

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| Focus, input, or leaving a field | empty / edited; validate according to policy | Label stays identifiable; instructions are associated with the control | Correct relevant errors while preserving other input |
| Invalid content is submitted | edited → invalid | Nearby reason and remedy; linked summary for multiple errors if useful | Guide focus to the first relevant error or summary; resubmit after correction |
| Valid submission | edited → pending | Identify the object being saved and progress in place; retain draft | Prevent duplicates; success updates the saved baseline, failure preserves draft |
| Editing continues during a request | pending and newer draft coexist | Distinguish the submitted version from new edits | Old response confirms only its submitted snapshot and cannot overwrite newer draft |
| Explicit failure or unknown outcome arrives | pending → error / outcome-unknown | Nearby field errors; persistent important overall problems | Correct, query the outcome, or retry safely; do not clear input or claim success |

Use [async behavior and recovery](../../references/async-recovery.md) for request identity, stale responses, continued editing, partial failures, and cancellation. Do not define a separate request protocol here.

## Validation and Feedback Containers

Do not repeatedly flag an error while the user is still completing a format. Validate required content on submission; update already-displayed errors as they are corrected. During input-method composition, do not treat Enter as submission or unfinished composition text as a final query.

Error copy identifies the field, cause, and next action. Associate it through existing component APIs or `aria-invalid` and `aria-describedby`. Async outcomes must not repeatedly steal typing focus. Announce overall feedback as needed without making the entire page a high-priority live region. See [WAI form notifications](https://www.w3.org/WAI/tutorials/forms/notifications/).

Follow [floating-component selection](../floating-components/SKILL.md): Tooltip can supplement transient explanations, while required conditions remain easy to find. Toast is for lightweight outcomes, never errors or actionable warnings. Persistent Alert handles overall sync/network failures; field errors stay nearby. Prefer inline or existing-page forms for simple input; the presence of fields does not justify Drawer. The page lead owns full-screen tasks. Modal is not for small informational displays or low-risk simple confirmation; irreversible confirmation follows the overlay module's risk-first rule.

## Selection and Range Controls

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| Switch/checkbox activates | checked changes; remote saving has separate pending state | Name, position, and state semantics agree | Allow reversing selection; remote failure rolls back or retains unsaved value with explanation |
| Radio/select navigation and selection | Candidate focus → committed value | Distinguish navigated candidate from selected value | Esc closes candidates without clearing input; preserve the component's commit policy |
| Slider drag, arrow key, or numeric input | Value changes within range and step | Track, thumb, readout, and unit use one actual value | Specify preview/commit timing and cancellation; maintain consistent boundary values |

Prefer existing or native controls. Custom controls expose a name, range, step, and current value; continuous sliders support appropriate arrows and Home/End. Searchable selectors distinguish input text, candidate focus, and selected value. Do not bind page-wide arrow keys to one list. See [APG Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/).

Determine whether segmented options represent a radio value, same-page tabs, or route navigation. The latter two follow [navigation interaction](../navigation-interaction/SKILL.md); similar appearance does not justify the wrong keyboard model.

## Filters and Results

Establish immediate application versus an explicit Apply action: `draft → applied → querying → result/error`. Current input, applied conditions, and displayed results must correspond. Clearing/resetting needs a defined scope. Debouncing reduces request frequency but cannot resolve out-of-order responses; reject stale responses by request identity.

During refresh, normally retain recent results and mark them as updating. On failure retain conditions and old content, explaining that results are not updated. Distinguish first-use emptiness, no filter matches, loading failure, and lack of permission, each with a suitable next action. Result-count updates normally preserve filter input focus and use a stable status area, rather than automatically moving into the table. The original page owner continues integrating table selection, sorting, and bulk actions.

## Delivery Checks

- Keyboard input, selection, submission, first-error location, and correction work; errors are readable and properly associated.
- Input survives failure. Unknown outcomes are not blindly retried as ordinary failures. Old responses cannot overwrite edits made during submission.
- Conditions and results correspond; cancel/clear scope is explicit; input-method composition cannot accidentally submit.
- Check actual form size, long error copy, touch, and reduced motion. Report scenario walkthroughs separately from real execution.
