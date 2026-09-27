"""
Builds DEMO analytics (metrics.json) and chart images from the synthetic dataset.
All outputs are watermarked "DEMO DATA - SYNTHETIC". Run after generate_synthetic_data.py.
"""
from __future__ import annotations

import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import RegularPolygon

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "data")
OUT = os.path.join(HERE, "charts")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)

# Palette (validated with the dataviz validator, light surface)
SAFFRON, BLUE, TEAL, OCHRE = "#E2711D", "#2F6DB5", "#1A9A8F", "#A67C1A"
NAVY, INK, MUTED, GRID = "#0B1F3A", "#1B2330", "#5B6573", "#E3E6EA"
NEG, POS, NEUTRAL = "#C4501A", "#2F6DB5", "#B9BEC6"
SEQ = ["#FCE9DA", "#F7C9A2", "#EFA066", "#E2711D", "#B4540F", "#7A3606"]

plt.rcParams.update({
    "font.family": "Liberation Sans", "font.size": 10, "axes.edgecolor": GRID,
    "axes.labelcolor": MUTED, "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
    "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
    "axes.titleweight": "bold", "axes.titlesize": 12, "axes.titlecolor": INK,
    "figure.dpi": 200, "savefig.bbox": "tight", "savefig.facecolor": "white",
})


def stamp(fig, note="DEMO DATA - SYNTHETIC - fictional constituency", y=-0.035):
    fig.text(0.995, y, note, ha="right", va="top", fontsize=7, color=MUTED, style="italic")


def load(name, dates=("date",)):
    df = pd.read_csv(os.path.join(DATA, f"{name}.csv"))
    for c in dates:
        if c in df:
            df[c] = pd.to_datetime(df[c])
    return df


sm = load("social_mentions")
mm = load("media_mentions")
sv = load("survey_responses", dates=("fieldwork_date",))
fa = load("field_activities")
ct = load("content_posts", dates=("publish_date",))
cc = load("call_centre")
metrics: dict = {"label": "DEMO DATA - SYNTHETIC", "constituency": "Aranyapur AC (fictional)"}

# ---------------------------------------------------------------- 1. Social volume + anomaly band
sm_d = sm[~sm.is_near_duplicate]
daily = sm_d.groupby("date").size()
med = daily.rolling(7, min_periods=4).median().shift(1)
mad = (daily - med).abs().rolling(14, min_periods=5).median().shift(1)
upper = med + 3 * 1.4826 * mad
anom = daily[(daily > upper)]
fig, ax = plt.subplots(figsize=(8, 3.2))
ax.fill_between(daily.index, (med - 3 * 1.4826 * mad), upper, color=BLUE, alpha=0.12, lw=0,
                label="Expected range (rolling median ± 3 robust SD)")
ax.plot(daily.index, daily.values, color=BLUE, lw=2, label="De-duplicated mentions / day")
ax.scatter(anom.index, anom.values, s=60, color=SAFFRON, zorder=5, edgecolor="white", lw=1.5,
           label="Anomaly flagged")
if len(anom):
    a0 = anom.index[0]
    ax.annotate("Spike: 'Water supply'\nHigh alert → analyst review", xy=(a0, anom.iloc[0]),
                xytext=(a0 + pd.Timedelta(days=2.5), anom.iloc[0] * 0.86), color=INK, fontsize=9,
                arrowprops=dict(arrowstyle="-", color=MUTED))
ax.set_title("Social mention volume with anomaly detection")
ax.set_ylabel("Mentions / day")
ax.legend(loc="upper left", frameon=False, fontsize=8)
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d %b"))
stamp(fig)
fig.savefig(os.path.join(OUT, "social_volume_anomaly.png"))
plt.close(fig)
metrics["social"] = {
    "total_mentions_raw": int(len(sm)), "near_duplicates_removed": int(sm.is_near_duplicate.sum()),
    "last7_avg": round(float(daily[-7:].mean()), 0), "prev7_avg": round(float(daily[-14:-7].mean()), 0),
    "anomaly_dates": [d.strftime("%Y-%m-%d") for d in anom.index],
    "geo_coverage_pct": round(100 * sm.zone_if_public.notna().mean(), 1),
    "negative_share_pct": round(100 * (sm_d.sentiment_label == "Negative").mean(), 1),
    "positive_share_pct": round(100 * (sm_d.sentiment_label == "Positive").mean(), 1),
}

