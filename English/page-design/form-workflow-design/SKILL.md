---
name: form-workflow-design
description: Design and implement full-page forms, edit screens, multi-step wizards, and settings pages. Organize field grouping, single vs sectioned vs stepped flow, dirty-state protection, validation summary, sticky save bars, cancel scope, and post-save navigation within the product shell and tokens.
metadata:
  version: 1.0.0
  tags: [form, settings, edit, wizard, create, configuration, validation, draft, admin]
---

# Form and Settings Workflow Design

Structure full-page creation, editing, and settings workflows so users understand what they are changing, never lose valid work, and know when changes are saved. Own page-level form architecture, sectioning, save/cancel flow, and post-save routing. Delegate low-level field/IME/async mechanics to `form-interaction` and shared input primitives to `component-system`.

## Establish the working contract

Confirm from the request and target project: workflow type (create, edit existing record, settings/preferences, or multi-step wizard), field groups and dependencies, required vs optional rules, save model (explicit submit, section-level save, or autosave), permission/read-only constraints, and return target after save or cancel. Resolve ordinary gaps with stated assumptions; ask only when missing business rules change workflow structure or data integrity.

## Choose form structure before layout

| Workflow profile | Recommended structure | Key safeguard |
| --- | --- | --- |
| 4–12 related fields (create/edit entity) | Single-column or clear 2-column sectioned page with top/bottom action bar | Keep one visual reading flow; match field width to expected value length |
| Broad product/account settings (15+ controls across domains) | Left section index or Tabs + independently scoped setting cards (or sticky dirty-save bar) | State clearly whether each section saves independently or together |
| Sequential dependent decisions (onboarding, provisioning, checkout) | Explicit stepped wizard with step summary, back/next, and final review | Preserve earlier step state when moving back; never discard valid steps on error |

## Core workflow rules

1. **Separate draft from committed state:** Edit an isolated draft snapshot so cancelling never mutates the underlying record and failed saves never clear user input.
2. **Make save scope and dirty state unmistakable:** Show when unsaved changes exist, confirm before discarding dirty drafts on navigation/cancel, and disable duplicate submissions while saving.
3. **Pair inline errors with an error summary for long forms:** Keep each error adjacent to its field (bound via `aria-describedby`); on submit failure in multi-section forms, show an `Alert` summary with jump links and move focus to the first invalid field or summary.
4. **Respect context and return paths:** Preserve source detail/list return continuity after saving or cancelling (`detail-page-design`, `data-list-design`, `app-shell-design`). Distinguish full-page edit workflows from context-preserving `Drawer` edits (`floating-components` excludes full-screen tasks from Drawers).
5. **Handle concurrency and partial readiness:** Cover initial load failure, read-only/locked fields, server-side field errors, and unknown/timed-out save outcomes cleanly.

Load on-demand details only as needed:

| Need | Read |
| --- | --- |
| Sectioning, settings navigation, wizard progression, responsive column rules | [Structure and flow](references/structure-and-flow.md) |
| Dirty-state guards, validation summaries, cancel scope, save failure recovery | [Validation and persistence](references/validation-and-persistence.md) |
| Standalone use without shared project conventions | [Portable conventions](references/foundations.md) |

## Integrate and verify

Reuse the product's shell, authoritative tokens, and existing form controls. Engage `form-interaction` for complex field validation, IME composition, or filter/request races, and `responsive-design` for narrow-screen action bars and input ergonomics.

Deliver the requested specification or working page, reporting workflow structure, save/cancel model, verified failure/draft-preservation flows, and any unverified runtime scope. Package scope: [PACKAGE](PACKAGE.md).
