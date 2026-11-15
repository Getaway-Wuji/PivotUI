# Maintaining and publishing PivotUI / 维护与发布

English is the maintenance source for authored instructions. Update the matching Chinese file and review semantic parity before recording hashes. External packages retain their fixed upstream bytes in both editions, including original licenses and disclosed distribution additions. Keep functional categories and stable identifiers.

内源规则先维护英文，再同步中文并审阅语义。外源包在两版中保留相同的固定来源文件、许可证与已注明增补；保持功能分类和稳定标识。哈希只能发现变化，不能证明翻译准确。

## Validate and build / 检查与打包

Install the builder dependency with `python -m pip install -r scripts/requirements.txt`.

```sh
python scripts/release.py --check-only
# Only after reviewing changed bilingual files:
python scripts/release.py --record-sync
python scripts/release.py
```

The builder checks metadata, edition inventories, local Markdown paths, package identity, original external-file parity and the reviewed hash baseline. It creates `dist/PivotUI-English-v0.4.0.zip`, `dist/PivotUI-Chinese-v0.4.0.zip` and `dist/CHECKSUMS.sha256`, then verifies every archived file against the selected edition. ZIP timestamps are fixed for reproducible output. It refuses to replace different bytes at an existing version: bump `VERSION`, update edition documentation and release links, review, then record the new baseline.

构建器检查元数据、双语清单、相对链接、包身份、外源字节一致性和审阅后的校验基线；生成两份 ZIP 与校验值后，逐文件比对发布目录。ZIP 使用固定时间戳，便于重复构建。相同版本已有不同内容时拒绝覆盖，应先更新版本及文档链接，再审阅、记录基线和打包。

Upload the two ZIPs and checksum file as GitHub Release assets. Keep ZIPs out of the source tree through `.gitignore`. Review the staged file list before every push. Do not add private launch settings, virtual environments, caches, local demos, authoring tests, research transcripts, raw screenshots or intermediate generated pictures. Preserve resources referenced by distributed upstream packages and their licenses; names such as `demo` or `tests` inside an upstream package are not sufficient grounds to remove them.

两份 ZIP 和校验文件作为 GitHub Release 附件上传，不提交进源码历史。提交前复查文件列表，排除私人配置、环境、缓存、本地演示与测试、调研转录、原始截图及中间生成图片。外源包引用的资源与许可需要一起保留，不能只因为上游目录名含 `demo` 或 `tests` 就删除。

## Public packaging changes / 公开发行整理

The initial PivotUI publication keeps the design behavior of the source cluster 0.4.0. It adds the project name, original-work MIT license, public guides, edition quickstarts and release infrastructure. Its edition MCP guides use host-neutral settings and connection checks. The local MCP authoring test file is omitted. External packages are unchanged; the internally authored reference research provenance now distinguishes the new PivotUI MIT license from VoltAgent's preserved MIT notice.

首次 PivotUI 发行保留原集群 0.4.0 的设计行为，增加项目名称、原创 MIT 许可、公开指南、版本入门文档及发布工具；MCP 指南改为通用宿主配置与连接验证，并排除本地 MCP 测试文件。外源包不改动；内源案例研究的来源说明区分新声明的 PivotUI MIT 与保留的 VoltAgent MIT。

The public baseline is `language-sync.json` and describes this publication tree. Authoring archives and prior release baselines remain outside the public repository. Test results should name their actual scope; a successful catalog read does not verify a complete user interface or third-party service.

公开基线 `language-sync.json` 对应本仓库发布目录，作者研究档案和此前发行基线不纳入。验证记录应说明实际范围，目录读取成功不代表完整界面或第三方服务已经验证。

## npx and project-copy packages / npx 与项目手动安装包

The repository's single Node bin is distributed as a fixed Release `.tgz` asset. The preferred invocation is `npx --yes --package=<asset-url> pivotui`, followed by installer options. This route uses npm's HTTP package fetching and cache without a Git clone, SSH fallback or source packaging on the user's machine. `npx --yes github:Getaway-Wuji/PivotUI` remains a compatible source route and requires Git. Both run the same installer, with no Python subprocess or npm-registry publication. `package.json` allowlists both complete editions, the reviewed baseline, the bin and its templates. Check the actual `npm pack` contents against that baseline before publishing changes; npm packaging must not drop a required resource. Runtime installation defaults to the current project, with portable relative paths; `--global` explicitly selects user scope.

