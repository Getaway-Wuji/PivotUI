# PivotUI 全部 Skill 详解

[首页](../README.md) · [安装配置](INSTALL.zh-CN.md) · [任务分配](ARCHITECTURE.zh-CN.md) · [English](SKILLS.en.md)

版本 **0.5.0** 包含 **25 个包：11 个内源模块、14 个外源包**。交互包内另有 4 个子模块，因此标准 `SKILL.md` 入口总数为 **29 个**。参考卡、模板和数据集属于资源，不另计为 Skill。

“内源”表示本项目编写的能力，“外源”表示从明确署名的上游引入的包。内源并不代表全部参考材料均为原创，例如产品案例研究模块使用了署名的 VoltAgent 来源元数据。许可范围和本地适配见 [THIRD_PARTY_NOTICES](../THIRD_PARTY_NOTICES.md)、各包的 `LICENSE` 与 `UPSTREAM.md`。

以下链接指向中文版，英文版采用相同目录与 Skill 标识。安装时保留完整包目录。

## 内源模块

### 1. `design-orchestrator`：任务统一入口

[入口](../Chinese/orchestration/design-orchestrator/SKILL.md) · `orchestration/design-orchestrator` · **1.3.0**

**用途。** 将自然语言需求转成可协作的设计任务。先判断用户要的是建议、审查、设计图、设计变量还是代码，再选出足够完成任务的最小能力组合。

**何时使用。** 作为界面任务默认入口，尤其适合页面、组件、交互、视觉决策和多个区域交织的工作。已经明确分配的局部任务可以直接进入专项模块。

**工作与产出。** 确认范围、参考权威性、已有主题和组件、可用工具、区域负责人及验收条件；形成简短工作约定，读取必要入口和资源，整合共用改动并推进到交付。公开网站和后台可以分别指定主负责人。

**边界。** 规则由宿主中的 AI 执行，主控不是独立调度程序，也不会把全部模块细则塞进入口。它保留上游明确调用规则，复用已读内容，避免循环转交，每个区域和组件只有一个整合负责人。

### 2. `global-style-skill`：视觉方向与设计变量

[入口](../Chinese/orchestration/global-style-skill/SKILL.md) · `orchestration/global-style-skill` · **1.1.3**（含静态校验脚本 `scripts/check_tokens.py`）

**用途。** 选择或比较视觉方向，生成、补充、迁移、整理和验证产品设计变量。包含 **40 张风格参考卡**，按七个可重叠的浏览分组组织，提供可选视觉属性。

**何时使用。** 新主题、品牌迁移、风格尚未确定、跨区域一致性问题或明确的变量检查。现有主题完整时，一处交互修复不需要启动此模块。

**工作与产出。** 找到当前可编辑的主题来源，理解参考，区分可验证值与截图估计值；按需给出具体的颜色、字体、间距、形状等值，检查非法值、重名、缺失引用、循环引用与实际使用情况。可以交付方向建议、可用变量修改或能定位的检查结果。

**边界。** 不负责页面组织和组件实现。页面负责人已有合适方向时直接复用；探索候选不等于授权替换主题。最终采用的值保留在目标产品的一份权威来源中。

### 3. `dashboard-design`：业务概览与分析

[入口](../Chinese/page-design/dashboard-design/SKILL.md) · `page-design/dashboard-design` · **1.1.4**

**用途。** 将业务问题转成指标层级、图表、摘要、信息表达和操作入口。七类结构覆盖业务概览、诊断分析、实时监控、团队工作台、账户资源概览、内容发现与专题报告。

**何时使用。** 分析、运营、监控、工作台和资源 Dashboard。用户参考可以指定结构或视觉方向。

**工作与产出。** 明确角色、要做的判断、指标定义、周期、对比基准、数据状态、首屏优先级与下钻路径；交付所需设计说明、实现提示词、工作页面或局部修改。状态按任务区分零值、缺失、加载、无结果、部分更新、错误和过期数据。

**边界。** 负责 Dashboard 内容与必要行为，复用应用框架。完整业务列表与全局导航交由对应模块。已有合适主题或忠实还原参考时，跳过视觉配方选择；也可只给原图还原的实现者提供数据语义建议，而不接管页面。