# ---------------------------------------------------------------- 2. Net sentiment by topic with bootstrap CI
rows = []
for t, g in sm_d.groupby("topic"):
    v = np.where(g.sentiment_label == "Positive", 1, np.where(g.sentiment_label == "Negative", -1, 0))
    boots = [rng.choice(v, size=len(v)).mean() for _ in range(300)]
    rows.append((t, v.mean() * 100, np.percentile(boots, 2.5) * 100, np.percentile(boots, 97.5) * 100, len(v)))
st = pd.DataFrame(rows, columns=["topic", "net", "lo", "hi", "n"]).sort_values("net")
fig, ax = plt.subplots(figsize=(8, 3.6))
for i, r in enumerate(st.itertuples()):
    c = NEG if r.net < -5 else (POS if r.net > 5 else MUTED)
    ax.plot([r.lo, r.hi], [i, i], color=c, lw=2)
    ax.scatter([r.net], [i], color=c, s=40, zorder=3)
    ax.text(max(r.hi, 0) + 1, i, f"{r.net:+.0f}  (n={r.n:,})", va="center", fontsize=8, color=INK)
ax.axvline(0, color=MUTED, lw=1)
ax.set_yticks(range(len(st)))
ax.set_yticklabels(st.topic)
ax.set_xlabel("Net sentiment (% positive − % negative), 95% bootstrap interval")
ax.set_title("Net sentiment by topic — public social data only (not representative of electorate)")
ax.set_xlim(min(st.lo) - 5, max(st.hi) + 22)
stamp(fig)
fig.savefig(os.path.join(OUT, "sentiment_by_topic_ci.png"))
plt.close(fig)

# ---------------------------------------------------------------- 3. Survey issue salience (weighted, CI with Kish deff)
sv_q = sv[~sv.qc_speeder & ~sv.qc_straightliner]
res = []
for w, g in sv_q.groupby("wave"):
    wt = g.weight.values
    n_eff = wt.sum() ** 2 / (wt ** 2).sum()
    for t in ["Water supply", "Jobs & skills", "Roads & transport", "Prices", "Health services"]:
        p = (wt * (g.top_issue == t)).sum() / wt.sum()
        moe = 1.96 * np.sqrt(p * (1 - p) / n_eff)
        res.append((w, t, p * 100, moe * 100, len(g), n_eff))
sr = pd.DataFrame(res, columns=["wave", "issue", "p", "moe", "n", "n_eff"])
fig, ax = plt.subplots(figsize=(8, 3.4))
issues = sr.issue.unique()
x = np.arange(len(issues))
for k, (w, col) in enumerate([(1, "#9DB6D8"), (2, BLUE), (3, SAFFRON)]):
    s = sr[sr.wave == w].set_index("issue").loc[issues]
    ax.bar(x + (k - 1) * 0.26, s.p, width=0.24, color=col, label=f"Wave {w}", edgecolor="white", lw=1)
    ax.errorbar(x + (k - 1) * 0.26, s.p, yerr=s.moe, fmt="none", ecolor=INK, elinewidth=1, capsize=2)
