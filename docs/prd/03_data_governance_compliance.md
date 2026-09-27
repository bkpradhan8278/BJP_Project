\newpage

# 8. Full Data Ecosystem

**Principle:** a source enters the platform only after it is registered with an owner, a lawful basis/authorisation, permitted purposes and a retention rule (§9). **API availability and permitted fields must be verified against the current platform documentation and access level** — no connector is assumed to exist.

## 8.1 A. Official / public data

| Source | Typical content | Access pattern | Notes / caveats |
|---|---|---|---|
| Election Commission of India — Statistical Reports & Index Cards (eci.gov.in/statistical-reports; ECINET app) | AC/PC-wise electors, polling stations, turnout, gender-wise participation, party vote share, constituency-wise detailed results | Download (PDF/XLS) → parsed & validated | For 2026 Assembly elections ECI published index cards/statistical reports within 72 hours of results (PIB, 2026). Use official files as the system of record |
| Historical results — curated research datasets (e.g., TCPD Lok Dhaba, Ashoka University) | Cleaned constituency/candidate results from 1962 | Download; **licence/terms to be confirmed** | Reconcile against ECI originals; record dataset version |
| Candidate affidavits / disclosures (public) | Assets, liabilities, education, cases as disclosed | Public ECI portals; manual/structured extraction | Use only as publicly disclosed; no enrichment with private data |
| Census of India & official statistics | Population, households, amenities (Census 2011); Census 2027 in progress — house-listing Apr–Sep 2026, population enumeration reference date 1 Mar 2027 | Download | Census 2011 is dated; plan to update when Census 2027 releases become available |
| Government reports & development indicators (data.gov.in, NFHS, PLFS, UDISE+, state dashboards) | Health, education, employment, infrastructure indicators | Download / OGD APIs where available | Aggregate only; note survey years and geographic resolution |
| Constituency / district boundaries | AC/PC/district geometry | Official sources preferred; community datasets (e.g., DataMeet, CC BY 2.5 India) for analysis with attribution | Some community AC boundaries pre-date delimitation — verify; official India outline required for national maps |

## 8.2 B. Campaign-owned data (only where lawfully obtained and authorised)

| Source | Examples | Controls |
|---|---|---|
| Website analytics | GA4 or equivalent: sessions, sources, landing pages, events | Consent banner/cookie policy; IP anonymisation; no PII in events |
| Social-media analytics (owned accounts) | Page/channel insights | Admin-authorised tokens; permitted fields only |
| Ad-platform reporting | Spend, impressions, reach, clicks, CPM/CPC | Platform policy compliance; MCMC certification reference captured per ad |
| CRM records | Volunteers, supporters who opted in, event registrations | DPDP-aligned notice and consent; purpose-bound; pseudonymised in analytics |
| Event records | Event type, location, time, estimated attendance | Aggregate; no facial recognition |
| Volunteer operations data | Tasks, assignments, completion | Operational only; access by role |
| Campaign activity data | Planned vs completed activities | Operational |
| Call-centre operational data | Volumes, wait times, categories, resolution | No recordings/transcripts unless lawfully authorised and disclosed; PII minimised |
| Survey data | See C | Consent recorded; microdata pseudonymised |
| Feedback forms | Event/website feedback | Consent; free text PII-scrubbed |

## 8.3 C. Survey data

Types: opinion surveys (issue and attitude, **aggregate reporting only**), issue surveys, awareness surveys, satisfaction surveys, event feedback, campaign feedback.

| Concept | What it means | How the platform handles it |
|---|---|---|
| **Sampling** | How respondents are selected (probability: SRS, stratified, cluster/multi-stage; non-probability: quota, online panel) | Sampling design stored as metadata; non-probability samples flagged with caveats |
| **Sample size** | Number of completed interviews; drives precision | Calculator: n = z²·p(1−p)/e² × deff; e.g., ±3 pts at 95% with p=0.5 and deff=1.5 → ≈1,600 completes |
| **Weighting** | Adjusting sample to known population margins (age, gender, area type, region) | Post-stratification or raking (iterative proportional fitting); weight trimming; weights versioned |
| **Confidence interval** | Range likely to contain the population value (e.g., 95%) | Shown on every estimate |
| **Margin of error** | Half-width of the CI; increases with weighting (design effect) | MoE uses effective sample size (Kish: n_eff = (Σw)²/Σw²) |
| **Non-response bias** | Those who don't respond differ from those who do | Response-rate tracking; comparison to benchmarks; weighting |
| **Response bias** | Social desirability, acquiescence, question-order, interviewer effects | Questionnaire review; interviewer-level QC; mode comparison |
| **Questionnaire design** | Neutral wording, balanced scales, order rotation, pre-testing | Design checklist; cognitive pre-test; translation back-check |
| **Quality control** | Speeders, straight-liners, duplicates, GPS/time anomalies (for tablet F2F), back-checks | Automated flags; exclusion rules documented per wave |

