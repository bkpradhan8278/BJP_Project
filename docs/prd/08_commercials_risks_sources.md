\newpage

# 27. ROI / Value Framework

We do **not** claim "we will guarantee victory". We measure what the platform can credibly change: speed, quality, visibility and learning.

| Value driver | KPI | Baseline method (Week 1) | Target (Day 90) |
|---|---|---|---|
| Reporting time | Analyst hours to produce daily + weekly reports | Time-and-motion on current process | −60% |
| Manual work | % of recurring report content auto-generated | Report audit | ≥ 70% |
| Issue detection speed | Median lag onset → alert (back-tested on known past incidents) | Reconstruct past incidents | ≤ 2 h for priority sources |
| Data quality | Sources with automated tests; quality score | Source audit | 100%; avg score ≥ 85 |
| Decision cycle | Time from signal to assigned owner/action | War-room log | ≤ 4 h for High/Critical |
| Dashboard adoption | Weekly active named users; AI Analyst queries/user | — | ≥ 80% WAU |
| Content learning | Documented tests with valid results; learnings applied | Experiment registry | ≥ 2 valid tests/week (Professional) |
| Operations visibility | % of planned field activities with structured reports | Field audit | ≥ 95% |
| Media coverage | % of priority outlets/languages monitored | Outlet list | ≥ 90% |
| Model accuracy | Per-language F1; forecast MAPE; interval coverage | Gold sets / back-tests | Meets model-card thresholds |
| Report automation | Automated reports on schedule | — | 100% on-time |
| Compliance assurance | Paid items with certification ref; AI items labelled | Compliance audit | 100% |

**Illustrative efficiency value (not a revenue claim):** if 6 analysts currently spend ~3 hours/day compiling reports, a 60% reduction releases ~11 analyst-hours/day for analysis — roughly 1.4 FTE redeployed to higher-value work.

# 28. Commercial Model

> **Indicative only; the final commercial proposal depends on constituency, election timeline, data availability, staffing, SLA and technology requirements.** All figures in INR, exclusive of GST; third-party pass-through at cost plus a disclosed handling fee.

## 28.1 Cost components

| # | Component | What it covers | Pricing basis |
|---|---|---|---|
| 1 | **One-time setup** | Discovery, architecture, cloud landing zone, connectors, data model, metric store, dashboards, security set-up, training | Fixed fee by tier |
| 2 | **POC** | 4–6 week proof of concept (§25) | Fixed fee; 50% creditable against setup if contracted within 30 days |
| 3 | **Monthly analytics retainer** | Named team, operating rhythm, daily/weekly reports, analysis, model upkeep | Monthly by tier / FTE mix |
| 4 | **Technology/platform fee** | Platform licence/IP use, maintenance, upgrades, support | Monthly |
| 5 | **Cloud/API** | Cloud compute/storage, LLM tokens, paid APIs (e.g., X API credits), map services | Pass-through + handling fee; monthly budget caps |
| 6 | **Survey/data vendor** | CATI/F2F/online survey waves; social-listening and media-monitoring licences; broadcast transcripts | Vendor quotes, passed through |
| 7 | **Field operations enablement** | Form app configuration, training, field data-ops support (field staff themselves are client-side unless separately scoped) | Setup + monthly |
| 8 | **24×7 war-room support** | Shift-based analysts, on-call engineering in high-intensity phase | Per pod per month |
| 9 | **Custom AI development** | New models, agents, integrations beyond tier scope | Per sprint or rate card |
| 10 | **Travel / on-site support** | War-room presence, workshops | At actuals, pre-approved |

## 28.2 Three commercial tiers (indicative bands)

| | **Starter** | **Professional** | **Enterprise** |
|---|---|---|---|
| Typical scope | 1 AC or by-election; 8–12 weeks | 1 PC or up to ~10 ACs; 3–6 months | Multi-constituency / state; 6–12 months |
| Modules | Executive, Digital, Social, Field, Alerts, Daily report, AI Analyst (basic) | All 14 modules; compliance tower; forecasting; experiments | All + custom models, multi-language expansion, multi-tenant views |
| Team (core FTE) | 6–8 | 12–15 | 30–60 |
| Support | Business hours + on-call for Critical | Extended hours; 24×7 in final 2 weeks | 24×7 war-room throughout campaign phase |
| **1. One-time setup** | ₹15–30 lakh | ₹40–80 lakh | ₹1.2–3.0 crore |
| **2. POC** (if taken) | ₹18–35 lakh | ₹18–35 lakh | ₹25–45 lakh (broader discovery) |
| **3. Monthly analytics retainer** | ₹12–22 lakh | ₹30–50 lakh | ₹0.8–2.0 crore |
| **4. Technology/platform fee** (monthly) | ₹1.5–3 lakh | ₹4–8 lakh | ₹10–25 lakh |
| **5. Cloud/API** (monthly, pass-through est.) | ₹0.5–1.5 lakh | ₹2–6 lakh | ₹8–30 lakh |
| **6. Survey/data vendor** | Per vendor quote (see 28.3) | Per quote | Per quote |
| **7. Field ops enablement** | ₹2–4 lakh setup | ₹4–8 lakh setup + ₹1–2 lakh/month | Scoped |
| **8. 24×7 war-room** (per pod/month) | Optional ₹8–12 lakh | ₹10–15 lakh | Included (sized by pods) |
| **9. Custom AI development** | Rate card | ₹5–9 lakh per 2-week sprint | Dedicated pod |
| **10. Travel/on-site** | At actuals | At actuals | At actuals |

