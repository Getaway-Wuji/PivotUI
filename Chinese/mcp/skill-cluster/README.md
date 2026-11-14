# PivotUI MCP

本地只读 MCP 服务，使用官方 Python SDK 2.3.0。它提供技能元数据和按需读取工具；连接它的 AI 选择相关 Skill、应用其规则，并完成用户的设计或实现任务。服务不调用模型 API、不执行技能脚本、不预加载所有正文，也不会自动安装外源 Skill。

## 选择一个语言版本

使用完整的 `English` 或 `Chinese` 版本。两套使用相同的 Skill 名称和标准 `SKILL.md` 入口。一个集群连接只登记一个语言版本；同时加入两套会造成同名歧义，不会自动翻译内容。

语言版本内部的服务按功能分类读取，例如 `Chinese/page-design/dashboard-design/SKILL.md`。同类内源和外源共享分类，来源与可用状态在该版本的 README 中标注。解压后可以更改整个版本文件夹的名称。默认位置按服务文件计算，与启动工作目录无关。

随包外源不需要额外根目录；不要再次登记同名包的另一份副本。

语言选择决定可用规则的语言；具体 Skill 正文和参考资料仍然按任务需要加载。外源 Skill 保持上游原文。

## 安装与启动

需要 Python 3.11 或更新版本。在本目录创建虚拟环境、安装锁定版本的依赖，并使用该环境的 Python 启动。

Windows PowerShell：

```powershell
python -m venv .venv
& ./.venv/Scripts/python.exe -m pip install -r requirements.txt
& ./.venv/Scripts/python.exe -X utf8 server.py
```

