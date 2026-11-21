# Case index

Snapshot: VoltAgent/awesome-design-md at `fcc70284932276d085f01ef9f83edde90b1258cb`, reviewed 2026-11-14 and expanded 2026-11-21. 84 source records; twelve document-reviewed local cards; 72 indexed-only records with unknown scope. No card claims current-site verification. This is a case library, not an official company-design-system catalog.

## Reviewed candidates

Read only the cases useful for the current task. These labels describe the inspected document's scope, not the whole company.

| Case | Surface scope | Useful dimensions | Important limit |
| --- | --- | --- | --- |
| [Linear](cases/linear.app.md) | Marketing | Dark surfaces, restrained accent, product imagery | Homepage product screenshots do not establish application workflows |
| [Stripe](cases/stripe.md) | Marketing, registration, illustrative composites | Gradient placement, CTA hierarchy, numeric typography | Inspired interpretation; no complete dashboard coverage |
| [Notion](cases/notion.md) | Marketing and pricing | Feature grouping, action/link distinction, pricing information | Not the editor/database UI; timing includes recommendations |
| [IBM](cases/ibm.md) | Enterprise marketing | Flat square surfaces, light display type, clear bands | Actual product tables/menus and full dark theme are missing |
| [SAP](cases/sap.md) | Marketing-like surfaces and illustrative SaaS examples | Quiet chrome, flat bands, equal-size type roles | No concrete source-page list; examples are not brand-native |
| [Vercel](cases/vercel.md) | Marketing and auto-derived examples | Neutral hierarchy, technical type roles, spacing rhythm | `ex-*` surfaces are illustrative, not verified shipped components |
| [Airbnb](cases/airbnb.md) | Marketplace search and details | Image/information balance, search, booking action placement | Loading, precise hover, full error states unobserved |
| [Kraken](cases/kraken.md) | Unspecified white-background website | Purple action roles, buttons, badges | Limited detail; breakpoint list has no reflow rules |
| [Sentry](cases/sentry.md) | Developer marketing and pricing (inspired) | Dual-polarity dark violet + white surfaces, focus ring, code pairing | Inspired analysis; does not verify live issue-triage tables |
| [Supabase](cases/supabase.md) | Platform marketing and UI mockups (inspired) | Quiet monochrome chrome, single emerald CTA with dark ink | Inspired analysis; does not verify live Studio SQL/table workflows |
| [PostHog](cases/posthog.md) | Developer marketing, docs, and analytics cards | Warm cream canvas, white bordered cards, soft/strong semantic badges | Does not verify live query builders or session replay |
| [Raycast](cases/raycast.md) | Marketing modeled on command-palette chrome | Disciplined near-black surface ladder, 1px hairlines, 15%-alpha category badges | Does not verify desktop keyboard trees or light-theme equivalents |

For a complete business Dashboard, permission-aware list, keyboard flow or interaction contract, these twelve cards supply at most scoped visual candidates. None provides a verified full operational workflow. [Selection rules](selection.md) explain fallback and claim-level evidence. [Patterns](patterns.md) compare transferable relationships only when needed.

## Find another named source

Open only the alphabetic shard covering the exact source ID. Each has 21 records. Unknown scope stays unknown until the source has actually been read; indexed-only cases require online source access or user-supplied material for further analysis. The twelve cards above work offline.

| ID range | Metadata file |
| --- | --- |
| `1win` through `expo` | [catalog-01.csv](catalog/catalog-01.csv) |
| `ferrari` through `mydealz` | [catalog-02.csv](catalog/catalog-02.csv) |
| `nerdwallet` through `sentry` | [catalog-03.csv](catalog/catalog-03.csv) |
| `shopify` through `zapier` | [catalog-04.csv](catalog/catalog-04.csv) |

Names use upstream IDs, including `linear.app`, `mistral.ai`, `opencode.ai`, `together.ai` and `x.ai`. Case-insensitive brand matching is fine; do not silently match an unrelated product.

CSV fields: `id`; `review_status`; semicolon-separated `surface_scope` and `tags`; package-relative local `card` (empty for indexed-only); upstream `source_path`; pinned `source_url`; original-file `sha256`; original-file `bytes`. Metadata identifiers stay in English in both editions to preserve matching. Hashes identify the original source, not the adapted case card. See [provenance](../UPSTREAM.md) for license and updates.
