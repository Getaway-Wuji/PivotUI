# Validation, Dirty-State Protection, and Persistence

## Draft isolation and cancel scope

- Initialize form state from an immutable snapshot of the loaded record.
- **Cancel when clean:** Navigate back immediately without an unnecessary confirmation prompt.
- **Cancel or route leave when dirty:** Prompt with clear options ("Keep editing" vs "Discard unsaved changes") before dropping user work. Cancelling must leave the underlying record store unchanged.

## Validation timing and error summary

- Validate on blur for format constraints after user interaction, and validate all fields on submit. Never show premature errors on untouched fields on initial render.
- Keep field-level errors directly below the control and bound via `aria-describedby` and `aria-invalid="true"`.
- For forms spanning multiple sections, display a top `Alert` error summary listing clickable links to each invalid field; move focus to the summary or first invalid field upon failed submit.
- Map server-side field validation errors back to the exact inputs while preserving all user-entered draft values.

## Async submission and failure recovery

- Enter explicit pending state on submit: disable duplicate triggers, preserve input visibility, and never clear the draft optimistically before server confirmation.
- On network error or 5xx failure: keep every edited field intact, display an actionable `Alert` with retry guidance, and restore interactive submit controls.
- On timeout / unknown outcome: warn the user before re-creating non-idempotent resources, or use an idempotency token when supported.

## Verification checklist

- Clean cancel returns immediately; dirty cancel/navigation confirms and leaves source data untouched.
- Client and server validation failures preserve all entered draft values and move focus to an actionable error location.
- Rapid double-click on Save triggers only one submission.
- Successful save updates the shared record store and returns cleanly to the detail page or source list without losing context.
