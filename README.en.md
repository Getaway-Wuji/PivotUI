<p align="center">
  <img src="assets/pivotui-brand-loop1.gif" alt="PivotUI brand animation — A Skill Cluster for UI" width="1200">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/Getaway-Wuji/PivotUI/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs welcome"></a>
</p>

# PivotUI

**Describe the interface you want. Let the cluster choose the skills it needs.**

[简体中文](README.md) · English · [Installation](docs/INSTALL.en.md) · [Every skill explained](#skills) · [Architecture and routing](docs/ARCHITECTURE.en.md)

PivotUI is a UI design Skill cluster that connects task routing, visual direction, page design, components, interaction, responsive behavior, design research, and selected external workflows. Its central idea is simple: **people should describe the work, without repeatedly searching a skill library, choosing modules, or explaining how those modules should cooperate.**

The management layer interprets the requested result, assigns a lead for each region, adds specialists for concrete gaps, and brings their results into the same product. A complete task can move from business structure to working interface while preserving the project's theme, components, and decisions.

Release **0.4.0** includes **23 packages: 9 authored modules and 14 external packages**, with **27 standard `SKILL.md` entrypoints** including four interaction submodules. The English and Chinese editions are independently usable. External packages retain their original language and notices in both editions.

## What is a Skill cluster?

A Skill is a reusable set of instructions for a particular kind of work, often accompanied by references, scripts, templates, or data. A Skill cluster adds an explicit collaboration system around several such packages:

- An entrypoint understands the user's task and chooses the relevant capabilities.
- Each capability has a defined responsibility, inputs, outputs, and handoff boundary.
- Shared conventions keep visual and implementation decisions consistent.
- Resources are loaded as needed, instead of putting every instruction into every task.

In PivotUI, the AI working inside your chosen host performs the reasoning and implementation. `design-orchestrator` supplies the management rules. The optional local MCP server exposes metadata and selected files; it does not run its own model or execute Markdown. The same cluster can also be used through direct file access.

## How it saves work

| Repeated work | What PivotUI organizes |
| --- | --- |
| Finding a suitable skill for every request | A common entrypoint routes by deliverable, page purpose, local scope, and available tools. |
| Guessing which other skills to add | Specialists join only for concrete component, behavior, responsive, research, or theme gaps. |
| Repeating the same context to several modules | A compact assignment carries region, owner, references, tokens, components, and acceptance scope. |
| Reconciling conflicting styles | One authoritative token source stays in the target product; one lead integrates each region. |
| Reading the whole library | Metadata discovery precedes selected entries and relevant resource reads. Already available rules are reused. |
| Restarting research after a decision | Suitable established themes and decisions are retained unless the task asks to reconsider them. |

These are workflow mechanisms, not a measured percentage improvement. The practical benefit depends on the task, the host's tool access, and how much of the product already exists.

## What can it do?

| Your request | How the management layer approaches it |
| --- | --- |
| “Build an operations dashboard using our existing theme.” | `dashboard-design` leads metrics, charts, and overview content. Existing shell and theme are reused; specialists fill actual gaps. |
| “Create an order list with filters, bulk actions, and a reliable return from detail.” | `data-list-design` owns the full list workflow and action scope; shared controls, async behavior, and narrow-screen adaptations receive targeted support. |
| “Unify navigation, headers, and scrolling across the admin application.” | `app-shell-design` owns the frame and route contract; page leads retain business content. |
| “Fix a form that loses input after a failed save.” | `form-interaction` and relevant async guidance handle the local problem, preserving the surrounding layout and theme. |
| “Compare design directions before building.” | `global-style-skill` returns candidates and a recommendation; named-product evidence can bring in `design-reference-research`. Advice stays advice until implementation is requested. |
| “Build a public product website.” | A compatible `design-taste-frontend` workflow can lead. Existing product constraints and tool prerequisites are checked before adopting its defaults. |
| “Generate mobile screen concepts” or “Create a brand board.” | The appropriate image-design skill produces the requested images through an available image tool. |
| “Fix just the table overflow on mobile.” | `responsive-design` handles the specific content and operation constraints. |

See the [routing guide](docs/ARCHITECTURE.en.md) for mixed projects, exact-image reproduction, optional styles, and task handoffs.

## Structure

```text
English/ or Chinese/
├── orchestration/       Task routing and global visual decisions
├── page-design/         Dashboard, data list, application shell, public websites
├── interaction/         Shared behavior and four focused submodules
├── components/          Reusable component implementation
├── responsive/          Layout, input, and overflow adaptation
├── design-research/     UI/UX recommendations and product-reference research
├── visual-styles/       Explicitly selected external style workflows
├── image-design/        Website images, mobile images, brand boards, image-first code
├── tool-integrations/   Stitch-oriented design workflow
├── legacy/              Deliberately selected historical workflows
├── design-system/       Shared methods and ownership agreement
└── mcp/skill-cluster/    Optional local catalog and file-reading service
```

Internal and external packages share functional categories. Their origin is documented explicitly rather than encoded in a separate directory hierarchy. Folder names and YAML skill names sometimes differ: `taste-skill` is the folder for `design-taste-frontend`, for example.

<a id="skills"></a>

## What each Skill does

All **27 entrypoints** are introduced below: **9 internal packages, 14 external packages, and 4 interaction submodules** included in their parent package. Internal modules are authored by PivotUI; external entries identify their upstream authors and retain their MIT notices. The native `pivotui` entry created during installation is the bootstrap that opens this library, not a 28th library skill. Links open the English source; the Chinese edition uses the same identifiers and directory structure.

### Management and visual direction

#### `design-orchestrator` — understand the request and assign the work

**Internal · [Skill entry](English/orchestration/design-orchestrator/SKILL.md).** The cluster's main entry identifies the requested result—advice, review, images, tokens, or working code—and selects the smallest suitable team. It assigns one lead per region, carries forward references and existing product decisions, and brings specialists' work together. For example, a dashboard with a new filter form can use Dashboard as the page lead and Form Interaction for submission behavior. It produces assignments and a consolidated deliverable; the host AI performs the work using these instructions.

#### `global-style-skill` — establish and maintain the product's visual system

**Internal · [Skill entry](English/orchestration/global-style-skill/SKILL.md).** Handles visual-direction comparisons and the product's named colors, typography, spacing, shapes, and other design tokens. Its 40 reference cards help explore a direction only when needed. For a brand refresh, it can compare options, update the adopted theme, and check invalid values, missing references, duplicates, and actual use. Outputs include recommendations, token changes, or specific validation findings. It keeps one authoritative theme source in the target product; page composition and component implementation remain with their respective owners.

### Page design

#### `dashboard-design` — turn business questions into useful dashboards

**Internal · [Skill entry](English/page-design/dashboard-design/SKILL.md).** Designs business overviews, analysis pages, monitoring screens, workspaces, and account/resource summaries. It organizes metrics, chart choices, comparison periods, priorities, and drill-down actions around the decisions a user needs to make. An operations dashboard might show current performance, explain changes, and expose follow-up actions. Outputs can be a design specification or a working page, including loading, empty, error, and stale-data behavior. It reuses the existing shell and theme; full operational lists belong to Data List Design.

#### `data-list-design` — connect finding records with acting on them

**Internal · [Skill entry](English/page-design/data-list-design/SKILL.md).** Owns complete record-management pages: search, applied filters, sorting, pagination, column/view choices, selection, bulk actions, exports, and return from detail. For an order list, it defines which records an action affects, distinguishes selecting this page from all matching results, and restores the user's filters and page after editing. It delivers a coherent list specification or implementation. Reusable Table controls belong to Component System; this skill owns their business meaning and the surrounding workflow.

#### `app-shell-design` — build the frame shared across application pages

**Internal · [Skill entry](English/page-design/app-shell-design/SKILL.md).** Organizes persistent navigation, breadcrumbs, page titles and actions, content widths, fixed regions, and scrolling. Use it when several administration pages need a consistent frame or when moving between list, detail, and edit loses context. It supplies a shell specification or implementation with clear route metadata and page slots, checking nested routes, long labels, collapse, keyboard access, and short or narrow screens. Page leads retain business content; existing routing and working navigation patterns are preserved where suitable.

#### `design-taste-frontend` — design and implement public websites

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/taste-skill) · [Skill entry](English/page-design/taste-skill/SKILL.md).** The current taste workflow creates or improves compatible company, product, service, place, portfolio, and marketing websites. It connects page structure, copy, photography or product imagery, typography, layout, motion, and browser checks. For example, it can turn a company brief into an implemented public website. Its strong defaults are checked against the existing product and requested scope; it is not the business-dashboard lead. Requires Node.js 22+ and Chrome, Edge, or Chromium; ffmpeg is optional.