## 28.3 Third-party cost guidance (to be validated with vendor quotes)

| Item | Indicative band | Note |
|---|---|---|
| CATI survey | ~₹250–600 per complete | Length, language, incidence dependent **[VERIFY]** |
| Face-to-face (tablet) survey | ~₹450–1,200 per complete | Geography and sampling design dependent **[VERIFY]** |
| Social-listening licence | ~₹1–10 lakh/month | Volume, platforms, languages |
| Media monitoring (print/online) | ~₹1–5 lakh/month | Outlets and languages |
| Broadcast transcripts (licensed) | ~₹2–8 lakh/month | Channels and hours |
| LLM usage | Capped per user/day; typically a small share of cloud/API | Token budgets enforced |
| X API | Pay-per-use credits (reported since Feb 2026) | Budget cap and read limits required |

## 28.4 Rate card (for change requests; per person-day, indicative)

| Role | ₹/day |
|---|---|
| Programme Director | 35,000–50,000 |
| Analytics Lead / Security & Privacy Lead | 20,000–28,000 |
| Senior Data Scientist / ML-NLP Engineer | 16,000–25,000 |
| Data Scientist / Data Engineer | 12,000–18,000 |
| Product / Project Manager | 12,000–18,000 |
| BI Developer / GIS Analyst | 10,000–14,000 |
| Data Analyst | 7,000–11,000 |
| Social / Media Intelligence Analyst | 6,000–9,000 |
| QA / Data Operations | 5,000–8,000 |

## 28.5 Worked example (Professional, 4 months, indicative)

| Line | Calculation | Indicative |
|---|---|---|
| Setup | one-time | ₹60 lakh |
| Retainer | 4 × ₹40 lakh | ₹1.60 crore |
| Platform fee | 4 × ₹6 lakh | ₹24 lakh |
| Cloud/API | 4 × ₹4 lakh | ₹16 lakh |
| Survey | 2 waves × ~₹20 lakh | ₹40 lakh |
| War-room pod | 1 month | ₹12 lakh |
| Travel | estimate | ₹5 lakh |
| **Total** | | **≈ ₹3.17 crore** (range roughly ₹2.3–4.5 crore) |

## 28.6 Cost guardrails (added capability)

Monthly cost report by component; per-module cloud budgets with alerts at 80%/100%; LLM token caps per user/day; approval required for new paid data sources; pass-through invoices shared transparently.

# 29. Client Dependency Checklist

| # | Dependency | Needed by | Owner (client/agency) |
|---|---|---|---|
| 1 | Campaign scope (objectives, questions leadership wants answered) | Week 1 | Agency lead |
| 2 | Geography (states, PCs/ACs, sub-units) | Week 1 | Agency lead |
| 3 | Timeline (key dates, expected phases) | Week 1 | Agency lead |
| 4 | Existing data inventory and samples | Week 1 | Team leads |
| 5 | API access / admin authorisation for owned accounts | Week 1–2 | Digital lead |
| 6 | Dashboard / BI tool access (if reusing) | Week 1 | IT |
| 7 | Survey data, questionnaires, methodology, weights | Week 2 | Research lead |
| 8 | Authorised first-party data with lawful-basis evidence | Week 2 | Data owner + legal |
| 9 | Field report formats and access to the field app | Week 2 | Field head |
| 10 | Media-monitoring access/licences | Week 2 | Media cell |
| 11 | Compliance contact (named) | Week 1 | Agency |
| 12 | Legal contact (named) | Week 1 | Campaign |
| 13 | Cloud preference and accounts | Week 1 | IT |
| 14 | Security requirements (IdP, device policy, residency) | Week 1 | IT/security |
| 15 | Reporting cadence and distribution list | Week 1 | Leadership office |
| 16 | Decision-makers and approval matrix | Week 1 | Leadership office |
| 17 | SLA expectations and support hours | Week 1 | Agency lead |
| 18 | Issue taxonomy input and language priorities | Week 1–2 | Research + comms |
| 19 | Annotators / language reviewers (or approval to use Partner annotators) | Week 2 | Agency |
| 20 | Brand assets **with authorisation** (if any official marks are to be used) | Before external use | Agency |

# 30. Risk Register

Scale: Probability and Impact 1 (low) – 5 (high). Score = P × I.

