# React Bits Public Component Selection Index

Read only the relevant category when finding candidates. See [React Bits integration](react-bits.md) for setup and inspected boundaries.

Checked 2026-11-14. The public catalog contains **216 entries**: 33 Text Animations, 38 Animations, 48 Components, 34 Micro, and 63 Backgrounds. Names, categories, and links come from the [official catalog](https://reactbits.dev/get-started/index) and were checked individually against [Categories.js](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/constants/Categories.js) at commit `4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce`. Each public component has JS-CSS / JS-TW / TS-CSS / TS-TW registry entries at that commit. This complete **discovery index** does not mean every component was run or passed accessibility/performance checks.

“Suggested use” and “cost signal” are original selection guidance. E = first inspect as single-event/local-state motion; D = may update continuously or with scrolling/pointer input; G = prioritize checking Canvas/WebGL/3D/physics/large-area drawing cost. These are heuristics, **not measurements or promises about implementation engines**. E can also become costly through large lists or resources. Actual cost depends on variant source, parameters, assets, resolution, active concurrent instances, and device.

Concentrate complex components in focal regions instead of filling several areas simultaneously. For selected items, establish lazy loading, offscreen pause/unmount, idle suspension, and static fallback. There is no official fixed-count limit here; tighten budgets based on target-device results. The page lead approves background regions. For business controls, inspect Micro before general animation wrappers.

Search order: Micro → Components → Animations → Text Animations → Backgrounds. Tables retain official category order to avoid implying a restriction on available choices. Re-read target Code/Props and current LICENSE whenever actually using a component.

## Text Animations · 33

| Official component | Suggested use in this module | Cost signal |
| --- | --- | --- |
| [Tech Text](https://reactbits.dev/text-animations/tech-text) | Pointer emphasis for display lettering | D |
| [Text Loop](https://reactbits.dev/text-animations/text-loop) | Curved-path scrolling text | D |
| [Masked Heading](https://reactbits.dev/text-animations/masked-heading) | Masked heading reveal | D |
| [Particle Text](https://reactbits.dev/text-animations/particle-text) | Particle heading display | G |
| [Split Flap Text](https://reactbits.dev/text-animations/split-flap-text) | Split-flap text announcements | E |
| [Warp Text](https://reactbits.dev/text-animations/warp-text) | Pointer-warped heading | G |
| [Stroke Text](https://reactbits.dev/text-animations/stroke-text) | Outline heading reveal | E |
| [Depth Text](https://reactbits.dev/text-animations/depth-text) | Pointer-responsive dimensional lettering | D |
| [Fold Text](https://reactbits.dev/text-animations/fold-text) | Folded text entrance | E |
| [Echo Text](https://reactbits.dev/text-animations/echo-text) | Text-trail entrance | E |
| [Split Text](https://reactbits.dev/text-animations/split-text) | Character/word entrance | E |
| [Blur Text](https://reactbits.dev/text-animations/blur-text) | Text sharpening entrance | E |
| [Circular Text](https://reactbits.dev/text-animations/circular-text) | Circular text decoration | D |
| [Text Type](https://reactbits.dev/text-animations/text-type) | Character-by-character display | D |
| [Shuffle](https://reactbits.dev/text-animations/shuffle) | Reordered-glyph reveal | E |
| [Shiny Text](https://reactbits.dev/text-animations/shiny-text) | Heading highlight decoration | D |
| [Text Pressure](https://reactbits.dev/text-animations/text-pressure) | Variable-letterform interaction | D |
| [Curved Loop](https://reactbits.dev/text-animations/curved-loop) | Curved marquee | D |
| [Fuzzy Text](https://reactbits.dev/text-animations/fuzzy-text) | Noisy heading decoration | G |
| [Gradient Text](https://reactbits.dev/text-animations/gradient-text) | Gradient heading decoration | D |
| [Falling Text](https://reactbits.dev/text-animations/falling-text) | Text physics exploration | G |
| [Text Cursor](https://reactbits.dev/text-animations/text-cursor) | Pointer text trail | D |
| [Decrypted Text](https://reactbits.dev/text-animations/decrypted-text) | Decoding-style reveal | E |
| [True Focus](https://reactbits.dev/text-animations/true-focus) | Phrase focus display | D |
| [Scroll Float](https://reactbits.dev/text-animations/scroll-float) | Scroll-driven text depth | D |
| [Scroll Reveal](https://reactbits.dev/text-animations/scroll-reveal) | Scroll reading reveal | D |
| [ASCII Text](https://reactbits.dev/text-animations/ascii-text) | Character-rendered heading effect | G |
| [Scrambled Text](https://reactbits.dev/text-animations/scrambled-text) | Pointer-driven text disturbance | D |
| [Rotating Text](https://reactbits.dev/text-animations/rotating-text) | Rotating short phrases | D |
| [Glitch Text](https://reactbits.dev/text-animations/glitch-text) | Glitch text decoration | D |
| [Scroll Velocity](https://reactbits.dev/text-animations/scroll-velocity) | Scroll-speed narrative | D |
| [Variable Proximity](https://reactbits.dev/text-animations/variable-proximity) | Proximity letterform feedback | D |
| [Count Up](https://reactbits.dev/text-animations/count-up) | Metric-value transition | E |

## Animations · 38

| Official component | Suggested use in this module | Cost signal |
| --- | --- | --- |
| [Crystalized Ball](https://reactbits.dev/animations/crystalized-ball) | Spherical visual focus | G |
| [Electric Logo](https://reactbits.dev/animations/electric-logo) | Electric brand-logo effect | G |
| [Dither Veil](https://reactbits.dev/animations/dither-veil) | Local image color reveal | G |
| [Glow Cursor](https://reactbits.dev/animations/glow-cursor) | Glowing pointer trail | G |
| [Scroll Expand](https://reactbits.dev/animations/scroll-expand) | Scroll-driven media expansion | D |
| [Ripple Distortion](https://reactbits.dev/animations/ripple-distortion) | Image ripple interaction | G |
| [Elastic Mesh](https://reactbits.dev/animations/elastic-mesh) | Soft-body brand-shape exploration | G |
| [Swarm Cursor](https://reactbits.dev/animations/swarm-cursor) | Swarming pointer effect | G |
| [Halftone Reveal](https://reactbits.dev/animations/halftone-reveal) | Halftone image reveal | G |
| [Pixel Swap](https://reactbits.dev/animations/pixel-swap) | Card-content replacement | G |
| [Cursor Grid](https://reactbits.dev/animations/cursor-grid) | Pointer-grid decoration | G |
| [Animated Content](https://reactbits.dev/animations/animated-content) | Content entrance hierarchy | E |
| [Fade Content](https://reactbits.dev/animations/fade-content) | Lightweight visibility candidate | E |
| [Electric Border](https://reactbits.dev/animations/electric-border) | Electric border emphasis | G |
| [Orbit Images](https://reactbits.dev/animations/orbit-images) | Orbiting image display | D |
| [Pixel Transition](https://reactbits.dev/animations/pixel-transition) | Pixel content transition | G |
| [Glare Hover](https://reactbits.dev/animations/glare-hover) | Card-surface glare feedback | D |
| [Logo Loop](https://reactbits.dev/animations/logo-loop) | Scrolling brand-logo strip | D |
| [Target Cursor](https://reactbits.dev/animations/target-cursor) | Custom targeting pointer | D |
| [Laser Flow](https://reactbits.dev/animations/laser-flow) | Regional beam decoration | G |
| [Ghost Cursor](https://reactbits.dev/animations/ghost-cursor) | Smoky pointer effect | G |
| [Gradual Blur](https://reactbits.dev/animations/gradual-blur) | Scroll-edge depth | D |
| [Click Spark](https://reactbits.dev/animations/click-spark) | Single-click decoration | G |
| [Magnet](https://reactbits.dev/animations/magnet) | Magnetic primary-action emphasis | D |
| [Strands](https://reactbits.dev/animations/strands) | Voice-themed visual | G |
| [Sticker Peel](https://reactbits.dev/animations/sticker-peel) | Draggable sticker exploration | G |
| [Pixel Trail](https://reactbits.dev/animations/pixel-trail) | Pixel pointer trail | G |
| [Cubes](https://reactbits.dev/animations/cubes) | Interactive cube wall | G |
| [Metallic Paint](https://reactbits.dev/animations/metallic-paint) | Metallic brand visual | G |
| [Noise](https://reactbits.dev/animations/noise) | Background grain texture | G |
| [Shape Blur](https://reactbits.dev/animations/shape-blur) | Shape-blur interaction | G |
| [Crosshair](https://reactbits.dev/animations/crosshair) | Coordinate pointer decoration | D |
| [Image Trail](https://reactbits.dev/animations/image-trail) | Image pointer trail | D |
| [Ribbons](https://reactbits.dev/animations/ribbons) | Ribbon pointer decoration | G |
| [Splash Cursor](https://reactbits.dev/animations/splash-cursor) | Fluid pointer effect | G |
| [Meta Balls](https://reactbits.dev/animations/meta-balls) | Liquid-shape display | G |
| [Blob Cursor](https://reactbits.dev/animations/blob-cursor) | Blob pointer effect | G |
| [Star Border](https://reactbits.dev/animations/star-border) | Edge-highlight decoration | D |

## Components · 48

| Official component | Suggested use in this module | Cost signal |
| --- | --- | --- |
| [Holo Card](https://reactbits.dev/components/holo-card) | Collectible-card presentation | G |
| [Circular Carousel](https://reactbits.dev/components/circular-carousel) | Circular media browsing | G |
| [Flex Carousel](https://reactbits.dev/components/flex-carousel) | Horizontal media presentation | G |
| [Infinite Spiral](https://reactbits.dev/components/infinite-spiral) | Spiral media gallery | G |
| [Depth Carousel](https://reactbits.dev/components/depth-carousel) | Browsing content in depth | G |
| [Morph Slider](https://reactbits.dev/components/morph-slider) | Image-transition display | G |
| [Drift Wall](https://reactbits.dev/components/drift-wall) | Flowing media wall | G |
| [Accordion Gallery](https://reactbits.dev/components/accordion-gallery) | Panel-based media exploration | D |
| [Specular Button](https://reactbits.dev/components/specular-button) | Material effect for focal buttons | D |
| [Option Wheel](https://reactbits.dev/components/option-wheel) | Compact option selection | E |
| [Curved Input](https://reactbits.dev/components/curved-input) | Expressive input display | D |
| [Line Sidebar](https://reactbits.dev/components/line-sidebar) | Sidebar proximity emphasis | D |
| [Animated List](https://reactbits.dev/components/animated-list) | Short selectable list | E |
| [Scroll Stack](https://reactbits.dev/components/scroll-stack) | Scroll-driven card narrative | D |
| [Bubble Menu](https://reactbits.dev/components/bubble-menu) | Brand-navigation expansion | E |
| [Magic Bento](https://reactbits.dev/components/magic-bento) | Feature-card presentation | G |
| [Circular Gallery](https://reactbits.dev/components/circular-gallery) | Immersive image browsing | G |
| [Reflective Card](https://reactbits.dev/components/reflective-card) | Identity-card presentation | G |
| [Card Nav](https://reactbits.dev/components/card-nav) | Grouped-navigation expansion | E |
| [Stack](https://reactbits.dev/components/stack) | Stacked-card media browsing | D |
| [Fluid Glass](https://reactbits.dev/components/fluid-glass) | Refractive brand presentation | G |
| [Pill Nav](https://reactbits.dev/components/pill-nav) | Pill-navigation emphasis | E |
| [Tilted Card](https://reactbits.dev/components/tilted-card) | Pointer-driven card tilt | D |
| [Masonry](https://reactbits.dev/components/masonry) | Image-grid browsing | D |
| [Glass Surface](https://reactbits.dev/components/glass-surface) | Glass container material | G |
| [Dome Gallery](https://reactbits.dev/components/dome-gallery) | Immersive image gallery | G |
| [Chroma Grid](https://reactbits.dev/components/chroma-grid) | Profile-card focus | G |
| [Folder](https://reactbits.dev/components/folder) | Folder-content preview | E |
| [Staggered Menu](https://reactbits.dev/components/staggered-menu) | Expressive brand navigation | E |
| [Model Viewer](https://reactbits.dev/components/model-viewer) | Three-dimensional product display | G |
| [Lanyard](https://reactbits.dev/components/lanyard) | Draggable identity badge | G |
| [Profile Card](https://reactbits.dev/components/profile-card) | Personal-brand card | D |
| [Dock](https://reactbits.dev/components/dock) | Application shortcuts | E |
| [Gooey Nav](https://reactbits.dev/components/gooey-nav) | Navigation selection transition | E |
| [Pixel Card](https://reactbits.dev/components/pixel-card) | Pixel card emphasis | G |
| [Carousel](https://reactbits.dev/components/carousel) | Small content carousel | E |
| [Spotlight Card](https://reactbits.dev/components/spotlight-card) | Pointer-focused card surface | D |
| [Border Glow](https://reactbits.dev/components/border-glow) | Illuminated border emphasis | G |
| [Flying Posters](https://reactbits.dev/components/flying-posters) | Poster-browsing narrative | G |
| [Card Swap](https://reactbits.dev/components/card-swap) | Automatic card presentation | D |
| [Glass Icons](https://reactbits.dev/components/glass-icons) | Icon-entry presentation | D |
| [Decay Card](https://reactbits.dev/components/decay-card) | Image-fragmentation effect | G |
| [Flowing Menu](https://reactbits.dev/components/flowing-menu) | Brand-navigation preview | D |
| [Elastic Slider](https://reactbits.dev/components/elastic-slider) | Continuous parameter adjustment | E |
| [Counter](https://reactbits.dev/components/counter) | Numeric-change display | E |
| [Infinite Menu](https://reactbits.dev/components/infinite-menu) | Spherical content exploration | G |
| [Stepper](https://reactbits.dev/components/stepper) | Multistep task shell | E |
| [Bounce Cards](https://reactbits.dev/components/bounce-cards) | Image-group entrance | E |

## Micro · 34

| Official component | Suggested use in this module | Cost signal |
| --- | --- | --- |
| [Shredder](https://reactbits.dev/micro/shredder) | Deletion-process visual | G |
| [Paper Crumple](https://reactbits.dev/micro/paper-crumple) | Paper-physics exploration | G |
| [Tear Ticket](https://reactbits.dev/micro/tear-ticket) | Ticket-tearing presentation | G |
| [Flip Card](https://reactbits.dev/micro/flip-card) | Two-sided card switching | E |
| [Branched Menu](https://reactbits.dev/micro/branched-menu) | Hierarchical menu expansion | E |
| [Folder Float](https://reactbits.dev/micro/folder-float) | Folder-preview expansion | E |
| [Refine Frame](https://reactbits.dev/micro/refine-frame) | Generation-phase display | E |
| [Thought Line](https://reactbits.dev/micro/thought-line) | Task-process summary transition | E |
| [Voice Pill](https://reactbits.dev/micro/voice-pill) | Recording-process display | E |
| [Slosh Gauge](https://reactbits.dev/micro/slosh-gauge) | Progress-gauge display | G |
| [Prompt Bar](https://reactbits.dev/micro/prompt-bar) | Conversational input workspace | E |
| [Swipe Toast](https://reactbits.dev/micro/swipe-toast) | Lightweight success/information; never errors | E |
| [Sling Button](https://reactbits.dev/micro/sling-button) | Expressive drag-to-send | E |
| [Bell Toggle](https://reactbits.dev/micro/bell-toggle) | Notification-toggle feedback | E |
| [Call Chip](https://reactbits.dev/micro/call-chip) | Tool-call status | E |
| [Status Mark](https://reactbits.dev/micro/status-mark) | Async-task state | E |
| [Glide Select](https://reactbits.dev/micro/glide-select) | Compact single selection | E |
| [Swipe Row](https://reactbits.dev/micro/swipe-row) | Inline row shortcuts | E |
| [Jelly Radio](https://reactbits.dev/micro/jelly-radio) | Mutually exclusive choices | E |
| [Comet Dial](https://reactbits.dev/micro/comet-dial) | Angle-parameter adjustment | E |
| [Wake Slider](https://reactbits.dev/micro/wake-slider) | Continuous-value adjustment | E |
| [Code Slots](https://reactbits.dev/micro/code-slots) | Verification-code input | E |
| [Dodge Field](https://reactbits.dev/micro/dodge-field) | Playful avoidance interaction | D |
| [Lattice Loader](https://reactbits.dev/micro/lattice-loader) | Waiting-state display | D |
| [Scrub Field](https://reactbits.dev/micro/scrub-field) | Draggable numeric input | E |
| [Fuse Button](https://reactbits.dev/micro/fuse-button) | Actions with undo windows | E |
| [Warm Tooltip](https://reactbits.dev/micro/warm-tooltip) | Related-entry hint groups | E |
| [Slide Commit](https://reactbits.dev/micro/slide-commit) | Slide-to-confirm action | E |
| [Rubber Segment](https://reactbits.dev/micro/rubber-segment) | Segmented-option switching | E |
| [Pulse Heart](https://reactbits.dev/micro/pulse-heart) | Like-state feedback | E |
| [Spring Check](https://reactbits.dev/micro/spring-check) | Task-completion check feedback | E |
| [Peek Rating](https://reactbits.dev/micro/peek-rating) | Discrete rating selection | E |
| [Hold Button](https://reactbits.dev/micro/hold-button) | Hold-to-confirm action | E |
| [Squish Switch](https://reactbits.dev/micro/squish-switch) | Binary-setting toggle | E |

## Backgrounds · 63

| Official component | Suggested use in this module | Cost signal |
| --- | --- | --- |
| [Gradient ASCII](https://reactbits.dev/backgrounds/gradient-ascii) | Character-gradient atmosphere | G |
| [Flux Lines](https://reactbits.dev/backgrounds/flux-lines) | Flowing-line atmosphere | G |
| [Pattern Waves](https://reactbits.dev/backgrounds/pattern-waves) | Patterned-wave atmosphere | G |
| [Micro Slats](https://reactbits.dev/backgrounds/micro-slats) | Slatted-wave atmosphere | G |
| [Shape Waves](https://reactbits.dev/backgrounds/shape-waves) | Geometric-wave atmosphere | G |
| [Aero Shards](https://reactbits.dev/backgrounds/aero-shards) | Glass-shard atmosphere | G |
| [Ghost Fibers](https://reactbits.dev/backgrounds/ghost-fibers) | Fibrous-depth atmosphere | G |
| [CRT Warp](https://reactbits.dev/backgrounds/crt-warp) | Retro-screen atmosphere | G |
| [Molten Metal](https://reactbits.dev/backgrounds/molten-metal) | Molten-metal atmosphere | G |
| [Gradient Waves](https://reactbits.dev/backgrounds/gradient-waves) | Gradient-wave atmosphere | G |
| [Web Threads](https://reactbits.dev/backgrounds/web-threads) | Glowing-web atmosphere | G |
| [Topography](https://reactbits.dev/backgrounds/topography) | Contour-terrain atmosphere | G |
| [Light Tunnel](https://reactbits.dev/backgrounds/light-tunnel) | Light-tunnel atmosphere | G |
| [Sliced Waves](https://reactbits.dev/backgrounds/sliced-waves) | Sliced-wave atmosphere | G |
| [Acid Squares](https://reactbits.dev/backgrounds/acid-squares) | Luminous-square atmosphere | G |
| [Scanner](https://reactbits.dev/backgrounds/scanner) | Scanning-texture atmosphere | G |
| [Ferrofluid](https://reactbits.dev/backgrounds/ferrofluid) | Magnetic-fluid atmosphere | G |
| [Lightfall](https://reactbits.dev/backgrounds/lightfall) | Falling-light atmosphere | G |
| [Liquid Ether](https://reactbits.dev/backgrounds/liquid-ether) | Liquid-space atmosphere | G |
| [Prism](https://reactbits.dev/backgrounds/prism) | Prismatic-geometric atmosphere | G |
| [Dark Veil](https://reactbits.dev/backgrounds/dark-veil) | Dark-light-curtain atmosphere | G |
| [Light Pillar](https://reactbits.dev/backgrounds/light-pillar) | Spatial-light-pillar atmosphere | G |
| [Antigravity](https://reactbits.dev/backgrounds/antigravity) | Antigravity-particle atmosphere | G |
| [Silk](https://reactbits.dev/backgrounds/silk) | Silk-texture atmosphere | G |
| [Floating Lines](https://reactbits.dev/backgrounds/floating-lines) | Floating-fine-line atmosphere | G |
| [Side Rays](https://reactbits.dev/backgrounds/side-rays) | Side-lighting atmosphere | G |
| [Light Rays](https://reactbits.dev/backgrounds/light-rays) | Edge-beam atmosphere | G |
| [Pixel Blast](https://reactbits.dev/backgrounds/pixel-blast) | Pixel-cloud atmosphere | G |
| [Color Bends](https://reactbits.dev/backgrounds/color-bends) | Curved-color-band atmosphere | G |
| [Line Waves](https://reactbits.dev/backgrounds/line-waves) | Linear-wave atmosphere | G |
| [Radar](https://reactbits.dev/backgrounds/radar) | Radar-themed atmosphere | G |
| [Soft Aurora](https://reactbits.dev/backgrounds/soft-aurora) | Soft-aurora atmosphere | G |
| [Magic Rings](https://reactbits.dev/backgrounds/magic-rings) | Concentric-light-ring atmosphere | G |
| [Aurora](https://reactbits.dev/backgrounds/aurora) | Horizontal-aurora atmosphere | G |
| [Plasma](https://reactbits.dev/backgrounds/plasma) | Plasma-color-field atmosphere | G |
| [Plasma Wave](https://reactbits.dev/backgrounds/plasma-wave) | Dual-band light-wave atmosphere | G |
| [Particles](https://reactbits.dev/backgrounds/particles) | Spatial-particle atmosphere | G |
| [Gradient Blinds](https://reactbits.dev/backgrounds/gradient-blinds) | Gradient-blind atmosphere | G |
| [Grainient](https://reactbits.dev/backgrounds/grainient) | Grainy-gradient atmosphere | G |
| [Grid Scan](https://reactbits.dev/backgrounds/grid-scan) | Spatial-grid scanning | G |
| [Beams](https://reactbits.dev/backgrounds/beams) | Striped-highlight atmosphere | G |
| [Pixel Snow](https://reactbits.dev/backgrounds/pixel-snow) | Pixel-snow atmosphere | G |
| [Lightning](https://reactbits.dev/backgrounds/lightning) | Lightning-themed atmosphere | G |
| [Prismatic Burst](https://reactbits.dev/backgrounds/prismatic-burst) | Prismatic-radiation atmosphere | G |
| [Galaxy](https://reactbits.dev/backgrounds/galaxy) | Starfield-travel atmosphere | G |
| [Dither](https://reactbits.dev/backgrounds/dither) | Dither-pattern atmosphere | G |
| [Faulty Terminal](https://reactbits.dev/backgrounds/faulty-terminal) | Glitch-terminal atmosphere | G |
| [Ripple Grid](https://reactbits.dev/backgrounds/ripple-grid) | Ripple-grid atmosphere | G |
| [Dot Field](https://reactbits.dev/backgrounds/dot-field) | Dot-matrix lens atmosphere | G |
| [Dot Grid](https://reactbits.dev/backgrounds/dot-grid) | Springy dot-grid interaction | G |
| [Threads](https://reactbits.dev/backgrounds/threads) | Flowing-thread atmosphere | G |
| [Hyperspeed](https://reactbits.dev/backgrounds/hyperspeed) | High-speed trail narrative | G |
| [Iridescence](https://reactbits.dev/backgrounds/iridescence) | Iridescent atmosphere | G |
| [Waves](https://reactbits.dev/backgrounds/waves) | Connected-line wave atmosphere | G |
| [Magnet Lines](https://reactbits.dev/backgrounds/magnet-lines) | Magnetic-line interaction | G |
| [Grid Distortion](https://reactbits.dev/backgrounds/grid-distortion) | Image-grid disturbance | G |
| [Ballpit](https://reactbits.dev/backgrounds/ballpit) | Ball-physics exploration | G |
| [Orb](https://reactbits.dev/backgrounds/orb) | Ring-energy atmosphere | G |
| [Letter Glitch](https://reactbits.dev/backgrounds/letter-glitch) | Letter-texture atmosphere | G |
| [Grid Motion](https://reactbits.dev/backgrounds/grid-motion) | Drifting image wall | G |
| [Shape Grid](https://reactbits.dev/backgrounds/shape-grid) | Geometric-grid atmosphere | G |
| [Liquid Chrome](https://reactbits.dev/backgrounds/liquid-chrome) | Liquid-chrome atmosphere | G |
| [Balatro](https://reactbits.dev/backgrounds/balatro) | Retro-game atmosphere | G |

## Entries Outside the Catalog and Tools

The pinned registry also contains four UI variants each for `EvilEye` and `FlyingButton`, which are absent from the public 216-entry catalog. Retain them only as [additional registry candidates](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/public/r/registry.json). Reconfirm public documentation, source, and support before use; do not include them in this table's count. Names do not establish stable APIs.

The site also provides [Background Studio](https://reactbits.dev/tools/background-studio), [Center Stage](https://reactbits.dev/tools/center-stage), [Shape Magic](https://reactbits.dev/tools/shape-magic), [Texture Lab](https://reactbits.dev/tools/texture-lab), and [Sound Lab](https://reactbits.dev/tools/sound-lab). These are authoring tools. Registry sounds and SoundEngine are audio capabilities, not animation UI components. Research them only when assets/sounds are requested; do not add interface audio by default. [Pro](https://pro.reactbits.dev/) is separate paid content; this initial version collected none of its private resources.

## Updating

Recheck the official catalog, then compare repository Categories, registry, and needed source. Put additions in the correct category, retain migration notes for renames, and mark unavailable entries instead of guessing replacement paths. Record check date, pinned commit, and actual inspection scope. Do not call an old snapshot a live whole-library index. Distribute this index and integration rules only, excluding the upstream library, original pages, and tool-export asset bundles.
