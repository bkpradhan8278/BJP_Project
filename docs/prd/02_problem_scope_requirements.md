\newpage

# 2. Business Problem

## 2.1 Why traditional campaign reporting is insufficient

Traditional campaign reporting answers "what did each team do yesterday?" It rarely answers "what changed across the whole campaign, where, and what should we look at next?" The failure is structural, not a matter of effort:

- **Reports are team-shaped, not question-shaped.** Digital reports platform metrics, the media cell reports clippings, the survey vendor reports toplines, field reports activity counts. Nobody owns the cross-source question.
- **Numbers disagree.** "Reach" means one thing in Meta, another in YouTube and a third in a vendor deck. Without a metric dictionary, meetings debate numbers instead of decisions.
- **Latency kills relevance.** A manually compiled weekly deck describes a campaign that no longer exists. Issues surface on social and in regional media hours or days before they reach a leadership review.
- **No uncertainty.** A survey that shows 21% vs 18% is presented as a "rise" without a margin of error; a sentiment score from 2,000 posts is treated as public opinion.
- **No audit trail.** Who approved a creative, whether it was MCMC-certified, whether an AI-altered visual was labelled, what was spent where — these live in e-mails and chats, which is untenable under 2026 regulatory expectations.

## 2.2 How Excel / WhatsApp workflows create blind spots

| Workflow symptom | Blind spot it creates | Consequence |
|---|---|---|
| Field reports sent as photos / voice notes in groups | Not machine-readable; lost after scroll | Coverage gaps invisible until too late |
| Multiple versions of the "master" spreadsheet | No single source of truth | Leadership sees conflicting numbers |
| Platform screenshots pasted into decks | No lineage, no refresh | Cannot trace or re-compute a number |
| Media clippings forwarded ad hoc | No classification, no trend | Emerging regional stories missed |
| Survey PDFs from vendors | Raw data, weights, and methodology not retained | Wave-to-wave comparisons unreliable |
| Credentials shared by message | No access control, no revocation | Security and privacy exposure |
| Approvals by thumbs-up emoji | No audit trail | Compliance risk on certification and AI labelling |

## 2.3 Problem inventory

| # | Problem | Who feels it | Target state |
|---|---|---|---|
| P1 | Data scattered across teams | Everyone | Registered sources feeding one governed warehouse |
| P2 | Different teams using different numbers | Leadership | Metric store: one definition per KPI, versioned |
| P3 | Delayed reporting | Leadership, war-room | Daily automated report by 07:00; intraday refresh for priority sources |
| P4 | Manual Excel reporting | Analysts | ≥70% of recurring report content auto-generated |
| P5 | No single source of truth | All | Warehouse + semantic layer + lineage |
| P6 | Social data disconnected from survey data | Strategy, research | Common issue taxonomy across social, media, survey, field, call-centre |
| P7 | Field feedback disconnected from digital analytics | Field, digital | Shared geography and time keys |
| P8 | Media monitoring disconnected from campaign performance | Media cell, comms | Media volume/tone alongside digital and field metrics on one timeline |
| P9 | No systematic anomaly detection | War-room | Statistical alert engine with 4 severity levels |
| P10 | No standardised KPI framework | Leadership | 3-level KPI tree with leading/lagging/diagnostic/data-quality indicators |
| P11 | Difficulty identifying emerging issues | Research, comms | Topic-velocity and novelty detection over multilingual text |
| P12 | Difficulty comparing time periods | Everyone | Standard period-over-period and rolling-baseline comparisons |
| P13 | No confidence/uncertainty in survey interpretation | Leadership | Weighted estimates with MoE and significance flags by default |
| P14 | Poor data quality | Analysts | Automated tests; quality score per source on every dashboard |
| P15 | Lack of auditability | Compliance | Immutable audit log; compliance control tower |
| P16 | Slow decision cycles | Leadership | Decision-support briefs with owners and follow-ups |
| P17 | AI outputs without verified source data | Everyone | Grounded AI Analyst with citations; refuses unsupported answers |

## 2.4 Current state vs future state

**Current state (typical):**

