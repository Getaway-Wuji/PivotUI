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
| Acceptance | Outcomes relevant to this task, their integration owner, and how they will be checked |

Record actually read skill names and entry points in the working environment if useful. Portable project documents use project-relative paths or skill names, without personal installation paths.

For multiple regions or shared changes, keep a compact acceptance record in the existing project notes: **decision/outcome → integration owner → implementation location → check result and evidence → unverified work**. Establish the decision, owner and intended check before implementation; fill in locations and actual results as work progresses. The same implementer may own all regions and integration. A short local fix can use a brief note instead of a table or new file. Evidence names the checked page/state/device and a locatable result, such as a browser observation, measurement or test; file existence alone establishes implementation, not runtime success.

For ongoing work, keep a compact working note of the selected canonical entries, assigned contributions, already read shared rules/resources and their revision when available, plus remaining capability gaps. Reuse the current context; do not create a new tracking file for every small repair. A backlink does not start a second workflow. After a context reset or changed source, reopen the rules actually needed rather than trusting a stale loaded flag.

## Passing case evidence into a product

First distinguish mood, specific visual borrowing, and requested case comparison/source verification or faithful reproduction. A name used only to describe mood needs a short interpretation and its basis, not an invented case ID or an automatic research pass. For concrete borrowing or case research, add only what affects the decision: source or case ID and revision when available, actual page/surface scope, borrowed traits, retained product rules, evidence type and relevant unknowns. Inspect missing source evidence before attributing specific traits; preserve supplied-image authority for reproduction. Explicit research requests still receive research. Keep recommendations and synthetic demonstrations separate from observations. State what was adopted, what remains provisional, and what still needs implementation or verification. Advice-only output stops at the recommendation.

When a project design document is requested, adapt these decisions into its existing records or `DESIGN.md`: purpose and regions, chosen visual relationships, component conventions, source links, and supplemental interaction/responsive decisions. Link the actual editable token source, or derive any included values from it; do not maintain another independent token table. Preserve the current brand unless the user requested its change. Preparing this document does not invoke Stitch or prove a rendered interface.

## Consolidating tokens

1. Find the existing theme file, CSS variables, or component-library configuration. Where outputs are generated, distinguish the editable source from generated results.
2. For new projects, choose the direction first, then specify the needed colors, typography, spacing, dimensions, and shapes. Do not invent an entire brand merely to fill a table.
3. Adopt an external system, map it to the existing theme, or replace it with project configuration. Keep one maintainable source of truth rather than two independently changing configurations.
4. Check existing semantics and variants before adding values. Use explicit region or component variants for marketing headlines, dense tables, destructive buttons, and similar differences.
5. Determine the impact of global changes, then update the source and affected components. Supporting modules propose changes; the orchestrator consolidates them. Do not assign conflicting values to the same global name in different files.

Track theme definition and theme consumption separately. After building multiple regions or changing shared values, select affected pages/components and meaningful states to check actual theme use and contrast against rendered backgrounds, including portals when present. Classify local constants by shared semantic role, intentional region variant or decorative artwork before proposing changes. Global style can supply validation alone without restarting selection. Record coverage and remaining gaps; reuse valid checks for unchanged consumers.

If an existing purple brand conflicts with an external skill's default ban on purple, preserve the user's brand requirement and look for supported adaptation. If incompatible, use selected guidance or choose another lead. Overriding colors at the end does not establish that the external skill's full checks passed.

Validate against the design goal chosen by the user. Faithful reproduction may deliberately introduce visuals different from an existing brand. If the business brand must remain, establish which parts of the reference apply first.

## Component, interaction, and responsive handoff

- Before layout: inventory shared components and prioritize content and actions on narrow screens. Establish states and transitions early for complex interactions.
- During implementation: the page lead organizes content; the component owner implements reuse and necessary variants. Other capabilities handle their assigned behavior and device concerns.
- After implementation: check the actual page and main flows. Reuse behavior already covered by the lead; supporting modules check or fill gaps.

Assign a clear owner to integrate shared tokens, component interfaces, and global styles. Independent regions can be delegated. Consolidate feedback on a single component instead of having several implementers rewrite it concurrently.

Choose integration checks from the actual change, regardless of how many people or agents are involved:

| Change | Minimum relevant integration evidence |
| --- | --- |
| Shared theme or several newly built regions | Representative affected consumers and states use the adopted theme; real foreground/background combinations have been checked; intentional local variants are identified |
| Shared component behavior or multiple overlay callers | Shared implementation location, affected callers, allowed differences and owner; representative callers satisfy the base contract, including applicable close/focus-return and Portal theme behavior. Initial focus may differ by task |
| Responsive reordering, navigation wrapping, breakpoint hiding or duplicate navigation | Reading and Tab/Shift+Tab order remain meaningful on both sides of the changed breakpoint; hidden copies do not receive focus and focus remains usable during the transition. A Modal-only check does not cover navigation |

Use relevant component/responsive guidance for detailed checks; the current implementer may perform them without another specialist pass. Record static reasoning and runtime evidence separately. Existing evidence may be reused when its implementation and conditions remain valid; check uncovered affected behavior rather than every page and state in the product.

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
