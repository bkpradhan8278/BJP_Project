\newpage

# 24. Team Structure & Operating Model

## 24.1 Three staffing scenarios

| Role | A. POC / MVP (5–7) | B. Single constituency / by-election (8–15 core + ops support) | C. Multi-constituency / state (20–50+) |
|---|---|---|---|
| Programme Director | 0.25 (shared) | 0.5 | 1 |
| Product Manager | 1 (combined with PM) | 1 | 1–2 |
| Project Manager | (combined) | 1 | 1–2 |
| Analytics Lead | 1 | 1 | 1 + 2–4 domain leads |
| Data Scientists | 1 | 2 | 4–8 |
| Data Analysts | 1 | 2–3 | 6–12 |
| Data Engineers | 1 | 2 | 3–6 |
| BI Developer | 0.5 | 1 | 2–3 |
| ML/NLP Engineer | 1 | 1 | 2–4 |
| GIS Analyst | — | 0.5 | 1–2 |
| Social Listening Analyst | (DA covers) | 1 | 2–4 (by language) |
| Media Intelligence Analyst | — | 1 | 2–4 (by language/region) |
| QA / Data Operations | — | 1 | 2–4 (24×7 rota) |
| Security / Privacy Lead | 0.25 | 0.5 | 1 |
| Political/Communications Liaison (client-side or agency) | Client-nominated | 1 (client/agency) | 1–3 (client/agency) |
| **Core total** | **5–7 FTE** | **~12–15 FTE** | **~32–60 FTE** |
| Operations support (not core) | — | Survey vendor, field-form ops, call-centre (client) | Plus 24×7 war-room shifts, language annotators |

## 24.2 Role cards

| Role | Responsibilities | Required skills | Daily outputs | Tools | Experience |
|---|---|---|---|---|---|
| **Program Director** | Accountable for outcomes, client relationship, risk, commercial | Programme leadership, analytics delivery, stakeholder management, ethics judgement | Leadership stand-up, risk log review, escalation decisions | Roadmap, RAID log | 15+ yrs |
| **Product Manager** | Owns requirements, backlog, UX, acceptance | Product discovery, analytics products, UX | Prioritised backlog, user feedback synthesis | Jira/Linear, Figma | 8+ yrs |
| **Project Manager** | Plan, dependencies, status, vendor coordination | Delivery management, agile | Status report, dependency tracker | Jira, MS Project | 6+ yrs |
| **Analytics Lead** | Analytical quality, KPI framework, report sign-off | Statistics, storytelling, domain knowledge | Approved daily report, KPI changes | SQL, Python, BI | 10+ yrs |
| **Data Scientist** | Statistics, survey analytics, forecasting, NLP, model validation, AI analytics | See §24.3 | Analyses, model runs, insight notes | Python, SQL, statsmodels, sklearn, Transformers | 4–10 yrs |
| **Data Analyst** | Dashboards QA, ad-hoc analysis, report drafting, data checks | SQL, BI, Excel, domain | Report sections, analysis tickets | SQL, Power BI, Python | 2–6 yrs |
| **Data Engineer** | Connectors, pipelines, warehouse, quality tests, lineage | Python, SQL, dbt, orchestration, cloud | Pipeline health, new sources, fixes | Dagster/Airflow, dbt, Postgres/BigQuery | 4–8 yrs |
| **BI Developer** | Dashboards, semantic model, RLS, performance | Power BI/React, DAX/TS, data viz | Dashboard releases | Power BI / Next.js | 4–8 yrs |
| **ML/NLP Engineer** | Multilingual models, embeddings, RAG, serving, monitoring | Transformers, Indic NLP, MLOps | Model releases, eval reports | PyTorch, HF, FAISS/pgvector, FastAPI | 4–8 yrs |
| **GIS Analyst** | Boundaries, geocoding (aggregate), map layers | GIS, spatial SQL, cartography | Map layer updates | QGIS, PostGIS | 3–6 yrs |
| **Social Listening Analyst** | Monitor public conversation, validate clusters, annotate | Languages, platforms, critical reading | Social section of report, validated alerts | Listening tool, Command Center | 2–5 yrs |
| **Media Intelligence Analyst** | Monitor media, story threads, summaries | Languages, media landscape | Media section, story log | Media monitoring feed | 2–5 yrs |
| **QA / Data Operations** | Data checks, pipeline monitoring, 24×7 triage | SQL, runbooks | Data-quality log, incident tickets | Monitoring, ticketing | 2–5 yrs |
| **Security / Privacy Lead** | Security architecture, DPDP alignment, access reviews, incidents | Cloud security, privacy law familiarity | Access review, security findings | IdP, SIEM, KMS | 8+ yrs |
| **Political / Communications Liaison** | Translates leadership questions into analytical asks; context for interpretation; ensures ethical scope | Campaign communications, ethics, domain | Question backlog, context notes | Command Center, AI Analyst | 8+ yrs |

