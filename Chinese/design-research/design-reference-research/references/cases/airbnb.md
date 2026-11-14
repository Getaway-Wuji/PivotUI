# Airbnb — 市场搜索与详情决策

案例 ID：`airbnb`。状态：`document_reviewed_product_unverified`。审查日期：2026-11-14。

## 页面与证据

消费者市场浏览/搜索、房源卡、房源详情与预订区、日期选择和表单。首批案例中它最贴近消费者市场布局任务，但没有独立测试线上预订流程。

以下是第三方文档的描述及声称提取的候选值，未独立测量当前网站；适配段落是本项目建议。完整来源路径、固定提交、原文件哈希和字节数见[元数据记录](../catalog/catalog-01.csv)中的 `airbnb` 行。

## 可用的视觉关系

- 摄影是主要比较表面，与紧凑标题、价格和上下文信息配对。来源把详细阅读区与相邻预订/行动区分开，不把预订控件散布在描述各处。
- 原文列出主要色 `#ff385c`、文字 `#222222`、次级文字 `#6a6a6a`、白色画布及柔和表面 `#f7f7f7`。可借鉴的是行动强调与主要中性的比较内容之间的分工。
- 标题角色包括 16px/600 和 16px/500，配合 16px 正文与 14px 小字。主按钮基础样式列出 48px 高和 14px 24px 内边距。这些是来源候选，不保证任何文案/字体组合都能容纳。

## 在目标产品中如何使用

市场搜索先明确哪些字段改变结果集，并让搜索范围易理解。图像旁应保留足以支持下一次选择的可比较信息；不为卡片整洁隐藏价格含义或关键约束。

详情页在宽屏保持阅读与主要决策相邻。窄屏行动区可作为候选，但信息、滚动、焦点和安全区域行为需在目标项目明确。表单/交互负责人仍要设计验证、异步价格变化、加载和恢复。测试真实中文名称、价格和日期标签。

## 证据边界与需要补全的内容

Known Gaps 说明精确 hover 提取不可靠、没有观察到加载，也没有捕获完整输入错误样式；地图等细节也不完整。本包不采用来源中的 no-hover 政策。原文开头圆角描述与 rounded Token 表不同，应为目标选择一致圆角，不复制矛盾。文档中的断点和触控声称不是运行检查。

实现时按目标内容补全键盘、焦点、加载、错误与窄屏行为，并检查真实对比度。案例数值不是全库默认 Token，也不构成无障碍通过结论。

## 固定版本出处

[VoltAgent 原始分析](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/airbnb/DESIGN.md)。原文定位：[数值与基础样式](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/airbnb/DESIGN.md#L6) · [市场与预订布局](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/airbnb/DESIGN.md#L420) · [响应式候选](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/airbnb/DESIGN.md#L518) · [已知缺口](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/airbnb/DESIGN.md#L539)。来源文档适用包内 [MIT LICENSE](../../LICENSE)；字体和品牌资产未随包提供。
