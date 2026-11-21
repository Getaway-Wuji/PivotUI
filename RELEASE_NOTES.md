# PivotUI v0.5.0

在完整保留全部 **14 个外源包** 的基础上，PivotUI v0.5.0 补齐中后台全链路页面矩阵、新增浏览器级自动化审计工具、扩充开发者/平台案例库，并完善开源 CI 与轻量 CLI 入口（总计 **25 个包：11 内源 + 14 外源，29 个标准入口**）：

- **补齐中后台页面闭环（+2 内源页面模块）**：新增 [detail-page-design](English/page-design/detail-page-design/SKILL.md)（实体详情页：身份与状态页头、结构化信息分组、关联数据、安全操作、404/403/过期异常状态与列表返回连续性）与 [form-workflow-design](English/page-design/form-workflow-design/SKILL.md)（整页新建/编辑表单、分步向导与系统设置页：草稿隔离、脏状态拦截、错误汇总定位与吸底保存栏）；`design-orchestrator` 升级至 `1.3.0`。
- **可复用 Playwright 浏览器界面审计脚本**：`responsive-design`（1.0.3）随包提供 `scripts/audit_ui.mjs`，支持多视口自动检测横向溢出、Tab 键盘顺序与隐藏焦点误落、交互控件可访问名称及窄屏触控尺寸，已在真实 Edge 浏览器中对联合样例验证通过。
- **产品参考案例库扩充至 12 张已审案例卡**：`design-reference-research`（1.1.0）基于固定快照 `fcc7028` 新增 4 张开发者/平台类已审文档案例卡（`sentry`、`supabase`、`posthog`、`raycast`），总计 12 张已审案例卡 + 72 项索引记录。
- **基础规范单一真源自动同步 + 子模块版本对齐**：全部 9 个含 `references/foundations.md` 的内源包现由统一脚本同步至 `Foundations 0.2 / Orchestration 0.5.0`；4 个嵌套交互子模块统一对齐 `metadata.version: 1.1.0`。
- **单语言 & 去重双语安装包 + 轻量 CLI + Python 安装器对齐 + GitHub Actions CI**：
  - 提供纯中文 `pivotui-installer-zh-v0.5.0.tgz`、纯英文 `pivotui-installer-en-v0.5.0.tgz` 与去重双语 `pivotui-installer-v0.5.0.tgz`（均约 29 MB）；
  - 新增 `< 10 KB` 零依赖 CLI 包目录 `cli/`（`@getaway-wuji/pivotui`），支持短命令与交互式安装并自动核验 `NPX-CHECKSUMS` SHA-256；
  - `scripts/install.py` 与 `bin/pivotui.mjs` 对齐支持 `--project`、`--status`、`--prune`、`--uninstall` 及 `antigravity`/`gemini`/`windsurf`/`opencode` 预设；
  - 新增 `.github/workflows/ci.yml`，在 Push / PR 时自动验证双语基线、链接、Token 校验器与双安装器干跑。

---

Release **v0.5.0** keeps all **14 external packages** intact while completing PivotUI's admin page matrix (**25 packages: 11 internal + 14 external; 29 standard entrypoints**), adding a reusable Playwright browser UI auditor, expanding reviewed developer-platform cases, and introducing CI and a lightweight CLI launcher:

- **Complete admin page matrix (+2 internal modules)**: adds `detail-page-design` (1.0.0) and `form-workflow-design` (1.0.0) alongside `app-shell-design`, `dashboard-design`, and `data-list-design`; `design-orchestrator` updated to `1.3.0`.
- **Reusable Playwright UI audit script**: `responsive-design` (1.0.3) bundles `scripts/audit_ui.mjs` to check horizontal overflow, Tab/hidden-focus violations, interactive accessible names, and narrow touch targets across viewports (verified in real Edge against the integrated workflow demo).
- **12 document-reviewed product cases**: `design-reference-research` (1.1.0) adds four developer/platform case cards (`sentry`, `supabase`, `posthog`, `raycast`) from pinned VoltAgent `fcc7028` (12 reviewed + 72 indexed-only).
- **Single-source foundations sync & submodule alignment**: all 9 internal `references/foundations.md` files are synchronized to Foundations 0.2 / Orchestration 0.5.0; all 4 nested interaction submodules declare `metadata.version: 1.1.0`.
- **Installer parity, lightweight CLI & GitHub Actions CI**: ships single-language (`zh`/`en`) and deduplicated bilingual `v0.5.0` tarballs (~29 MB each), adds the `< 10 KB` `cli/` launcher package (`@getaway-wuji/pivotui`), brings `scripts/install.py` to feature parity with `bin/pivotui.mjs` (`--project`, `--status`, `--prune`, `--uninstall`, expanded agent presets), and adds `.github/workflows/ci.yml`.

