import streamlit as st
from pathlib import Path
import json

st.set_page_config(page_title="ShowsSpeed: ML Laptime Predictor", page_icon="🏎️", layout="wide")

# =============== styles (Mercedes turquoise topbar + KPI turquoise numbers) ===============
st.markdown("""
<style>
.topbar{
  position:sticky; top:0; z-index:9999;
  display:flex; align-items:center; gap:20px;
  padding:16px 24px; height:100px;
  /* Mercedes theme */
  background:linear-gradient(90deg,#00D2BE 0%, #00B3A6 45%, #008E85 100%);
  border-bottom:4px solid #FFFFFF;
}
.topbar .brand{
  display:flex; align-items:center; gap:20px;
  font-weight:1000; letter-spacing:1px;
  color:#F5F5F5; font-size:48px;
}
[data-testid="stAppViewContainer"]{
  background:#0f1316;
  background-image:linear-gradient(180deg,#12171b 0%, #0f1316 50%, #0c1013 100%);
  background-attachment:fixed; background-size:cover;
}
section[data-testid="stSidebar"]{
  background:linear-gradient(180deg,#141a1e 0%, #0f1418 100%);
}
.block-container{padding-top:18px !important; padding-bottom:18px !important;}
h1,h2,h3,h4,h5,h6{margin:0.2em 0 0.35em 0 !important;}
p,ul,ol{margin:0.2em 0 0.45em 0 !important; line-height:1.45;}
li{margin:0.15em 0;}
hr{height:1px; border:none; background:rgba(255,255,255,0.08); margin:18px 0 !important;}
.blockpad{height:8px;}
#MainMenu, header, footer {visibility:hidden;}

/* --- KPI numbers in Mercedes turquoise --- */
[data-testid="stMetricValue"] > div { color:#00D2BE !important; }
/* optional: color the delta too, if used */
/* [data-testid="stMetricDelta"] svg, [data-testid="stMetricDelta"] { color:#00D2BE !important; } */
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar"><div class="brand">🏁 <span>ShowsSpeed: F1 Data Science Project</span></div></div>
<div class="blockpad"></div>
""", unsafe_allow_html=True)

# -------- helper: load metrics (from assets/metrics.json if present) --------
ASSETS = Path("assets")
METRICS_DEFAULT = {
    "overall": {"mae_ms": 63.0, "rmse_ms": 95.0, "p95_ms": 198.0, "r2": 0.9999, "bias_ms": -22.0},
    "sessions": {
        "R": {"mae_ms": 60.0, "p95_ms": 175.0, "bias_ms": -32.0},
        "Q": {"mae_ms": 84.0, "p95_ms": 384.0, "bias_ms": 19.0},
    },
    "years": {"2022": 60.0, "2023": 66.0, "2024": 64.0, "2025": 62.0}
}
def load_metrics():
    p = ASSETS / "metrics.json"
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception:
            return METRICS_DEFAULT
    return METRICS_DEFAULT

M = load_metrics()
ov  = M["overall"]
r_s = M["sessions"].get("R", {})
q_s = M["sessions"].get("Q", {})

# ---- page content ----
st.header("ML Laptime Predictor")

# ——— TL;DR (Best Model) ———
st.subheader("TL;DR — Best Model")
st.markdown(f"""
- **Winner:** Gradient-Boosted Trees (XGBoost/LightGBM variant)  
- **Why it wins:** handles non-linear effects (tyre age × compound × stint phase) and interactions without heavy manual feature crafting.  
- **Key metrics (val):** **MAE ~ {ov['mae_ms']:.0f} ms**, **P95 |error| ~ {ov['p95_ms']:.0f} ms**, **R² ~ {ov['r2']:.4f}**.  
  Race-only: **~{r_s.get('mae_ms','—')} ms MAE** *(Quali ~{q_s.get('mae_ms','—')} ms)*.  
- **Where it shines:** dry stints, mid-race laps with stable fuel load; robust to mild traffic noise.
""")

# ——— Data & Features ———
st.subheader("Data & Features")
st.markdown("""
- **Data scope:** 2022–2025 lap-level dataset (FastF1 + f1db join).  
- **Target:** `lap_time_s` normalized per session.  
- **Core features:**  
  - Tyre: compound, **tyre age (laps)**, stint id  
  - Session: lap number, sector deltas, pit-in/out flags  
  - Conditions: dry/wet tag, temp proxies (if available)  
  - Traffic proxies: gap to car ahead/behind *(if engineered)*  
- **Engineered bits:**  
  - **Tyre wear proxy:** binned tyre age + interaction with compound  
  - **Stint phase:** early/mid/late via quantiles of stint laps  
  - **Clean air flag:** heuristic using overtake windows / pit deltas *(optional)*
""")

