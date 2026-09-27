"""
Synthetic DEMO data generator for the Election Intelligence & Analytics Command Center POC.

EVERYTHING PRODUCED HERE IS SYNTHETIC ("DEMO DATA").
- The constituency ("Aranyapur", fictional) and all zones, outlets and events are invented.
- No real voter roll, no real person, no real account and no scraped data is used.
- No record stores or infers any individual's political belief, preference or vote intention.
  Survey records are anonymous, consented-style issue/awareness/satisfaction responses in coarse
  demographic bins, used only for weighted aggregate estimates.

Output: demo/data/*.csv (git-ignored; regenerate deterministically with this script).
Run:    python demo/generate_synthetic_data.py
"""
from __future__ import annotations

import os
from datetime import date, timedelta

import numpy as np
import pandas as pd

SEED = 20260927
rng = np.random.default_rng(SEED)
OUT = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUT, exist_ok=True)

START = date(2026, 8, 1)
DAYS = 42  # six-week demo window
DATES = [START + timedelta(days=i) for i in range(DAYS)]

CONSTITUENCY = "Aranyapur AC (FICTIONAL - DEMO)"
BLOCKS = ["North Block", "River Block", "Market Block", "Hill Block"]
ZONES = [f"Z{i:02d}" for i in range(1, 25)]
ZONE_BLOCK = {z: BLOCKS[(i) // 6] for i, z in enumerate(ZONES)}
ZONE_URBAN = {z: ("Urban" if ZONE_BLOCK[z] == "Market Block" or i % 5 == 0 else "Rural")
              for i, z in enumerate(ZONES)}

ISSUES = ["Water supply", "Roads & transport", "Jobs & skills", "Prices", "Health services",
          "Education", "Electricity", "Agriculture", "Public safety"]
ISSUE_BASE = np.array([0.14, 0.13, 0.15, 0.13, 0.11, 0.09, 0.09, 0.10, 0.06])
LANGS = ["Hindi", "English", "Hinglish", "Regional language", "Romanized regional"]
LANG_P = [0.38, 0.17, 0.27, 0.11, 0.07]
PLATFORMS = ["Facebook", "Instagram", "YouTube", "X", "News comments"]
PLAT_P = [0.30, 0.22, 0.18, 0.20, 0.10]

SPIKE_DAY = 30          # synthetic event: water-pipeline outage story breaks on day 31
SPIKE_TOPIC = "Water supply"


def day_weights() -> np.ndarray:
    base = 1200 + 12 * np.arange(DAYS)                 # gentle upward campaign trend
    weekly = 1 + 0.12 * np.sin(2 * np.pi * np.arange(DAYS) / 7)
    w = base * weekly
    w[SPIKE_DAY] *= 2.6
    w[SPIKE_DAY + 1] *= 1.9
    w[SPIKE_DAY + 2] *= 1.35
    return w / w.sum()


def social_mentions(n: int = 60_000) -> pd.DataFrame:
    d_idx = rng.choice(DAYS, size=n, p=day_weights())
    topic = rng.choice(ISSUES, size=n, p=ISSUE_BASE / ISSUE_BASE.sum())
    spike_mask = (d_idx >= SPIKE_DAY) & (d_idx <= SPIKE_DAY + 2) & (rng.random(n) < 0.55)
    topic = np.where(spike_mask, SPIKE_TOPIC, topic)
    # sentiment in [-1, 1]; topic-specific means; spike is negative
    t_mean = {t: m for t, m in zip(ISSUES, [-0.10, -0.18, -0.05, -0.22, -0.08, 0.06, -0.12, 0.02, -0.15])}
    mu = np.array([t_mean[t] for t in topic])
    mu = np.where(spike_mask, -0.45, mu)
    sent = np.clip(rng.normal(mu, 0.45), -1, 1)
    label = np.where(sent > 0.2, "Positive", np.where(sent < -0.2, "Negative", "Neutral"))
    geo = rng.random(n) < 0.18  # only ~18% of public posts carry usable coarse location
    zone = np.where(geo, rng.choice(ZONES, size=n), None)
    df = pd.DataFrame({
        "mention_id": [f"SM{i:06d}" for i in range(n)],
        "date": [DATES[i] for i in d_idx],
        "platform": rng.choice(PLATFORMS, size=n, p=PLAT_P),
        "language": rng.choice(LANGS, size=n, p=LANG_P),
        "topic": topic,
        "sentiment_score": sent.round(3),
        "sentiment_label": label,
        "classifier_confidence": np.clip(rng.beta(6, 2, size=n), 0.35, 0.99).round(3),
        "engagement": rng.negative_binomial(2, 0.04, size=n),
        "zone_if_public": zone,
        "is_near_duplicate": rng.random(n) < 0.07,
        "source_type": "Permitted API / licensed listening tool (SYNTHETIC)",
    })
    return df


def media_mentions(n: int = 6_000) -> pd.DataFrame:
    outlets = ["National daily", "Regional daily", "Regional TV (licensed transcript)",
               "Digital news", "Hyperlocal portal", "YouTube news channel"]
    d_idx = rng.choice(DAYS, size=n, p=day_weights())
    topic = rng.choice(ISSUES, size=n, p=ISSUE_BASE / ISSUE_BASE.sum())
    spike = (d_idx >= SPIKE_DAY) & (d_idx <= SPIKE_DAY + 3) & (rng.random(n) < 0.45)
    topic = np.where(spike, SPIKE_TOPIC, topic)
    tone = rng.choice(["Positive", "Neutral", "Negative"], size=n, p=[0.24, 0.51, 0.25])
    tone = np.where(spike & (rng.random(n) < 0.6), "Negative", tone)
    return pd.DataFrame({
        "article_id": [f"MM{i:05d}" for i in range(n)],
        "date": [DATES[i] for i in d_idx],
        "outlet_type": rng.choice(outlets, size=n, p=[0.12, 0.30, 0.10, 0.25, 0.13, 0.10]),
        "language": rng.choice(["Hindi", "English", "Regional language"], size=n, p=[0.5, 0.25, 0.25]),
        "topic": topic,
        "tone": tone,
        "reach_tier": rng.choice(["High", "Medium", "Low"], size=n, p=[0.15, 0.40, 0.45]),
        "mentions_campaign_org": rng.random(n) < 0.42,
    })


def survey_responses(n_per_wave: int = 4_000) -> pd.DataFrame:
    """Anonymous issue/awareness/satisfaction survey. No vote-intention or belief questions."""
    frames = []
    # "population" shares used for post-stratification (synthetic census-style margins)
    for wave, wave_date in zip([1, 2, 3], [DATES[6], DATES[20], DATES[34]]):
        n = n_per_wave
        age = rng.choice(["18-29", "30-44", "45-59", "60+"], size=n, p=[0.36, 0.30, 0.20, 0.14])
        gender = rng.choice(["Female", "Male"], size=n, p=[0.42, 0.58])  # deliberately skewed sample
        zone = rng.choice(ZONES, size=n)
        p_issue = ISSUE_BASE.copy()
        if wave == 3:                         # water-supply salience rises after the synthetic outage
            p_issue[0] += 0.07
            p_issue[3] -= 0.02
        if wave >= 2:
            p_issue[2] += 0.02
        top_issue = rng.choice(ISSUES, size=n, p=p_issue / p_issue.sum())
        aware = rng.random(n) < (0.31 + 0.07 * (wave - 1))
        sat = np.clip(np.round(rng.normal(3.0 - 0.1 * (wave == 3), 1.0, size=n)), 1, 5).astype(int)
        duration = rng.gamma(9, 55, size=n)
        speeder = duration < 180
        straight = rng.random(n) < 0.03
        frames.append(pd.DataFrame({
            "response_id": [f"W{wave}R{i:05d}" for i in range(n)],
            "wave": wave,
            "fieldwork_date": wave_date,
            "mode": rng.choice(["CATI", "Face-to-face (tablet)", "Online panel"], size=n, p=[0.5, 0.35, 0.15]),
            "age_band": age,
            "gender": gender,
            "zone": zone,
            "area_type": [ZONE_URBAN[z] for z in zone],
            "top_issue": top_issue,
            "aware_of_campaign_programme": aware,
            "local_services_satisfaction_1to5": sat,
            "interview_seconds": duration.round(0),
            "qc_speeder": speeder,
            "qc_straightliner": straight,
            "consent_recorded": True,
        }))
    df = pd.concat(frames, ignore_index=True)
    # post-stratification weights to synthetic population margins (age x gender)
    pop = {("18-29", "Female"): 0.17, ("18-29", "Male"): 0.18, ("30-44", "Female"): 0.15,
           ("30-44", "Male"): 0.15, ("45-59", "Female"): 0.10, ("45-59", "Male"): 0.10,
           ("60+", "Female"): 0.08, ("60+", "Male"): 0.07}
    df["weight"] = 1.0
    for w in df.wave.unique():
        m = df.wave == w
        cell = df[m].groupby(["age_band", "gender"]).size() / m.sum()
        df.loc[m, "weight"] = [pop[(a, g)] / cell[(a, g)] for a, g in zip(df.loc[m, "age_band"], df.loc[m, "gender"])]
    df["weight"] = df["weight"].clip(0.3, 3.0).round(4)  # trimmed weights
    return df


def field_activities(n: int = 9_000) -> pd.DataFrame:
    types = ["Community meeting", "Public event", "Information camp", "Volunteer training",
             "Grievance desk", "Material distribution check"]
    zone = rng.choice(ZONES, size=n)
    block = np.array([ZONE_BLOCK[z] for z in zone])
    comp_p = np.where(block == "Hill Block", 0.71, np.where(block == "River Block", 0.83, 0.90))
    completed = rng.random(n) < comp_p
    on_time = rng.random(n) < np.where(block == "Hill Block", 0.62, 0.86)
    return pd.DataFrame({
        "activity_id": [f"FA{i:05d}" for i in range(n)],
        "date": [DATES[i] for i in rng.integers(0, DAYS, size=n)],
        "zone": zone,
        "block": block,
        "activity_type": rng.choice(types, size=n, p=[0.25, 0.12, 0.2, 0.13, 0.18, 0.12]),
        "planned": True,
        "completed": completed,
        "attendance_headcount": np.where(completed, rng.poisson(45, size=n), 0),
        "issue_reports_logged": np.where(completed, rng.poisson(1.4, size=n), 0),
        "report_submitted_on_time": on_time,
        "report_quality_score": np.clip(rng.normal(np.where(on_time, 0.86, 0.68), 0.08), 0, 1).round(2),
    })


def content_posts(n: int = 1_500) -> pd.DataFrame:
    fmt = rng.choice(["Short video", "Long video", "Carousel", "Static image", "Text post", "Live stream"],
                     size=n, p=[0.3, 0.1, 0.15, 0.25, 0.12, 0.08])
    topic = rng.choice(["Development work", "Public services", "Youth & jobs", "Women's welfare",
                        "Agriculture", "Event coverage", "Explainer / FAQ"], size=n)
    platform = rng.choice(["Facebook", "Instagram", "YouTube", "X"], size=n, p=[0.3, 0.3, 0.2, 0.2])
    fmt_mult = {"Short video": 1.6, "Long video": 0.9, "Carousel": 1.25, "Static image": 0.85,
                "Text post": 0.6, "Live stream": 1.05}
    top_mult = {"Development work": 1.0, "Public services": 1.1, "Youth & jobs": 1.3, "Women's welfare": 1.15,
                "Agriculture": 0.95, "Event coverage": 0.8, "Explainer / FAQ": 1.2}
    impressions = rng.lognormal(10.2, 0.8, size=n).astype(int)
    er = np.clip(0.028 * np.array([fmt_mult[f] * top_mult[t] for f, t in zip(fmt, topic)])
                 * rng.lognormal(0, 0.35, size=n), 0.001, 0.25)
    engagements = (impressions * er).astype(int)
    video = np.isin(fmt, ["Short video", "Long video", "Live stream"])
    boosted = rng.random(n) < 0.35
    spend = np.where(boosted, rng.gamma(3, 1500, size=n), 0).round(0)
    clicks = (impressions * np.clip(rng.normal(0.011, 0.004, size=n), 0.001, 0.05)).astype(int)
    return pd.DataFrame({
        "content_id": [f"CT{i:04d}" for i in range(n)],
        "publish_date": [DATES[i] for i in rng.integers(0, DAYS, size=n)],
        "publish_hour": rng.choice(range(6, 23), size=n),
        "platform": platform,
        "format": fmt,
        "topic": topic,
        "language": rng.choice(["Hindi", "English", "Hinglish", "Regional language"], size=n, p=[0.45, 0.15, 0.25, 0.15]),
        "length_seconds_or_words": np.where(video, rng.integers(15, 900, size=n), rng.integers(20, 400, size=n)),
        "impressions": impressions,
        "reach": (impressions * rng.uniform(0.55, 0.85, size=n)).astype(int),
        "engagements": engagements,
        "shares": (engagements * rng.uniform(0.05, 0.2, size=n)).astype(int),
        "comments": (engagements * rng.uniform(0.03, 0.12, size=n)).astype(int),
        "video_views": np.where(video, (impressions * rng.uniform(0.2, 0.5, size=n)).astype(int), 0),
        "avg_watch_pct": np.where(video, rng.beta(3, 5, size=n).round(3), np.nan),
        "clicks": clicks,
        "boosted": boosted,
        "spend_inr": spend,
        "ad_precertification_ref": np.where(boosted, [f"MCMC-DEMO-{i:04d}" for i in range(n)], None),
        "ai_content_flag": rng.random(n) < 0.08,
    })


def call_centre(n: int = 11_500) -> pd.DataFrame:
    d_idx = rng.choice(DAYS, size=n, p=day_weights())
    cat = rng.choice(["Service request", "Event information", "Grievance", "Volunteer enquiry",
                      "Feedback", "Other"], size=n, p=[0.3, 0.18, 0.22, 0.1, 0.12, 0.08])
    answered = rng.random(n) < np.where(d_idx >= SPIKE_DAY, 0.84, 0.92)
    return pd.DataFrame({
        "call_id": [f"CC{i:05d}" for i in range(n)],
        "date": [DATES[i] for i in d_idx],
        "language": rng.choice(["Hindi", "English", "Regional language"], size=n, p=[0.6, 0.1, 0.3]),
        "category": cat,
        "zone": rng.choice(ZONES, size=n),
        "answered": answered,
        "wait_seconds": np.where(answered, rng.gamma(2, 22, size=n), rng.gamma(4, 30, size=n)).round(0),
        "resolved_first_contact": answered & (rng.random(n) < 0.68),
        "follow_up_required": rng.random(n) < 0.21,
        "agent_id": rng.choice([f"AG{i:02d}" for i in range(1, 19)], size=n),
        "qa_score": np.clip(rng.normal(0.82, 0.08, size=n), 0, 1).round(2),
        "caller_pii_stored": False,  # POC stores no caller identifiers
    })


def main() -> None:
    tables = {
        "social_mentions": social_mentions(),
        "media_mentions": media_mentions(),
        "survey_responses": survey_responses(),
        "field_activities": field_activities(),
        "content_posts": content_posts(),
        "call_centre": call_centre(),
    }
    total = 0
    for name, df in tables.items():
        df.insert(0, "data_label", "DEMO DATA - SYNTHETIC")
        df.to_csv(os.path.join(OUT, f"{name}.csv"), index=False)
        total += len(df)
        print(f"{name:18s} {len(df):>7,d} rows")
    print(f"{'TOTAL':18s} {total:>7,d} rows  ({CONSTITUENCY})")


if __name__ == "__main__":
    main()
