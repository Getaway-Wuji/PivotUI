# PivotUI

**Describe the interface you want. Let the cluster choose the skills it needs.**

[简体中文](README.md) · English · [Installation](docs/INSTALL.en.md) · [Every skill explained](docs/SKILLS.en.md) · [Architecture and routing](docs/ARCHITECTURE.en.md)

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

The [complete skill guide](docs/SKILLS.en.md) describes **every internal and external package**, its purpose, selection conditions, outputs, dependencies, and boundaries. Each edition also contains its own inventory and provenance links.

## Download and start

Choose **one** edition:

- [PivotUI English ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-English-v0.4.0.zip)
- [PivotUI Chinese ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-Chinese-v0.4.0.zip)
- [All releases](https://github.com/Getaway-Wuji/PivotUI/releases)

Each archive contains a complete edition with its local MCP source, references, necessary runtime resources, and license notices. Keep its internal directory structure intact.

1. Extract the chosen edition into a stable directory.
2. Follow the [installation guide](docs/INSTALL.en.md): connect its local MCP server or expose its files through your host's supported Skill mechanism.
3. Set `design-orchestrator` as the entry for interface tasks. This entry rule is what enables automatic routing; merely downloading a ZIP does not activate it.
4. Describe the result, scope, references, and existing project constraints in ordinary language.

Example:

```text
Use PivotUI for this interface task. Start with design-orchestrator and
select only the skills needed. Build an order-management list with search,
status filters, pagination, and bulk export. Keep our existing theme and
application shell. Returning from an order's detail must preserve the
applied filters and page number. Implement the page and check the main flow.
```

After the entry rule is saved in your project's instructions, everyday requests can simply describe the work. You can still enter a module directly for a clearly assigned local task.

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
