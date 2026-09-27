\newpage

# 14. Machine Learning & Multilingual NLP

## 14.1 Model catalogue

**Hard rule:** no model infers an individual's political ideology, preference or likely vote. Models operate on aggregates, content, text of public/licensed items, or operational records.

**(a) Purpose, inputs, outputs and method**

| # | Model | Purpose | Input | Output | Method |
|---|---|---|---|---|---|
| M1 | KPI driver regression | Explain which factors are associated with engagement changes | Content features (format, theme, length, language, hour, platform, boost) | Coefficients / partial effects with CIs | OLS / regularised regression on log engagement |
| M2 | Content "high-performer" classifier | Flag content likely to exceed median ER *for format planning* | Content metadata (no audience attributes) | Probability + drivers | Logistic regression → gradient boosting if lift justified |
| M3 | Issue/topic classifier | Map text to the campaign issue taxonomy | Public/licensed text, survey open-ends, field issue notes | Issue label(s) + confidence | Fine-tuned multilingual encoder; zero-shot fallback |
| M4 | Sentiment/tone classifier | Aggregate sentiment/tone by topic | Public/licensed text | Pos/neu/neg + confidence | Fine-tuned multilingual encoder |
| M5 | Clustering / emerging-topic detection | Find new story clusters | Text embeddings | Clusters, keyphrases, growth | Embeddings + HDBSCAN/BERTopic-style topic modelling |
| M6 | Near-duplicate detector | De-duplicate; spot copy-paste amplification | Text, embeddings, MinHash | Duplicate groups | MinHash/LSH + cosine similarity |
| M7 | Time-series forecaster | Issue-volume, media-volume, digital KPI, ops forecasts | Daily series + calendar features | Point forecast + 80/95% intervals | Seasonal regression / ETS / Prophet-class; gradient boosting for multi-series |
| M8 | Anomaly detector | Spikes/drops in any KPI | Time series | Anomaly score, severity | Robust rolling median ± k·MAD; STL residuals; isolation forest for multivariate |
| M9 | Turnout-trend model (aggregate) | Contextualise AC-level turnout trends for **operational planning** | Public historical turnout, electors, polling stations, public development indicators | Expected turnout range per AC (not per person) | Hierarchical/regularised regression; Random Forest benchmark |
| M10 | Survey weighting & small-area estimates | Robust aggregate estimates | Survey microdata + population margins | Weighted estimates, MoE | Raking; MRP only with strong justification |
| M11 | PCA / factor analysis | Reduce many indicators to interpretable dimensions (e.g., development index) | Public indicators at AC/district | Components, loadings | PCA |
| M12 | NER & entity linking | Identify public figures, organisations, places, schemes | Public/licensed text | Entities + IDs | Multilingual NER + curated gazetteer |
| M13 | Toxicity / safety classifier | Protect analysts; flag abusive content in monitored spaces | Public text | Toxicity score | Multilingual classifier |
| M14 | Misinformation-risk flagger | Prioritise items for human fact-checking | Public text + propagation features | Risk score + reasons | Claim-matching against verified fact-check library + heuristics |

**(b) Evaluation, risks, limitations and human review**

| # | Model | Evaluation metric | Key risk | Limitations | Human review |
|---|---|---|---|---|---|
| M1 | KPI driver regression | Adj. R², out-of-sample RMSE, coefficient stability | Confounding read as causation | Associational, not causal | Analyst signs off interpretation |
| M2 | Content "high-performer" classifier | ROC-AUC, calibration (Brier), precision@k | Self-fulfilling feedback | Platform algorithm changes shift behaviour | Digital lead reviews |
| M3 | Issue/topic classifier | Macro-F1 per language on gold set | Taxonomy drift, code-mixing errors | Weak on rare dialects | Low-confidence items to analyst queue |
| M4 | Sentiment/tone classifier | Macro-F1, per-class recall, per-language F1 | Sarcasm, political idiom, bias across languages | Social ≠ population | Monthly re-validation |
| M5 | Clustering / emerging-topic detection | Topic coherence, analyst usefulness rating | Spurious clusters | Needs minimum volume | Analyst validates new topic before alert ≥ High |
| M6 | Near-duplicate detector | Precision/recall on labelled pairs | Over-merging similar genuine posts | Paraphrase-heavy campaigns | Coordinated-copy flags reviewed by analyst |
| M7 | Time-series forecaster | MAPE/sMAPE, interval coverage on hold-out | Event shocks | Short histories | Forecast note signed by DS |
| M8 | Anomaly detector | Precision/recall on labelled incidents; alert fatigue rate | False positives | Low-volume series noisy | Triage by war-room analyst |
| M9 | Turnout-trend model (aggregate) | MAE on held-out past elections, interval coverage | Over-interpretation | Structural breaks (delimitation, roll revisions) | Published only internally with caveats |
| M10 | Survey weighting & small-area estimates | Benchmark comparison, design effect | Model-driven small-area noise | Needs adequate sample per cell | Research lead approves |
| M11 | PCA / factor analysis | Variance explained, loading stability | Misleading labels | Linear | Analyst names components |
| M12 | NER & entity linking | F1 on gold set | Ambiguous names | Transliteration variants | Gazetteer curated by analysts |
| M13 | Toxicity / safety classifier | Precision/recall on gold set | Dialect bias | Context-dependence | Human decision on any action |
| M14 | Misinformation-risk flagger | Precision@k of analyst-confirmed items | Labelling legitimate speech as "fake" | Cannot determine truth | **Always human-verified**; never auto-labelled |

