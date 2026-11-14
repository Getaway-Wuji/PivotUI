# Every Skill in PivotUI

[Home](../README.en.md) · [Installation](INSTALL.en.md) · [Routing](ARCHITECTURE.en.md) · [简体中文](SKILLS.zh-CN.md)

Release **0.4.0** contains **23 packages: 9 internal and 14 external**. Four interaction submodules are included inside their parent package, giving **27 `SKILL.md` entrypoints**. Reference cards, templates, and datasets are resources rather than additional skills.

“Internal” identifies this project's authored capability. “External” identifies an imported upstream package whose author is credited below. Internal authorship does not imply that all reference material is original: the product-reference research module, for example, includes attributed VoltAgent source metadata. Exact license scope and local adaptations are recorded in [THIRD_PARTY_NOTICES](../THIRD_PARTY_NOTICES.md), package `LICENSE` files, and `UPSTREAM.md` records.

Paths below point into the English edition; the Chinese edition has the same directory and Skill identifiers. Preserve full package directories when installing.

## Internal modules

### 1. `design-orchestrator` — the task entrypoint

[Entry](../English/orchestration/design-orchestrator/SKILL.md) · `orchestration/design-orchestrator` · version **1.2.5**

**Purpose.** Turn an ordinary request into a coordinated design assignment. It identifies whether the result should be advice, an audit, design images, tokens, or implemented code, then chooses the smallest sufficient set of capabilities.

**When selected.** Use it as the default entry for interface work, especially tasks spanning page structure, shared components, interaction, visual decisions, or several regions. An already assigned local task can enter its specialist directly.

**Work and output.** It establishes scope, reference authority, current theme/components, available tools, regional leads, and acceptance criteria. It records a compact assignment, loads relevant entries and resources, consolidates shared proposals, and continues through delivery. It can split a public site and administration area between different leads.

**Boundary.** The host AI executes these instructions. The orchestrator is not a standalone scheduling program and does not contain every module's detailed rules. It respects upstream opt-in policies, reuses already loaded guidance, and prevents circular handoffs. Each region and component has one integration owner.

### 2. `global-style-skill` — visual direction and tokens

[Entry](../English/orchestration/global-style-skill/SKILL.md) · `orchestration/global-style-skill` · version **1.1.1**

**Purpose.** Choose or compare visual directions and generate, extend, migrate, organize, or validate a product's named design values. Its **40 reference cards** offer selectable visual attributes in seven overlapping browsing groups.

**When selected.** New themes, brand changes, unresolved style choices, cross-region consistency, or an explicit token review. A local interaction repair under a complete existing theme does not require it.

**Work and output.** It begins with the current editable theme source, interprets references, distinguishes verified values from screenshot estimates, and supplies concrete color, typography, spacing, and shape values when required. It checks invalid values, duplicate names, missing references, cycles, and actual use. Output can be a recommendation, usable token changes, or locatable validation findings.

**Boundary.** It does not implement page composition or components. Suitable direction decisions from a page lead are reused. Candidate exploration does not automatically authorize applying a new theme; adopted values stay in one authoritative source in the target product.

### 3. `dashboard-design` — business overview and analysis

[Entry](../English/page-design/dashboard-design/SKILL.md) · `page-design/dashboard-design` · version **1.1.4**

**Purpose.** Translate a business question into metric hierarchy, useful representations, charts, summaries, and actions. Its seven structural families cover business overview, diagnosis, monitoring, team workspace, account/resource overview, discovery, and thematic reporting.

**When selected.** Analytics, operations, monitoring, workspaces, and resource dashboards. A reference can determine the required structure or visual language.

**Work and output.** It establishes user role, decisions, metric definitions, periods, comparison baselines, data status, first-screen priority, and drill-down paths. It delivers the requested design brief, implementation prompt, working page, or local change. Applicable states distinguish zero, missing, loading, no results, partial updates, errors, and stale data.

