# Portable shared conventions

Necessary excerpts and component-specific application of Shared Interface Design Foundations 0.2 and Orchestration 0.2, reviewed 2026-11-14. This file makes standalone use possible. In a target project, prefer its current explicit requirements and authoritative design conventions; original authoring paths are not required.

- Organize hierarchy around what users need to understand, decide and do. Use placement, grouping, size and spacing before adding decoration. Same semantics and component behavior stay consistent within a product; meaningful differences have named conditions.
- Tokens belong to the target product with one maintainable source. Global style creates/validates values where available; the orchestrator consolidates them. Existing themes, fonts, colors, radii and libraries take priority over reference defaults. New shared values need their purpose and impact recorded.
- Reuse existing components and supported extension points. Page leads own business structure; component implementation carries the agreed interaction and device rules. Missing optional skills do not block ordinary work. Do not claim an unavailable skill ran.
- Complete applicable states and meaningful empty/error/loading content. Preserve input on failure, prevent duplicate pending actions, keep key workflows operable by keyboard, provide names and visible focus, and handle long content and narrow layouts.
- UI behavior remains available when motion is reduced. Public-marketing effects do not become business-tool defaults. The cluster's `gpt-taste` role is public marketing only; `ui-ux-pro-max` supplies research and recommendations.
- Static screenshots do not establish hidden states or exact dimensions. Record estimates and supplemental decisions. Source claims and scenario reasoning are distinct from actual runtime checks.

## Overlay/message compatibility

When `floating-components` is available, read its relevant current rules and reuse its existing implementation. The following preserves this cluster's current distinctions for standalone work; these are project conventions, not universal definitions of every library:

| Component | Current use |
| --- | --- |
| Tooltip | Transient supplementary explanation; not required instructions available only on hover, not an interactive action container |
| Toast | Lightweight successful action outcome; errors and actionable warnings stay in persistent UI |
| Alert | Persistent important notice or error, with recovery where appropriate |
| Modal | Irreversible/high-risk confirmation or complex information; not routine simple confirmation |
| Popconfirm | Local low-risk confirmation that is actually useful; not a substitute for high-risk Modal |
| Drawer | Substantial editing that retains surrounding context; simple forms stay inline and independent full-screen flows use a page |

Use mature overlay primitives for focus, Escape, background interaction and sensible focus return. Actual modality determines focus trapping, not a side-panel appearance. Pending/close/cancel behavior follows the real operation; closing does not imply server cancellation. Keep failure and drafts available, inherit theme across portals, and coordinate stacking and scroll boundaries. Where the target project's explicit conventions differ, record the applicable override instead of maintaining two competing behaviors.
