# Portable shared conventions

Necessary methods adapted from Shared Interface Design Foundations **0.2** and Orchestration **0.4.1**. These excerpts support independent use; they do not require the original repository. Explicit user requirements and established target-product conventions take priority.

1. Organize the interface around users' tasks. Convey hierarchy through placement, alignment, spacing, typography and grouping before adding decoration.
2. Keep same-level pages consistent in navigation, content starting line, heading and global action placement. Page content may have task-specific composition.
3. Use the product's authoritative tokens and existing component conventions. This package specifies no universal palette, font, radius, density or theme. New shared values need one maintained source and clear consumers.
4. Assign one owner per region and component. Shell, page content, behavior, component implementation and responsive support have separate contributions; the named owner integrates them. Missing specialists do not block ordinary work.
5. Distinguish current/expanded/focus and other relevant states. Use named keyboard-operable controls, visible focus, and appropriate focus restoration. Preserve input and operation state through recoverable changes.
6. Separate page and local scrolling; fixed regions and overlays must leave content, actions and focus reachable. Adapt to real content and available space.
7. Record what references establish, what is estimated and what is supplemental. Product-specific decisions stay in that product. Do not generalize a sample brand to the library.
8. Inspect actual rendering and behavior when implementation is delivered. Report only performed checks; static instruction review does not establish runtime or device compatibility.

The standalone package includes these excerpts so shared essentials remain available without loading unrelated modules. Reconcile them with their source versions when maintaining future editions.
