# Optional Dashboard Interactions and Navigation Adaptation

Use this guide after choosing information structure to decide whether interaction enhancements are needed. It synthesizes and extends the references; it does not claim that screenshot animations, keyboard operation, or state management were implemented.

Sources: S01–S13 for navigation/motion, S20–S25 for glass interactions, and S32–S37 for navigation/content switching. See the [source summary](reference-index.md) for IDs. The conditions and behavior specifications below work independently of original images or per-image notes.

For existing products, inherit the shell, navigation components, routes, and motion preferences. Navigation choices here are conditional adaptations; they do not authorize Dashboard-wide ownership of the application shell. Keep stable, clear default behavior when enhancements are unnecessary; do not add every effect.

## 1. Define what each control changes

| Control meaning | Scope of change | Must stay synchronized | Sources |
| --- | --- | --- | --- |
| Page navigation | Open another page/view | Route, page title, main content, current location | S32, S37 |
| Entity switching | Switch among stores, warehouses, greenhouses, etc. | Entity name and all its metrics, trends, tasks, and details | S33 |
| Time/dimension filtering | Change data scope or perspective | Affected modules, scope labels, comparison periods, units, export scope | S01, S04, S18 |
| Module tabs | Switch views/content inside one module | Selected tab, corresponding panel, context | S02, S06 |
| Quick actions | Create, record, export, or another concrete action | In-progress state, outcome feedback, related data | S06 |
| Visual demonstration controls | Demonstrate styling/transitions only | State their demonstration purpose; do not impersonate real navigation | Original S36 prompt |

S36's original prompt permits updating only selection while leaving the main content unchanged. This is valid only for a menu-style demonstration. A real product must not label unchanged Dashboard content “Shoots” after selecting Shoots. Likewise, a real entity switch must not update only a yield card while retaining another entity's environmental data and tasks.

Current item, hover, and keyboard focus are distinct: current indicates location, focus identifies the next keyboard target. One state must not erase another's visibility.

## 2. Choose navigation conditionally

| Pattern | Use when | Avoid or switch when | Required adaptation | Sources |
| --- | --- | --- | --- | --- |
| Icon-and-text sidebar | Destinations need learning; names matter more than saved width; several levels exist | Very narrow workspace, few familiar destinations | Allow collapse; preserve grouping and clear current location | S32 |
| Top pills/text menu | Few stable top-level destinations and enough horizontal space | Long labels, hierarchy, or growing destination count | Scroll or collect items on narrow screens; keep labels recognizable | S36 |
| Transparent top bar | Controlled first-screen background, few destinations, continuous brand imagery | Changing photographs obscure text; navigation is complex | Add a stable background when needed; selection/focus cannot depend on opacity alone | S01 |
| Expanded label for current item | Experienced users, recognizable icons, manageable count | Many unfamiliar icons or repeated layout jumps | Reserve overall navigation width; name noncurrent icons too | S02 |
| Icon rail + large title | Few-page tools needing content width | Unfamiliar low-frequency functions or complex hierarchy | Synchronize title/content; place scope selection near the title | S04, S35 |
| Icon rail + Tooltip | Frequent expert use with a meaningful benefit from saved width | Touch users cannot recognize icons; key labels must remain visible | Names on hover and focus; expandable labels for touch | S05, S34 |
| Right-hand rail | A complete work canvas is explicitly needed and users accept right-side navigation | Existing left shell; relocation adds learning cost | Separate creation from navigation; preserve usable content width | S03 |
| Peer-entity tabs | A few stores/warehouses/greenhouses switched frequently | Many objects, long names, or cross-organization search | Use searchable selection/grouped lists instead; update entity data consistently | S33 |
| Bottom Dock | Few recognizable destinations in a light personal workspace | Hierarchical enterprise tools, dense tables, or permanently visible text menus | Reserve bottom space, show focus, name the current item | S24 |
| Quick-action column | A few frequent actions substantially shorten workflows | Rare/unclear actions or confusion with navigation | Name actions; handle progress/failure; collect them on narrow screens | S06 |

Right rails, Docks, and icon rails redistribute space; they do not create extra screen width. Evaluate readable content width, recognition effort, touch targets, and overlay coverage together.

