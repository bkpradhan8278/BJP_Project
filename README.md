# Election Intelligence & Analytics Command Center

**Proposal · PRD · Architecture · POC plan · Operating model · Commercials · Executive deck**
Prepared by [COMPANY NAME], an AI + Data + Digital Intelligence Partner, for the leadership of a political communications / PR agency. Version 1.0, 27 September 2026.

> **Not legal advice.** This is an analytics/technology proposal. The Campaign's authorised legal/compliance team should review final campaign compliance. Items marked **[VERIFY]** in the PRD come from reputable reporting of ECI press notes. They must be checked against the primary documents.
>
> **Ethical scope.** The platform works on lawful, privacy-aware, **aggregate** analytics and operational decision-support. It does not profile individuals' political beliefs. It does not do individualised persuasion, covert tracking or unauthorised scraping.
>
> **Demo data.** Every dashboard figure is **DEMO DATA, SYNTHETIC**. The figures come from a fictional constituency ("Aranyapur AC"). No party marks are used; logo boxes are placeholders.

## Deliverables

| Artefact | File |
|---|---|
| Executive presentation (35 slides, editable) | [`deliverables/Election_Intelligence_Command_Center_Executive_Deck.pptx`](deliverables/Election_Intelligence_Command_Center_Executive_Deck.pptx) |
| Executive presentation (PDF) | [`deliverables/Election_Intelligence_Command_Center_Executive_Deck.pdf`](deliverables/Election_Intelligence_Command_Center_Executive_Deck.pdf) |
| Detailed PRD / project proposal (58 pages, Word) | [`deliverables/Election_Intelligence_Command_Center_PRD.docx`](deliverables/Election_Intelligence_Command_Center_PRD.docx) |
| Detailed PRD / project proposal (PDF) | [`deliverables/Election_Intelligence_Command_Center_PRD.pdf`](deliverables/Election_Intelligence_Command_Center_PRD.pdf) |
| PRD (Markdown, readable on GitHub) | [`docs/PRD_Election_Intelligence_Command_Center.md`](docs/PRD_Election_Intelligence_Command_Center.md) |
| Conceptual database schema | [`poc/schema.sql`](poc/schema.sql) |
| Conceptual API (OpenAPI) | [`poc/openapi.yaml`](poc/openapi.yaml) |
| Synthetic demo data generator (100,000 records) | [`demo/generate_synthetic_data.py`](demo/generate_synthetic_data.py) |
| Demo analytics & charts | [`demo/build_charts.py`](demo/build_charts.py) → `demo/charts/` |

## Where to find each requested output

| # | Requested output | Location |
|---|---|---|
| 1 | Executive summary | PRD §1 · deck slides 2–6 |
| 2 | Complete PRD | PRD §1–§34 + Appendices |
| 3 | Presentation slide-by-slide content | Deck (35 slides, speaker notes included) · PRD §33 |
| 4 | Architecture diagrams | PRD §2.4, §11, §12, §15.2, §25.3 · deck slides 5, 9, 10, 19, 28 |
| 5 | Team structure | PRD §24 · deck slides 25–26 |
| 6 | Budget framework | PRD §28 · deck slide 30 |
| 7 | POC plan | PRD §25 · deck slides 27–28 |
| 8 | KPI framework | PRD §20, §27 · deck slide 31 |
| 9 | Risk register | PRD §30 · deck slide 32 |
| 10 | Source list | PRD Appendix A (legal / technical / data / AI-ML / design) · deck slide 35 |
| 11 | Capabilities added after self-review | PRD §1.8, §34.3 |

## Executive summary (short)

- **Product.** The Command Center is a single governed intelligence layer over public, consented and authorised campaign data: digital, social, media, survey, field, call-centre and compliance. It adds statistics, multilingual NLP, forecasting with uncertainty, an alert engine and a grounded AI Analyst that answers with citations. It also includes an Election Compliance Control Tower covering approvals, MCMC certification references, AI-content labels, spend and the audit trail.
- **Why now.** Several 2025–26 rules shape digital campaigning:
  - ECI requirements (20 Mar 2026): MCMC pre-certification of political ads, including on social media, and full reporting of internet spend.
  - ECI AI-labelling advisory (24 Oct 2025): AI-generated campaign content must be labelled and records kept, with 3-hour takedowns.
  - IT Amendment Rules 2026 on synthetically generated information.
  - DPDP Rules 2025, phased in through 14 May 2027.

  Together these make speed and auditability non-negotiable.
- **Positioning.** *"We do not simply provide analysts. We build the intelligence infrastructure that turns fragmented campaign data into a continuously learning decision-support system."*
- **Ask.** A 4–6 week POC with 13 measurable acceptance criteria (indicative ₹18–35 lakh), then Starter, Professional or Enterprise tiers. All commercials are indicative.
- **Boundaries.** We do not guarantee an election outcome, predict votes exactly, infer individual beliefs, access unauthorised data, track anyone secretly or guarantee ROI.

## Red-team summary

The full review is in PRD §34. The main findings, and what was changed in response:

- **Technical feasibility.** API access is paid, restricted or closed on several platforms, so each is tagged for verification in Week 1. Fallback routes and licensed vendors are defined.
- **Legal and compliance.** Secondary-source ECI items are marked [VERIFY]. The POC starts with a legal sign-off gate. A silence-period and exit-poll calendar guard is included. Brand marks and India boundaries are only used with authorisation or official sources.
- **Privacy.** Data is minimised, identifiers are pseudonymised and permitted-use tags are enforced at query time. No caller PII is kept. "Amplification" analysis is limited to public figures and media.
- **AI hallucination.** The AI Analyst answers through tools first. Numeric and citation checks run on every answer, citations are generated by the system, and a red-team evaluation harness gates acceptance (AC-07, AC-08).
- **Unrealistic claims.** The Health Score is defined as operational only. The synthetic model metrics are flagged as better than real-world performance would be.
- **Gaps closed.** Added annotators and 24×7 data-ops roles; added costs for listening and media licences, X API credits and pen-testing; added dependencies for the legal contact, brand authorisation and annotators.

## Rebuild

```bash
pip install python-pptx python-docx pypandoc_binary matplotlib pandas numpy
python demo/generate_synthetic_data.py      # 100,000 synthetic records -> demo/data (git-ignored)
python demo/build_charts.py                 # charts + metrics.json -> demo/charts
python tools/build_deck.py                  # -> deliverables/*.pptx
tools/render_deck.sh                        # -> deck PDF + slide PNGs (needs LibreOffice Impress, poppler)
python tools/build_prd.py                   # -> docs/PRD_*.md, deliverables/*_PRD.docx/.pdf
```

The PRD source sections live in `docs/prd/`. Edit them there and rebuild.
