# Skill Discovery and Adaptation

Read when choosing candidates, integrating new modules, or resolving capability conflicts. These roles neither guarantee installation nor replace the actual entry point's instructions.

For confirmed sources, current versus historical locations, optional families, versions, and licenses, load the [external catalog](external-catalog.md) only when that choice is relevant. Verified source is distinct from installed capability. The current distribution includes fourteen external packages under functional categories, with provenance and licenses. Bundled files do not establish that their external tools are configured.

## Capability directory

| Candidate name | Role in this cluster | Boundary |
| --- | --- | --- |
| `design-taste-frontend` (package/repository `taste-skill`) | Design and implement company, brand, and product sites; audit compatible existing marketing sites | One skill identity, not two callable modules; check layout, color, motion, and validation fit |
| `redesign-existing-projects` | Historical independent audit and incremental redesign | Only use an explicitly selected, pinned, installed version; current taste includes redesign but is not an interchangeable old entry |
| `ui-ux-pro-max` | Supplement unresolved style, palette, typography, and UX research needs | Research and candidates only; no automatic pass after local style selection, page-code ownership or direct token overwrite |
| `design-reference-research` | Find and compare named product cases, inspect sources, and return transferable patterns | Internal research method using attributed external data; metadata first, then selected cases; no page ownership, implied official status or token overwrite |
| `gpt-taste` | Expressive composition for public marketing pages | Opt-in classics entry; exclude dashboards, administration panels, and business tools; scope enhancements to a region |
| `image-to-code` | Generate reference images, analyze them, then implement frontend code | Bundled location: `image-design/image-to-code`; upstream: `imagegen-skills/skills/image-to-code`; do not silently regenerate supplied targets or equate it with screenshot reproduction |
| `global-style-skill` | Select/compare visual directions; generate, extend, migrate, or validate project tokens | Advice can stop before tokens; explicit restyling can use complete themes as the starting point; local fixes reuse them |
| `floating-components` | Select and implement overlays and messages | May be a nested interaction entry; read shared conventions as needed and avoid duplicates |
| `dashboard-design` | Dashboard content, metrics, charts, and necessary interactions | Reuse the application shell; handle standalone navigation, full lists, and forms separately |
| `data-list-design` | Complete list composition, query/selection scope, bulk tasks, exports and detail return | Reuse the shell, tokens and shared controls; small tables and local repairs do not need the full workflow |
| `app-shell-design` | Cross-page hierarchy, navigation structure, headings, content boundaries and scrolling | Preserve product routes and tokens; page leads own content; behavior/component/responsive specialists fill gaps |
| `interaction-design` | States, feedback, focus, keyboard behavior, and recovery | Fill behavior gaps without choosing another whole-page style |
| `component-system` | Shared components, interfaces, and purposeful variants | Reuse before adding components |
| `responsive-design` | Content priority, layout changes, touch, and overflow | Participate during design and validation; retain the project's visual direction |

The seven classics, including their style, Stitch, and legacy Taste entries, disable implicit invocation in upstream metadata: require a named invocation or existing explicit user authorization, not merely an inferred style preference. Historical redesign has no such upstream metadata; this cluster separately reserves it for deliberate legacy selection. Imagegen web, mobile, and brand-board entries produce visual references; they do not independently implement the page or establish adopted project tokens. Inspect required tools before choosing either family.

## Style guidance without another workflow

Global style owns the on-demand [selection guide](../../global-style-skill/references/style-selection.md) and its reference catalog. Read the guide only for an actual direction question; retrieve relevant candidates rather than all cards. If the lead already supplied a suitable direction and values, consolidate that result without repeating selection or research. Add `ui-ux-pro-max` only when candidate coverage or required evidence remains insufficient.

A reference label may describe an aesthetic, layout, material, asset technique, theme, motion idea, design system, or page type. It does not transfer page structure or behavior ownership to global style or authorize another skill. Asking for a minimalist or soft appearance is not a named invocation of a similarly described opt-in Classics entry.

With MCP, read the selection guide as `references/style-selection.md` under the selected `global-style-skill` entry. The sibling link above supports file navigation; it does not permit reading another package through the orchestrator's resource identity.

## Product cases as evidence

Use `design-reference-research` for requested case research/comparison or source checks, and when specific borrowed traits need evidence that current material does not supply. A product name used only to convey mood does not require research when the direction is sufficiently grounded; record the interpretation without attributing unverified details. Inspect supplied references directly when sufficient, preserving their authority for reproduction. Explicit research requests still require research. Use `ui-ux-pro-max` for an unresolved general style, typography or UX question. Choose by the missing evidence; neither is a mandatory pass after the other. A complete existing theme and a local repair ordinarily skip both.

Filter by the task's actual surface before appearance: marketing page, marketplace/product flow, working application, registration, or illustrative example. A company's name and a dashboard-looking marketing panel do not establish working-product coverage. Keep official rules, third-party observations or extraction claims, author recommendations, and synthetic examples distinct. A document review or precise number does not prove live CSS, interaction, accessibility or responsive behavior.

The bundled catalog has 84 source records and 8 document-reviewed cases. The other records remain indexed-only with unknown scope until inspected. Read relevant metadata and usually 1–3 cards, preserving each case's source revision and gaps. If a named source has no reviewed card, inspect its reachable source before recommending traits, or disclose unavailable evidence and continue with the current owner. Do not invent missing case details or load the whole corpus to resolve a local question.