仓库的单一 Node 入口以固定 Release `.tgz` 附件发布，首选调用为 `npx --yes --package=<asset-url> pivotui`，后接安装参数。这条路线使用 npm 的 HTTP 下载和缓存，无需在用户机器上执行 Git 克隆、SSH 回退或源码打包。`npx --yes github:Getaway-Wuji/PivotUI` 仍作为兼容的源码路线保留，需要 Git。两者运行相同安装器，不调用 Python，也不依赖发布到 npm registry。`package.json` 明确包含完整双版本、审阅基线、执行入口及模板。发布修改前，按基线核对实际 `npm pack` 内容，确保未漏掉必要资源。安装默认作用于当前项目并使用可搬移的相对路径；显式添加 `--global` 才选择用户范围。

Run `npm pack --json --pack-destination <staging-directory>`, verify both edition inventories including the fixed npm filename mapping, and publish the resulting bytes as `pivotui-installer-v0.4.0-r2.tgz` with `NPX-CHECKSUMS-v0.4.0-r2.sha256`. Test the actual public URL from an isolated project before claiming it works. Use a new packaging revision for changed bytes; never replace an existing asset. The first download is still a complete package and can be slow. An exit code alone is insufficient: confirm the generated entry, manifest and all installed library hashes.

执行 `npm pack --json --pack-destination <staging-directory>`，核对两版文件清单（包括 npm 的固定文件名恢复映射），再将产物以 `pivotui-installer-v0.4.0-r2.tgz` 和 `NPX-CHECKSUMS-v0.4.0-r2.sha256` 发布。实际在隔离项目中执行公开 URL 后，才能宣称该命令已验证。内容变化使用新打包修订号，不覆盖既有附件。首次仍需下载完整包，可能较慢；不能仅根据退出码判断成功，还要确认生成的入口、清单和完整集群文件哈希。

npm omits the nested MCP `.gitignore` file even when its source directory is included. The Node package therefore carries its original bytes as a fixed runtime resource. Only that missing source path may use the packaged mapping, and its hash must match the selected edition's baseline. Installed libraries retain the original filename and are checked against all 1,911 expected file hashes; missing unrelated files and edited originals still fail validation.

npm 会省略嵌套 MCP 目录中的 `.gitignore`，即使已经包含该源目录。Node 包因此以固定运行资源保存其原始字节，仅允许缺失的这一源路径使用映射，并要求哈希符合所选版本基线。安装后的集群恢复原文件名，仍按全部 1,911 个文件的哈希校验；其他文件缺失或原文件被修改时仍会拒绝安装。

Build the additional manual project archives with Node.js available and the existing Python builder dependencies:

```sh
python scripts/build_project_archives.py
```

在具备 Node.js 和现有 Python 构建依赖的维护环境中执行上面的命令，生成额外的项目手动安装包。下载用户只需解压和复制文件，不需要这些构建工具。

The builder uses the real Node project installer, verifies unchanged edition bytes, portable entry links and exact ZIP contents, and creates `PivotUI-English-project-v0.4.0-r2.zip`, `PivotUI-Chinese-project-v0.4.0-r2.zip`, and `PROJECT-CHECKSUMS-v0.4.0-r2.sha256`. Revision 2 simplifies the copy guide; its library and entry files match the original project packages. Upload them as additional release assets. Preserve the original single-edition and project ZIPs and their checksum assets. Do not replace an existing filename with different bytes; increment `PACKAGING_REVISION` for later archive changes.

构建器调用真实 Node 项目安装器，检查语言版本字节未变、入口链接可搬移及 ZIP 精确内容，生成 `PivotUI-English-project-v0.4.0-r2.zip`、`PivotUI-Chinese-project-v0.4.0-r2.zip` 和 `PROJECT-CHECKSUMS-v0.4.0-r2.sha256`。第 2 次打包简化了复制说明，集群资源和入口文件与原项目安装包一致。将它们作为额外发布附件上传，保留原单语言、原项目 ZIP 和对应校验文件。不得用不同内容替换已有同名文件，后续压缩包变化递增 `PACKAGING_REVISION`。
