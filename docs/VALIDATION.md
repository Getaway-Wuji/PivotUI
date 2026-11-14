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
