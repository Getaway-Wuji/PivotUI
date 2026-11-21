---
name: design-orchestrator
description: Lightweight entry point for a UI design skill cluster. Match the requested deliverable and scope to independent skills, assign regional ownership, and consolidate project tokens for websites, dashboards, references, components, interactions, and responsive work.
metadata:
  version: 1.2.7
  tags: [orchestration, routing, ownership, handoff, tokens]
---

# Design Orchestrator

Identify the task, choose the smallest sufficient set of skills, consolidate shared decisions, and continue to the requested deliverable. Selected modules own their detailed methods. Do not merge their bodies into this entry or replace an implementation request with a routing plan.

## Determine the assignment

Start with the deliverable: advice, audit, design images, tokens, or implemented code. Then establish change scope, reference authority, existing theme/components, page purpose, and available tools. A local issue takes precedence over the page's general category. Reuse supplied context; explicit user requirements take priority. Consult target-project conventions or the portable [foundations](references/foundations.md) only for relevant gaps.

## Match responsibility to need

This is a role map, not a sequence to run. Choose an appropriate lead and add a specialist only for a concrete gap or requested independent review.

| Need / trigger | Owner and output | Boundary / conditional support |
| --- | --- | --- |
| Select/compare a visual direction, or create/change/check shared design values | `global-style-skill`: recommend direction; generate or validate tokens as needed | Reuse suitable direction/values already provided by the theme or lead; explicit restyling can require selection even with complete tokens |
| Business overview, analytics, monitoring, workspace | `dashboard-design`: content hierarchy, metrics, charts and necessary states | Own the dashboard region; reuse its adequate component, interaction and narrow-screen behavior |
| Complete administrative data list | `data-list-design`: information priority, query/results, selection, bulk tasks, export scope and detail-return continuity | Reuse the product shell and tokens; Table/shared controls belong to `component-system`; add interaction or responsive support only for gaps |
| Application shell, cross-page navigation or frame consistency | `app-shell-design`: information architecture, headers, content boundaries and scroll ownership | Reuse an adequate shell; page leads own content; add navigation, component or responsive specialists only for gaps |
| Shared components, interfaces, variants or missing primitives | `component-system`: reusable implementation | Page composition and business semantics stay with the page implementer; add behavior specialists only for gaps |
| Button, form, navigation or overlay behavior | `button-interaction`, `form-interaction`, `navigation-interaction`, `floating-components`; `interaction-design` coordinates shared behavior | Select the relevant leaf; read shared parent rules once. Cross-component or async behavior may need the parent and referenced methods, not all siblings |
| Reflow, touch, navigation collapse or overflow | `responsive-design`: scoped adaptations | Preserve the chosen component type, interaction contract and visual system |
| Compatible public website or portfolio | `design-taste-frontend`: page design/implementation | Check its real defaults and prerequisites first. Existing-site/local repairs preserve their scope; use selected guidance or a different lead if the full workflow conflicts |
| Additional style, typography or UX evidence | `ui-ux-pro-max`: research and recommendations | Fill unresolved candidate/evidence gaps; no automatic research pass, page-code ownership or replacement of adopted tokens |
| Requested case research/comparison, source checks, or missing evidence for specific reference traits | `design-reference-research`: scoped cases, evidence and transferable patterns | A name used only to convey mood does not require research when direction is sufficiently grounded. Inspect needed sources for concrete borrowing; retain page ownership and token authority |
| Faithfully implement a supplied image | Image-capable page implementer: code matching that target | Retain the image's authority; do not regenerate it. Add global style only for needed token extraction/validation |
| Design images only | `imagegen-frontend-web`: website sections; `imagegen-frontend-mobile`: app screens/flows; `brandkit`: brand boards | Require a usable image tool; preserve requested quantity and format. Images are not code or adopted product tokens |
| Generate design images, then implement | `image-to-code`: image-first creation and code | Needs image and coding capabilities; do not substitute it for supplied-image reproduction |
| Explicitly selected creative direction | `gpt-taste`: expressive public marketing; `high-end-visual-design`: soft/polished; `minimalist-ui`: restrained; `industrial-brutalist-ui`: mechanical/brutalist | Respect upstream opt-in; select a fitting lead instead of stacking complete style workflows. `gpt-taste` does not serve business regions |
| Explicit Stitch workflow | `stitch-design-taste`: Stitch-oriented `DESIGN.md` | Distinguish the design document from screen generation or frontend code; inspect actual tool access |
| Explicit historical compatibility | `redesign-existing-projects`, `design-taste-frontend-v1`, `design-taste-frontend-v2-experimental` | Use the deliberately selected pinned version; never an automatic fallback for an unavailable current skill |

