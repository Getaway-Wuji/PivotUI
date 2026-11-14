---
name: data-list-design
description: Design and implement complete administrative data list pages. Use for list composition, search and filters, views and columns, selection and bulk work, export scope, and returning from detail; retain the product shell and shared controls.
metadata:
  version: 1.0.0
---

# Data List Design

Make finding records, acting on them, and resuming work one coherent flow. Own the complete list region and its business semantics. A small table inside a dashboard or a local control repair does not automatically require this whole workflow.

## Establish the working contract

Use the supplied task and existing product to identify the entity, users' main decisions, identifying/comparison fields, available operations, permissions, dataset scale, query API, devices, and inherited shell, components and token source. Resolve ordinary gaps directly; ask about missing business rules only when they change the outcome. Select features for the work: saved views, bulk actions and exports are optional capabilities, not a checklist every page must satisfy.

The user's reference direction is:

> Data list page layout refers to Ant Design Pro list page: filter bar at top, batch action buttons above table, column setting toggle, pagination at page bottom. Preserve filter state and page number after returning from detail page.

Use this as a structural reference and required continuity behavior. It does not establish a fixed brand, stack, pixel specification, or proof of upstream implementation. Read [layout and reference](references/layout-and-reference.md) when composing the page or interpreting that reference.

## Define the list before building it

Arrange the page around identification, comparison and next action. Inherit product density and text styles; make long content readable without letting secondary metadata dominate. Separate query controls, table/view controls, selection-dependent work and row actions.

Define what a query identifies, what is selected, what an action will affect, and what survives navigation. A page checkbox never silently means all matching records. A changed query never silently expands an earlier selection. The detail-return path must preserve the applied filters and page number and recover a useful location.

Load details only for the current need:

| Need | Read |
| --- | --- |
| Layout, density, hierarchy, columns or saved views | [Layout and reference](references/layout-and-reference.md) |
| Search, sorting, pagination, loading or detail return | [Query and return](references/query-and-return.md) |
| Selection, batch tasks, permissions or exports | [Selection and jobs](references/selection-and-jobs.md) |
| Implementation acceptance or handoff | [Verification](references/verification.md) |
| Standalone use without shared project conventions | [Portable conventions](references/foundations.md) |

## Integrate and finish

The orchestrator chooses this module as list-region lead. Reuse the target shell and tokens. `component-system` owns Table and shared control implementation; this module owns their page composition and business contract. `interaction-design` and relevant subentries fill uncovered behavior; `responsive-design` fills cross-screen gaps; `global-style-skill` handles actual theme gaps. Assign one implementation owner per component. Reuse adequate existing behavior and complete ordinary gaps directly when supporting skills are absent.

Deliver the requested specification or working page, with adopted sources, state/scope decisions, component ownership and actual checks. Record observations, estimates and supplemental decisions separately in the target project's existing notes. Validate relevant flows with real rendering and input when implementing; label demo data and report checks not run. Independent package scope and provenance are in [PACKAGE](PACKAGE.md).