**Boundary.** It owns dashboard content and necessary behavior, reusing the application shell. Full administrative lists and application-wide navigation belong to their respective modules. An adequate existing theme or faithful reference skips visual-recipe selection. It can supply targeted data-semantic advice while another implementer owns faithful image reconstruction.

### 4. `data-list-design` — complete operational lists

[Entry](../English/page-design/data-list-design/SKILL.md) · `page-design/data-list-design` · version **1.0.0**

**Purpose.** Make finding records, acting on them, and returning to work one continuous flow. It owns full list-page composition and its business semantics.

**When selected.** Administrative record lists with search, filters, sorting, pagination, column/view controls, selection, bulk tasks, exports, or detail-return continuity. Features are included according to the task, rather than automatically adding all of them.

**Work and output.** It defines identifying/comparison fields, query and result scope, permissions, dataset scale, selection boundaries, batch-operation impact, and exported records. It preserves applied filters and page number on return from detail and distinguishes current-page selection from all matching records. It delivers the specification or working list and actual flow checks.

**Boundary.** The module reuses shell and tokens. `component-system` owns reusable Table and control implementations; the list lead owns how they express business work. A small summary table inside a dashboard or one control repair does not automatically require the entire list workflow.

### 5. `app-shell-design` — the shared application frame

[Entry](../English/page-design/app-shell-design/SKILL.md) · `page-design/app-shell-design` · version **1.0.0**

**Purpose.** Keep location, navigation, page context, and scrolling coherent across an administration application.

**When selected.** Shared navigation hierarchy, sidebar/header work, breadcrumbs, page title/actions, cross-page width and inset, fixed regions, scroll ownership, and list–detail–edit continuity.

**Work and output.** It separates the persistent frame from route context and page content. It establishes route metadata, title/action slots, content boundaries, scroll containers, and return-state responsibilities. It can implement the shell or deliver the corresponding specification. Checks include nested routes, long labels, keyboard access, collapse, short/narrow viewports, overlap, and return paths.

**Boundary.** Page modules retain business content. The supplied Ant Design Pro-style pattern is a scoped reference rather than a universal requirement to use a sidebar or replace the router. It preserves working structure and uses navigation, component, and responsive specialists only where required.

### 6. `interaction-design` — states, feedback, and recovery

[Entry](../English/interaction/interaction-design/SKILL.md) · `interaction/interaction-design` · version **1.1.0**

**Purpose.** Make actions understandable and recoverable through the model **trigger → state change → feedback → exit or recovery**. It coordinates the four nested entries below and common asynchronous behavior.

**When selected.** Cross-component behavior, request lifecycles, state ambiguity, keyboard/focus problems, filter races, submissions, bulk outcomes, undo, or selected animation work.

**Work and output.** It distinguishes input feedback from business state, defines confirmed success and unknown outcomes, prevents duplicate submissions, rejects stale responses, and preserves context after failure. React Bits guidance and a catalog are available for suitable animation needs; existing working components can be reused. It delivers scoped behavior specifications or code and applicable checks.

**Boundary.** Layout, business validation rules, and theme remain with their established owners. An animation finishing is not proof of request success. The four submodules ship with this package and share its references; they are loaded selectively.

#### 6a. `button-interaction`

[Entry](../English/interaction/interaction-design/sub-skills/button-interaction/SKILL.md)

Owns command-button hover, focus, pressed, disabled, pending, result, and recovery behavior. It keeps a stable hit area and separates temporary feedback from persistent selection and remote operation state. It specifies native semantics, keyboard activation, accessible names, execution guards, and duplicate prevention. It handles hold/slide gestures only with equivalent accessible paths and real cancellation rules. Navigation links, whole-form validation, and feedback container choice belong to the matching sibling modules. Errors remain persistent near their context or in Alert, rather than Toast.

#### 6b. `form-interaction`

[Entry](../English/interaction/interaction-design/sub-skills/form-interaction/SKILL.md)