| # | Risk | P | I | Score | Mitigation | Owner |
|---|---|---|---|---|---|---|
| R1 | Poor data quality (late, incomplete, inconsistent) | 4 | 4 | 16 | Quality gates, source scorecards, badges on tiles, data-ops rota | Data Eng Lead |
| R2 | Incomplete or unavailable APIs | 4 | 3 | 12 | Week-1 verification; file-drop fallbacks; licensed vendors | Data Eng Lead |
| R3 | Platform restrictions / policy changes | 3 | 4 | 12 | Vendor diversity; contractual review; monitor developer changelogs | Product Manager |
| R4 | Biased surveys (sampling, non-response, mode) | 3 | 4 | 12 | Design review, weighting, QC, benchmark checks, AAPOR-style disclosure | Research Lead / DS |
| R5 | Social-media non-representativeness | 5 | 3 | 15 | Coverage index; mandatory caveats; triangulation with survey/field | Analytics Lead |
| R6 | Model drift | 3 | 3 | 9 | Monitoring, monthly re-validation, gold-set refresh | ML Lead |
| R7 | LLM hallucination | 3 | 5 | 15 | Tool-first answers, numeric/citation checks, eval harness, refusal policy | ML Lead |
| R8 | Overfitting (short histories) | 3 | 3 | 9 | Simple baselines, rolling-origin validation, parsimony | DS Lead |
| R9 | False-positive alerts (alert fatigue) | 4 | 2 | 8 | Thresholds tuned with feedback; grouping; precision KPI | Analytics Lead |
| R10 | False-negative alerts (missed issues) | 3 | 4 | 12 | Multi-signal rules; back-tests; analyst scanning | Analytics Lead |
| R11 | Compliance risk (uncertified ads, unlabelled AI, silence period) | 3 | 5 | 15 | Control tower rules; blocking states; legal sign-off | Compliance Officer |
| R12 | Privacy risk (excess personal data, purpose creep) | 3 | 5 | 15 | Minimisation, permitted-use tags, DPIA-style review, audits | Privacy Lead |
| R13 | Cyber risk (breach, credential theft, insider) | 3 | 5 | 15 | SSO/MFA, least privilege, logging, pen-test, DLP, IR runbook | Security Lead |
| R14 | Unrealistic client expectations | 4 | 4 | 16 | "What we will not promise" in contract; acceptance criteria; education | Programme Director |
| R15 | Vendor/API cost overrun | 3 | 3 | 9 | Budget caps; monthly cost report | Project Manager |
| R16 | Key-person dependency | 3 | 3 | 9 | Cross-training; documentation; bench | Programme Director |
| R17 | Reputational risk from misuse of outputs | 2 | 5 | 10 | Scope guardrails; refusal policy; audit logs; ethics escalation | Programme Director |
| R18 | Regulatory change mid-campaign | 3 | 4 | 12 | Legal watch; configurable rules engine | Compliance Officer |

**Heat view:**

| Impact ↓ / Probability → | 1–2 | 3 | 4–5 |
|---|---|---|---|
| **5** | R17 | R7, R11, R12, R13 | — |
| **4** | — | R3, R4, R10, R18 | R1, R14 |
| **3** | — | R6, R8, R15, R16 | R2, R5 |
| **2** | — | — | R9 |

# 31. What We Should Not Promise

| We will **not** promise | Why |
|---|---|
| Guaranteed election outcome | Outcomes depend on factors far outside analytics |
| Exact vote prediction | Not statistically defensible; restricted publication windows; not in scope |
| Complete voter-preference prediction | Neither possible nor ethical at individual level |
| Individual political-belief inference | Prohibited by design |
| Unauthorised personal-data access | Unlawful |
| Secret tracking | Unlawful and unethical |
| Illegal scraping | Breaches law and platform terms |
| Private-message monitoring | Unlawful; privacy violation |
| Guaranteed viral content | Platform algorithms and audiences are not controllable |
| Guaranteed persuasion | Out of scope; manipulative framing rejected |
| Guaranteed ROI | We commit to measurable operational KPIs (§27), not outcomes |

# 32. Visual Design & Asset Sourcing

## 32.1 Design direction

A premium political-technology aesthetic that is **professional, not propagandistic**: deep navy/charcoal as the dominant field; saffron as the signal/accent colour; white space; subtle gold for highlights; clean data visualisation; abstract network/"constellation" motifs representing connected data; dashboard mock-ups; no inflammatory imagery, no party symbols, no leaders' photographs.

| Token | Hex | Use |
|---|---|---|
| Deep navy | `#0B1F3A` | Title/closing slides, headers |
| Charcoal ink | `#1B2330` | Body text |
| Saffron | `#E2711D` | Accent, series 1, key numbers |
| Signal blue | `#2F6DB5` | Series 2 |
| Teal | `#1A9A8F` | Series 3 |
| Ochre-gold | `#A67C1A` / `#C9A227` | Series 4 / highlights |
| Light surface | `#F4F6F9` | Cards |