macOS/Linux：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -X utf8 server.py
```

后续示例中的 `python` 均指虚拟环境中的可执行文件。选择明确的技能根目录或加入已安装的外源库时，可重复使用 `--skill-root`。一旦指定任何根目录，就只使用所指定的目录，不再追加默认目录。

```text
python server.py --skill-root <所选语言版本目录> --skill-root <已安装的外源库>
```

支持根目录下的包、下一层功能分类中的包，以及包内嵌套 `sub-skills`。共用文档和支撑目录中的嵌套示例不会被登记为 Skill。外源包放到内源包旁边后，使用相同发现机制；README 中的来源标签不改变调度。每次操作刷新元数据，新加入或修改 Skill 不需要重启服务。目录名可以与 YAML `name` 不同；同名 Skill 返回歧义结果，使用目录提供的完整 `id` 选择。

多个根目录重叠时，同一个解析后的实际入口只登记一次，保留首次目录标识，并采用已配置根目录内发现的最外层技能包边界。仅登记嵌套入口的目录不会授予读取未配置父包的权限。不同文件系统位置的副本即使内容相同，仍是不同入口。

## 三个固定工具

| 工具 | 输入 | 返回 |
| --- | --- | --- |
| `catalog_skills` | 可选 `query`，按元数据筛选 | 名称、说明、id、别名、分类、上游隐式调用设置；没有 Skill 正文 |
| `load_skill` | `skill_id`，支持名称、别名或明确 id | 选中入口正文及其直接链接的资源文件名 |
| `read_skill_file` | `skill_id`、相对 `path`，可选 `offset`、`limit` | 一个包内 UTF-8 文本文件的指定字符片段 |

单次正文最多 12,000 字符，单文件最多 2 MiB。长文本返回 `truncated`、`next_offset` 和 `revision`；下一次用返回的 offset 继续读取。同一文件跨页 revision 变化时应重新读取，避免混合不同版本。

这些工具提供无状态读取，不维护会话缓存；重复调用会重新读取当前内容。宿主 AI 应复用任务上下文中已有的入口和资源，只在需要补齐内容或核实变更时重新读取。

嵌套子 Skill 可以读取所属顶层包内的共享参考，例如 `../../references/rules.md`。绝对路径、逃出包边界的路径及符号链接、二进制文件均不能通过资源工具读取。资源内容只作为文本返回，不被执行。

别名映射：`taste-skill` → `design-taste-frontend`，`dashboard-skill` → `dashboard-design`，`interaction-skill` → `interaction-design`，`floating-component-skill` → `floating-components`。`global-style-skill` 按其同名入口发现。taste 目录别名选择的是同一个入口，不会增加一份 Skill；别名也不表示目标已安装。历史 `redesign-existing-projects` 不会被静默映射为当前 taste 流程。

## 连接 MCP 宿主

在助手设置中添加名为 `pivotui` 的本地 stdio MCP 连接。启动程序使用虚拟环境中 **Python 可执行文件的绝对路径**，依次填写三个独立参数：`-X`、`utf8` 和**本目录 `server.py` 的绝对路径**。使用前，将下方占位符替换成真实路径。启动选定版本内部的服务，即可使用该版本的默认根目录。

支持常见 `mcpServers` JSON 格式的宿主可参考：

```json
{
  "mcpServers": {
    "pivotui": {
      "command": "<虚拟环境中的 Python 可执行文件>",
      "args": ["-X", "utf8", "<edition-root>/mcp/skill-cluster/server.py"]
    }
  }
}
```

Windows 可执行文件通常以 `.venv/Scripts/python.exe` 结尾；macOS/Linux 为 `.venv/bin/python`。JSON 路径使用正斜杠或经过转义的反斜杠。其他宿主可能采用不同设置格式，按其格式填写同一个程序和独立参数即可。将该条目合并到已有设置，保留其他连接。

如需明确指定根目录，在 `args` 中追加 `"--skill-root", "<所选技能根目录>"`，可以重复添加。AI 先获取目录元数据，再加载当前任务需要的入口和参考资料。保存配置不等于连接已生效，需要通过宿主验证。协议中的服务名称仍是 `design-skill-cluster`，可以与连接名称不同。

直接运行服务时，它通过标准输入等待 MCP 请求，不会打开网页。通常由宿主启动和停止。如果只想检查命令行入口而不等待连接，可使用虚拟环境执行 `python -X utf8 server.py --help`。

## 将主控设为默认入口

在目标项目的助手规则中加入以下常驻指令：

```text
界面工作使用 PivotUI，从 design-orchestrator 开始。先发现目录元数据，
再只读取选定 Skill 和必要资源。只使用一套语言版本。每个区域指定一个主责，
复用产品权威 Token 来源和组件。遵守外源调用限制，完成用户要求的交付物，
包括相关行为、响应式布局和验证。
```

仅连接目录，不能保证所有宿主都会自动选择管理入口。这条指令为宿主提供默认入口。具体工作由 AI 完成，服务只读取选定指令。

## 验证安装后的连接

连接后，依次调用以下工具：

1. `catalog_skills`，参数 `{}`：完整 0.4.0 版本返回 **27 个入口**，来自 23 个顶层包和 4 个嵌套交互 Skill。目录输出包含元数据，不包含 Skill 正文。
2. `load_skill`，参数 `{"skill_id":"design-orchestrator"}`：检查选定的管理入口。
3. `read_skill_file`，参数 `{"skill_id":"design-orchestrator","path":"references/scenarios.md","offset":0,"limit":1200}`：检查选定资源的文字片段。

宿主界面可能给工具名称加连接前缀。出现名称歧义时，移除重复语言根目录，或有意选择准确的目录 id。文本被截断时，按前文说明继续使用 `next_offset` 并核对 `revision`。本地编写测试不是安装所需内容，因此不包含在公开分发包中。虚拟环境和缓存也保留在本地。

读取器返回文本资源；运行脚本和读取二进制图片需要宿主自身的运行环境或媒体能力。目录可用，不代表每个外源图片、浏览器或设计工作流都已可用。

实现依据：[官方 Python SDK](https://py.sdk.modelcontextprotocol.io/)、[客户端接口](https://py.sdk.modelcontextprotocol.io/client/)、[stdio 运行方式](https://py.sdk.modelcontextprotocol.io/run/)。
