# 自有交互模板

只有目标项目缺少合适组件或需要行为适配时复制相应文件。现有组件优先；这些是无样式的 React + TypeScript 行为起点，不是完整组件库，不包含 React Bits 源码或默认品牌。非 React 项目沿用原栈，按规则实现即可。

## 文件与接口

- [AsyncActionButton.tsx](react/AsyncActionButton.tsx)：原生 `type="button"`，`onAction` 返回实际操作的 Promise；同步守卫防止同一实例在下一次渲染前重复激活。`busy` 可接外部请求状态；等待使用 `aria-disabled` 而不移除键盘焦点。`disabled` 用于确实不可操作的原生禁用状态。`onRejected` 由业务层呈现字段错误或持久 Alert。
- [Feedback.tsx](react/Feedback.tsx)：`ToastNotice` 仅接受 `success` / `info`，用于无需处理的轻量结果；`PersistentAlert` 用于同步失败、网络错误等持续提醒，可通过 `action` 接入异步重试按钮。字段错误仍应贴近字段，不必全部转为 Alert。

按钮等待结束只表示返回的 Promise 已结束。请求身份、幂等、结果未知、保存快照和新草稿由业务层管理；本模板不自动宣布成功、不回滚数据、不重试、不把卸载当成服务端取消。错误回调可能在组件卸载后到达，应绑定操作身份并交仍有效的数据/反馈所有者处理。

表单提交不要只给按钮加此适配器：表单的 `onSubmit` 同样需要校验和防重复，并处理输入法组合状态。`label` 始终保留为可见动作名，等待时附加 `pendingLabel`，例如“保存（处理中…）”。可访问名称直接来自同一可见文字，不用固定 `aria-label` 覆盖它；重要阶段另外在现有状态区域反馈。

## Toast 的受控生命期

保持 `ToastNotice` 挂载，用 `visible` 和 `message` 更新已存在的礼貌播报区域。模板没有自动倒计时；由宿主在任务结束后的合适时机关闭，避免阅读时突然消失。如宿主增加自动关闭，需暂停悬停、键盘聚焦和页面隐藏期间的计时，并验证焦点与阅读时长。

关闭按钮获得焦点时，模板先调用必填 `restoreFocus` 再调用 `onDismiss`。宿主应把焦点放回原动作或有效后备位置；外部主动关闭且焦点位于 Toast 内时，也先执行这一安排。不要把未解决错误或待处理告警传入 `info` 绕过选型规则。

关闭状态保留空的播报节点，不要通过根节点 `display:none` 或 `hidden` 破坏其生命期。相同文案再次出现时，宿主按真实通知实例更新；实际播报仍需在目标辅助技术下检查。

## Alert、样式与适配

`PersistentAlert` 不设超时。消息持续到问题解决或目标流程明确替代它；重试失败仍保留消息，成功后由宿主更新实际问题状态。视觉上的 Alert 默认礼貌播报，只有需要及时打断的动态重要消息才选 `announcement="urgent"`。不自动移动输入焦点。标题层级可按目标页面调整，保留 `aria-labelledby` 对应关系。

用 `className` 及 `data-feedback` / `data-kind` / `data-pending` 映射目标项目现有 token、焦点环、尺寸和状态样式。模板没有内联品牌值；不要覆盖浏览器焦点提示而不提供可见替代。若需要 React Bits 动画，只在相应表现层接入已核对的组件，业务结果仍由宿主决定。

## 验证边界

本版本完成 TypeScript 类型检查和模拟 DOM 事件检查，覆盖等待防重复、失败后重试、焦点保留、受控 Toast 关闭与持久 Alert。模拟环境不证明浏览器原生键盘激活、读屏播报、视觉布局或性能；接入后按子模块验收目标界面。

实现参考：[React DOM 通用事件和属性](https://react.dev/reference/react-dom/components/common)、[React useId](https://react.dev/reference/react/useId)、[WAI Alert 模式](https://www.w3.org/WAI/ARIA/apg/patterns/alert/)。模板代码为本模块原创。