### Interaction and feedback

#### `interaction-design` — coordinate states, outcomes, and recovery

**Internal · [Skill entry](English/interaction/interaction-design/SKILL.md).** Defines what triggers an action, how state changes, what feedback appears, and how the user exits or recovers. It handles shared asynchronous behavior such as duplicate prevention, stale responses, uncertain results, and preserving context after failure. For a bulk update, it can specify pending, confirmed, partial, and failed outcomes. It returns behavior specifications or implementation changes, loading only the relevant submodules below. Motion is added when useful; completing an animation never establishes that a request succeeded.

#### `button-interaction` — make command buttons predictable

**Internal interaction submodule · [Skill entry](English/interaction/interaction-design/sub-skills/button-interaction/SKILL.md).** Specifies hover, focus, pressed, disabled, pending, result, and recovery behavior for command buttons. For a Save button, it keeps the hit area stable, prevents duplicate execution, and distinguishes feedback from the real operation state. It covers native semantics, keyboard activation, accessible names, and accessible alternatives to hold/slide gestures. The output is an implementable button contract or local fix. Form validation and navigation use their matching modules; errors remain near their context or in Alert.

#### `form-interaction` — preserve input and make submission reliable

**Internal interaction submodule · [Skill entry](English/interaction/interaction-design/sub-skills/form-interaction/SKILL.md).** Handles fields, selectors, switches, sliders, validation, filter controls, and submission feedback. It fixes cases such as a failed save erasing a draft or a slow response overwriting newer edits. Its rules distinguish the submitted snapshot from current input, associate errors with fields, move focus appropriately, respect input-method composition, and keep applied filters aligned with results. Output is scoped field and request behavior that preserves the page's structure and established business-validation rules.