## 24.3 The Data Scientist role — in detail

> **"A Data Scientist is not just someone who builds ML models; the role is to convert data into statistically defensible decision-support."**

| # | Contribution | What it looks like in this programme |
|---|---|---|
| 1 | Statistical analysis | Period comparisons with proper tests; effect sizes rather than raw differences |
| 2 | Survey analysis | Weighting (raking), design effects, MoE, significance, cross-tab suppression |
| 3 | Trend detection | Rolling baselines, change-point detection, seasonality adjustment |
| 4 | Forecasting | Issue/media/digital/ops forecasts with intervals; back-testing |
| 5 | Anomaly detection | Robust thresholds, false-positive tuning with war-room feedback |
| 6 | NLP | Taxonomy design with analysts; model selection; code-mixed text handling |
| 7 | Sentiment analysis | Gold-set design, per-language validation, calibration |
| 8 | Topic modelling | Embedding clustering, coherence checks, analyst-in-the-loop naming |
| 9 | Content-performance analysis | Format × theme matrix, driver regression, confounder checks |
| 10 | Experiment analysis | Power analysis, pre-registration, correct stopping rules |
| 11 | Attribution / measurement (where valid) | Only with experimental or quasi-experimental designs; no over-claiming from last-click data |
| 12 | KPI modelling | Metric definitions, composite index design and sensitivity analysis |
| 13 | Model validation | Hold-outs, rolling-origin evaluation, calibration |
| 14 | Uncertainty estimation | Bootstrap, analytical CIs, prediction intervals |
| 15 | Data-quality analysis | Quantifying coverage/duplication; impact of quality issues on conclusions |
| 16 | Executive insights | Plain-language "what changed / how sure are we / what to check next" |
| 17 | AI-agent development | Tool definitions for the AI Analyst; guardrails; evaluation sets |
| 18 | RAG analytics | Retrieval quality (recall@k, citation validity), chunking strategies |
| 19 | Automated reporting | Parameterised report generation from the metric store |
| 20 | Model monitoring | Drift, performance decay, alert precision |
| 21 | Bias checks | Per-language/per-region performance; survey representativeness |
| 22 | Reproducibility | Version-controlled code, pinned environments, data snapshots, seeds |
| 23 | Documentation | Model cards, analysis notes, methodology appendices |

**A day in the life (campaign phase):** 06:30 pipeline and alert review → 07:00 daily report sign-off with Analytics Lead → 09:00 war-room stand-up → deep-dive analysis on an open question (e.g., "is the helpline dip driven by language mix?") → model monitoring check → 16:00 insight note to leadership → evening: gold-set review with annotators.

## 24.4 Operating rhythm

| Cadence | Forum | Output |
|---|---|---|
| Daily 07:00 | Daily War-Room Report published | Report + alerts |
| Daily 09:00 | War-room stand-up (15 min) | Actions and owners |
| Twice weekly | Data-quality & model review | Fixes, recalibrations |
| Weekly | Executive review (45 min) | Weekly report, decisions |
| Fortnightly | Governance board (data, privacy, compliance) | Approvals of new sources/purposes/models |
| Monthly | Commercial & roadmap review | Scope changes, cost report |

## 24.5 SLAs (indicative — Professional tier)

| Service | SLA |
|---|---|
| Daily report | Published by 08:00 IST, 7 days/week in campaign phase |
| Critical alert acknowledgement | ≤ 15 min (24×7 in high-intensity phase; business hours otherwise) |
| Dashboard availability | 99.5% monthly |
| Priority source freshness | ≤ 60 min where source permits |
| Ad-hoc analysis request | Standard: 2 business days; urgent: same day (capped per week) |
| Incident response (P1) | Engage ≤ 30 min; status updates hourly |

## 24.6 Escalation matrix

| Level | Trigger | Who | Time |
|---|---|---|---|
| L1 | Alert raised / data issue | On-duty analyst / Data Ops | Immediate |
| L2 | High alert unresolved 1 h; pipeline down > 1 h; client-visible error | Analytics Lead / Data Engineering Lead | ≤ 1 h |
| L3 | Critical alert; compliance exception; security incident; SLA breach | Programme Director + Security/Privacy Lead + Client Compliance Officer | ≤ 30 min |
| L4 | Legal/regulatory exposure; data breach; major reputational risk | Agency leadership + Campaign legal counsel | Immediate |

