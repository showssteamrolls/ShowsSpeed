import streamlit as st
from pathlib import Path

st.set_page_config(page_title="ShowsSpeed: Circuits & Conditions", page_icon="🏎️", layout="wide")

st.markdown("""
<style>
/* —— base styles (match app.py) —— */
.topbar{
  position:sticky; top:0; z-index:9999;
  display:flex; align-items:center; gap:20px;
  padding:16px 24px; height:100px;
  /* Ferrari theme */
  background:linear-gradient(90deg,#E63946 0%, #8B0000 100%);
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
st.header("Circuits & Conditions")

# --- Chart 1: Track Consistency Grid
st.subheader("Track Consistency Grid (2022–2025)")
st.markdown("""
- Question: which tracks produce the most consistent finishing positions across teams?  
- Approach: calculated the standard deviation of finishing position for each circuit over 2022–2025.  
- Lower std → tighter spread → more consistent races.  
""")

st.image("assets/consistency_across_grids.png", use_container_width=True)

st.markdown("### Key Takeaways")
st.markdown("""
- Hungaroring and Catalunya stand out as the most consistent circuits.  
- Street circuits like Marina Bay and Baku show larger spread — more unpredictable.  
- High-speed tracks (Monza, Spa) sit mid-range: not chaotic, but not locked-down.  
""")

with st.expander("Method Notes"):
    st.markdown("""
    - **Stat used:** standard deviation (std) of finishing positions per circuit.  
        - std is well-suited because it measures spread, not the average.  
        - low std → most drivers/teams cluster around similar outcomes (tight racing).  
        - high std → wider differences, suggesting opportunity for big swings.  
    - **Why not average finish?** averages flatten out the story, while std shows *volatility*, which was the real interest here.  
    - **Data:** 2022–2025 finishing positions from f1db and FastF1.  
    - **Visualization:** grid heatmap with Viridis colormap for readability.  
    """)

st.markdown("---")

# --- Chart 2: Track Performance by Team
st.subheader("Track Performance by Team (Relative to Team Avg)")
st.markdown("""
- Question: which circuits give teams a relative boost (or drag) compared to their usual performance?  
- Approach: compared each team’s average finishing position at a track vs their season average.  
- Positive values = better than usual. Negative values = worse than usual.  
""")

st.image("assets/track_perf_per_team.png", use_container_width=True)

st.markdown("### Key Takeaways")
st.markdown("""
- McLaren and Red Bull see notable spikes at certain circuits (positive relative positions).  
- Ferrari and Mercedes show fewer large swings — generally more stable across tracks.  
- Some teams (e.g. Haas, Kick Sauber) show strong outliers, suggesting certain tracks play to their setup strengths.  
""")

with st.expander("Method Notes"):
    st.markdown("""
    - **Stat used:** relative performance vs team average (finishing position delta).  
        - each cell = team’s performance at a track minus their overall mean performance.  
        - positive = they finished better than usual, negative = worse than usual.  
    - **Why this metric works:**  
        - controls for baseline strength of the team (e.g. Red Bull usually at the top).  
        - highlights *track fit* — circuits where teams gain or lose an edge.  
    - **Alternatives considered:**  
        - raw finishing positions → biased toward strong teams.  
        - points scored → nonlinear scale, can exaggerate effects.  
    - **Data:** 2022–2025 race results aligned by team + track.  
    - **Visualization:** heatmap with diverging red-green colormap to show over/underperformance clearly.  
    """)