### 4. `data-list-design`：完整业务数据列表

[入口](../Chinese/page-design/data-list-design/SKILL.md) · `page-design/data-list-design` · **1.0.0**

**用途。** 将查找记录、执行操作和返回继续工作组织成连续流程，负责完整列表页的组织与业务语义。

**何时使用。** 包含搜索、筛选、排序、分页、列设置、视图、选择、批量操作、导出或详情返回的后台列表。功能按实际任务选取，不强制每页都配齐。

**工作与产出。** 明确识别与比较字段、查询和结果范围、权限、数据规模、选择边界、批量任务影响和导出对象。从详情返回保留已应用筛选和页码，区分当前页选择与所有查询结果选择。交付设计规格或可用列表及实际流程检查。

**边界。** 复用应用框架和设计变量。`component-system` 负责可复用 Table 与控件实现，列表负责人决定它们如何表达业务工作。Dashboard 内的小摘要表或单个控件问题不自动触发完整列表流程。

### `detail-page-design`：实体详情页与安全操作

[入口](../Chinese/page-design/detail-page-design/SKILL.md) · `page-design/detail-page-design` · **1.0.0**

**用途。** 组织单条业务记录的身份页头、状态标签、结构化属性分组、关联数据、安全操作、404/403/过期异常状态以及来源列表返回连续性。

### `form-workflow-design`：整页表单、向导与设置页

[入口](../Chinese/page-design/form-workflow-design/SKILL.md) · `page-design/form-workflow-design` · **1.0.0**

**用途。** 组织整页新建/编辑表单、多分区系统设置与分步向导，落实草稿与源数据隔离、脏状态拦截、错误汇总定位与吸底保存栏。

### 5. `app-shell-design`：应用共用框架

[入口](../Chinese/page-design/app-shell-design/SKILL.md) · `page-design/app-shell-design` · **1.0.0**

**用途。** 让用户在后台的不同页面之间保持位置感，统一导航、页面上下文和滚动。

**何时使用。** 共用导航层级、侧栏或顶栏、面包屑、标题与操作区、内容宽度与内边距、固定区域、滚动归属，以及列表—详情—编辑之间的连续性。

**工作与产出。** 区分持续存在的框架、随路由变化的上下文和页面内容，约定路由元数据、标题/操作插槽、内容边界、滚动容器和返回状态责任。可以实现框架或交付对应规格，检查嵌套路由、长标签、键盘、折叠、窄短视口、遮挡及返回路径。

**边界。** 页面模块继续负责业务内容。Ant Design Pro 风格的框架是有范围的参考，不要求所有应用都使用侧栏，也不因此更换路由器。复用有效结构，仅在必要时加入导航交互、组件和响应式支持。

### 6. `interaction-design`：状态、反馈与失败恢复

[入口](../Chinese/interaction/interaction-design/SKILL.md) · `interaction/interaction-design` · **1.1.0**

**用途。** 按 **触发 → 状态变化 → 用户反馈 → 退出或恢复** 定义可理解、可恢复的交互，协调以下四个子入口与共用异步规则。

**何时使用。** 跨组件行为、请求生命周期、状态混淆、键盘/焦点问题、筛选竞态、提交、批量结果、撤销或具体动效需求。

**工作与产出。** 区分输入反馈与业务状态，明确真实成功和结果未知，防止重复提交，拒绝过时响应，失败后保留上下文。需要动画时可按需读取 React Bits 指南和目录，也可复用现有可靠组件。交付范围明确的行为规格或代码，以及适用检查。

**边界。** 保留已有布局、业务校验和主题归属；动画结束不代表请求成功。四个子模块随父包发布，共用父包资料，不需要全部同时读取。

#### 6a. `button-interaction`：按钮交互

[入口](../Chinese/interaction/interaction-design/sub-skills/button-interaction/SKILL.md)

负责命令按钮的 hover、focus、pressed、disabled、pending、结果和恢复状态，保持点击区域稳定，将短暂反馈、持续选择和远程操作分开。规定原生语义、键盘激活、可访问名称、执行保护和防重复机制。长按或滑动确认需要等价可访问路径和真实取消规则。导航链接、整表校验与消息容器选择由对应子模块负责；错误保留在附近或 Alert 中，不使用 Toast。

