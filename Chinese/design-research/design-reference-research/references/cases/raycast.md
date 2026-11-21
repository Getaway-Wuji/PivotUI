# Raycast — 深色命令面板表面阶梯

案例 ID：`raycast`。状态：`document_reviewed_product_unverified`。审阅日期：2026-11-21。

## 覆盖表面与证据边界

以命令面板界面与插件商店卡片为蓝本的营销页面分析（`Raycast-design-analysis`）。全幅产品截图呈现命令面板与 AI 对话视觉气质，不构成对桌面端键盘焦点树或网页无障碍行为的实测验证。

下文引用的关系与数值属于第三方分析描述或声称的提取值，并非对线上产品的独立测量；适配建议为本项目整理。固定版本、上游路径、原文件哈希与字节数见 [catalog-03.csv](../catalog/catalog-03.csv) 中的 `raycast` 记录。

## 可借鉴的视觉关系

- 通过克制的近黑表面阶梯（画布 `#07080a` → 表面 `#0d0d0d` → 抬升 `#101111` → 卡片 `#121212`）配 `1px` 细边线（`#242728`、`rgba(255,255,255,0.08–0.16)`）和紧凑 `6px–10px` 圆角区分层级，无需发光描边或重度模糊。
- 主框架保持单色极简，以高对比纯白胶囊按钮（`#ffffff` 配 `#000000` 字）突出唯一主操作；将四组高辨识分类色（蓝 `#57c1ff`、红 `#ff6161`、绿 `#59d499`、黄 `#ffc533`）搭配 15% 透明底色留给标签与图标分类。
- 紧凑标题阶梯（`24px`、`22px`、`20px`、`18px`）搭配 `14px–16px` 正文，贴合命令菜单、快速切换器与深色工具面板需求。

## 迁移到目标产品

面向深色命令面板、开发者工作台或键盘优先的工具界面，可迁移其细腻的深色表面抬升阶梯、`1px` 细边线与 15% 透明底色的语义标签组合。接入目标产品既有深色 Token，确保键盘焦点环与 `#242728` 边框明显区分，并在把灰字（`#9c9c9d` / `#6a6b6c`）用于功能标签前核实对比度。

## 证据局限与补齐项

上游分析面向由产品界面放大的营销页（注：上游文件第 4 行含一处非标准 YAML 键名，仅采信已核验的视觉描述数据）。真实的命令菜单键盘导航、输入法组合态、焦点恢复与浅色对应主题须通过 `navigation-interaction` 与 `global-style-skill` 补齐。

## 固定来源

[VoltAgent 来源分析](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/raycast/DESIGN.md)。来源定位：[深色表面阶梯与强调色](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/raycast/DESIGN.md#L8) · [字号阶梯](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/raycast/DESIGN.md#L41)。来源文档适用包内 [MIT LICENSE](../../LICENSE)；不包含字体与品牌素材授权。
