# Choose a direction without freezing a look

Use this when reference appearance affects component decisions. These alternatives are author synthesis from the supplied references, not universal presets or claims of runtime verification. The [source map](source-map.md) identifies evidence and limits.

## Compare by purpose

| Direction | Useful when | Component rules to borrow | Differences to retain |
| --- | --- | --- | --- |
| Restrained product controls | Frequent actions, settings, lists, forms | Clear priority, consistent text/icon alignment, modest surface hierarchy, coherent density; readable focus and errors | BoardUI's subtle borders/gradients and Apple platform conventions do not mandate flat controls, glass, or one radius |
| Mature product composition | A growing product needs stable families across pages | Explicit anatomy, composable regions, purposeful axes, predictable controlled values and events | HeroUI or enterprise library API names and framework requirements stay local to that library/version |
| Refined local feedback | Copy, save, choose, expand, status change | Keep identity and context during transitions; align feedback with real events; preserve label and current value | Bencho-like morphing, icons, timings and motion depend on the task; complete failure and reset paths first |
| Expressive presentation | Product highlights, discovery cards, a prominent action or detail reveal | Stronger local hierarchy, material or motion attached to a stable semantic structure | beUI, Aceternity, Rare UI and individual gallery works offer different treatments; adopt only an appropriate treatment for the chosen region |
| AI / futuristic state display | Generation, search, voice or asynchronous work | Couple motion to real state, keep status text and cancel/retry paths, isolate decorative rendering | Orbs, edge light, metal, fluid and shaders are choices; none is the definition of AI or a required theme |
| Dense enterprise work | Repeated comparison, large forms, bulk actions | Coordinated row/control density, stable identities, useful states, explicit selection and data ownership | Ant, Arco, TDesign, Element and Semi differ by framework and conventions; select by installed stack and task, not one compulsory ranking |

Directions can coexist in named regions. A marketing highlight and an administration table may share brand tokens while using different emphasis and density. A local special effect should not silently spread through the base Button or Card used throughout the product.

## Turn one reference into a reusable rule

1. Identify the actual component and task, excluding presentation frames, screenshot captions and unrelated page decoration.
2. Describe required/optional parts and reading order. Record relative relationships such as aligned labels, consistent padding, or secondary text smaller than the action label. Exact dimensions need source or measurement; otherwise mark an estimate.
3. Separate task semantics from appearance: an on/off setting, a submitted request and a completed operation are not equivalent because their animations look similar.
4. Name a conditional rule: “use a split action when one default action has related alternatives,” or “use a denser row with matched controls for a high-frequency desktop list.” Preserve alternatives when they serve different conditions.
5. Map the selected treatment to existing tokens and public APIs, then check it in its actual content and device context.

A source's attractive default does not prove its disabled state, contrast, touch target, keyboard access, asynchronous correctness or performance. Record observations, source statements and proposed additions separately. Verify what the actual task needs.

## Bound effects without losing useful feedback

Treat texture, glow, glass, shader and particle rendering as optional visual layers. They must not intercept essential input, obscure focus, lower text readability, or determine whether an operation succeeded. Keep a functional static rendering when reduced motion, unavailable graphics, or the target device requires it. Check mount/unmount cleanup and visibility-aware work if adopting an expensive effect; do not impose GPU effects on ordinary business controls.

Sound is optional and follows the product's audio preference and interaction design. A click cue and a success cue correspond to different events. Keep all essential feedback available when muted or browser audio is blocked. Avoid repeated bindings, automatic global volume changes and per-token sounds during streaming. A sound library does not require a second set of action components.

Brand Archive, Minimal Gallery, Footer and Happy Hues inform selected brand, layout, grouping or color-role questions. Page structure belongs to the page lead; global brand choices belong to global style/orchestration. Their examples do not supply a component API or justify copying an entire visual system.
