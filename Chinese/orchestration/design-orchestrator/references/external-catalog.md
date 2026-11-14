# 已核对外源与能力板块

核对日期：2026-11-14。用户已确认来源为 `Leonxlnx/taste-skill`、其中旧路径 `skills/image-to-code-skill/SKILL.md`，以及 `nextlevelbuilder/ui-ux-pro-max-skill`。按原作者迁移记录追溯，不用其他同名镜像替代。

各包按功能分类放在所选语言根目录下，同类内源和外源共享分类。0.3.0 包含下列十四个外源包及其依赖文件、许可证和来源记录。运行时发现实际安装位置，只读取选中入口和相关资源；随包提供规则不会自动执行规则。

## 身份与当前状态

`taste-skill` 是仓库名和包目录名，实际 Skill 名称为 **`design-taste-frontend`**，两者按同一项能力处理。MCP 接受这两个名称，返回同一入口，不重复登记。随包位置为 `page-design/taste-skill/`，只登记语言根目录即可发现；不要再登记另一份同名安装而造成重复。

当前包与明确固定版本的历史包均已纳入。Classics 保留上游明确选用策略，历史入口仅在明确选择时使用。生图、浏览器、Stitch 等工具仍取决于宿主环境；安装本库不会自动安装或登录这些工具。具体包路径见本版 README，署名见 THIRD_PARTY_NOTICES.md。

## 能力板块

| 板块 | Skill 标识 | 职责与选择规则 |
| --- | --- | --- |
| 官网与作品集 | `design-taste-frontend`（`taste-skill`） | 主导适配其规则的官网和产品展示；协调其生成主题、布局、动效及检查与项目要求 |
| 旧站视觉优化 | `design-taste-frontend`；历史 `redesign-existing-projects` | 当前 taste 声明适用于评审与改版；先核对其具体流程是否相容，不假定存在独立审计模式。历史入口仅在明确固定版本且实际可用时使用。后台区域仍交内源 Dashboard 主力 |
| 设计研究 | `ui-ux-pro-max` | 风格、字体、配色、UX 和组件候选；本集群仅研究与建议，采用值交全局风格归并 |
| 创意营销 | `gpt-taste` | 强构图与动效方向，遵守实际调用策略，仅在明确选择／授权时使用；禁止用于 Dashboard 和业务工具 |
| 指定视觉方向 | `high-end-visual-design`、`minimalist-ui`、`industrial-brutalist-ui` | 分别用于柔和精细、克制编辑式、机械粗野风格的可选经典方向。明确选择适合的一种，不叠加全部流程或替换已定产品 Token |
| 网页视觉稿 | `imagegen-frontend-web` | 生成网页区块参考图；只有用户要求后续实现时才交页面主力 |
| 移动端视觉稿 | `imagegen-frontend-mobile` | 生成一致的 App 页面与流程图，本身不实现前端响应式行为 |
| 品牌探索 | `brandkit` | 生成品牌视觉板与候选，不替代项目权威 Token 文件 |
| 图像先行实现 | `image-to-code` | 当前流程为生成设计图、分析，再实现网站；要求具备生图和编码能力 |
| 专项设计工具 | `stitch-design-taste` | 明确选用时生成面向 Stitch 的 DESIGN.md；另行生成屏幕需要实际 Stitch 访问，MCP 可选 |
| 历史兼容 | `design-taste-frontend-v1`、`design-taste-frontend-v2-experimental` | 仅用于明确的旧版复现，不作为当前 taste 的默认版本 |

用户提供现成图片并要求忠实还原时，保留该图作为目标，由合适的实现主力直接完成，或明确适配可用的图像分析方法。不能调用当前 image-to-code 的生图阶段替换用户原图后仍声称精确还原。只产图的 Skill 同样不能代替组件、交互或响应式实现。

## 原始仓库与路径

