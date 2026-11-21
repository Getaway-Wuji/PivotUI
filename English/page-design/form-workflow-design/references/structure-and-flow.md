# Form Structure, Settings Navigation, and Wizard Flow

## Section grouping and measure

- Constrain prose and standard single-column form containers to a comfortable reading measure (typically 640–840px) rather than stretching inputs across ultra-wide monitors.
- Group fields by user mental model (Identity, Access/Permissions, Schedule/Budget, Notifications) with concise section headings and optional 1-line helper context.
- Use 2-column rows only for naturally paired short fields (e.g., First/Last name, Start/End date, Currency + Amount); avoid zigzagging unrelated fields across columns.
- Place labels consistently above inputs for mixed Chinese/Latin copy and narrow-screen resilience.

## Settings page patterns

- **Section-scoped cards:** Each card owns its own Save button and error state when sections map to independent backend endpoints (e.g., Profile vs Password vs Danger Zone).
- **Unified dirty save bar:** When edits span multiple sections saved in one transaction, display a sticky footer/header bar only when dirty (showing Reset/Discard + Save Changes) so users never hunt for the submit button.
- **Danger Zone isolation:** Separate irreversible account/workspace actions (Delete, Transfer Ownership, Revoke All Keys) into a visually distinct final section with explicit `Modal` confirmation.

## Multi-step wizard discipline

- Show total steps, current step, and completed status clearly.
- Validate the current step before advancing; allow jumping back to completed steps without clearing entered values.
- For high-impact submissions, include a final Review step summarizing key choices with direct links back to edit specific sections.

## Narrow-screen rules

- Collapse 2-column field pairs to 1 column cleanly; ensure sticky save bars do not obscure focused inputs or virtual keyboard areas (`scroll-padding-bottom`).
- Keep primary action reachable without horizontal scrolling.
