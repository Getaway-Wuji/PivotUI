---
name: floating-components
description: Select Tooltip, Toast, Alert, Modal, Popconfirm, and Drawer within interaction-design; define appearance, feedback, exit, focus, and failure recovery for overlay/message selection and local fixes.
metadata:
  version: 1.1.0
  tags: [modal, drawer, toast, tooltip, alert, popconfirm, overlay, dialog]
---

# Floating and Message Components

This is an on-demand submodule of `interaction-design`. Inherit the established scope, tokens, components, and input methods. When entering here directly, first read the shared agreements in the [core entry](../../SKILL.md), then handle the task here without circular submodule loading. Do not rearrange pages or redefine visual direction.

## Decide Whether an Overlay Is Needed

This selection table adopts the user's explicit requirements dated 2026-11-14. These are this module's conventions, not universal definitions used by every component library. They take precedence over generic older references and external-library demos.

| Type | Applicable use | Excluded use |
| --- | --- | --- |
| Tooltip | Transient explanations, such as button hover hints or password-rule explanations | Important action feedback or actions requiring confirmation |
| Toast | Lightweight action outcomes, such as successful save or copy | Errors or warnings requiring user action |
| Alert | Persistent important notices, such as sync failure or network error | Fleeting action feedback |
| Modal | Irreversible confirmation, such as permanent deletion; complex information | Simple action confirmation or small informational displays |
| Popconfirm | Lightweight local confirmation, such as low-risk sharing removal or removing a favorite | High-risk confirmation |
| Drawer | Editing while retaining context, such as editing a list record or settings | Full-screen tasks or simple forms |

Decision order:

1. Use Tooltip for supplementary explanations only. Rules users must know before entering a field still need visible or associated instructions; hover alone is insufficient.
2. A completed lightweight action may use Toast. No errors belong in Toast. Show field errors inline and persistent sync/network problems in Alert. Alert can be in the content area; it need not be a floating overlay.
3. When confirmation is necessary, assess actual impact first. Use Modal for irreversible/high-risk actions; use Popconfirm for low-risk confirmation suited to the action's anchor. Names alone do not establish risk: removing sharing that affects an entire team's access may need escalation. Execute simple actions directly when confirmation adds no value.
4. Use Drawer when editing needs retained list/context and is more than a simple form. Use inline editing or a page form for a few simple fields. The page lead should use a separate page for full-screen space or a long independent flow, not a full-screen Drawer.
5. Modal can present complex information. Keep small information in place or in a semantically suitable lightweight explanation. Permanent deletion remains irreversible and uses Modal even when its explanation is one sentence; short copy does not justify Popconfirm.

## Tooltip: Supplementary Explanation

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| Trigger is hovered or keyboard-focused | hidden → visible | Brief explanation associated with target; focus stays on trigger | Esc dismisses; close after effective focus is lost and pointer leaves the shared trigger/tooltip region |
| Pointer moves from trigger into tooltip | Remains visible | Content stays available for reading | Close after leaving the shared region and losing effective focus |

Do not put confirmation, retry, links, or required clickable form controls inside Tooltip. Choose another component for interactive content. Provide clear names and associated descriptions; Tooltip must not be an icon button's only accessible name. On touch, provide visible explanation or a separate tappable help entry, not hover alone.

The naming/focus pattern is described in [APG Tooltip](https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/) (marked as a work in progress). Persistent readability and dismissal are covered by [WAI content on hover or focus](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html).

## Toast: Lightweight Outcomes

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| Actual lightweight copy/save action succeeds | hidden → shown | Brief outcome; polite announcement if appropriate; no focus theft | Ends under project policy or user dismissal; not a container for actionable errors |
| Same lightweight outcome repeats rapidly | Update/merge identical messages | Avoid stacks covering controls | Keep the latest outcome clear; add persistent status at the action site if needed |

Toast must not carry errors or actionable warnings; a longer duration does not make an error Toast acceptable. Optional undo may accompany a lightweight outcome, but matters requiring user action belong in a persistent area. The undo window must match actual business capability. Keep actionable Toast available while hovered/focused, and place focus sensibly when dismissing a focused Toast. Do not generate Toast for every progress frame or keystroke.

## Alert: Persistent Problems and Notices

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| Sync failure, offline state, or important condition arises | absent → present | Persist the problem, impact, and available next step in the affected region | Update/remove when resolved; an unresolved problem must not disappear on a timer |
| Retry activates | present → retrying | Show retry status in place and preserve context | Clear after confirmed success; on failure keep the issue and restore retry |

