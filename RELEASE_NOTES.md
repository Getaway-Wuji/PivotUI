# PivotUI v0.4.0

安装说明更新：Codex、DSH、Cursor 用户解压项目安装包后，**把 `.agents` 和 `.pivotui` 两个文件夹一起复制到项目文件夹，就装好了**。Claude Code 用户先在解压副本里把 `.agents` 改名成 `.claude`，再复制这两个文件夹。新的 `PivotUI-Chinese-project-v0.4.0-r2.zip` 与 `PivotUI-English-project-v0.4.0-r2.zip` 简化了包内说明，校验文件为 `PROJECT-CHECKSUMS-v0.4.0-r2.sha256`；集群文件和入口未变，已经安装好的项目不用重装。原有全部 ZIP 和校验文件继续保留。

命令安装改为直接获取已发布的 npm 安装包，无需 Git 获取源码：

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language zh
```

需要 Node.js 22+ 和 npm/npx。首次下载仍可能较慢，成功后会显示 `Installed PivotUI ...`。安装包校验文件为 `NPX-CHECKSUMS-v0.4.0-r2.sha256`。其他 Agent、英文版及排障步骤见仓库安装指南。

Installation guide update: for Codex, DSH and Cursor, **extract the project ZIP and copy both `.agents` and `.pivotui` into your project folder**. For Claude Code, rename `.agents` to `.claude` in the extracted download before copying the two folders. `PivotUI-English-project-v0.4.0-r2.zip` and `PivotUI-Chinese-project-v0.4.0-r2.zip` contain simpler copy instructions; verify them with `PROJECT-CHECKSUMS-v0.4.0-r2.sha256`. The library and entry files are unchanged, so existing installations do not need reinstalling. All earlier ZIPs and checksums remain available.

Command installation now fetches the published npm package directly, without Git source fetching:

```sh
npx --yes --package=https://github.com/Getaway-Wuji/PivotUI/releases/download/v0.4.0/pivotui-installer-v0.4.0-r2.tgz pivotui --agent codex --language en
```

Requires Node.js 22+ and npm/npx. The first download can still be slow; success prints `Installed PivotUI ...`. The package checksum file is `NPX-CHECKSUMS-v0.4.0-r2.sha256`. See the repository installation guide for other Agents, the Chinese edition, and troubleshooting.

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
