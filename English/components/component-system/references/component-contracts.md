# Component contracts and reuse decisions

Read when extending an interface, adding a variant, or making a component shared. These are design decisions to express through the project's current framework, not a mandatory new props schema.

## Choose the reuse level

| Evidence in the target project | Action | Preserve or establish |
| --- | --- | --- |
| Existing component covers the task | Use it directly | Import, theme, event meaning, keyboard behavior and form binding |
| Existing size, variant, theme slot, or composition covers it | Configure that capability | Supported API; no deep selectors against undocumented internal structure |
| Several callers need the same stable assembly or library adaptation | Compose a shared part or a thin adapter | One implementation, clear inputs/events, accessible names and focus/ref access |
| A required semantic or behavioral capability is absent | Build the missing part on suitable primitives | Explicit ownership, applicable states, device behavior, examples and checks |
| A layout is specific to one page or likely to change with its content | Keep it local | Page ownership; extraction later if a stable reusable contract emerges |

Inspect nearby callers before introducing a wrapper. A wrapper earns its place by enforcing a real product rule, adapting incompatible contracts, or composing repeated behavior; merely renaming every upstream prop creates another API to maintain. If source-copy components are used, adopt a single project-owned copy and record provenance. Do not scatter edited copies among pages.

## Describe a contract only as far as needed

For an affected component, capture:

- **Purpose and anatomy:** what task it serves; required and optional parts; which part owns the accessible name, value, action, or content group.
- **Inputs and ownership:** value type, stable identity, initial value, controlled/uncontrolled mode where supported, and who owns requests and validation. Avoid two competing stores for the same value. Do not silently switch control mode during a component's life.
- **Events:** trigger, payload, timing, and source of truth. Selection change, submit requested, operation completed, and animation finished are different events. Preserve the installed library's event semantics.
- **Composition:** supported content slots, native attributes, accessible descriptions, focus/ref APIs, and styling hooks. Expose what consumers actually need without making private DOM structure public.
- **Variants and states:** intended use, defaults, supported combinations, state precedence, and what remains constant across variants.
- **Consumers and change scope:** public import, current callers, integration owner, and migration needs if the contract changes.

Generic Select and Table primitives accept data and callbacks; project-specific requests, permissions, navigation and business validation belong to the page or a clearly named domain wrapper. Preserve the project's existing form controller rather than creating a second value store inside Field.

## Distinguish the variant axes

| Axis | Decision it expresses | Example of a valid reason |
| --- | --- | --- |
| Intent/role | What the action or status means | Destructive action versus ordinary action |
| Emphasis/appearance | Priority against nearby content | Primary action versus low-emphasis utility action |
| Size | Proportions appropriate to content and device | Toolbar control versus prominent call to action |
| Density | Amount of space within a repeated region | Compact desktop data table versus comfortable settings form |
| Composition | Different information or control structure | Split action; a button with secondary explanatory text |
| Runtime state | What is happening now | Pending, selected, invalid, disabled; not permanent style variants |

Use the project's names. `small`, `sm`, `mini`, or `default` are not interchangeable API values across libraries. Map concepts at an adapter boundary only when needed. A library's `type` may mean appearance while another's means native submit behavior; preserve both meanings explicitly. Do not introduce boolean combinations such as `small && large` or a `blueRoundSavingButton` variant.

Define applicable state combinations: pending may prevent a second action while retaining its label; selected can coexist with focus; an invalid field may contain a nonempty value; readonly is not disabled. A disabled state needs no invented hover behavior. Business unavailability, lack of permission, and an in-flight action may need different explanations. Follow the agreed interaction model for whether a submit stays enabled for validation.

## Treat size as a relationship

A size recipe couples line height, block padding, border, icon box, inline gap and visual alignment. A useful content-based relationship is:

`control block size >= max(text line box, icon box) + block padding + borders`

The actual minimum follows the product's theme and input-device constraints. Multi-line content may grow; a fixed height must not clip translation or text enlargement. The hit target can extend beyond the visual shape if it does not overlap neighbors. Do not reduce focus indicators or operability to obtain compactness.

Pair adjacent controls by their visible baseline and control box. If a compact table embeds Button and Select, choose compatible existing sizes or a justified scoped mapping. Do not independently shrink row height, field height and icon size. Preserve horizontal padding and readable labels where vertical density changes. Use logical spacing properties when the project supports bidirectional content.

## Three small contract examples

These are illustrative specifications, not executable component code or required names.

| Example | Stable contract | Intentional variation | Business owner |
| --- | --- | --- | --- |
| Action button used in an order list and settings | Existing `Button` import; native action semantics; current click/press event; pending tied to actual operation; accessible name retained | Existing size/emphasis per context; destructive intent only for destructive action | Caller executes action and reports result |
| Filter select | Stable option ID separated from label; value/change contract; clear value specified; open state separate if controlled | Single/multiple and local/remote search are explicit capabilities, not decorative skins | Page controls query, options and response ordering |
| Entity table shared by two lists | Stable row identity; column definitions and cell rendering; explicit sorting/paging/selection ownership; empty/loading/error slots | Existing density; scoped column visibility or overflow strategy | Page provides domain columns, requests and row actions |

For a new compact variant, record its need (for example, repeated controls in a desktop data toolbar), whether existing sizes suffice, mapped tokens, affected parts, allowed contexts, and checks. A temporary one-page padding adjustment is not automatically a new public token. For a public API change, inspect consumers, provide migration or a compatible adapter where justified, and update examples together.
