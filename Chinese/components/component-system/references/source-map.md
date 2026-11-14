# 来源地图与证据范围

研究快照：2026-11-14。只打开当前组件任务相关来源。此地图用于辅助选择，不是强制依赖清单。用户所说的克制、细腻、成熟、抓眼、未来感是研究方向，不是通用视觉默认。

第一版检查了官方页面、部分文档和部分官方源码接口，并在浏览器中观察了 Bencho、HeroUI、beUI 首页外观。这不证明组件运行行为。没有安装第三方库或执行其示例，也未完成全面键盘、辅助技术、音频、图形或性能测试。实现前重查已安装版本。详细研究及用户提供的七张图片保留在制作档案中。

## 组件与风格参考

| 来源与抽样证据 | 可借鉴内容 | 局限或采用边界 |
| --- | --- | --- |
| [BoardUI Button](https://www.boardui.com/components/button)、[Data Table](https://www.boardui.com/components/data-table) | 尺寸/图标/间距联动；表格基础组件与选择、标签、分页组合；常规/紧凑密度 | 来源像素值与技术栈仅作实例，不是全局默认；未运行行为 |
| [Bencho Copy field](https://bencho.dev/blocks/copy-field)、[Status picker](https://bencho.dev/blocks/status-picker)、[Form error](https://bencho.dev/blocks/form-error) | 局部结果反馈、当前值的连续性、字段附近的错误说明 | 简述说明意图，未验证完整 props 与恢复行为 |
| [HeroUI Button](https://heroui.com/en/docs/react/components/button)、[Select](https://heroui.com/en/docs/react/components/select) | 分开的外观/尺寸/状态维度、可组合结构与受控状态 | 当前文档不保证旧版已安装 API 与之相同 |
| [beUI Card](https://beui.dev/components/motion/card)、[Select](https://beui.dev/components/motion/select) | Header/body/footer 组合、密度相关间距、值与展开状态分开 | 仅阅读部分源码，未执行；视觉选中态仍需可操作语义 |
| [Libraries.dev](https://libraries.dev/)、[accessibility](https://libraries.dev/accessibility) | AI 状态视觉候选，以及装饰渲染与 DOM/文字分离 | 减少动态效果/性能描述是发布者声明，不是本模块测试结果 |
| [Watermelon buttons](https://ui.watermelon.sh/animated-components/category/buttons) | 比较外观前先区分执行、开关、分裂式操作和撤销任务 | 检查到分类层，不代表验证了全部所列组件 |
| [Uiverse](https://uiverse.io/) | 单个控件、表面与反馈方向候选 | 社区作品须分别核对 API、主题、行为及复用条款 |
| [Aceternity Stateful Button](https://ui.aceternity.com/components/stateful-button)、[Expandable Cards](https://ui.aceternity.com/components/expandable-card) | 局部动作反馈与展开详情结构 | 展示导向默认值需限定范围；缺少真实失败/取消/焦点处理时补齐 |
| [Rare UI Delete button](https://www.rareui.com/components/deletebutton)、[OTP Input](https://www.rareui.com/components/otpinput) | 确认与完成不同；输入填满与服务端验证不同；尺寸联动 | 本包不再分发源码。核查实际复用条款；漂亮的确认效果不能覆盖按风险进行的浮层选型 |

## 企业与平台参考

| 来源与抽样证据 | 可借鉴内容 | 局限或采用边界 |
| --- | --- | --- |
| [JD UDCDesign](https://findesign.jd.com/) | 组件/主题资源的官方研究入口 | 直接读取返回客户端外壳，未验证组件 API 及当前维护状态；不擅自以 NutUI 替代 |
| [Ant Button](https://ant.design/components/button/)、[Table](https://ant.design/components/table/)、[主题定制](https://ant.design/docs/react/customize-theme/) | 用途明确的维度、稳定行键和清楚的数据状态、主题/provider 接入 | 核对安装版本及静态浮层/消息上下文，不盲用当前 API |
| [Arco 官方 Button 接口](https://github.com/arco-design/arco-design/blob/main/components/Button/interface.ts) | 用途/status/size/shape 分开选择 | 组件站没有可读正文，改读官方源码；分支源码不等于安装版本 |
| [TDesign API 约定](https://github.com/Tencent/tdesign/wiki/component-api-guide)、[Button 接口](https://github.com/Tencent/tdesign-vue-next/blob/develop/packages/components/button/type.ts) | 语义一致、语法顺应框架；视觉 theme 与原生按钮 type 分开 | 将用户“TD design”理解为腾讯 TDesign；站点外壳不可读时使用官方源码替代 |
| [Element Plus Select](https://element-plus.org/en-US/component/select.html)、[主题定制](https://element-plus.org/en-US/guide/theming.html) | 稳定值标识、远程查询状态、插槽与已有主题机制 | 研究的是 Element Plus，不混用 Vue 2 的 Element UI API |
| [Semi Form](https://semi.design/en-US/input/form) | Field 封装将值/事件、标签、帮助、错误接入表单系统 | 以可读官方内容/索引摘录补充失败的分页读取，并非完整表单或 token 审查 |
| [Apple Design Resources](https://developer.apple.com/design/resources/)、[Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) | 内容/样式/角色区分，可见响应与可用操作区域 | 平台指导有适用条件，平台单位不转换成通用 CSS 尺寸 |
| [Atlassian Button usage](https://atlassian.design/components/button/usage) | 标签/操作区域/图标组成，操作与导航区分，优先级和有帮助的校验 | 具体工作流约定是待评估方案，不强制适用所有产品 |

## 用户图片中的来源

| 来源 | 在组件任务中的用途 | 边界 |
| --- | --- | --- |
| [21st Split Button](https://21st.dev/@shugar/components/split-button)、[Icon Label Subtext Button](https://21st.dev/@ruixen.ui/components/icon-label-subtext-button) | 发现组合方式，检查动作与次级信息如何分开 | 多作者目录；部分完整源码需要账号。用法示例不证明实现行为 |
| [Paper Fluted Glass](https://shaders.paper.design/fluted-glass)、[Pulsing Border](https://shaders.paper.design/pulsing-border) | 可选材质/边框层；文档中的静态渲染参数 | 效果不等于组件语义，实际降级与图形开销需要测试 |
| [Cuelume docs](https://cuelume.dev/docs) | 可选事件/结果音效、有作用域的绑定、清理及应用偏好 | 未试听或测试音频；静音/音频受阻时仍需完整反馈 |
| [Brand Archive](https://brandarchive.xyz/) | 向全局风格负责人提供品牌语言研究 | 直接读取返回 403，只检查用户图片与官方搜索索引 |
| [Minimal Gallery](https://minimal.gallery/) | 所选页面与组合方式的灵感 | 画廊不提供公共组件 API，也不保证所有案例同一风格 |
| [Footer](https://www.footer.design/sites/the-content-architecture) | 链接分组、订阅字段/操作和元信息组合 | 信息结构由页面主力负责，实际目的地与响应式行为须检查 |
| [Happy Hues](https://www.happyhues.co/palettes/4) | 在用途角色及真实组件上下文中评价配色 | 配色案例不是经过验证的对比度结果，也不是已选项目品牌 |

图片中的奶油色背景、衬线标题和倾斜展示框属于展示包装，不是已采纳的组件规则。保留链接与原创归纳，不再分发第三方源码或完整手册。网站的复制/安装 prompt 不代表获准运行命令或替换项目技术栈。
