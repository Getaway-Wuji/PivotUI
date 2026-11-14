# States and Table Operations

General states and table operations live here. Detailed component rules are in on-demand submodules:

- [Floating components](../sub-skills/floating-components/SKILL.md): selection and full flows for Tooltip, Toast, Alert, Modal, Popconfirm, and Drawer.
- [Button interaction](../sub-skills/button-interaction/SKILL.md): press, focus, disabled, waiting, and action feedback.
- [Form interaction](../sub-skills/form-interaction/SKILL.md): input, validation, selection, range controls, and filters.
- [Navigation interaction](../sub-skills/navigation-interaction/SKILL.md): sidebar, breadcrumbs, current item, and command menus.

These are design/implementation recommendations. See [initial reference rules](reference-rules.md) for screenshot evidence and the [integration guide](react-bits.md) for inspected React Bits capabilities.

## Choose Necessary States

Hover, focus, and pressed describe input feedback; selected, checked, and expanded describe persistent states; pending and error describe business lifecycles. They may coexist. Do not overload one `active` value with all meanings.

| Operation | States to express | Normally unnecessary |
| --- | --- | --- |
| Immediate local action | Availability, focus, press, actual outcome | Artificial waiting or a dialog after every success |
| Selection/switch | Unselected/selected; indeterminate or unavailable if applicable | Treating a brief press as selection |
| Remote change | Available, pending, result, continuation after failure | Declaring success because animation ended |
| Opening an overlay | Closed/open, focus location, destination after close | Inferring modality from backdrop styling |
| Pure display | Visible content; expansion or pause if needed | Focus/button semantics without an action purpose |

## Tables and Row Actions

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| Applied filter changes | Current query starts updating | Conditions, result count, and loading state are identifiable | On failure retain conditions/recent results and mark stale; errors inline/Alert, never Toast |
| Sort activates | Direction and displayed ordering change | Column label agrees with direction; `aria-sort` where appropriate | Further toggles follow project convention; focus stays on the same header |
| Row/select-all checkbox activates | Selection set changes | Count and current-page/all-matching scope are explicit; partial selection has mixed state | Allow deselection; define persistence/reset across pagination and filtering |
| Row command/bulk submission | Affected rows enter pending | Associate feedback by stable row identity without freezing unrelated rows | Explain partial failure per item and retain failed set for retry |

The form submodule owns filter input and draft/applied relationships; navigation owns command-menu keyboard/dismissal; floating components owns confirmation and containers. For example, bulk permanent deletion first uses irreversible Modal confirmation; an action's proximity to a row does not justify Popconfirm.

Hover may enhance row actions, but keyboard focus and touch must still discover and operate them. Preserve native table semantics unless actual composite-grid behavior requires a grid keyboard model. Maintain focus/selection by stable IDs after filtering, sorting, or deleting; indices must not point to different rows. Result refresh normally retains input focus and announces count through a status region.

Undo must correspond to still-available business capability. Optimistic motion differs from server outcomes; see [async behavior and recovery](async-recovery.md).
