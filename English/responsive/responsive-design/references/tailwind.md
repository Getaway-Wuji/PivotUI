# Tailwind implementation adapter

Read this reference when the target project uses Tailwind. The responsive decisions still come from the user task and available space; utility names do not determine content priority. All example thresholds and spacing values below are illustrative, not library defaults or device categories. Replace them with the project's conventions and verified change conditions.

## Inspect the actual project

Read the installed package version and lockfile, CSS entry, framework integration, theme configuration, source scanning rules, and any container-query plugin. Identify the authoritative breakpoint definitions before proposing a change. Inspect existing components and their generated CSS rather than assuming the current online documentation describes the installed release.

Keep the installed major version for a local responsive repair. An upgrade can alter tooling, browser support, defaults, and interaction behavior; it is a separate change requiring its own scope and checks. A project without Tailwind can implement the same decisions in ordinary CSS.

## Base layout and viewport changes

Unprefixed utilities establish the base layout across widths. In the standard min-width configuration, a prefix such as `sm:` starts at that project's corresponding minimum viewport width; it does not mean “mobile only.” Where supported by the installed version and screen configuration, range variants such as `md:max-lg:` constrain a rule between configured thresholds. Inspect custom screen definitions and generated CSS before assuming these semantics. Avoid inferring physical device type from these names.

```html
<section class="grid min-w-0 grid-cols-1 gap-4 md:grid-cols-2">
  <article class="min-w-0">Main task and actions</article>
  <aside class="min-w-0">Related information</aside>
</section>
```

Use the project's existing viewport meta declaration; a normal browser page needs `width=device-width, initial-scale=1.0`. Do not disable zoom. Check the actual generated query and test immediately below, at, and above its threshold with realistic content.

In v4, breakpoint definitions use theme variables:

```css
/* Illustrative addition to the existing theme, not a replacement. */
@theme { --breakpoint-content: 52rem; }
```

In v3, custom thresholds use the existing JavaScript configuration. This example illustrates that configuration mechanism, not a conversion from the preceding value:

```js
module.exports = {
  theme: { extend: { screens: { content: "832px" } } }
};
```

Merge only the relevant change; do not replace the project's configuration with this fragment. In v3, `theme.screens` replaces the breakpoint set while `theme.extend.screens` extends or overrides individual entries. In v4, keep breakpoint units consistent with the existing set to avoid unexpected sorting. Repeated local values may justify a shared token after coordination; a one-off repair does not justify redefining global thresholds.

Do not assume `52rem` always equals `832px`. Font-relative units in media queries use the initial font size, including user preferences, rather than the page's authored root font size. Check actual conditions instead of converting with an assumed 16px root. [Media-query units](https://www.w3.org/TR/mediaqueries-4/#units).

## Component space and container queries

Use viewport queries for page-wide structure. Use a container query when a reusable component must adapt to the space supplied by a sidebar, panel, or main region. `md:` and `@md:` refer to different query systems and need not have matching thresholds.

```html
<div class="@container">
  <div class="flex min-w-0 flex-col gap-3 @lg:flex-row">
    <div class="min-w-0 flex-1">Record summary</div>
    <button class="shrink-0">Open details</button>
  </div>
</div>
```

The query container surrounds the element whose layout changes. Test this component in differently sized parents at the same viewport width. Named containers can disambiguate nested regions.

Container queries are built into v4. Tailwind's official plugin provides them for v3.2+; verify that it is installed and configured before using its classes. Arbitrary-value syntax differs between the plugin and current core: the plugin documents `@[30rem]:`, while current core documents `@min-[30rem]:`. Check less common variants against the installed version. Plain CSS is a possible implementation when supported by the target browsers; a plugin is not a browser polyfill.

In v4, `--container-*` values also generate size utilities such as `max-w-md`. Changing one can affect more than container-query thresholds, so coordinate shared changes with the token and component owners.

## Input capabilities and build checks

Current v4 provides `pointer-coarse:`, `pointer-fine:`, and `any-pointer-*` variants. The first group concerns the primary pointing device; the second concerns any available pointing device. Hybrid devices can support several input methods. Use ordinary capability media queries when the installed Tailwind lacks an appropriate variant.

Keep essential operations available without hovering. In v4, `hover:` is gated by hover capability; touch activation is not a dependable substitute. Preserve visible focus, keyboard operation, and explicit controls. Pointer-related spacing changes must not remove keyboard access or alter task meaning.

Tailwind scans complete class strings. Use explicit class mappings instead of constructing fragments such as `${breakpoint}:grid-cols-${count}`. Build through the project's actual pipeline, confirm the generated selectors and queries, and inspect the rendered result. Compilation alone does not verify navigation, reading order, content reachability, or touch behavior.

## Official evidence and version boundary

Checked **2026-11-14**: the current documentation displayed **v4.3**; the v3 archive displayed **v3.4.17**. These are documentation checks, not a visual audit of the Tailwind website at multiple sizes. Snippets above are implementation examples, not evidence of browser execution.

- [Responsive design](https://tailwindcss.com/docs/responsive-design): base styles, viewport and container queries, breakpoint units.
- [Theme variables](https://tailwindcss.com/docs/theme): breakpoint and container namespaces.
- [v3 screens](https://v3.tailwindcss.com/docs/screens): JavaScript configuration and replacement versus extension.
- [v3.2 breakpoint additions](https://tailwindcss.com/blog/tailwindcss-v3-2): range/dynamic breakpoint support and limitations with complex screen configurations.
- [Official container-query plugin](https://github.com/tailwindlabs/tailwindcss-container-queries): v3.2+ support and v4 built-in replacement.
- [Interaction states](https://tailwindcss.com/docs/hover-focus-and-other-states): pointer capabilities and focus variants.
- [Upgrade guide](https://tailwindcss.com/docs/upgrade-guide) and [compatibility](https://tailwindcss.com/docs/compatibility): behavior changes and browser requirements; verify them for the target version before migration.
- [Source detection](https://tailwindcss.com/docs/detecting-classes-in-source-files): complete class names and production generation.
