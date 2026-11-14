---
name: interaction-design
description: Design and repair state transitions, keyboard focus, submission feedback, and failure recovery for buttons, forms, navigation, overlays, and table actions. Select interaction submodules and React Bits animations on demand while managing performance. Supplement a page lead or handle local behavior without replacing its layout, business rules, or visual system.
metadata:
  version: 1.1.0
---

# Detailed Interaction Design

Make it clear whether an action happened, its current state, and how to continue. Choose the states and animations the task needs and deliver implementable, verifiable behavior. When code is requested, implement the agreed scope.

## Scope and Existing Decisions

Establish the intended action, existing components and business states, token source, editable area, target devices, and input methods from the request and target project. Inherit context already supplied by the orchestrator. Resolve ordinary gaps with justified local choices; do not require a questionnaire.

Read supplied target-project conventions. If this series provides `design-system/FOUNDATIONS.md`, `design-system/ORCHESTRATION.md`, and relevant module records, locate them from the target project root. They are optional context; do not search for the workspace where this skill was authored. For standalone use without conventions, read the [shared-method extract](references/foundations.md).

Preserve the page lead's layout, information order, business rules, and visual direction, and reuse working behavior. Complete local fixes independently. If component, responsive, or orchestration support is unavailable, the current implementer completes necessary work. Propose changes to shared tokens, component interfaces, or cross-page behavior to their owner without expanding the edit scope.

## Define Behavior Before Choosing Effects

1. Inspect current behavior and references. Distinguish visible facts, source descriptions, code inspection, actual execution, and recommendations. Static screenshots cannot establish dynamic flows. See [references and evidence](references/evidence.md).
2. For each relevant operation, define **trigger → state change → user feedback → exit or recovery**. Mark unsupported parts as unknown or proposed. Select applicable states from the submodules below; every component does not need every state. For messages or overlays, read the overlay applicability and exclusion table.
3. For remote submissions, filter requests, autosave, or bulk actions, read [async behavior and recovery](references/async-recovery.md). Establish success evidence, duplicate prevention, stale-response handling, and what survives failure first.
4. When animation is needed, prefer React Bits components that fit the existing stack and task. Read [React Bits integration and selection](references/react-bits.md), then consult the [complete catalog](references/react-bits-catalog.md) by category when finding a component. Integrate selected items against current official source; do not preinstall the library. Reuse equivalent existing components first. Use native lightweight feedback or existing CSS/components when appropriate, explaining the tradeoff.
5. Apply [motion and performance](references/motion-performance.md) to active effects, input alternatives, and reduced motion. The user's preference is React Bits for most suitable animations while avoiding stacked complex effects. Neither component count nor visual complexity constitutes measured performance.

Success, errors, selection, and permissions come from actual business state. Animation completion only marks the end of a visual effect; it is not request success. Mock data, timers, and demo completion states must not become production business logic.

## On-Demand Reading and Collaboration

This entry owns shared boundaries and routing. `sub-skills/` owns component rules, `references/` contains cross-module methods and source indexes, and `assets/` contains optional original templates. Submodules ship in this package and need no separate installation. Do not load all of them or repeatedly read the root entry because submodules link back to it.

| Current task | Read and produce |
| --- | --- |
| Tooltip, Toast, Alert, Modal, Popconfirm, Drawer | [Floating components](sub-skills/floating-components/SKILL.md): choose the type, then specify appearance, dismissal, focus, and recovery |
| Button hover/focus/loading/disabled, press feedback, action results | [Button interaction](sub-skills/button-interaction/SKILL.md): distinguish input feedback from business state |
| Input, validation, selectors, switches, sliders, filters | [Form interaction](sub-skills/form-interaction/SKILL.md): preserve drafts and specify validation and submission |
| Sidebar, breadcrumbs, current item, command menus | [Navigation interaction](sub-skills/navigation-interaction/SKILL.md): preserve orientation, keyboard access, and return position |
| General state distinctions, table sorting/selection/bulk actions | [States and tables](references/interaction-patterns.md), with relevant submodules |
| Requests, submissions, filter races, optimistic updates, undo, bulk outcomes | [Async behavior and recovery](references/async-recovery.md): define success and failure paths |
| New or conflicting user references | [References and evidence](references/evidence.md); consult [initial reference rules](references/reference-rules.md) if needed |
| React Bits selection or integration | [Integration guide](references/react-bits.md) and optional [catalog](references/react-bits-catalog.md): record component, variant, source, and adaptation |
| Complex effects, constrained devices, touch, reduced motion | [Motion and performance](references/motion-performance.md): define activation, suspension, and fallbacks |
| Orchestration handoff, delivery, behavior checks | [Handoff and validation](references/handoff-validation.md): concise agreements and actual check results |
| No existing implementation; state button or result-message template needed | [Template guide](assets/README.md): adapt to the stack while retaining real outcomes and focus logic |

Apply the user's explicit overlay conventions: Tooltip provides supplementary explanations only; Toast presents lightweight outcomes and never errors; Alert persists important problems. Modal handles irreversible confirmation or complex information; Popconfirm handles low-risk local confirmation only; Drawer supports editing while retaining context, excluding simple forms and full-screen tasks. The overlay submodule defines complete conditions and alternatives. React Bits demos do not override them.

Assign one owner to integrate each component. Work with `component-system` on semantics, interfaces, and states, and with `responsive-design` on touch, scrolling, and input methods. Reuse decisions already covered by the lead without duplicate loading or circular handoffs.

## Delivery

For local tasks, deliver the necessary behavior specification or code and check results. For cross-module work, also identify affected components, state owners, proposed shared changes, and unverified items. Validate keyboard access, focus, submission feedback, and recovery using [handoff and validation](references/handoff-validation.md). Use representative scenario walkthroughs for rules-only work; test real flows when a running interface exists. Do not report document review, source inspection, or screenshot review as successful runtime testing.

Standalone example: Use `$interaction-design` to repair keyboard focus and save-failure recovery in an editing Drawer, preserve existing components and styles, and choose animation only for necessary state transitions.

Version 1.1.0. Shared-method sources: Interface Design Foundations 0.2 and Authored/External Design Skills Orchestration 0.1. Reference research and submodule/overlay conventions dated 2026-11-14. Effective target-project conventions and the user's current instructions take precedence.
