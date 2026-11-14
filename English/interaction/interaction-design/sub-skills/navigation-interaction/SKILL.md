---
name: navigation-interaction
description: Handle current location, expansion, keyboard input, and focus continuity in sidebars, breadcrumbs, collapsible navigation, page tabs, and command menus while preserving established information architecture.
---

# Navigation Interaction

This is an on-demand submodule of `interaction-design`. Inherit scope, tokens, evidence labels, and optional project conventions from the [root entry](../../SKILL.md); do not reload established context. When entering directly without it, read only the root's “Scope and Existing Decisions.”

Own navigation behavior while preserving the page lead's information architecture, routes, and layout. hover/focus indicate temporary exploration, current indicates actual location, and expanded indicates group disclosure. These states can coexist; temporary highlighting must not replace the true route. The following are implementation recommendations, not runtime findings from static references.

## Identify Navigation Semantics

| Type | State source and input model | Avoid |
| --- | --- | --- |
| Site/sidebar links | href or actual route; native links and natural Tab order | Applying command-menu arrow navigation merely because the visual component is named Menu |
| Collapsible group | Button controls expanded; Enter/Space toggles it | Ambiguous link/disclosure roles or hidden descendants remaining tabbable |
| Breadcrumbs | Hierarchical ancestors of the current page | Treating browsing history as hierarchy or marking every segment current |
| Same-page tabs | Selected tab and corresponding panel | Applying tab semantics to route links or radio values |
| Row actions/command menu | Focused menu item and actual command | Treating hover as execution or trapping Tab inside a nonmodal menu |

## Sidebars, Groups, and Breadcrumbs

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| Route actually changes | current updates | Current-page indicator agrees with content; use link `aria-current="page"` where appropriate | Failed navigation retains the actual location; pressing alone must not permanently change current |
| Another item is hovered/focused | Temporary emphasis changes | Focus ring and current-item marker both remain clear | Leave/blur returns to actual current; clear temporary state if there is no current item |
| Group expands/collapses | expanded toggles | Icon and `aria-expanded` agree | Before hiding focused content, move focus to a suitable disclosure control; hidden items lose focusability |
| Sidebar narrows | Width/label presentation changes | Icons retain names; current page remains identifiable | Preserve focus and route; essential entries must not be recognizable only on hover |
| Breadcrumb ancestor activates | Navigate to that level | Path and page title agree | Preserve native link/back behavior; current-page text usually needs no repeat navigation |

When a group heading both links and expands, provide distinguishable link and button controls. One activation must not both collapse and navigate. Sidebar adaptation belongs to the responsive capability or current implementer. Narrow screens do not automatically mean Drawer, and a local interaction task does not authorize redesigning all navigation.

Use a named navigation landmark and ordered hierarchy for breadcrumbs. Links follow natural Tab order; separators are not extra focus stops. A linked current page uses `aria-current="page"`; plain text need not become a button. Sources: [APG Breadcrumb](https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb/), [APG Disclosure](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/).

Follow the application's existing title, focus, and scroll management after client-side navigation. Ordinary hover, disclosure, or background refresh must not steal main-content focus. Actual page changes or returning to a list should restore the content entry or prior action location according to the task.

## Page Tabs and Command Menus

| Trigger | State change | User feedback | Exit or recovery |
| --- | --- | --- | --- |
| Arrow key moves within tabs | Focused tab changes; immediate selection depends on policy | Distinguish focus from the displayed panel | With manual activation, Enter/Space changes panel; Tab enters subsequent content |
| Command-menu button activates | collapsed → expanded; focus enters items | Current item is clear; trigger state agrees | Esc closes and returns to trigger; Tab closes and continues normal focus order |
| Menu navigation/execution | Item focus moves or command executes | Item names and unavailability reasons are understandable | Position focus for the next flow; if trigger disappears, choose a sensible fallback by stable object identity |

Follow component-library orientation, Home/End, and focus management for tabs. Consider automatic activation only when panels appear immediately. Network-loaded panels need explicit activation so each arrow step does not trigger waiting. Hidden panels must not retain focusable descendants. Source: [APG Tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/).

Command menus use appropriate arrows, Home/End, and typeahead where relevant, scoped to the component. Esc exits nested menus one level at a time. Closing animations must not leave hidden items tabbable. Restore row-menu focus by stable row ID; after sorting or filtering, an old index must not target another record. Source: [APG Menu Button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/).

Read [floating components](../floating-components/SKILL.md) when navigation needs Tooltip or commands need confirmation/result feedback. Tooltip must not carry important feedback, and Toast must not display errors. Check creative-menu gaps in semantics, Esc, focus, and reduced motion through [React Bits integration](../../references/react-bits.md); creative menus are not ready-made business modal Drawers.

## Delivery Checks

- Current page, temporary hover, focus, and group expansion remain distinct; failed routing leaves no false current state.
- Sidebars and breadcrumbs are fully keyboard-accessible; hidden items are unfocusable, and disclosure retains sensible focus.
- Menu Esc and Tab follow their respective exit paths; removed, reordered, or filtered rows retain a reliable focus destination.
- Tab activation matches loading latency; local controls do not capture global keyboard input or scrolling. Report only checks actually performed.
