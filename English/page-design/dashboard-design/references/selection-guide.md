# Choose a Dashboard from the Task

This guide distills and extends the references. A–G categories were created for this skill; they are not original source categories. See the [method summary](reference-index.md) for source IDs and [visual-recipes.md](visual-recipes.md) for visual choices. These rules work without original images.

## Identify the primary task

The questions below are decision candidates, not a first-match sequence. Use role, visit purpose, response deadlines, and main actions to identify what dominates.

1. **Is continuous monitoring, prompt acknowledgment, and incident response the main job?** Choose C. Trends and aggregates support response. An exception summary on an ordinary business overview does not automatically make it a monitoring page.
2. **Is the main job completing tasks or assigning people?** Choose D. Do not bury tasks below several rows of KPIs.
3. **Is the main job explaining causes, comparing groups, or exploring dimensions?** Choose B.
4. **Is the main job finding and opening content objects?** Choose F. Content cards or lists fit better than a KPI wall.
5. **Is the main job reviewing an account, resource pool, or personal status?** Choose E.
6. **Is the main job explaining a finding or result to readers?** Choose G.
7. **Is the main job quickly judging overall business performance?** Choose A.

Several may apply. Let this role's highest-priority task determine the primary structure; put secondary tasks in secondary areas or drill-downs. If the user only needs bulk record maintenance, recommend a data-list-centered interface instead of adding charts to justify the Dashboard label.

Common ambiguities: an owner checking refund exceptions daily while operations handles them usually still needs A; an operator who must take ownership of incidents needs C; a frontline worker meeting deadlines needs D; an analyst investigating metric changes needs B; someone explaining established findings and evidence needs G. The same data can support different views.

Then check data conditions: without group data, retain the overview and omit group analysis; without path edges, replace a Sankey with a valid conversion view of known steps. Mark core metrics that are not connected yet; do not redefine the page's main task as displaying only easily available data.

## Seven structural recipes

### A Business overview

- **Fits:** managers, commerce owners, SaaS operators, sales leads, store managers.
- **Answers:** How are we performing? How far from target? What contributes or detracts most?
- **Structure:** title + organization/time scope → a few core results → one main trend/target chart + structural explanation → significant exceptions or business summaries.
- **Candidates:** P02, P04; P01 for a conclusion-led narrative; P03 for an approachable product. Sources S16, S26, S29, V04.
- **Data conditions:** actual core values, units, and time range. Add targets, comparable history, and business grouping when available; absence of one does not invalidate a business overview.
- **Actions:** open details from exceptions/groups with the same filtering context.
- **Avoid:** equal area for every department; a row of a dozen KPIs; totals concealing worsening conversion or profit.

### B Diagnostic analysis

- **Fits:** growth, product behavior, channel performance, retention, sales composition, specialist analysis.
- **Answers:** Where does the change originate? Which group differs? At which path step does it occur?
- **Structure:** dimension/audience/period → main analysis view → period/group/path comparisons → corresponding records or explanation.
- **Candidates:** P01, P02, P04; P05 for dark projects. Sources S26–S30, V08.
- **Data conditions:** dimensions, granularity, and time windows required by the chosen analysis. Ratios require denominators and sample sizes; paths require connections. Totals alone cannot establish causes or segments.
- **Actions:** filter, select ranges, switch dimensions, inspect details, clear selections; make linked-view scope visible.
- **Avoid:** Sankeys for simple rankings; directly comparing conversion rates with different denominators; inventing causal conclusions without data.

### C Live monitoring and response

- **Fits:** service/device/inventory/production/multi-site monitoring and support operations.
- **Answers:** What is wrong? What is the impact? Is the data fresh? Who handles it next?
- **Structure:** refresh/connection status → severe exceptions/affected objects → trends and thresholds → prioritized event queue.
- **Candidates:** inherit the existing light/dark theme; P04 or P05; P07 for a few distinct business areas. Sources S05/V01 for operational partitioning, S30, V08. Alert mechanics are additions by this skill.
- **Data conditions:** timestamps, update status, and observed objects. Response queues also need event status, impact, and owner/assignment information. Severity and thresholds come from actual rules; indicate when unconfigured instead of inventing levels.
- **Actions:** inspect objects, acknowledge/assign events, temporarily pause scrolling; permissions are project-specific.
- **Avoid:** moving data that changes order and focus; automatic counts from zero; hiding alerts on card backs; brand orange meaning both ordinary selection and highest severity.

### D Task and team workspace

- **Fits:** project collaboration, design teams, CRM follow-up, recruiting, personal schedules, operations crews.
- **Answers:** What should I do now? What may be late? Are resources sufficient?
- **Structure:** tasks/risks and next steps → primary timeline, calendar, or task queue → progress/workload → recent collaboration.
- **Candidates:** P03, P04, P10; P09 with an explicit presentation goal. Sources S14, S19, S09, S12, S36, V05.
- **Data conditions:** task identifiers, status, and next steps; owners for collaboration, deadlines for scheduling, and dependencies/capacity when actual functionality uses them.
- **Actions:** open tasks, adjust plans, create quickly; provide non-drag alternatives to dragging.
- **Avoid:** completion rates and leaderboards displacing tasks; adding leaderboards to every team; changing only menu highlights while content stays unchanged.

### E Account and resource overview