# ——— Evaluation Setup ———
st.subheader("Evaluation Setup")
st.markdown("""
- **Split:** group by **raceId** (no session leakage).  
- **Metrics:** MAE for interpretability, RMSE for penalty on large misses, R² for fit quality.  
- **Preprocessing:**  
  - Standardize numeric features for linear baselines  
  - One-hot / categorical encoding for trees as needed  
  - Outlier trimming: drop absurd in/out laps if mislabeled
""")

# =================== ACCURACY DASHBOARD ===================
st.subheader("Model Accuracy (Validation)")

c1, c2, c3, c4 = st.columns(4)
c1.metric("MAE", f"{ov['mae_ms']:.0f} ms")
c2.metric("P95 |error|", f"{ov['p95_ms']:.0f} ms")
c3.metric("R²", f"{ov['r2']:.4f}")
c4.metric("Median bias", f"{ov['bias_ms']:+.0f} ms")

# Diagnostics
d1, d2 = st.columns(2)
with d1:
    st.markdown("**Predicted vs Actual**")
    st.image(str(ASSETS/"pva_rf_sct.png"), use_container_width=True, caption="Predicted vs Actual laptimes")
with d2:
    st.markdown("**Residuals (histogram)**")
    st.image(str(ASSETS/"res_hist.png"), use_container_width=True, caption="Residual distribution (Actual − Predicted, ms)")

d3, d4 = st.columns(2)
with d3:
    st.markdown("**Residuals vs Predicted**")
    st.image(str(ASSETS/"res_v_pred.png"), use_container_width=True, caption="Check heteroscedasticity / regime pockets")
with d4:
    st.markdown("**Feature Importance (RF)**")
    st.image(str(ASSETS/"feature_imp_rf.png"), use_container_width=True, caption="Relative importance of inputs")

# Breakdowns
st.markdown("### Breakdowns")
b1, b2 = st.columns(2)
with b1:
    st.markdown("**By Session**")
    st.markdown(f"""
- **Race (R):** MAE ~ **{r_s.get('mae_ms','—')} ms**, P95 ~ **{r_s.get('p95_ms','—')} ms**, bias {r_s.get('bias_ms','—')} ms  
- **Quali (Q):** MAE ~ **{q_s.get('mae_ms','—')} ms**, P95 ~ **{q_s.get('p95_ms','—')} ms**, bias {q_s.get('bias_ms','—')} ms
""")
with b2:
    st.markdown("**By Year — MAE**")
    y = M["years"]
    st.markdown(f"""
- 2022: **~{y.get('2022','—')} ms**  
- 2023: **~{y.get('2023','—')} ms**  
- 2024: **~{y.get('2024','—')} ms**  
- 2025: **~{y.get('2025','—')} ms**
""")

st.markdown("---")

# ——— Error/Notes ———
st.subheader("Error Notes & Ideas")
st.markdown("""
- **Hard cases:** heavy rain, safety-car restarts, pit in/out laps.  
- **By circuit:** street circuits show higher residuals (traffic/SC variance).  
- **By stint:** late-stint softs degrade faster than model expects → consider richer wear proxy.  
- **Next feature ideas:** track evolution rate, clean-air proxy from gaps, per-driver random effects.
""")

# ——— Experiment Log (Chronological) ———
st.subheader("Experiment Log (journey to best)")
st.markdown("**Baseline → Linear → Ridge → Random Forest → GBDT (winner)**")

with st.expander("Baseline (simple rules / mean-by-bins)"):
    st.markdown("""
- **Idea:** predict by session mean or tyre-age bins.  
- **Result:** fast but weak; ignores interactions.  
- **Kept:** binning strategy as a feature later.
    """)

with st.expander("Linear Regression"):
    st.markdown("""
- **Idea:** straight linear fit on core features.  
- **Result:** improves MAE a bit; underfits tyre-wear and stint-phase non-linearities.  
- **Why it fell short:** interactions matter; linear needs manual crosses.
    """)

with st.expander("Ridge (L2)"):
    st.markdown("""
- **Idea:** regularize linear to reduce variance.  
- **Result:** slightly better stability; still misses compound × age effects.  
- **Takeaway:** regularization ≠ non-linear modeling.
    """)

with st.expander("Random Forest"):
    st.markdown("""
- **Idea:** non-linear splits with low feature engineering.  
- **Result:** solid jump in MAE/RMSE, especially on mixed conditions.  
- **Limits:** can be chunky; less smooth on extrapolation.
    """)
    st.image(str(ASSETS/"pva_rf_sct.png"),
             caption="Predicted vs Actual (reference RF run).", use_container_width=True)
    st.image(str(ASSETS/"feature_imp_rf.png"),
             caption="RF feature importance (normalized).", use_container_width=True)

with st.expander("GBDT (XGB/LGBM) — **Final**"):
    st.markdown("""
- **Idea:** gradient-boosted trees with tuned depth/learning rate + early stopping.  
- **Result:** best across metrics; handles interactions (compound × age × stint).  
- **Notes:** consider monotone constraints if enforcing “older tyre = slower”.
    """)
