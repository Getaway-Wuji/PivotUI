# Handoff and Validation

Use for orchestration assignments or pre-delivery checks. A short note suffices for local issues; do not add a full management-document system.

## Orchestration Input and Module Output

Inherit the agreed region, user task, page lead, token source, reference purpose, editable files, and devices. The current implementer fills ordinary support-module gaps; do not send users to nonexistent entries.

Include only items actually relevant to the task:

| Handoff item | Content |
| --- | --- |
| Scope and owner | Current component/region and integration owner; preserved layout and business rules |
| Behavior | Trigger → state → feedback → exit/recovery; keyboard and focus destinations |
| State ownership | Whether parent/form/data layer owns selection, pending, and outcomes; facts supplied to presentation components |
| Component selection | Existing components reused; exact React Bits name, variant, official source, inspected revision, and adaptations |
| Devices and performance | Touch alternatives, reduced motion, complex-effect scope, start/stop conditions, and fallback |
| Proposed shared changes | New tokens, shared interfaces, or cross-page behavior and impact; orchestration/component owner integrates |
| Validation | Methods actually used, results, environment, and unverified scope |

Discover capabilities through actual `SKILL.md` name, description, resources, and feasible scope; no extra registration file is required. The orchestrator can read this skill directly. Do not assign a different page lead or call back to orchestration in a loop. React Bits supplies components; it does not replace project responsibilities.

The orchestrator can continue handing off to `interaction-design`; this package's root selects floating-components, button-interaction, form-interaction, or navigation-interaction. Record the submodules actually read without turning them into four mandatory external installations. When using templates, identify adopted files and adaptations; see the [template guide](../assets/README.md).

## Representative Task Checks

Choose meaningful examples for the scope. For rule authoring, independently walk through selection and boundaries; for implementation, execute corresponding operations. Keep the evidence distinct.

| Task | Observable checks |
| --- | --- |
| Only a selected-switch screenshot; add interaction | Treat visible appearance as observation; explicitly propose keyboard, async failure, and recovery; do not infer spring trajectory from a screenshot |
| Fix only menu/focus in an existing business table | Preserve columns, queries, and tokens; check command-menu keyboard/dismissal behavior; do not animate the entire page |
| Retry a failed editing-Drawer save | Appropriate initial focus and modality; preserved input, duplicate prevention, reachable error, sensible return focus after success |
| Fast filtering produces out-of-order responses | Results match current query; stale responses cannot overwrite; conditions and displayed-data freshness remain clear after failure |
| Bulk deletion partially succeeds and connection times out | Distinguish success, failure, and unknown; do not repeat successes; reliable recovery and sensible focus |
| Several flashy marketing candidates on a slow mobile device | Permit React Bits, limit complexity/active instances by purpose, define pause/fallback and actual validation plan |
| Non-React project or absent support modules | Complete ordinary interaction using the current stack; do not migrate the project for animation |
| Copy success, save failure, and persistent offline state | Success may use Toast; errors are inline/Alert; no errors in Toast |
| One-sentence permanent deletion versus local low-risk confirmation | Modal for the former; Popconfirm for the latter only if confirmation is needed; never select by word count alone |
| Two simple fields versus a complete settings flow | Inline/page form for simple fields; separate page for full-screen flow; neither uses Drawer |

## Minimum Post-Implementation Operations

- Complete the key flow from its entry using only the keyboard. Check Tab order, applicable Enter/Space/arrows, Esc, and visible focus. Follow each control's semantics rather than assigning identical shortcuts to all controls.
- Open/close menus/dialogs/Drawers, including focus after trigger deletion, list reordering, and scrolling. Hidden content must not remain focusable.
- Submit valid/invalid content, fail, and retry. Cover repeated activation, timeout, out-of-order responses, and continued editing during submission where needed. Visible and announced status must match real outcomes.
- During cancellable phases before business execution, check pointercancel, Esc, pointer leave, and focus loss. For slide controls, include reaching the endpoint without normal release; for hold controls, include focus transfer/release/Esc before threshold. Cancellation must not initiate a new submission. Already-started actions use async cancellation or undo. A cancellation handler's presence alone does not prove its branches are correct.
- On target narrow screens and applicable input methods, check entries, scrolling, overlay occlusion, touch alternatives, and reduced motion. Measure complex effects using [performance checks](motion-performance.md).
- Check accessible names, field-error association, and announcements. Without a screen reader test, do not claim screen reader compatibility was tested.

Use precise findings such as “scenario walkthrough passed,” “source contains this handler,” or “these operations ran in this environment.” Record branches not executed. Valid links, successful compilation, and metadata validation do not replace interaction testing.
