# Portable shared conventions

Necessary excerpts adapted from Shared Interface Design Foundations 0.2 and Orchestration 0.3, read 2026-11-14. This file supports independent use; within a target project, follow its current explicit requirements and established conventions.

- Organize information around what users need to understand, decide and do. Visual hierarchy follows task importance; density follows content and context.
- Inherit the project's colors, typography, spacing, radii, layering and components. Maintain one authoritative product token source. This module does not choose a universal font, palette or breakpoint scale.
- Give each region one implementation owner. The orchestrator selects modules and consolidates tokens; page leads own content; component owners integrate shared variants; interaction and responsive specialists define and check assigned behavior.
- Keep relevant loading, empty, error, selected and disabled states usable. Preserve entered values and selection across recoverable errors and layout changes. Primary operations need understandable names, keyboard access and visible focus.
- Use the existing Modal, Toast, Tooltip and Drawer conventions. Keep overlay content, focus and primary actions unobscured. Do not change confirmation or destructive-operation semantics merely because space is narrower.
- Distinguish page scrolling from local scrolling. Preserve important information and actions when content wraps, stacks, moves into disclosure or scrolls locally.
- Read only resources needed for the actual task. Complete ordinary missing capabilities with available methods rather than pretending another skill ran.
- Record references, adopted decisions, provisional assumptions and actual verification in the target project when continuity requires it. The original authoring workspace is not a runtime dependency.
- Separate observation from inference. Do not claim unprovided states or unperformed tests. Respect the user's edit boundary; propose shared changes to their owner instead of silently expanding a local repair.

These excerpts carry methods, not a target product's visual preferences. Updates to the shared specification require checking this snapshot's relevance before a new module release.
