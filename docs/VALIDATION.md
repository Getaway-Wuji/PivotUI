# Publication checks / 发布检查

Checked on 2026-11-14 for the first PivotUI v0.4.0 publication.

| Check / 检查 | Result / 结果 |
| --- | --- |
| Paired edition inventory / 双语文件清单 | 1,911 corresponding files in each edition; reviewed baseline recorded / 每版 1,911 个对应文件，已记录审阅基线 |
| Skill metadata / Skill 元数据 | 23 packages and 27 entrypoints per edition / 每版 23 包、27 入口 |
| Resource links / 资源链接 | Edition-relative Markdown links validated / 已检查版本内 Markdown 相对链接 |
| Upstream parity / 外源一致性 | All 14 external packages retain matching bytes across both editions / 14 个外源包在两版间字节一致 |
| Source license comparison / 来源许可比对 | Original MIT files match six pinned upstream source revisions / 原 MIT 文件与六个固定上游来源版本一致 |
| Public MCP smoke / 公开目录 MCP 检查 | Both edition servers exposed 3 tools and 27 entries; management entry and a 1,200-character scenario slice were read through real stdio clients / 两版服务均通过真实 stdio 客户端返回 3 个工具及 27 个入口，成功读取主控与 1,200 字符场景资源 |
| Archive equality / 压缩包一致性 | Each ZIP was checked for integrity, exact inventory and byte equality with its edition / 两份 ZIP 均已检查完整性、精确清单及逐文件字节一致性 |
| Public documentation / 公开文档 | README, architecture, install and full skill-guide pairs received an independent semantic review; all 27 guide entry names and links match actual skills / README、架构、安装指南与完整 Skill 详解完成独立双语语义审阅；27 个名称与入口链接均符合实际文件 |

The unchanged MCP implementation also passed the authoring suite: 24 passing tests and one Windows symlink-creation skip. The local test file is excluded from the public distribution. These checks establish packaging and selected protocol behavior, not measured productivity gains, full browser/device coverage, visual quality of a generated product, or successful execution of every upstream image and service integration.

未修改的 MCP 实现还通过原作者工作区测试：24 项通过，1 项因 Windows 不允许创建符号链接而跳过；该本地测试文件不随公开发行版上传。上述结果证明打包与限定协议行为，不代表已测量效率提升、完成所有浏览器和设备覆盖、验证生成产品的视觉质量，或执行全部外源图像和服务工作流。

## Agent quickstart documentation / Agent 快速开始说明

On 2026-11-14, the repository README, installation guides and reusable starter prompts were updated for Codex, Claude Code, DSH (DeepSeek Harness), and other file-capable or local-stdio-MCP Agents. Official host documentation was checked, and Codex CLI registration syntax was also checked against the installed CLI help. The bilingual additions received independent semantic review. JSON, TOML and YAML examples parsed successfully; command parity, local links, explicit anchors and actual edition entry paths were checked.

2026-11-14，仓库 README、安装指南和可复用入口提示词增加了 Codex、Claude Code、DSH（DeepSeek Harness）及其他支持文件读取或本地 stdio MCP 的 Agent 接入说明。已核实宿主官方资料，并用本机 Codex CLI 帮助核对注册语法。新增中英文内容经过独立语义审阅；JSON、TOML、YAML 示例通过解析，命令对应、本地链接、显式锚点和实际入口路径均已检查。

This update changes repository documentation only. The 1,911-pair edition baseline and both existing v0.4.0 archives were revalidated without changing their contents. New starter files live in the repository's `prompts/` directory; they are not additions to the existing ZIPs. No new end-to-end host connection test was performed for Codex, Claude Code, DSH or Cursor.

本次只更新仓库使用文档。1,911 对版本文件基线和现有两份 v0.4.0 压缩包均重新校验通过，内容保持不变。新增提示词位于仓库的 `prompts/` 目录，不属于现有 ZIP 的新增内容。本次没有在 Codex、Claude Code、DSH 或 Cursor 中重新执行端到端连接测试。

## Native command installer / 原生 Skill 命令安装器

A subsequent 2026-11-14 update moves quickstart after the cluster introduction and makes `python scripts/install.py` the primary installation route. It copies a complete edition and creates one native `pivotui` entry for Codex, Claude Code, DSH, Cursor, or a supplied compatible skills directory. MCP remains optional. Host discovery paths were checked against official documentation; both generated-entry templates were reviewed for equivalent behavior and valid metadata/resource targets.

