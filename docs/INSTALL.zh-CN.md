# 安装和使用 PivotUI

[English](INSTALL.en.md) · [项目介绍](../README.md) · [Skill 详细说明](SKILLS.zh-CN.md)

选择**一套完整语言版本**，让能够读取本地文件或连接本地 MCP 的 AI 助手使用它。完成首次配置后，直接描述设计任务即可。PivotUI 的 `design-orchestrator` 会选择相关 Skill，不需要每次都由你手动挑选一组 Skill。

按工具跳转：[Codex](#codex) · [Claude Code](#claude-code) · [DSH / DeepSeek Harness](#deepseek-harness) · [Cursor 和其他 Agent](#other-agents)。

首次尝试可以不配置 MCP：解压一套版本，复制[入口提示词](../prompts/pivotui-starter.zh-CN.txt)，替换其中的目录和任务占位符。Agent 必须能够读取该目录。长期使用时，按下方步骤配置，并保存[入口约定](#entry-rule)。

## 1. 获取一套版本

从 [Releases](https://github.com/Getaway-Wuji/PivotUI/releases/latest) 下载中文版或英文版压缩包，也可以克隆本仓库，使用其中的 `Chinese/` 或 `English/` 目录。压缩包包含完整语言版本、本地 MCP 服务和各包所需的资源。

- 选择 `Chinese/`，使用中文编写的内源指令；选择 `English/`，使用英文编写的内源指令。
- 外源包在两个版本中均保留上游原始语言。
- 保持目录结构，并将 `SKILL.md`、参考资料、脚本、数据集和许可声明一起保留。
- 只注册选定的一套版本。两套版本使用相同 Skill 名称，同时注册会产生重名歧义。

本文的 **`<edition-root>` 表示直接包含 `orchestration/`、`page-design/`、`design-system/` 和 `mcp/` 的目录的绝对路径**。它不是仓库根目录、ZIP 文件或 `mcp/` 目录。执行命令前，将所有尖括号占位符替换成实际路径。解压后的外层文件夹可以重命名。

## 2. 选择接入方式

| 方式 | 需要什么 | 适用情况 |
| --- | --- | --- |
| 本地 MCP | 支持本地 stdio MCP 的助手；Python 3.11 或更高版本 | 通过三个固定工具先发现元数据，再按需读取选定指令和资源 |
| 直接读取文件 | 能访问选定版本和目标项目文件的助手 | 没有 MCP 时，直接读取实际文件中的同一套指令 |

两种方式使用相同的 Skill 和路由规则。MCP 提供受约束的文件读取能力，由连接它的助手应用指令并完成任务。MCP 本身不会执行 Markdown、启动其他智能体或调用模型 API。

## 3A. 配置本地 MCP

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

## 3B. 配置直接读取文件

将选定版本放在助手能够访问的稳定位置。如果宿主支持原生 Skill 注册，按其机制注册实际包路径。不同宿主扫描的目录层级不同，不能默认认为将扫描器指向 `English/` 或 `Chinese/` 就能发现所有功能分类和嵌套入口。

如果不支持分类目录扫描，直接提供管理入口的准确路径：

```text
<edition-root>/orchestration/design-orchestrator/SKILL.md
```

助手可以通过版本内的 `README.md` 定位选中的包，只读取需要的入口和资源。必须手动注册时，注册实际包目录；嵌套交互入口应与父包放在一起。只复制 `SKILL.md` 会丢失资源，并可能破坏相对链接。尽量保持整套版本完整。

<a id="entry-rule"></a>

## 4. 让管理层成为默认入口

将下面的指令加入目标项目的助手工作规则，或在任务开始时发送一次。直接读文件时，替换其中的路径：

```text
本项目的界面工作使用 PivotUI，从 design-orchestrator 开始。
使用 MCP 时，先发现目录元数据，读取管理入口，再只加载选定的 Skill 和必要资源。
没有 MCP 时，读取 <edition-root>/orchestration/design-orchestrator/SKILL.md
以及选定文件。只使用这一套语言版本。每个区域指定一个主责，继承产品现有主题和组件，
保持一个权威 Token 来源。遵守外源 Skill 的调用限制。完成用户要求的实际交付物，
并包含相关交互、响应式行为和验证。
```

这条简短的常驻指令会让日常任务进入管理层。仅安装文件或连接目录，并不能保证所有宿主都会在每个界面任务中自动选择主控。

## 5. 用自然语言提交任务

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

## 6. 可选能力的依赖

| 能力 | 还需要什么 |
| --- | --- |
| 一般界面实现 | 目标项目访问权限及其框架、运行环境；进行视觉和交互检查所需的渲染或浏览器工具 |
| UI/UX Pro Max 调研 | Python 3；所附脚本和数据集的本地搜索使用标准库 |
| 图片设计 Skill | 选定上游入口实际要求的图片生成、图片读取工具 |
| Stitch 工作流 | 可用的 Stitch 工具连接，以及明确要求使用该流程的兼容任务 |
| 外源前端流程 | 固定版本包中要求的运行环境、资源、框架和验证工具 |

MCP 读取器提供 UTF-8 文本资源，不执行脚本，也不提供二进制图片读取；这些操作由宿主的一般文件、运行环境和媒体工具完成。运行选定包的脚本前，先解析其实际位置。提出交付要求时，应区分图片、设计文档和已经实现的代码。

## 常见问题

| 现象 | 检查方法 |
| --- | --- |
| `ModuleNotFoundError` | 确认配置使用的 Python 就是安装了 `requirements.txt` 的虚拟环境 |
| 服务无法启动 | 使用绝对路径；终端命令中给包含空格的路径加引号；MCP 参数分别填写 |
| 目录为空 | 根目录需要包含包或功能分类目录；检查是否显式配置了错误的 `--skill-root` |
| Skill 重名或含糊 | 移除第二套语言版本或重复库，或有意选择准确的目录 `id` |
| 参考文件缺失 | 恢复完整包及目录结构，不要将嵌套入口移出父包 |
| 返回的指令不完整 | 按返回的 `next_offset` 继续调用 `read_skill_file`；`revision` 改变时重新读取 |
| 宿主一次读取全部内容 | 加入上方常驻指令，先发现元数据，再只读取选定入口和资源 |
| 指令读到了，却没有图片或代码 | 检查要求的交付物，以及宿主实际具备的图片、编辑、运行或浏览器能力 |

## 更新版本

下载完整的新版本，阅读发布说明和许可声明。整体替换选定版本；路径或依赖改变时重建虚拟环境，更新宿主内的绝对启动路径，并重新验证目录和选定文件读取。产品专属 Token 和设计决策保留在目标项目中，使集群更新不会替换产品设置。[架构说明](ARCHITECTURE.zh-CN.md)介绍了各模块如何分工及协调共享决策。
