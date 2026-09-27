"""
Builds the executive presentation:
  deliverables/Election_Intelligence_Command_Center_Executive_Deck.pptx
Run from the repo root after demo/generate_synthetic_data.py and demo/build_charts.py.
"""
from __future__ import annotations

import json
import os
import sys

from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.oxml.ns import qn
from lxml import etree

sys.path.insert(0, os.path.dirname(__file__))
from deck_helpers import *  # noqa: E402,F401,F403

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "demo", "charts")
OUT = os.path.join(ROOT, "deliverables")
os.makedirs(OUT, exist_ok=True)
M = json.load(open(os.path.join(CH, "metrics.json")))

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(W), Inches(H)
BLANK = prs.slide_layouts[6]
FOOT = "[COMPANY NAME]  ·  Election Intelligence & Analytics Command Center  ·  Confidential — for discussion"
state = {"n": 0}


def chart_img(name):
    return os.path.join(CH, name)


def base(dark=False):
    s = prs.slides.add_slide(BLANK)
    state["n"] += 1
    bg = s.background.fill
    bg.solid()
    bg.fore_color.rgb = rgb(NAVY if dark else WHITE)
    return s


def frame(kicker, title, subtitle=None, demo=False):
    s = base()
    circle(s, MX, 0.47, 0.13, fill=SAFFRON)
    text(s, MX + 0.22, 0.36, 8.0, 0.32, kicker.upper(), size=10.5, color=SAFFRON, bold=True)
    tw = 11.0 if demo else 12.1
    tsize = next((z for z in (28, 24, 22, 20) if len(title) * 0.0078 * z <= tw), 20)
    text(s, MX, 0.64, tw, 0.62, title, size=tsize, color=NAVY, bold=True)
    if subtitle:
        text(s, MX, 1.26, 12.1, 0.4, subtitle, size=14, color=MUTED)
    if demo:
        pill(s, W - MX - 2.35, 0.4, 2.35, "DEMO DATA — SYNTHETIC", size=9.5)
    text(s, MX, 7.08, 9.0, 0.25, FOOT, size=8.5, color=MUTED)
    text(s, W - MX - 0.6, 7.08, 0.6, 0.25, str(state["n"]), size=8.5, color=MUTED, align="r")
    return s


def veil(s, x, y, w, h, alpha=78000):
    r = rect(s, x, y, w, h, fill=NAVY)
    clr = r.fill._xPr.find(qn("a:solidFill")).find(qn("a:srgbClr"))
    a = etree.SubElement(clr, qn("a:alpha"))
    a.set("val", str(alpha))
    return r


def notes(s, t):
    s.notes_slide.notes_text_frame.text = t


def kpi_card(s, x, y, w, h, value, label, delta=None, delta_color=MUTED, fill=SURFACE, vsize=24):
    box(s, x, y, w, h, fill=fill)
    text(s, x + 0.15, y + 0.1, w - 0.3, 0.5, value, size=vsize, color=NAVY, bold=True)
    text(s, x + 0.15, y + 0.1 + vsize / 72 * 1.25, w - 0.3, h - 0.6, label, size=10.5, color=MUTED)
    if delta:
        text(s, x + 0.15, y + h - 0.34, w - 0.3, 0.28, delta, size=10, color=delta_color, bold=True)


def card(s, x, y, w, h, title, lines, badge=None, badge_fill=SAFFRON, fill=SURFACE, tsize=14, bsize=11.5):
    box(s, x, y, w, h, fill=fill)
    tx = x + 0.2
    if badge is not None:
        circle(s, x + 0.2, y + 0.2, 0.42, fill=badge_fill, label=badge, size=12)
        tx = x + 0.75
    text(s, tx, y + 0.2, w - (tx - x) - 0.15, 0.45, title, size=tsize, color=NAVY, bold=True, anchor="m")
    paras = [{"t": l, "bullet": True, "size": bsize} for l in lines]
    text(s, x + 0.2, y + 0.75, w - 0.35, h - 0.85, paras, size=bsize, color=INK, spacing_after=3)


# ================================================================== 1. COVER
s = base(dark=True)
image(s, chart_img("cover_network.png"), 0, 0, w=W, h=H)
veil(s, 0, 0, 8.4, H)
text(s, MX, 1.2, 7.4, 0.4, "PROPOSAL · PRD · POC PLAN", size=12, color=GOLD, bold=True)
text(s, MX, 1.7, 7.6, 2.0, "Election Intelligence & Analytics Command Center", size=40, color=WHITE, bold=True,
     line_spacing=0.95)
text(s, MX, 3.75, 7.2, 0.9, "Unified data. Trusted analytics. AI-assisted intelligence. Faster decisions.",
     size=18, color="F28C28")
text(s, MX, 4.75, 7.2, 0.9, [
    {"t": "Prepared for the leadership of [AGENCY NAME]", "size": 13, "color": "C9D3E3"},
    {"t": "by [COMPANY NAME] — AI + Data + Digital Intelligence Partner", "size": 13, "color": "C9D3E3"},
    {"t": "September 2026  ·  Confidential  ·  For initial approval discussion", "size": 11, "color": "8FA3C0"},
])
b = box(s, MX, 6.15, 3.1, 0.7, fill=None, line="8FA3C0", dash=True)
shape_text(b, "[Client logo placeholder — official assets only with authorisation]", size=8.5, color="C9D3E3")
b = box(s, MX + 3.3, 6.15, 1.9, 0.7, fill=None, line="8FA3C0", dash=True)
shape_text(b, "[COMPANY LOGO]", size=9, color="C9D3E3")
notes(s, "Position the partner as an intelligence-infrastructure partner, not a staffing vendor. All figures in the deck "
         "marked DEMO DATA are synthetic, for a fictional constituency. No party marks are used; placeholders only.")

# ================================================================== 2. EXECUTIVE VISION
s = frame("Executive vision", "From fragmented data to a continuously learning intelligence loop",
          "Understand what is changing, where, why it may be changing — and how operations are performing")
steps = [("Data", "Governed, registered, quality-scored sources"),
         ("Intelligence", "Statistics, forecasting, anomaly detection, multilingual NLP"),
         ("Insight", "What changed, where, plausible why — facts vs interpretation"),
         ("Decision support", "Prioritised operational & monitoring follow-ups; humans decide"),
         ("Measurement", "Every action has a KPI and a baseline"),
         ("Learning loop", "Results recalibrate models, KPIs and playbooks")]
cols = [NAVY, NAVY2, BLUE, TEAL, OCHRE, SAFFRON]
for i, (t, d) in enumerate(steps):
    x = MX + i * 2.03
    c = shape(s, MSO_SHAPE.CHEVRON if i else MSO_SHAPE.PENTAGON, x, 2.05, 2.1, 0.95, fill=cols[i])
    shape_text(c, t, size=12, color=WHITE, bold=True, margin=0.02)
    text(s, x + 0.1, 3.18, 1.85, 1.2, d, size=12, color=INK)
lp = shape(s, MSO_SHAPE.LEFT_ARROW, MX + 0.3, 4.45, 11.7, 0.5, fill=SAFFRON_LT)
shape_text(lp, "Learning loop: measured outcomes feed back into data, models and KPIs every week", size=12,
           color=SAFFRON, bold=True)
for i, (h_, d) in enumerate([("AI on a trusted data layer", "LLMs answer only from verified, lineage-tracked data — with citations"),
                              ("Humans stay in charge", "Analysts interpret; leadership decides; AI drafts and flags"),
                              ("Every number is traceable", "Source, timestamp, quality and uncertainty on every tile")]):
    x = MX + i * 4.1
    box(s, x, 5.3, 3.9, 1.45, fill=SURFACE)
    text(s, x + 0.2, 5.42, 3.5, 0.4, h_, size=14, color=NAVY, bold=True)
    text(s, x + 0.2, 5.85, 3.5, 0.85, d, size=12, color=MUTED)
notes(s, "Core proposition: convert fragmented campaign, digital, survey, media, field and public data into a single "
         "intelligence layer. The loop is the product: data to decision support to measurement to learning.")

# ================================================================== 3. WHY IT MATTERS
s = frame("Why campaign intelligence matters now", "2026 campaigns need speed — and an audit trail")
stats = [("20 Mar 2026", "ECI: political ads on electronic media incl. social media need MCMC pre-certification; internet spend must be reported"),
         ("≥ 10%", "ECI advisory (24 Oct 2025): AI/synthetic campaign content labelled on ≥10% of display; records of AI material kept"),
         ("3 hours", "Removal window for deepfake / unlawful content (ECI advisories; IT Amendment Rules 2026 for intermediaries)"),
         ("14 May 2027", "DPDP Rules 2025 fully in force — privacy-by-design, security safeguards and 1-year logs")]
