# 安装和使用 PivotUI

[English](INSTALL.en.md) · [项目介绍](../README.md) · [Skill 详细说明](SKILLS.zh-CN.md)

安装一套完整语言版本和原生 **pivotui** Skill 入口，可选[一条 npx 命令安装](#command-install)或[下载 ZIP 后自行复制](#zip-install)。两种方式都从 `design-orchestrator` 开始，按任务读取需要的模块。

[可选的原始文件/MCP 接入](#manual-setup) · [旧版 Python 安装器](#legacy-python) · MCP：[Codex](#codex) / [Claude Code](#claude-code) / [DSH](#deepseek-harness) / [其他 Agent](#other-agents)。

<a id="command-install"></a>

## 方式一：一条 npx 命令安装

需要 **Node.js 22+ 和 npm/npx**。请在 Agent 实际运行的环境里，打开**目标项目根目录**并执行：

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language zh
```

npx 会下载已经打包好的发布包，再运行里面的安装器。这条命令不需要 Git、Python 或 MCP 配置。安装好 Node.js 和 npm/npx 后，Windows、macOS 和 Linux 终端都使用同一条命令。

首次运行需要下载完整安装包，可能等待较久。请以 **`Installed PivotUI ...`** 提示作为安装完成的标志；转圈停止或终端回到输入提示符，本身不代表成功。若报错，请保留报错内容，查看[常见问题](#npx-troubleshooting)。

选择你使用的 Agent：

```sh
# Claude Code
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent claude-code --language zh
# DSH / DeepSeek Harness
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent dsh --language zh
# Cursor
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent cursor --language zh
# 其他支持本地 SKILL.md 包的宿主
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent generic --language zh --skills-dir "<your-agent-skills-directory>"
```

英文版使用 `--language en`。该参数选择内源指令的语言，外源包仍保留上游原语言。选择 `generic` 时，需要提供宿主实际的 skills 目录，安装器会在其中创建 `pivotui/` 子目录。

### 项目范围与用户范围

默认安装到当前项目：

| Agent | 项目中的原生入口 |
| --- | --- |
| Codex / DSH / Cursor | `.agents/skills/pivotui/SKILL.md` |
| Claude Code | `.claude/skills/pivotui/SKILL.md` |
| Generic | `<your-agent-skills-directory>/pivotui/SKILL.md` |

完整集群保存在 `.pivotui/libraries/`。请从项目根目录执行，也可以显式指定项目：

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language zh --project "<target-project-directory>"
```

若希望安装到用户范围，在多个项目之间共用，改为加上 `--global`：

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language zh --global
```

用户范围的集群保存在 `~/.pivotui/libraries/`。Codex 和 Cursor 使用 `~/.agents/skills/pivotui/`；DSH 使用同一共享目录，并支持 `DSH_AGENTS_HOME`。Claude Code 使用 `~/.claude/skills/pivotui/`，并支持 `CLAUDE_CONFIG_DIR`。部分宿主还会读取其他工具的兼容目录，请让同一宿主只看到一个所选语言版本的入口。

官方发现机制：[Codex Skills](https://developers.openai.com/codex/skills)、[Claude Code Skills](https://code.claude.com/docs/en/skills)及[配置目录](https://code.claude.com/docs/en/claude-directory.md)、[DSH Skills](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md)、[Cursor Skills](https://cursor.com/docs/skills)。[npm 包规格](https://docs.npmjs.com/cli/v11/using-npm/package-spec)和 [npx 参考](https://docs.npmjs.com/cli/v11/commands/npx)说明了安装包地址及命令执行方式。

### 预览与自定义目录

只预览目标位置并验证源文件，不向项目安装文件：

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language zh --dry-run
```

npx 仍可能将执行包下载到 npm 缓存。需要时可以指定集群存储位置和入口目录：

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language zh --install-dir "<library-storage-directory>" --skills-dir "<your-agent-skills-directory>"
```

将占位符替换为实际路径，含空格的路径保留引号。完整集群需要保持可被 Agent 访问。本机安装不会自动出现在远程机器或云端会话中。

安装器保留其他 Skill、项目指令和 MCP 配置，校验复制后的完整版本，并拒绝覆盖无关或手动修改过的入口。支持重复安装；切换 `--language` 时更新所选入口，并保留此前的集群副本。

<a id="zip-install"></a>

## 方式二：下载 ZIP，复制两个文件夹

如果你用的是 **Codex、DSH 或 Cursor**，安装就是把 **`.agents` 和 `.pivotui` 两个文件夹一起复制到你的项目里**，不用运行命令。

### 按这几步复制

下载一份 ZIP：

- [PivotUI 中文项目安装 ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-Chinese-project-v0.4.0-r2.zip)
- [PivotUI English 项目安装 ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-English-project-v0.4.0-r2.zip)

1. 解压 ZIP，打开解压出来的 `PivotUI-Chinese` 或 `PivotUI-English` 文件夹。里面能看到 `.agents`、`.pivotui` 和 `INSTALL.md`。
2. 同时选中 **`.agents` 和 `.pivotui` 两个文件夹**，复制，再粘贴到你的项目文件夹里。整个文件夹一起复制，不用点进去挑文件。
3. 在 Agent 中打开这个项目，新建一个对话，选择 **pivotui**。

复制完成后，你的项目里应该是这样：

```text
你的项目/
├── .agents/
└── .pivotui/
```

**“项目文件夹”是哪一个？** 就是你在 Agent 中打开的项目最外层文件夹。如果项目里已经有 `src` 或 `package.json`，把这两个文件夹放在它们旁边；刚建好的空项目文件夹也可以。复制的是两个文件夹本身，不是外面的整个 `PivotUI-Chinese` 或 `PivotUI-English` 文件夹。

这样就完成了文件安装。**复制到哪个项目，哪个项目就装好了。** 以后移动项目时，把这两个文件夹一起带走即可。`INSTALL.md` 不用复制，压缩包里的文件也不用双击运行。

如果解压后看不到 `.agents` 和 `.pivotui`，打开文件管理器的“显示隐藏文件”。项目里已有同名文件夹时，合并内容，保留其他文件。若提示覆盖同名文件，先检查自己是否修改过原有的 PivotUI 文件，再决定是否替换；不要替换项目整个设置文件夹。

### 如果你用 Claude Code

1. 在**解压出来的文件夹里**，把 `.agents` 改名为 `.claude`。
2. 将 **`.claude` 和 `.pivotui` 两个文件夹一起**复制到你的项目文件夹里。
3. 在 Claude Code 中打开这个项目，新建一个对话，选择 **pivotui**。

只给解压出来的文件夹改名，不要改项目里原有的 `.agents`。如果项目里已经有 `.claude`，把下载的内容合并进去：PivotUI 的文件放在 `.claude/skills/pivotui/`，保留旁边其他 Skill 和设置。Claude Code 不需要再往 `.agents` 里复制一份 PivotUI。

其他 Agent 如果要求不同的文件夹位置，可以使用[自定义目录安装](#command-install)，由安装器设置对应的文件路径。

### 开始使用

两种安装方式都提供**一个原生 pivotui 入口**，按需读取完整集群中的 **27 个模块入口**。选中它并描述你要完成的界面即可，无须往项目规则中粘贴安装提示词。安装和文件校验与宿主完整工作流执行是不同检查，见[实际验证记录](VALIDATION.md)。

<a id="manual-setup"></a>

## 可选：手动文件与 MCP 接入

以上任意一种安装方式都足够使用原生 Skill。以下章节适用于需要 MCP 或原始文件读取的宿主，是替代方式，不是额外安装要求。

### 获取一套版本

原来的完整语言版压缩包继续保留：[中文版 ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-Chinese-v0.4.0.zip)、[English ZIP](https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/PivotUI-English-v0.4.0.zip)。其中包含原始语言目录、本地 MCP 服务和必要包资源；与上方项目安装 ZIP 的区别是，它们不包含项目级原生入口。已有仓库副本时，也可以使用其中的 `Chinese/` 或 `English/` 目录。

- 选择 `Chinese/`，使用中文编写的内源指令；选择 `English/`，使用英文编写的内源指令。
- 外源包在两个版本中均保留上游原始语言。
- 保持目录结构，并将 `SKILL.md`、参考资料、脚本、数据集和许可声明一起保留。
- 只注册选定的一套版本。两套版本使用相同 Skill 名称，同时注册会产生重名歧义。

本文的 **`<edition-root>` 表示直接包含 `orchestration/`、`page-design/`、`design-system/` 和 `mcp/` 的目录的绝对路径**。它不是仓库根目录、ZIP 文件或 `mcp/` 目录。执行命令前，将所有尖括号占位符替换成实际路径。解压后的外层文件夹可以重命名。

### 选择手动接入方式

| 方式 | 需要什么 | 适用情况 |
| --- | --- | --- |
| 本地 MCP | 支持本地 stdio MCP 的助手；Python 3.11 或更高版本 | 通过三个固定工具先发现元数据，再按需读取选定指令和资源 |
| 直接读取文件 | 能访问选定版本和目标项目文件的助手 | 没有 MCP 时，直接读取实际文件中的同一套指令 |

两种方式使用相同的 Skill 和路由规则。MCP 提供受约束的文件读取能力，由连接它的助手应用指令并完成任务。MCP 本身不会执行 Markdown、启动其他智能体或调用模型 API。

## 配置本地 MCP（可选）

### 安装服务依赖

在 `<edition-root>/mcp/skill-cluster` 中打开终端。服务的 `requirements.txt` 固定了 `mcp==2.3.0` 和 `PyYAML==6.0.3`。

Windows PowerShell：

```powershell
Set-Location "<edition-root>/mcp/skill-cluster"
python -m venv .venv
& ./.venv/Scripts/python.exe -m pip install -r requirements.txt
& ./.venv/Scripts/python.exe -X utf8 server.py --help
```

macOS/Linux：

```sh
cd "<edition-root>/mcp/skill-cluster"
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -X utf8 server.py --help
```

在助手连接设置中，使用此虚拟环境的 Python 可执行文件。即使安装已成功，使用另一个 Python 也可能导致缺少模块的错误。

### 注册连接

在宿主应用设置中添加一个**本地 stdio MCP 服务**，填写以下内容：

| 设置项 | 内容 |
| --- | --- |
| 连接名称 | `pivotui` |
| Windows 启动程序 | `<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe` |
| macOS/Linux 启动程序 | `<edition-root>/mcp/skill-cluster/.venv/bin/python` |
| 参数，依次填写 | `-X`、`utf8`、`<edition-root>/mcp/skill-cluster/server.py` |
| 传输方式 | `stdio` |

如果宿主支持常见的 `mcpServers` JSON 格式，可参考以下 Windows 示例：

```json
{
  "mcpServers": {
    "pivotui": {
      "command": "<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe",
      "args": [
        "-X",
        "utf8",
        "<edition-root>/mcp/skill-cluster/server.py"
      ]
    }
  }
}
```

macOS/Linux 将 `command` 改成 `<edition-root>/mcp/skill-cluster/.venv/bin/python`。Windows JSON 路径使用正斜杠比较方便；如果使用反斜杠，需要写成 `\\`。不同宿主的设置格式可能不同，请按它支持的格式填写同一个启动程序和独立参数。将该条目合并到已有配置，保留其他服务连接。

版本内的服务根据自身位置发现对应版本，工作目录不会决定语言。它在协议中报告的服务名称是 `design-skill-cluster`，可以与设置中的连接名称 `pivotui` 不同。

通常不需要指定根目录。如需明确指定，在 `args` 后追加 `--skill-root` 及根目录绝对路径。只有确实需要额外暴露其他兼容库时，才重复追加这一对参数。一旦指定根目录，默认目录会被替换，而不会自动追加。不要再注册一份与已收录包同名的副本。

### 选择你的 Agent

安装上方依赖后，选择以下**一种**注册方式。所有示例都使用同一个语言版本内的服务。终端命令为包含空格的路径加了引号；执行前请替换每一处 `<edition-root>`。

<a id="codex"></a>

#### Codex

已安装 Codex CLI 时，运行以下命令注册服务：

```sh
# Windows：PowerShell 或其他能够找到 codex 命令的终端
codex mcp add pivotui -- "<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe" -X utf8 "<edition-root>/mcp/skill-cluster/server.py"

# macOS / Linux
codex mcp add pivotui -- "<edition-root>/mcp/skill-cluster/.venv/bin/python" -X utf8 "<edition-root>/mcp/skill-cluster/server.py"
```

也可以将以下配置段合并到 `~/.codex/config.toml`，或已信任项目中的 `.codex/config.toml`。没有 CLI、直接配置桌面应用时，可以使用这种方式：

```toml
[mcp_servers.pivotui]
command = "<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe"
args = ["-X", "utf8", "<edition-root>/mcp/skill-cluster/server.py"]
```

macOS/Linux 使用 `<edition-root>/mcp/skill-cluster/.venv/bin/python`。运行 `codex mcp list` 查看注册情况，随后刷新客户端并完成下方工具检查。将[入口约定](#entry-rule)追加到目标项目的 `AGENTS.md`，保留原有指令。参考官方 [MCP 指南](https://developers.openai.com/codex/mcp)和 [AGENTS.md 指南](https://developers.openai.com/codex/guides/agents-md)。

<a id="claude-code"></a>

#### Claude Code

在用户范围注册本地服务，使其可用于你的不同项目：

```sh
# Windows
claude mcp add --transport stdio --scope user pivotui -- "<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe" -X utf8 "<edition-root>/mcp/skill-cluster/server.py"

# macOS / Linux
claude mcp add --transport stdio --scope user pivotui -- "<edition-root>/mcp/skill-cluster/.venv/bin/python" -X utf8 "<edition-root>/mcp/skill-cluster/server.py"
```

运行 `claude mcp list`，随后在 Claude Code 中使用 `/mcp` 查看连接状态，并完成下方工具检查。将[入口约定](#entry-rule)追加到目标项目的 `CLAUDE.md`。参考官方 [MCP 指南](https://code.claude.com/docs/en/mcp)和[项目记忆指南](https://code.claude.com/docs/en/memory)。

<a id="deepseek-harness"></a>

#### DSH / DeepSeek Harness

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 使用官方 `@deepseek-ai/dsh-mcp-client` 插件接入。它使用 Cordis YAML 补丁，不使用 `mcpServers` JSON 格式。替换路径后，将以下内容保存为 `pivotui.cordis.yml`：

```yaml
- insert:
    - id: mcp-pivotui
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: pivotui
        transport: stdio
        command: '<edition-root>/mcp/skill-cluster/.venv/Scripts/python.exe'
        args:
          - '-X'
          - 'utf8'
          - '<edition-root>/mcp/skill-cluster/server.py'
```

macOS/Linux 将 `command` 中的 Python 路径改为 `<edition-root>/mcp/skill-cluster/.venv/bin/python`。使用该补丁启动 web 配置：

```sh
dsh web --patch "<absolute-path-to-pivotui.cordis.yml>"
```

需要长期生效时，将这条 `insert` 操作合并到 web 配置的 `$DSH_HOME/profiles/web/cordis.patch.yml`，保留已有操作。同一服务选择长期配置或 `--patch` 其中一种方式，避免重复添加。默认主目录为 `~/.dsh`。将[入口约定](#entry-rule)追加到目标项目的 `AGENTS.md`，并将该项目作为 DSH 工作区。插件会提供 `mcp__pivotui__catalog_skills` 等工具。

DSH 目前处于开发者预览阶段；以上步骤依据其已公开的插件接口。参考官方 [MCP 配置指南](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/mcp-memory.md)、[插件参考](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/mcp/mcp-client/README.md)和 [CLI 参考](https://github.com/deepseek-ai/deepseek-harness/blob/master/apps/cli/reference/README.md)。

<a id="other-agents"></a>

#### Cursor 和其他 Agent 工具

使用 **Cursor** 时，将上方 `mcpServers` JSON 示例合并到目标项目的 `.cursor/mcp.json`，或用户级 `~/.cursor/mcp.json`。刷新 MCP 连接后完成下方检查。参考 [Cursor 官方 MCP 指南](https://cursor.com/docs/mcp)。

其他支持**本地 stdio MCP** 的宿主，按其支持的格式填写同一个 Python 启动程序和参数列表。仅接受远程 HTTP 服务的宿主无法直接启动这个本地 stdio 服务。如果 Agent 能读取本地文件，可以使用[直接读取文件](#direct-files)方式。将入口约定保存到该宿主的项目指令中，或在每次任务开始时粘贴。

这些是依据文档提供的配置方式。[验证记录](VALIDATION.md)说明了实际完成的检查，不代表每种宿主都已经过端到端测试。

### 验证连接

重新连接或刷新宿主中的 MCP 服务，确认以下工具可用：

| 工具 | 示例参数 | 预期结果 |
| --- | --- | --- |
| `catalog_skills` | `{}` | 完整 0.4.0 版本的 **27 个入口**元数据，不返回指令正文 |
| `load_skill` | `{"skill_id":"design-orchestrator"}` | 选定的管理入口正文及其链接资源名称 |
| `read_skill_file` | `{"skill_id":"design-orchestrator","path":"references/scenarios.md","offset":0,"limit":1200}` | 该场景参考文件中指定范围的文字 |

27 个入口来自 23 个顶层包和 4 个嵌套交互 Skill。宿主可能给工具名称加上连接前缀。保存配置不等于连接成功；能够获取目录并读取选定文件，才说明这条连接可用。

如果直接运行 `server.py` 且不加 `--help`，它会通过标准输入等待 MCP 请求，不会打开网页或显示图形菜单。正常使用时，由宿主启动和停止这个进程。

<a id="direct-files"></a>

## 手动直接读取文件（可选）

将选定版本放在助手能够访问的稳定位置。如果宿主支持原生 Skill 注册，按其机制注册实际包路径。不同宿主扫描的目录层级不同，不能默认认为将扫描器指向 `English/` 或 `Chinese/` 就能发现所有功能分类和嵌套入口。

如果不支持分类目录扫描，直接提供管理入口的准确路径：

```text
<edition-root>/orchestration/design-orchestrator/SKILL.md
```

助手可以通过版本内的 `README.md` 定位选中的包，只读取需要的入口和资源。必须手动注册时，注册实际包目录；嵌套交互入口应与父包放在一起。只复制 `SKILL.md` 会丢失资源，并可能破坏相对链接。尽量保持整套版本完整。

<a id="entry-rule"></a>

## 手动接入的入口约定

手动文件或 MCP 接入时，将下面的指令加入目标项目的助手工作规则，或在任务开始时发送一次。使用已安装的原生 **pivotui** Skill 时，跳过这一步。直接读文件时，替换其中的路径：

```text
本项目的界面工作使用 PivotUI，从 design-orchestrator 开始。
使用 MCP 时，先发现目录元数据，读取管理入口，再只加载选定的 Skill 和必要资源。
没有 MCP 时，读取 <edition-root>/orchestration/design-orchestrator/SKILL.md
以及选定文件。只使用这一套语言版本。每个区域指定一个主责，继承产品现有主题和组件，
保持一个权威 Token 来源。遵守外源 Skill 的调用限制。完成用户要求的实际交付物，
并包含相关交互、响应式行为和验证。
```

手动接入时，这条常驻指令会让任务进入管理层。安装器创建的原生 **pivotui** 入口已经包含这种分配规则，选择已安装的 Skill 即可，无须另加这段指令。

## 用自然语言提交任务

配置后，可以直接描述希望得到的结果，例如：

```text
沿用现有品牌和组件，做一个运营 Dashboard。
包含业绩总览、趋势图和需要处理的异常事项。
窄屏下也要能完成主要操作。
```

管理层可以把 Dashboard 区域交给 `dashboard-design`，复用已有且合适的外壳和主题，只在存在具体缺口时引入交互、组件或响应式模块。

还可以这样提需求：

- “做一个订单列表，支持搜索、筛选、选择和批量操作；从订单详情返回时保留筛选条件。”
- “修复这个表格的移动端溢出，保持现有视觉设计。”
- “比较三个适合这个产品的视觉方向，只提供建议。”
- “以这张截图为视觉目标实现页面。”
- “比较这些指定产品案例的导航和信息分组方式。”

如果任务范围已经明确，也可以直接点名某个 Skill。要求显式选择的外源 classics 和历史工作流仍然保留该规则，自动分配不会取消它们的调用限制。

## 可选能力的依赖

| 能力 | 还需要什么 |
| --- | --- |
| 一般界面实现 | 目标项目访问权限及其框架、运行环境；进行视觉和交互检查所需的渲染或浏览器工具 |
| UI/UX Pro Max 调研 | Python 3；所附脚本和数据集的本地搜索使用标准库 |
| 图片设计 Skill | 选定上游入口实际要求的图片生成、图片读取工具 |
| Stitch 工作流 | 可用的 Stitch 工具连接，以及明确要求使用该流程的兼容任务 |
| 外源前端流程 | 固定版本包中要求的运行环境、资源、框架和验证工具 |

MCP 读取器提供 UTF-8 文本资源，不执行脚本，也不提供二进制图片读取；这些操作由宿主的一般文件、运行环境和媒体工具完成。运行选定包的脚本前，先解析其实际位置。提出交付要求时，应区分图片、设计文档和已经实现的代码。

<a id="legacy-python"></a>

## 旧版 Python 安装器

已有完整仓库副本时，仍可使用此前的 Python 安装器。它需要 Python 3.11 或更高版本及完整仓库，npx 或 ZIP 安装不需要执行它：

```sh
python scripts/install.py --agent codex --language zh
```

macOS/Linux 使用 `python3`。旧安装器默认使用用户范围目录，与 npx 默认安装到项目的行为不同。维护旧安装时，保留此前的 `--skills-dir` 和 `--install-dir` 参数。新安装使用上面的任一主要方式即可。

<a id="npx-troubleshooting"></a>

## 常见问题

| 现象 | 检查方法 |
| --- | --- |
| npx 一直转圈 | 可能还在下载，等到出现 `Installed PivotUI ...` 才算完成；如果需要重试并查看详情，使用下方的详细日志命令 |
| npx 以错误码 `128` 退出 | 保留完整报错和日志，单凭这个数字无法判断原因；如果之前用的是旧版 GitHub 源码命令，改用上方的发布包命令重试 |
| 找不到原生 `pivotui` 入口 | 打开新会话，核对脚本输出的入口路径与宿主实际 skills 目录；自定义位置使用 `--skills-dir` |
| 安装器提示入口已修改 | 重装前先保留自己的修改；脚本不会覆盖自定义过的 `SKILL.md` |
| MCP 报 `ModuleNotFoundError` | 确认配置使用的 Python 就是安装了 `requirements.txt` 的虚拟环境 |
| 服务无法启动 | 使用绝对路径；终端命令中给包含空格的路径加引号；MCP 参数分别填写 |
| 目录为空 | 根目录需要包含包或功能分类目录；检查是否显式配置了错误的 `--skill-root` |
| Skill 重名或含糊 | 移除第二套语言版本或重复库，或有意选择准确的目录 `id` |
| 参考文件缺失 | 恢复完整包及目录结构，不要将嵌套入口移出父包 |
| 返回的指令不完整 | 按返回的 `next_offset` 继续调用 `read_skill_file`；`revision` 改变时重新读取 |
| 宿主一次读取全部内容 | 加入上方常驻指令，先发现元数据，再只读取选定入口和资源 |
| 指令读到了，却没有图片或代码 | 检查要求的交付物，以及宿主实际具备的图片、编辑、运行或浏览器能力 |

下载失败后要重试时，可以用这条命令显示更多细节。按需保留自己的 Agent、语言和目标位置参数。npm 的 `--loglevel=verbose` 和 `--timing` 必须放在 **`--package` 前面**：

```sh
npx --yes --loglevel=verbose --timing --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language zh
```

详细日志会显示请求和处理阶段，但不一定显示实时下载百分比。正在正常下载时，不必为了加日志而中断重来。

旧版 GitHub 源码命令仍保留为备用方式。它**需要 Git**，也可能重复获取仓库，因此建议优先使用上方的发布包命令：

```sh
npx --yes github:Getaway-Wuji/PivotUI --agent codex --language zh
```

## 更新版本

通过 npx 安装的用户，从本指南复制最新的发布包命令，保持原来的 Agent、语言和范围。保留此前指定的 `--project`、`--global`、`--install-dir` 或 `--skills-dir`。当前发布包命令是：

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language zh
```

命令中的下载地址对应一个固定发布包，重复运行旧地址不会自动获取更新的版本。安装器会校验所选包并更新它管理的入口，保留此前的集群副本。入口已被编辑，或目标位置的已有集群副本发生冲突时，会报告问题，不会静默覆盖。

通过项目安装 ZIP 使用的用户，下载新项目 ZIP，将完整集群和所选原生入口合并到原来的位置；先核对本地 PivotUI 修改，保留其他 Skill 和项目设置。旧版 Python 安装用户则更新仓库，并用原来的目标位置参数重新运行旧命令。

原始文件/MCP 安装的用户，下载完整的新版本，阅读发布说明和许可声明。整体替换选定版本；路径或依赖改变时重建虚拟环境，更新宿主内的绝对启动路径，并重新验证目录和选定文件读取。产品专属 Token 和设计决策保留在目标项目中。[架构说明](ARCHITECTURE.zh-CN.md)介绍了各模块如何分工及协调共享决策。