---

# PivotUI v0.4.2

在完整保留全部 **23 个包（9 个内源 + 14 个外源）与 27 个入口** 的前提下，本版本重点优化分发体积、安装管理、MCP 发现能力与确定性校验工具：

- **解决中英文强制同时下载，安装包体积直降近 50%**：新增单语言 npx 安装包 `pivotui-installer-zh-v0.4.2.tgz`（29.35 MB，仅含中文完整集群）与 `pivotui-installer-en-v0.4.2.tgz`（29.31 MB，仅含英文完整集群），同时提供外源去重后的双语通用包 `pivotui-installer-v0.4.2.tgz`（29.57 MB，较旧版 57.26 MB 缩减约 48.4%），安装时仍逐一核验全部 1,912 个文件 SHA-256。
- **安装器生命周期管理与更多 Agent 预设**：`pivotui` CLI 新增 `--status`（查看状态）、`--prune`（清理未使用的旧版本指纹库目录）、`--uninstall`（安全卸载受管入口），并新增 `antigravity`、`gemini`、`windsurf`、`opencode` 默认路径预设。
- **MCP 服务升级至 1.1.0**：增加基于文件 mtime/size 的 frontmatter 发现缓存、在目录元数据中直接返回 `version` / `tags` / `requires` / `exclude_scopes`（0 正文读取预过滤）、支持中英双语界面意图同义词与复合词搜索、扩展 `linked_resources` 识别行内反引号路径，并通过只读 MCP Resource（`pivotui://docs/`）暴露共享集群规范文档，同时保持三个只读固定工具与严格包内边界不变。
- **确定性静态 Token 校验脚本**：`global-style-skill` 1.1.3 随包附带零依赖 `scripts/check_tokens.py`，可对 CSS / JSON 设计变量执行重复定义、未定义引用、循环引用与 WCAG 2.1 对比度检查；全部 13 个内源入口补充结构化 `metadata.tags`。
- **同步 0.4.1 → 0.4.2 集群规则**：同步集成检查与参考意图路由规则，消除主仓与公开发布仓的版本漂移。

---

Release **v0.4.2** keeps all **23 packages (9 authored + 14 external) and 27 entrypoints** intact while optimizing distribution size, installer ergonomics, MCP discovery, and deterministic validation:

- **Independent single-language & deduplicated bilingual npm installers (~48% smaller)**: ships `pivotui-installer-en-v0.4.2.tgz` (29.31 MB, English-only), `pivotui-installer-zh-v0.4.2.tgz` (29.35 MB, Chinese-only), and a deduplicated universal package `pivotui-installer-v0.4.2.tgz` (29.57 MB vs 57.26 MB in v0.4.0) while preserving full SHA-256 verification of all 1,912 installed files.
- **Installer lifecycle & expanded Agent presets**: adds `--status`, `--prune` (cleans up unreferenced older managed libraries), `--uninstall`, plus built-in presets for `antigravity`, `gemini`, `windsurf`, and `opencode`.
- **MCP server 1.1.0**: adds mtime/size frontmatter caching, structured `version`/`tags`/`requires`/`exclude_scopes` catalog metadata, bilingual UI intent synonym matching, inline backtick resource discovery, and read-only `pivotui://docs/` MCP resources while preserving the fixed three-tool surface and package boundary checks.
- **Deterministic token validation**: `global-style-skill` 1.1.3 bundles zero-dependency `scripts/check_tokens.py` for CSS/JSON duplicate, undefined-ref, cycle, and WCAG contrast validation; all 13 internal entrypoints now include structured `metadata.tags`.

---

# PivotUI v0.4.0

Codex 全局目录更新：`r3` 命令安装包把 `--agent codex --global` 的默认入口放在 `~/.codex/skills/pivotui/SKILL.md`，并支持 `CODEX_HOME`；完整资源仍放在 `~/.pivotui/libraries/`。项目安装的 `.agents/skills/pivotui/` 不变。手动全局安装时，将 ZIP 里 `.agents/skills/` 下的 `pivotui` 文件夹复制到用户的 `.codex/skills/`，再把 `.pivotui` 文件夹放到用户主目录。已有共享目录的安装不会被自动移动或删除。

