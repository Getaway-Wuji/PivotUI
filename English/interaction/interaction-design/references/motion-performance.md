# Motion Selection and Performance

User preference: prefer React Bits directly for most suitable animations; complex effects are allowed, while avoiding stacks that cause sluggishness. The cost tiers below are design heuristics, not measured component rankings or device guarantees.

## Purpose and Runtime Cost

| Candidate characteristic | Selection approach | Costs to inspect |
| --- | --- | --- |
| Local press, selection, fade, or short movement | First choice for ordinary interactions; reuse existing feedback or suitable Micro components | Layout work, instance count, trigger rate, text clarity |
| Continuous motion, per-character animation, following, staggered lists | Use in a few areas where it aids understanding; stop when complete | Node count, per-frame work, scroll listeners, repeated animation |
| Particles, fluids, shaders, WebGL, 3D/physics | Evaluate for a specific visual focal area and confine it there | Canvas count, pixel ratio, resolution, particle count, materials/models/textures, GPU/CPU work |

Appearance or dependency names alone do not determine complexity. A small shader can cost less than a large DOM, while hundreds of simple instances can be expensive. Judge selected source, actual content volume, and target-device results.

For ordinary business pages, begin with brief event-driven feedback. For expressive pages, start complex effects in one focal area and add more only as results justify. This is a cautious starting strategy, not a one-effect-per-page limit. Do not simultaneously enable particles, pointer following, or perpetual loops in every row, button, and card.

## Define Each Effect's Lifetime

For continuous effects, record visible region, start/pause/disposal conditions, static fallback, and target devices. One line in the component handoff is enough.

- Make critical first-screen actions usable first and lazy-load heavy effects. For a local animation, inspect existing dependencies/variants before adding another engine.
- Pause continuous computation offscreen and unnecessary work when the page is hidden. CSS hiding or `opacity: 0` does not stop loops. Verify actual start/stop paths for requestAnimationFrame, timers, WebGL, and physics.
- On unmount, route departure, or reinitialization, clean up listeners, observers, and loops and dispose applicable graphics resources. Respect ownership of shared resources so other live instances are not broken.
- Reduce pixel ratio, particles, update rate, or texture size only through supported controls. Do not invent props from names. Without pause/fallback support, control mounting externally, adapt integrated source, or select another candidate.
- Limit simultaneously animated rows in large lists. Keep stable keys and avoid replaying whole-page entrance after filtering. Cooperate with existing virtualization without imposing it on ordinary small lists.

## Input Methods and Reduced Motion

- With `prefers-reduced-motion`, preserve information and task completion while removing large displacement, parallax, shaking, continuous particles, and unnecessary loops. Use instant changes, slight fades, or static visuals. CSS fallbacks do not automatically stop JavaScript/Canvas loops; verify source behavior.
- Treat hover and fine pointers as enhancements, not required entry conditions. Touch needs taps, buttons, or visible instructions; dragging needs an operable alternative. Avoid intercepting global scrolling or browser gestures.
- Provide pause controls for continuous carousels/scrolling displays as needed. Keyboard entry or user interaction must protect reading. Prefer static content for reduced motion. Essential text must not remain scrambled, blurred, or hidden.
- Feedback animation must not delay the user's next action or be the only state signal. Update state reliably first and let motion reflect it. Interrupted, reversed, or dismissed effects must preserve correct business state.

Implementation sources: [MDN reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion), [Page Visibility](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API), [Intersection Observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).

## Validate the Actual Interface

1. Compare a disabled-effects baseline with the effects-enabled version at target content volume. Cover scrolling, continuous input, opening/closing overlays, and rapid repeated actions.
2. Observe obvious frame drops, long tasks, input responsiveness, and resource growth after route departure. Record browser, device or emulation limits, and scope. A narrow viewport is not a low-end phone test and cannot guarantee physical-device smoothness.
3. Check loops/state after hiding/restoring the page, scrolling regions out/in, and unmounting/remounting. Verify reduced motion and touch alternatives.
4. If work blocks interaction, first reduce active instances/quality and pause offscreen work, then replace excessively expensive approaches. Preserve a usable static/lightweight path.

For skill authoring or screenshot review alone, record these as implementation requirements. Do not claim performance measurement or promise unsupported “stable 60fps.”
