---
name: responsive-design
description: Plan, implement, and check responsive layouts for pages and components. Use for content reflow, navigation collapse, narrow tables or charts, input-capability differences, and local overflow fixes while retaining the project's visual system.
metadata:
  version: 1.0.2
  tags: [responsive, mobile, narrow, overflow, table, breakpoint, touch, reflow]
---

# Responsive Design

Keep the user's task possible as available space and input capabilities change. Work as support to `design-orchestrator` or as the owner of an explicitly scoped page/component repair. Define constraints before layout, apply them during implementation, and inspect actual results afterward. When implementation is requested, deliver the change as well as the reasoning.

## Establish scope and evidence

Read the target region, user task, token source, existing components, breakpoint conventions, framework/version, target environments, and allowed edits from available project context. Reuse decisions already supplied by the lead. Ask only for missing information that materially changes the task; otherwise label reasonable assumptions and proceed.

Distinguish observed reference states, measured implementation behavior, and supplemental design. A desktop screenshot does not establish mobile layout, touch, hover, or keyboard behavior. Teaching slides explain techniques, not a product's cross-screen behavior. Record sources and adopted conditions in the target project's existing notes.

## Decide the change

For each affected region, establish **condition → retained content → rearrangement → continued operation**. Use a short statement for local repairs; use a small matrix when several regions change. Read [decision methods](references/decision-methods.md) for choosing fluid sizing, Flex/Grid, viewport or container queries.

- Priorities follow the user's work. Keep important information and actions reachable; relocation or disclosure needs an understandable entry and complete content. Do not remove business fields merely to fit.
- Follow existing breakpoints. Without them, find where actual content loses readability or operability, choose the smallest useful transition, then test around it. Device names and framework defaults are not universal thresholds.
- Preserve meaningful DOM, reading, and keyboard order. CSS `order`/Grid repositioning, breakpoint hiding or alternate navigation copies trigger the [sequence checks](references/handoff-validation.md) for the affected layouts. Carry filters, selections, drafts, and operation state across layout changes.
- Preserve the selected overlay's use conditions and exclusions during reflow. Do not turn Drawer into a full-screen editor; use a separate page or inline area when necessary. Adapt Modal presentation to its task and existing interaction contract.
- Choose page-wide rules from viewport constraints and reusable component rules from available container space when appropriate. Input capabilities are a separate axis from width.
- Avoid global horizontal clipping, uniformly reducing root/text size, or scaling the whole interface to hide a layout failure.

## Load only needed guidance

| Need | Read |
| --- | --- |
| Navigation, columns, controls, tables, charts, Modal or fixed regions | [Region patterns](references/region-patterns.md) |
| Long text, overflow diagnosis, touch, keyboard, hover, viewport height | [Input and overflow](references/input-and-overflow.md) |
| Target implementation uses Tailwind | [Tailwind adaptation](references/tailwind.md) |
| Coordinating owners or checking a completed change | [Handoff and validation](references/handoff-validation.md) |
| Standalone work lacks shared project conventions | [Portable foundations](references/foundations.md) |
| Source provenance or a framework claim needs checking | [Source map](references/source-map.md) |

## Implement and return

Inherit visual direction and the authoritative product tokens. Coordinate purposeful variants with `component-system` and input/focus behavior with `interaction-design`; the named page/component owner integrates the change. Reuse valid behavior already supplied by those modules. If they are unavailable, complete ordinary work directly using the relevant guidance here; do not require a circular handoff or invent an invocation.

Return the changed region/files, transition decisions, preserved content/action paths, and actual verification with limitations. For a coordinated task, also return variant requests, token proposals, and the integration owner. Local fixes do not regenerate the brand or expand the shell's scope. Authoring records and the full cluster are not required at runtime; see [package use](PACKAGE.md).
