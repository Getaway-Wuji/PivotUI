# Shared Dashboard Design Conventions

Source: Dashboard excerpt from *Shared Interface Design Foundations*, **0.2, 2026-11-14**.

This file ships with the standalone skill and retains only shared conventions needed for design work. Existing target-project standards and components, and explicit user requirements, take precedence. No particular directory structure, other skill, or original reference image is required.

## Inherit the target product's design system

- Identify its established theme, brand colors, typography, density, page shell, and components; inherit them within the current scope.
- Propose unresolved visual values for this task, but label them as suggestions rather than confirmed user preferences.
- Different products may use different systems. Within one product, use consistent expressions for the same semantics, components, and actions.
- Keep shared colors, spacing, radii, and shadows in the target project's maintainable source of truth. Do not create a duplicate Dashboard theme. When an orchestrator assignment exists, consolidate shared changes through that role.
- When compact, spacious, or different-theme variants are needed within a product, name their purpose instead of letting every card choose independent values.
- Local references apply to the current region by default. Product-wide changes must match the user's explicit requirements and state their impact in the target product.

## Define Dashboard ownership

- Arrange content around what users need to understand, judge, and do. Area, position, and emphasis reflect business importance.
- Own metric priority, chart selection, overview layout, and data explanation. Reuse existing navigation, title area, content origin, and scrolling shell.
- Overviews may include summary tables, filters, and detail links; this does not expand scope to application-wide form, list, or navigation redesign.
- Share basic buttons, inputs, badges, and overlays across modules. New variants need a real task-based reason.

## Preserve readable visual relationships

- Establish hierarchy through position, size, weight, spacing, and grouping before adding color and decoration.
- Container boundaries should express separate content, actions, or states; avoid decorative nesting.
- Keep a limited set of type levels with clear purposes. Coordinate Chinese text, numbers, and units; long names and real data volume must not break layouts.
- Page backgrounds, content surfaces, text, borders, interactive emphasis, business status, and chart series have distinct meanings; do not mix them indiscriminately.
- Keep color encoding stable for the same metric across charts when possible. Pair status color with text, icons, or another cue.
- Text, borders, selection, and focus must be distinguishable against actual backgrounds. Inspect light secondary text and dark surfaces closely.
- Use a consistent icon language; give difficult-to-recognize actions understandable names.

## Apply judgment when using references

- Extract structure, hierarchy, and reusable relationships, then substitute actual business content. Do not mechanically preserve card counts or sample brands.
- Assign distinct purposes to multiple references, and unify typography, surfaces, borders, and controls.
- Distinguish visible facts, prompt requirements, and added designs. Static images do not establish implemented keyboard, loading, narrow-screen, or animation behavior.
- Label unverified colors, type sizes, and dimensions as estimates or implementation suggestions. Do not describe visual observation as precise measurement.
- Motion in business interfaces explains feedback and state changes. Adjust intensity to the task, usage frequency, and motion preferences.

## Continue by task

- Metric definitions, chart prerequisites, density, and screen-specific arrangements: read [data-and-layout.md](data-and-layout.md).
- Navigation adaptation, expansion, reordering, updates, and operation states: read [interaction-patterns.md](interaction-patterns.md).
- For specifications, check rules and references. For implemented pages, verify rendered output and core operations, and report only what was actually completed.
