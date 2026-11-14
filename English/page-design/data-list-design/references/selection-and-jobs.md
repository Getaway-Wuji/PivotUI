# Selection and jobs

## Specify the selected universe

Support only scopes the product can execute. A simple list can select explicit IDs across pages without offering every matching result.

| Scope | Representation and visible meaning |
| --- | --- |
| Current page | Header checkbox selects eligible records on this loaded page; count excludes ineligible rows |
| Explicit records across pages | Stable selected IDs, total count and a way to inspect/clear them; the page checkbox reflects only eligible visible rows |
| All matching results | Explicit user transition after page selection, query snapshot/token or clearly described live-query semantics, count and exclusions |

Show checked/unchecked/indeterminate state correctly. Explain why a visible row cannot be selected without revealing forbidden information. When moving to all results, say what will be included and whether subsequently arriving records are included. For a destructive operation, prefer a server-resolved snapshot or preflight confirmation of scope; a client list of loaded IDs is not all results.

Changing filters must clear selection or obtain an explicit reconciliation; never silently broaden it. Sort/page changes need a consistent retention policy. With all-results scope, unchecking one record creates an exclusion rather than switching unnoticed to the loaded page. Distinguish matching count, eligible count and selected count when they differ.

## Batch task lifecycle

Before submission show action, scope/count, eligibility constraints and consequential effects. Use the inherited risk-based confirmation: irreversible deletion uses Modal, while low-risk local confirmation may use Popconfirm. Never use Tooltip for confirmation. Keep permissions enforced by the backend; disabled UI is explanatory, not security enforcement.

Capture an immutable submitted scope and prevent duplicate submission. For long jobs, show a durable job identity/status and provide a return path; leaving the page or closing a view is not cancellation. Offer cancellation only if the backend can honor it. Resolve an unknown timeout outcome via status/idempotency before retrying a possibly successful operation.

Report succeeded, failed, skipped and still-unknown records distinctly. Keep reasons and a usable failed-record list in a persistent results region; errors do not belong in Toast under the shared convention. Clear successful IDs from retry selection, retain eligible retryable failures, and retry only those IDs. Recheck authorization and changed records. Do not promise undo without real support or reapply successes to make a summary look clean.

Refresh affected data, counts and valid pagination after a completed mutation while retaining the query. If the triggering control disappears, move focus to the persistent outcome heading or another meaningful location.

## Export is a separate scope decision

Name the supported export scope: current page, selected records, or all matching results. Do not infer it from a generic Export label or a stale selection. Before execution make the scope, count/estimate, included fields and ordering understandable. Visible columns and exported fields are distinct choices; state whether export uses the current columns or a defined schema. Apply permissions and relevant query snapshot consistently.

For large exports, preserve a job/status path and the actual download result, with retry and expiration behavior where supported. A generated file or completed server job is success evidence; a timer ending is not. Protect text fields in spreadsheet-compatible exports from being interpreted as formulas, and follow the product's data-handling rules. Demo exports must identify their synthetic data and local-only behavior.