#### `navigation-interaction` — keep location and focus clear

**Internal interaction submodule · [Skill entry](English/interaction/interaction-design/sub-skills/navigation-interaction/SKILL.md).** Defines current-location indicators, group expansion, keyboard behavior, and focus continuity for sidebars, breadcrumbs, tabs, and command menus. For a collapsible sidebar, it separates the active route from hover, focus, and expansion; failed navigation must not falsely change the current location. It also plans focus recovery when items disappear or reorder. Outputs are navigation behavior or implementation fixes. Native links retain navigation semantics; the shell/page owner still decides information architecture and layout.

#### `floating-components` — choose the right overlay or feedback surface

**Internal interaction submodule · [Skill entry](English/interaction/interaction-design/sub-skills/floating-components/SKILL.md).** Chooses and specifies Tooltip, Toast, Alert, Modal, Popconfirm, and Drawer. For example, an irreversible deletion needs Modal confirmation, a persistent error belongs in Alert, and contextual editing may use Drawer; Toast never carries errors under this cluster's conventions. It defines opening, dismissal, focus, background access, async recovery, and narrow-screen alternatives. Drawer is reserved for work needing surrounding context, excluding simple forms and full-screen tasks. The result is a justified component choice and complete interaction behavior.

### Reusable components

#### `component-system` — implement shared controls and clear component interfaces

**Internal · [Skill entry](English/components/component-system/SKILL.md).** Builds or adapts shared components with consistent anatomy, variants, sizes, state ownership, events, and accessibility. For example, it can unify a status control used across a dashboard and order list or adapt an existing Table API. It first reuses, configures, or composes the installed library, building new parts for demonstrated gaps. Outputs are reusable implementations and checked usage examples. Page leads own business composition; a one-off block does not automatically need to become a public component.

### Responsive behavior

#### `responsive-design` — keep the same task usable across screen conditions

**Internal · [Skill entry](English/responsive/responsive-design/SKILL.md).** Adapts layout, navigation, charts, tables, fixed regions, and controls to available width, height, and input methods. For an overflowing order table, it decides what information stays visible, how content rearranges, and how users continue filtering and acting on records. Outputs are scoped layout/behavior changes and checks around relevant transitions. It preserves reading order, keyboard access, selections, drafts, and important business fields, inheriting the product's visual system instead of hiding overflow globally or redesigning the entire page.

### Design research

#### `design-reference-research` — learn from named products with traceable evidence

**Internal · [Skill entry](English/design-research/design-reference-research/SKILL.md).** Finds and compares concrete product references, separating source observations from recommendations. It includes attributed metadata from [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md): 84 source records, including eight document-reviewed case cards; the other 76 remain indexed-only. For a request inspired by a named product, it selects relevant cases and explains what can transfer, what needs adaptation, and what remains unchecked. It supplies research to the assigned owner; document review does not establish live-site behavior or authorize replacing the product's theme.