#### 6b. `form-interaction`：表单交互

[入口](../Chinese/interaction/interaction-design/sub-skills/form-interaction/SKILL.md)

负责字段、选择器、开关、滑块、校验、筛选和提交反馈。错误后保留草稿，区分已提交快照与请求期间继续输入的新内容，防止旧响应覆盖新编辑。处理错误关联、首个错误焦点、输入法组合输入、已应用筛选与结果一致性，以及结果未知后的安全继续路径。交付可实现的字段和请求行为，保持页面结构及业务校验规则。

#### 6c. `navigation-interaction`：导航交互

[入口](../Chinese/interaction/interaction-design/sub-skills/navigation-interaction/SKILL.md)

负责侧栏、面包屑、页内 Tabs 和命令菜单中的当前位置、展开、键盘与焦点连续性。区分真实路由、hover、focus 与展开状态；组件名叫 Menu 不代表普通导航链接就应使用命令菜单键盘模型。记录被删除或重排后选择合理焦点落点，路由失败时保留真实位置。信息架构和页面布局仍属于框架或页面负责人。

#### 6d. `floating-components`：浮层与反馈组件

[入口](../Chinese/interaction/interaction-design/sub-skills/floating-components/SKILL.md)

负责选择和实现 Tooltip、Toast、Alert、Modal、Popconfirm、Drawer。Tooltip 补充解释；Toast 提示轻量结果，不能承载错误；Alert 持续呈现重要问题。Modal 用于不可逆确认或复杂信息，Popconfirm 用于低风险局部确认，Drawer 用于需要保留周围上下文的编辑，排除简单表单和全屏任务。产出包括类型依据、打开/关闭、焦点、背景交互、异步恢复和窄屏替代方案；侧面滑出的外观本身不决定是否为模态。

### 7. `component-system`：可复用 UI 组件

[入口](../Chinese/components/component-system/SKILL.md) · `components/component-system` · **1.0.0**

**用途。** 通过清晰的结构、接口、状态归属、尺寸和必要变体，建立一致的共享组件。

**何时使用。** 缺少共享控件、跨页组件不一致、增加变体、接口适配或整合已有组件库。

**工作与产出。** 遵循 **复用 → 配置 → 组合/适配 → 构建已证实的缺口**。检查真实安装版本、调用方、主题/provider、事件、插槽与表单约定，实现当前所需共享元素，检查真实内容、portal、焦点、状态和屏幕尺寸。

**边界。** 页面负责人决定页面组织和业务含义，不把每个一次性区块都抽成公共组件，也不因参考风格不同就引入第二套 UI 库。每个组件由一位负责人整合，浮层沿用共用行为约定。

### 8. `responsive-design`：保持任务可用的响应式适配

[入口](../Chinese/responsive/responsive-design/SKILL.md) · `responsive/responsive-design` · **1.0.3**（含 Playwright 审计脚本 `scripts/audit_ui.mjs`）

**用途。** 当空间、视口高度和输入能力变化时，保留必要信息与操作。

**何时使用。** 内容重排、导航折叠、窄屏图表和表格、触摸/hover 差异、局部溢出、固定区域及响应式组件。

**工作与产出。** 按 **条件 → 保留内容 → 重排方式 → 操作延续** 定义变化，选择合适的流式尺寸、Grid/Flex、视口或容器查询。保留阅读顺序、键盘顺序、筛选、选择、草稿和操作状态，交付局部修改、变化决策及相关断点附近的实际检查。

**边界。** 继承产品视觉系统和组件语义，不为塞进屏幕而删除业务字段，不用全局裁切或缩放掩盖失败，也不把所有窄屏交互变成 Drawer。优先沿用已有断点，否则根据实际内容约束确定变化。

### 9. `design-reference-research`：指定产品案例研究

[入口](../Chinese/design-research/design-reference-research/SKILL.md) · `design-research/design-reference-research` · **1.1.0**（12 张已审案例卡 + 72 项索引）

