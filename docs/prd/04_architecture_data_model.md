\newpage

# 11. Data Engineering Architecture

## 11.1 Reference architecture

![Data architecture (from the executive deck)](../deliverables/slides/slide-09.png)

```
 SOURCES            Public/official · Campaign-owned · Survey · Digital platforms · Media (licensed) · Field · Call-centre
   │
 ACCESS MODES       API connector (verified) · file drop · DB replication · validated upload · survey export · licensed feed
   │
 INGESTION          Orchestrated jobs (Dagster/Airflow) · idempotent loads · schema contracts · secrets from vault
   │
 RAW ZONE           Object storage, immutable, partitioned by source/date, checksum + ingestion metadata
   │
 DATA-QUALITY       Tests: freshness · volume · schema · nulls · ranges · duplicates · integrity → quarantine on fail
   │
 STANDARDISED MODEL dbt models: staging → conformed dimensions (geography, time, language, issue, channel) → facts
   │
 WAREHOUSE          PostgreSQL (POC / single AC) → BigQuery or Snowflake (multi-AC / state) · metric store
   │
 ML / NLP LAYER     Batch & streaming inference · model registry · feature tables · embeddings (pgvector / FAISS)
   │
 BI / DASHBOARD     Power BI (fast rollout) or React/Next.js (bespoke Command Center) · Streamlit for POC prototypes
   │
 AI INTELLIGENCE    LLM + tool router (metrics API, SQL templates, search, vector retrieval) · guardrails · citation builder
   │
 EXECUTIVE COMMAND CENTER   Health score · 14 modules · alerts · reports · AI Analyst · compliance tower
```

## 11.2 Technology choices — and why each exists

We deliberately avoid "every tool". Each component earns its place:

