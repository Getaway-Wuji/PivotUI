# Layout and reference

## Source and interpretation

The authoring user specified the Ant Design Pro standard Table list and described its filter area, bulk toolbar, column configuration, pagination and detail-return behavior on 2026-11-14. The structural direction is adopted from that description. Official reference destinations are [Ant Design Pro list](https://preview.pro.ant.design/list/table-list/) and [ProTable documentation](https://procomponents.ant.design/en-US/components/table/).

The authoring web fetch did not expose readable page content; no upstream rendered inspection, source verification or version-specific runtime test is claimed. The detail-return requirement comes from the user. Selection snapshots, failure recovery, keyboard handling and narrow layouts below are supplemental design methods. No pixel dimensions were measured or estimated from an image. Verify the target project's installed library and actual documentation before using its API; this skill does not require Ant Design or redistribute its code.

## Compose around the work

Use the inherited page heading, then the query area, results toolbar, table and pagination. Keep the query and table aligned to the same content edges. Let the table occupy the working space; avoid adding summary cards unless they answer a concrete question about this list. A product's existing shell determines navigation and the content start.

Keep frequent filters visible. Place less frequent criteria behind a clearly named expansion, show when hidden criteria are active, and preserve those values when collapsing. Choose explicit Apply for costly or multi-field queries; immediate filtering can suit inexpensive searches with clear feedback. The user should be able to distinguish what they have typed from what the results represent.

Use the results toolbar for the list title/count and applicable actions. Group primary creation/import work separately from view, column and refresh controls. Show selection count and scope beside selection-dependent actions above the table. Destructive actions should be identifiable without competing with the normal primary task. Avoid repeating an action in every row when it is meaningful only for a selected set.

## Density and reading order

Choose columns from the decisions users make: identity first, useful comparisons and status next, less frequent metadata later. Place contextual actions consistently. Use a real detail link in the identifying cell; optional row click is an enhancement and must not intercept checkbox, link or text-selection behavior.

Reuse the product's density variants. Evaluate row height with realistic two-line names, missing values and status labels before choosing compact mode. Give the primary identifier more emphasis than secondary IDs or timestamps; use existing type roles rather than assigning every cell a unique size. Align comparable numeric values and units consistently. Distinguish zero, absent and loading values.

Long identifiers need wrapping or an explicit accessible full-value route; essential meaning cannot depend on a hover Tooltip. A second line is useful when it preserves row comparison, while verbose descriptions can live in expansion/detail. Do not hide action labels or reduce all text to squeeze in more columns.

## Columns and views

Column configuration controls presentation, not access authorization. Use named checkboxes and a reset to the agreed default; preserve an identification and detail/action route. For hiding, ordering or pinning, support only operations that the component and task need. Define the settings' persistence scope and migrate invalid columns when schema or permissions change. Sensitive fields must not arrive merely because they are visually hidden.

A saved view is a named preset with an explicit scope: for example applied filters, sort, density and columns. Keep selection and in-flight jobs outside saved views. Indicate unsaved view changes. Define whether saving changes only the current user's view or a shared view; sharing requires actual capability and authorization. A simple list may need no view manager.

## Narrow space

Reflow query controls and toolbar groups while keeping scope labels attached to actions. For comparison-heavy tables, retain a labelled local horizontal scroll region; for object-focused work, accessible row disclosure or cards may fit better. Keep every necessary field reachable with its label and every action keyboard/touch operable. Hidden columns need a column chooser or detail route. Verify page and local scrolling separately; sticky regions must not cover focus, pagination or action results. A narrower viewport does not change selection or query semantics.
