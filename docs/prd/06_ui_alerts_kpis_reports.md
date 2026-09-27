\newpage

# 18. Command Center UI

## 18.1 Design principles

- **Answer first, detail on demand.** Every screen opens with 3–5 KPI cards and a one-line "what changed" statement, then charts, then tables.
- **Trust signals on every tile:** source, "data as of", data-quality badge (green/amber/red), and coverage note where relevant.
- **Uncertainty is visible:** intervals on estimates; significance markers on changes; forecasts shaded.
- **Consistent grammar:** same period selector, geography filter and language filter across modules, in one row above the charts.
- **Accessible:** WCAG 2.1 AA, colour-blind-safe validated palette, status never shown by colour alone.

![Executive Command Center mock-up — DEMO DATA](../deliverables/slides/slide-21.png)

## 18.2 Home — Campaign Intelligence Health Score

A composite 0–100 index summarising eight Level-2 domains (Digital, Social, Media, Survey, Field, Operations, Data Quality, Compliance). It is an **operational health indicator**, not an electoral prediction.

- Each domain score = weighted average of normalised KPIs vs target/baseline (weights agreed with leadership in Week 1, versioned).
- The Health Score is displayed with its domain breakdown; a red domain cannot be hidden by green ones (any domain < 50 caps the headline at "Amber").
- Data Quality and Compliance scores gate trust: if Data Quality is red, the score is shown with a "low-confidence" banner.

## 18.3 Screen-by-screen wireframe descriptions

| # | Screen | Layout (top → bottom) | Primary users |
|---|---|---|---|
| 1 | **Executive Overview** | Header: Health Score dial + 8 domain chips · "Top 5 changes in last 24h" list with severity icons · KPI strip (mentions, net sentiment, media volume, digital ER, field completion, answer rate, open alerts, compliance exceptions) · 14-day trend small multiples · AI daily brief with citations | Leadership |
| 2 | **Digital Intelligence** | KPI strip (reach, impressions, ER, video views, avg watch %, CTR, CPC, CPM, spend) · platform comparison bars · Digital Performance Scorecard table vs targets · spend pacing vs plan · top/bottom content | Head of Digital |
| 3 | **Social Listening** | Coverage index banner · mention volume with anomaly band · sentiment distribution with CIs · topic share stream · platform split · emerging-cluster cards (keyphrases, growth, sample public posts) | Social analyst |
| 4 | **Issue Intelligence** | Issue taxonomy tree · cross-source issue matrix (social share, media share, survey salience, field reports, call-centre categories) · issue velocity leaderboard · issue detail drawer with timeline across sources | Research, leadership |
| 5 | **Media Intelligence** | KPI strip · weekly volume by outlet type · issue × tone heatmap · story threads with first-seen time and outlet count · regional coverage by district · licensed broadcast segments | Media cell |
| 6 | **Survey Intelligence** | Wave selector · topline with MoE · wave-over-wave change with significance markers · weighted cross-tabs (with suppression) · sample health (n, n_eff, deff, QC exclusions, profile vs population) · methodology panel | Research lead |
| 7 | **Field Operations** | KPI strip (planned, completed %, on-time %, attendance est., issue reports) · zone map · completion trend by block · bottleneck table with owners · data-submission quality | Field head |
| 8 | **Geographic Intelligence** | Layer switcher (historical results, turnout trend, survey coverage, activity coverage, events, issue distribution, media distribution, operational coverage) · AC/block/zone choropleth · side panel with selected-area profile (public + operational aggregates) | Leadership, field |
| 9 | **Forecasting** | Model selector · forecast chart with 80/95% intervals · model card summary (training window, validation metric, assumptions, limitations) · back-test accuracy history | Analysts |
| 10 | **Alerts** | Severity-sorted queue · alert detail (rule, evidence chart, affected entity, owner, SLA timer) · acknowledge / escalate / close with note · alert precision stats | War-room |
| 11 | **Compliance** | Exceptions banner · content pipeline Kanban (Draft → Review → Certified → Scheduled → Live) · certification status table · AI-label/provenance ledger · spend vs configured limits · silence-period calendar · audit trail search | Compliance officer |
| 12 | **Data Quality** | Source registry health grid (freshness, volume, tests passed) · failing tests · lineage explorer · quality score trend | Data team |
| 13 | **AI Analyst** | Chat with suggested questions · answers with Facts / Interpretation / Follow-ups, citations and "data as of" · "show the data" expanders · feedback buttons | All (role-scoped) |
| 14 | **Reports** | Daily/weekly report library · draft → review → approve workflow · export (PDF/PPTX) · distribution log | Leadership, account lead |

