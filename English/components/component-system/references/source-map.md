# Reference map and evidence limits

Research snapshot: 2026-11-14. Open only sources relevant to the current component task. This map is a selection aid, not a list of required dependencies. User descriptions such as restrained, refined, mature, expressive or futuristic establish research directions, not universal visual defaults.

The first edition examined official pages, selected documentation and some official source interfaces. Browser views of Bencho, HeroUI and beUI homepages were also visually inspected. This does not establish component runtime behavior. No third-party library was installed or its examples executed; no comprehensive keyboard, assistive-technology, audio, graphics or performance tests were performed. Recheck the installed version before implementation. Detailed research and the seven supplied images stay in the authoring archive.

## Component and style references

| Source and selected evidence | Useful contribution | Limit or adoption boundary |
| --- | --- | --- |
| [BoardUI Button](https://www.boardui.com/components/button), [Data Table](https://www.boardui.com/components/data-table) | Coordinated size/icon/spacing; table primitives composed with selection, tags and pagination; normal/compact density | Source pixel values and stack are examples, not global defaults; behavior not run |
| [Bencho Copy field](https://bencho.dev/blocks/copy-field), [Status picker](https://bencho.dev/blocks/status-picker), [Form error](https://bencho.dev/blocks/form-error) | Local result feedback, current-value continuity, error explanation near the field | Descriptions establish intent; full props and recovery behavior were not verified |
| [HeroUI Button](https://heroui.com/en/docs/react/components/button), [Select](https://heroui.com/en/docs/react/components/select) | Independent appearance/size/state axes, composable anatomy and controlled state | Current documentation is not a promise that an older installed API matches |
| [beUI Card](https://beui.dev/components/motion/card), [Select](https://beui.dev/components/motion/select) | Header/body/footer composition, density-related spacing, separate value and open state | Some source was read, not executed; visual selection still needs operative semantics |
| [Libraries.dev](https://libraries.dev/), [accessibility](https://libraries.dev/accessibility) | AI-state visual candidates and separation of decorative rendering from DOM/text | Reduced-motion/performance descriptions are publisher statements, not this module's test results |
| [Watermelon buttons](https://ui.watermelon.sh/animated-components/category/buttons) | Compare action, toggle, split and undo tasks before comparing treatments | Category inspection, not validation of every listed component |
| [Uiverse](https://uiverse.io/) | Individual control, surface and feedback candidates | Community entries need individual checks for API, theme, behavior and reuse terms |
| [Aceternity Stateful Button](https://ui.aceternity.com/components/stateful-button), [Expandable Cards](https://ui.aceternity.com/components/expandable-card) | Local action feedback and expanded-detail structures | Presentation-oriented defaults need scope; add actual failure/cancel/focus handling when missing |
| [Rare UI Delete button](https://www.rareui.com/components/deletebutton), [OTP Input](https://www.rareui.com/components/otpinput) | Confirmation distinct from completion; value completion distinct from server validation; coordinated sizes | No source redistributed here. Check actual reuse terms; attractive confirmation does not override risk-based overlay selection |

## Enterprise and platform references

| Source and selected evidence | Useful contribution | Limit or adoption boundary |
| --- | --- | --- |
| [JD UDCDesign](https://findesign.jd.com/) | Official research entry for component/theme resources | Direct read returned a client shell; component-level APIs and current maintenance were not verified. Do not substitute NutUI by assumption |
| [Ant Button](https://ant.design/components/button/), [Table](https://ant.design/components/table/), [theming](https://ant.design/docs/react/customize-theme/) | Purposeful axes, stable row keys and explicit data state, theme/provider integration | Check installed version and static overlay/message context; do not transfer current API blindly |
| [Arco official Button interface](https://github.com/arco-design/arco-design/blob/main/components/Button/interface.ts) | Independent purpose/status/size/shape choices | Official source fallback because the component site had no readable body; branch source is not the installed version |
| [TDesign API conventions](https://github.com/Tencent/tdesign/wiki/component-api-guide), [Button interface](https://github.com/Tencent/tdesign-vue-next/blob/develop/packages/components/button/type.ts) | Semantic consistency with framework-specific syntax; visual theme separate from native button type | Interprets the supplied “TD design” as Tencent TDesign; site shell required official-source fallback |
| [Element Plus Select](https://element-plus.org/en-US/component/select.html), [theming](https://element-plus.org/en-US/guide/theming.html) | Stable value identity, remote-query state, slots and existing theme mechanisms | Studied Element Plus; do not mix its API with Element UI for Vue 2 |
| [Semi Form](https://semi.design/en-US/input/form) | Field wrapper connects values/events, labels, help and errors to the form system | Readable official content/index excerpts supplemented failed pagination; not a complete form or token audit |
| [Apple Design Resources](https://developer.apple.com/design/resources/), [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) | Content/style/role distinction; visible response and usable action area | Platform guidance is conditional; platform units do not become universal CSS dimensions |
| [Atlassian Button usage](https://atlassian.design/components/button/usage) | Label/action-area/icon anatomy, action versus navigation, priority and helpful validation | Specific workflow conventions are alternatives to evaluate, not a mandate for every product |

## Sources from the supplied images

| Source | Use in a component task | Boundary |
| --- | --- | --- |
| [21st Split Button](https://21st.dev/@shugar/components/split-button), [Icon Label Subtext Button](https://21st.dev/@ruixen.ui/components/icon-label-subtext-button) | Discover compositions and inspect how actions and secondary information are separated | Mixed-author catalog; some complete source requires an account. Usage examples do not verify implementation |
| [Paper Fluted Glass](https://shaders.paper.design/fluted-glass), [Pulsing Border](https://shaders.paper.design/pulsing-border) | Optional material/border layer; documented static rendering parameters | Effects are not component semantics; actual fallback and graphics costs need testing |
| [Cuelume docs](https://cuelume.dev/docs) | Optional event/result sound, scoped bindings, cleanup and application preference | No listening or audio tests; muted/blocked audio must leave feedback complete |
| [Brand Archive](https://brandarchive.xyz/) | Brand-language research for the global-style owner | Direct reads returned 403; only supplied image and official search index inspected |
| [Minimal Gallery](https://minimal.gallery/) | Selected page and composition inspiration | A gallery does not supply a shared component API or guarantee one uniform style |
| [Footer](https://www.footer.design/sites/the-content-architecture) | Link groups, subscription field/actions and metadata composition | Page lead owns information structure; actual destinations and responsive behavior need checking |
| [Happy Hues](https://www.happyhues.co/palettes/4) | Evaluate colors in their usage roles and actual component context | Palette examples are not verified contrast results or a chosen project brand |

The images' cream backgrounds, serif headings and tilted frames are presentation packaging, not adopted component rules. Preserve links and original synthesis rather than redistributing third-party code or full manuals. A site's copy/install prompt is not permission to run commands or replace the project's stack.