- **Fits:** account balances, cash flow, cloud storage/quotas, personal health records, device resources.
- **Answers:** What do I have or what is my status? How is it changing? What happened recently?
- **Structure:** main balance/capacity/status + common actions → inflow/outflow or usage changes → composition or goals → recent transactions/events.
- **Candidates:** P02, P03, P06; P11 for a low-density brand homepage; P09 for resource presentation. Sources S15, S17–S18, S32, V03, V07.
- **Required data:** currency/capacity/metric units, time, total-to-part relationships, and authorization scope.
- **Actions:** inspect details, enter resource management or existing business operations; do not turn financial or medical examples into professional advice.
- **Avoid:** adding currencies without conversion; conflating balance and income; displaying missing health data as normal; copying sample health judgments.

### F Content and resource discovery

- **Fits:** asset libraries, portfolios, courses, trips, media, asset previews.
- **Answers:** What objects exist? Which fits my needs? How do I open or resume it quickly?
- **Structure:** search/categories → recommended/recent objects → image/content card feed → selected-object summary or context.
- **Candidates:** P08 with a restrained shell; use a list-first approach for heavy information management. Sources S37, V02.
- **Data conditions:** object identifiers, names, and task-relevant attributes. Add images, status, and recommendations only from real fields; use a consistent missing-image fallback. “Recently viewed” requires access records; modification time is not opening time. Object types such as assets or projects come from fields or defined collections, not guesses from covers. When fields are missing, use a supported label such as “Recently modified.”
- **Actions:** filter, open, continue browsing, bookmark only when required.
- **Avoid:** decorative photos without business meaning; completely truncated long titles; poor images becoming the page's dominant visual.

### G Thematic narrative and results report

- **Fits:** monthly business reports, research overviews, energy/sustainability results, reader-oriented topic pages.
- **Answers:** What finding matters most? Where is its evidence? What is the scope and progress?
- **Structure:** truthful conclusion or neutral topic title → key evidence → main chart → causal breakdown/goal progress → sources and detail links.
- **Candidates:** P01, P06; P02 for precise reading. Sources S26, S31, V06.
- **Data conditions:** evidence, period, and provenance for the conclusion; check baseline and target definitions when comparisons or goals are involved.
- **Actions:** inspect definitions, compare periods, expand evidence, export when required.
- **Avoid:** inventing findings for a large headline; implying data conclusions through natural colors; using a gauge to compensate for a missing target.

## Quick mapping of common needs

| Actual task | Primary structure | Recommended representation | Preferred visual/source |
| --- | --- | --- | --- |
| Owner reviews monthly sales and profit | A | Core results and trends; add period comparison, targets, and contribution ranking when corresponding data exists | P02/P04; S16/S29 |
| Commerce operator investigates falling conversion | B | Comparable trends, funnel, channel/device comparison, exception details | P01/P04; S26/S28 |
| Warehouse worker handles shortages and overdue items | C | Shortage/timeout queues, affected orders, location/inventory trends | P04; borrow spatial organization only from S04/S35 |
| Engineer investigates service error spikes | C→B | Alerts, error rate/latency, service groups, events | P05 or existing light theme; S30/V08 |
| Project manager allocates next week's work | D | Deadline risks, timeline, workload, tasks | P03/P04; S14/S19 |
| Individual reviews account income and spending | E | Balance, inflows/outflows, budget, transactions | P02/P06; S17/S18 |
| Individual reviews learning, focus, or practice | E+D; D when execution dominates | Goals and time invested → frequency/time allocation → current practice/habits → recent records and next steps; ability scores need definitions | P03/P10; S02/S06 |
| HR reviews attendance, leave, and recruiting | D+A | Tasks/staff distribution, gaps, recruitment stages | P03; S19–S25 |
| Healthcare user reviews appointments and records | E+D | Recent records, appointments, test progress | P03; S15; do not infer diagnoses |
| Editor browses assets and programs | F | Covers, categories, recent access | P08; S37/V02 |
| Manage cloud quotas and transfers | E+C | Capacity, expiring resources, transfer events | P04, P09 for presentation; V03 |
| Environmental team presents emission reductions | G; C when live response is required | Baseline/actual/target, time trends, sources | P06; S31 |
| Multi-site network compares regions | B/C | Site ranking; maps only for spatial questions | P01/P04; V06/V01 |
| Shared system for sales and support | Role-specific A/D/C | Shared metric definitions, separate first-screen priorities | Do not squeeze all roles into one homepage |

## Resolve competing requirements

- **Glass brand + dense reports:** keep material in the background or navigation; give tables/charts near-opaque surfaces, fixed alignment, and clear labels.
- **Professional dark theme + low contrast:** strengthen distinctions among surfaces, borders, and text; reduce glow. Theme does not replace readability.
- **Many metrics + small screen:** reorder task priorities, group content, or offer drill-downs; do not shrink the entire desktop page into a phone.
- **Visual impact + operational efficiency:** concentrate expression in the main chart or a key area; keep frequent controls stable.
- **Uncertain choice:** deliver one reasoned recommendation, with an alternative only for a meaningful tradeoff. Do not ask users to blindly choose among eleven styles first.

## Choose the display medium separately

Display medium and A–G task structure are separate decisions. A large display does not automatically require dark monitoring; mobile is not a proportional desktop reduction.

| Usage | Adjustments to the same task structure |
| --- | --- |
| Desktop workspace | Support comparison, filtering, details, and actions; set density from expertise and content volume |
| Mobile work | Put the current role's task, exceptions, and main actions first; move complex analysis into details; keep selected scope visible |
| Distant wall display/meeting presentation | Reduce parallel content; show key labels, units, and refresh time directly; essential status cannot depend on mouse or touch; choose type size for viewing distance |
| Static report/export | State time, filter scope, and data cutoff; turn hover information into direct labels or captions; remove inoperative controls |

Use wall-display rotation only when needed; critical exceptions must not disappear during rotation. If remote response is needed, provide a clear link to the operational interface. Do not present a read-only display as an actionable console.
