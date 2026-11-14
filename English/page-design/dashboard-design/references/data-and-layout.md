# Metrics, Charts, and Layout Methods

This guide distills sources including S26–S37 and adds design methods; it does not claim the screenshots implemented this behavior. Choose the A–G structure with [selection-guide.md](selection-guide.md), then check data and layout here. See [visual-recipes.md](visual-recipes.md) for themes. Existing project standards and components take precedence; these choices are not global user preferences.

## 1. Define metrics before drawing cards

Define at least the following for each major metric. Definitions or detail views can carry this information; it need not all fit inside the card body.

| Item | What to establish | Design consequence |
| --- | --- | --- |
| Name and question | The business question answered | Title, first-screen priority, and whether it belongs |
| Value and unit | Currency, count, duration, capacity, or ratio | Keep units beside values; do not total currencies without conversion |
| Calculation | Sum/deduplication/mean/median; ratio numerator and denominator | The same label must not conceal different definitions |
| Scope and time | Object, organization, region, audience, timezone, start/end | Match filter state and chart range |
| Comparison baseline | Previous period, same period last year, budget, or target | Name the comparison beside the change |
| Business direction | Higher is better, lower is better, valid range, or descriptive only | Status semantics are not determined by sign alone |
| Update and source | Source, last successful update, expected delay | Freshness cues and whether conclusions are justified |
| Next action | Definitions, groups, details, or an object to handle | Make a card clickable only when a real destination exists |

- Consider denominators and sample sizes: `10/20` and `1,000/2,000` are both 50%, with different reliability and impact.
- State whether averages are weighted by records, users, days, or another entity. Do not average group percentages directly into overall conversion.
- Year-over-year compares the corresponding prior-year period; period-over-period compares the previous comparable period. “Compared with last month” is clearer than “↑12%” alone.
- Change rate usually uses `(current−baseline)/baseline`. When the baseline is zero or negative, do not mechanically show a misleading percentage; use absolute change and explanation, or a business-defined method.
- Moving from 20% to 25% adds 5 percentage points and is 25% relative growth. Labels must distinguish `%` from percentage points.
- Label incomplete periods “to date.” Explain comparisons against a full prior period, or compare the same elapsed portion, to avoid false growth claims.
- Declines in refund rate, error rate, or latency may be improvements; declining revenue is usually unfavorable. Use neutral language when the direction is unknown instead of automatic red/green.
- Targets, thresholds, severity, and business findings require data or business-rule sources. Without a target, do not show completion; without a basis, do not label something anomalous.

### Select first-screen metrics

Work backward from the user's decision: first choose outcome metrics, then metrics that explain change or reveal costs. For example, revenue growth may be accompanied by gross margin or refunds so a total does not hide problems; add these only when relevant to the role's task. Put supporting metrics in explanatory areas and merge metrics repeating the same fact. Metric count follows decision value and readable space, not a fixed four-card layout.

Organize cards as needed around name + value/unit + period + comparison/status. Definitions, provenance, and update details can live in explanations. Targets, growth rates, sparklines, and buttons are conditional. Without history, show the current value; without a denominator, do not invent a percentage.

## 2. Distinguish data states

| State | Representation and action |
| --- | --- |
| Known zero | Show `0` and its unit; include zero in applicable calculations |
| Missing/not applicable | Show `—` and explain which; do not calculate it as zero |
| No data yet | Explain what produces data; provide existing connection or creation paths |
| No filter results | Preserve filters and allow clearing or relaxing them |
| Loading | Preserve layout dimensions and show feedback; do not animate fabricated counts |
| Load failure | Preserve useful context, identify the failed area, offer retry |
| Partial success | Show successful areas and identify failures separately; do not imply a full successful refresh |
| Stale/disconnected | Show last successful update and status; label cached data as previous results |
| No permission | Explain that the area is unavailable; do not leak restricted data through aggregates, hints, or exports |

