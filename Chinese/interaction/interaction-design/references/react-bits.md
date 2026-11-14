# React Bits 的选择与接入

需要动画、交互组件或替换自绘效果时读本页；寻找具体名称再读 [全量目录](react-bits-catalog.md) 的有关类别。仅修复已有控件焦点或提交逻辑时，无需为使用组件库而替换控件。

## 本模块采用方式

用户指定 React Bits 为多数适用动画的优先来源。先从它的 Micro 与 Components 找到满足任务的组件，再考虑 Animations 包装；匹配时直接采用官方源组件并映射项目 token。允许自由选择库内其他效果，但按页面目标、输入方式和运行预算筛选。没有合适组件、目标非 React、已有组件更完整或接入成本不合适时，用项目已有能力完成，记录理由。

本次截至 2026-11-14 的公开目录为 216 项。固定研究提交：[`4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce`](https://github.com/DavidHDev/react-bits/commit/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce)。目录与注册表已核对；以下代表性记录是 **TS-CSS 源码/API 关键分支抽查**，并非亲自操作演示，也不是全库运行认证。后续版本、其他变体和所用参数需在目标项目复核。

## 先按用户任务选型

消息与浮层先遵循 [浮层子模块](../sub-skills/floating-components/SKILL.md) 的适用/禁止表，再选库内表现。Swipe Toast 仅承载轻量成功/信息，不用于任何错误或待处理告警；错误放字段附近或持续 Alert。库自带主题/示例不会覆盖本模块约定。

先确认内容数量、排列形态、触发动作与目标状态，再匹配候选。例如多作品的圆柱卡带优先考察 Circular Carousel / Circular Gallery；Lanyard 表现单张悬挂身份牌，不能仅因“带”字相近就替代多图浏览。候选外观相近也不证明能精确还原参考中的全部行为。

| 任务 | 优先候选 | 接入时保留的责任 |
| --- | --- | --- |
| 二态设置、待办勾选 | Squish Switch、Spring Check | 受控值、可理解的名称、异步保存/回滚、表单字段接入 |
| 筛选单选、互斥方案、分段切换 | Glide Select、Jelly Radio、Rubber Segment | 草稿与已应用值、真实选择语义、无结果与清除行为 |
| 输入、验证码、参数调节 | Code Slots、Scrub Field、Wake Slider、Prompt Bar | 校验、粘贴/输入法、业务格式、提交与错误关联 |
| 正在执行/完成/失败 | Status Mark、Call Chip、Lattice Loader、Thought Line | 以真实请求状态驱动；提供下一步，不用动画定时器伪造成功 |
| 有撤销窗口的轻量操作 | Fuse Button、Swipe Toast | 真正的撤销事务与超时规则；失败另用内联/Alert，不进入 Toast；焦点不丢失 |
| 确需降低误触的操作 | Hold Button、Slide Commit 均需先处理下表所列取消缺口 | 按住/滑动必须适合场景；提供等价键盘路径，保留业务确认规则；高影响操作先验证取消或失焦绝不提交 |
| 短列表、分步填写 | Animated List、Stepper | 大列表性能、当前步校验、已输入值、服务器错误与回退 |
| 提示与局部显隐 | Warm Tooltip、Fade Content、Animated Content | 提示可由焦点触发；显隐不能让隐藏控件仍可聚焦 |
| 品牌导航、图片浏览 | Card Nav、Pill Nav、Staggered Menu、Carousel 等 | 由页面主力确认区域；导航语义、焦点、关闭、暂停与触屏 |
| 重点操作的视觉反馈 | Magnet、Click Spark、Glare Hover | 装饰不代表请求已完成；不移动密集业务控件的命中位置 |

目录中的营销字效、背景、指针与 3D 效果也可使用；选择它们是页面表现决定，应交接给页面主力。不要把创意导航组件直接当作模态抽屉、把粒子爆发当作提交成功，或把手势特效强加到所有按钮。

## 源码接入

[官方安装页](https://reactbits.dev/get-started/installation)采用逐组件源码安装或手动复制。选 JS/TS 与 CSS/Tailwind 变体，匹配目标项目现有技术栈；名称与大小写从目标页或注册表核对。例如：

```sh
npx shadcn@latest add @react-bits/SplitText-TS-TW
```

已有 `components.json` 时，将下列命名空间合并到其 registries，不覆盖其他设置：

```json
{
  "registries": {
    "@react-bits": "https://reactbits.dev/r/{name}.json"
  }
}
```

仓库同一提交的 [README 安装说明](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/README.md)也提供：

```sh
npx jsrepo@latest add https://reactbits.dev/r/SplitText-TS-TW
```

以上是实际文档中的例子，不是要求每个任务安装 Split Text。把名称换成已核对候选；只选一种接入方式。手动方式从目标页 Code 选择变体，复制必要文件并安装该组件列出的依赖。组件安装后从项目实际文件路径 import，不假设存在统一的 `reactbits` npm 导出包，也不固定用户项目目录。

接入前查看目标组件 Props、源码、CSS、registry 的 dependencies 与实际 package.json，避免重复动画引擎或不兼容依赖。尤其 Warm Tooltip 当前 TS-CSS 注册表列出 `react-dom@^19.0.0`；与已有 React 主版本核对，不能无条件升级整个项目。保留目标项目既有框架/路由，按需要处理客户端边界与 SSR。安装只能证明取得源码，不能证明流程可用。

原组件的颜色、时长、尺寸、z-index 和素材是默认值。先通过公开 props 或局部 CSS 变量映射现有 token；必要修改限制在该组件适配层。公开 API 不支持所需业务能力时，补行为或换用已有组件，说明实际适配。不要把官方默认值写成本产品的用户偏好。

## 代表性证据与四段行为

以下“源码”表示能从固定提交读到的实现；“补充”表示接入者需要结合任务落实的建议。所有行均未做浏览器或辅助技术运行验证。源码定位见下方逐项链接。

| 组件 / 证据 | 触发条件 → 状态变化 → 用户反馈 → 退出或恢复 | 接入判断与待补行为 |
| --- | --- | --- |
| Animated Content / 源码 | scroll 或 mount → 内容进入 → 可配置位移/透明度等 → once、scrub 或配置消失；读取减少动效偏好后直接显现 | `onComplete` 是动画完成。补充：不能用于确认请求成功；交互浮层的关闭和焦点另管 |
| Fade Content / 源码 | scroll 或 mount → 隐显效果 → 配置的 fade/focus 等 → once/exit/消失设置；减少动效分支直接显现 | GSAP + ScrollTrigger。补充：默认选简单 fade，避免对错误文字施加延迟或长模糊 |
| Click Spark / 源码 | 点击或 ref.spark → 生成画布装饰 → 短时火花 → 生命周期结束清理；有 disabled、减少动效分支 | 无额外 registry 依赖。补充：业务按钮本身必须保留名称、焦点和真实结果反馈 |
| Magnet / 源码 | 指针进入作用范围 → 位移/倾斜等 → 弹性跟随 → 离开后回位；disabled 或减少动效时不进入磁吸 | 无额外 registry 依赖。补充：用于少量重点入口，稳定命中区域，触屏保持可点击 |
| Animated List / 源码 | 指针或方向键/Home/End → 当前条目变化 → 选中标记移动；Enter/Space 可调用 onItemSelect → 离开不自动提交业务 | 有 listbox/option 相关语义和减少动效分支。补充：先确认任务确实是选择列表；密集业务表格继续复用原表格 |
| Stepper / 源码 | 前后或步骤入口 → step 变化 → 指示器和内容转换 → 返回前步或触发 onFinalStepCompleted | 支持受控 step、linear；回调不等待校验 Promise。补充：校验通过才更新 step；最终成功由提交结果决定 |
| Glide Select / 源码 | 按钮点击/键盘 → open → listbox 与活动项；方向键/Home/End/首字母定位 → Enter/Space 提交，Escape/Tab/外点关闭 | value/onChange 支持受控；选择后回到触发按钮；CSS 有减少动效规则。补充：和表单/过滤请求接线，检查辅助技术和长列表 |
| Spring Check / 源码 | button 激活 → checked 切换 → 勾选与文字效果 → 再次激活取消；disabled 阻止 | button role=checkbox，checked/onChange、减少动效。补充：需要提交字段时接入表单；勿将划线样式用于不表示完成的普通选项 |
| Squish Switch / 源码 | 点击或拖动 → checked 变化 → 滑块/色彩变化 → 再次切换或取消拖动 | button role=switch、aria-disabled、受控 checked/onChange、减少动效。补充：保存中锁定或队列策略、失败回滚及错误说明 |
| Warm Tooltip / 源码 | 触发器悬停/焦点等 → 延迟打开，共组后续可更快 → tooltip/描述关联 → 失焦/离开/Escape 等关闭 | motion、Portal，有减少动效处理；触发器移出会安排关闭，未见提示层保持悬停的处理。接入补触发器与提示共同悬停区域，验证移入提示仍可读；关键说明不只放 tooltip，触屏长按不干扰滚动 |
| Status Mark / 源码 | 父层 status/progress 更新 → pending/running/done/failed/cancelled → 图形和可选 label → 父层推进下一状态 | motion + 减少动效；不发请求、不实现重试。补充：持久文字、必要 live region、失败操作由业务层提供 |
| Swipe Toast / 源码 | open → open/closing/gone → 消息/动作/计时线 → 超时、滑动、动作、关闭、Escape 或程序关闭；悬停、焦点、页面隐藏会影响计时 | motion，aria-live，关闭原因回调。本模块只采用轻量成功/信息；错误/待处理告警用内联或 Alert，设 duration=0 也不能用于错误。按任务启用关闭按钮，接入公共层级 |
| Fuse Button / 源码 | 激活 → idle→armed → 撤销入口与计时线 → 撤销回 idle，窗口到期 reset/stay；onCommit 可在 press 或 fuseEnd | 有按钮/状态文字、焦点转换；CSS 降低动效。补充：onCommit/onUndo 是 void 回调，需真实事务与失败恢复；不能把 armed 文案当服务器确认 |
| Hold Button / 源码 | 指针或 Enter/Space 按住 → holding → 填充进度 → 提前释放/移出取消，达阈值 done 并 onHold | done 仅代表手势完成。**本次源码缺口**：Escape 仅取消键盘长按；有窗口 blur 处理，但未见控件失焦取消，Tab 移焦可能保留提交计时。接入补各种输入的取消及控件失焦清理，验证不误触 onHold；提供无需长按的等价路径，业务另管 pending/error/success |
| Slide Commit / 源码 | 拖至末端释放或键盘达到末端 → pending（onConfirm Promise）→ 完成/错误标签 → 失败回归可尝试状态、成功按 holdMs 收拢 | **本次源码缺口**：pointercancel 共用释放逻辑，末端取消会提交；拖动时 Home/Escape 也走该路径。接入先拆分取消与确认，验证取消绝不调用 onConfirm，再评估高影响用途。End/方向键达到末端会提交，应明确键盘约定；业务另补幂等、防重复与持久错误 |
| Carousel / 源码 | 按钮/拖动/方向键或 autoplay → 当前项改变 → 卡片过渡与页码 → 前后、Home/End；有焦点/悬停、离屏及减少动效处理 | 无需默认开启 autoplay。补充：检查显式暂停、隐藏页可聚焦元素、长内容与读屏次序 |
| Staggered Menu / 源码 | 开关按钮 → open → 分层滑入与错峰链接 → 开关或配置的外点关闭 | GSAP；有 aria-expanded/aria-hidden。本次 TS-CSS 抽查未见 Escape、焦点转移/返回、隐藏链接 inert 或减少动效分支。补充：按导航或模态语义补齐，不直接替代业务抽屉 |

### 固定源码链接

每个链接指向本次抽查变体。源码变化时重新查看，不用本表猜测新 API。

- [Animated Content](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Animations/AnimatedContent/AnimatedContent.tsx)、[Fade Content](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Animations/FadeContent/FadeContent.tsx)、[Click Spark](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Animations/ClickSpark/ClickSpark.tsx)、[Magnet](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Animations/Magnet/Magnet.tsx)。
- [Animated List](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Components/AnimatedList/AnimatedList.tsx)、[Stepper](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Components/Stepper/Stepper.tsx)、[Carousel](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Components/Carousel/Carousel.tsx)、[Staggered Menu](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Components/StaggeredMenu/StaggeredMenu.tsx)。
- [Glide Select](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/GlideSelect/GlideSelect.tsx)、[Spring Check](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/SpringCheck/SpringCheck.tsx)、[Squish Switch](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/SquishSwitch/SquishSwitch.tsx)、[Warm Tooltip](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/WarmTooltip/WarmTooltip.tsx)。
- [Status Mark](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/StatusMark/StatusMark.tsx)、[Swipe Toast](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/SwipeToast/SwipeToast.tsx)、[Fuse Button](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/FuseButton/FuseButton.tsx)、[Hold Button](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/HoldButton/HoldButton.tsx)、[Slide Commit](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/SlideCommit/SlideCommit.tsx)。

## 同屏预算与降级

先选择需要解释的状态或主视觉区域，再给装饰分配预算。复杂效果不要同屏堆叠：背景粒子、流体指针、3D 卡片和大量逐项入场会叠加成本；优先保留最能服务任务的一项，其余使用简单过渡或静态形态。这是选择原则，不是限制为固定组件数。

- 阅读所选源码，识别持续 requestAnimationFrame、Canvas/WebGL、物理求解、大面积 blur/filter、多个媒体实例和长列表逐项监听；不能只凭包体积或“无依赖”判断便宜。
- 把较重组件放到明确区域，按需加载、限制活跃实例、离屏暂停或卸载；卸载清理定时器、observer、事件及图形资源。读取现有实现后补缺口，不叠加重复全局监听器。
- 减少动效、触屏/粗指针或较弱设备上保留静态最终状态与基本操作。没有指针时不要求拖曳或 hover 才能访问关键内容。WebGL/素材加载失败应有静态替代。
- 用实际素材、目标分辨率与设备检查滚动、输入和主要操作；与效果关闭时比较。必要时降低粒子数量、分辨率/像素比、透明叠层或同时可见实例。没有测量时写“待运行验证”，不写帧率达标。
- 组件带 reduced-motion 分支不等于所有动画都停，也不证明系统偏好运行中切换可即时生效。验证最终效果、业务时序和可读性；不能因关闭动效跳过真实请求。

## 来源与分发边界

本次读取的 [LICENSE.md](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/LICENSE.md) 标识为 MIT + Commons Clause，并要求保留版权/许可声明；它对组件、工具、音效及单独导出包的再分发设有限制。接入目标应用时重新核对当前文件与具体资源的附带声明，保留必要署名。本 skill 分发原创方法、名称索引和官方链接；不内置上游组件库、工具、音效或整批导出资源供二次分发。原网页、许可快照与选中源码只进入项目研究档案，不进入 skill 分发包。

交接写清：所选组件与变体、来源提交/取得日期、目标文件、依赖变动、token 映射、补足行为、同屏预算和实测范围。外部网站暂不可用时保留已有实现或按本模块规则完成必要行为，说明未能取得的组件；不虚构已安装、已运行或已授权的 Pro 内容。

