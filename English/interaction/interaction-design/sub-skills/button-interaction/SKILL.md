---
name: button-interaction
description: Handle command-button hover, focus, press, disabled, loading, result, and recovery states while preserving action semantics, business logic, and a stable hit area.
metadata:
  tags: [button, press, loading, pending, disabled, keyboard]
---

# Button Interaction

This is an on-demand submodule of `interaction-design`. Inherit the scope, tokens, evidence labels, and component conventions established by the [root entry](../../SKILL.md); do not reread it when routed from there. When entering directly without this context, read only its “Scope and Existing Decisions” section. Target-project conventions remain optional context.

Own command buttons and their feedback. Delegate links to [navigation interaction](../navigation-interaction/SKILL.md), whole-form validation to [form interaction](../form-interaction/SKILL.md), and confirmation/result containers to [floating components](../floating-components/SKILL.md). These are implementation rules, not behavior observed in static references.

## Select Applicable States

Determine whether the action is immediate and local, a remote change, or opening an interface. hover/focus/pressed describe input feedback; selected/checked describe persistent selection; pending/error describe business lifecycles. They can coexist and must not collapse into one `active` flag.

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| Pointer enters or keyboard focuses an actionable button | hover / focus-visible | Existing surface, border, or focus ring; lightweight motion if useful | Clear temporary styling on leave/blur without changing persistent selection |
| User completes valid activation | pressed, then actual command execution | Optional press or ripple feedback; label stays understandable | Restore on release; a cancellation before business execution must not submit |
| Valid remote operation is submitted | idle → pending | In-place feedback such as “Saving,” with stable dimensions | Prevent duplicates; actual outcome determines confirmed / error / outcome-unknown |
| Current conditions prohibit execution | enabled → disabled | Discoverable reason and actionable prerequisites | Restore when conditions permit; never hide the only explanation in hover on an unfocusable control |
| Confirmed success or explicit failure arrives | pending → result | Lightweight success feedback as appropriate; persistent nearby failure or Alert | Preserve context; allow correction or safe retry; never show errors in Toast |

Do not invent loading for immediate actions or open a dialog for every success. Business impact determines risk and confirmation, not a red button. Do not use Modal for low-risk simple confirmation or Popconfirm for high-risk confirmation. Irreversible actions use Modal under the overlay rules even when the wording is short.

## Semantics and Input

- Execute commands with native buttons and an appropriate `type` to avoid unintended form submission. Preserve native Enter/Space activation without duplicate handlers. Icon-only buttons need accessible names.
- Native `disabled` affects focusability. When using `aria-disabled` to retain discoverability, guard the execution function against pointer, keyboard, and programmatic activation; grey styling alone does not disable anything.
- While pending, prevent duplicates both in the button and execution function. Do not remove the current focus without assigning a destination. Keep existing content readable; unrelated actions need not freeze. See [async behavior and recovery](../../references/async-recovery.md) for request identity, idempotency, and unknown outcomes.
- Use `aria-pressed` only for actual toggle-selection semantics. Ordinary command buttons must not remain selected after activation. Switches, checkboxes, and radio controls belong to the form module.
- Animation wrappers must not nest interactive elements or swallow link, button, or keyboard events. Magnetic effects need a stable hit area; decorative sparks do not establish success.

## Motion and Special Gestures

When motion is needed, select a fitting component through [React Bits integration](../../references/react-bits.md) and apply [performance constraints](../../references/motion-performance.md). Prefer brief, local button feedback. Do not repeat complex effects in every row or entry point.

Use hold/slide confirmation only when the gesture suits the task, with an equivalent path that requires neither prolonged holding nor dragging. Verify release, pointercancel, Esc, and focus transfer before the business action starts. Once the threshold has started an action, use its real cancellation or undo capability; reversing an animation is not cancellation. Address the known Hold Button and Slide Commit cancellation gaps documented in the integration guide before use.

## Delivery Checks

- Keyboard activation works and focus is visible; other event paths cannot bypass disabled or pending guards.
- Rapid repeated activation produces only the agreed business execution; success, failure, and timeout have explicit, truthful feedback.
- Loading transitions do not shift the hit area or lose focus; users can continue after failure.
- Hover, touch, and reduced motion retain the same action outcome. Report runtime success only after actually running it.