The categorical palette (saffron, blue, teal, ochre) passed an automated colour-vision-deficiency and contrast validation on a light surface.

**Branding rule:** party marks are used **only where the Agency holds written authorisation**; the deck contains a clearly labelled **"[Client logo placeholder — official assets only with authorisation]"** box.

**Map rule:** no India outline is used in the deck; any national/state map in client-facing material must use official Survey of India boundaries.

## 32.2 Visual assets register

| Asset | Source | Licence / usage consideration | Where used |
|---|---|---|---|
| Abstract network cover visual | Generated for this project (`demo/build_charts.py`) | Own work; no third-party rights | Slides 1, 34 |
| All charts (anomaly, sentiment, survey, content matrix, hex map, forecast, media, call-centre) | Generated from synthetic DEMO data | Own work; labelled DEMO DATA | Slides 12–18 and PRD |
| Diagrams, dashboard mock-ups, org charts, roadmap | Drawn natively in PowerPoint | Own work; editable | Slides 2–35 |
| *Optional:* night-lights Earth imagery | NASA Earth Observatory (Black Marble) | NASA imagery is generally not copyrighted but NASA media guidelines apply (no endorsement implied) — **verify per image** | Optional replacement for cover |
| *Optional:* control-room / team photographs | Unsplash / Pexels | Free commercial use under their licences; avoid identifiable people without releases; no implied endorsement | Optional for team slide |
| *Optional:* icons | Google Material Symbols (Apache 2.0) | Attribution in notes | Optional |
| *Optional:* official maps | Survey of India | Official boundaries; terms per SoI | Any national/state map |

No external images were used in the current deck; if suitable images cannot be safely sourced, the generated abstract visuals remain.

# 33. Presentation — Slide-by-Slide Content

The executive deck (`deliverables/Election_Intelligence_Command_Center_Executive_Deck.pptx`, 35 slides) follows this structure:

| # | Slide | Purpose | Key content | Visual |
|---|---|---|---|---|
| 1 | Cover | Set positioning | Title, subtitle, "AI + Data + Digital Intelligence Partner", placeholder logos | Generated network visual |
| 2 | Executive Vision | The idea in one loop | Data → Intelligence → Insight → Decision Support → Measurement → Learning | 6-node loop |
| 3 | Why Campaign Intelligence Matters | Urgency | 4 regulatory/operational shifts of 2025–26 | Stat cards with dates |
| 4 | The Current Problem | Pain | Fragmented workflows; 6 blind spots | Current-state diagram |
| 5 | Our Solution | Before/after | Current vs future state | Two-column comparison |
| 6 | Command Center Concept | Product | 9 capability pillars on one intelligence layer | Layered pillars |
| 7 | Data Ecosystem | Breadth with discipline | Six source families A–F | 6 cards |
| 8 | Data Sources & Access Reality | Honesty on APIs | Platform-by-platform access status to verify | Status table |
| 9 | Data Architecture | Engineering | Sources → … → Command Center | Pipeline diagram |
| 10 | Data Model & Analytics Stack | Structure | Conceptual ERD + 4 analytics levels | ERD + ladder |
| 11 | AI / NLP Layer | Multilingual intelligence | Listening → NLP → Topic → Sentiment → Trend → Alert | Flow + language chips |
| 12 | Social Intelligence | Demo | Anomaly chart + coverage caveat | Chart |
| 13 | Media Intelligence | Demo | Weekly outlet mix + modules | Chart |
| 14 | Survey Intelligence | Rigour | Weighted CIs; methodology controls | Chart |
| 15 | Digital Analytics | Scorecard | Scorecard + content matrix | Chart + KPI cards |
| 16 | Field & Call-centre Operations | Operations | KPIs + service levels | Chart + cards |
| 17 | GIS Intelligence | Geography | Zone map + layers + guardrails | Hex map |
| 18 | Forecasting & ML | Honest prediction | Forecast with intervals + model card | Chart + card |
| 19 | AI Analyst | Grounded AI | Architecture + sample answer with citations | Diagram + chat mock |
| 20 | Real-Time Alerts | Early warning | 4 levels, SLAs, examples | Severity ladder |
| 21 | Executive Dashboard | The product | Health score + domain chips + KPI strip | Dashboard mock-up |
| 22 | Compliance Control Tower | Auditability | Status table + regulatory anchors | Tower mock-up |
| 23 | Security & Governance | Trust | Controls grid | Shield grid |
| 24 | Responsible AI | Ethics | Principles + three kinds of AI | Three-column |
| 25 | Team Structure | Delivery | Three scenarios | Org chart |
| 26 | The Data Scientist Role | Depth | 23 contributions in 5 clusters | Cluster cards |
| 27 | POC Plan | Next step | 6-week plan + acceptance | Gantt |
| 28 | Technology POC | Build | Stack + endpoints | Architecture + endpoint list |
| 29 | Roadmap | Horizon | 30/60/90 + election cycle | Timeline |
| 30 | Commercial Model | Investment | Three tiers | Tier table |
| 31 | KPIs & Value | Measurable outcomes | KPI tree + value metrics | Tree + cards |
| 32 | Risks & Mitigation | Candour | Top risks heat map | Matrix |
| 33 | Boundaries & Dependencies | Expectations | What we won't promise; what we need | Two columns |
| 34 | From Campaign Data to Campaign Intelligence | Close | Platform · Team · Technology · Governance · Outcomes | Network visual |
| 35 | Sources & Notes | Credibility | Key sources, disclaimers | List |

