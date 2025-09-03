import streamlit as st
from pathlib import Path

st.set_page_config(page_title="ShowsSpeed: Strategy & Pit Stops", page_icon="🏎️", layout="wide")

st.markdown("""
<style>
.topbar{
  position:sticky; top:0; z-index:9999;
  display:flex; align-items:center; gap:20px;
  padding:16px 24px; height:100px;
  /* Green Lime Sauber theme */
  background:linear-gradient(90deg,#4CAF50 0%, #2E8B57 50%, #145A32 100%);
  border-bottom:4px solid #FFFFFF;
}
.topbar .brand{
  display:flex; align-items:center; gap:20px;
  font-weight:1000; letter-spacing:1px;
  color:#FFFFFF; font-size:48px;
}

/* background */
[data-testid="stAppViewContainer"]{
  background:#111118;
  background-image:linear-gradient(180deg,#14141b 0%, #111118 50%, #0e0e15 100%);
  background-attachment:fixed;
  background-size:cover;
}
section[data-testid="stSidebar"]{
  background:linear-gradient(180deg,#15151c 0%, #101018 100%);
}
.block-container{padding-top:18px !important; padding-bottom:18px !important;}
h1,h2,h3,h4,h5,h6{margin:0.2em 0 0.35em 0 !important;}
p,ul,ol{margin:0.2em 0 0.45em 0 !important; line-height:1.45;}
li{margin:0.15em 0;}
hr{height:1px; border:none; background:rgba(255,255,255,0.08); margin:18px 0 !important;}
.blockpad{height:8px;}
#MainMenu, header, footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar"><div class="brand">🏁 <span>ShowsSpeed: F1 Data Science Project</span></div></div>
<div class="blockpad"></div>
""", unsafe_allow_html=True)

# ---- page content ----
st.header("Strategy & Pit Stops")

# ---- Pit crews speed ----
st.subheader("Fastest Pit Crews (2022–2025)")
st.markdown("""
- Question: which constructors have the quickest and most consistent pit crews?  
- Approach: timed every pit stop from 2022–2025, comparing fastest, mean, and median.  
- Why median/mean? Pit times often skewed by botched stops — median gives stable benchmark.  
""")
st.image("assets/pit_crews_speed.png", use_container_width=True)

st.markdown("### Key Takeaways")
st.markdown("""
- Ferrari, Red Bull, and Williams regularly top pit speed across years.  
- Outliers in mean values show that even quick crews can have major misses.  
- Median line helps cut through noise and show sustainable performance.  
""")

with st.expander("Metric Notes"):
    st.markdown("""
    - Data: pit stop times logged in FastF1 (2022–2025).  
    - Metrics: fastest individual stop, team mean, and team median.  
    - Creative step: included median to handle extreme skew from failed stops.  
    - Visualization: horizontal bar charts per year + aggregate panel.  
    """)

# ---- Early undercut ----
st.subheader("Who wins with early undercut?")
st.markdown("""
- Question: which drivers convert early stops into higher finish positions?  
- Approach: flagged early stints (pitting before field median) and tracked finishing percentile.  
- Why percentile? Normalizes across seasons and grid sizes — easier to compare drivers.  
""")
st.image("assets/early_undercut.png", use_container_width=True)

st.markdown("### Key Takeaways")
st.markdown("""
- Verstappen, Leclerc, and Sainz consistently benefit from early stops.  
- Strategy bias: top cars gain more from clean air after undercut.  
- Midfield drivers less likely to profit — traffic cancels early-stint advantage.  
""")

with st.expander("Metric Notes"):
    st.markdown("""
    - Data: stint timing + finishing percentile from `qr_all_df`.  
    - Metric:  
        - Defined **first stop lap** for each driver.  
        - Undercut = stopping earlier than 25% quartile of the field.  
        - Finish measured by percentile (0 = last, 1 = race win).  
    - Creative steps:  
        - Engineered “early undercut” feature directly from pit summary.  
        - Used quartile split instead of absolute lap numbers, so it scales across different races.  
    - Visualization: bar chart of finish percentile under early-stop conditions.  
    """)

# ---- Tire stretch ----
st.subheader("Who wins with tire stretch?")
st.markdown("""
- Question: which drivers make long stints work?  
- Approach: identified long stints (top quartile in tyre life) and tracked results.  
- Why quartile? Captures drivers stretching tyres beyond the normal strategy window.  
""")
st.image("assets/tire_stretch.png", use_container_width=True)

st.markdown("### Key Takeaways")
st.markdown("""
- Verstappen dominates on tyre stretch — strong balance + tyre management.  
- Ferrari’s Leclerc and Sainz also adapt well to extended runs.  
- Midfield teams vary: McLaren shows gains, Alpine struggles more.  
""")

with st.expander("Metric Notes"):
    st.markdown("""
    - Data: stint length and compound usage from `qr_all_df`.  
    - Metric:  
        - Long stint flagged if longer than 75% quantile for that race.  
        - “Tire stretch” = maximizing compound durability beyond standard strategy.  
    - Creative steps:  
        - Engineered new feature `longest_stint` from stint grouping.  
        - Defined stretch not by absolute lap counts, but relative to field norms per race.  
    - Visualization: horizontal bar chart comparing finish percentile.  
    """)

# ---- Late overcut ----
st.subheader("Who wins with late overcut?")
st.markdown("""
- Question: which drivers profit from staying out longer than rivals?  
- Approach: compared finishing percentiles when drivers delay stops past median.  
- Why? Captures whether extending stint creates net advantage vs field.  
""")
st.image("assets/late_overcut.png", use_container_width=True)

st.markdown("### Key Takeaways")
st.markdown("""
- Verstappen and Leclerc often turn late overcuts into strong finishes.  
- McLaren drivers (Norris, Piastri) show solid overcut value in recent seasons.  
- Strategy risky — tyre fade can cancel benefits if mistimed.  
""")

with st.expander("Metric Notes"):
    st.markdown("""
    - Data: stint timing vs field median, mapped to finish percentiles.  
    - Metric:  
        - Overcut f
        lagged if first stop lap ≥ 75% quantile for that race.  
        - Finish measured as percentile vs full field.  
    - Creative steps:  
        - Built new engineered feature `first_stop_lap` relative to quartiles.  
        - Definition of “overcut” based on relative timing, not raw lap counts, making it robust across tracks.  
        - Combined stint count + tyre compound context to filter valid overcuts.  
    - Visualization: bar chart of finish percentile in overcut cases.  
    """)

