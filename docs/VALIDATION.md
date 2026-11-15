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

After publication, `npx --yes github:Getaway-Wuji/PivotUI --agent codex --language zh` was also executed from a clean temporary project on Windows, with a separate npm cache. It fetched the public repository and completed the installation. An independent check verified the generated entry and manifest, its relative library path, all 1,911 installed resource hashes and all 27 module entrypoints. This confirms the documented public GitHub command performs file installation; it does not test Agent-side discovery or task execution.

发布后，还在 Windows 的全新临时项目中实际执行了 `npx --yes github:Getaway-Wuji/PivotUI --agent codex --language zh`，并使用独立 npm 缓存。命令成功获取公开仓库并完成安装；独立检查确认了生成的入口和清单、相对资源路径、全部 1,911 个资源哈希及 27 个模块入口。这证明文档中的公开 GitHub 命令能够完成文件安装，不代表已测试 Agent 内的发现与任务执行。

Both project ZIPs contain **1,914 files**: the unchanged complete edition, native entry, installation manifest and localized copy guide. Two builds produced identical archive bytes. Each archive was extracted into a temporary project, moved to a path with spaces and Chinese characters, and checked against all 1,911 resource hashes. The same entry was also copied to `.claude/skills/pivotui/`, where its relative resource path still resolved correctly. These checks do not execute an Agent model or generate an interface.

两份项目 ZIP 均含 **1,914 个文件**：未修改的完整语言版本、原生入口、安装清单和本地化复制说明。两次构建的压缩包字节一致。两份压缩包均已实际解压到临时项目、移动到带中文与空格的路径，并逐项核对 1,911 个资源哈希；同一入口复制到 `.claude/skills/pivotui/` 后，相对资源路径仍正确。这些检查未运行 Agent 模型或生成界面。

The two project ZIPs and their separate checksum file supplement the release. All six uploaded asset digests matched the local files, including the original English/Chinese ZIPs and their unchanged checksum file. The existing download route remains available.

两份项目 ZIP 和单独的校验文件作为额外附件发布。六个已上传附件的哈希均与本地文件一致，包括原来的中英文 ZIP 及其未修改的校验文件；原下载方式继续保留。

## Clearer copy guide and direct npm package / 简化复制说明与直接 npm 安装包

The copy guide now starts with copying the two complete folders into the project. README, installation-guide and packaged-guide pairs were reviewed for equivalent steps, including existing-folder merges and renaming only the extracted copy for Claude Code. The project archives use a new `-r2` filename. Each contains 1,914 files and was checked against the original project archive: only `INSTALL.md` changed. An existing user-copied English installation was independently verified against all 1,911 baseline hashes, its 27 module entrypoints, entry digest and relative resource links.

复制说明改为先让用户把两个完整文件夹复制到项目。README、安装指南和包内说明的中英文步骤经过对应检查，包括合并已有目录、Claude Code 仅重命名解压副本。新项目压缩包使用 `-r2` 文件名，每份包含 1,914 个文件；与原项目包逐文件比较，只有 `INSTALL.md` 改变。另对用户实际手动复制的英文安装进行了独立检查：全部 1,911 个资源哈希、27 个模块入口、入口哈希和相对资源链接均正确。

One reported source-route attempt ended with npm exit code 128. The retained log contains no detailed error, so it does not establish whether that attempt failed because of transport, Git or interruption. The preferred command now uses a fixed Release `.tgz` through explicit `--package=URL pivotui`, removing the Git fetch and local source-packaging stages. The packaged contents were checked against both complete edition baselines, including the fixed `.gitignore` mapping. This does not promise that network downloads cannot fail or that first installation is instantaneous.

一次被报告的源码路线安装最终以 npm 错误码 128 退出，保留的日志没有详细错误，无法据此确定是传输、Git 还是中断造成。首选命令现在通过显式 `--package=URL pivotui` 获取固定 Release `.tgz`，移除 Git 获取和现场源码打包步骤。发布包内容已核对两套完整版本基线，包括固定 `.gitignore` 恢复映射。这不代表网络下载不会失败，也不承诺首次安装立即完成。

The actual public Release URL completed installation in a new temporary Windows project with a fresh npm cache and npm's Git executable deliberately pointed at a nonexistent file. Independent output checks matched all 1,911 Chinese resource hashes, the entry digest and 27 module entrypoints. All 11 release asset digests matched local artifacts. npm still fetched the same tarball through multiple temporary GitHub asset URLs during the first run, so this verification does not claim one HTTP request or guaranteed cache reuse. It verifies file installation, not Agent-side task execution.

公开 Release URL 已在 Windows 全新临时项目和独立 npm 缓存中实际安装成功，测试还故意将 npm 的 Git 可执行文件指向不存在的位置。独立输出检查确认了全部 1,911 个中文资源哈希、入口哈希及 27 个模块入口。发布页全部 11 个附件的哈希均与本地产物一致。首次运行时，npm 仍通过多个 GitHub 临时附件地址获取了相同包，因此此验证不宣称只有一次 HTTP 请求或缓存必定复用。验证范围是文件安装，不是 Agent 内的任务执行。

A second run of the same command against the same temporary project and npm cache also completed successfully with Git unavailable. It took 102.35 seconds, including a logged network fetch; the installer again reported all 1,911 files verified. Repeated installation is supported, but this observation is not evidence of fully offline reuse.

对相同临时项目和 npm 缓存再次执行同一命令，在 Git 不可用的情况下也安装成功。耗时 102.35 秒，其中包含一次日志记录的网络获取；安装器再次确认全部 1,911 个文件通过校验。重复安装可用，但该结果不代表完全离线复用。
