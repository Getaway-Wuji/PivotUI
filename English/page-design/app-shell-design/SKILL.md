---
name: app-shell-design
description: "Design, implement, or repair the shared shell of an administration application: navigation hierarchy, current location, headers, content boundaries, and scrolling across list, detail, and edit pages. Use for cross-page framework work; page modules own business content."
metadata:
  version: 1.0.0
  tags: [app-shell, navigation, sidebar, header, breadcrumb, scroll, layout]
---

# Application Shell Design

Make different pages feel like one application: users can locate themselves, reach another task, and return without losing their place. Own the frame around page content, including information architecture, sidebar/top navigation, breadcrumbs, page heading and actions, width, fixed regions, and scroll ownership.

## Start from the product

Inspect existing routes and layouts, navigation/permission rules, shared components, authoritative tokens, target screens, and the requested scope. Preserve working structure. A new reference does not justify replacing the router or creating a second theme.

Separate **persistent frame** (global navigation and controls), **route context** (breadcrumb, title, page actions), and **page content**. Map representative list → detail → edit routes before choosing their geometry. The same navigation item may represent all three routes; their titles and breadcrumb endpoints differ.

## Choose and define the shell

For a new backend shell adopting the supplied reference, use the Ant Design Pro direction: fixed collapsible left sidebar, top header with global controls, breadcrumbs above page content or inside the header, and an independently scrolling right content region. Preserve this recognizable composition while adapting it to the product. It is a reference pattern, not a requirement for every task or an assertion that all Ant Design Pro configurations are identical.

For new or substantially changed frames, or unresolved routing, scrolling, or return-state issues, read the relevant sections of [frame decisions](references/frame-decisions.md). Resolve these together:

- What persists across pages, and what comes from the active route?
- Which regions share a starting line and width, and where do boundaries belong?
- Which element owns each scroll axis, and which elements stay visible?
- How do navigation, focus, and return state continue when space changes?

Do not require a sidebar, page Tab system, fixed page heading, or a universal width when the existing task calls for another arrangement. For source attribution or framework configuration, read [reference scope](references/reference-scope.md). User statements, documented facts, estimates, and supplemental design remain distinguishable.

## Implement with clear ownership

The orchestrator selects this module as shell lead. Dashboard, list, detail, and form leads own content. Agree on route metadata, heading/action slots, content width and inset, scroll container, and return-state responsibilities; avoid duplicated headers or nested scroll containers.

Use `navigation-interaction` for concrete navigation/focus gaps, `component-system` for shared primitives, and `responsive-design` for collapse or cross-screen gaps. One named implementer integrates each region/component. Reuse adequate existing behavior; complete ordinary gaps directly if specialists are absent. Consume product tokens; `global-style-skill` handles genuine theme gaps and the orchestrator consolidates changes. Standalone essentials are in [shared conventions](references/foundations.md).

Deliver the requested implementation or specification. Keep the frame stable while content changes; preserve filters, drafts, selection, scroll, and focus according to the product's navigation contract, with safe fallbacks for direct entry or removed records.

## Verify and hand off

Use the applicable checks in [verification](references/verification.md). Exercise long labels, nested routes, return paths, keyboard use, collapse, narrow and short viewports, fixed-region overlap, and rendered text contrast. A static specification cannot establish runtime success.

Return the chosen frame and its conditions, route/content contract, reused components and tokens, source evidence and supplemental decisions, artifacts, and checks actually run. Record durable decisions in the target project's existing notes; this authoring repository is not a runtime dependency.