#### `ui-ux-pro-max` — search design guidance and compare candidates

**External · nextlevelbuilder · [Upstream](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · [Skill entry](English/design-research/ui-ux-pro-max/SKILL.md).** Searches local datasets for styles, palettes, typography, UX guidance, icons, motion, charts, and implementation-stack recommendations. For example, it can compare chart types for a business question or suggest accessible palette candidates. It returns targeted findings or a broader design-system recommendation, which the current owner evaluates before adoption. In PivotUI its role is research and recommendations; page implementation and adopted tokens retain their existing owners. Search requires Python 3.x with no external dependencies.

### Optional visual styles

These four upstream workflows are **explicit opt-in**. The management layer may recommend a suitable direction, but installation alone does not activate it or change the product's theme.

#### `gpt-taste` — expressive public marketing pages

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/taste-skill-classics) · [Skill entry](English/visual-styles/gpt-tasteskill/SKILL.md).** Uses varied hero compositions, AIDA page progression, asset-led sections, and GSAP-oriented scroll motion for an explicitly selected marketing direction. A suitable assignment might be an expressive product-launch page with a strong opening and clear conversion path. It delivers the agreed design or implementation, with actual code and motion dependencies checked. **Public marketing only: it is never assigned to dashboards or business tools.** Scope and existing product decisions continue to govern its use.

#### `high-end-visual-design` — soft, polished visual direction

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/taste-skill-classics) · [Skill entry](English/visual-styles/soft-skill/SKILL.md).** Offers soft contrast, generous whitespace, distinctive typography, tactile depth, and spring-like motion. Its alternatives include glass, editorial luxury, and soft structural layouts with mobile adaptations. Choose it explicitly for a fitting brief, such as a polished brand experience or a selected region needing this visual language. It supplies a direction or implementation reconciled with actual fonts, dependencies, accessibility, and adopted tokens. These are optional upstream choices, not a default style applied across PivotUI projects.

#### `minimalist-ui` — restrained editorial and product layouts

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/taste-skill-classics) · [Skill entry](English/visual-styles/minimalist-skill/SKILL.md).** Uses warm monochrome surfaces, typography-led hierarchy, flat structured grids, and selective muted accents. Choose it explicitly when a brief calls for this restrained language, for example an editorial product presentation with clear type hierarchy and quiet supporting controls. It returns a scoped visual direction or implementation. Its concrete font, icon, shape, and palette rules are checked against the target product before adoption and integrated into the agreed design source.

#### `industrial-brutalist-ui` — structured industrial visual language

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/taste-skill-classics) · [Skill entry](English/visual-styles/brutalist-skill/SKILL.md).** Uses rigid modular grids, Swiss-influenced typography, strong scale contrast, utilitarian color, and optional analog-display treatments. Its light industrial-print and dark telemetry/terminal directions are deliberate alternatives. Choose it explicitly for a region or product needing that expression; the output is the agreed style treatment or implementation. The page owner retains business structure and readability requirements, so visual direction does not justify fabricated data, missing essential actions, or unrelated global-theme changes.

### Image design

All four image workflows below require an available image-generation tool. Their presence in the library does not provide an image service by itself.

#### `imagegen-frontend-web` — generate website design-reference images

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/imagegen-skills) · [Skill entry](English/image-design/imagegen-frontend-web/SKILL.md).** Creates visual concepts for landing, marketing, and product-page sections. Its default workflow generates a separate horizontal image for each section while keeping a coherent palette and varied compositions. For example, it can deliver separate hero, features, and pricing concepts for visual review, honoring the requested quantity and format. The output is design-reference imagery. Turning it into a working frontend is a separate implementation assignment that must also resolve interaction and responsive behavior.

#### `imagegen-frontend-mobile` — generate mobile screen and flow concepts

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/imagegen-skills) · [Skill entry](English/image-design/imagegen-frontend-mobile/SKILL.md).** Produces mobile application concepts for onboarding, authentication, home, commerce, profiles, settings, and related flows. It maintains readable hierarchy, platform-aware composition, consistent framing, and shared visual language across screens. For example, it can create a coherent onboarding-to-home sequence for review. A subtle phone mockup is the upstream default, adjusted to the user's requested presentation. Deliverables are screen images, not application code, desktop layouts, or implemented responsive behavior.

