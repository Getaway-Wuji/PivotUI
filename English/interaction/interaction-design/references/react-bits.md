# React Bits Selection and Integration

Read when animation, interaction components, or replacements for custom effects are needed. Consult relevant categories of the [complete catalog](react-bits-catalog.md) to find specific names. A focus/submission-logic repair does not require replacing existing controls merely to use a library.

## Adoption Policy

The user selected React Bits as the preferred source for most suitable animations. Look first in Micro and Components, then consider Animations wrappers. When a component fits, adopt its official source and map project tokens. Other effects remain available, selected by page purpose, input methods, and runtime budget. Use existing project capabilities when no component fits, the stack is not React, existing components are more complete, or integration cost is unsuitable; record why.

The public catalog inspected as of 2026-11-14 contains 216 entries. Research commit: [`4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce`](https://github.com/DavidHDev/react-bits/commit/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce). Catalog and registry were checked. Representative findings below are **spot checks of TS-CSS source/API branches**, not hands-on demo use or whole-library runtime certification. Recheck later versions, other variants, and chosen parameters in the target project.

## Select by User Task

For messages/overlays, apply the [floating-component](../sub-skills/floating-components/SKILL.md) applicability/exclusion table before selecting a visual implementation. Swipe Toast is only for lightweight success/information, never errors or actionable warnings. Errors belong near fields or in persistent Alert. Library themes/demos do not override these conventions.

First establish content count, arrangement, trigger, and target state. For example, inspect Circular Carousel / Circular Gallery first for a cylindrical strip of multiple artworks. Lanyard represents one hanging identity card and does not replace multi-image browsing because of a similar word. Visual similarity alone does not establish exact reproduction of all reference behavior.

| Task | Preferred candidates | Integrator's responsibility |
| --- | --- | --- |
| Binary settings, task checkboxes | Squish Switch, Spring Check | Controlled values, understandable names, async save/rollback, form integration |
| Single-choice filters, exclusive options, segmented switching | Glide Select, Jelly Radio, Rubber Segment | Draft/applied values, real selection semantics, no-results and clearing behavior |
| Input, verification codes, parameter controls | Code Slots, Scrub Field, Wake Slider, Prompt Bar | Validation, paste/composition, business format, submission/error association |
| Running/completed/failed tasks | Status Mark, Call Chip, Lattice Loader, Thought Line | Drive from real request state; provide next steps; never manufacture success with animation timers |
| Lightweight actions with undo windows | Fuse Button, Swipe Toast | Real undo transactions and deadlines; failures inline/Alert, never Toast; preserve focus |
| Actions that genuinely need accidental-activation protection | Hold Button, Slide Commit, after fixing cancellation gaps below | Gesture must suit task; equivalent keyboard path; preserve business confirmation; verify cancel/blur never submits before high-impact use |
| Short lists, multistep forms | Animated List, Stepper | Large-list cost, current-step validation, retained input, server errors, backward navigation |
| Hints and local visibility | Warm Tooltip, Fade Content, Animated Content | Focus-triggered hints; hidden controls must not remain focusable |
| Brand navigation, image browsing | Card Nav, Pill Nav, Staggered Menu, Carousel, etc. | Page lead approves region; navigation semantics, focus, dismissal, pause, touch |
| Visual feedback for focal actions | Magnet, Click Spark, Glare Hover | Decoration is not request completion; keep dense business-control hit areas stable |

Marketing text effects, backgrounds, cursors, and 3D are also available. Their use is a page-presentation decision for the page lead. Do not treat creative navigation as a modal Drawer, particle bursts as submission success, or gesture effects as mandatory for every button.

## Source Integration

The [official installation page](https://reactbits.dev/get-started/installation) supports component-by-component source installation or manual copying. Choose JS/TS and CSS/Tailwind to match the existing stack. Verify exact names/case on the target page or registry. Example:

```sh
npx shadcn@latest add @react-bits/SplitText-TS-TW
```

If `components.json` exists, merge this namespace into registries without replacing other settings:

```json
{
  "registries": {
    "@react-bits": "https://reactbits.dev/r/{name}.json"
  }
}
```

The same commit's [README installation instructions](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/README.md) also provide:

```sh
npx jsrepo@latest add https://reactbits.dev/r/SplitText-TS-TW
```

These are documented examples, not instructions to install Split Text for every task. Substitute the verified candidate and choose one installation method. For manual use, select the variant in the target page's Code section, copy required files, and install its listed dependencies. Import from actual project paths, not an assumed unified `reactbits` npm export package or a fixed user directory.

Before integration, inspect Props, source, CSS, registry dependencies, and actual package.json to avoid duplicate engines/incompatible dependencies. In particular, the inspected Warm Tooltip TS-CSS registry requires `react-dom@^19.0.0`; compare the project's React major rather than upgrading the whole project unconditionally. Preserve framework/routing and handle client boundaries/SSR as needed. Installation proves source acquisition, not flow correctness.

Original colors, durations, dimensions, z-index, and assets are defaults. Map existing tokens through public props or local CSS variables first; confine necessary changes to the component adapter. If public APIs lack needed behavior, add it or use an existing component, documenting the adaptation. Official defaults are not the user's product preferences.

## Representative Evidence and Four-Stage Behavior

“Source” means implementation present at the pinned commit; “addition” means task-specific work for the integrator. No row has browser or assistive-technology runtime verification. Per-component links follow the table.

| Component / evidence | Trigger → state change → user feedback → exit or recovery | Integration decisions and gaps |
| --- | --- | --- |
| Animated Content / source | scroll or mount → content enters → configurable movement/opacity → once, scrub, or configured disappearance; reduced motion reveals directly | `onComplete` marks animation completion. Addition: it cannot confirm requests; overlay dismissal/focus remain separate |
| Fade Content / source | scroll or mount → visibility effect → configured fade/focus → once/exit/disappearance; reduced motion reveals directly | GSAP + ScrollTrigger. Addition: prefer simple fades; do not delay errors or blur them for extended periods |
| Click Spark / source | click or ref.spark → canvas decoration → brief sparks → lifetime cleanup; disabled/reduced-motion branches | No additional registry dependencies. Addition: business button retains name, focus, and truthful outcome feedback |
| Magnet / source | Pointer enters range → displacement/tilt → spring following → reset on leave; disabled/reduced motion prevents magnetism | No additional registry dependencies. Addition: a few focal entries, stable hit area, touch operability |
| Animated List / source | Pointer or arrows/Home/End → active item changes → selection marker; Enter/Space can call onItemSelect → leaving does not submit business action | listbox/option semantics and reduced-motion branch. Addition: confirm the task is a selection list; preserve existing dense business tables |
| Stepper / source | Previous/next or step entry → step changes → indicator/content transition → previous step or onFinalStepCompleted | Controlled step and linear supported; callbacks do not await validation Promises. Addition: update step only after validation; submission result determines final success |
| Glide Select / source | Button click/keyboard → open → listbox/active item; arrows/Home/End/typeahead → Enter/Space commits, Escape/Tab/outside click closes | Controlled value/onChange; selection returns to trigger; reduced-motion CSS. Addition: wire form/filter requests and test assistive technology/long lists |
| Spring Check / source | Button activation → checked toggles → check/text effect → activate again to clear; disabled blocks | button role=checkbox, checked/onChange, reduced motion. Addition: integrate submitted fields; do not apply strikethrough to ordinary options that do not mean completion |
| Squish Switch / source | Click/drag → checked changes → thumb/color → toggle again or cancel drag | button role=switch, aria-disabled, controlled checked/onChange, reduced motion. Addition: saving lock/queue strategy, rollback, error explanation |
| Warm Tooltip / source | Trigger hover/focus → delayed opening, faster subsequent grouped hints → tooltip/description association → blur/leave/Escape closes | motion, Portal, reduced motion; trigger leave schedules closure, with no observed tooltip-hover retention. Add a shared trigger/tooltip hover region and verify movement into the hint stays readable. Essential instructions need more than Tooltip; touch hold must not disrupt scrolling |
| Status Mark / source | Parent status/progress changes → pending/running/done/failed/cancelled → graphic/optional label → parent advances state | motion + reduced motion; no requests/retry. Addition: persistent text, appropriate live region, business-owned recovery actions |
| Swipe Toast / source | open → open/closing/gone → message/action/timer line → timeout, swipe, action, close, Escape, or programmatic dismissal; hover/focus/page visibility affect timing | motion, aria-live, dismissal reasons. Adopt only lightweight success/information; errors/actionable warnings inline/Alert, even with duration=0. Enable close as needed and integrate shared layering |
| Fuse Button / source | Activate → idle→armed → undo entry/timer line → undo to idle, expiry reset/stay; onCommit at press or fuseEnd | Button/status text, focus transitions, reduced-motion CSS. Addition: onCommit/onUndo are void callbacks requiring real transactions/recovery; armed text is not server confirmation |
| Hold Button / source | Hold pointer or Enter/Space → holding → progress fill → early release/leave cancels; threshold gives done/onHold | done means gesture completion only. **Inspected gap:** Escape cancels only keyboard holding; window blur is handled but control blur cancellation was not found, so Tab may leave submission timing active. Add cancellation across inputs and control-blur cleanup; verify no accidental onHold. Provide a no-hold equivalent; business layer owns pending/error/success |
| Slide Commit / source | Drag to endpoint and release, or keyboard reaches endpoint → pending (onConfirm Promise) → completion/error label → retry after failure; success collapses under holdMs | **Inspected gap:** pointercancel shares release handling and can submit at the endpoint; Home/Escape during drag takes the same path. Separate cancel from confirm and verify cancellation never invokes onConfirm before evaluating high-impact use. End/arrows reaching endpoint submit: define keyboard agreement. Add idempotency, duplicate guards, and persistent errors |
| Carousel / source | Buttons/drag/arrows or autoplay → current item → card/page transition → previous/next, Home/End; focus/hover, offscreen, reduced-motion handling | Autoplay need not be enabled. Addition: explicit pause, focusable content on hidden slides, long content, screen-reader order |
| Staggered Menu / source | Toggle button → open → layered sliding/staggered links → toggle or configured outside click closes | GSAP; aria-expanded/aria-hidden. Inspected TS-CSS had no identified Escape, focus transfer/return, hidden-link inert, or reduced-motion branch. Add appropriate navigation/modal behavior; not a direct business-Drawer substitute |

### Pinned Source Links

Each link targets the inspected variant. Reinspect changed source rather than guessing new APIs from this table.

- [Animated Content](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Animations/AnimatedContent/AnimatedContent.tsx), [Fade Content](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Animations/FadeContent/FadeContent.tsx), [Click Spark](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Animations/ClickSpark/ClickSpark.tsx), [Magnet](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Animations/Magnet/Magnet.tsx).
- [Animated List](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Components/AnimatedList/AnimatedList.tsx), [Stepper](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Components/Stepper/Stepper.tsx), [Carousel](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Components/Carousel/Carousel.tsx), [Staggered Menu](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Components/StaggeredMenu/StaggeredMenu.tsx).
- [Glide Select](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/GlideSelect/GlideSelect.tsx), [Spring Check](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/SpringCheck/SpringCheck.tsx), [Squish Switch](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/SquishSwitch/SquishSwitch.tsx), [Warm Tooltip](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/WarmTooltip/WarmTooltip.tsx).
- [Status Mark](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/StatusMark/StatusMark.tsx), [Swipe Toast](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/SwipeToast/SwipeToast.tsx), [Fuse Button](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/FuseButton/FuseButton.tsx), [Hold Button](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/HoldButton/HoldButton.tsx), [Slide Commit](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/src/ts-default/Micro/SlideCommit/SlideCommit.tsx).

## Concurrent-Effect Budget and Fallback

Select the state or focal region that needs explanation before budgeting decoration. Avoid stacking complex effects: background particles, fluid cursors, 3D cards, and widespread staggered entrances add up. Preserve the effect that best serves the task and simplify/staticize others. This is a selection principle, not a fixed component-count restriction.

- Inspect continuous requestAnimationFrame, Canvas/WebGL, physics, large blur/filter regions, multiple media instances, and per-item listeners in long lists. Bundle size or “dependency-free” does not establish low runtime cost.
- Confine heavier components to defined regions; lazy-load, limit active instances, pause offscreen, or unmount. Clean up timers, observers, events, and graphics resources. Inspect existing handling before filling gaps; do not duplicate global listeners.
- Preserve static final states and basic operations for reduced motion, touch/coarse pointers, and weaker devices. Critical content must not require dragging/hover when a pointer is absent. Provide static alternatives for WebGL/asset failure.
- Test actual assets, resolution, and devices during scrolling, typing, and key operations; compare effects disabled. Reduce particles, resolution/pixel ratio, transparent layers, or visible instances as needed. Without measurement, say “runtime validation pending,” not “frame-rate target met.”
- A reduced-motion branch does not prove every animation stops or that changing system preference applies immediately. Verify final behavior, business timing, and readability; disabling motion must not skip real requests.

## Sources and Distribution Boundaries

The inspected [LICENSE.md](https://github.com/DavidHDev/react-bits/blob/4e0d091d3b1ea8b7aadef33716a8d99d164ae4ce/LICENSE.md) identifies MIT + Commons Clause, requires retaining copyright/license notices, and restricts redistribution of components, tools, sounds, and standalone export packages. Recheck current terms and resource-specific notices when integrating into an application, retaining required attribution. This skill distributes original methods, a name index, and official links; it does not bundle upstream components, tools, sounds, or bulk exports for redistribution. Original pages, license snapshots, and selected source stay in project research archives, outside the skill package.

Record chosen component/variant, source commit/acquisition date, target files, dependency changes, token mapping, added behavior, concurrent-effect budget, and measured scope. If external sites are unavailable, retain existing implementations or complete necessary behavior using these rules, identifying unobtainable components. Do not claim installation, execution, or authorization for private Pro content.