# 34. Critical Self-Review & Red-Team

## 34.1 "What important capabilities have we missed?" — checklist result

| Capability | Covered in | Status |
|---|---|---|
| Data governance | §9 | ✓ |
| Privacy | §9, §16, §17 | ✓ |
| Cybersecurity | §16 | ✓ |
| Data lineage | §9, §11, AC-03 | ✓ |
| Data quality | §6, §9, §18 (screen 12) | ✓ |
| Model governance | §17.3 | ✓ |
| AI hallucination protection | §15.5 | ✓ |
| Multilingual NLP | §14.2 | ✓ |
| GIS | §22 | ✓ |
| Survey methodology | §8.3, §13.4 | ✓ |
| Media intelligence | §13.3 | ✓ |
| Digital analytics | §21 | ✓ |
| Field operations | §13.5 | ✓ |
| Call-centre analytics | §13.6 | ✓ |
| Anomaly detection | §14 (M8), §19 | ✓ |
| Forecasting | §14 (M7, M9), §17.3 | ✓ |
| Experiment measurement | §21.3 | ✓ (added) |
| Automated reporting | §23 | ✓ |
| Executive dashboards | §18 | ✓ |
| Compliance | §10 | ✓ |
| AI-content labelling | §10.2, §17.2 | ✓ |
| Audit trails | §9, §10, §16 | ✓ |
| Disaster recovery | §7, §16 | ✓ |
| Business continuity | §24.7 | ✓ (added) |
| Vendor/API dependency | §8.4, §9, R2/R3 | ✓ |
| Cost management | §28.6 | ✓ (added) |
| Staffing | §24 | ✓ |
| SLA | §24.5 | ✓ |
| Escalation matrix | §24.6 | ✓ (added) |
| Client dependencies | §29 | ✓ |
| POC success criteria | §25.4 | ✓ |
| Acceptance criteria | §25.4 | ✓ |

## 34.2 Red-team review

| Lens | Finding | Action taken |
|---|---|---|
| **Technical feasibility** | Real-time social listening at scale depends on paid, permitted access — not free APIs | API reality table; licensed vendors; file-drop fallbacks; "verify" tags |
| | Hinglish/romanised text breaks off-the-shelf sentiment models | Normalisation + per-language gold sets + thresholds |
| | 6-week POC risks over-scope | 6 modules in POC; others on roadmap; 4-week variant defined |
| **Legal/compliance** | Several ECI instructions verified through secondary reporting only | Marked [VERIFY]; legal sign-off gate in Week 1 |
| | Exit-poll and silence-period constraints could be breached by automated publishing | Calendar guard blocks publishing workflows and restricted report types |
| | Using party branding without authorisation | Placeholders only; authorisation required |
| | Incorrect India boundaries on maps | No national outline; SoI boundaries required |
| **Privacy** | Call-centre, CRM and field data can contain personal data | Minimisation, pseudonymisation, permitted-use tags, no caller PII in POC |
| | Public social data still contains personal data | Aggregate early; drop handles after de-dup; no individual profiles |
| | "Creator amplification" could drift into profiling individuals | Restricted to public figures/media/organisations, aggregated by account type |
| **AI hallucination** | LLM may invent numbers or sources | Tool-first answers, numeric checker, system-generated citations, eval harness, AC-07/AC-08 |
| | Prompt injection via retrieved documents | Document intake approval; injection filters; red-team suite |
| **Data quality** | Field reports late → under-counted completion | Timeliness KPI; late-report reconciliation; badges |
| | Survey weights unstable with small cells | Trimming; cell suppression; n_eff shown |
| **Unrealistic claims** | Health score could be misread as a win probability | Defined as operational; explicit disclaimer on screen |
| | Synthetic demo metrics (e.g., 2.2% MAPE) look better than reality | Model card states real-world error will be higher |
| **Missing team roles** | Annotators and language reviewers; 24×7 data-ops | Added to scenario C and dependencies |
| **Missing costs** | Listening/media licences, X API credits, annotation, pen-test, DR standby | Added to §28.3 and tiers |
| **Missing dependencies** | Legal contact, annotators, brand authorisation | Added to §29 |
| **Missing POC requirements** | Usability, red-team test, RBAC test users | AC-07, AC-09, usability score |

## 34.3 Additional capabilities added after self-review (and why)

