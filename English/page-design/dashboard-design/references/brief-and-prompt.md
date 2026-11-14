# Turn Selection into a Design Brief or Prompt

Use when the user needs a proposal, AI prompt, or transferable design input. This guide adds business constraints to reference styling; it does not require a long document in every response. For code tasks, incorporate necessary decisions into implementation rather than stopping at a completed template.

## Short design decisions

State the following from known requirements; omit irrelevant fields:

```text
User and task:
Role and scope: The region this module leads or supports, and allowed changes; inherit the orchestrator agreement.
Design authority: Actual locations of target-project tokens/theme and components; without an existing system, identify recommendations and who consolidates them.
Primary structure: An A–G category; optional secondary areas and their purposes.
Visual choice: The retained theme or faithful-reference source; when choosing a new direction, the selected P01–P11 recipe. Note the brand, typography, and components to inherit; a retained complete theme or faithful reference needs no recipe ID.
Design basis: Concrete layout/visual methods; source IDs are optional notes and do not require recipients to open original images.
First screen: Regions and their questions in reading-priority order.
Data representation: Metric definitions, units, periods, comparisons, and charts.
Interaction: Filter scope, drill-down, return, necessary states.
Display medium: Desktop/mobile/wall display/static report; corresponding content order and operations.
Assumptions and data connection: Missing inputs and how sample data is labeled.
Delivery: Design brief/editable interface/existing-code changes/prompt, according to the request.
Handoff result: For collaboration, add actual outputs, shared changes, and verified/unverified items; independent tasks do not need a separate handoff document.
```

Write findings such as “Repeat purchases drove revenue growth” only with reliable data. Otherwise use neutral titles such as “Revenue and repeat-purchase performance” or “Sources of growth.”

## Composable prompt

Fill this template before delivering it; do not leave placeholders in the final prompt. Do not choose an unrequested framework, icon library, brand, or font by default. Read the actual project for implementation.

```text
Design a Dashboard for [role] in [business context], primarily helping them [judge/act].
Inherit [existing framework and visual constraints]. Use [primary structure] with [retained theme/reference or newly selected visual recipe].
Apply [fully described layout/hierarchy/surface/chart methods], replacing unrelated sample brands and business content.

Organize the first screen in this priority order: [regions and main questions].
Main metrics are [metric + definition + unit + period], compared with [data-supported baseline].
The primary area uses [chart/list/tasks/content cards and rationale]; supporting areas use [explanatory/action content], together addressing [business question].
Data mode is [real data/concept demonstration]. Real data follows actual sources; demonstration data is clearly labeled and internally consistent. Preserve required core modules whose data is not connected, mark their connection status, and do not invent results.

Visually, use [specific layout relationships, focal point, surface hierarchy, and emphasis].
Give [primary content] the greatest reading weight, with consistent controls, number conventions, and color semantics.
Provide [filtering/drill-down/expansion/actions], stating the affected regions and return behavior.
Support [devices/display medium], rearranging by [task order]; cover relevant loading, empty, failure, and stale states.
Deliver [requested output] and verify [checks appropriate to that output].
```

Expand any A–G, P01–P11, and S/V IDs actually used into ordinary language in external prompts. The recipient should understand the design from the prompt alone. Internal records may retain IDs; do not invent a recipe ID for an inherited theme or faithful reference.

## Example 1: Commerce business overview

**Decision:** A + P04. Borrow S16's metric–trend–order relationship and S29's area hierarchy; inherit the product's light-blue brand.

**Usable prompt example:**

> Design a daily business homepage for a commerce owner to evaluate revenue, gross profit, refunds, and target gaps. Inherit the existing light-blue backend, navigation, and controls. Prioritize revenue, gross profit, refunds, and configured targets on the first screen. Label each with date range and unit, showing change only when comparable history exists. Define refund-rate denominators; without one, show available refund amounts or counts. Show revenue trends in the main area, adding a target line only when target data has matching time granularity. If profit needs a different scale, use vertically aligned small charts sharing a time axis. Add contribution rankings only with category/channel data, and order summaries/links only with order details. Give the main trend more width than supporting cards; unify white surfaces and light borders; use blue for the current series and main actions. Date filters synchronize related regions; mark independent periods explicitly. On mobile, retain core results and necessary exceptions first, then trends and details. If a requested target section is not configured, state this rather than inventing completion. Deliver the requested output; for implementation, verify key filters and narrow layouts.

## Example 2: User-behavior diagnosis

**Decision:** B + P05 when the user requested dark mode. S30 contributes product paths and muted teal; S26 contributes question–evidence–explanation organization. P05 governs surfaces.

**Usable prompt example:**

> Design a user-behavior analysis page for product managers investigating drop-off between visits and key actions. Use the existing dark theme with graphite surfaces, clear text, and limited teal for the current path. Put period, audience, platform, and comparison-period controls at the top. Show a visit path in the main area only when actual nodes and flow data support it, with selected-path users, share, and change alongside. If only fixed-step conversion data exists, use a funnel instead. Supporting areas show feature-use frequency and segment comparisons, with corresponding records or explanations below. Keep series colors consistent across charts; synchronize affected regions after filtering and show data timestamps. Offer keyboard or list alternatives for path selection; retain the chosen path and key values on narrow screens. Do not add server status without monitoring data or generate unsupported insights.

## Example 3: Warm-peach glass team workspace

**Decision:** D + P09 warm-peach variant. S14 contributes timeline/task structure, S19 people information, S25 material. Add other interactions only as needed.

**Usable prompt example:**

> Build a daily workspace for a small design team. Help members find today's and overdue tasks first, then review project progress and available people. Retain existing navigation. Use a soft warm-peach gradient, copper-orange emphasis, and a limited number of translucent frosted surfaces with thin borders and soft shadows. Give task lists stable solid backgrounds for long-text readability; size headings for the actual viewport. The primary area shows tasks with owner, status, and deadline; secondary areas show timeline and workload. Open project details inline or in a side panel; on close, return to the original task and preserve filters. Add card reordering only when personalization is required, with save, reset, and non-drag controls. On mobile, prioritize tasks, then progress and people. For management work alone, omit 3D flipping and card-gathering effects. Add optional lightweight effects only when the user explicitly requests presentation motion.

## Write delivery notes

Explain the selected structure/style and rationale, the reference methods adopted, and adaptations made. List only behaviors actually implemented and verified. Describe concepts, demonstration data, working interactions, and real backend integration separately and accurately. A source author's words such as “premium,” “professional,” or “polished” are not completed acceptance evidence.
