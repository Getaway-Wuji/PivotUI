<p align="center">
  <img src="assets/pivotui-brand-loop1.gif" alt="PivotUI 品牌动图：A Skill Cluster for UI" width="1200">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/Getaway-Wuji/PivotUI/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs welcome"></a>
</p>

# PivotUI

**你描述要做的界面，Skill 集群负责选择和协作。**

简体中文 · [English](README.en.md) · [安装配置](docs/INSTALL.zh-CN.md) · [全部 Skill 详解](docs/SKILLS.zh-CN.md) · [架构与任务分配](docs/ARCHITECTURE.zh-CN.md)

PivotUI 是一套面向 UI 设计与实现的 **Skill 集群**，把任务分配、全局风格、页面设计、组件、交互、响应式、设计研究和外源工作流组织成可协作的系统。它的核心想法是：**用户只需要说明要完成什么，不必每次翻找 Skill、判断该选哪一个，再逐一交代它们如何配合。**

管理层先理解你要的结果，为每个区域确定主负责人，再根据具体缺口引入辅助 Skill，并把结果整合到同一个产品中。从业务结构到可运行界面，各模块共享已有主题、组件和设计决策，减少重复选择与来回协调。

当前版本 **0.4.0** 包含 **23 个包：9 个内源模块、14 个外源包**；计入交互模块的 4 个子入口，共有 **27 个标准 `SKILL.md` 入口**。中文与英文版均可独立使用；外源包在两版中保留上游原语言和声明。

## 什么是 Skill 集群？

一个 Skill 是针对某类工作的可复用方法与指令，通常配有参考资料、脚本、模板或数据。Skill 集群在多个独立 Skill 之间建立明确的协作机制：

- **统一入口理解任务**：识别用户要建议、设计图、设计变量、局部修改，还是完整代码。
- **独立模块承担职责**：每个模块有自己的适用场景、输入、输出和工作边界。
- **共用约定保持一致**：主题、组件和任务归属能够在模块之间延续。
- **按需读取必要内容**：先看能力目录，再读取选中的入口和相关资料。

在 PivotUI 中，真正理解任务、应用规则并完成工作的，是你所使用的宿主工具中的 AI。`design-orchestrator` 提供管理规则，可选的本地 MCP 服务提供能力目录和文件读取。MCP 本身不运行模型，也不执行 Markdown 指令；不使用 MCP 时，也可以通过直接读取文件使用整套集群。

## 它如何提高效率？

| 原本需要反复处理的事情 | PivotUI 的组织方式 |
| --- | --- |
| 每次从 Skill 列表中找合适的工具 | 统一入口根据交付物、页面用途、局部范围和实际工具条件选择能力。 |
| 猜测还需要搭配哪些 Skill | 仅在组件、交互、响应式、研究或主题存在具体缺口时补充专家模块。 |
| 向多个模块重复交代背景 | 用简短任务约定传递区域、负责人、参考、设计变量、组件和验收范围。 |
| 合并互相冲突的颜色、字体和组件 | 产品中保留一份权威设计变量，每个区域由一位主负责人整合。 |
| 为简单任务读取整套资料 | 先发现元数据，再读取选定入口与相关资源；已有规则直接复用。 |
| 已经决定方向后再次调研 | 保留适用的既有主题与决策，只在任务要求或确有缺口时重新研究。 |

这些是具体的流程改进机制，并非经过量化实验的提效百分比。实际收益取决于任务复杂度、宿主工具能力和项目已有基础。

## 可以用来做什么？

| 你的需求 | 管理层如何分配 |
| --- | --- |
| “沿用我们的主题，做一个运营 Dashboard。” | `dashboard-design` 主导指标、图表和概览内容，复用现有框架与主题，按缺口补充支持。 |
| “做订单列表，带筛选、批量操作，并能从详情回到原位置。” | `data-list-design` 负责完整列表流程和操作范围，按需加入共享控件、异步交互与窄屏适配。 |
| “统一后台各页面的导航、标题和滚动。” | `app-shell-design` 负责应用框架与路由约定，各页面模块继续负责业务内容。 |
| “修复保存失败后丢失输入的表单。” | `form-interaction` 与相关异步规则处理局部问题，继承周围的布局和主题。 |
| “先比较几种设计方向，再决定做哪种。” | `global-style-skill` 提供候选与建议；需要具体产品证据时引入 `design-reference-research`，仅咨询时只交付建议。 |
| “制作一个公开产品官网。” | 可由适配当前要求的 `design-taste-frontend` 主导，先核对其工作流与项目要求、工具条件是否兼容。 |
| “生成移动端界面概念图”或“制作品牌视觉板。” | 选择对应的图像设计 Skill，通过实际可用的图像工具生成结果。 |
| “只修复手机上表格溢出。” | `responsive-design` 处理具体内容与操作约束。 |

混合项目、原图还原、可选风格和任务交接的详细示例见[架构与任务分配](docs/ARCHITECTURE.zh-CN.md)。

## 集群结构

```text
English/ 或 Chinese/
├── orchestration/       任务分配与全局视觉决策
├── page-design/         Dashboard、数据列表、应用框架、公开网站
├── interaction/         共用交互规则与四个专项子模块
├── components/          可复用组件实现
├── responsive/          布局、输入方式与溢出适配
├── design-research/     UI/UX 建议与产品案例研究
├── visual-styles/       需明确选择的外源风格工作流
├── image-design/        网站图、移动端图、品牌板、先图后代码
├── tool-integrations/   面向 Stitch 的设计工作流
├── legacy/              明确指定时使用的历史工作流
├── design-system/       共用方法与职责约定
└── mcp/skill-cluster/    可选的本地能力目录与文件读取服务
```

