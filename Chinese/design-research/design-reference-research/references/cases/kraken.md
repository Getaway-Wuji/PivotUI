# Kraken — 有限的白底紫色参考

案例 ID：`kraken`。状态：`document_reviewed_product_unverified`。审查日期：2026-11-14。

## 页面与证据

白底、紫色强调的网站，未列具体来源页面。仓库摘要提到暗色交易 UI，但本篇文档不建立该范围。

以下是第三方文档的描述及声称提取的候选值，未独立测量当前网站；适配段落是本项目建议。完整来源路径、固定提交、原文件哈希和字节数见[元数据记录](../catalog/catalog-02.csv)中的 `kraken` 行。

## 可用的视觉关系

- 来源主要紫色 `#7132f5` 搭配白底、文字 `#101114` 和冷灰 `#686b82`。不同紫色变体分配给实心、描边和浅色控件。
- 实心候选的内边距为 13px 16px、圆角 12px；描边控件在白底保留紫色文字/边框。白色按钮描述却使用 10px 圆角，构成来源矛盾。
- 成功徽章使用半透明绿色背景与深绿 `#026b3f` 文字，与紫色行动强调分离。展示和正文有不同字体角色，来源列出 48px/700 展示字与 16px/400 正文。

## 在目标产品中如何使用

当目标方向需要紫色或用户指定 Kraken 时，可用于狭窄的行动与徽章角色比较。状态与行动语义分开，并映射既有 Token。若目标品牌不是紫色，借鉴角色区分而不是引入该色相。

目标的实心、描边、浅色按钮应使用一致几何规则，再验证可见状态和真实内容。常规密集交易 Dashboard 使用既有 Dashboard/列表方法；本卡缺少任务结构及交易交互证据。

## 证据边界与需要补全的内容

这份简短文档的响应部分只有断点列表，没有实际重排规则。一般规则要求所有按钮 12px，而白色按钮候选写 10px；两者都不是已验证的普遍要求。字体资源、键盘/焦点、加载/错误行为和可访问颜色组合都需要目标产品决策与检查。

实现时按目标内容补全键盘、焦点、加载、错误与窄屏行为，并检查真实对比度。案例数值不是全库默认 Token，也不构成无障碍通过结论。

## 固定版本出处

[VoltAgent 原始分析](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/kraken/DESIGN.md)。原文定位：[参考范围与配色](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/kraken/DESIGN.md#L1) · [文字层级](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/kraken/DESIGN.md#L34) · [白色按钮几何](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/kraken/DESIGN.md#L77) · [规则与仅断点的覆盖](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/kraken/DESIGN.md#L103)。来源文档适用包内 [MIT LICENSE](../../LICENSE)；字体和品牌资产未随包提供。