| # | Capability | Why it matters |
|---|---|---|
| 1 | Source & lawful-basis registry with permitted-use tags enforced at query time | Turns purpose limitation from policy into a technical control |
| 2 | Metric store / semantic layer | Ends "whose number is right" debates; AI and dashboards agree |
| 3 | Coverage & Representativeness Index | Prevents over-reading social data |
| 4 | Multilingual gold sets with agreement targets | Makes NLP accuracy measurable per language |
| 5 | Experiment & test registry | Turns content performance into valid learning |
| 6 | Silence-period & exit-poll calendar guard | Hard control on legally restricted windows |
| 7 | AI Content Provenance Ledger | Mirrors ECI record-keeping expectations for AI material |
| 8 | Official-boundary map rule | Avoids a common legal pitfall |
| 9 | Escalation matrix, SLAs, BCP runbooks | Poll-week resilience |
| 10 | Cost guardrails | Prevents API/LLM bill shock |
| 11 | AI red-team & hallucination harness | Evidence that the AI is safe to use |
| 12 | Exit & data-return plan | Client retains control of its data |
| 13 | Health-score "red domain cap" rule | Prevents good news hiding bad news |
| 14 | Late-report reconciliation for field data | Avoids false operational alarms |

\newpage

# Appendix A — Sources

*Retrieved/checked September 2026. Where the ECI primary document could not be retrieved directly, the reputable report of the ECI press note/advisory is cited and the item is marked [VERIFY] in the body. This appendix does not constitute legal advice.*

## A.1 Legal sources

| ID | Source | Date | Supports |
|---|---|---|---|
| L1 | ECI press note on regulation of political advertising & digital campaigning for 2026 Assembly elections — reported by ANI: https://www.aninews.in/news/national/general-news/eci-mandates-pre-certification-of-political-ads-on-social-electronic-media-ahead-of-elections20260320194334/ ; Akashvani (Prasar Bharati): https://www.newsonair.gov.in/ec-issues-order-to-regulate-political-advertisements-across-electronic-digital-media ; primary: https://www.eci.gov.in (press releases) | 20 Mar 2026 | MCMC pre-certification incl. social media; social-media account disclosure; 75-day expenditure statements incl. internet spend |
| L2 | ECI on pre-certification of political advertisements in print media — Akashvani: https://www.newsonair.gov.in/election-commission-mandates-pre-certification-of-political-advertisements-in-print-media | 6 Apr 2026 | Print-ad pre-certification |
| L3 | ECI advisory on labelling AI-generated/synthetic content — Business Today: https://www.businesstoday.in/india/story/eci-mandates-clear-labelling-of-ai-generated-content-in-political-campaigns-499535-2025-10-24 ; ANI: https://www.aninews.in/news/national/general-news/eci-issues-advisory-to-control-misuse-of-ai-generated-content-during-elections-urges-parties-to-report-fake-accounts-deepfakes20251025015121/ ; Akashvani: https://www.newsonair.gov.in/ec-issues-fresh-guidelines-on-ai-and-synthetic-content-use-in-bihar-poll-campaigns | 24–25 Oct 2025 | Label text, 10% area / first 10% audio, responsible-entity disclosure, records, 3-hour takedown |
| L4 | ECI advisory on labelling synthetic content — Akashvani: https://www.newsonair.gov.in/eci-directs-political-parties-to-label-ai-generated-synthetic-content-in-campaigns ; IndiaAI: https://indiaai.gov.in/article/election-commission-of-india-embraces-ai-ethics-in-campaigning-advisory-on-labelling-ai-generated-content | 16 Jan 2025 | Earlier AI-labelling advisory |
| L5 | ECI guidelines on responsible and ethical use of social media — DD India: https://ddindia.co.in/2024/05/eci-issues-guidelines-for-ethical-social-media-use-in-campaigns/ | 6 May 2024 | Deepfake prohibition; 3-hour removal |
| L6 | ECI reiteration for 2026 elections — SCC Online: https://www.scconline.com/blog/post/2026/04/21/eci-regulates-social-media-during-elections-2026/ ; MediaNama: https://www.medianama.com/2026/04/223-eci-orders-3-hour-takedown-rule-ai-fake-content-elections/ | Apr 2026 | 3-hour takedown; labels; enforcement statistics |
| L7 | ECI instructions on use of social media in election campaigning (25 Oct 2013) — ECI FAQ on Social Media: https://old.eci.gov.in/files/file/13753-faq-on-social-media/ ; Nyaaya explainer: https://nyaaya.org/legal-explainer/social-media-advertisements/ | 2013 (FAQ updated periodically) | MCC applies online; pre-certification; social-media expenditure |
| L8 | IT (Intermediary Guidelines and Digital Media Ethics Code) Amendment Rules, 2026 — Khaitan & Co: https://www.khaitanco.com/thought-leadership/MeitY-notifies-the-IT-Amendment-Rules-2026 ; Freshfields: https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/india-targets-deepfakes-and-ai-generated-content-key-changes-under-meitys-2026-102mjwn ; MeitY FAQ on SGI: https://www.meity.gov.in/static/uploads/2025/10/065b6deb585441b5ccdf8be42502a49c.pdf | Notified 10 Feb 2026; in force 20 Feb 2026 | SGI labelling; 3-hour intermediary takedown |
| L9 | Representation of the People Act, 1951 (ss. 77, 126, 126A) — India Code: https://www.indiacode.nic.in | As amended | Expenditure accounts; silence period; exit-poll restriction |
| L10 | Report of the Committee on Section 126 of the RP Act — ECI: https://eci.gov.in/files/file/9276-report-of-the-committee-on-section-126-of-the-representation-of-the-people-act-1951/ ; PIB: https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=187412 | Jan 2019 | Silence period and digital media; platform code of ethics (3-hour processing) |
| L11 | ECI press release — limits of candidates' expenses enhanced: https://old.eci.gov.in/files/file/13928-limits-of-candidate%E2%80%99s-expenses-enhanced/ | 6 Jan 2022 | ₹95/75 lakh (PC), ₹40/28 lakh (AC) |
| L12 | Digital Personal Data Protection Act, 2023 — MeitY: https://www.meity.gov.in/data-protection-framework | Aug 2023 | Data-protection obligations |
| L13 | DPDP Rules, 2025 — notified 14 Nov 2025; analysis: https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/ ; Rule 6 text: https://www.dpdpa.com/dpdparules/rule6.html | 14 Nov 2025 (phased to 14 May 2027) | Security safeguards, 1-year logs, breach reporting |
| L14 | CERT-In Directions under s.70B(6) IT Act — https://www.cert-in.org.in ; summary: https://www.internetsociety.org/resources/doc/2022/internet-impact-brief-india-cert-in-cybersecurity-directions-2022/ | 28 Apr 2022 (effective 28 Jun 2022) | 6-hour incident reporting; 180-day logs in India |
| L15 | India AI Governance Guidelines — PIB/MeitY: https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf | 5 Nov 2025 | Responsible-AI principles |
| L16 | Meta — Ads about Social Issues, Elections or Politics: https://transparency.meta.com/policies/ad-standards/SIEP-advertising/SIEP/ | Current (checked Sep 2026) | Authorisation and disclaimers |
| L17 | Google — Political content policy: https://support.google.com/adspolicy/answer/6014595 ; India election-ads pre-certificate requirements: https://support.google.com/adspolicy/contact/in_elections_pre_cert_requirements | Current (checked Sep 2026) | Verification; ECI pre-certificate per ad |
| L18 | ECI exit-poll prohibition for 2026 Assembly elections — Newsgram: https://www.newsgram.com/india/2026/04/08/ec-restricts-exit-polls-rpa-1951 | 8 Apr 2026 | Exit-poll window (9–29 Apr 2026) |

