# Shared Interface Design Foundations

Version: 0.2  
Created: 2026-11-14  
Status: Shared rules are established; visual direction awaits the user's references.

These foundations serve the interface design skills as a common agreement on design methods, component behavior, and collaboration across pages within one product. Each area develops its specialized methods from the user's references and inherits the product's established global visual settings. See the [skill orchestration plan](ORCHESTRATION.md) for the division of work between authored and external modules.

## 1 Scope and working principles

Applies to admin application shells, Dashboards, data lists, forms, detail pages, settings, and relevant shared design work for public websites, portfolios, and existing-site redesigns. Business data rules apply to business areas; marketing narrative rules apply to presentation areas. Each skill and its project module record add the relevant details.

- Organize content around the user's work: what they need to understand, decide, and do.
- Let visual hierarchy reflect information importance. Establish hierarchy through position, size, weight, spacing, and grouping before choosing color or decoration.
- Use consistent expressions for the same meaning, component, and interaction within a product. Document the conditions for intentional differences.
- Set information density from the working context and references. Compact layouts, generous whitespace, light themes, and dark themes can all be valid directions.
- Reuse an existing project's components, style variables, and interaction conventions first. When the user requests a redesign, update them within the requested scope.
- Explicit user requirements take precedence. When requirements conflict, first determine the scope of the effect. Resolve local differences within the module; clarify choices that affect several pages only when they cannot reasonably be inferred.

## 2 Global visual settings

Use the following table as a template for recording the target product's visual settings. This library does not impose one brand color, font, theme, or decorative style across products. Visual recipes in the Dashboard reference library remain candidates for that module.

When building a product, record its visual settings and token location in the target project. The orchestrator consolidates the settings for that product, and both external and authored modules consume them. Different products may use different visual systems. If a public website and admin application need different type sizes or densities, define explicit component or area variants. These general foundations do not automatically inherit a particular product's brand.

| Setting | Current status | What to record when decided |
| --- | --- | --- |
| Overall style | Awaiting references | Specific visual characteristics, sources, applicable pages |
| Theme | Undecided | Light, dark, or both; switching requirements |
| Color | Undecided | Page and container backgrounds, text hierarchy, borders, accents, status colors, chart colors |
| Typography | Undecided | Chinese and Latin fonts, fallbacks, type scale, weights, line heights, numeral styles |
| Spacing and density | Undecided | Spacing scale, page margins, component padding, control heights, table row heights |
| Application shell | Undecided | Navigation position and size, content width strategy, title area, scrolling behavior |
| Shape and layering | Undecided | Corner radius scale, strokes, shadows, overlay layers |
| Icons and motion | Undecided | Icon source and style, sizes, motion patterns and duration |
| Components and technical constraints | Project-dependent | Existing component library, implementation framework, inherited constraints |

After receiving references, record only decisions they support. If exact font sizes, color values, or dimensions cannot be confirmed from a screenshot, label them as estimates from the screenshot rather than measured values. When source code or design files are available, use values that can actually be checked.

A local reference applies to the current area by default. When the user says it represents the whole product or requests a unified global style, record the choices in the target product's design records, using the table above if useful. Include sources and affected modules. A temporary experiment in the first area does not automatically become a global rule. Update these foundations only when the user explicitly changes the general rules for this skill series.

If global settings are not yet established, proceed with a temporary approach consistent with the references and record it in the module's project notes. For areas without references, first follow the existing interface; otherwise use a simple default that supports the current task.

## 3 Derive design methods from references

Before creating a module, combine the user's description with the available references to determine what to borrow: overall layout, table density, card hierarchy, color, or interaction, for example. Act on details the user already supplied. Resolve reasonably inferable details and distinguish those decisions in the record.

Extract relevant observations without mechanically filling every category:

| Observation | What to extract |
| --- | --- |
| Page structure | Content regions, priority, navigation and action placement, reading order |
| Spatial organization | Content width, alignment lines, columns and gaps, whitespace distribution, information density |
| Typography and color | Heading and body hierarchy, numeric presentation, emphasis, surface hierarchy |
| Component details | Control dimensions, table structure, card boundaries, labels, icons, overlays |
| Interaction and state | Observable filtering, expansion, switching, feedback, and state changes |
| Applicability | Tasks suited to the layout; adaptations for more or less content |

