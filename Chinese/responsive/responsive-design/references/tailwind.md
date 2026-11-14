# Tailwind 实现适配

目标项目使用 Tailwind 时读取。响应式决定仍来自用户任务与可用空间，工具类名称不能决定内容优先级。以下所有示例阈值和间距都用于演示，不是本库默认值或设备类别。替换为项目约定和已验证的变化条件。

## 检查实际项目

读取已安装包版本与锁文件、CSS 入口、框架集成、主题配置、源码扫描规则及容器查询插件。提议修改前，确定权威的断点定义。检查已有组件及生成的 CSS，不要假设当前在线文档描述的就是已安装版本。

局部响应式修复保留已安装的主版本。升级可能改变工具、浏览器支持、默认值和交互行为，是需要独立范围与检查的另一项修改。未使用 Tailwind 的项目可以用普通 CSS 实现相同决定。

## 基础布局与视口变化

无前缀工具类建立适用于各宽度的基础布局。在标准最小宽度配置中，`sm:` 等前缀从该项目对应的最小视口宽度起生效，不代表“仅手机”。已安装版本和屏幕配置支持时，`md:max-lg:` 等范围变体将规则限定在配置的阈值之间。在假定这些语义之前，检查自定义屏幕定义和生成的 CSS。不要根据名称推断物理设备类别。

```html
<section class="grid min-w-0 grid-cols-1 gap-4 md:grid-cols-2">
  <article class="min-w-0">Main task and actions</article>
  <aside class="min-w-0">Related information</aside>
</section>
```

使用项目已有的 viewport meta 声明；普通浏览器页面需要 `width=device-width, initial-scale=1.0`。不要禁用缩放。检查实际生成的查询，并用真实内容测试阈值略低于、等于和略高于的位置。

v4 使用主题变量定义断点：

```css
/* Illustrative addition to the existing theme, not a replacement. */
@theme { --breakpoint-content: 52rem; }
```

v3 的自定义阈值使用已有 JavaScript 配置。此示例说明配置机制，不是对前一个值的换算：

```js
module.exports = {
  theme: { extend: { screens: { content: "832px" } } }
};
```

仅合并相关修改，不用此片段替换项目配置。v3 的 `theme.screens` 替换断点集合，`theme.extend.screens` 则扩展或覆盖单独条目。v4 的断点单位应与已有集合一致，以免出现非预期排序。重复的局部值经协调后可能值得成为共享 token；一次局部修复不足以成为重定义全局阈值的理由。

不要假设 `52rem` 始终等于 `832px`。媒体查询中的字体相对单位使用初始字号，其中包括用户偏好，而不是页面作者设置的根字号。检查实际条件，不要假定根字号为 16px 再换算。[媒体查询单位](https://www.w3.org/TR/mediaqueries-4/#units)。

## 组件空间与容器查询

整页结构使用视口查询。可复用组件需要适应侧栏、面板或主体区域分配的空间时，使用容器查询。`md:` 和 `@md:` 属于不同查询体系，不必有相同阈值。

```html
<div class="@container">
  <div class="flex min-w-0 flex-col gap-3 @lg:flex-row">
    <div class="min-w-0 flex-1">Record summary</div>
    <button class="shrink-0">Open details</button>
  </div>
</div>
```

查询容器包围需要改变布局的元素。在同一视口宽度下，将组件放入不同尺寸的父级测试。嵌套区域可用具名容器消除歧义。

v4 内置容器查询。Tailwind 官方插件为 v3.2+ 提供此能力；使用相关类名前，确认插件已经安装并配置。插件与当前核心的任意值语法不同：插件文档使用 `@[30rem]:`，当前核心文档使用 `@min-[30rem]:`。较少使用的变体要针对已安装版本核对。目标浏览器支持时，也可以用普通 CSS 实现；插件不是浏览器兼容补丁。

v4 的 `--container-*` 值还生成 `max-w-md` 等尺寸工具类。修改某个值可能影响容器查询阈值之外的用途，因此共享修改须与 token 和组件负责人协调。

## 输入能力与构建检查

当前 v4 提供 `pointer-coarse:`、`pointer-fine:` 和 `any-pointer-*` 变体。前一组关注主要指向设备，后一组关注任意可用指向设备。混合设备可支持多种输入方式。已安装 Tailwind 缺少合适变体时，使用普通能力媒体查询。

不依赖悬停也要能够完成必要操作。v4 的 `hover:` 受悬停能力条件约束，不能依赖触摸激活来替代。保留可见焦点、键盘操作和明确控件。与指针有关的间距变化不得移除键盘访问或改变任务含义。

Tailwind 扫描完整的类名字符串。使用明确的类名映射，不要拼接 `${breakpoint}:grid-cols-${count}` 这样的片段。通过项目实际流程构建，确认生成的选择器和查询，并检查渲染结果。仅编译成功不能证明导航、阅读顺序、内容可达性或触控行为正确。

## 官方依据与版本边界

核对日期为 **2026-11-14**：当前文档显示 **v4.3**，v3 档案显示 **v3.4.17**。这些是文档核对，不是对 Tailwind 网站进行多尺寸视觉审查。以上片段是实现示例，不是浏览器执行证据。

- [响应式设计](https://tailwindcss.com/docs/responsive-design)：基础样式、视口与容器查询、断点单位。
- [主题变量](https://tailwindcss.com/docs/theme)：断点与容器命名空间。
- [v3 screens](https://v3.tailwindcss.com/docs/screens)：JavaScript 配置，以及替换与扩展的区别。
- [v3.2 断点新增能力](https://tailwindcss.com/blog/tailwindcss-v3-2)：范围／动态断点支持，以及复杂屏幕配置下的限制。
- [官方容器查询插件](https://github.com/tailwindlabs/tailwindcss-container-queries)：v3.2+ 支持，以及 v4 内置替代。
- [交互状态](https://tailwindcss.com/docs/hover-focus-and-other-states)：指针能力和焦点变体。
- [升级指南](https://tailwindcss.com/docs/upgrade-guide)与[兼容性](https://tailwindcss.com/docs/compatibility)：行为变化和浏览器要求；迁移前针对目标版本核对。
- [源码检测](https://tailwindcss.com/docs/detecting-classes-in-source-files)：完整类名和生产构建生成。