```
  Meta/YouTube/X dashboards ──screenshots──┐
  Ad platform exports ──────────CSV────────┤
  Survey vendor ────────────────PDF────────┤        ┌───────────────┐        ┌────────────────┐
  Media cell ──────────WhatsApp clips──────┼──────► │ Analyst Excel │ ─────► │ Weekly PPT deck│ ──► Leadership
  Field coordinators ──photos/voice notes──┤        │  (manual)     │        │ (stale, no     │
  Call-centre tool ─────────────exports────┤        └───────────────┘        │  lineage)      │
  Public election data ──ad hoc downloads──┘                                 └────────────────┘
        No quality checks · No lineage · No access control · No audit · No uncertainty · Days of latency
```

**Future state (Command Center):**

```
  Sources (API · file · DB · form · survey · licensed monitoring)
        │  registered, lawful-basis tagged, credentials in vault
        ▼
  Ingestion ─► Raw zone (immutable) ─► Data-quality gates ─► Standardised model ─► Warehouse + metric store
                                                                                    │
                                         ┌──────────────────────────────────────────┼──────────────────────┐
                                         ▼                                          ▼                      ▼
                                   ML / NLP layer                          BI & dashboards        Compliance tower
                                         │                                          │                      │
                                         └──────────────► AI Analyst (RAG + tools, citations) ◄────────────┘
                                                                   │
                                                                   ▼
                                              Executive Command Center · Alerts · Automated reports
             Quality scores · Lineage · RBAC/SSO/MFA · Audit logs · Uncertainty on every estimate · Minutes-to-hours latency
```

# 3. Objectives & Success Measures

| Objective | Measure | POC target | Production target (by day 90) |
|---|---|---|---|
| O1 Single source of truth | % of leadership KPIs served from the metric store | 60% | 95% |
| O2 Faster reporting | Time to produce daily war-room report | ≤ 30 min analyst review of auto-draft | Auto-draft by 07:00, published by 08:00 |
| O3 Less manual work | % of recurring report sections auto-generated | ≥ 50% | ≥ 70% |
| O4 Faster issue detection | Median lag between emerging-issue onset and alert (in back-tests) | ≤ 6 h | ≤ 2 h for priority sources |
| O5 Better data quality | Sources with automated quality tests | 100% of POC sources | 100% of production sources |
| O6 Trustworthy AI | AI Analyst answers with valid citations on the evaluation set | ≥ 95% | ≥ 98% |
| O7 Auditable compliance | Published paid/AI content with complete approval + certification + label record | 100% (demo) | 100% |
| O8 Adoption | Weekly active leadership/manager users | Demo | ≥ 80% of named users |

# 4. Scope & Non-scope

## 4.1 In scope

- Ingestion, storage, quality control and modelling of: public/official datasets; historical election results; aggregate demographic and development indicators; campaign-owned first-party data **with documented authorisation**; consented survey data; platform-provided analytics via permitted APIs/exports; licensed media monitoring; permitted public social data; field reports; lawfully collected call-centre operational data; website analytics; campaign spend and compliance records.
- Descriptive, diagnostic, predictive (with uncertainty) and decision-support analytics at **aggregate** levels (constituency, block, ward/zone, channel, content, issue, time).
- Multilingual NLP for public/licensed text (topic, sentiment, entities, issues, duplicates, toxicity, misinformation-*risk* flags for human review).
- AI Analyst with RAG over approved documents and tool-based access to governed data.
- Command Center dashboards, alert engine, automated daily/weekly reports.
- Election Compliance Control Tower (workflow and audit support).
- Security, privacy, data governance, model governance, and responsible-AI controls.
- Team, operating model, POC, and roadmap.

## 4.2 Explicitly out of scope (non-scope)

| Out of scope | Reason |
|---|---|
| Individual-level political-belief, ideology or vote-preference inference or scoring | Ethically unacceptable; sensitive; not required for aggregate decision-support |
| Individualised persuasion, psychological manipulation, micro-targeting on sensitive attributes | Manipulative; conflicts with platform policies and responsible-AI principles |
| Covert tracking of people, private-message/closed-group monitoring, device tracking | Unlawful/unethical; violates privacy and platform terms |
| Scraping personal data or platforms in breach of terms of service | Legal and platform risk |
| Use of voter rolls to build individual profiles | Not required; privacy and legal risk. Aggregate public statistics (e.g., elector counts per AC from ECI statistical reports) are in scope |
| Generating deceptive content, deepfakes, impersonation, or unlabelled synthetic media | Prohibited by ECI advisories and IT Rules; the platform *tracks labels*, it does not generate campaign creative |
| Voter suppression, intimidation or discouraging participation | Unlawful and contrary to democratic norms |
| Publishing exit polls / election-matter in restricted windows | RP Act ss.126, 126A — platform enforces calendar guards |
| Final legal determinations | Owned by the Campaign's legal/compliance team |