## 24.7 Business continuity (added capability)

Poll-week runbooks cover: cloud-region incident (warm standby), connector/API outage (manual file-drop fallback), LLM provider outage (AI Analyst degrades to dashboards + templated summaries), key-person absence (cross-trained pairs), power/network failure at war-room (remote access with MFA, mobile hotspots), and vendor feed delays (SLA escalation and coverage banners).

# 25. Proof of Concept (4–6 weeks)

## 25.1 Plan

| Week | Focus | Deliverables |
|---|---|---|
| **1** | Data discovery · source mapping · architecture · KPI definition | Source Registry v1; data-access status per platform (verified); architecture decision record; KPI tree & metric definitions v1; RBAC matrix; POC success criteria signed |
| **2** | Data ingestion · cleaning · database · first dashboard | Pipelines for 6+ sources (synthetic + authorised samples); quality tests; PostgreSQL model; Executive Overview v1 |
| **3** | Social/NLP pipeline · survey analytics · historical analytics | Language ID, topic, sentiment models with gold-set metrics; survey engine (weights, MoE, significance); ECI historical results layer |
| **4** | AI Analyst · alerts · automated reporting | AI Analyst with tools + RAG + citations; alert engine (4 levels); auto-drafted daily report |
| **5** | Validation · security · UX improvements | Model validation report; hallucination/red-team test results; SSO/MFA/RBAC; audit logs; usability fixes |
| **6** | Executive demo · documentation · handover | Live demo; model cards; data dictionary; runbooks; production recommendation & plan |

A 4-week "fast" variant compresses weeks 5–6 into weeks 3–4 by limiting scope to 4 modules.

## 25.2 Demo scenario — fictional constituency

- **Aranyapur AC (FICTIONAL)**: 4 blocks (North, River, Market, Hill), 24 zones (Z01–Z24), six-week window (1 Aug–11 Sep 2026).
- **100,000 synthetic records** (no real voter database): 60,000 public-style social mentions; 6,000 media items; 12,000 anonymous survey responses in 3 waves; 9,000 field activities; 1,500 owned content posts with performance and spend; 11,500 call-centre operational records.
- **Embedded storyline** for the demo: a synthetic water-pipeline outage on 31 Aug produces a social spike, a regional media surge, a helpline service dip and a significant rise in survey salience — showing how the Command Center links signals across sources.
- Every screen and export carries the label **"DEMO DATA — SYNTHETIC"**. Generator: `demo/generate_synthetic_data.py` (seeded, reproducible); charts: `demo/build_charts.py`.

## 25.3 Technology POC architecture

```
          ┌─────────────────────────── Scheduled ETL (Dagster/cron) ───────────────────────────┐
 Sources ─┤  CSV/API samples ─► raw (object store) ─► quality tests ─► dbt models (PostgreSQL)   │
          └───────────────────────────────────────────┬─────────────────────────────────────────┘
                                                      │
          NLP pipeline (Python: LID → normalise → topic/sentiment/NER → embeddings (SentenceTransformers))
                                                      │                         │
                                             PostgreSQL + metric views    pgvector / FAISS index
                                                      │                         │
                                  FastAPI service (RBAC via SSO token, audit middleware)
                                                      │
                          ┌───────────────────────────┼─────────────────────────────┐
                    Power BI / React UI        LLM + tool router (AI Analyst)   Report generator (PDF/PPTX)
```

**Conceptual API endpoints** (full sketch in `poc/openapi.yaml`):

| Method | Endpoint | Returns |
|---|---|---|
| GET | `/dashboard/overview` | Health score, domain scores, KPI strip, top changes, data-as-of |
| GET | `/social/trends?from&to&topic&platform&language` | Daily volume, anomaly flags, sentiment with CIs, coverage index |
| GET | `/media/intelligence?from&to` | Volume by outlet type, tone, issues, story threads |
| GET | `/survey/summary?wave&question` | Weighted estimates, MoE, n, n_eff, significance vs previous wave |
| GET | `/field/operations?block&zone` | Completion, coverage, on-time, bottlenecks |
| GET | `/digital/scorecard?period` | Scorecard metrics vs prior period and targets |
| GET | `/alerts?severity&status` | Alert queue |
| POST | `/alerts/{id}/ack` | Acknowledge/escalate/close with note |
| GET | `/compliance/items?status` | Content items with approval/certification/label status |
| GET | `/data-quality/sources` | Source registry health |
| GET | `/metrics/{metric_id}` | Metric definition + values (metric store) |
| POST | `/ai/query` | Answer with facts, interpretation, citations, data-as-of, confidence |
| GET | `/reports/daily/{date}` | Rendered daily report |
| GET | `/lineage/{metric_id}` | Source-to-metric lineage |