# 19. Real-Time Alert Engine

## 19.1 Severity levels

| Level | Definition | Response target | Channel |
|---|---|---|---|
| **Critical** | Compliance breach risk, pipeline outage on priority source, security incident, or extreme anomaly on a leadership KPI | Acknowledge ≤ 15 min; action ≤ 1 h (compliance takedown clock: < 3 h) | Phone/SMS + app + war-room screen |
| **High** | Significant anomaly (e.g., > 4 robust SD) on priority metrics; fast-growing issue; high-reach media story | Acknowledge ≤ 1 h | App + messaging integration |
| **Medium** | Notable movement (3–4 robust SD) or sustained trend change; data-quality degradation | Same day | App + daily report |
| **Low** | Informational; minor deviations; stale approvals | Weekly review | Digest |

## 19.2 Alert catalogue

| Alert | Rule (default; tunable) | Default level |
|---|---|---|
| Sudden social-volume spike | Daily/hourly mentions > rolling median + 3·(1.4826·MAD) and volume > minimum | High (Critical if > 6 SD and top-3 issue) |
| Abnormal sentiment movement | Net sentiment change beyond 99% bootstrap interval of 14-day baseline, n ≥ 300 | Medium/High |
| Viral content | Public item in scope with engagement velocity in top 0.1% of 30-day distribution | High |
| Unusual digital-performance movement | ER/CTR/CPM outside forecast 95% interval for 2 consecutive periods | Medium |
| Media spike | Media items on an issue > baseline + 3 SD or ≥ 2 high-reach outlets within 6 h | High |
| Data pipeline failure | Job failed / freshness SLA missed for priority source | Critical (priority) / Medium (other) |
| Survey anomaly | Interviewer/area outliers; QC exclusion rate > 10%; profile deviation > 5 pts | Medium |
| Data-quality deterioration | Source quality score drops > 10 pts or below 70 | Medium/High |
| Compliance deadline | Expenditure filing, certification expiry, silence-period start in < 24 h | High/Critical |
| Abnormal spend | Daily spend > 150% of pacing plan, or cumulative > 80%/95% of configured limit | High/Critical |
| Unexpected KPI movement | Any metric-store KPI outside its forecast interval | Low/Medium |
| AI label missing | AI-flagged content without label record | Critical |

**Alert hygiene:** de-duplication and grouping (one incident, many signals), suppression windows, owner assignment, closure notes, weekly precision review (target ≥ 60% of High/Critical alerts rated "useful" by the war-room).

# 20. KPI Framework

## 20.1 KPI tree

```
LEVEL 1  Campaign Intelligence Health (0–100, operational)
   │
LEVEL 2  Digital · Social · Media · Survey · Field · Operations · Data Quality · Compliance
   │
LEVEL 3  (detailed, measurable KPIs below)
```

| Level 2 | Level 3 KPIs | Type |
|---|---|---|
| **Digital** | Reach; impressions; engagement rate; video views; avg watch %; CTR; CPC; CPM; landing-page conversion (sign-ups/volunteer forms — lawful, consented); spend vs pacing | Leading (ER, CTR) / Lagging (reach totals) |
| **Social** | De-duplicated mention volume; net sentiment (with CI); issue share; issue velocity; share of voice among tracked entities; emerging-cluster count | Leading / Diagnostic |
| **Media** | Media volume; tone distribution; issue share; regional share; high-reach outlet coverage; story-thread count | Leading / Diagnostic |
| **Survey** | Issue salience (weighted, MoE); programme awareness; service satisfaction; wave-over-wave significant changes; sample health (n_eff, deff) | Lagging (periodic) / Data-quality |
| **Field** | Activity completion %; zone coverage %; on-time reporting %; issue reports logged; response time | Leading (operational) |
| **Operations** | Call answer rate; FCR; median wait; backlog; alert acknowledgement time; report on-time delivery | Leading (operational) |
| **Data Quality** | Sources green %; freshness SLA %; test pass rate; duplicate rate; coverage index; lineage completeness | Data-quality |
| **Compliance** | Paid items with certification ref %; AI items labelled %; approvals within SLA %; silence-period violations (target 0); takedown within 3 h %; spend within configured limits | Leading (risk) |

## 20.2 Indicator types