# 5. Users & Personas

| Persona | Role | Primary questions | Key screens | Access level |
|---|---|---|---|---|
| **Campaign Director** ("Leadership") | Final decision-maker | What changed? What needs my attention? Are operations on track? | Executive Overview, Alerts, Daily Report, AI Analyst | Read all aggregates; no raw PII |
| **Agency Account Lead** | Runs the client relationship | Is the programme delivering? Are we compliant? | Executive Overview, Compliance, Reports | Read aggregates; approve reports |
| **Head of Digital** | Owns channels and content | Which formats/themes perform? Spend efficiency? | Digital, Content Matrix, Experiments | Digital data incl. spend |
| **Media Cell Lead** | Monitors coverage | What's the coverage trend, tone, and emerging stories? | Media Intelligence, Issue Intelligence | Media data |
| **Research / Survey Lead** | Owns surveys | Are changes significant? Is the sample healthy? | Survey Intelligence | Survey microdata (pseudonymised) |
| **Field Operations Head** | Runs field teams | Where are gaps and bottlenecks? | Field Ops, Geographic | Field data at zone level |
| **Call-centre Manager** | Runs helpline | Service levels, issue categories, backlog | Call-centre | Call operational data (no content recordings unless lawfully authorised) |
| **Compliance Officer** | Legal/compliance liaison | Approval, certification, AI labels, spend, silence period | Compliance Control Tower, Audit | Compliance records, audit logs |
| **Data Analyst / Scientist** | Builds analysis | Is the data right? What explains the change? | Data Quality, notebooks, model registry | Governed warehouse (role-scoped) |
| **Platform Admin / Security Lead** | Runs platform | Who accessed what? Are pipelines healthy? | Admin, Audit, Pipeline status | Admin; no default data access |

# 6. Functional Requirements

Priority: **M** = Must (POC/MVP), **S** = Should (by day 60), **C** = Could (by day 90+).

## 6.1 Data ingestion & management

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Register every data source in a Source Registry with owner, lawful basis/authorisation, permitted purposes, refresh cadence, sensitivity, retention | M |
| FR-02 | Ingest via API connectors (only where access is verified), scheduled file drops (CSV/XLSX/JSON), database replication, manual upload with validation, survey platform exports, form submissions | M |
| FR-03 | Store raw data immutably with ingestion timestamp, source ID and checksum | M |
| FR-04 | Apply automated data-quality tests (schema, completeness, freshness, uniqueness, ranges, referential integrity, anomaly on volumes) and block promotion on critical failures | M |
| FR-05 | Standardise geography (state → district → AC → block/ward/zone), time (IST), language and issue taxonomy | M |
| FR-06 | Maintain column-level lineage from source to dashboard tile and AI answer | S |
| FR-07 | Support pseudonymisation / tokenisation of any personal identifiers at ingestion; drop fields not needed for the stated purpose | M |
| FR-08 | Support deletion requests and retention-based purges with deletion certificates | S |

## 6.2 Analytics & intelligence

| ID | Requirement | Priority |
|---|---|---|
| FR-10 | KPI metric store with versioned definitions consumed by BI, reports and AI | M |
| FR-11 | Period-over-period comparisons (D/D, W/W, vs 4-week baseline) with significance/interval where applicable | M |
| FR-12 | Diagnostic decomposition ("which channel/content/geography/issue drove the change") | S |
| FR-13 | Survey engine: weighting (post-stratification/raking), design effect, MoE, CIs, cross-tabs, significance testing, quality flags | M |
| FR-14 | Forecasts (issue volume, media volume, digital performance, turnout-trend at aggregate level) with prediction intervals, training window, validation metrics | S |
| FR-15 | Anomaly detection on all priority time series | M |
| FR-16 | Content Performance Matrix and experiment registry | S |
| FR-17 | Field and call-centre operational analytics | M |
| FR-18 | GIS layers at aggregate levels with official boundaries where available | S |