## A.2 Technical sources

| ID | Source | Date | Supports |
|---|---|---|---|
| T1 | Meta Graph API documentation: https://developers.facebook.com/docs/graph-api | Current | Page insights access model |
| T2 | Instagram Platform documentation: https://developers.facebook.com/docs/instagram-platform ; Basic Display EOL (4 Dec 2024) | Current | Business/Creator-only APIs |
| T3 | Meta Ad Library tools: https://transparency.meta.com/researchtools/ad-library-tools | Current | Ad Library API, verification |
| T4 | Meta Content Library announcement: https://about.fb.com/news/2023/11/new-tools-to-support-independent-research/ ; CrowdTangle shutdown: https://www.cjr.org/tow_center/meta-is-getting-rid-of-crowdtangle.php | Nov 2023; 14 Aug 2024 | Researcher-only access |
| T5 | YouTube Data API v3: https://developers.google.com/youtube/v3 ; YouTube Analytics API: https://developers.google.com/youtube/analytics | Current | Public metadata; owned-channel analytics |
| T6 | X API pay-per-use announcement: https://devcommunity.x.com/t/announcing-the-launch-of-x-api-pay-per-use-pricing/256476 | 2026 | Pricing model (budget caps) |
| T7 | Google Trends API (alpha): https://developers.google.com/search/blog/2025/07/trends-api | 24 Jul 2025 | Application-gated alpha |
| T8 | GA4 Data API: https://developers.google.com/analytics/devguides/reporting/data/v1 | Current | Website analytics |
| T9 | Google Ads API: https://developers.google.com/google-ads/api/docs/start | Current | Owned ad-account reporting |
| T10 | PostgreSQL: https://www.postgresql.org/docs/ ; pgvector: https://github.com/pgvector/pgvector | Current | Warehouse + vectors |
| T11 | FAISS: https://github.com/facebookresearch/faiss | Current | Vector similarity |
| T12 | dbt: https://docs.getdbt.com/ | Current | Transformations, tests, lineage |
| T13 | Dagster: https://docs.dagster.io/ ; Apache Airflow: https://airflow.apache.org/docs/ | Current | Orchestration |
| T14 | FastAPI: https://fastapi.tiangolo.com/ | Current | API layer |
| T15 | Sentence-Transformers: https://www.sbert.net/ | Current | Embeddings |
| T16 | Power BI row-level security: https://learn.microsoft.com/power-bi/enterprise/service-admin-rls | Current | RLS |
| T17 | OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/ | Current | App-security baseline |