#### `brandkit` — present a coherent visual identity

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/imagegen-skills) · [Skill entry](English/image-design/brandkit/SKILL.md).** Generates brand-guideline boards, logo-system concepts, visual-world presentations, and identity applications. It brings symbolic marks, sparse typography, coordinated imagery, and mockups into a consistent presentation. For a new product, it can visualize a candidate identity across a mark, palette, and sample applications. These outputs support exploration and review; they are not automatically approved logos, vector masters, usable font files, or authoritative UI tokens. Adopted values can be implemented through Global Style when requested.

#### `image-to-code` — move from new visual concepts to a website

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/imagegen-skills) · [Skill entry](English/image-design/image-to-code/SKILL.md).** Generates new design images, analyzes their composition and visual relationships, then implements the frontend. It uses readable section-specific references to connect concept creation with code delivery. Choose it when the request includes both stages and image-generation plus coding capabilities are available. Faithfully reproducing an image already supplied by the user follows that original reference instead of requiring new concepts. The delivered implementation still needs real behavior and responsive checks; static images cannot establish either.

### Tool integration

#### `stitch-design-taste` — prepare design instructions for Google Stitch

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/taste-skill-classics) · [Skill entry](English/tool-integrations/stitch-skill/SKILL.md).** An **explicit opt-in** workflow that writes a Stitch-oriented `DESIGN.md`: atmosphere, colors, typography, component behavior, layout, responsiveness, and motion. For example, it can turn an agreed product direction into consistent instructions for generating screens in Stitch. Its declared prerequisite is actual Stitch access; a Stitch MCP connection is optional. The document references the product's adopted design source. Writing it, generating screens, and implementing frontend code are distinct deliverables requiring their corresponding tools and scope.

### Historical workflows

These three packages preserve specific earlier behavior and require **deliberate historical selection**. They are not automatic fallbacks for current skills.

#### `design-taste-frontend-v1` — retain the original taste workflow

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/taste-skill-classics) · [Skill entry](English/legacy/taste-skill-v1/SKILL.md).** Preserves the original dial-based workflow for design variance, motion intensity, and density, together with its React/Next.js, Tailwind, component, and dependency conventions. Use it by name when maintaining or reproducing a project intentionally tied to this version. It produces the design or implementation requested under those historical rules, after checking the actual project stack. Its retained defaults do not replace the current taste package or the cluster's specialized business-page methods.

#### `design-taste-frontend-v2-experimental` — retain the experimental taste workflow

