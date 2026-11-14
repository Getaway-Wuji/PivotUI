# 来源与采用边界

研究日期：2026-11-14。本包含原创综合指导和少量演示片段，不复制第三方教程、UI 套件或产品代码。

## 用户提供的材料

八张中文教学图片介绍百分比尺寸、媒体查询、rem、Flex、Grid、视口单位、rpx 和框架栅格。它们是概念起点。没有任何图片展示某产品的桌面／平板／手机连续状态、实时交互或实测布局切换。原始图片与详细接收记录保留在作者研究档案，不进入本分发包。

采用尺寸、布局与条件规则之间的区分。不采用图片中的根字号缩小、示例断点、固定列数、纯视口字号，或 Grid 全面优于 Flex 的排序。原图水印、颜色或字体不成为目标产品偏好。rpx 内容仅适用于支持它的平台；本版本不声称验证过小程序实现。

## 核心实现参考：Tailwind

用户选择 [Tailwind CSS](https://tailwindcss.com/) 作为核心技术参考。官方文档用于核对实现语义，没有对该网站做跨视口审查。[Tailwind 指导](tailwind.md) 将这些事实转为模块方法，不要求未使用 Tailwind 的项目引入它。

- [响应式设计](https://tailwindcss.com/docs/responsive-design)：基础样式、视口变体、范围与容器查询。
- [主题变量](https://tailwindcss.com/docs/theme)：配置和共享变量范围。
- [状态与能力](https://tailwindcss.com/docs/hover-focus-and-other-states)：键盘焦点及指针／悬停条件。
- [升级指南](https://tailwindcss.com/docs/upgrade-guide)：版本与兼容性边界。
- [源码检测](https://tailwindcss.com/docs/detecting-classes-in-source-files)：可被发现的完整类名。
- [v3 屏幕配置](https://v3.tailwindcss.com/docs/screens)与[官方容器查询插件](https://github.com/tailwindlabs/tailwindcss-container-queries)：旧项目适配。

当前文档标明 v4.3，v3 档案标明 v3.4.17；这些是实际观察的文档标签，不是对用户已安装依赖的假设。面向其他版本时重新核对相关行为。

## 补充一手文档

- [MDN 容器查询](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)：祖先包含关系与组件局部空间。
- [MDN overflow-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)：为原本不可断行的文字提供断行。
- [W3C 媒体查询](https://www.w3.org/TR/mediaqueries-4/#mf-interaction)：包括混合输入的输入能力。
- [W3C 视口单位](https://www.w3.org/TR/css-values-4/#viewport-relative-lengths)：小／大／动态视口与键盘局限。
- [W3C 重排](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)与[目标尺寸](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)：限定范围的无障碍检查和例外，不是认证。

内容优先级、状态延续、保留任务能力的区域模式、四部分决策记录和整合检查，属于本模块的设计综合。它们不是逐字来自 Tailwind 或截图的指令。阅读文档既不能证明示例片段编译成功，也不能证明产品的真机行为。
