# Portable Shared Design Foundations — Application Shell Design

Synchronized excerpt from *Shared Interface Design Foundations* **0.2** and *Orchestrating Authored and External Design Skills* **0.5.0**. Read only when the target project lacks its own design standards; inside the full cluster, the edition's `design-system/FOUNDATIONS.md` and `design-system/ORCHESTRATION.md` remain authoritative.

## Core invariants

- **Task-first hierarchy:** Organize layout, grouping, alignment, and emphasis around what the user must understand, decide, and do.
- **One authoritative token source:** Reuse the target product's existing CSS variables, theme objects, or component library configuration. Express region differences as explicit named variants; never maintain two independently editable themes or push client brand defaults back into the skill library.
- **One owner per region and component:** A named page lead owns region composition; shared components have one integration owner; specialists fill concrete gaps rather than running as a mandatory pipeline.
- **Realistic content and complete states:** Handle long text, mixed Chinese/Latin copy, tabular numbers, zero vs missing vs unloaded values, loading, empty, error, permission, focus, and keyboard states.
- **Overlay and safety boundaries:** Tooltip explains briefly; Toast carries lightweight non-error feedback (never errors); Alert persists problems; Modal guards irreversible actions; Popconfirm covers low-risk local confirmation; Drawer preserves editing context without absorbing full-screen workflows. `gpt-taste` is restricted to public marketing and never used in dashboards or business tools.
- **Responsive and scroll discipline:** Adapt content and controls to available width, height, and input capability without global horizontal clipping or hiding critical business fields. Separate shell scrolling from local table/panel scrolling.
- **Honest verification:** Distinguish static document inspection, script validation, rendered browser checks, and physical-device testing. Never report unperformed checks as passed.