**External · Leonxlnx · [Upstream](https://github.com/Leonxlnx/taste-skill-classics) · [Skill entry](English/legacy/taste-skill-v2-experimental/SKILL.md).** Preserves an experimental workflow that reads page type, audience, references, assets, and constraints before applying design dials. It supports deliberately selected historical landing-page, portfolio, and redesign work. Its own scope excludes dashboards, data tables, and multi-step product interfaces. The output follows that pinned version with dependencies checked against the project. Use it when those exact historical behaviors matter, rather than treating it as an alias for the current taste workflow.

#### `redesign-existing-projects` — retain the earlier targeted-redesign method

**External · Leonxlnx · [Upstream revision](https://github.com/Leonxlnx/taste-skill/tree/e04409a461022e1b9d0e898eac6b9224e2b9dc4e/skills/redesign-skill) · [Skill entry](English/legacy/redesign-skill/SKILL.md).** Preserves the historical scan → diagnose → fix method for an existing website or app. It audits typography, colors, surfaces, and layout, then proposes or applies targeted improvements within the current stack. Choose it explicitly when that earlier method is required. Current taste already incorporates redesign, so the word “redesign” alone does not select this package. Business-page ownership and the product's shared design source remain in place.

For versions, fuller selection conditions, dependencies, overlap comparisons, and provenance, see the [complete skill guide](docs/SKILLS.en.md), [routing guide](docs/ARCHITECTURE.en.md), and [third-party notices](THIRD_PARTY_NOTICES.md).

## Quick start

Use PivotUI with **Codex, Claude Code, DSH (DeepSeek Harness), Cursor, or another compatible Agent**. Choose one of the two installation routes below. Both provide one native **pivotui** entry that reads the complete library's **27 module entrypoints** as needed.

### Option 1: Install with one npx command

With **Node.js 22+, npm/npx and Git** installed, open a terminal in your target project's root and run:

```sh
npx --yes github:Getaway-Wuji/PivotUI --agent codex --language en
```

npx fetches the installer automatically. You do not need to clone the repository yourself or run Python. For another Agent, use the matching command:

```sh
# Claude Code
npx --yes github:Getaway-Wuji/PivotUI --agent claude-code --language en
# DSH / DeepSeek Harness
npx --yes github:Getaway-Wuji/PivotUI --agent dsh --language en
# Cursor
npx --yes github:Getaway-Wuji/PivotUI --agent cursor --language en
```

Use `--language zh` for Chinese. The default installation stays in this project: the complete library goes under `.pivotui/libraries/`, and the native entry goes under `.agents/skills/pivotui/` (or `.claude/skills/pivotui/` for Claude Code). Add `--global` for user-wide installation. [Other Agents, custom paths and preview](docs/INSTALL.en.md#command-install).

### Option 2: Download a ZIP and install it yourself

Download one **project-ready ZIP**: [English](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-English-project-v0.4.0.zip) · [Chinese](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-Chinese-project-v0.4.0.zip).

1. Extract it and open the outer `PivotUI-English/` or `PivotUI-Chinese/` folder. Show dot-prefixed folders if your file manager hides them.
2. Copy its `.pivotui/` contents into the same location at your project's root, keeping the complete library together.
3. For **Codex, DSH or Cursor**, copy `.agents/skills/pivotui/` to your project's `.agents/skills/pivotui/`. For **Claude Code**, copy that same `pivotui/` folder to `.claude/skills/pivotui/` instead; its directory depth stays the same.

Merge only PivotUI's folders and preserve other project skills and settings. Copy the whole `pivotui/` folder, including its hidden manifest; do not install both Agent entries for the same host. This route needs no installation command. The ZIP includes `INSTALL.md`; see also [manual project installation](docs/INSTALL.en.md#zip-install).

Open a new Agent session, select **pivotui**, and describe the interface you want. No MCP setup or manual prompt installation is needed for either route.

The original complete-edition downloads remain available for raw-file or MCP use: [English ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-English-v0.4.0.zip) · [Chinese ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-Chinese-v0.4.0.zip). See the [installation guide](docs/INSTALL.en.md) and [verification record](docs/VALIDATION.md) for details.

## Selection rules and tool requirements

The management layer automates ordinary selection within the cluster's declared boundaries. Seven upstream classics remain explicit opt-in, and historical versions require deliberate selection. The core may recommend them; it does not silently activate them because they are installed. `gpt-taste` is restricted to public marketing and is never assigned to dashboards or business tools.

The cluster runs in a host with the ability to read instructions and perform the requested work. Image workflows need an image-generation tool; Stitch workflows need the corresponding service; public-site checks may need Node and a browser. The local MCP service supplies files rather than those capabilities. Both language roots use the same identifiers, so connect one edition at a time.

## Authorship, external packages, and licenses

PivotUI's cluster organization, management agreement, and nine internal modules are maintained by this project. Original project content is released under the [MIT License](LICENSE), copyright © 2026 Getaway-Wuji. **The 14 external packages were written by their respective upstream authors, not by PivotUI's author.** Their original identities, fixed revisions, copyright notices, and license files are retained.

| Upstream project | Included contributions |
| --- | --- |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Current public-site skill and a pinned historical redesign skill |
| [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) | Four visual directions, Stitch integration, and two historical taste versions |
| [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) | Four image-design and image-first implementation packages |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Searchable UI/UX research guidance, scripts, and datasets |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | Source metadata used by the internally authored product-reference research module |

Read [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md) and each package's `LICENSE` and `UPSTREAM.md` for the exact terms and documented adaptations. Upstream MIT licenses apply to the material they cover; photos, icons, fonts, and other assets may have separate terms. Attribution in this README supplements the bundled legal notices.

## Distribution scope

This repository publishes the usable cluster and its documentation. Local demos, generated test output, private launch settings, virtual environments, caches, raw research, and intermediate reference images are excluded. Necessary upstream runtime assets and their provenance remain with the package that needs them.

Metadata, resource links, language parity, and archive consistency can be checked independently of design execution. A package's presence does not establish that every image service, browser workflow, or target host has been exercised. The research library contains 84 source records and eight document-reviewed case cards; those cards describe their evidence limits. Global style offers 40 reference cards, loaded only when a direction needs exploring.
