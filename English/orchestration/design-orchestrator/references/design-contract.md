# Project Design Agreement and Handoff

Read this when establishing shared styles, coordinating regions, resolving external-skill conflicts, or continuing across chats. Reuse the target project's records. Local fixes need only key decisions, not an additional documentation system.

## Working agreement

Before implementation, record the following briefly. Fill in known information directly; do not require the user to answer every item.

| Item | What to establish |
| --- | --- |
| Goal and scope | Page or region, user task, proposal or implemented interface, allowed changes |
| Reference purpose | Faithful reproduction, selected inspiration, existing brand, or new direction |
| Responsibilities | One lead per region, specific supporting contributions, and work the current implementer covers without a matching skill |
| Design sources | Actual token or theme location, existing components, adopted style, and provisional choices |
| Behavior and devices | Necessary states, primary actions, target devices, and motion scope |
| Acceptance | Deliverable locations and outcomes relevant to this task |

Record actually read skill names and entry points in the working environment if useful. Portable project documents use project-relative paths or skill names, without personal installation paths.

For ongoing work, keep a compact working note of the selected canonical entries, assigned contributions, already read shared rules/resources and their revision when available, plus remaining capability gaps. Reuse the current context; do not create a new tracking file for every small repair. A backlink does not start a second workflow. After a context reset or changed source, reopen the rules actually needed rather than trusting a stale loaded flag.

## Passing case evidence into a product

For named references or case research, add only what affects the decision: case ID and source revision, actual page/surface scope, the traits being borrowed, retained product rules, evidence type and relevant unknowns. Keep recommendations and synthetic demonstrations separate from observations. State what the owner adopted, what remains provisional, and which behavior still needs implementation or verification. Advice-only output stops at the recommendation.

When a project design document is requested, adapt these decisions into its existing records or `DESIGN.md`: purpose and regions, chosen visual relationships, component conventions, source links, and supplemental interaction/responsive decisions. Link the actual editable token source, or derive any included values from it; do not maintain another independent token table. Preserve the current brand unless the user requested its change. Preparing this document does not invoke Stitch or prove a rendered interface.

## Consolidating tokens

1. Find the existing theme file, CSS variables, or component-library configuration. Where outputs are generated, distinguish the editable source from generated results.
2. For new projects, choose the direction first, then specify the needed colors, typography, spacing, dimensions, and shapes. Do not invent an entire brand merely to fill a table.
3. Adopt an external system, map it to the existing theme, or replace it with project configuration. Keep one maintainable source of truth rather than two independently changing configurations.
4. Check existing semantics and variants before adding values. Use explicit region or component variants for marketing headlines, dense tables, destructive buttons, and similar differences.
5. Determine the impact of global changes, then update the source and affected components. Supporting modules propose changes; the orchestrator consolidates them. Do not assign conflicting values to the same global name in different files.

If an existing purple brand conflicts with an external skill's default ban on purple, preserve the user's brand requirement and look for supported adaptation. If incompatible, use selected guidance or choose another lead. Overriding colors at the end does not establish that the external skill's full checks passed.

Validate against the design goal chosen by the user. Faithful reproduction may deliberately introduce visuals different from an existing brand. If the business brand must remain, establish which parts of the reference apply first.

## Component, interaction, and responsive handoff

- Before layout: inventory shared components and prioritize content and actions on narrow screens. Establish states and transitions early for complex interactions.
- During implementation: the page lead organizes content; the component owner implements reuse and necessary variants. Other capabilities handle their assigned behavior and device concerns.
- After implementation: check the actual page and main flows. Reuse behavior already covered by the lead; supporting modules check or fill gaps.

Assign a clear owner to integrate shared tokens, component interfaces, and global styles. Independent regions can be delegated. Consolidate feedback on a single component instead of having several implementers rewrite it concurrently.

## Shell and page return ownership

For shell/page combinations, the shell exposes route identity, heading/action slots and actual scroll containers; the page owns query, selection, draft and result validity. Reuse the product state mechanism and name one return coordinator. Restore the correct route instance, resolve data/permission changes, then restore valid page/local positions and stable-record focus once. A page must not assume `window` is the shell scroll container; independent navigation and page effects must not race to restore focus. Read the relevant module guidance only for concrete gaps.

## Persisting and resuming work

For multiple pages or chats, update existing design records first. When no record exists and continuity requires one, an optional `design-system/PROJECT.md` in the target project can track the adopted direction, token source, region responsibilities, and unfinished work. This is not a runtime dependency.

Record the current effective state:

- Adopted brand and component rules, plus provisional choices.
- Region leads, scope of reference adoption, and actual deliverable locations.
- Related files and references that can be reopened; attachments in one chat may be unavailable elsewhere.
- Checks completed, aspects not actually verified, and remaining work.

Use project-relative paths. Do not duplicate every skill's instructions or write a client's tokens back into this library as defaults for all projects.

Read current files before resuming. Continue from unfinished work when previous results remain valid. Change the route only when requirements, available capabilities, or observed evidence change.
