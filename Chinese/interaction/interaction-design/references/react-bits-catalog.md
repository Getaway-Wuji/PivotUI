# React Bits 公开组件选型索引

仅在需要寻找候选组件时读取对应类别；接入步骤与已抽查边界见 [React Bits 接入](react-bits.md)。

核对日期：2026-11-14。官网公开目录 **216 项**：文字 33、动效 38、组件 48、Micro 34、背景 63。名称、分类和链接来自[官网目录](https://reactbits.dev/get-started/index)，与固定提交 `4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce` 的 [Categories.js](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/constants/Categories.js) 逐项核对一致。公开组件在该提交的注册表中均有 JS-CSS / JS-TW / TS-CSS / TS-TW 四种条目。此表为全量**发现索引**，不表示每项已运行或已通过可访问性与性能检查。

“用途”和“成本信号”是本模块原创选型建议。E＝优先作为单次事件/局部状态动画考察；D＝可能持续更新，或随滚动/指针更新；G＝优先检查 Canvas/WebGL/3D/物理/大面积绘制成本。标签是启发式，**不是测量结论，也不承诺某组件的实现引擎**；E 也可能因大列表或资源而变重。实际成本由所选变体源码、参数、素材、分辨率、同屏活跃实例及设备决定。

复杂组件集中在关键区域，不同时铺满多个区域；选中后确认按需加载、离屏暂停或卸载、无交互时休眠和静态降级。数量不设为官方固定标准，以目标设备运行结果收紧预算。背景类默认交给页面主力确认适用区域；业务控件优先 Micro，再考虑通用动效包装。

查找顺序：Micro → Components → Animations → Text Animations → Backgrounds。表内保留官网分类顺序，避免误认为本模块限制了用户可选组件。每次实际使用重新读取目标页 Code/Props 与当前 LICENSE。

## Text Animations · 33

| 官方组件 | 本模块用途建议 | 成本信号 |
| --- | --- | --- |
| [Tech Text](https://reactbits.dev/text-animations/tech-text) | 标志字指针强调 | D |
| [Text Loop](https://reactbits.dev/text-animations/text-loop) | 弧线路径滚动字 | D |
| [Masked Heading](https://reactbits.dev/text-animations/masked-heading) | 标题遮罩揭示 | D |
| [Particle Text](https://reactbits.dev/text-animations/particle-text) | 粒子标题展示 | G |
| [Split Flap Text](https://reactbits.dev/text-animations/split-flap-text) | 翻牌文字播报 | E |
| [Warp Text](https://reactbits.dev/text-animations/warp-text) | 指针扭曲标题 | G |
| [Stroke Text](https://reactbits.dev/text-animations/stroke-text) | 描边标题揭示 | E |
| [Depth Text](https://reactbits.dev/text-animations/depth-text) | 立体字指针响应 | D |
| [Fold Text](https://reactbits.dev/text-animations/fold-text) | 折叠文字入场 | E |
| [Echo Text](https://reactbits.dev/text-animations/echo-text) | 文字残影入场 | E |
| [Split Text](https://reactbits.dev/text-animations/split-text) | 分字分词入场 | E |
| [Blur Text](https://reactbits.dev/text-animations/blur-text) | 文字清晰化入场 | E |
| [Circular Text](https://reactbits.dev/text-animations/circular-text) | 圆形字装饰 | D |
| [Text Type](https://reactbits.dev/text-animations/text-type) | 逐字输出展示 | D |
| [Shuffle](https://reactbits.dev/text-animations/shuffle) | 字形重排揭示 | E |
| [Shiny Text](https://reactbits.dev/text-animations/shiny-text) | 高光标题装饰 | D |
| [Text Pressure](https://reactbits.dev/text-animations/text-pressure) | 可变字形互动 | D |
| [Curved Loop](https://reactbits.dev/text-animations/curved-loop) | 曲线跑马灯 | D |
| [Fuzzy Text](https://reactbits.dev/text-animations/fuzzy-text) | 噪化标题装饰 | G |
| [Gradient Text](https://reactbits.dev/text-animations/gradient-text) | 渐变标题装饰 | D |
| [Falling Text](https://reactbits.dev/text-animations/falling-text) | 文字物理试玩 | G |
| [Text Cursor](https://reactbits.dev/text-animations/text-cursor) | 指针文字尾迹 | D |
| [Decrypted Text](https://reactbits.dev/text-animations/decrypted-text) | 解码式揭示 | E |
| [True Focus](https://reactbits.dev/text-animations/true-focus) | 词组聚焦展示 | D |
| [Scroll Float](https://reactbits.dev/text-animations/scroll-float) | 滚动文字层次 | D |
| [Scroll Reveal](https://reactbits.dev/text-animations/scroll-reveal) | 滚动阅读揭示 | D |
| [ASCII Text](https://reactbits.dev/text-animations/ascii-text) | 字符化标题特效 | G |
| [Scrambled Text](https://reactbits.dev/text-animations/scrambled-text) | 指针文字扰动 | D |
| [Rotating Text](https://reactbits.dev/text-animations/rotating-text) | 轮换短句展示 | D |
| [Glitch Text](https://reactbits.dev/text-animations/glitch-text) | 故障文字装饰 | D |
| [Scroll Velocity](https://reactbits.dev/text-animations/scroll-velocity) | 滚动速度叙事 | D |
| [Variable Proximity](https://reactbits.dev/text-animations/variable-proximity) | 近邻字形反馈 | D |
| [Count Up](https://reactbits.dev/text-animations/count-up) | 指标数值过渡 | E |

## Animations · 38

| 官方组件 | 本模块用途建议 | 成本信号 |
| --- | --- | --- |
| [Crystalized Ball](https://reactbits.dev/animations/crystalized-ball) | 球形视觉焦点 | G |
| [Electric Logo](https://reactbits.dev/animations/electric-logo) | 品牌标志电光 | G |
| [Dither Veil](https://reactbits.dev/animations/dither-veil) | 图片局部显色 | G |
| [Glow Cursor](https://reactbits.dev/animations/glow-cursor) | 指针光迹 | G |
| [Scroll Expand](https://reactbits.dev/animations/scroll-expand) | 滚动媒体扩展 | D |
| [Ripple Distortion](https://reactbits.dev/animations/ripple-distortion) | 图片波纹互动 | G |
| [Elastic Mesh](https://reactbits.dev/animations/elastic-mesh) | 品牌形状软体试玩 | G |
| [Swarm Cursor](https://reactbits.dev/animations/swarm-cursor) | 群体指针特效 | G |
| [Halftone Reveal](https://reactbits.dev/animations/halftone-reveal) | 网点图片揭示 | G |
| [Pixel Swap](https://reactbits.dev/animations/pixel-swap) | 卡片内容替换 | G |
| [Cursor Grid](https://reactbits.dev/animations/cursor-grid) | 指针网格装饰 | G |
| [Animated Content](https://reactbits.dev/animations/animated-content) | 内容进场层次 | E |
| [Fade Content](https://reactbits.dev/animations/fade-content) | 轻量显隐候选 | E |
| [Electric Border](https://reactbits.dev/animations/electric-border) | 电光边框强调 | G |
| [Orbit Images](https://reactbits.dev/animations/orbit-images) | 轨道图片展示 | D |
| [Pixel Transition](https://reactbits.dev/animations/pixel-transition) | 像素内容过渡 | G |
| [Glare Hover](https://reactbits.dev/animations/glare-hover) | 卡面掠光反馈 | D |
| [Logo Loop](https://reactbits.dev/animations/logo-loop) | 品牌标志滚动带 | D |
| [Target Cursor](https://reactbits.dev/animations/target-cursor) | 自定义指针目标 | D |
| [Laser Flow](https://reactbits.dev/animations/laser-flow) | 区域光束装饰 | G |
| [Ghost Cursor](https://reactbits.dev/animations/ghost-cursor) | 烟雾指针特效 | G |
| [Gradual Blur](https://reactbits.dev/animations/gradual-blur) | 滚动边缘层次 | D |
| [Click Spark](https://reactbits.dev/animations/click-spark) | 单次点击装饰 | G |
| [Magnet](https://reactbits.dev/animations/magnet) | 主操作磁吸强调 | D |
| [Strands](https://reactbits.dev/animations/strands) | 语音主题视觉 | G |
| [Sticker Peel](https://reactbits.dev/animations/sticker-peel) | 贴纸拖曳试玩 | G |
| [Pixel Trail](https://reactbits.dev/animations/pixel-trail) | 像素指针尾迹 | G |
| [Cubes](https://reactbits.dev/animations/cubes) | 立方体互动墙 | G |
| [Metallic Paint](https://reactbits.dev/animations/metallic-paint) | 金属品牌视觉 | G |
| [Noise](https://reactbits.dev/animations/noise) | 背景颗粒质感 | G |
| [Shape Blur](https://reactbits.dev/animations/shape-blur) | 形状模糊互动 | G |
| [Crosshair](https://reactbits.dev/animations/crosshair) | 坐标指针装饰 | D |
| [Image Trail](https://reactbits.dev/animations/image-trail) | 图片指针尾迹 | D |
| [Ribbons](https://reactbits.dev/animations/ribbons) | 飘带指针装饰 | G |
| [Splash Cursor](https://reactbits.dev/animations/splash-cursor) | 流体指针特效 | G |
| [Meta Balls](https://reactbits.dev/animations/meta-balls) | 液态形状展示 | G |
| [Blob Cursor](https://reactbits.dev/animations/blob-cursor) | 团状指针特效 | G |
| [Star Border](https://reactbits.dev/animations/star-border) | 边缘亮点装饰 | D |

## Components · 48

| 官方组件 | 本模块用途建议 | 成本信号 |
| --- | --- | --- |
| [Holo Card](https://reactbits.dev/components/holo-card) | 收藏卡展示 | G |
| [Circular Carousel](https://reactbits.dev/components/circular-carousel) | 环形媒体浏览 | G |
| [Flex Carousel](https://reactbits.dev/components/flex-carousel) | 横向媒体展示 | G |
| [Infinite Spiral](https://reactbits.dev/components/infinite-spiral) | 螺旋媒体展厅 | G |
| [Depth Carousel](https://reactbits.dev/components/depth-carousel) | 纵深内容浏览 | G |
| [Morph Slider](https://reactbits.dev/components/morph-slider) | 图片过渡展示 | G |
| [Drift Wall](https://reactbits.dev/components/drift-wall) | 流动媒体墙 | G |
| [Accordion Gallery](https://reactbits.dev/components/accordion-gallery) | 分栏媒体探索 | D |
| [Specular Button](https://reactbits.dev/components/specular-button) | 重点按钮材质 | D |
| [Option Wheel](https://reactbits.dev/components/option-wheel) | 紧凑选项选择 | E |
| [Curved Input](https://reactbits.dev/components/curved-input) | 特色输入展示 | D |
| [Line Sidebar](https://reactbits.dev/components/line-sidebar) | 侧栏近邻强调 | D |
| [Animated List](https://reactbits.dev/components/animated-list) | 可选择短列表 | E |
| [Scroll Stack](https://reactbits.dev/components/scroll-stack) | 滚动卡片叙事 | D |
| [Bubble Menu](https://reactbits.dev/components/bubble-menu) | 品牌导航展开 | E |
| [Magic Bento](https://reactbits.dev/components/magic-bento) | 功能卡片展示 | G |
| [Circular Gallery](https://reactbits.dev/components/circular-gallery) | 沉浸图片浏览 | G |
| [Reflective Card](https://reactbits.dev/components/reflective-card) | 人物证件展示 | G |
| [Card Nav](https://reactbits.dev/components/card-nav) | 分组导航展开 | E |
| [Stack](https://reactbits.dev/components/stack) | 卡堆媒体浏览 | D |
| [Fluid Glass](https://reactbits.dev/components/fluid-glass) | 折射品牌展示 | G |
| [Pill Nav](https://reactbits.dev/components/pill-nav) | 胶囊导航强调 | E |
| [Tilted Card](https://reactbits.dev/components/tilted-card) | 卡片指针倾斜 | D |
| [Masonry](https://reactbits.dev/components/masonry) | 图片网格浏览 | D |
| [Glass Surface](https://reactbits.dev/components/glass-surface) | 玻璃容器材质 | G |
| [Dome Gallery](https://reactbits.dev/components/dome-gallery) | 沉浸图片展厅 | G |
| [Chroma Grid](https://reactbits.dev/components/chroma-grid) | 人物卡片聚焦 | G |
| [Folder](https://reactbits.dev/components/folder) | 文件夹内容预览 | E |
| [Staggered Menu](https://reactbits.dev/components/staggered-menu) | 品牌导航演出 | E |
| [Model Viewer](https://reactbits.dev/components/model-viewer) | 产品三维展示 | G |
| [Lanyard](https://reactbits.dev/components/lanyard) | 可拖曳身份牌 | G |
| [Profile Card](https://reactbits.dev/components/profile-card) | 人物品牌卡片 | D |
| [Dock](https://reactbits.dev/components/dock) | 应用快捷入口 | E |
| [Gooey Nav](https://reactbits.dev/components/gooey-nav) | 导航选中迁移 | E |
| [Pixel Card](https://reactbits.dev/components/pixel-card) | 像素卡片强调 | G |
| [Carousel](https://reactbits.dev/components/carousel) | 少量内容轮播 | E |
| [Spotlight Card](https://reactbits.dev/components/spotlight-card) | 卡面指针聚焦 | D |
| [Border Glow](https://reactbits.dev/components/border-glow) | 边界光照强调 | G |
| [Flying Posters](https://reactbits.dev/components/flying-posters) | 海报浏览叙事 | G |
| [Card Swap](https://reactbits.dev/components/card-swap) | 自动卡片展示 | D |
| [Glass Icons](https://reactbits.dev/components/glass-icons) | 图标入口展示 | D |
| [Decay Card](https://reactbits.dev/components/decay-card) | 图片破碎特效 | G |
| [Flowing Menu](https://reactbits.dev/components/flowing-menu) | 品牌导航预览 | D |
| [Elastic Slider](https://reactbits.dev/components/elastic-slider) | 连续参数调节 | E |
| [Counter](https://reactbits.dev/components/counter) | 数值变化呈现 | E |
| [Infinite Menu](https://reactbits.dev/components/infinite-menu) | 球面内容探索 | G |
| [Stepper](https://reactbits.dev/components/stepper) | 多步任务外壳 | E |
| [Bounce Cards](https://reactbits.dev/components/bounce-cards) | 图片组入场 | E |

## Micro · 34

| 官方组件 | 本模块用途建议 | 成本信号 |
| --- | --- | --- |
| [Shredder](https://reactbits.dev/micro/shredder) | 删除过程视觉 | G |
| [Paper Crumple](https://reactbits.dev/micro/paper-crumple) | 纸张拟物试玩 | G |
| [Tear Ticket](https://reactbits.dev/micro/tear-ticket) | 票据撕除展示 | G |
| [Flip Card](https://reactbits.dev/micro/flip-card) | 双面卡内容切换 | E |
| [Branched Menu](https://reactbits.dev/micro/branched-menu) | 层级菜单展开 | E |
| [Folder Float](https://reactbits.dev/micro/folder-float) | 文件夹预览展开 | E |
| [Refine Frame](https://reactbits.dev/micro/refine-frame) | 生成阶段呈现 | E |
| [Thought Line](https://reactbits.dev/micro/thought-line) | 任务过程收拢 | E |
| [Voice Pill](https://reactbits.dev/micro/voice-pill) | 录音过程呈现 | E |
| [Slosh Gauge](https://reactbits.dev/micro/slosh-gauge) | 进度仪表呈现 | G |
| [Prompt Bar](https://reactbits.dev/micro/prompt-bar) | 对话输入工作区 | E |
| [Swipe Toast](https://reactbits.dev/micro/swipe-toast) | 轻量成功/信息通知，禁错误 | E |
| [Sling Button](https://reactbits.dev/micro/sling-button) | 拖曳发送演出 | E |
| [Bell Toggle](https://reactbits.dev/micro/bell-toggle) | 通知开关反馈 | E |
| [Call Chip](https://reactbits.dev/micro/call-chip) | 工具调用状态 | E |
| [Status Mark](https://reactbits.dev/micro/status-mark) | 异步任务状态 | E |
| [Glide Select](https://reactbits.dev/micro/glide-select) | 紧凑单项选择 | E |
| [Swipe Row](https://reactbits.dev/micro/swipe-row) | 行内快捷操作 | E |
| [Jelly Radio](https://reactbits.dev/micro/jelly-radio) | 互斥选项选择 | E |
| [Comet Dial](https://reactbits.dev/micro/comet-dial) | 角度参数调节 | E |
| [Wake Slider](https://reactbits.dev/micro/wake-slider) | 连续数值调节 | E |
| [Code Slots](https://reactbits.dev/micro/code-slots) | 验证码输入 | E |
| [Dodge Field](https://reactbits.dev/micro/dodge-field) | 趣味避让互动 | D |
| [Lattice Loader](https://reactbits.dev/micro/lattice-loader) | 等待状态呈现 | D |
| [Scrub Field](https://reactbits.dev/micro/scrub-field) | 拖曳数值输入 | E |
| [Fuse Button](https://reactbits.dev/micro/fuse-button) | 有撤销窗口操作 | E |
| [Warm Tooltip](https://reactbits.dev/micro/warm-tooltip) | 相关入口提示组 | E |
| [Slide Commit](https://reactbits.dev/micro/slide-commit) | 滑动确认操作 | E |
| [Rubber Segment](https://reactbits.dev/micro/rubber-segment) | 分段选项切换 | E |
| [Pulse Heart](https://reactbits.dev/micro/pulse-heart) | 点赞状态反馈 | E |
| [Spring Check](https://reactbits.dev/micro/spring-check) | 任务勾选反馈 | E |
| [Peek Rating](https://reactbits.dev/micro/peek-rating) | 离散评分选择 | E |
| [Hold Button](https://reactbits.dev/micro/hold-button) | 按住确认操作 | E |
| [Squish Switch](https://reactbits.dev/micro/squish-switch) | 二态设置切换 | E |

## Backgrounds · 63

| 官方组件 | 本模块用途建议 | 成本信号 |
| --- | --- | --- |
| [Gradient ASCII](https://reactbits.dev/backgrounds/gradient-ascii) | 字符渐变氛围 | G |
| [Flux Lines](https://reactbits.dev/backgrounds/flux-lines) | 流线氛围 | G |
| [Pattern Waves](https://reactbits.dev/backgrounds/pattern-waves) | 纹样波面氛围 | G |
| [Micro Slats](https://reactbits.dev/backgrounds/micro-slats) | 百叶波面氛围 | G |
| [Shape Waves](https://reactbits.dev/backgrounds/shape-waves) | 几何波面氛围 | G |
| [Aero Shards](https://reactbits.dev/backgrounds/aero-shards) | 玻璃碎片氛围 | G |
| [Ghost Fibers](https://reactbits.dev/backgrounds/ghost-fibers) | 纤维纵深氛围 | G |
| [CRT Warp](https://reactbits.dev/backgrounds/crt-warp) | 复古屏幕氛围 | G |
| [Molten Metal](https://reactbits.dev/backgrounds/molten-metal) | 熔融金属氛围 | G |
| [Gradient Waves](https://reactbits.dev/backgrounds/gradient-waves) | 渐变波面氛围 | G |
| [Web Threads](https://reactbits.dev/backgrounds/web-threads) | 网状发光氛围 | G |
| [Topography](https://reactbits.dev/backgrounds/topography) | 等高线地形氛围 | G |
| [Light Tunnel](https://reactbits.dev/backgrounds/light-tunnel) | 光隧道氛围 | G |
| [Sliced Waves](https://reactbits.dev/backgrounds/sliced-waves) | 分片波浪氛围 | G |
| [Acid Squares](https://reactbits.dev/backgrounds/acid-squares) | 方格光面氛围 | G |
| [Scanner](https://reactbits.dev/backgrounds/scanner) | 扫描纹理氛围 | G |
| [Ferrofluid](https://reactbits.dev/backgrounds/ferrofluid) | 磁性流体氛围 | G |
| [Lightfall](https://reactbits.dev/backgrounds/lightfall) | 下落光线氛围 | G |
| [Liquid Ether](https://reactbits.dev/backgrounds/liquid-ether) | 液态空间氛围 | G |
| [Prism](https://reactbits.dev/backgrounds/prism) | 棱镜几何氛围 | G |
| [Dark Veil](https://reactbits.dev/backgrounds/dark-veil) | 暗色光幕氛围 | G |
| [Light Pillar](https://reactbits.dev/backgrounds/light-pillar) | 光柱空间氛围 | G |
| [Antigravity](https://reactbits.dev/backgrounds/antigravity) | 反重力粒子氛围 | G |
| [Silk](https://reactbits.dev/backgrounds/silk) | 丝绸纹理氛围 | G |
| [Floating Lines](https://reactbits.dev/backgrounds/floating-lines) | 漂浮细线氛围 | G |
| [Side Rays](https://reactbits.dev/backgrounds/side-rays) | 侧向光照氛围 | G |
| [Light Rays](https://reactbits.dev/backgrounds/light-rays) | 边缘光束氛围 | G |
| [Pixel Blast](https://reactbits.dev/backgrounds/pixel-blast) | 像素云场氛围 | G |
| [Color Bends](https://reactbits.dev/backgrounds/color-bends) | 曲面色带氛围 | G |
| [Line Waves](https://reactbits.dev/backgrounds/line-waves) | 线形波面氛围 | G |
| [Radar](https://reactbits.dev/backgrounds/radar) | 雷达主题氛围 | G |
| [Soft Aurora](https://reactbits.dev/backgrounds/soft-aurora) | 柔和极光氛围 | G |
| [Magic Rings](https://reactbits.dev/backgrounds/magic-rings) | 同心光环氛围 | G |
| [Aurora](https://reactbits.dev/backgrounds/aurora) | 极光横幕氛围 | G |
| [Plasma](https://reactbits.dev/backgrounds/plasma) | 等离子色面氛围 | G |
| [Plasma Wave](https://reactbits.dev/backgrounds/plasma-wave) | 双带光波氛围 | G |
| [Particles](https://reactbits.dev/backgrounds/particles) | 空间粒子氛围 | G |
| [Gradient Blinds](https://reactbits.dev/backgrounds/gradient-blinds) | 渐变百叶氛围 | G |
| [Grainient](https://reactbits.dev/backgrounds/grainient) | 颗粒渐变氛围 | G |
| [Grid Scan](https://reactbits.dev/backgrounds/grid-scan) | 网格空间扫描 | G |
| [Beams](https://reactbits.dev/backgrounds/beams) | 条带高光氛围 | G |
| [Pixel Snow](https://reactbits.dev/backgrounds/pixel-snow) | 像素雪景氛围 | G |
| [Lightning](https://reactbits.dev/backgrounds/lightning) | 闪电主题氛围 | G |
| [Prismatic Burst](https://reactbits.dev/backgrounds/prismatic-burst) | 棱光放射氛围 | G |
| [Galaxy](https://reactbits.dev/backgrounds/galaxy) | 星空航行氛围 | G |
| [Dither](https://reactbits.dev/backgrounds/dither) | 抖色纹样氛围 | G |
| [Faulty Terminal](https://reactbits.dev/backgrounds/faulty-terminal) | 终端故障氛围 | G |
| [Ripple Grid](https://reactbits.dev/backgrounds/ripple-grid) | 涟漪网格氛围 | G |
| [Dot Field](https://reactbits.dev/backgrounds/dot-field) | 点阵透镜氛围 | G |
| [Dot Grid](https://reactbits.dev/backgrounds/dot-grid) | 弹性点阵互动 | G |
| [Threads](https://reactbits.dev/backgrounds/threads) | 流动线束氛围 | G |
| [Hyperspeed](https://reactbits.dev/backgrounds/hyperspeed) | 高速轨迹叙事 | G |
| [Iridescence](https://reactbits.dev/backgrounds/iridescence) | 彩虹光泽氛围 | G |
| [Waves](https://reactbits.dev/backgrounds/waves) | 连线波浪氛围 | G |
| [Magnet Lines](https://reactbits.dev/backgrounds/magnet-lines) | 磁性线条互动 | G |
| [Grid Distortion](https://reactbits.dev/backgrounds/grid-distortion) | 图片网格扰动 | G |
| [Ballpit](https://reactbits.dev/backgrounds/ballpit) | 球体物理试玩 | G |
| [Orb](https://reactbits.dev/backgrounds/orb) | 环形能量氛围 | G |
| [Letter Glitch](https://reactbits.dev/backgrounds/letter-glitch) | 文字纹理氛围 | G |
| [Grid Motion](https://reactbits.dev/backgrounds/grid-motion) | 漂移图片墙 | G |
| [Shape Grid](https://reactbits.dev/backgrounds/shape-grid) | 几何网格氛围 | G |
| [Liquid Chrome](https://reactbits.dev/backgrounds/liquid-chrome) | 液态铬光氛围 | G |
| [Balatro](https://reactbits.dev/backgrounds/balatro) | 复古游戏氛围 | G |

## 目录外条目与工具

本次固定提交的注册表还有 `EvilEye` 和 `FlyingButton` 的四种 UI 变体，但官网公开 216 项目录没有列入它们。仅作为[注册表附加候选](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/public/r/registry.json)保留；使用时重新确认公开文档、源码和支持状态，不混入本表数量。不要因组件名推定稳定 API。

官网还提供 [Background Studio](https://reactbits.dev/tools/background-studio)、[Center Stage](https://reactbits.dev/tools/center-stage)、[Shape Magic](https://reactbits.dev/tools/shape-magic)、[Texture Lab](https://reactbits.dev/tools/texture-lab)、[Sound Lab](https://reactbits.dev/tools/sound-lab)。它们是创作工具；注册表的音效及 SoundEngine 属于音频能力，不计入动画 UI 组件数量。仅在任务要求素材或音效时进一步研究，默认不为界面添加声音。[Pro](https://pro.reactbits.dev/) 是另一套付费内容，本首版未收集其私有资源。

## 更新方式

先重新核对官网目录，再比对仓库 Categories、registry 和需要使用的源码。新增条目补入正确类别；改名保留迁移说明；失效条目标记状态而非猜测替代路径。记录核对日期、固定提交、实际抽查范围；不要把旧快照称为实时全库。分发只带本索引与接入规则，不携带整套上游组件源码、原网页或工具导出素材包。