ax.set_xticks(x)
ax.set_xticklabels(issues)
ax.set_ylabel("Weighted % naming as top local issue")
ax.set_title("Survey: top local issue by wave (weighted, 95% CI incl. design effect)")
ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper right")
stamp(fig)
fig.savefig(os.path.join(OUT, "survey_issue_salience.png"))
plt.close(fig)
w1 = sr[(sr.wave == 1) & (sr.issue == "Water supply")].iloc[0]
w3 = sr[(sr.wave == 3) & (sr.issue == "Water supply")].iloc[0]
diff = w3.p - w1.p
se = np.sqrt((w1.moe / 1.96) ** 2 + (w3.moe / 1.96) ** 2)
metrics["survey"] = {
    "waves": 3, "responses_total": int(len(sv)), "responses_after_qc": int(len(sv_q)),
    "qc_excluded_pct": round(100 * (1 - len(sv_q) / len(sv)), 1),
    "wave3_n": int(w3.n), "wave3_n_eff": int(w3.n_eff),
    "water_w1_pct": round(w1.p, 1), "water_w3_pct": round(w3.p, 1), "water_w3_moe": round(w3.moe, 1),
    "water_change_pts": round(diff, 1), "water_change_z": round(diff / se, 2),
    "awareness_w1_pct": round(100 * np.average(sv_q[sv_q.wave == 1].aware_of_campaign_programme, weights=sv_q[sv_q.wave == 1].weight), 1),
    "awareness_w3_pct": round(100 * np.average(sv_q[sv_q.wave == 3].aware_of_campaign_programme, weights=sv_q[sv_q.wave == 3].weight), 1),
}

# ---------------------------------------------------------------- 4. Content performance matrix
ct["er"] = ct.engagements / ct.impressions
mat = ct.pivot_table(index="format", columns="topic", values="er", aggfunc="median") * 100
cnt = ct.pivot_table(index="format", columns="topic", values="er", aggfunc="size")
order_f = mat.mean(axis=1).sort_values(ascending=False).index
order_t = mat.mean(axis=0).sort_values(ascending=False).index
mat, cnt = mat.loc[order_f, order_t], cnt.loc[order_f, order_t]
fig, ax = plt.subplots(figsize=(8.4, 3.6))
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("seq", SEQ)
im = ax.imshow(mat.values, cmap=cmap, aspect="auto")
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        v = mat.values[i, j]
        ax.text(j, i, f"{v:.1f}%\n(n={cnt.values[i, j]})", ha="center", va="center", fontsize=7,
                color="white" if v > np.nanpercentile(mat.values, 70) else INK)
ax.set_xticks(range(mat.shape[1]))
ax.set_xticklabels(mat.columns, rotation=20, ha="right")
ax.set_yticks(range(mat.shape[0]))
ax.set_yticklabels(mat.index)
ax.grid(False)
ax.set_title("Content Performance Matrix — median engagement rate (format × theme)")
cb = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.02)
cb.outline.set_visible(False)
stamp(fig, "DEMO DATA - SYNTHETIC - small cells (n<25) should be read as directional", y=-0.2)
fig.savefig(os.path.join(OUT, "content_matrix_heatmap.png"))
plt.close(fig)
spend = ct.spend_inr.sum()
metrics["digital"] = {
    "posts": int(len(ct)), "impressions": int(ct.impressions.sum()), "reach": int(ct.reach.sum()),
    "engagements": int(ct.engagements.sum()),
    "engagement_rate_pct": round(100 * ct.engagements.sum() / ct.impressions.sum(), 2),
    "video_views": int(ct.video_views.sum()), "clicks": int(ct.clicks.sum()),
    "ctr_pct": round(100 * ct.clicks.sum() / ct.impressions.sum(), 2),
    "boosted_posts": int(ct.boosted.sum()), "spend_inr": int(spend),
    "cpm_inr": round(spend / ct[ct.boosted].impressions.sum() * 1000, 1),
    "cpc_inr": round(spend / ct[ct.boosted].clicks.sum(), 2),
    "boosted_with_precert_ref_pct": 100.0,
    "ai_flagged_posts": int(ct.ai_content_flag.sum()),
    "best_format": str(order_f[0]), "best_theme": str(order_t[0]),
}