Show missing chart points as gaps or missing markers rather than automatic zeroes. Clearly distinguish forecasts, estimates, and interpolation from observations. Numbers from references are usable only as labeled examples.

Distinguish delivery type first: real-data interfaces follow actual sources; concepts/prototypes may use labeled, internally consistent demonstration data while retaining metric definitions and future connection conditions. Required core modules without data show “not connected/configured.” Omit only optional analysis without business support. A visual example does not prove a live data capability.

## 3. Choose charts from business questions

| Question | Preferred representation | Preconditions and boundaries |
| --- | --- | --- |
| How does it change over time? | Line; light area when magnitude matters | Consistent time granularity; preserve real peaks and gaps |
| Which objects are higher/lower? | Sorted horizontal bars or dot plot | Horizontal bars suit long names; include values for precise reading |
| How far is current performance from a baseline? | Grouped bars, dot plot, difference bars, or reference line | Comparable units, definitions, and periods |
| What makes up the total? | Stacked bars; donut for a few categories | Mutually exclusive categories covering the same whole; not all percentages add |
| How do group shares change? | Percentage-stacked bars | Also show sample size/total to reveal scale differences |
| How are values distributed? | Histogram, box plot, or quantile summary | Enough individual observations; define bins or quantiles |
| How do ranges or uncertainty change? | Range bars, bands, or error bars | Actual upper/lower bounds; label min/max, forecast range, or statistical interval distinctly |
| Do two measures vary together? | Scatterplot | Paired data for the same entity; correlation is not causation |
| At which step do users drop out? | Funnel or step-conversion bars | Fixed ordered steps, deduplication definition, conversion window |
| Where do users/resources flow? | Sankey or path diagram | Nodes, links, and flows; branching is the actual question |
| How far from a target? | Target bar, bullet chart, value plus target line | Real target, period, and actual value using the same definition |
| How do cohorts change? | Cohort heatmap | Clear entry cohorts and relative observation periods |
| How does location matter? | Map plus object details | Position, distance, routes, coverage, or regional patterns affect judgment |
| Which record needs action now? | Ordered queue/table with states | The list itself is the best representation; a chart is not required |

- Sparklines show direction; main trend charts also need time, units, and baselines. Do not reuse one decorative curve for every KPI.
- Bar length comparisons start the value axis at zero. For small differences, use dots or difference charts with clearly marked ranges.
- Keep one unit and an interpretable scale per axis. Prefer aligned small multiples for different units. Necessary dual axes must explicitly identify axes, units, and series relationships without implying unsupported synchrony.
- Side-by-side small charts normally use comparable time ranges and value scales. Independent scales show each trend only and must be clearly marked; similar curves must not imply equal magnitude.
- Stacked areas show total and composition trends. For precise changes in intermediate series, use small multiples or separate lines.
- With many categories, use rankings plus “Other” or searchable details. Explain aggregation rules and how they relate to the total.
- Circular progress suits a few targets not requiring precise side-by-side comparison. Prefer bars for multiple targets, and retain true values beyond target.
- Dot matrices support approximate scans of completion or people distribution. Define the count per dot and include a summary. Use bars/details for precision; decorative dot counts must not impersonate records.
- Sankeys support branching and flow exploration. Fixed-path drop-off is more directly shown by a funnel. Node totals alone cannot establish links.
- Use rankings when regions differ only in rank; maps are not filler. Choose total-versus-rate color encoding from the question and denominator.
- Do not hide histogram boundaries, scatterplot outliers, or future/unobserved heatmap periods merely to make charts tidy.
- Smoothing, motion, and gradients must not change value positions, peaks, target lines, or selection results. Necessary legends and labels cannot depend solely on hover.

## 4. Establish primary and supporting areas

List “business question → required data → representation → next action” before placing blocks. Merge or remove modules without an independent question.

