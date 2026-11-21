# Detail Page Layout and Sections

## Header anatomy

Place inside the application shell's content header slot:

1. **Return link / breadcrumb context:** Return to the exact source list entry when coming from a list; fall back to the parent list route on direct deep links.
2. **Primary identity:** Record display name, copyable stable ID (monospaced/tabular), and current lifecycle status badge (color paired with text).
3. **Key summary metadata:** Up to 3–5 high-signal facts (owner, last updated, priority, amount/count) so users confirm they opened the right record before scrolling.
4. **Action cluster:** One clear primary action (e.g., Edit, Approve), secondary actions, and destructive actions separated into a secondary menu or clearly isolated trigger with confirmation.

## Choosing stacked sections vs tabs vs split summary

| Record complexity | Recommended structure | Caution |
| --- | --- | --- |
| Compact entity (1–3 groups, no heavy sub-tables) | Single column or 2-column description grid + stacked sections | Avoid adding tabs for fewer than 3 substantial domains |
| Medium entity with metadata + activity feed | Main content column (details + related table) + secondary summary/activity rail on wide screens | Collapse rail cleanly in logical reading order on narrow screens |
| Rich entity with independent sub-domains (Overview, Items, Billing, Audit Log) | Persistent identity header + Tabs switching sub-domains | Sync active tab to URL or route state; keep critical status alerts visible above tabs |

## Field formatting rules

- Align numeric amounts, quantities, and timestamps with `font-variant-numeric: tabular-nums`.
- Distinguish explicit zero (`0`), empty/unset (`—` or `Not set`), masked/redacted, and still-loading values.
- Support long names, multi-line notes, and variable badge counts without clipping labels or pushing actions off-screen.
- Keep related sub-tables scoped: small inline tables belong here, while full filter/bulk/export list management routes to `data-list-design`.
