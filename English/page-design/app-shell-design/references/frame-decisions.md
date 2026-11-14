# Frame decisions

Read for a new shell, structural redesign, or a specific unresolved routing/geometry/scroll question. Use the relevant sections, not a mandatory checklist for every local fix.

## 1. Separate location from presentation

Use the product's route definitions and permissions as the source of truth. Map navigation by stable route identity or an explicit matching rule, not substring matching that confuses similarly named paths. Detail and edit routes can share a visible navigation ancestor without adding one sidebar item per record.

| Route example | Navigation location | Breadcrumb | Heading / page action |
| --- | --- | --- | --- |
| /orders | Orders | Workspace / Orders | Orders / Create order |
| /orders/:id | Orders | Workspace / Orders / record label | Record label / Edit |
| /orders/:id/edit | Orders | Workspace / Orders / record label / Edit | Edit record / Save, Cancel |

These are semantic examples, not required route names. Non-navigable ancestors may be text. Do not invent links to missing or forbidden pages. Unknown routes need the product's not-found behavior rather than a false active item. Breadcrumbs express hierarchy; Back expresses travel history or an explicit return destination.

Derive current location only after navigation succeeds. Keep current, hover, focus, expanded group, and selected same-page tab as separate states. Reveal active ancestors on entry so a nested page is discoverable; allow deliberate user collapse without pretending the route changed. Group labels with both a destination and disclosure need separate controls.

Follow existing permission handling. Hiding a navigation link is not access control; authorization remains with the product. Preserve valid paths for deep links, reloads, and browser Back/Forward.

## 2. Establish the frame and its boundaries

Select geometry from the task and reference:
- A persistent sidebar suits repeated switching among hierarchical work areas.
- Top navigation can suit fewer peer destinations; mixed layouts need a clear division between global areas and local sections.
- A focused editor may reduce persistent navigation if the product already provides a clear exit and state-preserving return.
- Route Tabs are optional. Do not add a multi-tab workspace merely because the reference is an admin scaffold.

For the supplied classic pattern, choose a full-width top header above the sidebar and right content region unless the target product already uses another header/side relationship. Put identity/account and cross-page controls in the header. Keep page-specific actions beside the page heading or in the agreed page slot, rather than repeatedly moving them into the global header.

Define one primary left alignment for breadcrumb, heading, and content. Record deliberate exceptions, such as a bounded reading form within a fluid table page. Use the same outer inset and heading arrangement for sibling pages; content modules control their internal columns and density. Keep chrome subordinate to working content. Use separators or surface changes where regions need distinction; avoid wrapping every level in another bordered card.

Choose sidebar width from readable labels and hierarchy, content width from the work, and header height from its controls. Long labels can wrap or use accessible full-label disclosure; icon-only navigation must remain understandable by keyboard and touch. Exact dimensions, colors, fonts, and radii come from product tokens or explicit sample choices, never a supposed universal scaffold standard.

## 3. Assign scrolling before fixing elements

Write a small scroll map: region, vertical/horizontal owner, persistent elements, overflow behavior. For this reference pattern:

| Region | Behavior |
| --- | --- |
| Global header | Remains visible outside the main scroller |
| Sidebar | Stays in place; its menu scrolls vertically when taller than available space |
| Right content | Owns primary vertical page scrolling |
| Wide table or other local content | May own local horizontal scrolling; does not create a second accidental vertical viewport |
| Page heading | Scrolls with content unless the task justifies a sticky variant |

An element can remain stationary through grid/flex containment; literal CSS `position: fixed` is not required. Size the frame to usable viewport space, allow grid/flex descendants to shrink, and avoid a body scrollbar competing with the intended content scrollbar. If the product instead uses document scrolling, retain it and define sticky boundaries accordingly.

Account for persistent header/action heights, scroll offsets, safe areas, zoom, and the on-screen keyboard where applicable. Menus and overlays must not be clipped by a local overflow boundary; coordinate their layer/portal rules with the existing component system. Check the final navigation item and final page action at short heights. Never solve overflow by globally clipping useful content.

## 4. Keep navigation and work continuous

For each transition, identify what survives and who restores it:
- List → detail → list: filters, sorting/page, selection where relevant, scroll, and the originating control identified by record ID.
- Detail → edit → detail: record identity and meaningful context; drafts, save/cancel, and unsaved-change policy belong to the page/form owner.
- Direct detail/edit entry: use a valid hierarchy destination when no known internal return context exists. Do not blindly send users out of the application with history.back().
- Collapse or resize: keep the active route and work state. Move focus to a visible control before hiding the element that contains it.

Use the router's existing state/restoration facilities before building another store. Store return context at the appropriate history-entry or route-instance scope, not one global scroll value shared by unrelated pages. If the originating row no longer exists, restore the list context and focus a meaningful surviving heading or control.

Native links retain expected navigation and modifier-key behavior. Disclosure buttons use accurate expanded/controlled relationships and hidden descendants leave the tab order. Follow existing page-change focus management; an actual route change may focus the page heading, while simple menu expansion must not steal content focus. Provide a reachable content entry such as the product's skip link.

## 5. Adapt at the point of failure

Reuse product breakpoints; otherwise find where real labels, page actions, or content stop fitting. Narrowing the desktop sidebar and opening mobile navigation are different states. Preserve the user's desktop collapse preference without forcing it onto the mobile experience.

Use an established compact rail, disclosed panel, or relocated navigation as appropriate. If navigation is modal, implement complete focus containment, inert background, close/Escape, and focus return; if it is nonmodal, retain natural document navigation. A narrow viewport does not automatically require a Drawer component. On route selection, close temporary navigation and place focus at the new content entry. Define what happens if the viewport changes while it is open.

Check around each transition, not only one desktop and one phone size. Short heights may require scrollable navigation and non-sticky page actions even at desktop width. Keep controls usable with long translations and enlarged text; do not shrink the whole interface to make it fit.