## 8.4 D. Digital data — API reality check

> **For every platform: API availability and permitted fields must be verified against the current platform documentation and access level.** The table records what public documentation indicated as of September 2026; it is a starting point for the discovery phase, not a guarantee.

| Platform | Likely access route | Observations (verify) |
|---|---|---|
| Meta — Facebook Pages | Graph API page insights (page admin token); Business Suite exports | Access limited to owned/authorised assets; permissions require app review |
| Meta — Instagram | Instagram Graph API / "Instagram API with Instagram Login" for Business/Creator accounts | Instagram Basic Display API reached end-of-life on 4 Dec 2024; personal accounts not supported |
| Meta — Ads | Marketing API insights for authorised ad accounts; **Ad Library** (and Ad Library API) for public transparency on ads about social issues, elections or politics | Ad Library API requires identity/country verification. Political advertisers must complete Meta's authorisation and disclaimer process |
| Meta — public content research | Meta Content Library & API | Restricted to eligible academic/non-profit researchers (via ICPSR); CrowdTangle was shut down on 14 Aug 2024. **Not a general campaign listening tool** |
| YouTube | YouTube Data API v3 (public metadata), YouTube Analytics / Reporting API (owned channels) | Quotas apply; owned-channel analytics require channel authorisation |
| X (Twitter) | X API | Since Feb 2026 new developers default to pay-per-use credits; legacy Basic/Pro tiers being migrated (reported Aug 2026). **Budget and read caps must be confirmed** |
| Google Search / Ads | Google Ads API for owned accounts; Google Ads Transparency Center | Google requires India election-ad advertiser verification and an ECI/authorised **pre-certificate for each election ad** |
| Google Trends | Web interface; official **Trends API is an application-gated alpha** (announced 24 Jul 2025) | Do not assume access; treat Trends as indicative only |
| Website analytics | GA4 Data API / exports; Search Console API | Owned properties only |
| Listening vendors | Licensed social-listening tools | Vendor must document lawful data sourcing and platform compliance; contract includes audit rights |

## 8.5 E. Media data

| Source | Access | Notes |
|---|---|---|
| News websites & RSS | Public feeds; licensed aggregators | Respect robots.txt and terms; store headline, URL, snippet, metadata; full text only if licensed |
| Public news feeds / wire | Licensed | Contracted terms |
| TV / broadcast | Licensed monitoring vendor transcripts/clips | **Only where licensed**; no unlicensed recording/redistribution |
| Public YouTube news content | YouTube Data API (metadata, public captions where permitted) | Quotas; ToS |
| Search trends | Google Trends (web/alpha API) where legally available | Relative index, not volume |
| Regional & hyperlocal media | Licensed vendors / public feeds | Priority for Indian-language coverage |

## 8.6 F. Field data

