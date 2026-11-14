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
