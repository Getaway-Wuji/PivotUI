---
name: detail-page-design
description: Design and implement entity detail pages, inspection views, and record workspaces. Organize record identity, status, structured attribute groups, related records, safe actions, missing/forbidden states, and source-list return continuity within the product shell and tokens.
metadata:
  version: 1.0.0
  tags: [detail, record, entity, inspection, summary, timeline, return-state, admin]
---

# Detail Page Design

Turn a single business entity into a clear inspection and decision surface. Own detail-region structure, information grouping, action placement, missing/error states, and return continuity. Reuse the product's application shell, shared components, and authoritative tokens.

## Establish the working contract

Identify from the request and target project: entity type and stable ID, user's primary inspection or approval goal, critical status/exception cues, attribute groups, related collections or history, available actions and permission boundaries, and whether the user arrives from a list, deep link, or search result. Resolve ordinary gaps with stated assumptions; ask only when missing business rules change structure or permissions.

## Structure the detail surface

1. **Identity and status header first:** Display the entity title, stable identifier, current lifecycle status, and primary/secondary actions in a scannable header zone inside the shell's content area. Keep destructive actions visually separated from routine edits.
2. **Prioritize scannable groups over raw field dumps:** Group attributes by decision relevance (summary facts, operational details, ownership/timestamps, related records, audit history). Use tabular numerals for IDs, amounts, and dates; distinguish `0`, empty (`—`), redacted, and unloaded values.
3. **Separate reading from editing:** Keep read-only inspection clean; route substantial multi-field edits to `form-workflow-design` or an agreed edit route/Drawer (`floating-components` governs overlay eligibility—never force full-screen tasks into a Drawer).
4. **Handle non-happy paths explicitly:** Cover loading skeleton/state, not-found (404 / deleted record), insufficient permission (403), stale/concurrently updated record, and partial failure when a secondary related-records panel fails without blanking the primary entity.
5. **Preserve return continuity:** Honor the source list's route/history entry when returning from detail or after editing (`data-list-design` + `app-shell-design` share one return coordinator). Support direct deep links cleanly with a sensible fallback back to the entity's parent list.

Load on-demand guidance only for the current need:

| Need | Read |
| --- | --- |
| Header anatomy, attribute grouping, related lists, tabs vs stacked sections | [Layout and sections](references/layout-and-sections.md) |
| Primary/destructive actions, permissions, deep links, return continuity, checks | [Actions and continuity](references/actions-and-continuity.md) |
| Standalone use without shared project conventions | [Portable conventions](references/foundations.md) |

## Integrate and verify

`app-shell-design` owns persistent navigation, breadcrumbs, and the outer scroll container; do not assume `window` is the scroll container. `component-system` owns shared description lists, tabs, badges, and tables; `interaction-design` and `responsive-design` fill uncovered behavior or narrow-screen reflow gaps.

Deliver the requested specification or working page, noting adopted token/component sources, handled edge states (missing, forbidden, stale, deep link), return behavior, and actual runtime vs static checks performed. Package scope: [PACKAGE](PACKAGE.md).
