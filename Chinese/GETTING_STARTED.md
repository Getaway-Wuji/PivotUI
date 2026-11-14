# 开始使用 PivotUI

将这一完整版本交给支持文件读取的智能助手，或连接其本地 MCP 服务。以[管理层](orchestration/design-orchestrator/SKILL.md)为统一入口，让它按任务选择相关模块。保留目录结构，不要同时注册两个语言版本的同名 Skill。

使用 MCP 时先安装 Python 3.11 或更高版本，按照[服务安装与配置指南](mcp/skill-cluster/README.md)连接，再在宿主的项目规则中要求界面任务先发现元数据并加载 `design-orchestrator`。服务只提供可读取的规则，由宿主使用自己的工具执行任务。

[清单](README.md)介绍全部模块，[第三方声明](THIRD_PARTY_NOTICES.md)列明原作者及素材条款。PivotUI 原创内容采用 [MIT 许可](LICENSE)。