## 3. Lightweight state feedback

### Sliding highlights and liquid pills

- Sources: S11 sliding highlight; S20 directional stretch and spring-back.
- Explain movement between current items. Establish a clear final selection before deciding whether sliding or slight elasticity helps.
- Move only the background highlight layer; do not shift menu text, hit targets, or the entire layout.
- Rapid selections interrupt and redirect toward the latest target; do not queue obsolete animations.
- Keep focus rings independent. A moving selected background does not replace focus management.
- With reduced motion, switch directly or fade lightly. Routing/data updates must not wait for animation completion.

### Data entry and updates

- Source: S08. Counting from zero and sequential line drawing are source-prompt presentation effects, not business requirements.
- A low-frequency overview may enter subtly. Live monitoring, monetary reconciliation, and precise comparisons should show actual values directly so intermediate numbers are not misread.
- Show loading before data returns. Distinguish missing values, zero, denied permission, and failure; animation must not conceal data status.
- When refreshing retained values, show updating and data time. On refresh failure, retain old values if useful and mark them stale; do not silently treat them as new.
- When entity/time scope changes, establish the target scope and loading state. Late responses from previous requests must not overwrite the new scope.
- Periodic refresh preserves filters, scroll, expansion, selection, and chart-reading position. Do not replay all entrance animations on every update.
- Critical exceptions remain timely and visible. Ordinary updates must not steal keyboard focus. Use concise status announcements when needed rather than repeatedly announcing every number.
- Keep comparison chart axes interpretable. If rescaling is necessary, show axis context so scaling alone does not create an apparent sudden trend change.

## 4. From overview to detail

### Link charts, objects, and records

- Before an exception, bar, or object is clickable, decide whether it highlights explanation, filters current details, or navigates to detail. Feedback must match the result.
- For inventory, selecting “Out of stock” filters details to those objects and states the applied condition. Selecting a product synchronizes its map/summary/details. Explicitly state the retained scope of areas not participating in the link.
- Show selected items, counts, and filter labels; offer clearing and return paths. Explain how multi-selections combine so invisible conditions do not accumulate.
- Preserve overview context when no detail matches, permission is denied, or detail loading fails. Opening a new detail must not accidentally trigger another filter; returning restores selection and position.

### Card expansion or in-place enlargement

- Sources: S12 task-panel expansion; S22 main view with bottom thumbnails.
- Use to inspect one metric's trend details or a bounded task set while preserving its relationship to the overview.
- Detail adds actual content, explanation, or actions, rather than merely enlarging the same card. For simultaneous module comparison, use side-by-side layout, a sidebar, or a dedicated comparison view.
- Decide whether this is in-flow expansion, side detail, a Modal, or a separate page before implementing its behavior. Mixed modes cause scrolling/focus confusion.
- Preserve the triggering module, entity, period, filters, and scroll context on open; return to the same module and a sensible position on close.
- A Modal needs visible close, Esc, contained focus, and focus return. Inline expansion needs explicit expanded/collapsed state without unnecessarily locking the page.
- Hidden original content must no longer accept accidental clicks/focus. Bottom thumbnails need readable names and current-item states, not recognition from miniatures alone.
- S12's four-cards-per-row is only a desktop reference. Column count follows minimum readable content width; narrow layouts may use a detail page with Back.
- With reduced motion, show detail directly and preserve logical context. Return behavior must not depend on animation.

### 3D flipping

- Source: S10. Consider only for an explicitly preferred brand experience, low-risk cards, or demonstrations; it is not a general detail-entry pattern.
- Prefer expansion or side details for comparison, repeated chart reading, or live alerts. Never hide key metrics/alerts on the back.
- Use explicit “View details”/“Back to overview” buttons. Do not bind whole-card clicks to flipping when the card already contains buttons, chart interactions, or links.
- If both faces exist, only the visible face is interactive/focusable. Support touch and keyboard. With reduced motion, switch content directly.

## 5. Personal layouts and presentation-only collapsing

### Drag reordering