Owns fields, selectors, switches, sliders, validation, filters, and submission feedback. It retains drafts after errors, distinguishes the submitted snapshot from edits made during a request, and prevents stale responses from overwriting newer input. It addresses error association, first-error focus, input-method composition, applied-filter/result consistency, and safe continuation after unknown outcomes. It produces implementable field and request behavior while retaining page structure and business validation rules.

#### 6c. `navigation-interaction`

[Entry](../English/interaction/interaction-design/sub-skills/navigation-interaction/SKILL.md)

Owns current location, group disclosure, keyboard behavior, and focus continuity in sidebars, breadcrumbs, same-page tabs, and command menus. It distinguishes current route, hover, focus, and expanded state; native navigation links do not acquire command-menu keyboard behavior merely because a component is called Menu. It restores focus sensibly after rows disappear or reorder and preserves true location after failed routing. Information architecture and page layout remain with the shell/page lead.

#### 6d. `floating-components`

[Entry](../English/interaction/interaction-design/sub-skills/floating-components/SKILL.md)

Selects and specifies Tooltip, Toast, Alert, Modal, Popconfirm, and Drawer. Tooltip adds supplementary explanation; Toast carries lightweight outcomes and never errors; Alert keeps important problems visible. Modal handles irreversible confirmation or complex information. Popconfirm serves low-risk local confirmation. Drawer supports editing that needs retained surrounding context, excluding simple forms and full-screen tasks. Output includes selection rationale, opening/dismissal, focus, background interaction, async recovery, and narrow-screen alternatives. Appearance alone does not establish modality.

### 7. `component-system` — reusable UI implementation

[Entry](../English/components/component-system/SKILL.md) · `components/component-system` · version **1.0.0**

**Purpose.** Build consistent shared components with clear anatomy, interfaces, state ownership, sizes, and purposeful variants.

**When selected.** Missing shared controls, inconsistent cross-page components, new variants, interface adaptations, or integration of existing component libraries.

**Work and output.** It follows **reuse → configure → compose/adapt → build a demonstrated gap**. It inspects actual installed versions, callers, theme/provider, events, slots, and form conventions. It implements the required shared elements and checks realistic content, portals, focus, states, and screen sizes.

**Boundary.** Page owners decide composition and business meaning. The module does not turn every one-off block into a public abstraction or introduce a second full UI library because a reference looks different. One owner integrates each component; overlay behavior follows the shared overlay contract.

### 8. `responsive-design` — adaptation that preserves the task

[Entry](../English/responsive/responsive-design/SKILL.md) · `responsive/responsive-design` · version **1.0.1**

**Purpose.** Keep necessary information and operations usable as available space, viewport height, and input capabilities change.

**When selected.** Content reflow, navigation collapse, narrow charts/tables, touch/hover differences, local overflow, fixed regions, and responsive component work.

**Work and output.** It defines **condition → retained content → rearrangement → continued operation**, then chooses fluid sizing, Grid/Flex, viewport or container queries as appropriate. It preserves reading order, keyboard order, filters, selections, drafts, and operation state. It delivers scoped changes, transition decisions, and actual checks around relevant breakpoints.

**Boundary.** It inherits the product's visual system and component semantics. It does not remove business fields just to make a screen fit, hide failures with global clipping/scaling, or convert every narrow-screen interaction into Drawer. Existing breakpoint conventions take priority; otherwise transitions follow observed content constraints.

### 9. `design-reference-research` — evidence from named products

[Entry](../English/design-research/design-reference-research/SKILL.md) · `design-research/design-reference-research` · version **1.0.0**

**Purpose.** Find, compare, and adapt concrete product design references with explicit evidence boundaries. The internal research method uses attributed metadata from [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md), revision `fcc70284932276d085f01ef9f83edde90b1258cb`.

**When selected.** Named-brand references, sourced comparisons, source checks, or a concrete unresolved visual question. Routine local fixes under an adequate theme skip it.

