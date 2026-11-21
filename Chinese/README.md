# PivotUI — 中文版

集群发布版本：0.4.2
语言：自制规则使用中文；外源包保留作者原文。

Skills 按功能分类。同一功能的内源与外源包放在同一板块，来源在下表登记。从 [design-orchestrator](orchestration/design-orchestrator/SKILL.md) 开始，或对范围明确的任务直接使用对应模块。主控只加载选中的入口与当前需要的参考。

```text
Chinese/
├── orchestration/
│   ├── design-orchestrator/
│   └── global-style-skill/
├── page-design/
│   ├── dashboard-design/
│   ├── data-list-design/
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

`design-system/` 保存共用方法，`mcp/` 提供加载支持。分类目录组织能力，不合并各 Skill 的正文；每个包保留标准 `SKILL.md` 和自己的资源。

## Skill 清单与来源

| Skill | 来源 | 功能目录 | 状态 | 职责与入口 | 来源 / 版本 |
| --- | --- | --- | --- | --- | --- |
| `design-orchestrator` | 内源 | `orchestration` | 已包含 | [路由、区域分工与 Token 汇总](orchestration/design-orchestrator/SKILL.md) | 本项目 / 1.2.7 |
| `global-style-skill` | 内源 | `orchestration` | 已包含 | [视觉方向与项目 Token](orchestration/global-style-skill/SKILL.md) | 本项目 / 1.1.3 |
| `dashboard-design` | 内源 | `page-design` | 已包含 | [Dashboard 结构、指标、图表与摘要](page-design/dashboard-design/SKILL.md) | 本项目 / 1.1.4 |
| `data-list-design` | 内源 | `page-design` | 已包含 | [完整列表、查询／选择范围、批量任务与详情返回](page-design/data-list-design/SKILL.md) | 本项目 / 1.0.0 |
| `app-shell-design` | 内源 | `page-design` | 已包含 | [应用框架、路由上下文、内容边界与滚动](page-design/app-shell-design/SKILL.md) | 本项目 / 1.0.0；MIT，见本版 LICENSE |
| `design-taste-frontend` | 外源 | `page-design` | 已导入 | [适配其规则的官网、产品页与既有站点审计](page-design/taste-skill/SKILL.md) | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · 2.5.1 · `f6b7657` · MIT |
| `interaction-design` | 内源 | `interaction` | 已包含 | [状态、反馈、焦点、键盘与恢复](interaction/interaction-design/SKILL.md) | 本项目 / 1.1.0 |
| `component-system` | 内源 | `components` | 已包含 | [共用组件、接口与有用途的变体](components/component-system/SKILL.md) | 本项目 / 1.0.1 |
| `responsive-design` | 内源 | `responsive` | 已纳入 | [内容优先级、布局变化、触屏与溢出](responsive/responsive-design/SKILL.md) | 本项目 / 1.0.2 |
| `design-reference-research` | 内源 | `design-research` | 已包含；案例经文档审查 | [具名产品参考与限定范围的比较](design-research/design-reference-research/SKILL.md) | 本项目 / 1.0.1；[VoltAgent 来源数据](https://github.com/VoltAgent/awesome-design-md) · `fcc7028` · 数据为 MIT；自制规则为 MIT，见本版 LICENSE |
| `ui-ux-pro-max` | 外源 | `design-research` | 已导入；本地检索已验证 | [仅设计研究与候选](design-research/ui-ux-pro-max/SKILL.md) | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 2.15.0 · `6ae86f6` · MIT |
| `gpt-taste` | 外源 | `visual-styles` | 已导入；显式选用 | [高表现力对外营销；禁止用于业务工具](visual-styles/gpt-tasteskill/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `high-end-visual-design` | 外源 | `visual-styles` | 已导入；显式选用 | [柔和精细视觉方向](visual-styles/soft-skill/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `minimalist-ui` | 外源 | `visual-styles` | 已导入；显式选用 | [克制的编辑式及产品视觉](visual-styles/minimalist-skill/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `industrial-brutalist-ui` | 外源 | `visual-styles` | 已导入；显式选用 | [工业、机械与粗野视觉方向](visual-styles/brutalist-skill/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `imagegen-frontend-web` | 外源 | `image-design` | 已导入；需生图工具 | [网页区块设计图](image-design/imagegen-frontend-web/SKILL.md) | [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT |
| `imagegen-frontend-mobile` | 外源 | `image-design` | 已导入；需生图工具 | [App 页面与流程设计图](image-design/imagegen-frontend-mobile/SKILL.md) | [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT |
| `brandkit` | 外源 | `image-design` | 已导入；需生图工具 | [品牌视觉板与候选](image-design/brandkit/SKILL.md) | [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT |
| `image-to-code` | 外源 | `image-design` | 已导入；需生图与编码能力 | [先生成设计图，再分析与实现](image-design/image-to-code/SKILL.md) | [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT |
| `stitch-design-taste` | 外源 | `tool-integrations` | 已导入；显式选用；需 Stitch | [Google Stitch 专项流程](tool-integrations/stitch-skill/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `design-taste-frontend-v1` | 外源 | `legacy` | 已导入；明确选用历史版本 | [历史兼容；非当前默认](legacy/taste-skill-v1/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `design-taste-frontend-v2-experimental` | 外源 | `legacy` | 已导入；明确选用历史版本 | [实验历史版本兼容](legacy/taste-skill-v2-experimental/SKILL.md) | [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT |
| `redesign-existing-projects` | 外源 | `legacy` | 已导入；明确选用历史版本 | [固定历史独立改版流程](legacy/redesign-skill/SKILL.md) | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · `e04409a` · MIT |

上表登记 **23 个包：9 个内源、14 个外源**，按其实际标准入口文件统计共 **27 个 Skill 入口**；其中四个交互入口嵌套在父包内：`button-interaction`、`form-interaction`、`navigation-interaction`、`floating-components`。保留这些入口的父包与共享资源。此数量与已登记包及当前标准入口文件一致，包括已完成的数据列表与应用框架模块。响应式已通过独立双语文档与本地链接审阅并纳入；尚未进行浏览器或真机测试。

`taste-skill` 是 `design-taste-frontend` 的包／仓库别名，不是另一个 Skill。`gpt-tasteskill`、`soft-skill` 等目录保留上游包名，其 YAML 名称仍为 `gpt-taste`、`high-end-visual-design`。[外源目录](orchestration/design-orchestrator/references/external-catalog.md) 记录当前与历史位置、固定提交和路由边界。

14 个外源包均按固定提交导入，并保留原始许可声明。作者、提交、增补文件及素材条款见 [第三方声明](THIRD_PARTY_NOTICES.md) 和各包的 `UPSTREAM.md`。清单中的 MIT 指上游代码／规则，不是对全部照片、图标、字体或其他素材的统一授权。

## 选择与使用

0.4.1 在已有项目记录中把共享决定对应到负责人、实现和实际验证，单人完成也适用。检查按改动触发：主题实际使用、公共组件调用处，以及响应式重排后的阅读／键盘顺序。复用有效证据，局部修复保持范围。名称仅传达氛围且方向依据充分时不自动触发案例研究；明确研究要求和缺失来源依据仍需处理。本次不新增产品案例或界面运行验证声明。

[产品案例研究](design-research/design-reference-research/SKILL.md)增加 84 项来源目录与 8 张经文档审查的案例卡。从[简短索引](design-research/design-reference-research/references/index.md)进入，只读相关目录分片或 1–3 张案例卡。其余 76 项在查验前保留页面范围未知。第三方分析、作者建议与演示示例分别标明；文档审查不代表已验证线上产品。研究模块提供证据与适配建议，页面负责人和项目 Token 来源保持原有职责。无需强制第二遍研究，也不增加 MCP 工具。

全局风格包含[40张风格参考卡](orchestration/global-style-skill/references/styles/index.md)，分为七个可交叉的浏览分类。方向未定时使用[选型规则](orchestration/global-style-skill/references/style-selection.md)，再只读相关卡片。沿用已有视觉设定；任务明确时自动选择暂定方案；明显不同且无法推断的方向才询问用户。只咨询时止于建议。这些参考不增加 Skill 入口，也不自动调用研究或需明确选用的外源流程。

- **直接读文件**：按宿主支持的技能机制接入选中的包目录。宿主不能扫描分类或嵌套目录时，使用上表中的实际入口路径，并保留完整包资源。
- **MCP**：按 [本地服务说明](mcp/skill-cluster/README.md) 接入。语言版根目录可发现按功能分类的包；目录元数据包含 `category` 与 `allow_implicit_invocation`。先选入口，再读取必要资源，发现目录不全量加载 Skill 正文。

一个集群连接选择一种语言。两版保留相同标识，同时连接可能造成同名歧义。语言选择不预加载全部规则，也不强制对话或生成产品的语言。

保留上游调用规则。七个 Classics 入口需显式选用，文件已导入不等于允许静默调用。历史版本只用于相匹配的明确历史任务，不自动替代当前版本。`gpt-taste` 仅用于对外营销，禁止用于 Dashboard 或业务工具。`ui-ux-pro-max` 在本集群中负责研究与建议，不接管页面实现或已采用的 Token 来源。

图像设计包需要入口要求的实际生图工具，Stitch 需要相应工具连接。下载文件不等于工具依赖已经满足，也不代表浏览器、生图或设计流程已执行。当前 `image-to-code` 先生成参考图，再分析与实现；忠实还原已有图片时，保留所给图片作为目标，选择具备读图能力的实现主力。

[共用规范](design-system/FOUNDATIONS.md) 与 [联动方案](design-system/ORCHESTRATION.md) 用于制作 Skill 和复杂协作；普通界面任务只读相关约束。产品 Token 保留在目标产品唯一的权威来源中，本集群维护可复用的方法。

## 维护与验证

先维护英文自制规则，再同步等义的中文规则与资源。外源保留原文，两版逐字节一致。UI/UX Pro Max 做了已记录的最小命令路径适配，以支持迁移；检索代码与数据未改。更新时保留上游包标识并固定来源版本。

清单前两列供发布检查识别 Skill 名称与来源，两版须保持一致。新包放入适合的功能板块，带齐实际依赖与必要声明，并更新来源记录，不增加按内外源划分的容器目录。

发布检查涵盖元信息、相对引用、两版清单、调用策略发现、语言隔离与压缩包和源文件的一致性。实际检查与边界记录在制作档案中。UI/UX 本地检索已在包移动并更名后检查，但不代表全部外源流程或宿主都已验证。本次发布不表示已上传 GitHub 或执行所有远端设计流程。

每份发布包包含一套完整语言版、本地 MCP 源码与使用说明；排除个人启动配置、虚拟环境、缓存、原始研究和历史演示。

## 项目许可

PivotUI 原创规则、文档及 MCP 实现由 Getaway-Wuji 以 MIT 许可发布，见 [LICENSE](LICENSE)。外源包与素材保留各自许可和署名。公开发行版不包含本地 MCP 测试文件；上游包自带的示例和资源保持完整。参见 [开始使用](GETTING_STARTED.md)。