Codex global-directory update: the `r3` command package places `--agent codex --global` at `~/.codex/skills/pivotui/SKILL.md`, respecting `CODEX_HOME`. Complete resources remain under `~/.pivotui/libraries/`. Project installation still uses `.agents/skills/pivotui/`. For manual global installation, copy the ZIP's `pivotui` folder from `.agents/skills/` into the user's `.codex/skills/`, and put `.pivotui` in the user home folder. Existing shared-directory installations are not moved or deleted automatically.

安装说明更新：Codex、DSH、Cursor 用户解压项目安装包后，**把 `.agents` 和 `.pivotui` 两个文件夹一起复制到项目文件夹，就装好了**。Claude Code 用户先在解压副本里把 `.agents` 改名成 `.claude`，再复制这两个文件夹。新的 `PivotUI-Chinese-project-v0.4.0-r2.zip` 与 `PivotUI-English-project-v0.4.0-r2.zip` 简化了包内说明，校验文件为 `PROJECT-CHECKSUMS-v0.4.0-r2.sha256`；集群文件和入口未变，已经安装好的项目不用重装。原有全部 ZIP 和校验文件继续保留。

命令安装改为直接获取已发布的 npm 安装包，无需 Git 获取源码：

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r3.tgz pivotui --agent codex --language zh
```

需要 Node.js 22+ 和 npm/npx。首次下载仍可能较慢，成功后会显示 `Installed PivotUI ...`。安装包校验文件为 `NPX-CHECKSUMS-v0.4.0-r3.sha256`。其他 Agent、英文版及排障步骤见仓库安装指南。

Installation guide update: for Codex, DSH and Cursor, **extract the project ZIP and copy both `.agents` and `.pivotui` into your project folder**. For Claude Code, rename `.agents` to `.claude` in the extracted download before copying the two folders. `PivotUI-English-project-v0.4.0-r2.zip` and `PivotUI-Chinese-project-v0.4.0-r2.zip` contain simpler copy instructions; verify them with `PROJECT-CHECKSUMS-v0.4.0-r2.sha256`. The library and entry files are unchanged, so existing installations do not need reinstalling. All earlier ZIPs and checksums remain available.

Command installation now fetches the published npm package directly, without Git source fetching:

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r3.tgz pivotui --agent codex --language en
```

Requires Node.js 22+ and npm/npx. The first download can still be slow; success prints `Installed PivotUI ...`. The package checksum file is `NPX-CHECKSUMS-v0.4.0-r3.sha256`. See the repository installation guide for other Agents, the Chinese edition, and troubleshooting.

PivotUI 首次公开发行：通过统一管理入口按需选择设计 Skill，让使用者专注描述需求。

- 23 个包：9 个内源模块、14 个明确署名的外源包，共 27 个入口。
- 独立中文版和英文版；每个 ZIP 含完整集群、MCP 源码、安装说明及必要资源。
- 提供集群原理、场景分配、全部 Skill 详解和两种接入方式的双语文档。
- 原创部分采用 MIT；保留全部外源作者、固定版本、MIT 及其他素材许可。
- 排除本地测试文件、研究原图、个人配置、缓存和中间产物。上游包自带且被引用的资源与示例保持完整。

下载 `PivotUI-Chinese-v0.4.0.zip` 或 `PivotUI-English-v0.4.0.zip`，选择一个语言版本接入。`CHECKSUMS.sha256` 用于核对下载文件。

验证范围：双语文件清单、Skill 元数据、相对链接、外源文件一致性、MCP 目录与选定内容读取，以及 ZIP 与发布源码逐文件一致性。不将这些检查等同于每个外部图像或设计服务的完整执行测试。

---

First public release of PivotUI: one management entry selects relevant design skills from the requested outcome.

- 23 packages: 9 authored modules and 14 attributed upstream packages, with 27 entrypoints.
- Complete, independent Chinese and English archives with local MCP source, installation guidance and required resources.
- Bilingual explanations of the cluster, routing scenarios, every skill and both connection methods.
- Original PivotUI work is MIT licensed. Upstream authors, pinned versions and applicable code/asset licenses are preserved.
- Local authoring tests, research originals, personal configuration, caches and intermediate outputs are excluded. Referenced upstream resources and examples remain intact.

Choose one edition and verify its download with `CHECKSUMS.sha256`. Validation covers metadata, local links, paired inventories, upstream parity, selected MCP reads and archive equality; it does not claim full execution of every external workflow.
