# SAP — 安静页框与平面色带

案例 ID：`sap`。状态：`document_reviewed_product_unverified`。审查日期：2026-11-14。

## 页面与证据

带应用页框外观的营销型首屏、功能区和色带结构。来源没有提供具体页面 URL 清单；十个 SaaS 演示表面被明确说明为非品牌原生组件。

以下是第三方文档的描述及声称提取的候选值，未独立测量当前网站；适配段落是本项目建议。完整来源路径、固定提交、原文件哈希和字节数见[元数据记录](../catalog/catalog-03.csv)中的 `sap` 行。

## 可用的视觉关系

- 来源列出白色画布、浅灰页框 `#f5f6f7`、色带 `#eaecee` 和蓝色行动 `#0057d2`。宽阔平面区域承担分组，而不是大量抬升容器。
- 产品标签栏上方的 60px 导航条形成页框节奏。这是分析文档的描述，不证明完整上线应用框架。
- 导航与列表文字均为 15px、21px 行高，但来源字重分别为 400 与 350；控件圆角为 8px，媒体圆角为 12px。可复用思路是在不大量增加字号或形状的前提下区分语义角色。

## 在目标产品中如何使用

企业产品说明页可比较安静的固定页框与宽内容色带。真实导航层级、标题插槽和滚动归应用框架/页面负责人；卡片只提供视觉候选。不要在未确定焦点和布局连续性前，照搬来源中不同的活动标签高度。

字体字重可用且能清楚区分时，同字号角色可以减少杂乱。若中文替代字体不支持 350，或差别难以感知，使用已有可用字重或其他层级提示。所有选用值都映射到产品主题。

## 证据边界与需要补全的内容

演示块不能作为 SAP 真实 Table、表单、Dashboard 或 App Shell 实现的证据。没有具体来源页面清单支持广泛产品覆盖的结论。专有字体名称、控件尺寸和响应建议仍是来源候选。演示存在不等于已完成产品状态审查。

实现时按目标内容补全键盘、焦点、加载、错误与窄屏行为，并检查真实对比度。案例数值不是全库默认 Token，也不构成无障碍通过结论。

## 固定版本出处

[VoltAgent 原始分析](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/sap/DESIGN.md)。原文定位：[描述与数值](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/sap/DESIGN.md#L4) · [导航与列表文字](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/sap/DESIGN.md#L80) · [页框基础样式](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/sap/DESIGN.md#L122) · [演示排除说明](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/sap/DESIGN.md#L595)。来源文档适用包内 [MIT LICENSE](../../LICENSE)；字体和品牌资产未随包提供。