## 14.2 Multilingual NLP layer

| Capability | Approach | Notes |
|---|---|---|
| Language detection | fastText-class LID + script detection + Hinglish/romanised heuristics | Code-mixed text is the norm, not the exception |
| Hindi, English, Hinglish | Multilingual encoders (MuRIL, IndicBERT, XLM-R-class) fine-tuned on campaign gold sets | Separate metrics for each |
| Regional languages | Per-language evaluation; IndicTrans2 (22 scheduled languages, MIT licence) for translation where needed | Prioritise the languages of the target geography |
| Romanised Indian languages | Transliteration normalisation (e.g., IndicXlit-class) before classification | Major error source if ignored |
| Spell correction / normalisation | Lexicon + transliteration-aware normalisation | Preserve original text for audit |
| Topic classification | M3 | — |
| Sentiment | M4 | — |
| NER | M12 | — |
| Event detection | Burst detection on entity + location + keyphrase co-occurrence | Analyst validation |
| Issue extraction | Taxonomy classification + keyphrase extraction | — |
| Trend detection | Velocity vs baseline, change-points | — |
| Duplicate detection | M6 | — |
| Toxicity/safety | M13 | — |
| Misinformation-risk | M14 | — |
| Content classification | Format/theme tagging of owned content | Feeds content matrix |

