---
name: dashboard-design
description: Design or improve a backend Dashboard (including "dash broad") from business roles, data tasks, and reference images. Choose information structure, charts, visual language, and necessary interactions for business overviews, analysis, live monitoring, workspaces, and resource overviews. Standalone application navigation, forms, and full data-list design are outside this module.
metadata:
  version: 1.1.4
---

# Dashboard Design

Turn business questions into dashboards people can read, interpret, and act on. Choose the task structure first, then the visual language, then useful interactions. When the user requests a specific reference, start from that reference and preserve their explicit requirements.

## Read project constraints first

- Check the target project's available design standards and component conventions. If it follows this series' directory convention, resolve `design-system/FOUNDATIONS.md` and `design-system/modules/dashboard.md` from that project's root and read them only if present. These optional files are not prerequisites for using this skill.
- If the target project has no design standards, read the bundled [shared design conventions](references/foundations.md), excerpted from *Shared Interface Design Foundations*, **0.2, 2026-11-14**. Target-project rules take precedence; the excerpt fills methodological gaps.
- Resolve every Markdown resource link relative to its containing file. The methods are documented as text rules; original images and research notes used to build this skill are unnecessary.
- The reference library does not establish the target product's brand colors, fonts, theme, or radii. Styles and values below are candidates, not confirmed user preferences. Record adopted values in the target product. Update the series' shared foundations only when the user explicitly changes its general methods.
- Own Dashboard content, metric hierarchy, charts, summary lists within overviews, and necessary interactions. Reuse the page shell. Choose a navigation variant only when requested or when no shell exists; do not also redesign application-wide forms and lists.

## Continue an orchestrator assignment

This skill works independently or through `design-orchestrator`. When a work agreement already exists, inherit its region, role, reference purpose, authoritative token source, existing components, target devices, allowed changes, and acceptance criteria. Reuse established decisions without asking for them again. New explicit user requirements take precedence; update the agreement when they change it.

- **Follow the assigned role:** As lead, complete the assigned Dashboard content. As support for reference reconstruction, inspect only the agreed data semantics and states; do not choose a new composition or take over the page.
- **Unify shared styles:** Map recipes to the agreed tokens and components. Consolidate new shared values or component changes through the orchestrator role; name local variants. Do not create a second independently editable theme. The orchestrator and implementer may be the same agent; no additional approval step is needed.
- **Fill capability gaps as needed:** Reuse this skill's existing interaction and narrow-screen rules. If component, interaction, or responsive skills are unavailable, the current agent fills those gaps under the agreement and reports this honestly. Do not claim to have invoked missing capabilities. This series does not use `gpt-taste` for business areas; available `ui-ux-pro-max` contributes research and advice only.
- **Return verifiable results:** State the completed region, outputs and changed files, adopted tokens/components, proposed or consolidated shared changes, and verified versus unverified behavior. Do not resend the entire research collection; existing project records can carry the handoff.

When called directly, continue the dashboard task. If the project has an orchestrator and this task needs a new application shell, global styling changes, or coordination with other regions, locate and read the orchestrator entry and relevant agreements through the current environment's catalog. Read this series' `design-system/ORCHESTRATION.md` only when it exists in the target project. Do not repeatedly reroute an already assigned task. Standalone distribution does not require the orchestrator package.

## Make choices from the requirements

Obtain the following from existing requirements, data, and project context. Ask only when missing information changes the design; continue ordinary gaps with clearly stated assumptions.

| Information needed | What it changes |
| --- | --- |
| Who uses the page and what they need to judge or complete first | Main narrative and first-screen priorities |
| Key metrics, entities, units, definitions, and time range | Whether KPIs and charts are valid |
| Viewing frequency, data delay, and incident response needs | Overview, exploration, or monitoring |
| Data volume, grouping dimensions, and comparison targets | Density, charts, and summary/detail boundaries |
| Brand, existing components/theme, devices, and delivery format | Style, responsiveness, and implementation scope |

Form one internal design statement: **“Help [role] judge [question] in [context], then [action].”** If no action is needed, the outcome can be understanding, reporting, or comparison; do not force action buttons into the design.

### 1. Choose a primary structure

Use [selection-guide.md](references/selection-guide.md) to choose the structure:

| ID | Page task | First-screen priority |
| --- | --- | --- |
| A | Business overview | Results, gap to target, major changes, and routes to explanations |
| B | Diagnostic analysis | Filter context, main analytical chart, group comparison, and drill-down |
| C | Live monitoring and response | Exceptions, impact, freshness, and response entry points |
| D | Task and team workspace | My tasks, deadline risks, progress, and resource allocation |
| E | Account and resource overview | Current balance/capacity/status, inflows and outflows, recent events |
| F | Content and resource discovery | Previews, categories, search, and recent access |
| G | Thematic narrative and results report | Evidence-backed findings, trends, explanations, and sources |