| Layer | Recommended | Why it exists | When to choose alternatives |
|---|---|---|---|
| Language | **Python + SQL** | Python for ingestion, statistics, ML/NLP; SQL for transformation and analytics — the common language of analysts and engineers | — |
| Operational DB + POC warehouse | **PostgreSQL** (managed, Indian region) | Reliable, cheap, strong SQL, row-level security, **pgvector** for embeddings — one engine for POC | Move analytics to BigQuery/Snowflake when data > ~1 TB or > 50 concurrent analysts |
| Scale warehouse | **BigQuery** (GCP) *or* **Snowflake** | Serverless scale, separation of storage/compute, strong governance | Choose per the Agency's cloud preference and existing contracts |
| Cloud | **AWS / Azure / GCP** — Indian regions | Data residency, managed security services | Follow client preference; avoid multi-cloud in POC |
| Orchestration | **Dagster** (asset-centric, built-in lineage) *or* **Airflow** (widely known) | Scheduling, retries, dependencies, observability | Airflow if the client's team already runs it |
| Transformation | **dbt** | Versioned SQL models, tests, documentation, lineage | — |
| Data quality | dbt tests + Great Expectations-style checks | Automated quality gates | — |
| Statistics | **Pandas, NumPy, SciPy, Statsmodels** | Weighting, CIs, significance tests, time-series | — |
| ML | **scikit-learn**, gradient boosting (LightGBM/**XGBoost** where it beats simpler models) | Tabular models with explainability | PyTorch only where deep models are justified |
| NLP | **Transformers**, multilingual encoders (e.g., MuRIL, IndicBERT, XLM-R-class), **IndicTrans2** for translation | Indian-language coverage incl. Hinglish/romanised text | Commercial APIs where accuracy is proven on our gold sets and data terms allow |
| Embeddings / retrieval | **SentenceTransformers** (multilingual models) + **pgvector** (POC) / **FAISS** (large, in-memory) | Semantic search, clustering, duplicates, RAG | Managed vector DB only at very large scale |
| API | **FastAPI** | Typed, fast, OpenAPI docs, easy auth integration | — |
| BI | **Power BI** (Agency-friendly, RLS, mobile) *or* **React/Next.js** | Leadership dashboards | React for a bespoke, branded Command Center; Power BI for speed |
| Prototype UI | **Streamlit** | 1–2 day iterations during POC | Not for production leadership use |
| LLM | Enterprise LLM endpoint with no-training-on-data terms and Indian/approved region where available | AI Analyst & summarisation | Self-hosted open model where data terms require |
| Observability | Cloud monitoring + OpenTelemetry; pipeline dashboards | Know when data or models break | — |
| Secrets | Cloud KMS + secrets manager / Vault | No credentials in code | — |

## 11.3 Metric store (semantic layer) — *added capability*

Every KPI (e.g., `engagement_rate`, `answer_rate`, `activity_completion_rate`) is defined **once** — formula, grain, filters, owner, version — and consumed identically by dashboards, reports and the AI Analyst. This single addition removes the most common source of leadership distrust: "why does your number differ from theirs?"

# 12. Conceptual Data Model

**Design rule:** the model stores **aggregate or appropriately authorised operational records**. There is **no table of individuals' political beliefs, preferences or vote intentions**. Survey microdata is anonymous/pseudonymised, holds coarse demographic bins only, and is used for weighted aggregate estimates.

![Conceptual ERD (from the executive deck)](../deliverables/slides/slide-10.png)

```
 campaign ─┬─< constituency >── geography (state/district/AC/block/zone; official codes)
           │        └─< historical_election (year, turnout, electors, party vote share — public)
           ├─< data_source >──< data_quality (test, status, score, run_at)
           ├─< survey >──< survey_question
           │        └──< survey_response (anonymous, weight, bins, QC flags) ──> issue
           ├─< digital_channel >──< content >──< content_performance (daily) 
           │                          └──< compliance_record (approval, MCMC ref, AI label, audit)
           ├─< campaign_spend (channel, category, amount, certification ref)
           ├─< media_mention (outlet type, language, topic, tone) ──> issue
           ├─< sentiment_record (aggregated social: date × platform × topic × language × zone*) ──> issue
           ├─< field_activity (zone, type, planned, completed, attendance est.) ──> event
           ├─< operational_metric (call-centre & ops aggregates)
           ├─< alert (rule, severity, status, owner, ack/closure)
           ├─< report (type, period, version, approver, distribution)
           └─< model_run (model, version, data window, metrics, approval)
   * zone only where public location metadata exists and is permitted
```

| Entity | Grain | Key fields | Sensitivity |
|---|---|---|---|
| campaign | One per engagement | name, phase, dates | Low |
| constituency | AC/PC | official code, name, state, reserved category (public) | Public |
| geography | Admin unit | code, parent, level, geometry ref, boundary source/version | Public |
| historical_election | AC × election | electors, votes polled, turnout %, party vote share (public) | Public |
| survey | Wave | design, mode, fieldwork dates, vendor, target n, weighting scheme | Internal |
| survey_question | Question | wording (all languages), scale, version | Internal |
| survey_response | Anonymous respondent × wave | age band, gender, area type, zone, answers, weight, QC flags, consent flag | Confidential (pseudonymised) |
| digital_channel | Account/page/channel | platform, owner, authorised token ref | Internal |
| content | Creative/post | format, theme, language, length, publish time, AI flag | Internal |
| content_performance | Content × day | impressions, reach, engagement, views, watch time, clicks, spend | Internal |
| media_mention | Article/segment | outlet, type, language, topic, tone, reach tier, URL, licence ref | Internal |
| issue | Taxonomy node | name, parent, keywords/examples, languages | Internal |
| sentiment_record | Date × platform × topic × language (× zone) | counts by label, mean score, coverage | Internal (aggregate) |
| field_activity | Activity | zone, type, planned/completed, attendance estimate, report timeliness | Internal |
| event | Event | type, zone/site, date, estimated attendance | Internal |
| operational_metric | Metric × day × unit | call volume, answer rate, FCR, backlog | Internal |
| campaign_spend | Line item | channel, vendor, category, amount, certification ref | Confidential |
| compliance_record | Content × control | approval, certification, AI label, takedown, audit | Confidential |
| data_source | Source | registry fields (§9) | Internal |
| data_quality | Test run | test, status, rows affected, score | Internal |
| alert | Alert | rule, severity, entity, status, owner, timestamps | Internal |
| report | Report | type, period, version, approver | Internal |
| model_run | Run | model, version, window, metrics, approval | Internal |

A conceptual DDL is provided in `poc/schema.sql`.

# 13. Analytics Layer & Intelligence Modules

## 13.1 Analytics catalogue

| Level | Question | Examples | Methods | Output guardrail |
|---|---|---|---|---|
| **Descriptive** | What happened? | Daily/weekly/monthly trends; KPI summaries; channel performance; historical comparison vs previous elections (turnout, electors) | Aggregations, rolling baselines, indexed comparisons | Show "data as of", source, quality |
| **Diagnostic** | Why did a KPI change? Which factor/content/channel/geography changed? | Engagement down 18% W/W → driven by X platform, static images, 2 themes; completion drop concentrated in Hill Block | Contribution/variance decomposition, drill-down, mix-vs-rate analysis, change-point detection | Label as "contributing factors", not causes, unless tested |
| **Predictive** (where statistically justified) | What is likely next? | Issue-volume and media-volume forecasts; digital performance forecasts; turnout-*trend* estimates at AC level from historical/public data; campaign operations forecasts (completion, backlog) | Time-series models, regression, gradient boosting | Every forecast shows interval, assumptions, training window, validation metric, limitations; **never certainty; never individual-level** |
| **Decision support** | What should we look at / prioritise operationally? | Operational priorities (zones behind plan), data-quality priorities, monitoring priorities (rising issues), resource-measurement insights, content-performance learnings, recommended analytical follow-ups | Rules + ranking + analyst judgement | **No individualised persuasion instructions**; recommendations are operational/analytical, owned by humans |

## 13.2 Social Listening module

**Pipeline:** Social Listening → NLP → Topic → Sentiment → Trend → Alert.

![Social listening — anomaly detection on DEMO DATA](../demo/charts/social_volume_anomaly.png)

| Dashboard component | Definition | Warning shown |
|---|---|---|
| Mention volume | De-duplicated public mentions matching the campaign's tracked keywords/entities | Coverage index; platform mix |
| Sentiment | Distribution of positive/neutral/negative with model confidence; net sentiment with bootstrap CI | "Public social data only — not representative of the electorate" |
| Topic trends | Share of mentions by issue taxonomy over time | Classifier accuracy per language |
| Issue velocity | Growth rate of an issue vs its 7-day baseline (z-score / robust MAD) | Minimum-volume threshold |
| Engagement | Interactions on public posts in scope | Platform-reported; not comparable across platforms without indexing |
| Content performance | Top public posts by engagement (aggregate) | No profiling of individual posters |
| Creator/media amplification | Accounts/outlets driving *reach* on a topic — public figures, media houses, verified organisations | **Aggregated by account type**; no private individuals profiled |
| Platform comparison | Volume/sentiment split by platform | Access differs per platform |
| Geographic aggregation | Zone/district only where public location metadata exists and use is permitted | Typically < 20% of posts carry usable location — shown explicitly |
| Time-series movement | Hourly/daily lines with anomaly bands | — |
| Emerging-issue detection | New clusters of semantically similar posts growing faster than baseline | Human analyst validates before escalation |

**Coverage & Representativeness Index (added capability)** — each tile shows: platforms covered, % of posts with language confidence ≥ threshold, % geo-attributable, estimated duplicate share, and a standard caveat. In the DEMO data: 18.1% geo-attributable, 7.0% near-duplicates removed.

![Net sentiment by topic with 95% intervals — DEMO DATA](../demo/charts/sentiment_by_topic_ci.png)

## 13.3 Media Intelligence module

| Component | Description |
|---|---|
| Media monitoring | Ingest licensed/public news feeds, regional outlets, broadcast transcripts (licensed) |
| Article classification | Issue taxonomy; article type (news, opinion, interview, explainer) |
| Topic extraction | Keyphrases, clusters, story threads across outlets |
| Sentiment / tone | Tone towards tracked entities/issues, with confidence |
| Candidate/organisation mention | NER + entity linking to a curated list of public figures and organisations |
| Issue tracking | Share of voice by issue, outlet type, language, region |
| Media-volume trend | Daily/weekly volume with anomaly detection |
| Regional media monitoring | Indian-language outlets prioritised; translation for leadership summaries |
| Broadcast transcript analysis | **Only where licensed**; transcript segments classified like articles |
| Alerting | Spike in volume/negative tone for an issue; high-reach outlet coverage |

**Media Intelligence Dashboard** layout: KPI strip (articles 24h / 7d, % negative, share of regional coverage, top issue) → weekly volume by outlet type → issue × tone matrix → story-thread list with outlet count and first-seen time → "coverage map" by district (where outlet geography is known) → daily AI summary with citations.

![Weekly media volume by outlet type — DEMO DATA](../demo/charts/media_weekly_outlets.png)

## 13.4 Survey Intelligence module

| Capability | Specification |
|---|---|
| Questionnaire design support | Neutral-wording checklist, scale balance, order rotation, translation/back-translation, cognitive pre-test log, sensitive-question review (no vote-intention questions unless the Campaign's research lead and legal approve and outputs remain aggregate and internal) |
| Sampling | Design registry (stratified/cluster/quota), sampling frame description, allocation by stratum |
| Sample-size calculation | n = z²·p(1−p)/e² × deff, with finite-population correction where relevant; calculator in the UI |
| Weighting | Post-stratification / raking to Census/official margins; trimming (e.g., 0.3–3.0); weight diagnostics |
| Confidence intervals & MoE | Using effective sample size; shown by default |
| Cross-tabulation | Weighted cross-tabs with column %, n and MoE; suppression of cells with n < 50 |
| Statistical significance | Two-proportion z-tests with design effect; wave-over-wave change flags; multiple-comparison control (Benjamini–Hochberg) for large cross-tab batteries |
| Response quality | Speeders, straight-liners, duplicates, interviewer effects, GPS/time anomalies (tablet F2F), back-check results |
| Missing data | Item non-response rates; explicit "Don't know/Refused"; imputation only when documented |
| Bias checks | Sample vs population profile; mode effects; non-response analysis |
| Trend comparison | Same-question, same-population comparisons only; methodology changes flagged |

**DEMO example:** Wave 3 (n = 3,851; effective n = 3,704 after weighting) shows 21.0% ± 1.3 naming *water supply* as the top local issue vs 13.0% in Wave 1 — a change of +8.0 points, statistically significant (z ≈ 9). Awareness of the campaign's public programme rose from 30.2% to 44.1%. **Surveys describe the sampled population at fieldwork time; they do not guarantee or predict election results.**

![Survey issue salience with 95% CIs — DEMO DATA](../demo/charts/survey_issue_salience.png)

## 13.5 Field Operations Analytics module

| KPI | Definition |
|---|---|
| Activity completion rate | Completed / planned activities |
| Event count | Events held by type |
| Attendance (where lawfully recorded) | Headcount *estimates* per event; no identity capture |
| Geographic coverage | % of zones with ≥ 1 completed activity in last 7 days |
| Issue-report volume | Local issue reports logged by category |
| Volunteer activity | Active volunteers, tasks per volunteer (aggregate) |
| Task completion | On-time task completion % |
| Response time | Time from issue report to acknowledgement |
| Data submission quality | Timeliness + completeness + validation pass rate |
| Operational bottlenecks | Zones/blocks with persistent under-completion or late reports |

**Field Operations Dashboard:** completion by zone (map), completion trend, on-time reporting by block, bottleneck list with owner, issue-report categories.

![Field completion by zone — DEMO DATA, fictional geography](../demo/charts/zone_map_field_completion.png)

## 13.6 Call-centre Analytics module (if authorised data is available)

Metrics: call volume, answer rate, response/wait time, issue categories, resolution rate (first-contact and overall), follow-up status, language mix, geographic aggregation (zone/district), agent performance (operational metrics for the helpline's own management, not surveillance beyond lawful workplace norms), quality-monitoring scores. **Not used:** private communications, unauthorised personal data, or any inference about callers' political views. Recordings/transcripts only where callers are informed and the Campaign's legal team has approved.

![Call-centre service levels — DEMO DATA](../demo/charts/call_centre_weekly.png)