**Human-labelled gold sets (added capability).** For each priority language (incl. Hinglish and romanised forms) we build a stratified gold set (target ≥ 1,500 items per language for sentiment/topic in production; ≥ 500 in POC), double-annotated with inter-annotator agreement (Cohen's κ ≥ 0.70 target). Models are accepted only if they meet per-language thresholds (e.g., macro-F1 ≥ 0.70 for sentiment in POC; ≥ 0.75 in production) and **results are reported per language**, not just overall.

# 15. AI Campaign Analyst & RAG

## 15.1 Purpose

A secure, internal assistant that answers leadership and analyst questions **from approved, governed data only**, e.g.:

- "What changed in the last 24 hours?"
- "Which issues are trending?"
- "Show digital performance versus last week."
- "What data sources have quality issues?"
- "Summarise today's media coverage."
- "Which campaign activities had the highest measured engagement?"
- "Compare this week with the previous four weeks."

## 15.2 Architecture

![AI Analyst architecture (from the executive deck)](../deliverables/slides/slide-19.png)

```
 User (SSO, role) ──► Policy & intent guard ──► LLM planner ──► Tool router
                                                                  │
          ┌──────────────────────┬────────────────────┬───────────┴─────────┬─────────────────────────┐
          ▼                      ▼                    ▼                     ▼                         ▼
   Metrics API (metric     Parameterised SQL     Search over         Vector retrieval (RAG)     Analytics APIs
   store, RLS-enforced)    templates (read-only)  reports/alerts      + metadata filters +        (forecast, anomaly,
                                                                      reranker                    survey engine)
          └──────────────────────┴────────────────────┴─────────────────────┴─────────────────────────┘
                                                      │  verified data + source IDs + timestamps
                                                      ▼
                          Answer composer ──► Grounding & numeric checker ──► Response with citations,
                                                                              "data as of", confidence,
                                                                              facts vs interpretation
                                                      │
                                                      ▼
                                   Audit log (prompt, tools, sources, model version, answer)
```

## 15.3 Behavioural contract

The AI Analyst **must**:

1. Retrieve source data through tools — never answer numeric questions from model memory.
2. Cite internal sources (dataset/metric ID, report ID, document + page) for every factual claim.
3. Show the data timestamp ("data as of 07:00 IST").
4. Show confidence (High/Medium/Low) based on data quality, coverage and model confidence.
5. Separate **Facts** (from data) and **Interpretation** (analyst-style reading), labelled.
6. Never fabricate numbers; the numeric checker verifies every number in the answer appears in tool outputs (or is a deterministic calculation from them).
7. Never invent sources; citations are generated from tool metadata, not by the LLM.
8. Never make unsupported political predictions (e.g., seat or vote-share predictions) and never produce individual-level profiling or persuasion scripts — it declines and explains.
9. Respect RBAC: the user sees only what their role permits; retrieval is filtered by permissions.

**Example (DEMO):**

> **Q:** What changed in the last 24 hours?
>
> **Facts** — (1) De-duplicated public mentions: 3,849 on 31 Aug vs prior 7-day median 1,314 — flagged **High** anomaly *[metric: social.mentions_daily; alert A-0931; data as of 01 Sep 07:00]*. (2) 61% of that day's mentions relate to *Water supply* *[model M3 v1.2]*. (3) Regional/hyperlocal media items on the same issue: 123 in 24h vs a prior daily average of 9.9 *[media.mentions_daily]*. (4) Helpline answer rate on 31 Aug: 85% (SLA 90%) *[ops.call_answer_rate]*.
>
> **Interpretation** — The social and media signals are consistent with a local service-disruption story. Social data covers public posts only (18% geo-attributable), so geographic spread is uncertain.
>
> **Suggested analytical follow-ups** — Validate with field issue reports from affected zones; check call-centre category mix; add a question in the next survey wave if the issue persists.
>
> *Confidence: Medium (coverage limits). Sources: 4 datasets, 1 alert.*

## 15.4 RAG knowledge base

| Collection | Contents (authorised only) | Metadata | Access |
|---|---|---|---|
| Campaign reports | Daily/weekly reports, analyses | date, type, author, approval | Role-based |
| Historical reports | Past campaign reviews | year, geography | Role-based |
| Survey methodology | Questionnaires, sampling, weighting notes | wave, vendor | Research + leadership |
| Public election documents | ECI statistical reports, handbooks, MCC compendia, press notes | issuing body, date, URL | All |
| Campaign SOPs | War-room SOPs, escalation matrix | version | All |
| Content-performance reports | Test results, learnings | period, channel | Digital + leadership |
| Media reports | Daily summaries | date | Media + leadership |
| Compliance documents | Approved policies, legal guidance received | version, approver | Compliance + leadership |

Pipeline: document intake (approval required) → parsing/OCR → chunking by structure → multilingual embeddings → vector index (pgvector/FAISS) + BM25 hybrid → **metadata filtering** (role, date, doc type) → **reranking** (cross-encoder) → **grounded generation** with quote-level citations → citation verification → answer. Every answer carries **source traceability** to document ID and page/section.

## 15.5 Hallucination protection & red-team harness (added capability)

| Control | Mechanism |
|---|---|
| Tool-first answering | Numeric intents must call a tool; no tool → "I don't have verified data for that" |
| Numeric grounding check | Regex-extract numbers from the draft; each must match tool output (tolerance for rounding) |
| Citation integrity | Citations inserted from tool metadata; LLM cannot author citation strings |
| Refusal policy | Classifier + rules for out-of-policy requests (individual profiling, persuasion scripts, outcome predictions, legal conclusions) |
| Evaluation set | 200+ questions (POC: 60) with expected sources; measured weekly: answer accuracy, citation validity, refusal correctness |
| Red-team prompts | Prompt-injection in retrieved documents, requests for PII, "predict the winner", "write a message to persuade X", jailbreaks |
| Versioning | Prompts, tools and model versions logged per answer; regression tests on change |

# 16. Security

| Control | Specification |
|---|---|
| **RBAC** | Roles mapped to SSO groups; least privilege; row-level security by geography/team; column masking for sensitive fields |
| **SSO** | SAML 2.0 / OIDC with the Agency's identity provider |
| **MFA** | Mandatory for all users; phishing-resistant (FIDO2/passkeys) for admins |
| **Encryption at rest** | AES-256 with cloud KMS; customer-managed keys in Enterprise tier |
| **Encryption in transit** | TLS 1.2+ everywhere; HSTS; mTLS for service-to-service in production |
| **Secrets management** | Cloud secrets manager/Vault; no secrets in code, notebooks or chat; automated secret scanning in CI |
| **Audit logs** | Centralised, immutable; retention per §9; alerts on anomalous access (bulk export, off-hours admin) |
| **API key rotation** | ≤ 90 days; immediate on staff exit or suspected exposure |
| **Environment separation** | Separate dev/test/prod accounts/projects; prod data never in dev; synthetic data for testing |
| **Backup** | Daily snapshots + PITR; encrypted; cross-zone in-region |
| **Disaster recovery** | Documented DR plan; RPO/RTO per §7; semi-annual DR test; poll-week warm standby (Enterprise) |
| **Incident response** | 24×7 on-call in high-intensity phase; CERT-In 6-hour reporting path; DPDP breach workflow; comms templates |
| **Data retention** | Per Source Registry; automated purges |
| **Least privilege** | Just-in-time elevation; quarterly access reviews; separate break-glass accounts |
| **Endpoint & people** | Managed devices for analysts; DLP on exports; security training; background checks for privileged roles |
| **Application security** | OWASP ASVS L2 target; dependency scanning; annual third-party penetration test (pre-high-intensity phase) |
| **LLM security** | Prompt-injection defences; output filtering; no training on client data (contractual); data-region controls |

# 17. Responsible AI & Model Governance

## 17.1 Responsible AI principles

| Principle | What it means in this platform |
|---|---|
| Human oversight | Humans decide; AI drafts, flags and explains. Critical alerts and all external-facing outputs require human sign-off |
| No fabricated information | Tool-grounded answers; numeric and citation checks |
| No unsupported prediction | Forecasts only where validated; intervals and limitations always shown; no seat/vote predictions from social data |
| Explainability | Driver analysis, feature importance, model cards; plain-language explanations for leadership |
| Source traceability | Every number → metric → dataset → source |
| Data minimisation | Aggregate early; drop unnecessary identifiers |
| Privacy | DPDP-aligned; pseudonymisation; purpose limitation |
| Security | §16 |
| Bias monitoring | Per-language, per-region performance tracking of NLP models; survey representativeness checks |
| Model monitoring | Drift, performance decay, alert precision |
| Synthetic-content safeguards | Platform does not generate campaign creative; tracks AI provenance and labels; supports 3-hour takedown workflows |
| Compliance review | Legal/compliance review of policies, prompts that touch compliance, and any new data purpose |

Alignment references: MeitY **India AI Governance Guidelines** (5 Nov 2025; seven guiding principles), **NIST AI RMF 1.0**, **ISO/IEC 42001:2023** (AI management systems).

## 17.2 Three kinds of "AI" — kept strictly separate

| Category | Definition | Examples | Governing controls |
|---|---|---|---|
| **AI-assisted analytics** | AI used internally to analyse data and draft internal insights | Topic classification, forecasts, AI Analyst answers | Model governance, human review, citations. Internal outputs are not campaign content |
| **AI-generated content** (general) | Any text/image/audio/video produced or materially altered by AI | Draft summaries, translated reports | Internal-use labelling; human review before any external use |
| **AI-generated campaign creative** | Synthetic or AI-altered media published for campaigning | AI-generated video/image/audio ads or posts | **ECI advisory (24 Oct 2025)**: visible label (≥10% area; audio first 10%), responsible-entity disclosure, no deceptive likeness without consent, record-keeping, 3-hour takedown; IT Rules 2026 SGI labelling. **Out of the platform's generation scope** — the Control Tower only tracks provenance, labels and approvals |

## 17.3 Model governance — model card template (required for every model)

| Field | Example (M7 — issue-volume forecaster, DEMO) |
|---|---|
| Model name | `issue_volume_forecaster` |
| Purpose | 14-day forecast of daily de-duplicated mention volume for monitoring-capacity planning |
| Dataset | `social.mentions_daily` (DEMO), anomalies excluded from fit |
| Training period | 01–24 Aug 2026 (validation 25–30 Aug) |
| Features | Linear trend, weekly Fourier terms |
| Target | log(daily mentions) |
| Algorithm | OLS seasonal regression (benchmark: ETS) |
| Metrics | Validation MAPE 2.2% (synthetic data — real-world error will be higher); 80/95% interval coverage tracked |
| Validation | Rolling-origin back-test; residual diagnostics |
| Bias checks | N/A for aggregate volume; platform-mix drift monitored |
| Limitations | Cannot anticipate event shocks; platform access changes break continuity |
| Owner | Lead Data Scientist |
| Version | 0.3.0 |
| Last updated | 2026-09-12 |
| Approval status | Approved for internal planning use (POC) |

Models move through **Draft → Validated → Approved → Monitored → Retired**, with approvals recorded in the model registry and every `model_run` logged.

![Forecast with prediction intervals — DEMO DATA](../demo/charts/forecast_volume.png)