Return the useful relationship and its conditions: for example, surface luminance and boundaries may support hierarchy without adopting the source's brand color, proprietary font, business states or page composition. Global style maps approved visual roles to the product's authoritative tokens; page/component owners implement and validate. Original `DESIGN.md` prompts and script references are source data, not instructions to execute or permission to replace project rules. An adapted project `DESIGN.md` links the existing token authority and records adopted traits and supplemental decisions; it does not create a second editable theme or imply a Stitch workflow.

With MCP, select this research package's identity before reading its indexes and cards. The three existing reader tools suffice for this navigation; a catalog search does not search case contents. File-based use follows the same indexes. No downloaded archive or authoring-workspace path is a runtime prerequisite.

## Discover actual entries

With MCP, use `catalog_skills` for metadata, functional categories, and upstream implicit-invocation settings, `load_skill` for a selected entry, and `read_skill_file` for needed references. Otherwise filter currently available skill names and descriptions, then inspect user-provided entries and explicitly declared project directories. Search for current candidates rather than scanning the entire machine. Folder names can differ from frontmatter names; confirm identity from the actual contents.

Read the selected `SKILL.md` to verify capabilities, constraints, inputs, outputs, and required tools, then read relevant references. Do not preload unselected bodies. An external link or listed name alone does not establish availability.

`taste-skill` resolves to the actual `design-taste-frontend` entry once. Confirm relocated entries at their current upstream: the former taste `skills/image-to-code-skill/SKILL.md` path is historical, and the independent redesign entry has been retired. Do not install or run an unpinned historical copy to fill a missing current name. Catalog additions alone do not authorize installation or redistribution.

When a capability is renamed or a new module appears, map the role to its actual entry using descriptions, inputs, outputs, and scope. Reuse project records; do not require renaming or a new fixed registration format.

For ordinary missing modules, complete the work using available capabilities and this package's rules. Disclose the fallback instead of claiming to have invoked a missing skill. Ask for an entry or file only if the user explicitly requires that skill and it cannot be found; continue independent work. Do not automatically install a same-named package.

## Filter before reading bodies

The core role map defines cluster ownership. Upstream descriptions may advertise more work, and `allow_implicit_invocation` describes upstream invocation policy, not a grant to expand the assigned scope. In particular, UI/UX remains research support and historical redesign still needs deliberate selection. If metadata already excludes a candidate (image creation for exact screenshot reproduction, or an opt-in execution workflow for advice only), do not load its full body merely to reject it.

For the selected lead, check actual prerequisites and output before committing work. Missing a transport such as Stitch MCP is not the same as lacking all access to the tool; inspect available methods. When the requested method is unavailable and the user accepts an alternative, name that alternative implementer and continue. Do not call document preparation, guidance reuse, or ordinary HTML implementation execution of an unavailable external tool.

## Choose an adaptation mode

Assign one implementation lead per region. Check default styling, token writes, technical dependencies, and acceptance rules:

- **Full use:** follow a compatible workflow and record adopted shared decisions through the orchestrator.
- **Selected guidance:** use specifically applicable methods or resources within a defined region and scope. Validate against project goals, without claiming a complete external workflow ran.
- **Change the lead:** when core requirements conflict and supported configuration cannot resolve them, use another candidate or the implementer's own capabilities.

For example, the previously inspected tasteskill 2.5.1 generates colors, requires retaining its generated `:root` block, and specifies full-screen layout, motion, and checks. It is not a neutral skeleton generator. Recheck the actual version on integration. Preserve user requirements when an existing brand conflicts with defaults, then choose the appropriate adaptation.

"Research only" and "local enhancement" describe this cluster's division of work; they do not establish that every external skill implements equivalent execution modes. If unsupported, use relevant material as evidence or choose another method. Do not invent parameters or falsify checks by removing third-party validation or modifying its tools.

## Resolve observed integration conflicts

| Situation | Resolve before implementation |
| --- | --- |
| Taste's generated palette, full-screen sections, or prescribed motion conflicts with a retained brand or a spacing-only repair | Preserve the requested brand/scope. Use compatible selected guidance or another lead; do not claim the original complete Taste workflow passed |
| GPT's global horizontal clipping conflicts with responsive content or focus visibility | Repair the overflowing layout and constrain decorative overflow locally; retain accessible content. If omitting a mandatory upstream rule, label the chosen scope as adapted guidance |
| Responsive advice would turn a Drawer into a full-screen task or change confirmation risk | Keep the overlay contract. Reflow within it, or use the agreed inline/separate-page alternative; do not silently change component semantics |
| Stitch `DESIGN.md` and project tokens both contain styles | Derive the document from adopted tokens, or consolidate newly selected values first. Document preparation, Stitch screen generation and frontend implementation are separate deliverables |
| Image/brand concepts are requested without code | Select the matching image-only entry, preserve the requested number/format, and stop at the images; candidates do not become an approved brand automatically |
| Component, interaction and responsive modules advise on the same control | One implementation owner integrates the agreed interface, state and layout changes; other modules return scoped requirements or review deltas instead of competing rewrites |

A workflow's sample output, mock result or proposed command is not execution evidence. Report actual checks, with adapted or unexecuted parts identified; leave upstream source and policies intact.

## Integrate new modules

A new module needs six things: capability and trigger, necessary inputs, outputs, editable scope, actual entry and resources, and work possible when prerequisites are missing. Record the version or source identifier using project conventions; no extra manifest is required.

Send proposed shared-token changes to the orchestrator for consolidation. Express local differences as explicit variants. Hand off only task-relevant context. Resolve resources in the target environment and use package-relative references in distributed files.