Turn observations into reusable rules. For example, keeping key metrics in the first viewport while retaining their definitions and comparison periods is more useful in a skill than instructing it to place four cards like a screenshot. When the user requests precise reproduction, retain the requested structure.

Different references may solve different problems, with clear ownership. For example, use A's layout and B's table organization while applying the project's established typography and controls. Select deliberately among their colors, corner radii, and shadows rather than combining every treatment.

A single static screenshot does not establish hover, keyboard, loading, or narrow-screen behavior. Label reasonable designs for those states as supplemental decisions. Replace reference business copy, data, and identifying marks as required by the current project.

## 4 Shared visual and component rules

### Layout and information hierarchy

- Pages at the same hierarchy level share navigation, content starting positions, title areas, and global action placement. Modules may choose a task-appropriate layout within the main content area.
- Establish clear primary alignment lines. Adjacent headings, containers, tables, and action areas should have understandable alignment relationships.
- Express relationships through grouping. Add a container only when its content needs a separate boundary, background, or actions; avoid wasting space through repeated nesting.
- Make the page's primary action easy to identify and distinguish secondary and destructive actions. Unrelated actions should not all compete for the highest visual emphasis.
- Handle realistic content lengths and quantities. Long headings and names, large numbers, multiple labels, and missing content must not break the basic layout.

### Typography, numbers, and copy

- Reuse type size, weight, and line height for the same semantic level. Use a limited set of purposeful levels for headings, body copy, supporting text, and data.
- Choose coordinated fonts and spacing for mixed Chinese and Latin text, numbers, units, and dates. Consider tabular numerals and consistent alignment for numbers compared row by row in tables.
- Follow one project convention for money, percentages, dates, units, precision, and positive or negative signs. Distinguish zero, missing values, and values not yet loaded.
- Action labels describe concrete actions. Error messages explain what happened and how to continue. Headings and supporting copy serve the current business task.

### Color and shared style values

- Name shared style values by purpose. For example, distinguish page background, container background, primary text, secondary text, border, interaction accent, and status colors.
- Once colors, spacing, radii, and other values are chosen, maintain them centrally in the project. Modules should reference them, retaining existing project names instead of creating a duplicate system.
- A color should not convey contradictory states in adjacent contexts. Pair status colors with text, icons, or other cues so understanding does not rely on color alone.
- Keep chart series colors stable. Use consistent encoding for a metric across charts where possible. Assign accent colors and chart colors according to their different purposes.
- Make text, boundaries, selected states, and focus clearly distinguishable. Check contrast against actual backgrounds, especially pale supporting text and dark themes.

### Shared components

- The same kinds of buttons, inputs, selects, labels, cards, tables, dialogs, and messages share base dimensions and state logic across modules.
- Define names and use conditions for compact, regular, or other necessary variants. Modules use existing variants; explain the concrete need for a new one.
- Use a consistent icon source or visual language. Icon-only actions need understandable names. Provide visible labels or hints when an action's meaning is not obvious.
- Coordinate overlay and fixed-region layers to prevent clipped menus, obscured dialogs, or fixed elements covering focus and primary actions.

## 5 Interaction states and screen sizes

- Complete applicable states for components in scope: default, hover, keyboard focus, pressed, selected, disabled, loading, success, and error. Do not add states that do not apply to a component.
- Distinguish initially empty data, no filter results, loading, load failure, and insufficient permissions. Offer the next action appropriate to each condition.
- Forms identify required fields, field meanings, and error locations. Preserve entered values after validation failures and provide clear feedback after submission.
- Prevent duplicate submissions while an operation is in progress. Provide confirmation or an opportunity to undo deletion, bulk operations, and similar actions according to their actual impact.
- Key workflows must be keyboard operable, with visible focus and clearly named controls. Manage focus appropriately when dialogs open and close.
- Motion explains changes in state or position and respects reduced-motion preferences. Follow global settings for duration and easing.
- Under this project's division of responsibilities, use `gpt-taste` only for public marketing pages, never for Dashboards or business tools. Admin interfaces may retain lightweight feedback and state transitions that support their tasks.
- On narrow screens, prioritize the content and actions needed for the task, adapting arrangement to the content. Tables may use horizontal scrolling, priority columns, or expandable details while keeping field meanings understandable.
- Specify page-level and local scrolling separately. Check that sticky headers, sidebars, and overlays do not obscure content.