内源与外源包按功能放在同一分类下，来源在文档中明确标注。目录名与 Skill 的 YAML 名称有时不同，例如 `taste-skill` 是 `design-taste-frontend` 的包目录，二者属于同一个能力。

[全部 Skill 详解](docs/SKILLS.zh-CN.md)逐项介绍**全部内源和外源包**的用途、触发条件、产出、依赖和边界；每个语言版本内还附有独立清单与来源记录。

## 快速开始

支持 **Codex、Claude Code、DSH（DeepSeek Harness）、Cursor 和其他兼容 Agent**。选择下面任意一种安装方式即可：两种方式都会提供一个原生 **pivotui** 入口，按任务读取完整集群中的 **27 个模块入口**。

### 方式一：一条 npx 命令安装

准备好 **Node.js 22+、npm/npx 和 Git**，在目标项目根目录打开终端，执行：

```sh
npx --yes github:Getaway-Wuji/PivotUI --agent codex --language zh
```

npx 会自动获取并运行安装器，无需自己克隆仓库，也无需运行 Python。其他 Agent 使用对应命令：

```sh
# Claude Code
npx --yes github:Getaway-Wuji/PivotUI --agent claude-code --language zh
# DSH / DeepSeek Harness
npx --yes github:Getaway-Wuji/PivotUI --agent dsh --language zh
# Cursor
npx --yes github:Getaway-Wuji/PivotUI --agent cursor --language zh
```

英文版使用 `--language en`。默认安装到当前项目：完整集群放在 `.pivotui/libraries/`，原生入口放在 `.agents/skills/pivotui/`，Claude Code 则使用 `.claude/skills/pivotui/`。加上 `--global` 可安装到用户范围。[其他 Agent、自定义目录和预览](docs/INSTALL.zh-CN.md#command-install)。

### 方式二：下载 ZIP，自行放入项目

下载一套**项目安装 ZIP**：[中文版](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-Chinese-project-v0.4.0.zip) · [English](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-English-project-v0.4.0.zip)。

1. 解压后打开外层 `PivotUI-Chinese/` 或 `PivotUI-English/` 文件夹。文件管理器隐藏点开头的目录时，先启用隐藏文件显示。
2. 把其中 `.pivotui/` 的内容复制到目标项目根目录下的同名位置，保留完整集群。
3. **Codex、DSH、Cursor**：把 `.agents/skills/pivotui/` 复制到项目的 `.agents/skills/pivotui/`。**Claude Code**：将同一个 `pivotui/` 文件夹改放到 `.claude/skills/pivotui/`，保持目录深度一致。

只合并 PivotUI 的文件夹，保留项目里其他 Skill 和设置。复制完整 `pivotui/` 文件夹，包括隐藏清单；不要为同一宿主同时放置两种入口。这种方式不需要运行安装命令。ZIP 内附 `INSTALL.md`，也可查看[项目手动安装步骤](docs/INSTALL.zh-CN.md#zip-install)。

安装后打开新的 Agent 会话，选择 **pivotui**，直接描述要完成的界面。两种方式都不需要配置 MCP 或手动粘贴安装提示词。

原来的完整语言版压缩包也保留，供原始文件或 MCP 接入使用：[中文版 ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-Chinese-v0.4.0.zip) · [English ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-English-v0.4.0.zip)。详见[安装指南](docs/INSTALL.zh-CN.md)和[验证记录](docs/VALIDATION.md)。

## 自动选择的范围与工具条件

管理层在集群声明的边界内完成常规自动选择。上游七个 classics 保留“明确调用”规则，历史版本也需要刻意选择；主控可以推荐这些能力，但不会因为已经安装就静默启用。`gpt-taste` 仅用于公开营销页面，不分配给 Dashboard 或业务工具。

使用集群需要一个能读取指令并执行相应任务的宿主。图像流程需要图像生成工具，Stitch 流程需要对应服务，公开网站的检查流程可能需要 Node 和浏览器。本地 MCP 提供文件，不替代这些执行能力。两套语言版本使用相同标识，每次连接其中一套即可。

## 作者、外源内容与许可证

PivotUI 的集群组织、管理约定及九个内源模块由本项目维护。项目原创内容采用 [MIT 协议](LICENSE)，版权归 © 2026 Getaway-Wuji。**14 个外源包来自各自的上游作者，不是 PivotUI 作者原创。** 发布内容保留它们的原始身份、固定版本、版权声明与许可证文件。

| 上游项目 | 本集群使用的内容 |
| --- | --- |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 当前公开网站 Skill，以及固定历史版本的改版 Skill |
| [Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) | 四种视觉方向、Stitch 集成、两个历史 taste 版本 |
| [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) | 四个图像设计与先图后代码包 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 可检索的 UI/UX 指南、脚本与数据集 |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 内源产品案例研究模块使用的来源元数据 |

具体适用范围与本地适配记录见 [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md)，以及各包内的 `LICENSE` 和 `UPSTREAM.md`。上游 MIT 协议只覆盖其声明的材料；照片、图标、字体等素材可能另有条款。README 中的署名不能替代随包保留的法律声明。

## 发布内容

本仓库发布可用集群及使用文档，排除本地演示、生成的测试结果、私人启动配置、虚拟环境、缓存、原始调研和中间参考图片。外源工作流实际需要的运行素材及其来源说明随所属包保留。

元数据、资源链接、双语对应和压缩包一致性可单独检查；文件已收录并不代表每个图像服务、浏览器流程或宿主都已执行验证。研究库包含 84 条来源记录与 8 张经过文档审阅的案例卡，各卡明确证据范围；全局风格提供 40 张参考卡，仅在需要探索方向时加载。