# ---------------------------------------------------------------- 5. Fictional zone hex map (field completion)
zc = fa.groupby("zone").agg(done=("completed", "mean"), n=("completed", "size"),
                            ontime=("report_submitted_on_time", "mean")).reset_index()
fig, ax = plt.subplots(figsize=(6.4, 4.6))
coords = []
for i in range(24):
    r, c = divmod(i, 6)
    coords.append((c * 1.73 + (0.87 if r % 2 else 0), -r * 1.5))
norm = matplotlib.colors.Normalize(vmin=0.6, vmax=0.95)
for (xy, row) in zip(coords, zc.itertuples()):
    col = cmap(norm(row.done))
    ax.add_patch(RegularPolygon(xy, 6, radius=0.98, facecolor=col, edgecolor="white", lw=2))
    ax.text(xy[0], xy[1] + 0.18, row.zone, ha="center", fontsize=8, color=INK if row.done < 0.85 else "white", weight="bold")
    ax.text(xy[0], xy[1] - 0.32, f"{row.done * 100:.0f}%", ha="center", fontsize=8, color=INK if row.done < 0.85 else "white")
ax.set_xlim(-1.2, 10.9)
ax.set_ylim(-5.4, 1.2)
ax.set_aspect("equal")
ax.axis("off")
for k, b in enumerate(["North Block", "River Block", "Market Block", "Hill Block"]):
    ax.text(-1.25, -k * 1.5, b.split()[0], ha="right", va="center", fontsize=8, color=MUTED)
ax.set_title("Field activity completion by zone (fictional hex geography)")
sm_ = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)
cb = fig.colorbar(sm_, ax=ax, fraction=0.03, pad=0.01)
cb.outline.set_visible(False)
cb.ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
stamp(fig)
fig.savefig(os.path.join(OUT, "zone_map_field_completion.png"))
plt.close(fig)
fb = fa.groupby("block").agg(planned=("planned", "size"), completion=("completed", "mean"),
                             on_time=("report_submitted_on_time", "mean"),
                             quality=("report_quality_score", "mean")).reset_index()
metrics["field"] = {
    "activities_planned": int(len(fa)), "completion_pct": round(100 * fa.completed.mean(), 1),
    "on_time_reports_pct": round(100 * fa.report_submitted_on_time.mean(), 1),
    "attendance_total": int(fa.attendance_headcount.sum()), "issue_reports": int(fa.issue_reports_logged.sum()),
    "by_block": {r.block: {"completion_pct": round(100 * r.completion, 1), "on_time_pct": round(100 * r.on_time, 1),
                           "quality": round(r.quality, 2)} for r in fb.itertuples()},
    "lowest_zone": zc.sort_values("done").iloc[0].zone,
    "lowest_zone_completion_pct": round(100 * zc.done.min(), 1),
}

# ---------------------------------------------------------------- 6. Forecast (trend + weekly seasonality, PI)
y = np.log(daily.values.astype(float))
t = np.arange(len(y))
train_end = 24  # train on days 0-23, validate on 24-29 (pre-spike), forecast 14 days beyond data
def design(tt):
    return np.column_stack([np.ones_like(tt), tt, np.sin(2 * np.pi * tt / 7), np.cos(2 * np.pi * tt / 7)])