Establish a clear primary task, then arrange explanatory and action areas as needed. When tasks compete for the first screen, use role, response deadlines, and visit purpose; split role-specific views or drill-downs when useful. Do not impose a fixed number of secondary areas. Industry is only a clue: the owner, operator, and warehouse worker in one commerce system need different primary structures.

### 2. Reuse or choose the visual language

When an existing complete theme is to be retained or a specified design is the visual authority for faithful reproduction, record that source and reuse the agreed visuals. Skip recipe selection and `visual-recipes.md` unless a specific visual gap or requested change needs it; no P-ID is required. A reproduction-support role keeps its assigned scope.

When visual direction needs choosing, use the quick reference in [visual-recipes.md](references/visual-recipes.md) to select candidates, then read only their matching entries. Preserve their hierarchy, whitespace, and surface relationships.

Existing themes take precedence. With no theme and ordinary requirements, start light, with clear boundaries and moderate density; do not default to glass, neon, all-black, or rainbow cards. Honor an explicitly requested style, then make it readable.

### 3. Arrange content around questions

Read [data-and-layout.md](references/data-and-layout.md). Express each block as “question → data → representation → next action.” The primary area answers the main question; secondary areas explain it or support execution. A task queue or content cards can be primary; a hero chart is not mandatory. Omit unsupported optional analysis or use a valid alternative. Preserve the structure of required core modules whose data is not connected yet, and label their missing-data state. Concept designs may use clearly labeled, internally consistent demonstration data, without presenting it as real results.

Before implementation, make a short decision record: role and task, A–G structure, retained theme/reference source or chosen visual direction and rationale, first-screen order, principal representations, interactions, display medium, and data status. Include a P01–P11 ID only when a recipe was actually selected. Categories support judgment; not every task must fit one ID. A clear user layout takes precedence. When the user wants only code, compress the record to a few sentences and finish implementation without requesting extra approval.

### 4. Load navigation and motion guidance only when needed

Read relevant entries in [interaction-patterns.md](references/interaction-patterns.md). Use expansion, filtering, linked selections, or command palettes to solve actual operational needs. Introduce reordering only when personalization is required. Hover flips, light tracking, and one-click aggregation are optional effects for specific styles.

A reference screenshot establishes static appearance only. Behavior described in an embedded prompt is a design requirement, not an observed implementation. Label added keyboard, touch, reduced-motion, and error-recovery behavior as design additions.

## Read resources on demand

Follow the routing above directly to the needed rules; do not browse all sources first. To understand which examples informed a method, read the [source and method summary](references/reference-index.md). Its S/V IDs identify evidence; they do not require opening external files.

When the user provides another design image, distinguish the requested features from sample business content. Do not import poster backgrounds, numbering, watermarks, or presentation perspective into the product. Do not retain sample brands, AI assistants, or promotions by default. Request the target image when exact reconstruction is required but the image is absent; continue ordinary design tasks with the available rules.

## Deliver and verify

Deliver the requested design brief, AI prompt, interface implementation, or page changes; [brief-and-prompt.md](references/brief-and-prompt.md) can organize the output. When implementation is requested, complete a working page and core interactions rather than stopping at a written proposal.

- Information: the main question is immediately clear; data has definitions, periods, units, and applicable comparison baselines; status and numeric direction are distinct; missing core data is not silently removed.
- Visuals: one main focus, explainable alignment, and stable series colors; long titles, large numbers, Chinese text, and dense lists remain readable.
- Operations: filter scope is clear, selected states match actual content, drill-downs have a return path, and core information does not require hover, flipping, or dragging.
- Data states: distinguish zero, missing, loading, empty filters, errors, partial updates, and stale data. Describe sample data and real connection status accurately.
- Devices: reorder by task priority on narrow screens, retain critical alerts and filters, provide readable chart/table alternatives, and support core actions on touchscreens.
- Check rendered output only for implementation tasks: desktop and target narrow screens, key filters/drill-downs, keyboard operation, and reduced motion. For specification-only work, check content, references, and applicability without claiming runtime validation.
- If the target project has a module-record convention, record sources, local choices, actual outputs, and validation scope accordingly. This series uses `design-system/modules/dashboard.md` under the project root. Elsewhere, retain necessary decisions in the delivery notes without creating a separate module-management directory.