**用途。** 带着明确证据范围查找、比较并转化产品设计参考。研究方法由本项目编写，使用署名的 [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 元数据，来源版本为 `fcc70284932276d085f01ef9f83edde90b1258cb`。

**何时使用。** 指定品牌参考、带来源的比较、来源核查或尚未解决的具体视觉问题。主题充分的常规局部修复跳过研究。

**工作与产出。** 小索引组织 **84 条来源记录**、**8 张经过文档审阅的案例卡**和四类有条件适用的跨案例模式。通常从 1–3 张卡开始，交付案例与来源、真实页面范围、观察与建议的区分、可迁移关系、所需适配、待验证项和整合负责人。

**边界。** 另外 76 条仅有索引，页面范围仍未知。文档审阅不等于验证当前网站、交互、无障碍或响应式。研究向原负责人提供建议，不接管代码或替换既有变量。元数据保留上游 MIT 声明，应区分原创指导与来源材料。

## 外源包

以下 **14 个包由上游作者编写，不是 PivotUI 原创 Skill**。发布保留原包身份、许可证和固定来源记录。集群为它们选择具体职责，上游描述中的广泛适用范围不会覆盖区域分工；执行前应检查选中入口的实际依赖。

### 10. `design-taste-frontend`：当前公开网站工作流

[入口](../Chinese/page-design/taste-skill/SKILL.md) · 目录 `page-design/taste-skill` · 作者 **Leonxlnx** · [来源](https://github.com/Leonxlnx/taste-skill) · **2.5.1**，`f6b7657` · MIT

**用途与选择。** 面向符合其方法的公司、产品、服务、场所、作品集和公开营销页面，包含改版与审查。`taste-skill` 是同一能力的目录别名。

**工作与产出。** 按业务类型选择页面结构，结合文案、真实照片或产品 UI、字体、布局、动效与浏览器检查。包内包含可执行脚本、参考、系统资源和正式运行素材，交付网站或范围兼容的局部改进及该流程的检查。

**依赖与边界。** 入口要求 **Node 22+** 和 **Chrome、Edge 或 Chromium**，ffmpeg 可选。上游对布局、内容与动效有较强规定，主控会先核对是否兼容用户范围与已有产品。它不担任业务 Dashboard 主负责人。照片、图标等素材在适用时保留各自的来源和许可记录。

### 11. `ui-ux-pro-max`：可检索的设计建议

[入口](../Chinese/design-research/ui-ux-pro-max/SKILL.md) · `design-research/ui-ux-pro-max` · 作者 **nextlevelbuilder** · [来源](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · **2.15.0**，`6ae86f6` · MIT

**用途与选择。** 针对风格、字体、配色、UX、图表或实现技术栈问题补充候选与依据。存在实际未解决的研究缺口时使用，不是所有任务必经步骤。

**工作与产出。** 包内 Python 搜索读取本地数据集，覆盖风格、产品配色、字体、UX、图标、动效预设、图表和技术栈。可针对单一领域检索，也可生成较完整的设计系统建议；采纳或持久化前检查结果是否与问题相符。

**依赖与边界。** 搜索使用 Python 3.x，无额外依赖。本地记录了命令路径的可移植性适配，使脚本从真实安装位置运行，脚本和数据内容保留上游版本。在 PivotUI 中它提供研究与建议，页面实现和已采用变量仍归指定负责人。

### 12. `gpt-taste`：表现力较强的公开营销页面

[入口](../Chinese/visual-styles/gpt-tasteskill/SKILL.md) · `visual-styles/gpt-tasteskill` · 作者 **Leonxlnx** · [classics 来源](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **需要明确选择**

提供指向鲜明的营销工作流，包含变化的 Hero 构图、AIDA 页面推进、素材主导分区和 GSAP 滚动动效。只在明确要求或授权采用这个创意流程时使用，产出约定的营销设计或实现，代码与动效依赖需要实际可用。它在 PivotUI 中**仅服务公开营销，绝不用于 Dashboard 或业务工具**。方法属于上游作品，选用也不意味着可以改动无关主题或声称执行了未运行的脚本。

### 13. `high-end-visual-design`：柔和精致的视觉方向

[入口](../Chinese/visual-styles/soft-skill/SKILL.md) · `visual-styles/soft-skill` · 作者 **Leonxlnx** · [classics 来源](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **需要明确选择**

提供柔和对比、大留白、特色字体、触感层次和弹性动效的艺术指导方法，包含玻璃、编辑式奢华、柔和结构等方向及相应移动端变化。方向适合时按名称选择，再核对字体、依赖、可访问性和目标产品是否兼容。可指导或实现约定视觉区域，不会成为 PivotUI 全局默认主题，也不会静默替换已有设计变量。

### 14. `minimalist-ui`：编辑式产品极简方向

[入口](../Chinese/visual-styles/minimalist-skill/SKILL.md) · `visual-styles/minimalist-skill` · 作者 **Leonxlnx** · [classics 来源](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **需要明确选择**

通过暖色单色表面、排版主导的层级、平面结构化网格和少量柔和强调色形成克制的编辑式产品语言，包含具体视觉与实现规则。当需求适合这种表达时明确选择，结果是范围内的方向或实现，并整合到已约定的产品设计来源。它的字体、图标、形状和配色偏好属于上游工作流，不能直接升级为整套集群的通用规则，采用前需检查兼容性。

### 15. `industrial-brutalist-ui`：工业与机械视觉语言

[入口](../Chinese/visual-styles/brutalist-skill/SKILL.md) · `visual-styles/brutalist-skill` · 作者 **Leonxlnx** · [classics 来源](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **需要明确选择**

提供严格模块网格、瑞士风格排版、强烈尺度对比、功能性颜色和可选的模拟显示器处理。主要方向为浅色工业印刷与深色遥测/终端，按项目选择其一，不随意混合。明确需要此类表达的产品或区域可按名称调用。业务结构和可读性仍归页面负责人，不能因为选择该风格就虚构数据、隐藏关键操作或越权改变全局主题。

### 16. `imagegen-frontend-web`：网站分区概念图

[入口](../Chinese/image-design/imagegen-frontend-web/SKILL.md) · `image-design/imagegen-frontend-web` · 作者 **Leonxlnx** · [imagegen 来源](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT

为落地页、营销页和产品页生成分区设计参考。上游流程采用**每个分区一张独立横向图片**，保持配色一致，同时变化不同分区的构图。请求网站概念图时选择，遵循用户要求的数量和格式，需要实际图像生成能力。输出是视觉参考，不是可运行前端；后续代码需要单独明确，静态图之外的交互与响应式也需要实现和检查。

### 17. `imagegen-frontend-mobile`：移动应用屏幕与流程图

[入口](../Chinese/image-design/imagegen-frontend-mobile/SKILL.md) · `image-design/imagegen-frontend-mobile` · 作者 **Leonxlnx** · [imagegen 来源](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT

生成引导、登录、首页、电商、个人页、设置等移动应用屏幕概念和连贯的多屏流程，强调清晰层级、平台特征、统一颜色和一致呈现。默认使用轻量手机外框，也应根据用户要求调整。适用于移动端**图像**交付，需要图像生成工具；不生成应用代码、桌面网站或响应式前端行为。

### 18. `brandkit`：品牌视觉板与概念

[入口](../Chinese/image-design/brandkit/SKILL.md) · `image-design/brandkit` · 作者 **Leonxlnx** · [imagegen 来源](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT

用图片生成品牌规范板、Logo 系统概念、视觉世界展示和品牌应用，通过简洁排版、符号、统一面板、图像和样机表达一个连贯品牌想法。用于品牌探索或展示，需要图像工具。视觉板属于候选和图像成果，不自动等于获批 Logo、字体文件、矢量母版或产品权威设计变量。用户要求落地时，可由全局风格将采用的方向转成产品设计值。

### 19. `image-to-code`：生成设计图、分析、实现

[入口](../Chinese/image-design/image-to-code/SKILL.md) · `image-design/image-to-code` · 作者 **Leonxlnx** · [imagegen 来源](https://github.com/Leonxlnx/imagegen-skills) · `beb16b0` · MIT

按顺序先生成新设计图，分析构图和视觉关系，再实现网站，倾向于可读的分区参考，而非拥挤的整站合成图。需要同时进行概念创作和前端实现，且图像与代码能力均可用时选择。它不是精确还原已有图片的默认路径：那种任务保留原图为目标，由具备读图能力的实现者负责。生成图并不证明交互或跨屏行为可用，仍需要实现与验证。

### 20. `stitch-design-taste`：面向 Stitch 的设计约定

[入口](../Chinese/tool-integrations/stitch-skill/SKILL.md) · `tool-integrations/stitch-skill` · 作者 **Leonxlnx** · [classics 来源](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **需要明确选择**

编写面向 Google Stitch 的 `DESIGN.md`，用描述性语言和具体值表达氛围、配色、字体、组件行为、布局、响应式与动效。明确请求 Stitch 工作流时选择，其入口声明需要 Stitch 访问，Stitch MCP 可选。生成设计文档、在 Stitch 中生成屏幕、交付前端代码属于不同阶段，需要对应的实际工具和任务范围。文档应关联已采用的产品设计来源，避免出现竞争的设计值。

### 21. `design-taste-frontend-v1`：保留原版 taste 行为

[入口](../Chinese/legacy/taste-skill-v1/SKILL.md) · `legacy/taste-skill-v1` · 作者 **Leonxlnx** · [classics 来源](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **明确指定历史版本**

保留原版通过设计变化程度、动效强度和信息密度等参数驱动的 taste 工作流，并包含 React/Next.js、Tailwind、组件与依赖约定。项目明确依赖该版本行为，需要复现或维护时按名称使用，先检查真实技术栈和安装包。它的历史默认值不会覆盖当前 taste 包或 PivotUI 的业务页面方法，也不会因为当前 Skill 缺失就被静默启用。

### 22. `design-taste-frontend-v2-experimental`：保留实验工作流

[入口](../Chinese/legacy/taste-skill-v2-experimental/SKILL.md) · `legacy/taste-skill-v2-experimental` · 作者 **Leonxlnx** · [classics 来源](https://github.com/Leonxlnx/taste-skill-classics) · `5e08c93` · MIT · **明确指定历史版本**

保留单文件实验工作流，先读取页面类型、受众、参考、已有素材和约束，再使用设计参数。适用落地页、作品集和改版，其自身范围排除 Dashboard、数据表格与多步骤产品 UI。只在刻意的历史版本需求下使用，产出遵循所选版本，依赖根据目标项目检查。它是独立保留的能力，不是当前 taste 的别名或自动备用方案。

### 23. `redesign-existing-projects`：历史版局部改进流程

[入口](../Chinese/legacy/redesign-skill/SKILL.md) · `legacy/redesign-skill` · 作者 **Leonxlnx** · [历史来源](https://github.com/Leonxlnx/taste-skill/tree/e04409a461022e1b9d0e898eac6b9224e2b9dc4e/skills/redesign-skill) · `e04409a` · MIT · **在 PivotUI 中需要明确指定历史版本**

保留 **扫描 → 诊断 → 修复** 流程，在现有技术栈内改进网站或应用，检查排版、颜色/表面、布局等问题，给出或实施有针对性的修改。仅在明确需要这一固定历史行为时选择。当前上游已将改版能力并入现行 taste，PivotUI 为有意的兼容需求保留此包，不因需求中出现“改版”就自动启用。业务区域仍沿用合适的页面负责人和共用设计来源。

## 相似能力如何区分？

| 容易混淆的选择 | 区分依据 |
| --- | --- |
| 全局风格与某个 classics 风格 | 全局风格管理产品方向和变量；classic 是明确选定的上游视觉工作流。 |
| Dashboard 与数据列表 | 支撑概览的摘要由 Dashboard 负责；完整记录查找和操作流程由数据列表负责。 |
| 应用框架与导航交互 | 框架负责层级、外围布局和路由上下文；导航交互负责输入、当前位置和焦点行为。 |
| 组件系统与交互 | 组件负责共享实现和接口；交互为具体缺口提供状态与恢复约定。 |
| UI/UX 研究与产品案例研究 | 前者检索通用候选与指南；后者检查指定来源和案例证据。 |
| 网站图像与 image-to-code | 仅图像流程交付概念；image-to-code 创作新概念并继续实现代码。 |
| 当前 taste 与历史包 | 一般选择适配当前任务的现行流程；需要特定历史行为时刻意指定版本。 |

全部模块围绕请求的交付物工作。被收录在目录中，不意味着每次都要读完全部正文、执行全部流程，或重做已经确定的决策。
