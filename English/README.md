# PivotUI — English

Cluster release: 0.5.0
Language: English for authored instructions; original upstream language for external packages.

Skills are grouped by function. Internal and external packages serving the same function share a category; origin is recorded in the table below. Start with [design-orchestrator](orchestration/design-orchestrator/SKILL.md), or enter a clearly scoped module directly. The orchestrator loads only selected entries and relevant references.

```text
English/
├── orchestration/
│   ├── design-orchestrator/
│   └── global-style-skill/
├── page-design/
│   ├── dashboard-design/
│   ├── data-list-design/
│   ├── detail-page-design/
│   ├── form-workflow-design/
│   ├── app-shell-design/
│   └── taste-skill/
├── interaction/
│   └── interaction-design/
├── components/
│   └── component-system/
├── responsive/
│   └── responsive-design/
├── design-research/
│   ├── ui-ux-pro-max/
│   └── design-reference-research/
├── visual-styles/
│   ├── gpt-tasteskill/
│   ├── soft-skill/
│   ├── minimalist-skill/
│   └── brutalist-skill/
├── image-design/
│   ├── imagegen-frontend-web/
│   ├── imagegen-frontend-mobile/
│   ├── brandkit/
│   └── image-to-code/
├── tool-integrations/
│   └── stitch-skill/
├── legacy/
│   ├── taste-skill-v1/
│   ├── taste-skill-v2-experimental/
│   └── redesign-skill/
├── design-system/
├── mcp/
├── README.md
└── THIRD_PARTY_NOTICES.md
```

`design-system/` contains shared methods and `mcp/` contains loading infrastructure. Category directories organize capabilities without merging their instructions. Every package retains a standard `SKILL.md` and its own resources.

## Skill inventory and provenance