- The primary area answers the page's highest-priority question. Charts need complete scales and sufficient plotting space; task queues/content cards need room for recognition and actions. Supporting areas explain sources, groups, or consequences.
- Business overviews may follow “results → main trend/target gap → contribution/exceptions → details.” Diagnostic analysis puts filter context and the main analysis first.
- Monitoring puts exceptions, impact, and freshness first. Workspaces put tasks and deadline risks first. KPIs need not always sit at the top.
- Narrative titles can state supported conclusions. With insufficient evidence, use a neutral topic/question while retaining chart definitions and sources.
- Peer metrics share dimensions; enlarge one only for clear business importance, not because its number is short.
- Summary lists retain fields needed to identify an object, judge status, and open details. Full filtering, pagination, and bulk actions belong in list views.
- Consider a separate container when a region owns filters, scrolling, actions, or independent state. Related information may instead use whitespace and rules.
- Do not default to AI assistants, welcome banners, rankings, or upgrade promotions. Give them first-screen area only when the task needs them.

### Turn information relationships into layout

| Reading path | Possible composition | Reason |
| --- | --- | --- |
| Results, then explanation | Top metric strip; wide trend area plus narrow contribution area below; then summaries | Results and causes remain adjacent; details do not compete with the main trend |
| Decide what to do first | Primary task/calendar area; side deadline risks and workload; secondary statistics later | Operational objects have room; statistics support execution |
| Handle exceptions first | Update status and key exceptions on top; event queue beside relevant trends | Selecting an event immediately exposes evidence and actions |
| Find content first | Search/categories on top; cards or lists primary; selected details expand as needed | Actual content fields identify objects; no forced KPI strip |

These are starting compositions, not fixed widths or module inventories. Align headings, inner edges, and plotting areas across primary/supporting regions. Repeat internal order for similar cards; emphasize key regions with area and position. Narrow screens preserve the same reading path.

## 5. Density and alignment

- Choose density from reading frequency, decision complexity, and object count: reports emphasize hierarchy, routine analysis emphasizes comparison, monitoring emphasizes status and response.
- Establish the content origin after navigation and the main/supporting columns. Organize card edges, headings, and plots along a few clear alignment lines.
- Use unequal grid widths for multiple modules, with more space for primary areas. Align the start of modules in a row without filling them with useless content to force equal height.
- Build compact/regular variants from existing project spacing, controls, and text scales; do not independently shrink every module's typography.
- When too dense, remove repeated metrics, reduce redundant legends/decoration, and move secondary content into drill-downs before adjusting spacing. Retain labels and units.
- Chart space must accommodate data, axes, annotations, and interaction. Enlarge or rearrange containers when headings/filters grow; do not squash charts into thin strips.
- Example counts, widths, and module quantities are not rigid rules. Reallocate space around the primary question as content volume changes.

## 6. Rearrange for desktop, tablet, and mobile

Breakpoints follow where real content becomes crowded; reuse existing project breakpoints. These are arrangement principles, not universal pixel values.

| Screen condition | Arrangement | Preserve |
| --- | --- | --- |
| Wide desktop | Main + supporting areas; multiple metric/comparison columns when useful | Complete main-chart scales, filter scope, exceptions, detail links |
| Tablet/medium width | Fewer parallel columns; supporting regions follow the main chart; wrap long filters | Main task order and selected conditions |
| Mobile/narrow | Single-column task flow; metrics grouped by priority; complex exploration in details | Key values, exceptions, units, periods, main actions |

- DOM, reading, and keyboard order must match task priority. The visually first element must not become the last accessible element after rearrangement.
- Collapse secondary explanations, long details, and advanced filters when useful; do not hide exceptions, required units, or meaning-defining baselines by default.
- When filters collapse into a panel, retain a selected-scope summary and clear action on the page. If there is an Apply button, distinguish draft from applied values.
- On narrow charts, reduce tick count, shorten visible labels, or emphasize selected series while retaining access to complete information. Do not scale everything down proportionally.
- Multi-series charts may switch series, use small multiples, or offer a summary table. Tables needing horizontal comparison may scroll locally while retaining key identifier columns.
- Maps, Sankeys, and complex calendars can begin with mobile summaries/lists and open dedicated views. Core tasks must not require dragging or hover.
- Mobile must expose the same critical details and actions as desktop. A touch press must not trigger two mutually exclusive behaviors.