| Type | Purpose | Examples |
|---|---|---|
| Leading | Move before outcomes; used for early action | Issue velocity, ER, field completion, alert acknowledgement |
| Lagging | Confirm outcomes over time | Survey awareness, cumulative reach, weekly satisfaction |
| Diagnostic | Explain movement | Platform/format/theme mix, zone breakdown |
| Data-quality | Tell you whether to trust the rest | Freshness, coverage, test pass rate, n_eff |

# 21. Digital Campaign & Content Intelligence

## 21.1 Digital Performance Scorecard (DEMO DATA, trailing 7 days to 11 Sep 2026 vs prior 7 days)

| Metric | This week | Prior week | Δ | Status |
|---|---|---|---|---|
| Posts published | 248 | 233 | +6.4% | — |
| Impressions | 9.21 M | 9.13 M | +0.9% | On plan |
| Engagement rate | 3.49% | 3.31% | +0.18 pts | ▲ Above target (3.2%) |
| Video views | 1.50 M | 1.56 M | −3.8% | Watch |
| CTR | 1.11% | 1.14% | −0.03 pts | On plan |
| Paid spend | ₹3.04 lakh | ₹3.45 lakh | −12.1% | Within pacing |
| CPM (boosted) | ₹116 | ₹111 | +4.5% | Watch |
| Boosted items with MCMC certification ref | 100% | 100% | — | ✓ Compliant |

Definitions are platform-reported; cross-platform totals are indicative because platforms define reach/views differently. **Conversion metrics** are used only where legitimately measurable (e.g., volunteer sign-ups on owned forms with consent).

## 21.2 Content Performance Matrix

Content is analysed by format, topic/theme, length, language, publishing time, engagement, retention (avg watch %), reach, watch time, shares and comments. The matrix shows median engagement rate per format × theme cell with cell counts; cells with n < 25 are marked directional.

![Content Performance Matrix — DEMO DATA](../demo/charts/content_matrix_heatmap.png)

Use: **format and theme planning at aggregate level** (e.g., "short explainer videos on youth employment outperform static images by ~1.8×"). The matrix is **not** used to tailor messages to individuals or sensitive audience segments.

## 21.3 Experiment & test registry (added capability)

Content learning is only reliable when tests are designed up-front.

| Field | Description |
|---|---|
| Hypothesis | e.g., "Hindi captions increase average watch % for 30–60 s explainers" |
| Design | Platform-native A/B (where offered) or matched time-slot rotation |
| Primary metric & MDE | e.g., avg watch %, minimum detectable effect 3 pts |
| Sample/budget | Pre-computed from power analysis |
| Stopping rule | Fixed horizon (no peeking) or sequential test with alpha spending |
| Result | Effect, CI, p-value; decision; learning logged |
| Guardrails | Only content-level variations (format, length, language, time); no targeting on sensitive attributes; all variants compliant (certified/labelled) |

# 22. GIS / Geospatial Intelligence

| Layer | Grain | Source |
|---|---|---|
| Constituency map | AC/PC | Official boundaries where available; community datasets with attribution for analysis; verify delimitation vintage |
| District/block/admin map | District/block | Official/State GIS portals where available |
| Historical result visualisation | AC × election | ECI statistical reports (public) |
| Turnout trends | AC × election | ECI statistical reports |
| Survey coverage | Zone | Survey metadata (counts of interviews; no respondent points) |
| Campaign activity coverage | Zone | Field activity aggregates |
| Event locations | Site (public events only) | Event records |
| Issue distribution | Zone/district | Field issue reports, call-centre categories, geo-attributable public mentions |
| Media distribution | District | Outlet geography |
| Operational coverage | Zone | Field + call-centre aggregates |

**Guardrails:** no individual voter targeting; no household-level plotting; small-area suppression (e.g., hide cells with < 10 records); **maps depicting India's national or state boundaries must use official boundaries (Survey of India) — incorrect external boundaries are a legal risk** [VERIFY exact requirements with legal].

# 23. Reporting

## 23.1 Sample Daily War-Room Report (DEMO DATA)

