# Verified External Sources and Capability Groups

Checked: 2026-11-14. The user confirmed `Leonxlnx/taste-skill`, its former `skills/image-to-code-skill/SKILL.md` path, and `nextlevelbuilder/ui-ux-pro-max-skill`. Follow the original author's migration records rather than unrelated same-named mirrors.

Packages are grouped into functional directories under one language root. Internal and external packages share those categories. Release 0.3.0 includes the fourteen external packages below, with their dependency files, licenses, and provenance. Discover the actual installation at runtime and read only selected entries and relevant resources; bundled instructions do not execute themselves.

## Identity and current availability

`taste-skill` is the repository and package-folder name; its actual skill name is **`design-taste-frontend`**. Treat these as one capability. MCP accepts either name and returns the same entry, without a duplicate registration. The included package is `page-design/taste-skill/`; the edition root is sufficient for discovery. Do not also register another installed copy with the same identity.

Current packages and deliberately pinned historical packages are included. Classics retain their upstream explicit-invocation policies; legacy entries require deliberate selection. Image generation, browser, Stitch, and other workflow tools still depend on the host environment. Installing this library does not install or authenticate those tools. See the edition README for exact package paths and THIRD_PARTY_NOTICES.md for attribution.

## Capability groups

| Group | Skill identity | Role and selection rule |
| --- | --- | --- |
| Marketing sites and portfolios | `design-taste-frontend` (`taste-skill`) | Lead compatible public company/product sites; reconcile its generated theme, layout, motion, and checks with project requirements |
| Existing-site refinement | `design-taste-frontend`; historical `redesign-existing-projects` | Current taste declares review and redesign applicability; inspect its prescriptive workflow for compatibility, without assuming a separate audit mode. Use the historical entry only when deliberately pinned and available. Route business dashboard regions to the internal dashboard lead |
| Design research | `ui-ux-pro-max` | Style, typography, palette, UX, and component candidates; research/advice only in this cluster, with adopted tokens consolidated through global style |
| Expressive public marketing | `gpt-taste` | Strong composition and motion direction, only when explicitly selected/authorized under the actual invocation policy; never dashboards or business tools |
| Specific visual directions | `high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui` | Optional classic directions for soft/polished, restrained/editorial, or mechanical/brutalist work. Select a fitting direction explicitly; do not combine all three or replace established product tokens |
| Website design images | `imagegen-frontend-web` | Produce website section reference images; hand them to an implementation lead only when subsequent implementation is requested |
| Mobile design images | `imagegen-frontend-mobile` | Produce coherent app screen/flow images; does not itself implement responsive frontend behavior |
| Brand exploration | `brandkit` | Produce visual identity boards and candidates; does not replace the authoritative project token file |
| Image-first implementation | `image-to-code` | Current workflow generates design images, analyzes them, then implements a site; requires image generation and coding capability |
| Specific design tooling | `stitch-design-taste` | Produce a Stitch-oriented DESIGN.md when explicitly selected; generating screens separately requires actual Stitch access, with MCP optional |
| Historical compatibility | `design-taste-frontend-v1`, `design-taste-frontend-v2-experimental` | Use only for explicit legacy reproduction; do not select them as the current taste default |

For an existing image that must be reproduced faithfully, retain that image as the target. Use an appropriate implementation lead directly or explicitly adapt applicable image-analysis guidance. Do not invoke the current image-to-code generation stage to replace the supplied design while claiming exact reproduction. Images-only skills likewise do not replace component, interaction, or responsive implementation.

## Original repositories and paths

| Source | Checked revision | Package locations |
| --- | --- | --- |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `f6b76575f949707b4e3c37cd86cb44b0b98643e8` | `skills/taste-skill/SKILL.md`; name `design-taste-frontend`, tasteskill 2.5.1 |
| [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) | `5e08c9383dc4ad7fc0df70e1ac8cfa09ec356305` | `skills/soft-skill`, `minimalist-skill`, `brutalist-skill`, `gpt-tasteskill`, `stitch-skill`, `taste-skill-v1`, `taste-skill-v2-experimental`; each has `SKILL.md` |
| [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) | `beb16b0d0f4dae9a6f5cb04ea41e97b93a54ab8e` | Under `skills/`: `imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit`, `image-to-code`; each has `SKILL.md` |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `6ae86f61f520d6ca229d2f40e070410638c908c5` | `.claude/skills/ui-ux-pro-max/SKILL.md`; source data/scripts/templates must follow the actual entry's dependencies. Repository `skill.json` identifies 2.15.0 |

The former `taste-skill/skills/image-to-code-skill/SKILL.md` is the user's confirmed historical locator. The current original is [imagegen-skills/skills/image-to-code/SKILL.md](https://github.com/Leonxlnx/imagegen-skills/blob/beb16b0d0f4dae9a6f5cb04ea41e97b93a54ab8e/skills/image-to-code/SKILL.md). Record old and current paths without inventing a second skill identity.

The last inspected full independent redesign entry is [the historical redesign skill](https://github.com/Leonxlnx/taste-skill/blob/e04409a461022e1b9d0e898eac6b9224e2b9dc4e/skills/redesign-skill/SKILL.md). The [current migration table](https://github.com/Leonxlnx/taste-skill#moved-skills) folds that capability into taste. `full-output-enforcement` was removed upstream and is outside this design cluster; do not create a placeholder or silently add its replacement utility.

## Invocation, coordination, and distribution

All seven classics are opt-in in the inspected upstream version. Preserve their explicit invocation settings. The core may recommend a suitable candidate; availability alone does not authorize silent invocation. Apply explicit user selection or authorization within the host's supported policy, and describe any deliberate adaptation accurately. Do not change upstream metadata and claim unchanged behavior. See the [classics invocation contract](https://github.com/Leonxlnx/taste-skill-classics#skills).

Keep one lead per region. Global style owns token generation/validation; the orchestrator consolidates adopted values. The dashboard, interaction, component, and responsive modules retain their business responsibilities. External style and image tools fill a selected role rather than replacing all of them.

The inspected roots use MIT for their own code: [taste](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/LICENSE), [classics](https://github.com/Leonxlnx/taste-skill-classics/blob/5e08c9383dc4ad7fc0df70e1ac8cfa09ec356305/LICENSE), [imagegen](https://github.com/Leonxlnx/imagegen-skills/blob/beb16b0d0f4dae9a6f5cb04ea41e97b93a54ab8e/LICENSE), [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/6ae86f61f520d6ca229d2f40e070410638c908c5/LICENSE). Preserve original copyright and license notices when extracting a package, including a copy of its root license. README attribution supplements those notices.

Taste photos/icons have individual licenses; retain their source manifests and obligations. The UI/UX repository also includes unrelated `ui-styling` content with conflicting MIT/Apache metadata and separately licensed fonts. The UI/UX import contains only the required skill package and its Python/data dependencies; unrelated ui-styling and font files were not copied. Taste retains its original asset records and added local license notices. Root MIT is not blanket clearance for every asset. See [taste photo records](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/assets/photos/photos.json) and the [ui-styling license](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/6ae86f61f520d6ca229d2f40e070410638c908c5/.claude/skills/ui-styling/LICENSE.txt).

Both editions contain identical external package bytes and original upstream language. Each package includes LICENSE and UPSTREAM.md. UI/UX command-path instructions have a documented portability adaptation; its scripts and datasets remain unchanged. Future updates preserve dependency closure and notices, then update both editions together. Package discovery and local checks do not establish that every external design workflow has run successfully.