## 7. Scrolling, long Chinese text, and large numbers

- Prefer clear page scrolling. Add local scrolling only for queues, detail tables, logs, or similar independently viewed content, and show its boundaries.
- Avoid nested scrolling layers. Sticky navigation, headers, and action bars must not cover headings, final rows, menus, or keyboard focus.
- Allow natural Chinese heading wraps. Give long labels more horizontal space, stack them, or add explanation rather than rendering one character per line.
- Do not reduce key object names to ellipses alone. Truncated list names need complete-name/details access by touch and keyboard.
- Use consistent grouping separators, precision, and units for large numbers. For compact notation, label scales such as ten-thousands, hundred-millions, or `k`, and provide exact values. Do not mix incompatible conventions across cards.
- Keep values near units; currency symbols and signs must not wrap onto isolated lines. Align table numbers consistently; tabular numerals may help.
- Check long Chinese text, very large numbers, negatives, zero, empty values, multiple tags, and longer lists. Short English labels and tidy examples alone are insufficient.

## 8. Filter scope and freshness

- Distinguish page-wide filters, regional filters, and single-chart selections. Position, headings, or selected-condition labels must communicate scope rather than implying universal linking.
- Changing a store/greenhouse/account updates all related data and headings. Explicitly label modules aggregating across entities as global information.
- Drill-downs carry relevant time, entity, audience, and selection context. Return paths restore a reasonable context instead of unnecessarily clearing the analysis.
- Retain old values during refresh when useful, but mark updating. Identify differing time batches; do not claim the whole page is current while mixing old/new data.
- Automatic refresh preserves open details, selections, and scroll position. High-frequency queues may pause updates and indicate new data.
- Choose long-series granularity for the task. State hourly/daily grouping and aggregation such as sums or means; averaging must not hide monitoring spikes. Large event sets use summaries and continuable queues; a few visible rows must not imply completeness.
- Time labels follow the agreed timezone and granularity. Today, last seven days, calendar week, and rolling windows differ; selection copy should say which.
- Empty filters, failures, partial updates, and stale states follow section 2. Do not label all problems “No data.”

When saving views, sharing, or exporting is required, preserve organization/object, period, filters, baseline, and data cutoff. State whether sharing creates a live view or fixed snapshot. Exported headings, units, legends, and necessary notes must stand alone. Saving layout and saving filters are distinct actions; add only the needed features.

## 9. Semantic style values and completion checks

These names are optional when no convention exists. Reuse project names rather than creating a duplicate system; do not turn sample colors into global preferences.

| Semantic purpose | Optional names | Relationship |
| --- | --- | --- |
| Surfaces and boundaries | `surface.page`, `surface.panel`, `border.subtle` | Distinguish page, modules, necessary boundaries |
| Text | `text.primary`, `text.secondary`, `text.muted` | Secondary text remains readable; pale text must not conceal definitions |
| Interaction | `action.primary`, `selection`, `focus` | Stable selection, primary-action, and focus expressions |
| Business status | `status.good`, `status.warning`, `status.critical` | Pair with text/symbols; interpret rises/falls from business direction |
| Data series | `chart.series.*`, `chart.reference`, `chart.target` | Preserve metric encoding across charts; distinguish baselines and targets |

Before delivery, confirm that the main question matches the main content; metric definitions/units are traceable; targets/exceptions have support; filters match data; states are distinct; long content and target devices remain readable. For specifications, check that these rules are clear. For implementations, also check rendering and key interactions. Do not report unexecuted checks as passed.