| 来源 | 已核对提交 | 包位置 |
| --- | --- | --- |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `f6b76575f949707b4e3c37cd86cb44b0b98643e8` | `skills/taste-skill/SKILL.md`；名称 `design-taste-frontend`，tasteskill 2.5.1 |
| [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) | `5e08c9383dc4ad7fc0df70e1ac8cfa09ec356305` | `skills/` 下的 `soft-skill`、`minimalist-skill`、`brutalist-skill`、`gpt-tasteskill`、`stitch-skill`、`taste-skill-v1`、`taste-skill-v2-experimental`，各含 `SKILL.md` |
| [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) | `beb16b0d0f4dae9a6f5cb04ea41e97b93a54ab8e` | `skills/` 下的 `imagegen-frontend-web`、`imagegen-frontend-mobile`、`brandkit`、`image-to-code`，各含 `SKILL.md` |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `6ae86f61f520d6ca229d2f40e070410638c908c5` | `.claude/skills/ui-ux-pro-max/SKILL.md`；数据、脚本、模板按实际入口依赖获取。仓库 `skill.json` 标识版本 2.15.0 |

用户给出的 `taste-skill/skills/image-to-code-skill/SKILL.md` 是已确认的历史定位；当前原版位于 [imagegen-skills/skills/image-to-code/SKILL.md](https://github.com/Leonxlnx/imagegen-skills/blob/beb16b0d0f4dae9a6f5cb04ea41e97b93a54ab8e/skills/image-to-code/SKILL.md)。记录旧路径与当前位置，不虚构第二个 Skill 身份。

已核对的完整独立旧版见 [历史 redesign 入口](https://github.com/Leonxlnx/taste-skill/blob/e04409a461022e1b9d0e898eac6b9224e2b9dc4e/skills/redesign-skill/SKILL.md)。[当前迁移表](https://github.com/Leonxlnx/taste-skill#moved-skills) 已将该能力归入 taste。`full-output-enforcement` 已从上游移除，且不属于本设计集群范围；不创建占位包，也不自动加入其替代工具。

## 调用、协作与分发

已核对版本中的七个 classics 均要求明确选择调用，保留其显式调用设置。主控可以推荐候选，但仅仅发现已安装并不意味着可以静默调用。结合用户明确选择或授权及宿主实际支持的策略执行；有意适配时如实说明，不修改上游元信息后声称行为未变。见 [classics 调用约定](https://github.com/Leonxlnx/taste-skill-classics#skills)。

每个区域保持一个主力。全局风格生成与校验 Token，主控归并已采用值；Dashboard、交互、组件库、响应式保留各自业务职责。外源风格与图像工具承担选定角色，不包办全部工作。

已核对根仓库的自有代码采用 MIT：[taste](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/LICENSE)、[classics](https://github.com/Leonxlnx/taste-skill-classics/blob/5e08c9383dc4ad7fc0df70e1ac8cfa09ec356305/LICENSE)、[imagegen](https://github.com/Leonxlnx/imagegen-skills/blob/beb16b0d0f4dae9a6f5cb04ea41e97b93a54ab8e/LICENSE)、[UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/6ae86f61f520d6ca229d2f40e070410638c908c5/LICENSE)。抽取子包时保留版权与许可声明，包括所需的仓库根许可证副本；README 署名是补充说明。

Taste 照片和图标有各自许可，需保留来源清单并履行对应条件。UI/UX 仓库还包含与本次核心能力无关的 `ui-styling`，存在 MIT／Apache 标注冲突及独立许可字体，本次 UI/UX 仅导入所需 Skill 与 Python／数据依赖，没有复制无关的 ui-styling 或字体文件。Taste 保留原素材记录并补充本地许可说明，根 MIT 不能代表全部素材的许可。见 [taste 照片记录](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/assets/photos/photos.json) 和 [ui-styling 许可](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/6ae86f61f520d6ca229d2f40e070410638c908c5/.claude/skills/ui-styling/LICENSE.txt)。

两版外源文件逐字节一致并保留原文，每包包含 LICENSE 和 UPSTREAM.md。UI/UX 的命令路径说明做了有记录的便携适配，脚本与数据未改。后续更新保留依赖闭包与声明，并同步两版。包发现和本地检查不等于全部外源设计流程已运行通过。