**Work and output.** An index points to **84 source records**, **8 document-reviewed case cards**, and four conditional cross-case patterns. Start with 1–3 relevant cards. Output identifies case/source, actual page scope, observations versus recommendations, transferable relationships, required adaptation, missing checks, and integration owner.

**Boundary.** The other 76 sources remain indexed-only with unknown scope. Document review does not verify current live sites, interactions, accessibility, or responsiveness. Research supplies advice to the existing owner; it does not implement pages or replace adopted tokens. Source metadata carries the upstream MIT notice; original guidance and source material must not be confused.

## External packages

The following **14 packages are upstream work, not original PivotUI skills**. They retain package identities, licenses, and fixed-source records. Cluster routing gives each a selected role; broad statements in an upstream description do not override the regional division of work. Read a selected entry's real prerequisites before running it.

### 10. `design-taste-frontend` — current public website workflow

[Entry](../English/page-design/taste-skill/SKILL.md) · folder `page-design/taste-skill` · **Leonxlnx** · [source](https://github.com/Leonxlnx/taste-skill) · **2.5.1**, `f6b7657` · MIT

**Purpose and selection.** A detailed workflow for compatible company, product, service, place, portfolio, and public marketing pages, including redesign and review. The folder alias `taste-skill` resolves to this same capability.

**Work and output.** It selects page structure by business kind and combines copy, real photographs/product UI, typography, layout, motion, and browser checks. The package contains executable scripts, references, system resources, and legitimate runtime assets. It produces a site or scoped compatible improvement, with the workflow's checks.

**Dependencies and boundary.** Its entry requires **Node 22+** and **Chrome, Edge, or Chromium**; ffmpeg is optional. The upstream workflow has strong layout, content, and motion prescriptions, so the orchestrator checks compatibility with the user's scope and existing product first. It is not the business-dashboard lead. Photos, icons, and other assets retain separate attribution/license records where applicable.

### 11. `ui-ux-pro-max` — searchable design recommendations

[Entry](../English/design-research/ui-ux-pro-max/SKILL.md) · `design-research/ui-ux-pro-max` · **nextlevelbuilder** · [source](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · **2.15.0**, `6ae86f6` · MIT

**Purpose and selection.** Provide additional design candidates and evidence for a targeted style, typography, palette, UX, chart, or implementation-stack question. It is selected for an actual unresolved research gap, rather than a mandatory pass for every task.

**Work and output.** The bundled Python search accesses local datasets covering styles, product palettes, fonts, UX guidance, icons, motion presets, charts, and stacks. Searches can target one domain or generate a broader design-system recommendation. Results are checked for relevance before being adopted or persisted.

**Dependencies and boundary.** The search uses Python 3.x with no external dependencies. A documented command-path adaptation makes the script addressable from the installed package location; scripts and datasets retain upstream content. In PivotUI this skill supplies research and recommendations, while page implementation and adopted tokens stay with their assigned owners.

### 12. `gpt-taste` — expressive public marketing

[Entry](../English/visual-styles/gpt-tasteskill/SKILL.md) · `visual-styles/gpt-tasteskill` · **Leonxlnx** · [classics source](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **explicit opt-in**

Provides a strongly directed marketing workflow with varied hero composition, AIDA page progression, asset-led sections, and GSAP-oriented scroll motion. Choose it only when explicitly requested or authorized as a matching creative workflow. Output is the agreed marketing design or implementation; actual code and motion dependencies must be available. It serves **public marketing only** in PivotUI and never dashboards or business tools. Its instructions remain upstream work; selection does not authorize unrelated theme changes or unverified claims of script execution.

### 13. `high-end-visual-design` — soft, polished direction

[Entry](../English/visual-styles/soft-skill/SKILL.md) · `visual-styles/soft-skill` · **Leonxlnx** · [classics source](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **explicit opt-in**

Provides an art-directed workflow with soft contrast, generous whitespace, distinctive type, tactile depth, and spring-like motion. It includes alternatives such as glass, editorial luxury, and soft structural layouts, with corresponding mobile adaptations. Select it by name for a fitting direction, then reconcile its prescriptions with actual fonts, dependencies, accessibility, and the target product. It can guide or implement the agreed visual region; it does not become the universal PivotUI theme or silently replace established tokens.

### 14. `minimalist-ui` — editorial product minimalism

[Entry](../English/visual-styles/minimalist-skill/SKILL.md) · `visual-styles/minimalist-skill` · **Leonxlnx** · [classics source](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **explicit opt-in**

Provides a restrained editorial/product direction based on warm monochrome surfaces, typography-led hierarchy, flat structured grids, and selective muted accents. It contains concrete visual and implementation rules. Choose it explicitly when that language fits the brief. The result is a scoped direction or implementation integrated into the product's agreed design source. Its font, icon, shape, and palette preferences are upstream workflow choices, not library-wide rules; compatibility is checked before adopting them.

### 15. `industrial-brutalist-ui` — mechanical visual language

[Entry](../English/visual-styles/brutalist-skill/SKILL.md) · `visual-styles/brutalist-skill` · **Leonxlnx** · [classics source](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **explicit opt-in**

Provides rigid modular grids, Swiss-influenced typography, strong scale contrast, utilitarian color, and optional analog-display treatments. Its two principal directions are light industrial print and dark telemetry/terminal language, selected deliberately rather than mixed indiscriminately. Choose it by name for a product or region needing that specific expression. The page owner retains business structure and readability requirements; the style does not justify inventing data, hiding essential actions, or changing the product's global theme outside scope.

### 16. `imagegen-frontend-web` — website section concepts

[Entry](../English/image-design/imagegen-frontend-web/SKILL.md) · `image-design/imagegen-frontend-web` · **Leonxlnx** · [imagegen source](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT

Creates website design-reference images for landing, marketing, and product sections. The upstream workflow uses **one separate horizontal image per section**, with a coherent palette and varied compositions across the page. Select it when the requested deliverable is website concept images, honoring the user's quantity and format. It requires actual image generation. The result is visual references, not working frontend code; later implementation requires a separate assignment and must complete behavior and responsiveness beyond the static images.

### 17. `imagegen-frontend-mobile` — application screens and flows

[Entry](../English/image-design/imagegen-frontend-mobile/SKILL.md) · `image-design/imagegen-frontend-mobile` · **Leonxlnx** · [imagegen source](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT

Creates mobile app screen concepts and coherent multi-screen flows for areas such as onboarding, authentication, home, commerce, profiles, or settings. It emphasizes readable hierarchy, platform-aware composition, shared color language, and consistent screen framing; its default presentation includes a subtle phone mockup. Select it for mobile **image** deliverables, adapting presentation to the user's request. It requires image generation and does not create app code, desktop sites, or responsive frontend behavior.

### 18. `brandkit` — identity boards and visual concepts

[Entry](../English/image-design/brandkit/SKILL.md) · `image-design/brandkit` · **Leonxlnx** · [imagegen source](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT

Creates brand-guideline boards, logo-system concepts, visual-world presentations, and identity applications as images. It organizes a coherent brand idea through sparse typography, symbolic marks, coordinated panels, imagery, and mockups. Select it for visual identity exploration or presentation, with an available image tool. Its boards are candidates and visual deliverables; they do not automatically become approved logos, usable font files, vector masters, or the authoritative product token source. Adopted values can be translated into the product by global style when requested.

### 19. `image-to-code` — generate, analyze, implement

[Entry](../English/image-design/image-to-code/SKILL.md) · `image-design/image-to-code` · **Leonxlnx** · [imagegen source](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT

Uses a sequential workflow: generate new design images, analyze their composition and visual relationships, then implement the website. It favors readable section-specific references over an overcrowded whole-site image. Select it when both concept creation and frontend implementation are requested and image plus coding capabilities exist. It is not the default for faithfully reproducing an already supplied image: in that case the original remains the target and an image-capable implementation lead takes responsibility. Generated images do not establish working interactions or cross-screen behavior; those must be implemented and checked.

### 20. `stitch-design-taste` — Stitch-oriented design instructions

[Entry](../English/tool-integrations/stitch-skill/SKILL.md) · `tool-integrations/stitch-skill` · **Leonxlnx** · [classics source](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **explicit opt-in**

Writes a `DESIGN.md` tailored to Google Stitch, expressing atmosphere, color values, typography, component behavior, layout, responsive rules, and motion through descriptive instructions. Select it for an explicitly requested Stitch workflow. Its declared prerequisite is Stitch access, with a Stitch MCP connection optional. Producing the design document is different from generating screens in Stitch or delivering frontend code; those stages require actual tools and requested scope. The document should refer to the adopted project design source rather than creating competing values.

### 21. `design-taste-frontend-v1` — pinned original taste behavior

[Entry](../English/legacy/taste-skill-v1/SKILL.md) · `legacy/taste-skill-v1` · **Leonxlnx** · [classics source](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **explicit historical selection**

Preserves the original dial-based taste workflow for projects depending on that behavior. It defines design variance, motion intensity, and density, alongside React/Next.js, Tailwind, component, and dependency conventions. Use it by name when reproducing or maintaining a project deliberately tied to this version. Check the actual stack and installed packages. Its retained defaults do not replace the current taste package or PivotUI's business-page methods, and unavailability of the current skill is not a reason to activate it silently.

### 22. `design-taste-frontend-v2-experimental` — pinned experimental workflow

[Entry](../English/legacy/taste-skill-v2-experimental/SKILL.md) · `legacy/taste-skill-v2-experimental` · **Leonxlnx** · [classics source](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **explicit historical selection**

Preserves a single-file experimental workflow that reads the brief's page type, audience, references, existing assets, and constraints before applying design dials. It targets landing pages, portfolios, and redesigns; its own scope excludes dashboards, data tables, and multi-step product UI. Use it only for a deliberate historical requirement. Output follows that selected version, with dependencies checked against the target project. It remains a separate pinned capability rather than an alias or automatic fallback for current taste.

### 23. `redesign-existing-projects` — historical targeted redesign

[Entry](../English/legacy/redesign-skill/SKILL.md) · `legacy/redesign-skill` · **Leonxlnx** · [historical source](https://github.com/Leonxlnx/taste-skill/tree/e04409a461022e1b9d0e898eac6b9224e2b9dc4e/skills/redesign-skill) · `e04409a` · MIT · **explicit historical selection in PivotUI**

Preserves the historical **scan → diagnose → fix** workflow for improving an existing website or app within its current stack. It audits typography, color/surfaces, layout, and other visual weaknesses and proposes or applies targeted upgrades. Choose it when its pinned historical behavior is specifically wanted. The current upstream project has incorporated redesign into current taste; PivotUI keeps this package for deliberate compatibility and does not select it merely because the request says “redesign.” Business regions keep their appropriate page ownership and shared design source.

## Choosing among overlapping capabilities

| Question | Use this distinction |
| --- | --- |
| Global style or a style classic? | Global style manages the product's direction and tokens; a classic is a specifically chosen upstream visual workflow. |
| Dashboard or data list? | A summary supporting an overview stays with Dashboard; a full record-finding and operational workflow belongs to data-list. |
| App shell or navigation interaction? | Shell owns hierarchy/frame/route context; navigation interaction owns input, current state, and focus behavior. |
| Component system or interaction? | Components own shared implementation/interfaces; interaction supplies state and recovery contracts for identified gaps. |
| UI/UX research or product-reference research? | UI/UX research queries general design candidates and guidelines; product research evaluates named sources and case evidence. |
| Website images or image-to-code? | Images-only returns concepts; image-to-code creates new concepts and continues through code. |
| Current taste or a historical package? | Use the compatible current workflow ordinarily; choose a historical identity deliberately for that behavior. |

All modules serve the requested deliverable. Their presence in the catalog does not require loading every body, executing every workflow, or repeating decisions already made.