## 6.3 NLP & AI

| ID | Requirement | Priority |
|---|---|---|
| FR-20 | Language identification incl. Hinglish and romanised Indian languages | M |
| FR-21 | Topic/issue classification against the campaign issue taxonomy | M |
| FR-22 | Sentiment/tone classification with confidence; validated against human-labelled test sets per language | M |
| FR-23 | Named-entity recognition for public figures, organisations, places, schemes | S |
| FR-24 | Near-duplicate/coordinated-copy detection | S |
| FR-25 | Toxicity/safety and misinformation-*risk* flags routed to human review (never auto-labelled as "fake") | S |
| FR-26 | AI Analyst: natural-language questions answered via tools (SQL/metrics/search/vector) with citations, timestamps and confidence | M |
| FR-27 | RAG over approved document library with metadata filters and access control | M |
| FR-28 | AI Analyst refuses questions outside policy (individual profiling, persuasion scripts, outcome guarantees) and explains why | M |

## 6.4 Command Center, alerts & reporting

| ID | Requirement | Priority |
|---|---|---|
| FR-30 | Campaign Intelligence Health Score with drill-down to 8 Level-2 domains | M |
| FR-31 | 14 dashboard modules (see §18) | M (6 in POC) / S (rest) |
| FR-32 | Alert engine with Critical/High/Medium/Low levels, routing, acknowledgement and closure notes | M |
| FR-33 | Automated Daily War-Room Report (auto-draft, analyst review, approval, distribution) | M |
| FR-34 | Weekly Executive Report (10–15 pages) | S |
| FR-35 | Export to PDF/PPTX with source footnotes and "data as of" timestamps | S |

## 6.5 Compliance Control Tower

| ID | Requirement | Priority |
|---|---|---|
| FR-40 | Track each paid or AI-assisted content item: owner, approver, approval time, MCMC certification ref/status, platform, spend, AI-label status, takedown events | M |
| FR-41 | Silence-period and exit-poll calendar per phase/constituency; blocks scheduled report types and publishing workflows in restricted windows | M |
| FR-42 | Spend tracking vs budget and vs statutory limits (as configured by the compliance team) with alerts | S |
| FR-43 | Immutable audit trail for approvals, overrides and data access | M |

## 6.6 Administration & security

| ID | Requirement | Priority |
|---|---|---|
| FR-50 | SSO (SAML/OIDC), MFA, RBAC + row/column-level security | M |
| FR-51 | Secrets in a managed vault; API key rotation | M |
| FR-52 | Environment separation (dev/test/prod) | M |
| FR-53 | Admin audit and access reviews | S |

# 7. Non-functional Requirements

| Category | Requirement |
|---|---|
| Availability | 99.5% monthly for dashboards (POC: best effort); 99.9% during declared high-intensity phase (Enterprise tier) |
| Freshness | Priority sources ≤ 60 min (where source permits); daily sources by 06:00 IST |
| Performance | Executive dashboard P95 load < 3 s; AI Analyst P95 < 15 s for tool-based answers |
| Scalability | Up to 50 ACs / 1 state in Professional tier; multi-state in Enterprise |
| Security | Encryption in transit (TLS 1.2+) and at rest (AES-256/KMS); least privilege; MFA mandatory |
| Privacy | Data minimisation; pseudonymisation of identifiers; DPDP-aligned notices/consent for first-party data |
| Data residency | Primary storage in Indian cloud regions; CERT-In log retention (180 days in India) |
| Auditability | Every KPI traceable to source; every AI answer logs prompt, tools called, sources, model version |
| Accessibility | WCAG 2.1 AA for dashboards; colour-blind-safe palettes validated |
| Localisation | UI English + Hindi; content analysis in configured Indian languages |
| Recoverability | RPO ≤ 1 h, RTO ≤ 4 h for production (Professional); RPO ≤ 15 min, RTO ≤ 1 h (Enterprise, high-intensity phase) |
| Maintainability | Infrastructure-as-code; CI/CD; data tests in CI; documented runbooks |
| Cost control | Per-module budget alerts; LLM token caps per user/day; monthly cost report |
