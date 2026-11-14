# Shared Design Conventions

Adapted from Shared UI Design Foundations 0.2, dated 2026-11-14. This file contains the methods needed for standalone use and does not require the original project documents. Prefer target-project conventions; explicit user instructions take priority over defaults.

## Visuals and information

- Organize content around what users need to understand, decide, and do. Express hierarchy through position, size, weight, spacing, and grouping.
- Keep equivalent semantics and components consistent within a product. Different products may use different brands; a product's marketing and application regions may have explicit typography and density variants.
- Do not require every project to be light, dark, minimal, or use a particular brand color. Follow references, business needs, and the existing project. Do not record provisional choices as confirmed user preferences.
- Maintain shared styles by purpose and reuse existing themes and components. Give adjacent regions clear alignment relationships; use container boundaries for meaningful grouping.
- Handle realistic lengths and quantities: long headings, large numbers, mixed-language text, and missing content. Follow project conventions for money, dates, units, and precision.

## References and states

- Extract structure, spacing, typography and color, component details, and applicable conditions. Define the adopted scope and avoid combining incompatible visual languages from different references.
- For exact reproduction, follow the specified reference and label unmeasurable values as estimates. Treat interactions and narrow-screen behavior absent from static images as supplementary design.
- Supply applicable hover, focus, selected, disabled, loading, empty, error, and completion states. Do not mechanically give every component all states.
- Give clear action feedback, preserve form input on errors, support keyboard completion of key flows, and communicate state through more than color.
- Reorder narrow layouts by task priority; make tables and charts readable and key actions available by touch. Respect reduced-motion preferences and keep motion from obstructing reading or action.

## Responsibilities and validation

- Assign one lead per page or region. Involve component, interaction, and responsive capabilities during design and implementation.
- Maintain shared design decisions in the target product, with clear scope for local differences. Use readable records to continue across chats.
- Check only relevant deliverables. Runtime, rendering, and interaction checks apply to implementations; do not claim page testing when delivering rules only.
- Do not use `gpt-taste` for dashboards or business tools. In this cluster, `ui-ux-pro-max` supplies research and advice. Scope marketing capabilities by region while retaining necessary lightweight business feedback.
