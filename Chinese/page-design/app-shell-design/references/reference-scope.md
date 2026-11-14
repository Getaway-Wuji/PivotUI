# 参考范围与来源

采用所给模式、核对框架声明或归属设计依据时读取。核对日期为 2026-11-14；复制 API 前检查目标项目实际安装的版本。

## 采用的需求

用户提供了以下方向：

> UI shell layout follows Ant Design Pro layout specification: fixed left sidebar, top header, breadcrumb navigation above page content area.

即：外壳布局遵循 Ant Design Pro 的布局方向，使用固定左侧栏、顶部 Header，以及位于页面内容区上方的面包屑导航。

落实时，这意味着保持原位且可折叠的左侧导航、全局顶部 Header、面包屑定位，以及独立纵向滚动的右侧内容区。适用于兼容的新外壳，或任务明确采用本参考时。已有产品结构和明确任务范围仍然优先。

这是用户选定的组合。Ant Design Pro 提供可配置布局；上述需求不表示每个 Ant 应用都必须采用同一配置。右侧内容滚动方式由用户指定，不是从截图推断，也不宣称为官方通用要求。

## 来源及其支持范围

| 来源 | 支持用途 | 边界 |
| --- | --- | --- |
| [Ant Design Pro / ProLayout](https://procomponents.ant.design/en-US/components/layout/) 与[官方默认配置](https://github.com/ant-design/ant-design-pro/blob/master/config/defaultSettings.ts) | 布局类型、菜单／面包屑集成、可配置布局与固定区域 | 默认值和选项名称随版本而变，不盲目移植配置 |
| [Arco Design Pro 布局源码](https://github.com/arco-design/arco-design-pro/blob/main/arco-design-pro-vite/src/layout.tsx) | Navbar、Sider、路由派生导航、Breadcrumb 与 Content 的具体组合 | 参考结构；不宣称每个 Arco 产品都采用相同滚动方式或主题 |
| [Next.js 布局与页面](https://nextjs.org/docs/app/getting-started/layouts-and-pages) | 包围路由内容的共享布局 | “Next.js Admin” 不指向唯一视觉规范或软件包 |

本包未包含上游源码、标志、图片或主题。本技能从用户需求和公开文档提炼可复用决策。

## 依据标注

- **用户要求：**选定的组合与右侧内容独立滚动。
- **观察／文档事实：**在所给材料、官方文档、源码或运行中的实现里核实的事实；注明是哪一种依据。
- **估计：**从视觉参考推断的数值，保留其不确定性。
- **补充设计：**完成任务所需、但参考未提供的决定，例如键盘行为、移动端导航、返回恢复、宽度和 Token。

当前参考为文字，没有从截图测得的尺寸，也没有观察到的交互状态。为目标产品选择并验证缺失细节；样例数值不成为集群默认值。