for i, (v, l) in enumerate(stats):
    x = MX + (i % 2) * 3.95
    y = 1.85 + (i // 2) * 2.45
    box(s, x, y, 3.75, 2.25, fill=SURFACE)
    text(s, x + 0.25, y + 0.2, 3.3, 0.7, v, size=30, color=SAFFRON, bold=True)
    text(s, x + 0.25, y + 0.95, 3.3, 1.25, l, size=12, color=INK)
text(s, 8.7, 1.9, 4.0, 0.45, "What this means for leadership", size=16, color=NAVY, bold=True)
text(s, 8.7, 2.45, 4.0, 3.6, [
    {"t": "Decisions must move faster than the news cycle — hours, not days", "bullet": True},
    {"t": "Every paid or AI-assisted item needs approval, certification and label records", "bullet": True},
    {"t": "Teams must work from one set of defensible numbers", "bullet": True},
    {"t": "AI is useful only on top of verified, governed data", "bullet": True},
    {"t": "Human judgement remains essential — the system supports it", "bullet": True},
], size=13, spacing_after=10)
text(s, MX, 6.72, 12.1, 0.3, "Sources: ECI press notes/advisories as reported (Appendix L1, L3, L6); MeitY IT Amendment Rules 2026 (L8); "
     "DPDP Rules 2025 (L13). Not legal advice — verify against primary documents.", size=9, color=MUTED, italic=True)
notes(s, "Regulatory context summarised from public reporting of ECI press notes and MeitY notifications. The compliance "
         "team must confirm against primary documents.")

# ================================================================== 4. CURRENT PROBLEM
s = frame("The current problem", "Fragmented workflows create blind spots at the worst possible time")
srcs = [("Meta / YouTube / X dashboards", "screenshots"), ("Ad-platform exports", "CSV"), ("Survey vendor", "PDF toplines"),
        ("Media cell", "WhatsApp clips"), ("Field coordinators", "photos / voice notes"), ("Call-centre tool", "exports"),
        ("Public election data", "ad-hoc downloads")]
for i, (a, b_) in enumerate(srcs):
    y = 1.85 + i * 0.68
    bx = box(s, MX, y, 2.9, 0.56, fill=SURFACE)
    shape_text(bx, [{"runs": [{"t": a + "  ", "bold": True, "size": 11}, {"t": b_, "size": 10, "color": MUTED}]}],
               align="l", size=11, margin=0.12)
    arrow(s, MX + 2.95, y + 0.28, 4.35, 4.05, color=LINE, width=1.25)
ex = box(s, 4.4, 3.45, 1.9, 1.2, fill=AMBER_LT)
shape_text(ex, [{"t": "Analyst Excel", "bold": True, "size": 13}, {"t": "manual, versioned by e-mail", "size": 10, "color": MUTED}])
arrow(s, 6.35, 4.05, 6.85, 4.05, color=MUTED)
dk = box(s, 6.9, 3.45, 1.9, 1.2, fill=AMBER_LT)
shape_text(dk, [{"t": "Weekly deck", "bold": True, "size": 13}, {"t": "stale, no lineage → leadership", "size": 10, "color": MUTED}])
text(s, 9.25, 1.85, 3.5, 0.4, "Six blind spots", size=16, color=NAVY, bold=True)
spots = ["Teams report different numbers", "Days of latency before leadership sees change",
         "No uncertainty on survey or sentiment figures", "No systematic early warning / anomaly detection",
         "No audit trail for approvals, certification, AI labels", "AI summaries without verified source data"]
for i, sp in enumerate(spots):
    y = 2.4 + i * 0.72
    circle(s, 9.25, y + 0.05, 0.36, fill=RED_LT, label="✕", size=12, color=RED)
    text(s, 9.75, y, 2.95, 0.6, sp, size=12, color=INK, anchor="m")
notes(s, "Most campaign reporting is team-shaped rather than question-shaped. The consequences are inconsistent numbers, "
         "latency, no uncertainty and no auditability.")

# ================================================================== 5. SOLUTION
s = frame("Our solution", "One governed intelligence layer, not seven disconnected workflows")
rows = [["Dimension", "Today", "With the Command Center"],
        ["Source of truth", "Multiple spreadsheets and decks", "Governed warehouse + metric store (one definition per KPI)"],
        ["Latency", "Weekly, manual", "Daily report by 08:00; intraday for priority sources"],
        ["Early warning", "Someone notices", "Statistical alert engine — Critical / High / Medium / Low"],
        ["Uncertainty", "Absent", "Margins of error, intervals and coverage warnings by default"],
        ["Cross-source view", "Social, media, survey, field in silos", "Common issue taxonomy, geography and time keys"],
        ["AI", "Unverified summaries", "Grounded AI Analyst with citations, timestamps, confidence"],
        ["Compliance", "Approvals in chats", "Control tower: approvals, MCMC refs, AI labels, spend, audit trail"],
        ["Security & privacy", "Shared credentials", "SSO, MFA, RBAC, encryption, audit logs, DPDP-aligned"]]
fills = {(r, 2): TEAL_LT for r in range(1, 9)}
table(s, MX, 1.85, 12.13, rows, col_w=[2.5, 3.9, 5.73], row_h=0.53, size=12, fills=fills, first_col_bold=True,
      zebra=False)
notes(s, "Contrast the current state with the future state. The right column is what the platform guarantees as "
         "process; it does not guarantee electoral outcomes.")

# ================================================================== 6. COMMAND CENTER CONCEPT
s = frame("Command Center concept", "Intelligence infrastructure — not just analysts")
layers = [("Executive Command Center", "Health score · 14 modules · alerts · reports", NAVY, 5.0),
          ("AI intelligence layer", "Grounded Q&A · summaries · decision-support briefs", SAFFRON, 5.6),
          ("Analytics, ML & multilingual NLP", "Statistics · forecasts · anomalies · topics · sentiment", BLUE, 6.2),
          ("Governed data foundation", "Registry · quality · lineage · security · privacy", TEAL, 6.8)]
for i, (t, d, c, wd) in enumerate(layers):
    x = MX + (6.8 - wd) / 2
    y = 1.9 + i * 1.18
    b = box(s, x, y, wd, 1.02, fill=c, radius=0.12)
    shape_text(b, [{"t": t, "bold": True, "size": 15, "color": WHITE}, {"t": d, "size": 11, "color": WHITE}])
text(s, 7.9, 1.9, 4.8, 0.4, "Capability pillars", size=16, color=NAVY, bold=True)
pillars = ["DATA", "AI", "ANALYTICS", "SOCIAL\nINTELLIGENCE", "MEDIA\nINTELLIGENCE", "DIGITAL\nMEASUREMENT",
           "FIELD\nINTELLIGENCE", "AUTOMATION", "COMMAND\nCENTER"]
for i, p in enumerate(pillars):
    x = 7.9 + (i % 3) * 1.63
    y = 2.45 + (i // 3) * 0.86
    b = box(s, x, y, 1.53, 0.74, fill=SAFFRON_LT if i in (1, 8) else SURFACE)
    shape_text(b, p, size=10, color=NAVY, bold=True, margin=0.03)
q = box(s, 7.9, 5.2, 4.83, 1.6, fill=NAVY)
shape_text(q, [{"t": "“We do not simply provide analysts. We build the intelligence infrastructure that turns fragmented "
                     "campaign data into a continuously learning decision-support system.”", "size": 12.5,
                "color": WHITE, "italic": True}], align="l", margin=0.2)
notes(s, "Four layers, nine capability pillars. The differentiator is infrastructure that keeps learning, owned and "
         "governed on the client's behalf.")

# ================================================================== 7. DATA ECOSYSTEM
s = frame("Data ecosystem", "Six source families — each with owner, lawful basis, retention")
fams = [("A", "Official / public", ["ECI statistical reports & index cards", "Historical results (ECI; curated research sets)",
                                     "Census & official indicators", "Public candidate disclosures"]),
        ("B", "Campaign-owned (authorised)", ["Website & social analytics", "Ad-platform reporting",
                                              "CRM / volunteer / event records (consented)", "Call-centre operational data"]),
        ("C", "Survey", ["Issue, awareness, satisfaction surveys", "Event & campaign feedback",
                         "Weighting, MoE, bias & QC metadata", "Consent recorded"]),
        ("D", "Digital platforms", ["Meta, Instagram, YouTube, X, Google", "Owned-account insights via permitted APIs",
                                    "Ad transparency libraries", "API access verified per platform"]),
        ("E", "Media", ["News sites & feeds (public/licensed)", "Regional & hyperlocal outlets",
                        "Broadcast transcripts — licensed only", "Search trends where available"]),
        ("F", "Field", ["Daily structured field reports", "Activity completion & coverage",
                        "Local issue reports", "Volunteer activity metrics"])]
for i, (lbl, t, ls) in enumerate(fams):
    x = MX + (i % 3) * 4.1
    y = 1.8 + (i // 3) * 2.5
    card(s, x, y, 3.93, 2.32, t, ls, badge=lbl, badge_fill=[NAVY, SAFFRON, BLUE, TEAL, OCHRE, NAVY2][i], bsize=11.5)
notes(s, "Breadth with discipline: no source enters without an owner, lawful basis or authorisation, permitted purposes "
         "and a retention rule. Public, consented and authorised data only.")

# ================================================================== 8. ACCESS REALITY
s = frame("Data sources & access reality", "We never assume an API exists — access is verified in Week 1")
rows = [["Platform / source", "Likely access route", "What must be verified (as of Sep 2026)"],
        ["Facebook Pages", "Graph API insights for owned pages", "App review, permissions, fields available"],
        ["Instagram", "Instagram Graph API (Business/Creator)", "Basic Display API ended 4 Dec 2024"],
        ["Meta ads & Ad Library", "Marketing API (owned); Ad Library API", "Identity/country verification; disclaimers"],
        ["Meta public content", "Meta Content Library", "Researcher-only (ICPSR); CrowdTangle closed Aug 2024"],
        ["YouTube", "Data API v3; Analytics API (owned)", "Quotas; channel authorisation"],
        ["X", "X API (pay-per-use credits)", "Budget caps, read limits, current terms"],
        ["Google Ads / Search", "Google Ads API; Transparency Center", "Election-ads verification; ECI pre-certificate per ad"],
        ["Google Trends", "Web; Trends API alpha (gated)", "Alpha access not assured — indicative only"],
        ["Website", "GA4 Data API; Search Console", "Consent mode; no PII in events"],
        ["Listening / media vendors", "Licensed feeds", "Lawful sourcing, licence scope, audit rights"]]
table(s, MX, 1.8, 12.13, rows, col_w=[2.6, 4.1, 5.43], row_h=0.405, size=11, first_col_bold=True)
b = box(s, MX, 6.35, 12.13, 0.5, fill=SAFFRON_LT)
shape_text(b, "API availability and permitted fields must be verified against the current platform documentation and access level.",
           size=12, color=SAFFRON, bold=True)
notes(s, "Honesty about access is a differentiator. Several popular routes have closed or become paid or restricted.")

# ================================================================== 9. DATA ARCHITECTURE
s = frame("Data architecture", "Production-grade pipeline from source to executive decision")
top = [("1  Sources", "API · file · DB · upload · survey · licensed feed"), ("2  Ingestion", "Dagster / Airflow; idempotent; secrets from vault"),
       ("3  Raw zone", "Immutable object storage; checksums"), ("4  Quality gates", "Freshness · volume · schema · ranges · dupes"),
       ("5  Standardised model", "dbt: geography · time · language · issue")]
bot = [("6  Warehouse + metric store", "PostgreSQL → BigQuery / Snowflake"), ("7  ML / NLP layer", "Models · embeddings · registry"),
       ("8  BI / dashboards", "Power BI or React/Next.js"), ("9  AI intelligence layer", "LLM + tool router + citations"),
       ("10  Executive Command Center", "Health score · alerts · reports")]
xs = [MX + i * 2.5 for i in range(5)]
for i, (t, d) in enumerate(top):
    b = box(s, xs[i], 1.9, 2.13, 1.25, fill=SURFACE, line=LINE)
    shape_text(b, [{"t": t, "bold": True, "size": 12, "color": NAVY}, {"t": d, "size": 10, "color": MUTED}])
    if i < 4:
        arrow(s, xs[i] + 2.15, 2.52, xs[i + 1] - 0.03, 2.52, color=SAFFRON, width=2)
arrow(s, xs[4] + 1.06, 3.18, xs[4] + 1.06, 3.62, color=SAFFRON, width=2)
for j, (t, d) in enumerate(bot):
    i = 4 - j
    fill = NAVY if j == 4 else (SAFFRON_LT if j == 3 else SURFACE)
    b = box(s, xs[i], 3.65, 2.13, 1.25, fill=fill, line=None if j == 4 else LINE)
    shape_text(b, [{"t": t, "bold": True, "size": 12, "color": WHITE if j == 4 else NAVY},
                   {"t": d, "size": 10, "color": "C9D3E3" if j == 4 else MUTED}])
    if j < 4:
        arrow(s, xs[i] - 0.02, 4.27, xs[i - 1] + 2.15, 4.27, color=SAFFRON, width=2)
g = box(s, MX, 5.3, 12.13, 1.45, fill=TEAL_LT)
shape_text(g, [{"t": "Cross-cutting governance & security", "bold": True, "size": 13, "color": TEAL},
               {"t": "Source & lawful-basis registry · permitted-use tags · column-level lineage · RBAC/SSO/MFA · encryption · "
                     "immutable audit logs · retention & deletion · model registry · cost guardrails", "size": 11.5, "color": INK}],
           align="l", margin=0.25)
notes(s, "Each component earns its place: Postgres + pgvector for the POC, a scale warehouse only when volumes demand it, "
         "dbt for tested and documented transformations, and an AI layer that sits on top rather than beside the data.")

# ================================================================== 10. DATA MODEL + ANALYTICS
s = frame("Data model & analytics stack", "Aggregate, authorised records joined on geography, time and issue")
groups = [("Reference & public", ["campaign", "constituency", "geography", "historical_election", "issue"], BLUE),
          ("Intelligence facts", ["survey_response (anonymous)", "content_performance", "media_mention", "sentiment_record (aggregate)",
                                  "field_activity · event", "operational_metric", "campaign_spend"], SAFFRON),
          ("Governance & operations", ["data_source", "data_quality", "compliance_record", "alert · report", "model_run", "audit_log"], TEAL)]
for i, (t, ents, c) in enumerate(groups):
    x = MX + i * 2.3
    text(s, x, 1.8, 2.15, 0.3, t, size=11.5, color=c, bold=True)
    for j, e in enumerate(ents):
        b = box(s, x, 2.18 + j * 0.52, 2.15, 0.42, fill=SURFACE, line=LINE)
        shape_text(b, e, size=10, color=INK, margin=0.03)
b = box(s, MX, 5.95, 6.75, 0.8, fill=RED_LT)
shape_text(b, "By design there is no table of individuals' political beliefs or preferences. Survey microdata is anonymous, "
              "binned and used only for weighted aggregates.", size=11, color=RED, bold=True, align="l", margin=0.15)
text(s, 7.75, 1.8, 5.0, 0.35, "Analytics maturity ladder", size=14, color=NAVY, bold=True)
ladder = [("Descriptive", "What happened? Trends, KPIs, channel & historical comparison", BLUE_LT),
          ("Diagnostic", "Why did it change? Channel, content, geography, issue decomposition", BLUE_LT),
          ("Predictive", "What is likely next? Forecasts with intervals, assumptions, validation", SAFFRON_LT),
          ("Decision support", "Operational, monitoring & data-quality priorities; humans decide", TEAL_LT)]
for i, (t, d, f) in enumerate(ladder):
    y = 5.75 - i * 1.02
    x = 7.75 + i * 0.3
    b = box(s, x, y, 5.0 - i * 0.3, 0.9, fill=f)
    shape_text(b, [{"t": t, "bold": True, "size": 12.5, "color": NAVY}, {"t": d, "size": 10.5, "color": INK}],
               align="l", margin=0.15)
notes(s, "Conceptual ERD in three groups. The full DDL is in poc/schema.sql. Predictions are never presented as "
         "certainty and never at individual level.")

# ================================================================== 11. AI / NLP LAYER
s = frame("AI / NLP layer", "Multilingual NLP: listening → topic → sentiment → trend → alert")
flow = [("Public & licensed text", "permitted APIs, licensed feeds"), ("Language ID + normalise", "Hinglish, romanised, spelling"),
        ("Topic / issue", "campaign taxonomy classifier"), ("Sentiment / tone", "per-language validated"),
        ("Trend & velocity", "baselines, change-points"), ("Alert", "severity + human triage")]
for i, (t, d) in enumerate(flow):
    x = MX + i * 2.05
    b = box(s, x, 1.9, 1.8, 1.25, fill=NAVY if i == 5 else SURFACE, line=None if i == 5 else LINE)
    shape_text(b, [{"t": t, "bold": True, "size": 12, "color": WHITE if i == 5 else NAVY},
                   {"t": d, "size": 10, "color": "C9D3E3" if i == 5 else MUTED}])
    if i < 5:
        arrow(s, x + 1.82, 2.52, x + 2.03, 2.52, color=SAFFRON, width=2)
text(s, MX, 3.5, 5.0, 0.35, "Languages", size=14, color=NAVY, bold=True)
for i, lg in enumerate(["Hindi", "English", "Hinglish", "Regional languages", "Romanised Indian languages"]):
    pill(s, MX + (i % 3) * 1.85 if i < 3 else MX + (i - 3) * 2.75, 3.95 if i < 3 else 4.38,
         1.75 if i < 3 else 2.65, lg, fill=BLUE_LT, color=BLUE, size=10.5, h=0.34)
text(s, MX, 4.95, 5.4, 1.9, [
    {"t": "Also: NER · event detection · duplicate / copy detection · toxicity · misinformation-risk flags (always human-verified)", "bullet": True},
    {"t": "Gold sets per language, double-annotated (κ ≥ 0.70); POC gate macro-F1 ≥ 0.70 per language", "bullet": True},
], size=12, spacing_after=8)
rows = [["Capability", "Approach", "Metric"],
        ["Topic / issue", "Fine-tuned multilingual encoder", "Macro-F1 / language"],
        ["Sentiment / tone", "Encoder + calibration", "Macro-F1, per-class recall"],
        ["Emerging topics", "Embeddings + clustering", "Coherence, analyst rating"],
        ["Duplicates", "MinHash + cosine", "Pair precision / recall"],
        ["Translation", "IndicTrans2 (22 languages)", "Human spot-check"],
        ["Misinformation-risk", "Claim-matching + heuristics", "Precision@k (human-confirmed)"]]
table(s, 6.4, 3.5, 6.33, rows, col_w=[1.9, 2.5, 1.93], row_h=0.44, size=10.5, first_col_bold=True)
notes(s, "Code-mixed and romanised text is the norm in Indian social media. Accuracy is reported per language, never "
         "just overall. Misinformation flags are prioritisation aids for human fact-checkers, never automated verdicts.")

# ================================================================== 12. SOCIAL INTELLIGENCE
s = frame("Social intelligence", "Detect change — and state how much of the conversation we see", demo=True)
image(s, chart_img("social_volume_anomaly.png"), MX, 1.75, w=5.8)
image(s, chart_img("sentiment_by_topic_ci.png"), MX, 4.25, w=5.8)
sm = M["social"]
kpi_card(s, 6.75, 1.8, 2.9, 1.25, "3,849", "mentions on 31 Aug vs 1,314 prior-week median", "High alert · Water supply", SAFFRON)
kpi_card(s, 9.83, 1.8, 2.9, 1.25, f"{sm['negative_share_pct']}%", "negative share (de-duplicated, 6 weeks)")
kpi_card(s, 6.75, 3.2, 2.9, 1.25, f"{sm['geo_coverage_pct']}%", "posts with usable public location — coverage limit")
kpi_card(s, 9.83, 3.2, 2.9, 1.25, f"{M['data_quality']['duplicate_mentions_pct']}%", "near-duplicates removed before counting")
text(s, 6.75, 4.65, 6.0, 1.3, [
    {"t": "Modules: volume · sentiment · topic trends · issue velocity · engagement · platform comparison · amplification by account type · emerging issues", "bullet": True},
    {"t": "Every tile carries a Coverage & Representativeness Index", "bullet": True},
], size=11.5, spacing_after=6)
b = box(s, 6.75, 6.0, 5.98, 0.78, fill=RED_LT)
shape_text(b, "Public social data is not the electorate. Sentiment describes visible online conversation only.",
           size=11.5, color=RED, bold=True, align="l", margin=0.15)
notes(s, "Synthetic storyline: a water-pipeline outage on 31 Aug creates a spike. The anomaly band is a rolling median "
         "plus or minus three robust standard deviations. Intervals on sentiment come from bootstrap resampling.")

# ================================================================== 13. MEDIA INTELLIGENCE
s = frame("Media intelligence", "Multilingual media monitoring — licensed where required", demo=True)
image(s, chart_img("media_weekly_outlets.png"), MX, 1.75, w=7.6)
md = M["media"]
kpi_card(s, MX, 5.05, 2.4, 1.3, f"{md['last7']:,}", "items in the last 7 days")
kpi_card(s, MX + 2.6, 5.05, 2.4, 1.3, f"{md['regional_share_pct']}%", "regional & hyperlocal share")
kpi_card(s, MX + 5.2, 5.05, 2.4, 1.3, f"{md['last7_negative_pct']}%", "negative tone, last 7 days")
text(s, 8.6, 1.8, 4.1, 0.4, "Media Intelligence Dashboard", size=15, color=NAVY, bold=True)
text(s, 8.6, 2.3, 4.1, 4.4, [{"t": t, "bullet": True} for t in [
    "Article & segment classification by issue", "Topic extraction & story threads across outlets",
    "Tone towards tracked entities, with confidence", "Candidate / organisation mentions (NER + entity linking)",
    "Issue share of voice by outlet type & language", "Regional-language outlets prioritised",
    "Broadcast transcripts — only where licensed", "Volume & tone alerts; daily AI summary with citations"]],
    size=12, spacing_after=7)
notes(s, "Regional media often leads national coverage on local issues. Broadcast analysis only with licensed "
         "transcripts; no unlicensed recording or redistribution.")

# ================================================================== 14. SURVEY INTELLIGENCE
s = frame("Survey intelligence", "Statistically defensible — every estimate carries its uncertainty", demo=True)
image(s, chart_img("survey_issue_salience.png"), MX, 1.75, w=7.6)
sv = M["survey"]
b = box(s, MX, 5.15, 7.6, 1.6, fill=SAFFRON_LT)
shape_text(b, [{"runs": [{"t": f"+{sv['water_change_pts']} pts ", "size": 24, "bold": True, "color": SAFFRON},
                         {"t": "water-supply salience, Wave 1 → Wave 3", "size": 13, "bold": True, "color": NAVY}]},
               {"t": f"{sv['water_w1_pct']}% → {sv['water_w3_pct']}% ± {sv['water_w3_moe']} (95% CI, n_eff {sv['wave3_n_eff']:,}); "
                     f"significant (z ≈ {sv['water_change_z']:.0f}). QC excluded {sv['qc_excluded_pct']}% of interviews.",
                "size": 11.5, "color": INK}], align="l", margin=0.2)
text(s, 8.6, 1.8, 4.1, 0.4, "Methodology built in", size=15, color=NAVY, bold=True)
text(s, 8.6, 2.3, 4.1, 3.3, [{"t": t, "bullet": True} for t in [
    "Sampling design & sample-size calculator", "Post-stratification / raking with trimmed weights",
    "Design effect → effective n → honest MoE", "Weighted cross-tabs with small-cell suppression",
    "Significance tests with multiple-comparison control", "Speeders, straight-liners, interviewer & mode checks",
    "Non-response & profile bias checks"]], size=12, spacing_after=6)
b = box(s, 8.6, 5.75, 4.13, 1.0, fill=RED_LT)
shape_text(b, "Surveys describe the sampled population at fieldwork time. They do not guarantee or predict results.",
           size=11, color=RED, bold=True, align="l", margin=0.15)
notes(s, "Issue, awareness and satisfaction surveys only, reported in aggregate. Margins of error use the effective "
         "sample size after weighting (Kish).")

# ================================================================== 15. DIGITAL ANALYTICS
s = frame("Digital analytics", "Digital Performance Scorecard and Content Performance Matrix", demo=True)
cards = [("9.21 M", "impressions (7 days)", "+0.9% W/W", TEAL), ("3.49%", "engagement rate", "+0.18 pts W/W", TEAL),
         ("1.50 M", "video views", "−3.8% W/W", SAFFRON), ("1.11%", "click-through rate", "−0.03 pts", MUTED),
         ("₹116", "CPM (boosted)", "+4.5% W/W", SAFFRON), ("100%", "boosted items with MCMC ref", "Compliant", TEAL)]
for i, (v, l, d, c) in enumerate(cards):
    kpi_card(s, MX + i * 2.04, 1.75, 1.9, 1.3, v, l, d, c, vsize=20)
image(s, chart_img("content_matrix_heatmap.png"), MX, 3.2, h=3.6)
text(s, 8.95, 3.25, 3.8, 0.4, "What leadership learns", size=15, color=NAVY, bold=True)
text(s, 8.95, 3.75, 3.8, 2.3, [{"t": t, "bullet": True} for t in [
    "Short video leads engagement across themes (~1.8× static images)",
    "Explainers and youth & jobs content over-index",
    "Test before scaling: pre-registered experiments with power analysis"]], size=12, spacing_after=7)
b = box(s, 8.95, 5.95, 3.78, 0.85, fill=SURFACE)
shape_text(b, "Format & theme planning at aggregate level — never individual-level targeting.", size=10.5,
           color=MUTED, bold=True, align="l", margin=0.12)
notes(s, "Platform-reported metrics; cross-platform totals are indicative because definitions differ. Conversions only "
         "where legitimately measurable on owned, consented forms.")

# ================================================================== 16. FIELD & CALL CENTRE
s = frame("Field operations & call-centre intelligence", "See where operations are behind — and why", demo=True)
image(s, chart_img("call_centre_weekly.png"), MX, 1.75, w=6.6)
fd, cc = M["field"], M["call_centre"]
kpi_card(s, MX, 4.55, 2.1, 1.3, f"{cc['answer_rate_last7_pct']}%", "answer rate, 7 days", "SLA 90% — breach", RED, vsize=20)
kpi_card(s, MX + 2.25, 4.55, 2.1, 1.3, "55.6%", "first-contact resolution", None, vsize=20)
kpi_card(s, MX + 4.5, 4.55, 2.1, 1.3, f"{cc['median_wait_s']} s", "median wait (answered)", None, vsize=20)
text(s, MX, 6.0, 6.6, 0.8, "Call-centre analytics use aggregate operational data only — no private communications, no inference "
     "about callers' views.", size=10.5, color=MUTED, italic=True)
text(s, 7.55, 1.8, 5.2, 0.4, "Field operations (last 7 days)", size=15, color=NAVY, bold=True)
kpi_card(s, 7.55, 2.3, 2.5, 1.3, "83.2%", "activities completed (target 85%)", None, vsize=20)
kpi_card(s, 10.23, 2.3, 2.5, 1.3, "79.3%", "reports submitted on time", None, vsize=20)
kpi_card(s, 7.55, 3.75, 2.5, 1.3, "67.4%", "Hill Block completion", "Bottleneck", RED, vsize=20)
kpi_card(s, 10.23, 3.75, 2.5, 1.3, "1,842", "local issue reports logged", None, vsize=20)
text(s, 7.55, 5.25, 5.2, 1.5, [{"t": t, "bullet": True} for t in [
    "Tracks completion, coverage, attendance estimates, response time, submission quality",
    "Bottleneck list with named owners; late-report reconciliation avoids false alarms"]], size=12, spacing_after=6)
notes(s, "Operational analytics, not surveillance. Attendance is an estimate; no identity capture at events.")

# ================================================================== 17. GIS
s = frame("Geographic intelligence", "Aggregate maps for coverage — never individual targeting", demo=True)
image(s, chart_img("zone_map_field_completion.png"), MX, 1.75, h=4.95)
text(s, 8.1, 1.8, 4.6, 0.4, "Map layers", size=15, color=NAVY, bold=True)
layers = ["Constituency & admin boundaries", "Historical results (public)", "Turnout trends (public)", "Survey coverage",
          "Campaign activity coverage", "Event locations (public events)", "Issue distribution", "Media distribution",
          "Operational coverage"]
for i, l in enumerate(layers):
    pill(s, 8.1 + (i % 2) * 2.33, 2.3 + (i // 2) * 0.45, 2.23, l, fill=BLUE_LT, color=BLUE, size=9.5, h=0.36, bold=False)
b = box(s, 8.1, 4.7, 4.63, 2.05, fill=SURFACE)
shape_text(b, [{"t": "Guardrails", "bold": True, "size": 13, "color": NAVY},
               {"t": "No household or individual plotting", "bullet": True, "size": 11},
               {"t": "Small-area suppression (cells < 10 hidden)", "bullet": True, "size": 11},
               {"t": "Official Survey of India boundaries for any national/state outline", "bullet": True, "size": 11},
               {"t": "Delimitation vintage recorded for every boundary layer", "bullet": True, "size": 11}],
           align="l", anchor="t", margin=0.18)
notes(s, "Fictional hexagonal geography for the demo. Real deployments use official boundaries and record their "
         "vintage; community boundary datasets are used with attribution and verification.")

# ================================================================== 18. FORECASTING & ML
s = frame("Forecasting & machine learning", "Forecasts with intervals and validation — never certainty", demo=True)
image(s, chart_img("forecast_volume.png"), MX, 1.75, w=7.5)
text(s, MX, 4.95, 7.5, 0.35, "Model toolkit (fit for purpose, simplest first)", size=13, color=NAVY, bold=True)
tk = ["Regression", "Logistic regression", "Classification", "Clustering", "Time-series", "Anomaly detection",
      "Random Forest", "Gradient boosting / XGBoost", "PCA", "Topic modelling", "Embeddings", "Similarity search"]
for i, t in enumerate(tk):
    pill(s, MX + (i % 4) * 1.9, 5.4 + (i // 4) * 0.44, 1.8, t, fill=SURFACE, color=NAVY, size=9.5, h=0.34, bold=False)
fc = M["forecast"]
rows = [["Model card", "issue_volume_forecaster v0.3"],
        ["Purpose", "Monitoring-capacity planning"],
        ["Training window", "01–24 Aug (validation 25–30 Aug)"],
        ["Method", "Trend + weekly seasonality (OLS)"],
        ["Validation", f"MAPE {fc['validation_mape_pct']}% (synthetic; real error higher)"],
        ["Assumptions", "No new shocks; stable platform access"],
        ["Limitations", "Cannot anticipate events"],
        ["Human review", "Signed off by Lead Data Scientist"],
        ["Status", "Approved — internal planning only"]]
table(s, 8.4, 1.8, 4.33, rows, col_w=[1.45, 2.88], row_h=0.5, size=10.5, first_col_bold=True)
b = box(s, 8.4, 6.4, 4.33, 0.4, fill=RED_LT)
shape_text(b, "No model infers an individual's political preference", size=10.5, color=RED, bold=True)
notes(s, "Every model has a card: purpose, data, window, features, metrics, validation, bias checks, limitations, owner, "
         "version and approval status.")

# ================================================================== 19. AI ANALYST
s = frame("AI Campaign Analyst", "Grounded answers with citations, timestamps and confidence")
steps = [("User (SSO, role)", SURFACE, NAVY), ("Policy & intent guard", SURFACE, NAVY), ("LLM planner", SURFACE, NAVY),
         ("Tool router", SAFFRON, WHITE)]
for i, (t, f, c) in enumerate(steps):
    b = box(s, MX, 1.85 + i * 0.72, 2.6, 0.55, fill=f, line=None if f == SAFFRON else LINE)
    shape_text(b, t, size=11.5, color=c, bold=True)
    if i < 3:
        arrow(s, MX + 1.3, 2.41 + i * 0.72, MX + 1.3, 2.56 + i * 0.72, color=MUTED)
tools_ = ["Metrics API", "SQL templates", "Search", "Vector / RAG", "Analytics APIs"]
for j, t in enumerate(tools_):
    b = box(s, MX + 2.95, 1.85 + j * 0.62, 2.25, 0.5, fill=BLUE_LT)
    shape_text(b, t, size=11, color=BLUE, bold=True)
    arrow(s, MX + 2.62, 4.28, MX + 2.93, 2.1 + j * 0.62, color=LINE, width=1)
for i, t in enumerate(["Verified data + source IDs", "Numeric & citation check", "Answer + audit log"]):
    b = box(s, MX + (0 if i == 0 else 0), 5.0 + i * 0.62, 5.2, 0.5, fill=TEAL_LT if i < 2 else NAVY)
    shape_text(b, t, size=11, color=TEAL if i < 2 else WHITE, bold=True)
arrow(s, MX + 4.07, 4.95, MX + 4.07, 4.99, color=MUTED)
# chat mock
cx = 6.35
box(s, cx, 1.8, 6.38, 5.0, fill=SURFACE, line=LINE)
b = box(s, cx + 2.4, 1.98, 3.8, 0.48, fill=NAVY, radius=0.3)
shape_text(b, "What changed in the last 24 hours?", size=11.5, color=WHITE, bold=True)
text(s, cx + 0.25, 2.6, 5.9, 3.5, [
    {"runs": [{"t": "FACTS", "bold": True, "color": TEAL, "size": 11.5}]},
    {"t": "Public mentions 3,849 vs prior-week median 1,314 — High anomaly  [social.mentions_daily · alert A-0931]", "bullet": True, "size": 11.5},
    {"t": "61% of mentions on Water supply  [model M3 v1.2]", "bullet": True, "size": 11.5},
    {"t": "Regional media on the issue: 123 items vs 9.9/day  [media.mentions_daily]", "bullet": True, "size": 11.5},
    {"t": "Helpline answer rate 85% vs 90% SLA  [ops.call_answer_rate]", "bullet": True, "size": 11.5},
    {"runs": [{"t": "INTERPRETATION", "bold": True, "color": SAFFRON, "size": 11.5}], "after": 2},
    {"t": "Signals are consistent with a local service-disruption story; geographic spread uncertain (18% geo-coverage).", "size": 11.5},
    {"runs": [{"t": "FOLLOW-UPS", "bold": True, "color": BLUE, "size": 11.5}], "after": 2},
    {"t": "Validate with field issue reports; review helpline category mix; consider a survey item in next wave.", "size": 11.5},
], size=11.5, spacing_after=5)
pill(s, cx + 0.25, 6.3, 2.9, "Confidence: Medium · data as of 07:00 IST", fill=WHITE, color=MUTED, size=9, h=0.32, bold=False)
pill(s, cx + 3.3, 6.3, 2.85, "Refuses: profiling · persuasion · predictions", fill=RED_LT, color=RED, size=9, h=0.32)
notes(s, "The LLM never answers numbers from memory. Citations are generated from tool metadata, not by the model. Every "
         "prompt, tool call, source and model version is logged. DEMO DATA in the sample answer.")

# ================================================================== 20. ALERTS
s = frame("Real-time alert engine", "Four severity levels, owners and response clocks")
lv = [("CRITICAL", RED, RED_LT, "Compliance-breach risk, priority pipeline outage, security incident, extreme KPI anomaly",
       "Ack ≤ 15 min · act ≤ 1 h"),
      ("HIGH", SAFFRON, SAFFRON_LT, "Significant anomaly (> 4 robust SD), fast-growing issue, high-reach media story",
       "Ack ≤ 1 h"),
      ("MEDIUM", AMBER, AMBER_LT, "Notable movement (3–4 SD), sustained trend change, data-quality degradation",
       "Same day"),
      ("LOW", GREEN, GREEN_LT, "Informational deviations, stale approvals, minor forecast misses", "Weekly review")]
for i, (t, c, f, d, sla) in enumerate(lv):
    y = 1.85 + i * 1.2
    b = box(s, MX, y, 1.7, 1.02, fill=c)
    shape_text(b, t, size=13, color=WHITE, bold=True)
    b = box(s, MX + 1.85, y, 4.9, 1.02, fill=f)
    shape_text(b, d, size=11.5, color=INK, align="l", margin=0.15)
    b = box(s, MX + 6.9, y, 1.5, 1.02, fill=SURFACE)
    shape_text(b, sla, size=10.5, color=NAVY, bold=True)
text(s, 9.35, 1.85, 3.4, 0.4, "Alert catalogue", size=15, color=NAVY, bold=True)
text(s, 9.35, 2.3, 3.4, 4.5, [{"t": t, "bullet": True} for t in [
    "Social-volume spike", "Abnormal sentiment movement", "Viral content", "Digital-performance movement",
    "Media spike", "Pipeline failure", "Survey anomaly", "Data-quality deterioration", "Compliance deadline",
    "Abnormal spend", "Unexpected KPI movement", "AI label missing"]], size=11.5, spacing_after=3)
notes(s, "Alert hygiene matters as much as detection: grouping, suppression windows, owner assignment and a weekly "
         "precision review keep alert fatigue down.")

# ================================================================== 21. EXECUTIVE DASHBOARD
s = frame("Executive dashboard", "One screen, eight domains, drill-down to 14 modules", demo=True)
box(s, MX, 1.75, 12.13, 5.15, fill=SURFACE, line=LINE, radius=0.03)
nav = rect(s, MX, 1.75, 12.13, 0.38, fill=NAVY)
shape_text(nav, "Overview   Digital   Social   Issues   Media   Survey   Field   Geo   Forecast   Alerts   Compliance   Data Quality   AI Analyst   Reports",
           size=9.5, color=WHITE, align="l", margin=0.15)
box(s, 0.8, 2.3, 3.0, 2.7, fill=WHITE)
cd = CategoryChartData()
cd.categories = ["score", "rest"]
cd.add_series("Health", (74, 26))
gf = s.shapes.add_chart(XL_CHART_TYPE.DOUGHNUT, Inches(1.2), Inches(2.4), Inches(2.2), Inches(2.0), cd)
ch = gf.chart
ch.has_title = False
ch.has_legend = False
ch.plots[0].has_data_labels = False
pts = ch.plots[0].series[0].points
pts[0].format.fill.solid(); pts[0].format.fill.fore_color.rgb = rgb(SAFFRON)
pts[1].format.fill.solid(); pts[1].format.fill.fore_color.rgb = rgb("E3E6EA")
ch.plots[0].series[0].format.line.fill.background()
from pptx.oxml.ns import qn as _qn
hole = ch.plots[0]._element.find(_qn("c:holeSize"))
if hole is not None:
    hole.set("val", "72")
text(s, 1.2, 3.05, 2.2, 0.6, "74", size=30, color=NAVY, bold=True, align="c")
text(s, 0.9, 4.42, 2.8, 0.5, [{"t": "Campaign Intelligence Health", "size": 10.5, "bold": True, "color": NAVY, "align": "c", "after": 0},
                              {"t": "AMBER · operational, not electoral", "size": 9, "color": AMBER, "align": "c"}], size=10)
box(s, 4.0, 2.3, 4.3, 2.7, fill=WHITE)
text(s, 4.15, 2.35, 4.0, 0.3, "Domain scores (0–100)", size=10.5, color=NAVY, bold=True)
cd = CategoryChartData()
doms = ["Compliance", "Digital", "Data Quality", "Survey", "Media", "Social", "Operations", "Field"]
vals = [86, 80, 78, 77, 75, 70, 64, 62]
cd.categories = doms[::-1]
cd.add_series("Score", vals[::-1])
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(4.05), Inches(2.62), Inches(4.2), Inches(2.35), cd)
ch = gf.chart
ch.has_title = False
ch.has_legend = False
pl = ch.plots[0]
pl.gap_width = 60
pl.has_data_labels = True
pl.data_labels.font.size = Pt(8.5)
pl.data_labels.font.color.rgb = rgb(INK)
pl.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
ser = pl.series[0]
ser.format.fill.solid(); ser.format.fill.fore_color.rgb = rgb(BLUE)
for idx, v in enumerate(vals[::-1]):
    if v < 65:
        p_ = ser.points[idx]
        p_.format.fill.solid(); p_.format.fill.fore_color.rgb = rgb(SAFFRON)
ch.value_axis.maximum_scale = 100
ch.value_axis.visible = False
ch.value_axis.has_major_gridlines = False
ch.category_axis.tick_labels.font.size = Pt(8.5)
ch.category_axis.tick_labels.font.color.rgb = rgb(MUTED)
ch.category_axis.format.line.fill.background()
box(s, 8.5, 2.3, 4.03, 2.7, fill=WHITE)
text(s, 8.65, 2.35, 3.8, 0.3, "Top changes · last 24 h", size=10.5, color=NAVY, bold=True)
chg = [("H", SAFFRON, "Helpline answer rate 84% < 90% SLA"), ("M", AMBER, "Hill Block completion 67% (target 85%)"),
       ("M", AMBER, "X connector latency — amber source"), ("L", GREEN, "'Jobs & skills' share +1.8 pts"),
       ("L", GREEN, "ER 3.49%, +0.18 pts W/W")]
for i, (lv_, c, t) in enumerate(chg):
    y = 2.72 + i * 0.44
    circle(s, 8.68, y + 0.04, 0.3, fill=c, label=lv_, size=9)
    text(s, 9.08, y, 3.4, 0.4, t, size=10, color=INK, anchor="m")
kp = [("1,344", "mentions (day)"), ("41.2%", "negative share"), ("122", "media items"), ("3.49%", "engagement rate"),
      ("83.2%", "field completion"), ("84.4%", "answer rate"), ("1 High", "open alerts"), ("0", "compliance exceptions")]
for i, (v, l) in enumerate(kp):
    x = 0.8 + i * 1.475
    box(s, x, 5.2, 1.38, 1.5, fill=WHITE)
    text(s, x + 0.1, 5.3, 1.2, 0.45, v, size=16, color=NAVY, bold=True)
    text(s, x + 0.1, 5.78, 1.2, 0.5, l, size=9, color=MUTED)
    text(s, x + 0.1, 6.35, 1.2, 0.3, "● source ok", size=8, color=GREEN)
notes(s, "The Health Score is an operational indicator. Any domain below 50 caps the headline at Amber so good news "
         "cannot hide bad news. Every tile shows its data-quality status.")

# ================================================================== 22. COMPLIANCE CONTROL TOWER
s = frame("Election Compliance Control Tower", "Approvals, certification, AI labels, spend — one audit trail", demo=True)
rows = [["Item", "Type", "Approval (owner · time)", "MCMC certification", "AI disclosure / label", "Spend", "Alert"],
        ["CT-0417", "Paid video", "Approved · Compliance · 12 Sep 16:42", "Certified · MCMC-DEMO-0417", "AI-generated · label ✓ · entity ✓", "₹1.8 L", "—"],
        ["CT-0422", "Paid carousel", "Approved · Compliance · 12 Sep 18:05", "Applied · awaiting", "Not AI", "₹0.9 L", "Block publish"],
        ["CT-0425", "Organic video", "Legal review", "Not required (organic)", "AI-assisted edit · label ✗", "—", "CRITICAL"],
        ["CT-0431", "Bulk SMS", "Approved · Compliance · 13 Sep 10:11", "Certified · MCMC-DEMO-0431", "Not AI", "₹0.4 L", "—"],
        ["CT-0433", "Paid static", "Draft", "—", "Not AI", "—", "—"],
        ["SP-TOTAL", "Digital spend", "Finance reconciled 13 Sep", "—", "—", "82% of limit", "HIGH"]]
colors = {(2, 6): SAFFRON, (3, 6): RED, (6, 6): SAFFRON, (3, 4): RED, (2, 3): AMBER}
bold = {(2, 6), (3, 6), (6, 6), (3, 4)}
table(s, MX, 1.8, 12.13, rows, col_w=[1.0, 1.35, 2.75, 2.2, 2.45, 1.1, 1.28], row_h=0.46, size=10, colors=colors,
      bold_cells=bold, first_col_bold=True)
text(s, MX, 5.2, 5.8, 0.35, "Rules engine (configured by legal)", size=13, color=NAVY, bold=True)
text(s, MX, 5.6, 5.8, 1.3, [{"t": t, "bullet": True} for t in [
    "Paid item without certification ref → block “ready”", "AI flag without label → Critical",
    "Scheduled post inside silence window → block", "Takedown notice unactioned at 2 h → Critical (3 h limit)"]],
    size=11, spacing_after=2)
text(s, 6.75, 5.2, 6.0, 0.35, "Regulatory anchors (verify with legal)", size=13, color=NAVY, bold=True)
anc = ["MCC & social media — ECI 2013", "MCMC pre-certification — ECI 20 Mar 2026", "AI labels & records — ECI 24 Oct 2025",
       "SGI labelling — IT Rules 2026", "Silence period — RP Act s.126", "Exit polls — RP Act s.126A"]
for i, a in enumerate(anc):
    pill(s, 6.75 + (i % 2) * 3.0, 5.6 + (i // 2) * 0.4, 2.9, a, fill=BLUE_LT, color=BLUE, size=9, h=0.33, bold=False)
notes(s, "The control tower supports the compliance team; it does not make legal determinations. This is an "
         "analytics/technology proposal, not legal advice.")

# ================================================================== 23. SECURITY & GOVERNANCE
s = frame("Security & data governance", "Enterprise controls from day one — privacy by design")
ctl = [("RBAC + RLS", "Least privilege by role & geography"), ("SSO", "SAML / OIDC with agency IdP"), ("MFA", "Mandatory; passkeys for admins"),
       ("Encryption", "At rest (KMS) · in transit (TLS 1.2+)"), ("Secrets", "Vault; scanning; no creds in chat"), ("Audit logs", "Immutable; ≥ 1 yr; 180 d in India"),
       ("Key rotation", "≤ 90 days; revoke on exit"), ("Environments", "Dev / test / prod separated"), ("Backup & DR", "PITR; RPO ≤ 1 h; RTO ≤ 4 h"),
       ("Incident response", "CERT-In 6 h path; DPDP breach workflow"), ("Retention", "Per-source schedules; deletion certs"), ("Vendors", "DPAs, residency, audit rights")]
for i, (t, d) in enumerate(ctl):
    x = MX + (i % 4) * 2.08
    y = 1.85 + (i // 4) * 1.62
    box(s, x, y, 1.96, 1.45, fill=SURFACE)
    circle(s, x + 0.15, y + 0.15, 0.3, fill=NAVY, label="✓", size=10)
    text(s, x + 0.15, y + 0.52, 1.7, 0.35, t, size=12.5, color=NAVY, bold=True)
    text(s, x + 0.15, y + 0.86, 1.7, 0.6, d, size=10, color=MUTED)
b = box(s, 9.05, 1.85, 3.68, 4.9, fill=NAVY)
shape_text(b, [{"t": "Data governance", "bold": True, "size": 15, "color": WHITE, "after": 8}] +
           [{"t": t, "bullet": True, "size": 11, "color": WHITE, "after": 4} for t in [
               "Source & lawful-basis registry", "Permitted-use tags enforced at query time", "Data dictionary & metadata",
               "Column-level lineage", "Consent / authorisation tracking", "Minimisation & purpose limitation",
               "Quality monitoring on every source", "Exit plan: export + deletion certificate"]],
           align="l", anchor="t", margin=0.25)
notes(s, "Built to the fully in-force DPDP standard now. CERT-In requires specified incidents reported within 6 hours "
         "and ICT logs kept for 180 days in India.")

# ================================================================== 24. RESPONSIBLE AI
s = frame("Responsible AI", "Human oversight, no fabrication, full traceability")
pr = ["Human oversight", "No fabricated information", "No unsupported prediction", "Explainability", "Source traceability",
      "Data minimisation", "Privacy", "Security", "Bias monitoring", "Model monitoring", "Synthetic-content safeguards",
      "Compliance review"]
for i, p in enumerate(pr):
    x = MX + (i % 2) * 2.55
    y = 1.85 + (i // 2) * 0.72
    b = box(s, x, y, 2.43, 0.6, fill=SURFACE)
    shape_text(b, p, size=11, color=NAVY, bold=True)
text(s, MX, 6.3, 5.0, 0.5, "Aligned to MeitY India AI Governance Guidelines (Nov 2025), NIST AI RMF, ISO/IEC 42001.",
     size=10, color=MUTED, italic=True)
kinds = [("AI-assisted analytics", BLUE, BLUE_LT, "Internal analysis & drafting", ["Topic/sentiment models", "Forecasts",
                                                                                     "AI Analyst answers"], "Model governance · citations · human review"),
         ("AI-generated content", TEAL, TEAL_LT, "Any AI-produced text/image/audio", ["Draft summaries", "Translations",
                                                                                     "Internal visuals"], "Marked internal · reviewed before any external use"),
         ("AI-generated campaign creative", SAFFRON, SAFFRON_LT, "Synthetic media published for campaigning", ["AI video/image/audio ads", "AI-altered posts"],
          "ECI label ≥10% · entity disclosed · records · 3-h takedown · not generated by this platform")]
for i, (t, c, f, sub, ex, ctrl) in enumerate(kinds):
    x = 5.95 + i * 2.28
    box(s, x, 1.85, 2.18, 4.95, fill=f)
    text(s, x + 0.15, 1.97, 1.9, 0.75, t, size=13, color=c, bold=True)
    text(s, x + 0.15, 2.75, 1.9, 0.6, sub, size=10.5, color=INK, italic=True)
    text(s, x + 0.15, 3.4, 1.9, 1.4, [{"t": e, "bullet": True} for e in ex], size=10.5, spacing_after=3)
    text(s, x + 0.15, 4.85, 1.9, 1.9, [{"t": "Controls", "bold": True, "size": 10.5, "color": c}, {"t": ctrl, "size": 10.5}], size=10.5)
notes(s, "Keep the three categories separate. The platform performs AI-assisted analytics; it tracks, but does not "
         "generate, campaign creative.")

# ================================================================== 25. TEAM STRUCTURE
s = frame("Team structure", "A multidisciplinary intelligence team — sized to the election")
b = box(s, 5.17, 1.8, 3.0, 0.6, fill=NAVY)
shape_text(b, "Programme Director", size=12.5, color=WHITE, bold=True)
units = [("Product & Delivery", "Product Mgr · Project Mgr"), ("Analytics & Data Science", "Analytics Lead · DS · DA"),
         ("Data & Platform Eng.", "Data Eng · BI · ML/NLP · Security"), ("Intelligence Ops", "Social · Media · GIS · QA")]
for i, (t, d) in enumerate(units):
    x = MX + i * 3.08
    arrow(s, 6.67, 2.42, x + 1.45, 2.72, color=LINE, width=1, head=False)
    b = box(s, x, 2.75, 2.9, 0.82, fill=SURFACE, line=LINE)
    shape_text(b, [{"t": t, "bold": True, "size": 11.5, "color": NAVY}, {"t": d, "size": 9.5, "color": MUTED}])
b = box(s, 9.9, 1.8, 2.83, 0.6, fill=None, line=SAFFRON, dash=True)
shape_text(b, "Client: Political / Comms liaison", size=10, color=SAFFRON, bold=True)
sc = [("A · POC / MVP", "5–7", "4–6 weeks", ["Analytics Lead", "Data Scientist", "Data Engineer", "ML/NLP Engineer",
                                               "Data Analyst", "PM (+0.5 BI, shared Director & Security)"]),
      ("B · Single constituency / by-election", "8–15 core", "+ ops support", ["+ 2nd Data Scientist, 2–3 Analysts", "Social & Media analysts",
                                                                                  "BI Developer, QA/Data Ops", "0.5 GIS, 0.5 Security/Privacy"]),
      ("C · Multi-constituency / state", "20–50+", "24×7 war-room", ["Domain leads per module", "4–8 DS · 6–12 DA", "Language pods for social/media",
                                                                     "24×7 Data Ops rota · annotators"])]
for i, (t, n, sub, ls) in enumerate(sc):
    x = MX + i * 4.1
    box(s, x, 3.85, 3.93, 2.95, fill=SURFACE)
    text(s, x + 0.2, 3.95, 3.5, 0.4, t, size=12.5, color=NAVY, bold=True)
    text(s, x + 0.2, 4.35, 3.5, 0.55, [{"runs": [{"t": n + " ", "size": 22, "bold": True, "color": SAFFRON},
                                                 {"t": "people · " + sub, "size": 11, "color": MUTED}]}], size=11)
    text(s, x + 0.2, 5.0, 3.6, 1.8, [{"t": l, "bullet": True} for l in ls], size=11, spacing_after=2)
notes(s, "Role cards with responsibilities, skills, daily outputs, tools and experience are in PRD section 24.")

# ================================================================== 26. DATA SCIENTIST ROLE
s = frame("The Data Scientist role", "Converting data into statistically defensible decision-support")
q = box(s, MX, 1.8, 12.13, 0.85, fill=NAVY)
shape_text(q, [{"t": "“A Data Scientist is not just someone who builds ML models; the role is to convert data into statistically "
                    "defensible decision-support.”", "italic": True}], size=14, color=WHITE, margin=0.2)
cl = [("Statistics & surveys", ["Statistical analysis", "Survey analysis", "Trend detection", "Uncertainty estimation", "Bias checks"]),
      ("Forecasting & detection", ["Forecasting", "Anomaly detection", "Model validation", "Model monitoring"]),
      ("Language & AI", ["NLP", "Sentiment analysis", "Topic modelling", "AI-agent development", "RAG analytics"]),
      ("Measurement", ["Content-performance analysis", "Experiment analysis", "Attribution (where valid)", "KPI modelling"]),
      ("Trust & communication", ["Data-quality analysis", "Executive insights", "Automated reporting", "Reproducibility", "Documentation"])]
for i, (t, ls) in enumerate(cl):
    x = MX + i * 2.45
    box(s, x, 2.9, 2.3, 3.85, fill=SURFACE)
    circle(s, x + 0.18, 3.05, 0.42, fill=[NAVY, BLUE, TEAL, OCHRE, SAFFRON][i], label=str(i + 1), size=12)
    text(s, x + 0.18, 3.55, 2.0, 0.6, t, size=13, color=NAVY, bold=True)
    text(s, x + 0.18, 4.2, 2.0, 2.5, [{"t": l, "bullet": True} for l in ls], size=11, spacing_after=4)
notes(s, "23 contributions grouped into five clusters. A typical day: pipeline and alert review at 06:30, report "
         "sign-off, war-room stand-up, deep-dive analysis, model monitoring, insight note to leadership.")

# ================================================================== 27. POC PLAN
s = frame("Proof of concept", "4–6 weeks to a working Command Center on realistic DEMO data")
gx, gw = MX + 2.55, 5.4
for w_ in range(6):
    b = box(s, gx + w_ * gw / 6, 1.8, gw / 6 - 0.05, 0.38, fill=NAVY, radius=0.2)
    shape_text(b, f"W{w_ + 1}", size=10.5, color=WHITE, bold=True)
ws = [("Discovery, sources, KPIs", 0, 1, NAVY), ("Ingestion, cleaning, DB", 1, 2, BLUE), ("First dashboards", 1, 3, BLUE),
      ("NLP, survey, historical", 2, 3, TEAL), ("AI Analyst, alerts, reports", 3, 4, SAFFRON), ("Validation, security, UX", 4, 5, OCHRE),
      ("Exec demo & handover", 5, 6, NAVY)]
for i, (t, a, b_, c) in enumerate(ws):
    y = 2.35 + i * 0.6
    text(s, MX, y, 2.45, 0.45, t, size=11, color=INK, anchor="m")
    bb = box(s, gx + a * gw / 6, y + 0.07, (b_ - a) * gw / 6 - 0.05, 0.32, fill=c, radius=0.4)
text(s, MX, 6.6, 8.0, 0.3, "Demo: fictional Aranyapur AC · 100,000 synthetic records · every screen labelled DEMO DATA",
     size=10.5, color=MUTED, italic=True)
text(s, 8.85, 1.8, 3.9, 0.4, "Acceptance criteria (13)", size=15, color=NAVY, bold=True)
ac = ["Dashboards P95 < 3 s", "ETL ≥ 99% success, 5 days", "Lineage for 10/10 sampled tiles", "NLP processes 50k texts",
      "Sentiment macro-F1 ≥ 0.70 / language", "Issue detection ≥ 90% of test events", "AI: 0 fabricated numbers; 100% refusals",
      "Citations + data-as-of on every answer", "RBAC: 0 exposures in 40 tests", "Audit log captures 100% of events",
      "Daily report ≥ 70% auto-drafted", "Alerts at correct severity ≤ 5 min", "Model card for every model"]
text(s, 8.85, 2.25, 3.9, 4.6, [{"t": a, "bullet": True, "char": "✓", "bcolor": TEAL} for a in ac], size=10.5, spacing_after=2)
notes(s, "POC success means all Must criteria met and at least two of the remaining three, with a leadership usability "
         "score of at least 4 out of 5.")

# ================================================================== 28. TECHNOLOGY POC
s = frame("Technology POC", "A lean, production-ready POC stack",
          "Python · FastAPI · PostgreSQL · pgvector/FAISS · SentenceTransformers · LLM · scheduled ETL")
stack = [("Power BI / React UI  ·  Streamlit prototypes", NAVY, WHITE), ("FastAPI service — SSO token, RBAC, audit middleware", SAFFRON, WHITE),
         ("LLM + tool router (AI Analyst)  ·  report generator", SAFFRON_LT, NAVY),
         ("PostgreSQL + metric views  ·  pgvector / FAISS index", BLUE_LT, NAVY),
         ("NLP pipeline: LID → normalise → topic/sentiment/NER → embeddings", TEAL_LT, NAVY),
         ("Scheduled ETL (Dagster / cron): raw → quality tests → dbt models", SURFACE, NAVY)]
for i, (t, f, c) in enumerate(stack):
    b = box(s, MX, 1.85 + i * 0.8, 6.4, 0.68, fill=f)
    shape_text(b, t, size=11.5, color=c, bold=True)
rows = [["Method", "Endpoint", "Returns"],
        ["GET", "/dashboard/overview", "Health, domains, KPI strip"],
        ["GET", "/social/trends", "Volume, anomalies, sentiment CIs"],
        ["GET", "/media/intelligence", "Outlets, tone, threads"],
        ["GET", "/survey/summary", "Weighted estimates, MoE"],
        ["GET", "/field/operations", "Completion, bottlenecks"],
        ["GET", "/digital/scorecard", "Scorecard vs targets"],
        ["GET", "/alerts", "Alert queue"],
        ["GET", "/compliance/items", "Approval, cert, AI label"],
        ["GET", "/lineage/{metric}", "Source-to-metric graph"],
        ["POST", "/ai/query", "Facts, citations, confidence"]]
table(s, 7.3, 1.85, 5.43, rows, col_w=[0.75, 2.2, 2.48], row_h=0.44, size=10.5, colors={(r, 0): SAFFRON for r in range(1, 11)},
      bold_cells={(r, 0) for r in range(1, 11)})
notes(s, "Full OpenAPI sketch in poc/openapi.yaml and conceptual schema in poc/schema.sql.")

# ================================================================== 29. ROADMAP
s = frame("Roadmap", "30 / 60 / 90 days to a full Command Center — then the election cycle")
rm = [("30 days", "Foundation", ["Indian-region cloud, SSO/MFA/RBAC", "Source registry; 10–15 sources", "Metric store v1",
                                 "Overview, Digital, Social, Field", "Automated daily report"]),
      ("60 days", "Intelligence", ["Media, Survey, Issue, Geo modules", "Regional-language NLP", "Alert tuning; experiments",
                                   "Compliance tower v1"]),
      ("90 days", "AI + Automation", ["AI Analyst GA + eval harness", "RAG library; forecasting", "Weekly report automation",
                                      "War-room screens; DR & pen-test"])]
for i, (d, t, ls) in enumerate(rm):
    x = MX + i * 4.1
    box(s, x, 1.8, 3.93, 2.75, fill=SURFACE)
    text(s, x + 0.2, 1.9, 3.5, 0.5, [{"runs": [{"t": d + "  ", "size": 20, "bold": True, "color": SAFFRON},
                                               {"t": t, "size": 14, "bold": True, "color": NAVY}]}], size=14)
    text(s, x + 0.2, 2.5, 3.6, 2.0, [{"t": l, "bullet": True} for l in ls], size=11.5, spacing_after=3)
ph = [("Pre-campaign", "Baselines, Wave 0, taxonomy, authorisations"), ("Campaign", "Daily reports, alerts, MCC-aware workflows"),
      ("High-intensity", "Intraday refresh, 24×7 war-room, DR standby"), ("Final phase", "Silence-period guard; no publishing workflows"),
      ("Poll day", "Operational analytics, incidents, misinformation-risk triage"), ("Post-poll", "Measurement, spend reconciliation, deletion")]
for i, (t, d) in enumerate(ph):
    x = MX + i * 2.03
    c = shape(s, MSO_SHAPE.CHEVRON if i else MSO_SHAPE.PENTAGON, x, 4.85, 2.1, 0.7, fill=[NAVY, NAVY2, BLUE, TEAL, OCHRE, SAFFRON][i])
    shape_text(c, t, size=11.5, color=WHITE, bold=True)
    text(s, x + 0.1, 5.7, 1.85, 1.1, d, size=10.5, color=INK)
notes(s, "Poll-day and post-poll work is limited to operational analytics, compliance and measurement.")

# ================================================================== 30. COMMERCIAL MODEL
s = frame("Commercial model", "Transparent components across three tiers (indicative INR, excl. GST)")
rows = [["Component", "Starter", "Professional", "Enterprise"],
        ["Typical scope", "1 AC / by-election, 8–12 wks", "1 PC or ≤ 10 ACs, 3–6 months", "Multi-constituency / state"],
        ["Core team", "6–8 FTE", "12–15 FTE", "30–60 FTE"],
        ["POC (4–6 weeks)", "₹18–35 lakh", "₹18–35 lakh", "₹25–45 lakh"],
        ["One-time setup", "₹15–30 lakh", "₹40–80 lakh", "₹1.2–3.0 crore"],
        ["Monthly analytics retainer", "₹12–22 lakh", "₹30–50 lakh", "₹0.8–2.0 crore"],
        ["Technology / platform fee (monthly)", "₹1.5–3 lakh", "₹4–8 lakh", "₹10–25 lakh"],
        ["Cloud / API (monthly, pass-through)", "₹0.5–1.5 lakh", "₹2–6 lakh", "₹8–30 lakh"],
        ["24×7 war-room (per pod / month)", "Optional ₹8–12 lakh", "₹10–15 lakh", "Included"],
        ["Survey vendor · field enablement · custom AI · travel", "Quoted / at actuals", "Quoted / at actuals", "Quoted / at actuals"]]
fl = {(r, 2): SAFFRON_LT for r in range(1, 10)}
table(s, MX, 1.8, 12.13, rows, col_w=[3.9, 2.6, 2.9, 2.73], row_h=0.44, size=11.5, first_col_bold=True, fills=fl)
b = box(s, MX, 6.35, 12.13, 0.5, fill=SURFACE)
shape_text(b, "Indicative only; final commercial proposal depends on constituency, election timeline, data availability, "
              "staffing, SLA and technology requirements.", size=11, color=MUTED, bold=True)
notes(s, "Worked example (Professional, four months): about 3.2 crore rupees, range roughly 2.3 to 4.5 crore. POC fee "
         "50% creditable against setup if contracted within 30 days.")

# ================================================================== 31. KPIs & VALUE
s = frame("KPIs & value", "We measure what the platform can credibly change — not election outcomes")
b = box(s, 1.9, 1.85, 3.2, 0.62, fill=NAVY)
shape_text(b, "Campaign Intelligence Health", size=12, color=WHITE, bold=True)
l2 = ["Digital", "Social", "Media", "Survey", "Field", "Operations", "Data Quality", "Compliance"]
for i, t in enumerate(l2):
    x = MX + (i % 4) * 1.46
    y = 2.85 + (i // 4) * 0.75
    arrow(s, 3.5, 2.48, x + 0.68, y, color=LINE, width=0.75, head=False)
    b = box(s, x, y, 1.36, 0.55, fill=SAFFRON_LT if t in ("Data Quality", "Compliance") else SURFACE)
    shape_text(b, t, size=10.5, color=NAVY, bold=True)
text(s, MX, 4.5, 5.8, 2.3, [
    {"runs": [{"t": "Leading: ", "bold": True}, {"t": "issue velocity, ER, field completion, alert ack time"}], "bullet": True},
    {"runs": [{"t": "Lagging: ", "bold": True}, {"t": "survey awareness, cumulative reach"}], "bullet": True},
    {"runs": [{"t": "Diagnostic: ", "bold": True}, {"t": "platform, format, theme, zone mix"}], "bullet": True},
    {"runs": [{"t": "Data-quality: ", "bold": True}, {"t": "freshness, coverage, test pass rate, n_eff"}], "bullet": True},
], size=11.5, spacing_after=5)
vals = [("−60%", "analyst time on recurring reports"), ("≥ 70%", "report content auto-generated"),
        ("≤ 2 h", "issue onset → alert (priority sources)"), ("100%", "paid / AI items with complete compliance record"),
        ("≥ 80%", "weekly active leadership users"), ("≥ 95%", "field activities with structured reports")]
for i, (v, l) in enumerate(vals):
    x = 6.9 + (i % 2) * 2.95
    y = 1.85 + (i // 2) * 1.65
    kpi_card(s, x, y, 2.83, 1.5, v, l, vsize=26)
notes(s, "Value is measured against a Week-1 baseline. We never claim guaranteed victory or guaranteed ROI.")

# ================================================================== 32. RISKS
s = frame("Risks & mitigation", "Named owners, explicit mitigations — no surprises")
gx0, gy0, cw, chh = 1.55, 1.85, 1.7, 1.45
for r_ in range(3):
    for c_ in range(3):
        sev = (2 - r_) + c_
        f = [GREEN_LT, AMBER_LT, SAFFRON_LT, RED_LT, RED_LT][sev]
        box(s, gx0 + c_ * (cw + 0.06), gy0 + r_ * (chh + 0.06), cw, chh, fill=f, radius=0.04)
cells = {(0, 0): "R17", (0, 1): "R7 R11\nR12 R13", (1, 1): "R3 R4\nR10 R18", (1, 2): "R1 R14", (2, 1): "R6 R8\nR15 R16",
         (2, 2): "R2 R5 R9"}
for (r_, c_), t in cells.items():
    text(s, gx0 + c_ * (cw + 0.06), gy0 + r_ * (chh + 0.06), cw, chh, [{"t": ln_, "align": "c"} for ln_ in t.split("\n")],
         size=12, color=NAVY, bold=True, align="c", anchor="m")
for i, t in enumerate(["High", "Medium", "Low"]):
    text(s, MX, gy0 + i * (chh + 0.06), 0.9, chh, t, size=10, color=MUTED, anchor="m", align="r")
for i, t in enumerate(["Low", "Medium", "High"]):
    text(s, gx0 + i * (cw + 0.06), gy0 + 3 * (chh + 0.06), cw, 0.3, t, size=10, color=MUTED, align="c")
text(s, MX, 6.55, 6.2, 0.3, "Rows: impact · Columns: probability  (full 18-risk register in PRD §30)", size=10, color=MUTED, italic=True)
rows = [["Risk", "Mitigation", "Owner"],
        ["R1 Poor data quality", "Quality gates, badges, data-ops rota", "Data Eng Lead"],
        ["R5 Social ≠ electorate", "Coverage index, caveats, triangulation", "Analytics Lead"],
        ["R7 LLM hallucination", "Tool-first, numeric & citation checks", "ML Lead"],
        ["R11 Compliance breach", "Blocking rules, legal sign-off", "Compliance"],
        ["R12 Privacy", "Minimisation, purpose tags, audits", "Privacy Lead"],
        ["R13 Cyber", "SSO/MFA, least privilege, pen-test", "Security Lead"],
        ["R14 Expectations", "Explicit non-promises, acceptance criteria", "Programme Dir."]]
table(s, 7.2, 1.85, 5.53, rows, col_w=[1.85, 2.4, 1.28], row_h=0.58, size=10.5, first_col_bold=True)
notes(s, "Top risks are data quality, representativeness of social data, hallucination, compliance, privacy, cyber and "
         "unrealistic expectations.")

# ================================================================== 33. BOUNDARIES & DEPENDENCIES
s = frame("Boundaries & dependencies", "Clear expectations protect the campaign, the agency and the partner")
nop = ["Guaranteed election outcome", "Exact vote prediction", "Complete voter-preference prediction",
       "Individual political-belief inference", "Unauthorised personal-data access", "Secret tracking",
       "Illegal scraping", "Private-message monitoring", "Guaranteed viral content", "Guaranteed persuasion", "Guaranteed ROI"]
box(s, MX, 1.8, 5.9, 5.0, fill=RED_LT)
text(s, MX + 0.25, 1.92, 5.4, 0.4, "What we will not promise", size=15, color=RED, bold=True)
text(s, MX + 0.25, 2.45, 5.5, 4.3, [{"t": t, "bullet": True, "char": "✕", "bcolor": RED} for t in nop], size=14, spacing_after=6)
dep = ["Campaign scope, geography, timeline", "Existing data & authorised first-party data", "API / dashboard access for owned accounts",
       "Survey data & methodology", "Field report formats & media-monitoring access", "Named compliance & legal contacts",
       "Cloud preference & security requirements", "Reporting cadence, decision-makers, SLA", "Language priorities & annotators",
       "Brand assets — only with authorisation"]
box(s, 6.83, 1.8, 5.9, 5.0, fill=TEAL_LT)
text(s, 7.08, 1.92, 5.4, 0.4, "What we need from you", size=15, color=TEAL, bold=True)
text(s, 7.08, 2.45, 5.5, 4.3, [{"t": t, "bullet": True, "char": "✓", "bcolor": TEAL} for t in dep], size=14, spacing_after=8)
notes(s, "These lists go into the statement of work. Most are needed in Week 1 of the POC.")

# ================================================================== 34. CLOSING
s = base(dark=True)
image(s, chart_img("cover_network.png"), 0, 0, w=W, h=H)
veil(s, 0, 0, W, H, alpha=55000)
text(s, MX, 0.9, 8.5, 1.5, "From Campaign Data to Campaign Intelligence", size=38, color=WHITE, bold=True, line_spacing=0.95)
text(s, MX, 2.45, 8.0, 0.6, "Unified data. Trusted analytics. AI-assisted intelligence. Faster decisions.", size=18, color="F28C28")
fin = [("Platform", "Command Center, AI Analyst, alerts, compliance tower"), ("Team", "Data scientists, engineers, analysts — sized to the election"),
       ("Technology", "Governed warehouse, multilingual NLP, grounded AI"), ("Governance", "Privacy by design, audit trails, responsible AI"),
       ("Measurable outcomes", "Faster reporting, earlier detection, better data")]
for i, (t, d) in enumerate(fin):
    x = MX + i * 2.45
    b = box(s, x, 3.7, 2.3, 1.9, fill="10284A", line="2B4A78")
    text(s, x + 0.18, 3.85, 2.0, 0.4, t, size=13, color=GOLD, bold=True)
    text(s, x + 0.18, 4.5, 2.0, 1.05, d, size=11.5, color="DCE3EE")
text(s, MX, 5.95, 9.0, 0.5, "Next step: approve a 4–6 week POC with 13 measurable acceptance criteria.", size=14, color=WHITE, bold=True)
text(s, MX, 6.45, 9.0, 0.4, "No guaranteed outcomes — guaranteed rigour, transparency and accountability.", size=12, color="8FA3C0", italic=True)
notes(s, "Close on the ask: a time-boxed POC with measurable acceptance criteria.")

# ================================================================== 35. SOURCES
s = frame("Sources & notes", "Key references (full list with URLs and dates in PRD Appendix A)")
left = ["ECI press note on political advertising & digital campaigning — 20 Mar 2026 (as reported by ANI / Akashvani)",
        "ECI: print-ad pre-certification — 6 Apr 2026 (Akashvani)",
        "ECI advisory: labelling AI-generated / synthetic content — 24 Oct 2025 (Business Today, ANI)",
        "ECI advisories: 16 Jan 2025 (labelling); 6 May 2024 (deepfakes, 3-hour removal)",
        "ECI instructions on social media — 25 Oct 2013; ECI FAQ on social media",
        "RP Act 1951 ss. 77, 126, 126A (India Code); Committee on s.126 report — Jan 2019",
        "MeitY IT Amendment Rules 2026 — notified 10 Feb, in force 20 Feb 2026",
        "DPDP Act 2023; DPDP Rules 2025 — notified 14 Nov 2025 (phased to 14 May 2027)",
        "CERT-In Directions — 28 Apr 2022; MeitY India AI Governance Guidelines — 5 Nov 2025"]
right = ["ECI Statistical Reports; PIB on ECINET index cards (2026); TCPD Lok Dhaba; Census 2027 (PIB, Apr 2026)",
         "Meta Graph / Instagram Platform / Ad Library docs; Meta Content Library; CrowdTangle closure 14 Aug 2024",
         "YouTube Data & Analytics APIs; X API pay-per-use (2026); Google Trends API alpha (24 Jul 2025)",
         "Google political content policy & India pre-certificate requirement; Meta SIEP policy",
         "AI4Bharat IndicTrans2 & IndicBERT (MIT); MuRIL; NIST AI RMF; ISO/IEC 42001",
         "Visuals: all charts and cover generated for this deck from synthetic data; no third-party images"]
text(s, MX, 1.8, 6.0, 4.6, [{"t": "LEGAL & REGULATORY", "bold": True, "color": SAFFRON, "size": 11}] +
     [{"t": t, "bullet": True, "size": 12} for t in left], size=12, spacing_after=6)
text(s, 6.85, 1.8, 5.88, 4.6, [{"t": "DATA · TECHNICAL · AI/ML · DESIGN", "bold": True, "color": SAFFRON, "size": 11}] +
     [{"t": t, "bullet": True, "size": 12} for t in right], size=12, spacing_after=6)
b = box(s, MX, 6.15, 12.13, 0.68, fill=SURFACE)
shape_text(b, "This is an analytics/technology proposal, not legal advice. Final campaign compliance should be reviewed by the "
              "campaign's authorised legal/compliance team. DEMO DATA is synthetic. Party marks are placeholders unless authorised.",
           size=10.5, color=NAVY, bold=True, align="l", margin=0.15)
notes(s, "Several ECI items were verified through reputable reporting of the press notes; confirm against the primary "
         "ECI documents before reliance.")

path = os.path.join(OUT, "Election_Intelligence_Command_Center_Executive_Deck.pptx")
prs.save(path)
print("saved", path, "slides:", state["n"])