## A.3 Data sources

| ID | Source | Date | Supports |
|---|---|---|---|
| D1 | ECI Statistical Reports: https://www.eci.gov.in/statistical-reports | Current | Historical results, turnout, electors |
| D2 | PIB — Index Cards and Statistical Reports published on ECINET: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2258991 | 2026 | 72-hour publication for 2026 Assembly elections |
| D3 | TCPD Lok Dhaba (Ashoka University): https://tcpd.ashoka.edu.in/lok-dhaba/ ; https://lokdhaba.ashoka.edu.in/ | Current | Cleaned historical results (licence to confirm) |
| D4 | Census 2027 — PIB document: https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/apr/doc2026425856601.pdf | 25 Apr 2026 | Census timeline |
| D5 | Open Government Data Platform: https://data.gov.in | Current | Public indicators |
| D6 | DataMeet community maps — Assembly Constituencies: https://projects.datameet.org/maps/assembly-constituencies/ | Current | Boundaries (CC BY 2.5 India; delimitation vintage caveats) |
| D7 | Survey of India: https://surveyofindia.gov.in | Current | Official boundaries |
| D8 | ECINET: https://ecinet.eci.gov.in | Current | ECI unified portal |

## A.4 AI/ML sources

| ID | Source | Supports |
|---|---|---|
| A1 | IndicTrans2 (AI4Bharat, MIT): https://github.com/AI4Bharat/IndicTrans2 | Translation, 22 scheduled languages |
| A2 | IndicBERT (AI4Bharat, MIT): https://huggingface.co/ai4bharat/indic-bert | Indic encoder |
| A3 | MuRIL (Google): https://huggingface.co/google/muril-base-cased | Indic + transliterated encoder (licence to confirm) |
| A4 | Indic NLP Catalog: https://ai4bharat.github.io/indicnlp_catalog/ | Resource discovery |
| A5 | NIST AI Risk Management Framework 1.0: https://www.nist.gov/itl/ai-risk-management-framework | AI risk governance |
| A6 | ISO/IEC 42001:2023: https://www.iso.org/standard/81230.html | AI management systems |
| A7 | Mitchell et al., "Model Cards for Model Reporting": https://arxiv.org/abs/1810.03993 | Model cards |
| A8 | Gebru et al., "Datasheets for Datasets": https://arxiv.org/abs/1803.09010 | Dataset documentation |
| A9 | Lewis et al., "Retrieval-Augmented Generation": https://arxiv.org/abs/2005.11401 | RAG |
| A10 | Grootendorst, "BERTopic": https://arxiv.org/abs/2203.05794 | Topic modelling |
| A11 | AAPOR Code of Professional Ethics and Practices: https://aapor.org/standards-and-ethics/ | Survey transparency |
| A12 | Kish, L. (1965). *Survey Sampling*. Wiley | Design effect, effective sample size |

## A.5 Design / visual sources

| ID | Source | Licence / consideration |
|---|---|---|
| V1 | Generated network cover and all charts (`demo/build_charts.py`) | Own work |
| V2 | NASA Earth Observatory — Night Lights: https://earthobservatory.nasa.gov/features/NightLights ; NASA media guidelines: https://www.nasa.gov/nasa-brand-center/images-and-media/ | Optional; verify per image |
| V3 | Unsplash License: https://unsplash.com/license | Optional photography |
| V4 | Pexels License: https://www.pexels.com/license/ | Optional photography |
| V5 | Google Material Symbols: https://fonts.google.com/icons | Apache 2.0 icons (optional) |
| V6 | Survey of India official maps: https://surveyofindia.gov.in | Required for India boundaries |

# Appendix B — Glossary

| Term | Meaning |
|---|---|
| AC / PC | Assembly Constituency / Parliamentary Constituency |
| MCC | Model Code of Conduct |
| MCMC | Media Certification and Monitoring Committee (district/state) |
| SGI | Synthetically generated information (IT Rules 2026) |
| DPDP | Digital Personal Data Protection Act 2023 / Rules 2025 |
| MoE | Margin of error |
| deff / n_eff | Design effect / effective sample size |
| MAD | Median absolute deviation (robust spread) |
| MAPE | Mean absolute percentage error |
| RAG | Retrieval-augmented generation |
| RLS / RBAC | Row-level security / role-based access control |
| RPO / RTO | Recovery point / time objective |
| ER / CTR / CPC / CPM | Engagement rate / click-through rate / cost per click / cost per thousand impressions |
| FCR | First-contact resolution |
