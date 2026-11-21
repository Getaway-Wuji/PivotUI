# Sentry — 双极性深紫开发工具界面

案例 ID：`sentry`。状态：`document_reviewed_product_unverified`。审阅日期：2026-11-21。

## 覆盖表面与证据边界

以启发式分析形式呈现的公开营销页、定价页与开发者工具展示（`Sentri-Inspired-design-analysis`）。不构成对线上 Sentry 异常追踪列表、分诊工作流或后台告警规则的实测验证。

下文引用的关系与数值属于第三方分析描述或声称的提取值，并非对线上产品的独立测量；适配建议为本项目整理。固定版本、上游路径、原文件哈希与字节数见 [catalog-03.csv](../catalog/catalog-03.csv) 中的 `sentry` 记录。

## 可借鉴的视觉关系

- 将深紫夜色表面（`#150f23`、`#1f1633`、细边线 `#362d59`）与纯净白底定价/文档区块（`#ffffff`、细边线 `#cfcfdb` / `#e5e7eb`）并置，并通过深紫黑主按钮（`#150f23` 配 `#ffffff` 文字）在明暗两极均保持稳定识别度。
- 将高饱和强调色（亮绿 `#c2ef4e`、粉红 `#fa7faa`、紫色 `#6a5fc1`）克制用于高亮与标签，界面正文使用中性无衬线 Rubik / 系统无衬线（`16px`），代码段使用等宽 Monaco/Menlo（`16px`）。
- 明确标注了蓝色焦点环（`#9dc1f5`）以及按钮与卡片的 6–12px 克制圆角。

## 迁移到目标产品

针对兼具深色技术展示/控制台区域与高密度浅色定价/配置表的开发或监控类产品，可借鉴其双极性克制思路：深色底保持低饱和紫灰而非荧光化，业务状态与告警严重级别应沿用目标产品自身可访问的状态 Token，不直接把装饰性亮绿/粉红当成业务状态色。

## 证据局限与补齐项

来源明确标为启发式分析，仅覆盖公开营销与定价展示，不证明真实异常列表筛选、键盘快捷键、告警升级流或生产后台主题切换。定制展示字体未随包附带。落地时须实测明暗表面下的前景/背景对比度，并在本地补齐键盘、加载与窄屏行为。

## 固定来源

[VoltAgent 来源分析](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/sentry/DESIGN.md)。来源定位：[配色与排版](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/sentry/DESIGN.md#L6) · [按钮 Token](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/design-md/sentry/DESIGN.md#L146)。来源文档适用包内 [MIT LICENSE](../../LICENSE)；不包含字体与品牌素材授权。