| Skill | Origin | Functional directory | Status | Role and entry | Source / version |
| --- | --- | --- | --- | --- | --- |
| `design-orchestrator` | Internal | `orchestration` | Included | [Routing, regional ownership, token consolidation](orchestration/design-orchestrator/SKILL.md) | This project / 1.3.0 |
| `global-style-skill` | Internal | `orchestration` | Included | [Visual direction and project tokens](orchestration/global-style-skill/SKILL.md) | This project / 1.1.3 |
| `dashboard-design` | Internal | `page-design` | Included | [Dashboard structure, metrics, charts, summaries](page-design/dashboard-design/SKILL.md) | This project / 1.1.4 |
| `data-list-design` | Internal | `page-design` | Included | [Complete lists, query/selection scope, bulk tasks and detail return](page-design/data-list-design/SKILL.md) | This project / 1.0.0 |
| `detail-page-design` | Internal | `page-design` | Included | [Entity detail views, attribute groups, safe actions and return continuity](page-design/detail-page-design/SKILL.md) | This project / 1.0.0 |
| `form-workflow-design` | Internal | `page-design` | Included | [Full-page forms, edit flows, wizards, settings and dirty-state protection](page-design/form-workflow-design/SKILL.md) | This project / 1.0.0 |
| `app-shell-design` | Internal | `page-design` | Included | [Application frame, route context, content boundaries and scrolling](page-design/app-shell-design/SKILL.md) | This project / 1.0.0; MIT; see edition LICENSE |
| `design-taste-frontend` | External | `page-design` | Imported | [Compatible company/product pages and existing-site audits](page-design/taste-skill/SKILL.md) | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · 2.5.1 · `f6b7657` · MIT |
| `interaction-design` | Internal | `interaction` | Included | [States, feedback, focus, keyboard, recovery](interaction/interaction-design/SKILL.md) | This project / 1.1.0 |
| `component-system` | Internal | `components` | Included | [Shared components, interfaces, purposeful variants](components/component-system/SKILL.md) | This project / 1.0.1 |
| `responsive-design` | Internal | `responsive` | Included | [Content priority, layout changes, touch, overflow and browser audit](responsive/responsive-design/SKILL.md) | This project / 1.0.3 |
| `design-reference-research` | Internal | `design-research` | Included; 12 document-reviewed cases | [Named product references and scoped comparisons](design-research/design-reference-research/SKILL.md) | This project / 1.1.0; [VoltAgent source data](https://github.com/VoltAgent/awesome-design-md) · `fcc7028` · MIT data; MIT authored guidance; see edition LICENSE |
| `ui-ux-pro-max` | External | `design-research` | Imported; local research checked | [Design research and candidates only](design-research/ui-ux-pro-max/SKILL.md) | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 2.15.0 · `6ae86f6` · MIT |
| `gpt-taste` | External | `visual-styles` | Imported; explicit opt-in | [Expressive public marketing; never business tools](visual-styles/gpt-tasteskill/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `high-end-visual-design` | External | `visual-styles` | Imported; explicit opt-in | [Soft, polished visual direction](visual-styles/soft-skill/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `minimalist-ui` | External | `visual-styles` | Imported; explicit opt-in | [Restrained editorial/product direction](visual-styles/minimalist-skill/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `industrial-brutalist-ui` | External | `visual-styles` | Imported; explicit opt-in | [Industrial, mechanical, brutalist direction](visual-styles/brutalist-skill/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `imagegen-frontend-web` | External | `image-design` | Imported; image tools required | [Website section design images](image-design/imagegen-frontend-web/SKILL.md) | [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT |
| `imagegen-frontend-mobile` | External | `image-design` | Imported; image tools required | [App screen and flow design images](image-design/imagegen-frontend-mobile/SKILL.md) | [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT |
| `brandkit` | External | `image-design` | Imported; image tools required | [Brand identity boards and candidates](image-design/brandkit/SKILL.md) | [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT |
| `image-to-code` | External | `image-design` | Imported; image and coding tools required | [Generate design images, analyze, then implement](image-design/image-to-code/SKILL.md) | [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT |
| `stitch-design-taste` | External | `tool-integrations` | Imported; explicit opt-in; Stitch required | [Google Stitch-specific workflow](tool-integrations/stitch-skill/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `design-taste-frontend-v1` | External | `legacy` | Imported; explicit historical selection | [Historical compatibility; not the current default](legacy/taste-skill-v1/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `design-taste-frontend-v2-experimental` | External | `legacy` | Imported; explicit historical selection | [Experimental historical compatibility](legacy/taste-skill-v2-experimental/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `redesign-existing-projects` | External | `legacy` | Imported; explicit historical selection | [Pinned historical standalone redesign workflow](legacy/redesign-skill/SKILL.md) | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · `e04409a` · MIT |

The inventory above registers **25 packages: 11 internal and 14 external**, with **29 Skill entrypoints** counted from their actual standard entry files including four nested interaction entries: `button-interaction`, `form-interaction`, `navigation-interaction`, and `floating-components`. Keep those nested entries with their parent and shared resources. These counts match the registered packages and current standard entry files, including `data-list-design`, `detail-page-design`, `form-workflow-design`, and `app-shell-design`. Responsive design includes a reusable Playwright browser audit script verified on the workspace's integrated workflow demo; physical-device testing has not been performed.

`taste-skill` is the package/repository alias of `design-taste-frontend`, not another skill. Folder names such as `gpt-tasteskill` and `soft-skill` preserve upstream identities while their YAML names remain `gpt-taste` and `high-end-visual-design`. The [external catalog](orchestration/design-orchestrator/references/external-catalog.md) records current and historical locations, fixed revisions, and routing boundaries.

All 14 external packages are imported from pinned revisions and retain their original license notices. See [third-party notices](THIRD_PARTY_NOTICES.md) and each package's `UPSTREAM.md` for authors, revisions, additions, and applicable asset terms. MIT in the inventory identifies upstream code/instructions; it is not a blanket license for all bundled photos, icons, fonts, or other assets.

## Selection and use

Release 0.4.1 connects shared decisions to their owner, implementation and actual verification in existing project records, including solo work. Checks follow the change: theme consumption, shared component callers, and reading/keyboard order after responsive rearrangement. Reuse valid evidence and keep local repairs scoped. Mood-only references with sufficient direction do not automatically trigger case research; explicit research and missing source evidence still do. This update adds no product case or runtime-verification claim.

[Product reference research](design-research/design-reference-research/SKILL.md) includes an 84-record source catalog and twelve document-reviewed case cards. Start with its [small index](design-research/design-reference-research/references/index.md), then read only relevant catalog shards or 1–3 case cards. The other 72 records retain unknown page scope until inspected. Third-party analyses, recommendations and illustrative examples remain distinct; document review does not verify the live product. Research proposes evidence and adaptations while page leads and the project token source retain ownership. No automatic second research pass or new MCP tool is required.

Global style includes [40 style reference cards](orchestration/global-style-skill/references/styles/index.md) in seven overlapping browsing groups. For an unresolved direction, use its [selection rules](orchestration/global-style-skill/references/style-selection.md), then read only relevant cards. Inherit established visuals, choose provisionally when the task is clear, and ask about materially different unresolved alternatives. Advice-only work stops at recommendations. These references add no skill entries and do not automatically invoke research or opt-in external workflows.

- **Files:** expose selected package directories using the host's supported skill mechanism. Hosts that cannot scan category or nested directories can use the actual entry paths above. Preserve each package's full resources.
- **MCP:** follow the [local server guide](mcp/skill-cluster/README.md). The edition root discovers functionally grouped packages. Catalog metadata includes `category` and `allow_implicit_invocation`; select an entry, then read only necessary resources. Catalog discovery does not load every Skill body.

Choose one language edition per cluster connection. Both editions share stable identifiers; connecting both can create duplicate-name ambiguity. Language selection does not preload all instructions or dictate the language of the conversation or generated product.

Retain upstream invocation rules. The seven classics entries are explicit opt-in; their presence does not authorize silent invocation. Legacy versions require a matching explicit historical task and do not automatically replace the current version. `gpt-taste` serves public marketing only, never dashboards or business tools. `ui-ux-pro-max` supplies research and recommendations in this cluster; it does not take over page implementation or the adopted token source.

Image-design packages need the actual image-generation tools required by their entries; Stitch needs its tool connection. Downloading the files does not satisfy those dependencies or prove browser, image, or design workflows have run. Current `image-to-code` generates reference images before analysis and implementation. For faithful reproduction of an existing image, keep that image as the target and select an appropriate image-capable implementation lead.

The [foundations](design-system/FOUNDATIONS.md) and [orchestration agreement](design-system/ORCHESTRATION.md) guide skill authoring and complex coordination. Ordinary interface work reads relevant constraints only. Product tokens remain in one authoritative source in the target product; this cluster maintains reusable methods.

## Maintenance and verification

Maintain authored English instructions first, then synchronize equivalent Chinese instructions and resources. External packages remain in their original language with identical bytes in both editions. UI/UX Pro Max has a documented minimal command-path adaptation for portability; its search code and datasets remain unchanged. Preserve upstream package identifiers and fixed source revisions when updating.

The first two inventory columns identify skill name and origin for release checks. Keep both edition tables aligned. Place future packages in the appropriate functional category, include their actual dependency closure and required notices, and update provenance rather than introducing source-based container directories.

Release checks cover metadata, relative references, paired inventories, invocation-policy discovery, language isolation, and archive-to-source equality. Actual checks and their limits belong in the authoring records. Local UI/UX research was checked after moving and renaming its package; this does not establish every external workflow or host has been tested. This publication does not imply execution of every remote design workflow.

Each release contains one complete language edition, its local MCP source, and usage documents. Personal launch settings, virtual environments, caches, raw research, and historical demos are excluded.

## Project license

PivotUI original instructions, documentation and MCP implementation are MIT licensed by Getaway-Wuji; see [LICENSE](LICENSE). External packages and assets retain their own licenses and credits. The public distribution omits the local MCP test file; upstream package examples and resources remain intact. See [GETTING_STARTED](GETTING_STARTED.md).