beta, *_ = np.linalg.lstsq(design(t[:train_end]), y[:train_end], rcond=None)
resid_sd = np.std(y[:train_end] - design(t[:train_end]) @ beta, ddof=4)
val = slice(train_end, 30)
pred_val = np.exp(design(t[val]) @ beta)
mape = float(np.mean(np.abs(pred_val - daily.values[val]) / daily.values[val]) * 100)
# refit on all non-anomalous days for the forward forecast
keep = ~daily.index.isin(anom.index) & ~daily.index.isin(anom.index + pd.Timedelta(days=1))
beta2, *_ = np.linalg.lstsq(design(t[keep]), y[keep], rcond=None)
sd2 = np.std(y[keep] - design(t[keep]) @ beta2, ddof=4)
tf = np.arange(len(y), len(y) + 14)
mu = design(tf) @ beta2
fdates = pd.date_range(daily.index[-1] + pd.Timedelta(days=1), periods=14)
fig, ax = plt.subplots(figsize=(8, 3.2))
ax.plot(daily.index, daily.values, color=BLUE, lw=2, label="Observed (de-duplicated)")
ax.fill_between(fdates, np.exp(mu - 1.96 * sd2), np.exp(mu + 1.96 * sd2), color=SAFFRON, alpha=0.15, lw=0, label="95% prediction interval")
ax.fill_between(fdates, np.exp(mu - 1.28 * sd2), np.exp(mu + 1.28 * sd2), color=SAFFRON, alpha=0.25, lw=0, label="80% prediction interval")
ax.plot(fdates, np.exp(mu), color=SAFFRON, lw=2, ls="--", label="Point forecast")
ax.axvspan(daily.index[train_end], daily.index[29], color=GRID, alpha=0.6, lw=0)
ax.text(daily.index[train_end], ax.get_ylim()[1] * 0.97, " validation", fontsize=8, color=MUTED, va="top")
ax.set_title(f"Mention-volume forecast, 14 days (validation MAPE {mape:.1f}%) — operational planning only")
ax.set_ylabel("Mentions / day")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d %b"))
stamp(fig)
fig.savefig(os.path.join(OUT, "forecast_volume.png"))
plt.close(fig)
metrics["forecast"] = {"model": "log-linear trend + weekly Fourier terms (OLS)", "train_days": train_end,
                       "validation_days": 6, "validation_mape_pct": round(mape, 1),
                       "horizon_days": 14, "anomalies_excluded_from_fit": int((~keep).sum())}

# ---------------------------------------------------------------- 7. Media: weekly volume by outlet type (stacked)
mm["week"] = mm.date.dt.to_period("W-SUN").dt.start_time
wk = mm.groupby(["week", "outlet_type"]).size().unstack(fill_value=0)
top_out = wk.sum().sort_values(ascending=False).index
groups = list(top_out[:3]) + ["Other"]
wk["Other"] = wk[top_out[3:]].sum(axis=1)
fig, ax = plt.subplots(figsize=(8, 3.2))
bottom = np.zeros(len(wk))
for g, col in zip(groups, [SAFFRON, BLUE, TEAL, OCHRE]):
    ax.bar(wk.index, wk[g], bottom=bottom, width=5, color=col, label=g, edgecolor="white", lw=1)
    bottom += wk[g].values
ax.set_title("Media mentions per week by outlet type")
ax.set_ylabel("Articles / segments")
ax.legend(frameon=False, fontsize=8, ncol=4, loc="upper left")
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d %b"))
ax.set_ylim(0, bottom.max() * 1.2)
stamp(fig)
fig.savefig(os.path.join(OUT, "media_weekly_outlets.png"))
plt.close(fig)
last7 = mm[mm.date > mm.date.max() - pd.Timedelta(days=7)]
metrics["media"] = {
    "articles_total": int(len(mm)), "last7": int(len(last7)),
    "last7_negative_pct": round(100 * (last7.tone == "Negative").mean(), 1),
    "overall_negative_pct": round(100 * (mm.tone == "Negative").mean(), 1),
    "top_topic_last7": str(last7.topic.value_counts().index[0]),
    "regional_share_pct": round(100 * mm.outlet_type.str.contains("Regional|Hyperlocal").mean(), 1),
}