The Alert component does not automatically require `role="alert"`. Use alert semantics for important dynamic errors needing immediate announcement; use suitable status/region semantics for less urgent persistent states to avoid repeated interruptions. Alert appearance must not steal focus. Before removing a focused retry button, assign a sensible destination. If dismissal is allowed, keep unresolved essential status discoverable elsewhere. See [APG Alert](https://www.w3.org/WAI/ARIA/apg/patterns/alert/).

## Modal: Irreversible Confirmation or Complex Information

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| User initiates irreversible/high-risk action or opens complex information | closed → open | Clear object, consequences, and options; background noninteractive; focus enters | Esc/cancel/close exits; return to trigger or sensible next location |
| Explicit confirmation with valid submission | open → pending | In-progress status; duplicate prevention | Close or continue after confirmed success; on failure retain content, inline error/Alert, and retry |

Before confirmation, prefer focus on the less destructive choice; complex content may initially focus the heading. Tab/Shift+Tab cycles within the modal, and its accessible name is associated with the visible title. Claim modal semantics only when background interaction is actually blocked. Content, fixed buttons, and scrolling must not obscure focus.

Escape, cancel, and close meanings must match request state. Users can leave before submission; closing after submission does not cancel the server operation. Explain an uncancellable running action and retain outcome tracking. Never silently treat closing as success or undo. Protect unsaved content under existing draft rules. See [APG Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).

## Popconfirm: Local Low-Risk Confirmation

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| User activates a low-risk action that genuinely needs confirmation | closed → open | Anchored object/action explanation and explicit confirm/cancel | Esc, cancel, or appropriate outside click closes; no action before submission |
| Confirmation sends a request | open → pending | Preserve anchor, in-progress feedback, and duplicate prevention | Close on success; retain nearby error/Alert and retry on failure, never error Toast |

It contains buttons and must not use tooltip role. Follow existing dialog/popover semantics and focus management; it is generally nonmodal and must not automatically trap focus. Focus cancel or explanatory content appropriately on open; return to trigger on close, or a suitable adjacent entry if removed. Adjust anchoring and visible position for small screens. Do not downgrade high-risk Modal to Popconfirm to save space. Outside-click handling must not accidentally activate dangerous background actions.

## Drawer: Editing with Retained Context

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| List/settings opens an editing area that needs surrounding context | closed → editing | Clear entity/title, recognizable original context, appropriate initial focus | Explicit close/Esc with draft protection; return to original entity entry |
| Draft is saved | editing → pending → confirmed/error/unknown | Actual saving state; preserve draft | Stay/close on success as appropriate; permit correction on failure; verify unknown outcome first |

A side-panel appearance does not determine modality. Preserve background tasks when nonmodal; enforce modal focus/background restrictions when modal. A workflow requiring simultaneous background interaction cannot lock that background and still claim to support side-by-side editing.

If content cannot fit a narrow screen, work with the page lead/responsive capability on a separate editing page or inline area. The exclusions for full-screen Drawer and simple-form Drawer still apply. Menu/Drawer close buttons must remain visible; gestures are enhancements only.

Read [async behavior and recovery](../../references/async-recovery.md) for snapshots, continued editing, timeout, stale responses, and retry; read [form interaction](../form-interaction/SKILL.md) for fields.

## Integration and Checks

Reuse existing accessible components first. React Bits Warm Tooltip and Swipe Toast are visual/behavior candidates only; see the [integration guide](../../references/react-bits.md) for capabilities and known gaps. Library error themes or animations do not change these selection restrictions. Manage complex overlay motion through [performance conventions](../../references/motion-performance.md); delayed entrance must not obstruct error reading.

For React templates covering lightweight outcomes and persistent errors, read the [template guide](../../assets/README.md). Templates do not replace mature Modal/Drawer focus management.

Check selection and behavior together: successful copy → Toast; network failure → Alert; temporary password explanation → Tooltip; permanent deletion → Modal; low-risk local confirmation → Popconfirm; simple two-field editing → inline form; complex editing requiring list context → Drawer; independent full-screen flow → page. Then check keyboard-only completion, focus after trigger removal, hover-readable explanations, persistent errors/retry, reduced motion, and touch alternatives. Record scenario walkthroughs separately from actual execution.
