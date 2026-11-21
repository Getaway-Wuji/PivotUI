# Actions, Edge States, and Return Continuity

## Action safety and permissions

- **Read vs write gating:** Hide or disable unauthorized actions with clear explanation according to project policy; never rely on UI hiding alone to claim backend security.
- **Destructive actions:** Irreversible delete/archive requires `Modal` confirmation stating the exact record name/ID and impact; low-risk local toggles may use `Popconfirm` (`floating-components`).
- **Async state protection:** Disable duplicate clicks during submission, keep the current record visible if an action fails, and render persistent errors in an `Alert` (never rely on ephemeral `Toast` for errors).

## Edge states

| Condition | Required UI behavior |
| --- | --- |
| Loading | Preserve shell/header frame; show structured skeleton or loading indicator without layout shift |
| Record not found / deleted (404) | Clear explanation naming the requested ID + safe link back to the parent list |
| Insufficient permission (403) | Explain access boundary without leaking sensitive fields + safe navigation exit |
| Partial related-panel failure | Render the primary record normally; show local error + retry control inside only the failed panel |
| Stale record / edit conflict | Warn before overwriting; let the user reload latest state or review conflicting fields |

## Return continuity contract

- Read from the same authoritative record store as the parent list so edits immediately reflect in both detail and list views.
- When returning to the source list (via back button or browser Back), delegate restoration to the agreed return coordinator: re-apply saved query/filters/page, handle cases where the edited record no longer matches the source filter (clamp valid page, explain change, move focus safely instead of focusing a missing row).
- Never assume `window` is the scroll container; restore scroll inside the shell's actual scroll host.

## Verification checklist

- Direct deep link to valid ID and invalid ID both resolve cleanly without broken navigation.
- Edit → save → return to list reflects updated data and restores filter/page/position accurately.
- Narrow screens stack header actions and description groups cleanly without horizontal overflow.
- Keyboard traversal covers return link, primary actions, tabs, and confirmation dialogs with visible focus.