> **DAILY WAR-ROOM REPORT — Aranyapur AC (FICTIONAL) — Friday 12 September 2026, 07:00 IST**
> *Coverage: 11 Sep 2026 (00:00–23:59). DEMO DATA — SYNTHETIC. Prepared by: AI draft + analyst review (R. Analyst). Approved by: Analytics Lead.*
>
> **1. Executive Summary**
>
> - Overall Campaign Intelligence Health: **74 / 100 (Amber)** — Field domain below target in Hill Block; all other domains green/amber.
> - Social conversation volume is back within its expected range after the 31 Aug water-supply spike; **Jobs & skills** is the fastest-rising issue (+1.8 pts share vs 7-day baseline).
> - Helpline answer rate (84.4%, 7-day) remains **below the 90% SLA** for the second week.
>
> **2. Major Changes (vs trailing 7-day baseline)**
>
> | Signal | Yesterday | Baseline | Assessment |
> |---|---|---|---|
> | Public mentions (de-dup.) | 1,344 | 1,411/day | Within range |
> | Negative share (social) | 41.2% | 40.8% | No significant change |
> | Media items | 122 | 151/day | −19%, within range |
> | Field completion (7-day) | 83.2% | target 85% | Below target (Hill Block 67.4%) |
>
> **3. Digital Performance** — ER 3.49% (+0.18 pts W/W), impressions 9.21 M (+0.9%), video views −3.8% W/W; CPM ₹116 (+4.5%). All boosted items carry certification references.
>
> **4. Social Intelligence** — Top issues by share: Jobs & skills 16.3%, Water supply 14.2%, Prices 12.9%, Roads & transport 12.7%. *Coverage: public posts only; 18% geo-attributable; not representative of the electorate.*
>
> **5. Emerging Issues** — Cluster "skill-centre admissions" (Hinglish, 3 days, growing 2.1× baseline, n = 240) — **Medium**; analyst validated; no misinformation-risk flags.
>
> **6. Media Intelligence** — 122 items; 23.8% negative tone; top topics Roads & transport (18), Prices (17), Jobs & skills (16); regional/hyperlocal share 52.5%.
>
> **7. Survey Movement** — No new wave. Latest (Wave 3, fieldwork 4 Sep, n_eff 3,704): water supply salience 21.0% ± 1.3 (significant rise from 13.0% in Wave 1).
>
> **8. Field Operations** — 1,520 planned activities in last 7 days; 83.2% completed; 79.3% reports on time; bottleneck: Hill Block (Z19–Z24) completion 67.4%. 1,842 local issue reports logged.
>
> **9. Alerts** — 0 Critical · 1 High (helpline SLA breach, open, owner: Call-centre Manager) · 2 Medium (Hill Block completion; X-platform connector latency) · 4 Low.
>
> **10. Data Quality** — 11/14 sources green; 2 amber (X connector latency; field form late submissions); 1 red (regional TV transcripts feed delayed 26 h — vendor notified).
>
> **11. Compliance** — 0 exceptions. 12 paid items live, all certified; 3 AI-assisted items, all labelled with responsible-entity disclosure; no silence period in the next 7 days for this AC.
>
> **12. Recommended Analytical Follow-ups** (operational / analytical only)
> 1. Field Ops to review Hill Block staffing and connectivity; Data team to check whether late reports under-count completion.
> 2. Call-centre Manager to review peak-hour staffing; analytics to break down wait time by hour and language.
> 3. Research to consider adding a skills/training question to Wave 4 to test whether the social trend reflects broader salience.
> 4. Data team to escalate the TV-transcript feed delay with the vendor under the SLA.
>
> *Sources: metric store v1.4; social.mentions_daily; media.mentions_daily; digital.content_daily; field.activity; ops.call_centre; survey.w3. All figures DEMO DATA.*

## 23.2 Weekly Executive Report (10–15 pages)

| Page | Section | Content |
|---|---|---|
| 1 | Executive Summary | 5 key findings, Health Score trend, top risks, decisions requested |
| 2 | KPI Scorecard | Level-2 domain scores and Level-3 KPIs vs targets, W/W and 4-week trend |
| 3 | Trends | Cross-source timeline of the week's major developments |
| 4 | Digital | Scorecard, platform comparison, top/bottom content, spend pacing |
| 5 | Social | Volume, sentiment with CIs, issue shares, emerging clusters, coverage notes |
| 6 | Media | Volume/tone, story threads, regional coverage |
| 7 | Survey | Latest wave, significant changes, sample health, methodology notes |
| 8 | Field | Completion, coverage, bottlenecks, data-submission quality |
| 9 | Geography | Zone/AC maps: activity coverage, issue distribution, survey coverage |
| 10 | Forecast | Next-2-week forecasts with intervals; back-test accuracy |
| 11 | Risks | Operational, data, compliance and reputational risk items with owners |
| 12 | Data Quality | Source health, incidents, fixes |
| 13 | Compliance | Certification, AI labels, spend vs limits, upcoming deadlines |
| 14 | Next-week analytical priorities | Questions to answer, tests to run, data to acquire |
| 15 | Appendix | Definitions, methodology, sources |