## 25.4 POC acceptance criteria (measurable)

| # | Criterion | Test | Pass threshold |
|---|---|---|---|
| AC-01 | Dashboard loads successfully | Scripted load of 6 POC modules, 20 runs | P95 < 3 s; 0 errors |
| AC-02 | Data refresh works | Scheduled ETL over 5 consecutive days | ≥ 99% job success; freshness SLA met |
| AC-03 | Source lineage available | Random 10 KPI tiles traced to source | 10/10 traceable |
| AC-04 | NLP pipeline works end-to-end | Process 50k texts | ≥ 99% processed; throughput documented |
| AC-05 | Sentiment validated on test set | Held-out gold set (≥ 500/lang for Hindi, English, Hinglish) | Macro-F1 ≥ 0.70 per language; report per class |
| AC-06 | Issue detection works | Back-test on injected/known events | Detects ≥ 90% of labelled events; ≤ 6 h lag; precision ≥ 60% |
| AC-07 | AI Analyst answers only from approved data | 60-question eval set incl. 15 out-of-scope/red-team | ≥ 95% grounded answers; 100% correct refusals on policy-violating prompts; 0 fabricated numbers |
| AC-08 | Citations displayed | Same eval set | 100% of factual answers carry ≥ 1 valid citation and data-as-of |
| AC-09 | Role-based access works | Test users for 4 roles | 0 unauthorised data exposures in 40 test cases |
| AC-10 | Audit logs work | Logins, queries, exports, AI prompts, approvals | 100% of test events captured, immutable |
| AC-11 | Report generation automated | Daily report for 5 days | Auto-draft ≥ 70% of sections; analyst edit time ≤ 30 min |
| AC-12 | Alerts trigger correctly | Synthetic scenarios (spike, pipeline failure, missing AI label, spend threshold) | 100% trigger at correct severity; ≤ 5 min latency |
| AC-13 | Model metrics documented | Model registry | Model card for every POC model |

**POC success = all Must criteria (AC-01–AC-10, AC-12) met and ≥ 2 of 3 remaining; leadership usability score ≥ 4/5.**

# 26. Roadmap

## 26.1 30 / 60 / 90 days (post-POC production)

| Horizon | Theme | Outcomes |
|---|---|---|
| **Day 0–30** | **Foundation** | Production cloud (Indian region), SSO/MFA/RBAC, Source Registry, 10–15 sources live, metric store v1, Executive Overview + Digital + Social + Field modules, daily report automated, governance board running |
| **Day 31–60** | **Intelligence** | Media, Survey, Issue, Geographic modules; multilingual NLP expanded to target regional languages; alert engine tuned; experiment registry; compliance control tower v1 |
| **Day 61–90** | **AI + Automation + Command Center** | AI Analyst GA with evaluation harness; RAG library; forecasting module; weekly report automation; war-room screens; DR test; pen-test; adoption KPIs |

## 26.2 Election-cycle roadmap

| Phase | Analytics focus | Compliance & operations focus |
|---|---|---|
| **Pre-campaign** (months before notification) | Baselines: historical results, public indicators, issue baselines, digital benchmarks; survey Wave 0; taxonomy & gold sets | Source authorisations, DPAs, consent notices, RBAC, policies, training |
| **Campaign** (after announcement/MCC) | Daily reports, alerts, content learning, field coverage, media monitoring | MCC-aware workflows; MCMC certification tracking; AI-label ledger; spend tracking |
| **High-intensity phase** (final weeks) | Intraday refresh on priority sources; 24×7 war-room; tighter alert SLAs | Takedown SLA timers; heightened security monitoring; DR warm standby |
| **Final phase** (48-hour silence window per phase) | Internal monitoring continues; **no publishing workflows**; operational analytics only | Silence-period calendar guard active; paid items verified paused; exit-poll window restrictions |
| **Poll day** | Operational analytics only: helpline service levels, field logistics status, incident logs, media/social monitoring for misinformation-risk (human-verified, routed to legal/comms and official channels) | Full compliance; no election-matter publication in restricted windows; incident escalation matrix at L3/L4 readiness |
| **Post-poll** | Measurement: campaign operations review, content learnings, forecast accuracy review, data-quality retrospective | Expenditure statement support (digital spend reconciliation), record retention, data deletion per schedule, lessons-learned report |
