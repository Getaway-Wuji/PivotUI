# 案例索引

快照：VoltAgent/awesome-design-md，提交 `fcc70284932276d085f01ef9f83edde90b1258cb`，审查日期 2026-11-14，2026-11-21 扩充。共 84 项来源，12 张已审读文档的本地案例卡，72 项仅登记且范围未知。任何卡片都不声称已核验当前网站。本库是案例参考，不是公司官方设计系统目录。

## 已审读候选

只读取当前任务需要的案例。下列标签描述被检查文档的范围，不代表整家公司。

| 案例 | 页面范围 | 可用维度 | 重要边界 |
| --- | --- | --- | --- |
| [Linear](cases/linear.app.md) | 营销 | 深色表面、克制强调色、产品图 | 官网产品截图不证明应用工作流 |
| [Stripe](cases/stripe.md) | 营销、注册、演示组合图 | 渐变位置、CTA 层级、数字排版 | 受启发的解读，未完整覆盖 Dashboard |
| [Notion](cases/notion.md) | 营销与定价 | 功能分组、行动/链接区分、定价信息 | 不是编辑器/数据库 UI；时长包含推荐值 |
| [IBM](cases/ibm.md) | 企业营销 | 平面方正表面、轻展示字、清晰色带 | 缺少实际产品表格/菜单及完整暗色主题 |
| [SAP](cases/sap.md) | 营销型表面与演示 SaaS 示例 | 安静页框、平面色带、同字号文字角色 | 无具体来源页面清单；示例不是品牌原生组件 |
| [Vercel](cases/vercel.md) | 营销与自动派生示例 | 中性色层级、技术字体角色、间距节奏 | `ex-*` 是演示，不是已核验上线组件 |
| [Airbnb](cases/airbnb.md) | 市场搜索与详情 | 图像/信息比例、搜索、预订行动位置 | 加载、精确 hover、完整错误态未观察到 |
| [Kraken](cases/kraken.md) | 未明确具体页面的白底网站 | 紫色行动角色、按钮、徽章 | 细节有限；断点列表没有重排规则 |
| [Sentry](cases/sentry.md) | 开发工具营销与定价（启发式） | 深紫+纯白双极性表面、焦点环、代码排版搭配 | 启发式分析，未核验线上异常分诊表格 |
| [Supabase](cases/supabase.md) | 平台营销与界面示意（启发式） | 极简中性框、单一祖母绿主按钮配深色文字 | 启发式分析，未核验线上 Studio SQL/表编辑流 |
| [PostHog](cases/posthog.md) | 开发工具营销、文档与分析卡片 | 暖米白画布、细边框白卡、浅底/深字语义标签 | 未核验实时漏斗查询器与会话回放 |
| [Raycast](cases/raycast.md) | 基于命令面板放大的营销表面 | 近黑表面阶梯、1px 细边线、15% 透明底分类色 | 未核验桌面端键盘焦点树及浅色对应主题 |

完整业务 Dashboard、权限列表、键盘流程或交互约定最多只能从这十二张卡片获得局部视觉候选。没有一张提供已核验的完整运营工作流。[选择规则](selection.md)说明回退方式和逐项证据；需要时才读取[模式](patterns.md)来比较可迁移关系。

## 查找其他具名来源

只打开涵盖准确来源 ID 的字母分片，每片 21 项。在实际阅读来源前，未知范围保持未知；仅登记案例需要联网读取来源或用户提供资料才能继续分析。上面十二张卡片可离线使用。

| ID 范围 | 元数据文件 |
| --- | --- |
| `1win` 至 `expo` | [catalog-01.csv](catalog/catalog-01.csv) |
| `ferrari` 至 `mydealz` | [catalog-02.csv](catalog/catalog-02.csv) |
| `nerdwallet` 至 `sentry` | [catalog-03.csv](catalog/catalog-03.csv) |
| `shopify` 至 `zapier` | [catalog-04.csv](catalog/catalog-04.csv) |

名称使用上游 ID，包括 `linear.app`、`mistral.ai`、`opencode.ai`、`together.ai` 和 `x.ai`。可忽略品牌名大小写，但不能默默匹配无关产品。

CSV 字段：`id`；`review_status`；分号分隔的 `surface_scope` 和 `tags`；相对于包根目录的本地 `card`（仅登记项为空）；上游 `source_path`；固定版本 `source_url`；原文件 `sha256`；原文件 `bytes`。两版元数据标识符均保留英文以保持匹配。哈希标识原始来源，不标识改写后的案例卡。许可与更新见[来源说明](../UPSTREAM.md)。