2026-11-14 的后续更新将快速开始移到集群介绍之后，并以 `python scripts/install.py` 作为主要安装方式。安装器复制完整语言版本，为 Codex、Claude Code、DSH、Cursor 或指定的兼容技能目录创建一个原生 `pivotui` 入口，MCP 保持可选。已依据官方资料核实宿主发现路径，并检查两版入口模板的语义、元数据和资源目标。

The installer passed **11 actual CLI tests on Windows** using temporary directories: complete edition byte equality and 27 preserved module entrypoints; spaces and Chinese characters in paths; repeat installation; language switching with the previous library retained; dry-run without writes; required generic-host directory; unrelated-file preservation; refusal to overwrite unmanaged or edited entries and edited libraries; destination protection for both source editions; and an existing installation lock. No tests wrote to the user's actual Agent directories. These are file-installation tests, not end-to-end host discovery or generated-interface tests.

安装器在 Windows 临时目录中通过 **11 项实际 CLI 测试**：完整版本逐文件一致、保留 27 个模块入口、中文与空格路径、重复安装、切换语言并保留旧库、dry-run 不写入、通用宿主目录必填、其他文件保全、拒绝覆盖非托管或修改过的入口与库、两套源版本目录保护、已有安装锁处理。测试没有写入用户实际的 Agent 目录。这些属于文件安装验证，不代表宿主发现或生成界面的端到端测试。

The existing 1,911-pair edition baseline still validates. The installer and its templates are repository-level additions; the v0.4.0 edition ZIPs are unchanged and remain usable through manual files or MCP setup.

现有 1,911 对版本文件基线仍通过校验。安装器和模板属于仓库级新增内容，v0.4.0 语言版 ZIP 保持不变，仍可通过手动文件或 MCP 方式使用。

## npx package and manual project ZIPs / npx 包与项目安装 ZIP

The Node installer adds project scope, optional user scope and relative entry paths without changing the existing 1,911-file edition baseline. npm's omission of the nested MCP `.gitignore` is handled by a fixed copy of its original bytes; source hashes still have to match the baseline, and installed libraries receive the original path and full inventory checks.

Node 安装器增加项目范围、可选用户范围和相对入口路径，现有每版 1,911 个文件的基线保持不变。npm 会省略的嵌套 MCP `.gitignore` 通过固定的原始字节副本恢复；源文件哈希仍须符合基线，安装后的集群使用原始路径并接受完整清单检查。

The Node installer passed **16 tests in two batches on Windows**, with no skips. These cover actual npm packaging and offline npx execution for both editions, complete 1,911-file hash equality and 27 module entrypoints, project relocation, project/user/custom scope, Python-installer compatibility, repeated installs, language changes, dry-run, locking, unrelated-file preservation, and refusal of altered or incomplete sources, libraries and entries. The local package test uses explicit `--package <archive> pivotui` invocation and isolated temporary directories; it does not install into the user's actual Agent directories.

Node 安装器在 Windows 上分两批通过 **16 项测试**，无跳过：实际 npm 打包与两版离线 npx 执行、全部 1,911 个文件哈希一致和 27 个模块入口、项目搬移、项目/用户/自定义范围、旧 Python 安装兼容、重复安装、切换语言、dry-run、安装锁、其他文件保全，以及拒绝修改过或不完整的源文件、库和入口。本地包测试使用显式 `--package <archive> pivotui` 调用及隔离的临时目录，没有安装到用户实际的 Agent 目录。

Both project ZIPs contain **1,914 files**: the unchanged complete edition, native entry, installation manifest and localized copy guide. Two builds produced identical archive bytes. Each archive was extracted into a temporary project, moved to a path with spaces and Chinese characters, and checked against all 1,911 resource hashes. The same entry was also copied to `.claude/skills/pivotui/`, where its relative resource path still resolved correctly. These checks do not execute an Agent model or generate an interface.

两份项目 ZIP 均含 **1,914 个文件**：未修改的完整语言版本、原生入口、安装清单和本地化复制说明。两次构建的压缩包字节一致。两份压缩包均已实际解压到临时项目、移动到带中文与空格的路径，并逐项核对 1,911 个资源哈希；同一入口复制到 `.claude/skills/pivotui/` 后，相对资源路径仍正确。这些检查未运行 Agent 模型或生成界面。

The two project ZIPs and their separate checksum file supplement the release. All six uploaded asset digests matched the local files, including the original English/Chinese ZIPs and their unchanged checksum file. The existing download route remains available.

两份项目 ZIP 和单独的校验文件作为额外附件发布。六个已上传附件的哈希均与本地文件一致，包括原来的中英文 ZIP 及其未修改的校验文件；原下载方式继续保留。
