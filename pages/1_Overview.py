import streamlit as st
from pathlib import Path

st.set_page_config(page_title="ShowsSpeed: Overview", page_icon="🏎️", layout="wide")

st.markdown("""
<style>
.topbar{
  position:sticky; top:0; z-index:9999;
  display:flex; align-items:center; gap:20px;
  padding:16px 24px; height:100px;
  background:linear-gradient(90deg,
  #1E90FF 0%,   /* lighter blue left */
  #005AFF 50%,  /* Williams bright blue center */
  #002060 100%  /* deep navy right */);
  border-bottom:4px solid #FFFFFF;
}

.topbar .brand{
  display:flex; align-items:center; gap:20px;
  font-weight:1000; letter-spacing:1px;
  color:#F5F5F5; font-size:48px;
}

/* background: fixed gradient around #111118 */
[data-testid="stAppViewContainer"]{
  background:#111118;
  background-image:linear-gradient(180deg,#14141b 0%, #111118 50%, #0e0e15 100%);
  background-attachment:fixed;
  background-size:cover;
}

/* sidebar bg to match */
section[data-testid="stSidebar"]{
  background:linear-gradient(180deg,#15151c 0%, #101018 100%);
}

/* tighter vertical rhythm */
.block-container{padding-top:18px !important; padding-bottom:18px !important;}
h1,h2,h3,h4,h5,h6{margin:0.2em 0 0.35em 0 !important;}
p,ul,ol{margin:0.2em 0 0.45em 0 !important; line-height:1.45;}
li{margin:0.15em 0;}
hr{height:1px; border:none; background:rgba(255,255,255,0.08); margin:18px 0 !important;}

.blockpad{height:8px;}
#MainMenu, header, footer {visibility:hidden;}

.big-text{font-size:48px !important; line-height:1.6;}

section[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] span{font-size:26px !important;}
section[data-testid="stSidebar"] .css-1d391kg::before{
  content:"ShowsSpeed: Home"; font-size:28px; font-weight:800; color:#E63946; display:block; margin:8px 0 16px 0;
}
section[data-testid="stSidebar"] .css-1d391kg>span{display:none;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar"><div class="brand">🏁 <span>ShowsSpeed: F1 Data Science Project</span></div></div>
<div class="blockpad"></div>
""", unsafe_allow_html=True)

st.header("Overview")
st.write("Each section contains: visualizations, takeaways, and my thought processes.")

st.subheader("Table of Contents")
st.markdown("""
- **Circuits & Conditions** – track traits, weather, dry vs wet
- **Strategy & Pit stops** – stint windows, tyre choices
- **Drivers** – home advantage, consistency, deltas
- **ML Laptime Predictor** – baseline vs ML variants
""")

st.subheader("Work in Progress")
st.markdown("""
- interactive charts (Altair/Plotly) replacing static previews  
- add rolling form metrics by team/driver  
- wire notebook pipelines → parquet + joblib for live updates  
""")

st.subheader("Data Foundations")
st.markdown("""
- **f1db (CSV datasets)**  
  - Public F1 database with 40+ CSVs (drivers, constructors, circuits, engines, results, pit stops, etc.).  
  - Provides long-term historical structure → who raced where, which teams, which engines.  
  - Used as the backbone for metadata: linking circuits, teams, and drivers across seasons.  

- **FastF1 scrape (`qr_all_df`)**  
  - Queried lap-by-lap telemetry and race event data (qualifying + race).  
  - Columns include lap times, stint info, tyre compounds, weather/track conditions.  
  - Cleaned by:
    - ensuring `driver_number` and `lap` were integers,  
    - merging with f1db race IDs for consistency,  
    - filtering incomplete rows (e.g., missing lap times, pit entry duplicates).  
  - Final product → 86k+ rows, 21 columns (2022–2025).  

Together, these datasets let me combine **long-term race context** (f1db) with **session-level performance detail** (FastF1).
""")

c1, c2 = st.columns(2)
with c1:
    st.image("assets/f1db.png", use_container_width=True, caption="f1db – 40+ structured CSV datasets")
with c2:
    st.image("assets/qr_all_df.png", use_container_width=True, caption="FastF1 scrape – `qr_all_df` sample (86k+ rows)")

st.caption("Data: f1db, FastF1.")
