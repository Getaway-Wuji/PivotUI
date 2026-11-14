# Original Interaction Templates

Copy the relevant files only when the target project lacks suitable components or needs behavior adaptation. Prefer existing components. These are unstyled React + TypeScript starting points, not a full component library; they include no React Bits source or default brand. Non-React projects keep their existing stack and implement the rules there.

## Files and Interfaces

- [AsyncActionButton.tsx](react/AsyncActionButton.tsx): native `type="button"`; `onAction` returns the actual operation Promise. A synchronous guard prevents repeated activation of one instance before the next render. `busy` accepts external request state; waiting uses `aria-disabled` without removing keyboard focus. `disabled` provides actual native unavailability. The business layer uses `onRejected` to present field errors or persistent Alert.
- [Feedback.tsx](react/Feedback.tsx): `ToastNotice` accepts only `success` / `info` for lightweight outcomes requiring no action. `PersistentAlert` presents ongoing sync/network failures and can receive an async retry button through `action`. Field errors remain next to fields; not every error needs Alert.

Button waiting ends when the returned Promise settles, which does not itself mean success. The business layer owns request identity, idempotency, unknown outcomes, saved snapshots, and newer drafts. The template does not announce success, roll back data, retry, or treat unmounting as server cancellation. Error callbacks may arrive after unmount; bind operation identity and forward to a still-valid data/feedback owner.

For forms, adapting only the button is insufficient: `onSubmit` also needs validation, duplicate guards, and input-method composition handling. `label` remains the visible action name; waiting appends `pendingLabel`, for example “Save (Processing…)”. The accessible name comes directly from the same visible text; do not override it with a fixed `aria-label`. Announce important phases through an existing status area.

## Controlled Toast Lifecycle

Keep `ToastNotice` mounted and update `visible`/`message` in an existing polite live region. The template has no countdown. The host dismisses it at an appropriate point after task completion, avoiding disappearance during reading. If adding automatic dismissal, pause timing during hover, keyboard focus, and page hiding; verify focus and reading time.

When the close button has focus, the template invokes required `restoreFocus` before `onDismiss`. The host returns focus to the original action or a valid fallback. If closing externally while focus is inside Toast, perform the same focus arrangement first. Never label unresolved errors or actionable warnings as `info` to bypass selection rules.

The closed state retains an empty announcement node; do not break its lifecycle with root-level `display:none` or `hidden`. For repeated identical text, update according to actual notification instances. Announcements still require testing with target assistive technology.

## Alert, Styling, and Adaptation

`PersistentAlert` has no timeout. The message remains until resolution or an explicit replacement by the target flow. Failed retry preserves it; after success, the host updates actual problem state. Visual Alert defaults to polite announcements; choose `announcement="urgent"` only for important dynamic messages needing prompt interruption. It does not move input focus automatically. Adjust heading level for the page while retaining `aria-labelledby` association.

Map `className` and `data-feedback` / `data-kind` / `data-pending` to existing tokens, focus rings, dimensions, and state styles. Templates have no inline brand values. Do not remove browser focus indicators without a visible replacement. Add inspected React Bits components only in relevant presentation layers; the host still determines business results.

## Validation Scope

This version passed TypeScript checking and simulated-DOM event checks for duplicate prevention while waiting, retry after failure, focus retention, controlled Toast dismissal, and persistent Alert. Simulation does not establish native browser keyboard activation, screen-reader announcements, visual layout, or performance. Validate the integrated interface using submodule checks.

Implementation references: [React DOM common events and properties](https://react.dev/reference/react-dom/components/common), [React useId](https://react.dev/reference/react/useId), [WAI Alert pattern](https://www.w3.org/WAI/ARIA/apg/patterns/alert/). Template code is original to this module.
