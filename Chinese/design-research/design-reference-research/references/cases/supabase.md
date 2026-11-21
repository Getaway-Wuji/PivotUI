# Supabase — 低彩度技术平台与单一祖母绿主操作

案例 ID：`supabase`。状态：`document_reviewed_product_unverified`。审阅日期：2026-11-21。

## 覆盖表面与证据边界

以启发式分析形式整理的公开营销页及合成数据库平台界面示意（`Supabaze-Inspired-design-analysis`）。界面示意仅体现视觉气质，不构成对线上 Supabase Studio 表编辑器或 SQL 控制台的实测验证。

下文引用的关系与数值属于第三方分析描述或声称的提取值，并非对线上产品的独立测量；适配建议为本项目整理。固定版本、上游路径、原文件哈希与字节数见 [catalog-04.csv](../catalog/catalog-04.csv) 中的 `supabase` 记录。

## 可借鉴的视觉关系

- 几乎全部外框与表面都由安静的浅中性色（`#ffffff`、`#fafafa`、细边线 `#dfdfdf` / `#ededed`）和深中性色（`#1c1c1c`、`#202020`）搭配炭黑文字（`#171717`、次级 `#707070`）构成，从而让唯一的祖母绿强调色（`#3ecf8e`，按下 `#24b47e`）成为页面最清晰的主操作锚点。
- 祖母绿主按钮（`#3ecf8e`）采用深色文字（`#171717`）而非白色文字，确保中等明度品牌色上的按钮可读性。
- 控件与卡片采用紧凑克制的圆角（`4px–8px`）与 `8px 16px` 按钮内边距，适配技术控制台与高密度工具界面。

## 迁移到目标产品

面向开发者控制台、云管理后台和 B2B 数据工具，可迁移其“极简中性框 + 单一品牌锚点”的色彩纪律：让表面、边框与次级控件保持中性，避免装饰色与主操作或真实状态色争抢视线。将唯一强调色映射到目标产品自身品牌 Token，并在中等明度品牌按钮上实测对比度后再决定深字或白字。

## 证据局限与补齐项

来源明确标为公开营销页与合成产品示意的启发式解读，未验证真实数据表虚拟滚动、权限边界、键盘操作或完整深色模式控件状态。Circular 字体为专有字体且未随包附带，实际项目须替换为可用中英文字体栈。

## 固定来源

[VoltAgent 来源分析](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/supabase/DESIGN.md)。来源定位：[配色与排版](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/supabase/DESIGN.md#L6) · [控件 Token](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/supabase/DESIGN.md#L127)。来源文档适用包内 [MIT LICENSE](../../LICENSE)；不包含字体与品牌素材授权。