## 6 Module responsibilities

The following are optional future divisions of work; creating every skill at once is not required.

| Module | Primary responsibility | Shared foundations inherited |
| --- | --- | --- |
| Application shell | Navigation, title area, content width, overall scrolling structure | Typography, colors, spacing, shared components |
| Dashboard | Metric priority, chart selection, overview layout, data interpretation | Application shell, cards, numeric and chart styles |
| Data lists | Tables, search and filters, sorting and pagination, bulk actions | Controls, density, state presentation, numeric conventions |
| Forms and settings | Field groups, entry flow, validation, saving, feedback | Typography, controls, spacing, messages, overlays |
| Detail pages | Information groups, status, related data, action entrypoints | Application shell, components, information hierarchy |
| Visual refinement | Inspect the current page and fix specific visual or interaction issues | Established project style and module intent |

A skill warrants an independent boundary when it has a distinct use case and method. Button radii, a particular palette, or one industry example generally belong in shared settings or module references.

Each module skill states its use cases, required inputs, design decision method, deliverables, relevant references, and necessary checks. Add reference examples, code templates, or assets only when needed.

## 7 Collaboration across chats and updates

Use these foundations and available project module records as shared context. Other chats can reliably continue a decision only after it is recorded in project files. Authoring records from the original repository are optional context and are not required to use a distributed skill.

When creating a module:

1. Read these foundations and any existing relevant module records, then check the global visual settings.
2. Examine the current references, extract the characteristics the user wants, and establish the local scope.
3. Complete the current module's skill or interface output, reusing established shared settings.
4. Record new or changed decisions and actual output locations in the target project's module notes, for example `design-system/modules/<module>.md` when that convention is used.
5. If the request explicitly affects the product's global style, update its design records and tokens, naming affected modules and what was actually synchronized. If it changes the general rules of this skill series, update the relevant foundation entries, status, version, and history.

Keep module records focused on information that helps future work. Useful fields include:

| Field | Content |
| --- | --- |
| Module and scope | Tasks and page areas covered |
| Reference sources | User-provided links, file locations, or reference descriptions |
| Adopted characteristics | Layout, style, or interaction choices and their conditions of use |
| Shared settings | Inherited global decisions, with foundation version when needed |
| Local decisions | Module-specific variants, estimates, and supplemental designs |
| Global impact | Shared components or settings affected; modules requiring synchronization |
| Delivery and verification | Skill, example, or interface locations; checked behavior and outstanding work |

Record accessible locations for references needed across chats. Do not assume another chat can read an attachment visible only in the current conversation. Archive available files and record their locations; otherwise preserve sufficiently specific observations and source descriptions.

Different chats should edit their own module records and skills where practical. Reread a shared file before changing it and edit only relevant entries. When edits overlap, retain valid decisions from other tasks and resolve the specific conflict.

Maintain one authoritative set of foundation rules, with the English edition as the maintenance source and the Chinese edition synchronized to it. Skills in this distribution refer to these foundations. When distributing a skill separately, include the necessary excerpts and identify their source version; check whether those copies need synchronization after updates.

## 8 Delivery checks

Check the items relevant to the actual task without adding work for unaffected modules:

- The main task and actions are clear, and the information hierarchy supports the user's needs.
- Explain how references were used, distinguishing temporary choices from global decisions.
- Typography, colors, spacing, controls, and states follow established shared settings.
- Layout remains usable with long text, large numbers, missing content, and different data volumes.
- Applicable empty, error, loading, and keyboard states are addressed.
- For interface implementation, inspect actual rendering, required screen sizes, and primary actions. When writing only specifications or skills, check rule clarity and resource links.
- Module records, delivered artifacts, and global settings agree. State what remains unverified; do not report unperformed checks as passed.

History:

- 2026-11-14, 0.2: Expanded coordination between authored and external design skills; added independent token ownership for each product, region-specific motion rules, and the orchestration plan link. No specific brand color or font was selected.
- 2026-11-14, 0.1: Established shared rules, reference-analysis methods, and collaboration across chats; visual settings await later references.

The distributed Dashboard skill includes necessary excerpts from version 0.2. Use the current foundations within the project. The original version 0.1 snapshot remains in the authoring repository's research archive and is not a runtime dependency. Check excerpt content and source version before future releases.
