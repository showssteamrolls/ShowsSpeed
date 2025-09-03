import streamlit as st
from pathlib import Path

st.set_page_config(page_title="ShowsSpeed: Drivers", page_icon="🏎️", layout="wide")

st.markdown("""
<style>
/* —— base styles —— */
.topbar{
  position:sticky; top:0; z-index:9999;
  display:flex; align-items:center; gap:20px;
  padding:16px 24px; height:100px;
  /* McLaren theme orange */
  background:linear-gradient(90deg,#FF8000 0%, #CC5500 100%);
  border-bottom:4px solid #FFFFFF;
}
.topbar .brand{
  display:flex; align-items:center; gap:20px;
  font-weight:1000; letter-spacing:1px;
  color:#F5F5F5; font-size:48px;
}

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
st.header("Drivers")

st.subheader("Dry vs Wet Performance by Constructor (2022–2025)")
st.markdown("""
- Question: how much does each team slow down in the wet compared to their own dry benchmark?  
- Approach: calculated average lap times separately for dry vs wet stints, then expressed % slowdown relative to that team’s dry baseline.  
- Bars show both dry (solid) and wet (striped) averages for context.  
""")

st.image("assets/dry_v_wet_perf_by_team.png", use_container_width=True)

st.markdown("### Key Takeaways")
st.markdown("""
- RB and Kick Sauber show the least performance loss in the wet (<8%).  
- Midfield teams like Alpine, Haas, McLaren hover around ~10% slowdown.  
- Williams, Alfa Romeo, AlphaTauri lose 12–15%.  
- Racing Bulls are the most sensitive, nearly 20% slower in the wet.  
""")

with st.expander("Method Notes"):
    st.markdown("""
    - Data: 2022–2025 lap times, tagged with session weather (FastF1 metadata).  
    - Metric: avg lap time per constructor in dry vs wet, % diff = (wet − dry) / dry.  
    - Why this metric: keeps comparison fair — each team is benchmarked against its own dry pace, not absolute lap times.  
    - Viz: grouped bar chart with hatching for wet laps to highlight the gap.  
    """)

st.subheader("Dry/Wet Averages and % Change — Heatmap (2022–2025)")
st.markdown("""
- Question: which teams are most sensitive to wet conditions when averaging across multiple seasons?  
- Approach: combined avg lap times in dry vs wet, plus computed % slowdown. Displayed all three in one heatmap.  
- Color scale lets you scan patterns across teams at a glance.  
""")

st.image("assets/dry_wet_avg_change_heatmap.png", use_container_width=True)

st.markdown("### Key Takeaways")
st.markdown("""
- Racing Bulls show the sharpest drop-off in wet (≈20%), matching the bar chart story.  
- AlphaTauri, Alfa Romeo, Williams also see double-digit slowdowns.  
- Top teams like Red Bull, Mercedes, Kick Sauber are far steadier (~7–10%).  
- RB (the team, not Racing Bulls) barely moves — just 1.8% difference.  
""")

with st.expander("Method Notes"):
    st.markdown("""
    - Data: 2022–2025 lap times, split by weather.  
    - Metrics:  
      - **Dry** = avg lap time across dry stints.  
      - **Wet** = avg lap time across wet stints.  
      - **% change** = slowdown relative to each team’s dry avg.  
    - Why this works: condenses the bar chart into a dense matrix, so comparisons are instant.  
    - Viz: Seaborn heatmap with annotations, warm-to-cool colormap highlights differences.  
    """)