# ---------------------------------------------------------------- 8. Call centre weekly service levels
cc["week"] = cc.date.dt.to_period("W-SUN").dt.start_time
cw = cc.groupby("week").agg(answer=("answered", "mean"), fcr=("resolved_first_contact", "mean"), n=("call_id", "size"))
fig, ax = plt.subplots(figsize=(8, 3.0))
ax.plot(cw.index, cw.answer * 100, color=BLUE, lw=2, marker="o", ms=5, label="Answer rate")
ax.plot(cw.index, cw.fcr * 100, color=TEAL, lw=2, marker="o", ms=5, label="First-contact resolution")
ax.axhline(90, color=MUTED, ls=":", lw=1)
ax.text(cw.index[0], 90.6, "SLA target: 90% answered", fontsize=8, color=MUTED)
ax.set_ylim(30, 100)
ax.set_ylabel("% of calls")
ax.set_title("Call-centre service levels by week (aggregate, no caller PII)")
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d %b"))
stamp(fig)
fig.savefig(os.path.join(OUT, "call_centre_weekly.png"))
plt.close(fig)
metrics["call_centre"] = {
    "calls": int(len(cc)), "answer_rate_pct": round(100 * cc.answered.mean(), 1),
    "answer_rate_last7_pct": round(100 * cc[cc.date > cc.date.max() - pd.Timedelta(days=7)].answered.mean(), 1),
    "fcr_pct": round(100 * cc.resolved_first_contact.mean(), 1),
    "median_wait_s": int(cc[cc.answered].wait_seconds.median()),
    "top_category": str(cc.category.value_counts().index[0]),
}

# ---------------------------------------------------------------- 9. Data quality summary
metrics["data_quality"] = {
    "sources_registered": 14, "sources_green": 11, "sources_amber": 2, "sources_red": 1,
    "field_reports_on_time_pct": metrics["field"]["on_time_reports_pct"],
    "social_geo_coverage_pct": metrics["social"]["geo_coverage_pct"],
    "survey_qc_excluded_pct": metrics["survey"]["qc_excluded_pct"],
    "duplicate_mentions_pct": round(100 * sm.is_near_duplicate.mean(), 1),
    "note": "source counts are illustrative for the demo source registry",
}

# ---------------------------------------------------------------- 10. Abstract cover visual (generated, no map outline)
fig = plt.figure(figsize=(13.33, 7.5), dpi=150)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor("#081830")
fig.patch.set_facecolor("#081830")
pts = rng.uniform([0, 0], [13.33, 7.5], size=(230, 2))
pts = pts[(pts[:, 0] > 6.2) | (rng.random(len(pts)) < 0.25)]
for i in range(len(pts)):
    d = np.hypot(*(pts - pts[i]).T)
    for j in np.argsort(d)[1:3]:
        ax.plot(*zip(pts[i], pts[j]), color="#2B4A78", lw=0.6, alpha=0.7)
sizes = rng.uniform(4, 22, len(pts))
hot = rng.random(len(pts)) < 0.12
ax.scatter(pts[~hot, 0], pts[~hot, 1], s=sizes[~hot], color="#6F8FBF", alpha=0.8, lw=0)
ax.scatter(pts[hot, 0], pts[hot, 1], s=sizes[hot] * 2.2, color="#F28C28", alpha=0.95, lw=0)
ax.scatter(pts[hot, 0], pts[hot, 1], s=sizes[hot] * 9, color="#F28C28", alpha=0.12, lw=0)
xs = np.linspace(6.5, 13.3, 200)
for k, a in enumerate([0.35, 0.25, 0.15]):
    ax.plot(xs, 1.2 + 0.5 * k + 0.35 * np.sin(xs * 1.3 + k) + 0.08 * xs, color="#C9A227", lw=1.2, alpha=a)
ax.set_xlim(0, 13.33)
ax.set_ylim(0, 7.5)
ax.axis("off")
fig.savefig(os.path.join(OUT, "cover_network.png"), facecolor="#081830")
plt.close(fig)

with open(os.path.join(OUT, "metrics.json"), "w") as f:
    json.dump(metrics, f, indent=2, default=str)
print(json.dumps(metrics, indent=2, default=str))