For a settings form or other page without an available dedicated page skill, name the current implementer as composition/business-flow owner; component, interaction, and responsive modules supply specific gaps. Do not force a dashboard workflow onto every administration page.

Assign one lead per region and one code owner per component; the same implementer may hold all roles. Split mixed marketing/application work by region while sharing the authoritative theme. Catalog descriptions and invocation flags describe upstream capabilities; they do not override this role map. Generic aesthetic preferences do not invoke opt-in classics. Reassess the route when requirements, available tools, or observed gaps change; finish assigned work without circular handoffs.

## Discover and reuse loaded rules

Select one language edition. With MCP, inspect `catalog_skills` metadata (including `category`, `version`, `tags`, `requires`, `exclude_scopes`, and `allow_implicit_invocation`) to filter out incompatible or opt-in entries before calling `load_skill` for selected entries. Shared edition guides (`FOUNDATIONS.md`, `ORCHESTRATION.md`, `README.md`) are also readable as MCP resources under `pivotui://docs/` when needed. Resolve aliases to one actual entry: `taste-skill` and `design-taste-frontend` are the same skill. If different installed copies share a name, choose one compatible exact catalog id; do not combine copies or language editions.

Within the current task, reuse already read entries and resources by resolved file identity and revision. A parent backlink, alias, or second supporting role is not a reason to reload unchanged content or rerun the workflow. Re-read when content changes, context no longer contains the needed rules, or new scope requires unread guidance. MCP is stateless; it does not manage this working memory for the agent.

Use `read_skill_file` for needed resources explicitly referenced by the selected entry or its relevant resources, including inline filenames as well as Markdown links. `linked_resources` is a convenience index, not a complete dependency list. Continue needed pagination and restart if the revision changes. Do not enumerate all assets or load unselected bodies.

For product-case research, discover `design-reference-research`, then use its own small indexes to select usually 1–3 cases. `catalog_skills` searches skill metadata, not case bodies; the existing reader does not perform semantic search. An indexed source is not a reviewed case. Skip research for a themed local repair unless a named-reference comparison or evidence gap is part of the request.

Without MCP, discover the same modules from available skills, user-supplied entries or declared directories. Check the selected workflow's actual prerequisites. Complete ordinary missing capabilities directly and disclose the fallback; if the user requires a specific unavailable method with no acceptable substitute, ask only for that dependency while continuing independent work. Do not automatically install same-named packages or claim unavailable tools ran.

Read [adapter guidance](references/skill-adapters.md) for conflicts/new integrations, [scenarios](references/scenarios.md) for complex combinations, and the [external catalog](references/external-catalog.md) for source/version choices. Ordinary tasks skip irrelevant references.

## Consolidate and deliver

For a new theme, reuse a suitable direction from the lead or select through global style's on-demand reference library. A sufficient brief supports a reasoned provisional choice; ask only about material choices that cannot be inferred. Ordinary local repairs need no style selection or questionnaire. Adopt compatible generated values or let global style supply missing values, then validate one authoritative token source; do not commission two independent themes. Existing themes and faithful-reference decisions remain authoritative within scope unless the user explicitly changes them. Advice-only work stops at recommendations, without applying a theme or writing page code.

State a concise agreement: deliverable/region, lead and support contributions, token/component source, concrete gaps, and acceptance scope. Support proposes changes; the named owner integrates them. For multiple regions, shared changes, or cross-chat continuity, use [handoff guidance](references/design-contract.md) to connect decisions, owner, implementation and actual evidence in existing records. This also applies to solo work. Keep product tokens in the product project.

Before delivery, derive checks from the changes: theme consumers after shared styling work, shared behavior across affected component callers, and reading/keyboard order after responsive reordering. The implementer may perform these checks; add specialists only for gaps, and reuse still-applicable evidence. Token generation or a passing local flow alone does not establish cross-region integration. Report actually used skills and their contributions, outcomes, checked scope and remaining unverified items; do not expand local repairs into a full-site audit.
