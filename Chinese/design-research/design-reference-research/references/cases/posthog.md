# PostHog — 暖米白文档与分析卡片体系

案例 ID：`posthog`。状态：`document_reviewed_product_unverified`。审阅日期：2026-11-21。

## 覆盖表面与证据边界

开发者工具官网、文档框架与分析卡片视觉整理（`PostHog-design-analysis`）。覆盖表面层次、文档排版与语义标签配色，不代表对线上漏斗查询器或会话回放工作流的实测验证。

下文引用的关系与数值属于第三方分析描述或声称的提取值，并非对线上产品的独立测量；适配建议为本项目整理。固定版本、上游路径、原文件哈希与字节数见 [catalog-03.csv](../catalog/catalog-03.csv) 中的 `posthog` 记录。

## 可借鉴的视觉关系

- 在暖米白画布（`#eeefe9`，次级 `#e5e7e0`）上放置纯白内容卡片（`#ffffff`）与文档底（`#fcfcfa`），依靠清晰橄榄灰细边线（`#bfc1b7`、`#dcdfd2`）与紧凑 `4px–6px` 圆角建立层次，避免厚重投影。
- 采用暖橄榄炭黑文字层级（主标题 `#23251d`、正文 `#4d4f46`、弱化 `#6c6e63`），搭配琥珀黄主按钮（`#f7a501` 配深色文字 `#23251d`）以及成对的浅底/深字语义色（蓝 `#2c84e0`/`#dceaf6`、红 `#cd4239`/`#f7d6d3`、绿 `#2c8c66`/`#d9eddf`、紫 `#7c44a6`/`#e7d8ee`）。
- 展示标题尺寸克制（`36px`/`24px`），与 `14px–16px` 正文及 `14px` 代码字号衔接合拍，非常适合文档中心与高信息密度分析工作台。

## 迁移到目标产品

当数据分析平台、内部运维后台或文档站希望采用温和亲和的浅色体系而非冷白或全黑极客风时，可迁移其“暖米白底 + 纯白卡片 + 细边线”的表面梯队及浅/深成对语义状态色。插画装饰保持可选且限定边界，不得干扰表格、筛选或表单主操作。

## 证据局限与补齐项

文档审阅仅涵盖官网、文档与静态分析卡片样式；实时漏斗构建器、多条件表格、键盘快捷键及移动端抽屉导航未验证。实际落地时须核验弱化灰字（`#6c6e63` / `#9b9c92`）在 `#eeefe9` 与 `#ffffff` 上的对比度，并确保状态表达结合文字/图标而非仅靠颜色。

## 固定来源

[VoltAgent 来源分析](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/posthog/DESIGN.md)。来源定位：[配色与语义强调色](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/posthog/DESIGN.md#L7) · [字号阶梯](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/posthog/DESIGN.md#L38)。来源文档适用包内 [MIT LICENSE](../../LICENSE)；不包含字体与品牌素材授权。