Daily field reports (structured mobile forms), event attendance (headcount estimates, not identities), campaign activity completion, local issue reports (categorised), operational status, geographic coverage (zone-level), volunteer activity metrics (counts, completion, timeliness). Collected via a structured form app (e.g., ODK/KoboToolbox-class tool or the campaign's own app) with validation, offline support and geotag at *site* level only where operationally necessary and disclosed.

# 9. Data Governance Framework

## 9.1 Governance model

| Element | Design |
|---|---|
| **Data ownership** | Campaign/Agency is the data owner (and, under DPDP, the Data Fiduciary for personal data it determines purposes for); the Intelligence Partner acts as **Data Processor** under a Data Processing Agreement. Each source has a named business owner and technical steward |
| **Source Registry** | Mandatory record per source: ID, owner, description, lawful basis/authorisation evidence, permitted purposes, sensitivity class, fields collected, refresh cadence, retention, deletion method, contract/licence ref, API credential ref |
| **Permitted-use tags (added)** | Each dataset carries purpose tags (e.g., `ops_analytics`, `media_monitoring`, `survey_aggregate`). Queries/AI tools check tags at run-time; a request outside permitted purposes is refused and logged |
| **Data dictionary** | Business definition, type, allowed values, owner, sensitivity per field; published in the catalogue |
| **Metadata & lineage** | Technical metadata and column-level lineage captured by the orchestration/transform layer (dbt docs / OpenLineage-compatible) |
| **Access controls** | RBAC via SSO groups; row-level security by geography/team; column masking for sensitive fields; just-in-time elevated access with approval |
| **Encryption** | TLS in transit; KMS-managed keys at rest; field-level encryption for any personal identifiers retained |
| **Audit logs** | Immutable, append-only logs of logins, queries on sensitive tables, exports, AI prompts/answers, approvals; retained ≥ 1 year (DPDP Rules, Rule 6) and ≥ 180 days in India (CERT-In) — whichever is longer |
| **Retention policy** | Per source; default: raw social/media 12 months, survey microdata 24 months (pseudonymised), operational logs 13 months, compliance records per legal advice (election-related records typically retained until expiry of election-petition limitation and any litigation) **[VERIFY with legal]** |
| **Deletion policy** | Automated purges on expiry; verified deletion from backups on rotation; deletion certificates at contract end |
| **Consent/authorisation tracking** | Consent artefacts (notice version, timestamp, channel, purpose) stored for first-party personal data; authorisation letters for platform accounts; licences for media feeds |
| **Data minimisation** | Collect only fields needed; drop handles/IDs from public social data after de-duplication unless required and permitted; aggregate early |
| **Purpose limitation** | Enforced through permitted-use tags and RBAC; new purposes require governance approval |
| **Data-quality monitoring** | Tests on freshness, volume, schema, nulls, ranges, duplicates; quality score per source on every dashboard |
| **Incident response** | Runbook: detect → triage → contain → notify (CERT-In within 6 hours for reportable incidents; DPDP Board/affected principals per Rule 7 timelines once in force) → recover → post-mortem |
| **Backup/recovery** | Daily snapshots + point-in-time recovery for warehouse and app DB; quarterly restore tests |
| **Vendor governance** | Due diligence for listening/media/survey/cloud/LLM vendors: data sourcing, security certifications, sub-processors, residency, DPA, audit rights, exit terms |
| **API credential management** | Service accounts per connector; secrets in vault; least-privilege scopes; rotation ≤ 90 days; revocation on staff exit |
| **Exit & data return (added)** | At contract end: full export in open formats, documentation, and deletion certificate |

## 9.2 Data Governance Checklist

| # | Control | Evidence | Owner | POC | Prod |
|---|---|---|---|---|---|
| 1 | Every source registered with owner and lawful basis | Source Registry entry | Data Steward | ✓ | ✓ |
| 2 | Authorisation evidence for each platform account/API | Signed authorisation / admin grant | Client + Partner | ✓ | ✓ |
| 3 | Licence terms captured for media/listening/survey vendors | Contract ref | Procurement | ✓ | ✓ |
| 4 | Permitted-use tags assigned per dataset | Catalogue | Data Steward | ✓ | ✓ |
| 5 | Data dictionary published for all modelled tables | dbt docs / catalogue | Analytics Lead | ✓ | ✓ |
| 6 | PII inventory and minimisation review | PII register | Privacy Lead | ✓ | ✓ |
| 7 | Consent notices reviewed (DPDP-aligned) for first-party collection | Notice versions | Legal | — | ✓ |
| 8 | RBAC matrix approved | Access matrix | Security Lead | ✓ | ✓ |
| 9 | SSO + MFA enforced | IdP config | Security Lead | ✓ | ✓ |
| 10 | Encryption at rest and in transit verified | Config evidence | DevOps | ✓ | ✓ |
| 11 | Secrets in vault; no credentials in code or chat | Scan report | DevOps | ✓ | ✓ |
| 12 | Audit logging enabled and tamper-evident | Log config | Security Lead | ✓ | ✓ |
| 13 | Retention and deletion schedules configured | Policy + jobs | Data Steward | ✓ | ✓ |
| 14 | Data-quality tests on every source | Test report | Data Engineer | ✓ | ✓ |
| 15 | Lineage available source → tile | Lineage graph | Data Engineer | Partial | ✓ |
| 16 | Incident response runbook tested | Tabletop record | Security Lead | — | ✓ |
| 17 | Backup restore tested | Restore log | DevOps | — | ✓ |
| 18 | Vendor due diligence completed | DD checklist | Procurement | Partial | ✓ |
| 19 | Model cards for every production model | Model registry | DS Lead | ✓ | ✓ |
| 20 | Quarterly access review | Review record | Security Lead | — | ✓ |
| 21 | Exit/data-return plan agreed | Contract schedule | Programme Director | ✓ | ✓ |

## 9.3 DPDP readiness note

The DPDP Rules 2025 were notified on 14 November 2025 with staggered commencement (immediate for administrative provisions including the Data Protection Board; further provisions from 14 November 2026 and 14 May 2027). Rule 6 (reasonable security safeguards, including log retention of at least one year) and Rule 7 (breach intimation, with a detailed report to the Board within 72 hours) are among the operational obligations. **Our design builds to the fully-in-force standard now**, so the platform does not need re-engineering as commencement dates arrive. Exact applicability of each rule to the Campaign on a given date is a legal determination **[VERIFY with legal]**.

# 10. Election Compliance

> **This is an analytics/technology proposal, not legal advice. Final campaign compliance should be reviewed by the Campaign's authorised legal/compliance team.** The summary below reflects public sources as of September 2026; primary ECI documents were not directly retrievable from our research environment in every case, so items drawn from reputable secondary reporting of ECI press notes are marked **[VERIFY]**.

## 10.1 Regulatory anchors relevant to the platform

| Area | What the source says (summary) | Platform implication | Source (Appendix A) |
|---|---|---|---|
| **Model Code of Conduct (MCC) & social media** | ECI's 25 Oct 2013 instructions apply the MCC to content posted on the internet/social media by candidates and parties, require pre-certification of political ads on internet-based media, and require inclusion of social-media campaign expenditure (ad payments, content development, staff operating accounts) in expenditure statements | Compliance tower tracks content approvals, certification, and full digital spend categories | L7 |
| **Pre-certification of political ads (2026)** | ECI press note of 20 Mar 2026 (for Assam, Kerala, Puducherry, Tamil Nadu, West Bengal and bye-elections) required parties, candidates and associated organisations to obtain **MCMC pre-certification** for political ads on electronic media including social media/internet platforms, bulk SMS/voice; candidates to disclose authentic social-media accounts; parties to file expenditure statements within 75 days incl. internet/social-media spend **[VERIFY]** | Certification reference is a **mandatory field** before a paid item can be marked "ready"; alert on missing ref | L1 |
| **Print ad pre-certification** | ECI (6 Apr 2026) reiterated pre-certification of political advertisements in print media in the pre-poll window **[VERIFY exact window]** | Calendar-aware rule in compliance tower | L2 |
| **AI-generated / synthetic content** | ECI advisory of 24 Oct 2025: synthetically generated or AI-altered image/audio/video used for campaigning must be labelled ("AI-Generated", "Digitally Enhanced" or "Synthetic Content") covering ≥10% of visible area (audio: during first 10% of duration); disclose the responsible entity in metadata or caption; no content misrepresenting identity/appearance/voice without consent; takedown within 3 hours of notice; **maintain internal records** of AI-generated material (creator, timestamp) **[VERIFY]**. Earlier advisories: 6 May 2024 (deepfakes, 3-hour removal), 16 Jan 2025 (labelling). ECI reiterated in April 2026 | **AI Content Provenance Ledger**; label-status field; takedown SLA timer; audit trail | L3–L6 |
| **IT Rules — synthetic information** | MeitY IT (Intermediary Guidelines and Digital Media Ethics Code) Amendment Rules 2026, notified 10 Feb 2026, in force 20 Feb 2026: due-diligence obligations for synthetically generated information (SGI), clear/prominent labelling, metadata/identifiers where feasible, 3-hour takedown for intermediaries on valid notice | Platform's own publishing partners (intermediaries) will enforce; campaign content must be labelled consistently | L8 |
| **Silence period** | RP Act 1951 s.126: no display of election matter by television or similar apparatus in the polling area during the 48 hours ending with the close of poll; ECI applies it across media; platforms process s.126 violation reports within 3 hours under the 2019 Voluntary Code of Ethics | **Silence-period calendar guard**: blocks scheduled publishing workflows and flags any paid/boosted items still running; internal analytics continue | L9, L10 |
| **Exit polls** | RP Act s.126A: no conducting/publishing exit polls during the ECI-notified window (from start of first phase to 30 minutes after close of last phase); s.126(1)(b) also covers opinion-poll display in the 48-hour window | Platform does **not** conduct exit polls; survey outputs are internal; restricted report types disabled in notified windows | L9 |
| **Expenditure** | Candidate expenditure limits (notified Jan 2022): ₹95 lakh (PC, larger states) / ₹75 lakh (smaller states); ₹40 lakh (AC, larger states) / ₹28 lakh (smaller states) **[VERIFY current limits]**; digital spend must be reported | Spend tracker by category with configurable limits and threshold alerts; reconciliation with finance | L11 |
| **Platform policies** | Meta requires authorisation + "Paid for by" disclaimers for ads about social issues, elections or politics; Google requires India election-ads verification and an ECI/authorised pre-certificate per ad | Platform-policy checklist per ad; transparency-library reconciliation | L16, L17 |
| **Data protection** | DPDP Act 2023 + DPDP Rules 2025 (phased) | §9 governance; consent tracking; breach runbook | L12, L13 |
| **Cyber incident reporting** | CERT-In Directions (28 Apr 2022): report specified incidents within 6 hours; maintain ICT logs 180 days in India | Security runbook; log residency | L14 |
| **Misinformation / disinformation** | ECI works with State IT Nodal Officers and platforms; April 2026 reporting cited >11,000 violative posts actioned since 15 Mar 2026 **[VERIFY]** | Misinformation-*risk* flags → human verification → escalation to legal/comms; platform never auto-declares content "fake" | L6 |

## 10.2 Election Compliance Control Tower

**Purpose:** give the Compliance Officer and Agency leadership one auditable view of every regulated item — and make non-compliance visible *before* it happens.

**Tracked object model:** `content_item` → `approval` → `certification` → `ai_provenance` → `publication` → `spend` → `takedown_event`, each with owner, timestamp and immutable audit entries.

| Field | Description | Example (DEMO) |
|---|---|---|
| Content ID | Unique ID for creative/ad/post | CT-0417 |
| Type | Organic post / paid ad / bulk SMS / print / AV | Paid ad — video |
| Content approval status | Draft → Legal review → Approved / Rejected | Approved |
| Approval owner | Named approver | Compliance Officer (Agency) |
| Approval timestamp | IST | 2026-09-12 16:42 |
| Advertisement certification status | Not required / Applied / Certified / Rejected; MCMC reference | Certified — MCMC-DEMO-0417 |
| Platform policy status | Disclaimer/authorisation done per platform | Meta ✓ / Google ✓ |
| Spend tracking | Committed / delivered spend; category | ₹1.8 lakh committed |
| AI-content disclosure/label status | Not AI / AI-assisted (non-deceptive edit) / AI-generated — label applied ✓/✗; label text; responsible-entity disclosure | AI-generated — label ✓ "Synthetic Content", entity in caption ✓ |
| AI provenance | Tool, creator, timestamp, source assets, consent for likeness | Tool X; creator ID; consent ref |
| Compliance alerts | Missing certification, label missing, silence-period conflict, spend threshold | None |
| Takedown events | Notice time, action time, SLA (3 h) | — |
| Audit trail | Every state change, who/when/why | 7 events |

**Rules engine (examples, configurable by legal):**

- `PAID_ITEM_WITHOUT_CERT_REF` → **Critical**: block "ready to publish" status.
- `AI_FLAG = true AND label_applied = false` → **Critical**.
- `scheduled_publish_time IN silence_window(constituency)` → **Critical**: block and notify.
- `spend_to_date / configured_limit > 0.8` → **High**; > 0.95 → **Critical**.
- `takedown_notice_received AND elapsed > 2h AND not actioned` → **Critical** (before 3-hour limit).
- `approval_age > 7 days AND not published` → **Low** (re-review stale approvals).

**Approval workflow:**

```
 Creator ──► Content owner review ──► Compliance/legal review ──► Certification (MCMC, if paid/electronic)
      │                                                               │
      └──── AI provenance record (if AI used) ────────────────────────┤
                                                                      ▼
                                          Platform policy checks ──► Scheduled ──► Published ──► Monitored
                                                                                       │
                                                               Takedown notice ◄───────┘ (3-hour SLA timer)
```

The tower **supports** the compliance team; it does not make legal determinations and does not replace the Campaign's statutory filings.