- Source: S09. Suitable for long-term workspaces where roles truly need different module orders.
- Provide a useful default first. Without a personalization requirement, retain fixed structure to reduce maintenance and learning effort.
- Use an “Edit layout” state and handles to distinguish dragging from chart brushing, text selection, scrolling, and card actions.
- Show valid targets, placeholders, and affected modules. Respect minimum readable card dimensions; moving across rows/columns does not mean unrestricted overlap.
- Provide keyboard reordering or Move up/Move down alternatives, with readable result feedback. Dragging must not be required to complete the task.
- Save the personal layout and communicate the outcome; support cancel/undo and reset. Do not show “Saved” after failure.
- Use an independent reading order or a reasonable mobile transformation. Do not squeeze unchanged desktop three-column coordinates into one column; retain an understandable module order.

### One-click aggregation

- Source: S13. Here “aggregation” means cards gathering toward the center, not mathematical aggregation of business values.
- Use only for an explicitly requested demonstration or optional collapsing mode; never as the default for business review, alerts, or task execution.
- The collapsed state needs a clear restore action and mode label. Critical-alert access remains available. Restore layout, filters, module states, and focus context.
- Do not use it when collapsing hides information required for the current task. With reduced motion, switch directly to a concise list/collapsed state.

## 6. Command palette

Source: S23. The screenshot does not show an open palette; the search overlay, results, and keyboard states require additional design.

- Useful for experts frequently navigating across modules, as a supplement to existing navigation. The Dashboard specifies integration needs; the shell owns the global entry and route consistency.
- Provide a clickable entry. Choose usable ⌘K/Ctrl+K shortcuts for the host and handle existing conflicts.
- Focus the search field on open. If modal, prevent accidental background operation. Results show name, type, and current location rather than isolated icons.
- Filter as the user types and show no-match results. Arrow keys move the active result, Enter executes, Esc closes. Do not intercept normal IME composition.
- Return focus to the entry/previous position on close. After navigation, focus a sensible point in the new view rather than an unmounted search input.
- Distinguish page navigation, entity search, and direct commands through grouping/copy. Executing commands is a separate feature, not automatically implied by filtering a menu.
- Generate results from actual permissions and scope. Handle absent versus inaccessible results according to product conventions.
- Glass and background blur are optional materials. Result contrast, selection, and keyboard focus remain clear regardless.

## 7. Cursor-following light, hover tilt, and Dock magnification

- Sources: S21 light tracking/slight tilt; S24 proximity-based Dock magnification. All are optional presentation effects.
- Use on a few presentation cards or explicitly preferred brand details. Do not tilt dense tables, precise chart coordinates, or content being edited.
- Confine tracking light to decoration. It must not intercept clicks, reflow text, or encode business status. Information and functions remain complete without the effect.
- S21's maximum four-degree tilt is a source-specific limit, not a global default. Keeping only a brighter border is valid.
- Dock magnification must not shift stable hit targets or cover adjacent content. Reserve space for maximum extent. Focused icons also show their names.
- Touch defaults to a stable presentation without mouse-hover simulation. Keyboard uses ordinary focus/text feedback. Reduced motion disables tracking displacement, tilt, and proximity magnification.
- If glass and dynamic light impair text, add a solid surface or remove the effect. Brand expression does not take priority over work content.

## 8. Deliver and verify

Validate only selected patterns. Distinguish what the reference shows, what this design adds, and what was actually verified.

| Check | Observable success |
| --- | --- |
| Route/entity/filter consistency | Selection, headings, data scope, tasks, and exports share one context |
| Keyboard and touch | Essential operations do not require hover/dragging; focus is clear; touch users can recognize entries |
| Open and close | Clear entry, exit, and return; hidden content does not receive focus |
| Data updates | Rapid switching cannot let old results overwrite new ones; refresh preserves state; failure/staleness are distinct |
| Reordering | Valid targets, saving, failure feedback, resetting, and alternative operations work |
| Motion preferences | Reduced motion retains functions/current state; operations do not await animation |
| Content boundaries | Dock, sidebars, and overlays do not cover current actions; long labels/narrow screens remain readable |
| Static design delivery | Unimplemented interactions are labeled behavior specifications, without claiming tested clicks, switching, or animation |

Pass the selected pattern, conditions, and consistency requirements to the page-shell module. Pass filtering context and entry/return behavior to data-list/detail modules. Preserve ownership boundaries so a product does not acquire independent competing navigation and state rules.
