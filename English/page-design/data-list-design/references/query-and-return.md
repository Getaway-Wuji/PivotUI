# Query and return

## State contract

Maintain distinct state for draft inputs, the applied query, presentation preferences, selection and jobs. A useful query contract includes filters/search, stable ordering, page or cursor, page size and any data version used by the API. Identify what is shareable in the URL and what belongs in session/user preferences; avoid putting sensitive query values into URLs or broad shared storage.

| Event | Required decision |
| --- | --- |
| Apply a different search/filter | Commit the query, reset to its first valid page, and clear or explicitly reconcile selection |
| Reset query | Restore defined query defaults; do not silently reset unrelated column/view preferences |
| Change sort or page size | Show the new order/size, choose a valid position, and state the selection policy |
| Change page | Preserve the applied query; distinguish current-page selection from retained IDs on other pages |
| Receive an older request | Ignore/cancel it so it cannot replace the current query's results |
| Data count shrinks | Clamp to a valid page or cursor, explain the adjustment, and retain the query |

Use stable record IDs for row keys and operations, never row indexes. Server sorting/pagination must cover the same result universe as counts and filtering; sorting only the loaded page must not look like global sorting. Use a stable tie-breaker. For cursor APIs, preserve usable cursors and explain invalidation instead of inventing an exact page number the API cannot support.

## Result states

Initial loading, background refresh, no records, no matches, denied access and load failure require different presentations. Keep applied filters visible during no-match and failure states. A no-match action clears relevant criteria; an initial-empty action may create/import if authorized; denied access explains the available access path without disclosing hidden records. Failed refresh may keep old rows marked as stale. Do not label failed or denied requests as zero results.

Keep a persistent error/retry area for failures and preserve user input. Choose announcement semantics deliberately; an update should not steal focus or announce every keystroke. Update counts and pagination only from the response that belongs to the current query.

## Detail round trip

Before navigation, capture applied filters, sort, page/cursor and size, relevant view/columns, a stable origin record ID, and the page/local scroll anchor. Preserve drafts separately if unfinished input is expected to survive. Use the product's router/history or scoped state store so browser Back works as well as a visible return link. Choose persistence lifetime explicitly; do not depend solely on a mounted component remaining alive.

On return:

1. Restore query/presentation state before fetching or rendering the list. Refresh according to the product's freshness rule without erasing the restored context.
2. Resolve a valid page and the origin record after data arrives. Restore scroll and focus once the target exists; focus with scroll control so it does not undo the restored location.
3. If deletion, permission changes or reordering removed the origin, use the nearest meaningful row or results heading, announce the change, and preserve remaining query context. Do not restore an obsolete action or selection blindly.

A direct detail link with no list history needs a predictable fallback list route. Keep the return destination internal and validated. Returning from detail does not rerun a completed batch job. Selection restoration is a separate product decision: if retained, recheck eligible IDs and show scope; if cleared, communicate it.

Test a filtered later page, changed sort/page size, browser Back, visible return control, and a removed origin. An unchanged input box alone does not prove the query, page and position were restored.
