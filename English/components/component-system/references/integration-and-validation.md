# Integration, cross-page reuse and verification

Read for orchestrator handoff, multiple consumers or delivery checks. Use an existing project record; no new manifest or document bureaucracy is required.

## Handoff contract

Incoming context should establish the region and task, allowed edits, page/component owners, installed stack/library, theme location, requested references, behavior/device constraints and expected output. Locate facts in the project before asking the user. Absent specialists are optional: complete ordinary requirements using this skill and available methods.

Return only relevant facts:

| Item | Useful handoff |
| --- | --- |
| Components | Reused imports, shared implementation locations, changed files, new components and consuming pages |
| Contract | Props/value types, stable identifiers, events, composition points and ownership of requests/state |
| Variants | Name, use condition, difference from existing choices, supported combinations, defaults and allowed per-page differences |
| Tokens | Authoritative source; existing mappings; proposed shared additions with reason and affected components/pages |
| Responsibilities | Page lead's business content, behavior rules received or filled, responsive decisions, one integration owner; the current implementer may perform all these roles |
| Evidence | Checks actually executed and their scope, results, limitations and any migration still needed |

The orchestrator consolidates shared-token changes, with global style generation/validation where available. Without a controller, make only needed project-scoped additions in its existing authoritative source and document their purpose and consumers. Do not invent a library-wide palette. For local fixes with a complete theme, no new token process is required.

Existing overlay specialists own overlay selection and behavior; this module integrates shared interfaces and consumes their implementation. If an overlay implementation is already adequate, reuse it. Shared Modal behavior covers naming, focus entry/containment/return, dismissal and pending-operation rules as applicable; within the agreed interaction rules, initial focus can differ with the task and risk. Record intentional differences instead of forcing every Modal to focus the same control. A component task may enter this skill directly; discovering every other module is unnecessary.

## The three task classes

| Task | Exercise | Observable result |
| --- | --- | --- |
| Reuse existing components | Implement the requested area using its existing Button/Field/Select or equivalents, including a real form or action path | Original imports/API/theme are preserved; values and event payloads remain correct; actual results drive feedback; no redundant wrapper/library |
| Add a purposeful variant | First compare available sizes/variants; add only a demonstrated gap, then inspect ordinary and changed contexts | Variant has a task-based name/use condition; coordinated anatomy and token mapping; no global default change; applicable focus, pending, disabled and error behavior remains usable |
| Use across pages | Consume the same implementation in distinct pages such as a dense list and a settings/detail view | One public import and event meaning; explicit density/emphasis choices; no copy divergence; theme and content differences handled; independent instances do not share accidental state |

For a skill-only authoring task, run realistic scenario walkthroughs against the entry and resources. These evaluate decision guidance, not a rendered implementation. For implementation tasks, execute appropriate available checks on the changed code and relevant callers. Do not declare runtime verification from a source reading or a passing metadata validator.

## Check what changed

When adding cross-page consumers or changing a shared implementation, interface or theme, use the affected callers to select representative rendered checks covering the changed variants and theme contexts. Compare the shared base contract and permitted differences; include a Portal/Modal path and focus return when affected. Record the chosen pages, states, actions and actual outcomes so one successful caller does not stand for all contexts. Local reuse with no shared change needs checks of that use, not an unrelated site-wide audit or a mandatory specialist handoff.

- **Token inheritance:** inspect actual source and generated values; check a consumer in every affected theme. Include a portal/Modal/message path if touched, since it may escape theme context. New values name a use, not a screenshot color.
- **Interface consistency:** verify controlled changes and initial values, event payload/timing, stable row/option keys, native attributes and focus access. Preserve current library naming. Check existing consumers of a changed public API.
- **Content and geometry:** long/multilingual text, large numbers, zero/missing values, repeated labels, empty data and multiple instances; no clipping at relevant widths or text enlargement. Dense visual controls still need usable targets.
- **Behavior:** applicable keyboard actions, focus visibility/return, chosen/expanded state, pending/duplicate prevention and recovery. Test real success and failure; animation completion is not success.
- **Device and effects:** relevant viewport/input modes, overflow/stacking, reduced motion and static fallbacks when affected. Do not claim exhaustive device or assistive-technology coverage from one browser.
- **Maintainability:** no duplicated component or parallel token store, no private DOM styling dependency introduced without need, examples match the current contract, scope of impact is stated.

Use existing type/build/component tests or an appropriate manual flow. Add targeted tests only where they exercise meaningful new behavior. A textual specification may need no code sample; if executable examples are included, run them with their stated dependencies and report the actual extent.

## Updating this skill with new references

Append provenance, actual observations, adopted rules, local differences and checks to the author's module record/research archive. Update the relevant rule instead of growing a mandatory reference list. Keep raw images, full transcripts and research outside the distribution. Preserve source-version and authorization context for any code actually reused. Keep both authored language editions semantically equivalent, with identical identifiers and file topology; record hashes only after semantic review.
