import streamlit as st
from pathlib import Path
import fastf1, os
fastf1.Cache.enable_cache('/tmp/fastf1')
os.makedirs('/tmp/fastf1', exist_ok=True)

st.set_page_config(page_title="ShowsSpeed: Home", page_icon="🏎️", layout="wide")

st.markdown("""
<style>
.topbar{
  position:sticky; top:0; z-index:9999;
  display:flex; align-items:center; gap:20px;
  padding:16px 24px; height:100px; 
  background:linear-gradient(180deg,#14141b 0%, #111118 50%, #0e0e15 100%);
  border-bottom:4px solid #E63946;
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

.big-text{font-size:48px !important; line-height:1.6;}

section[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] span{font-size:26px !important;}
section[data-testid="stSidebar"] .css-1d391kg::before{
  content:"ShowsSpeed: Home"; font-size:28px; font-weight:800; color:#E63946; display:block; margin:8px 0 16px 0;
}
section[data-testid="stSidebar"] .css-1d391kg>span{display:none;}

.contact-links a{
  display:block;
  margin:4px 0;
  text-decoration:none;
  color:#F5F5F5;       /* white normal text */
  font-weight:400;
  font-size:18px;
}
.contact-links a:hover{color:#E63946;} /* red on hover */
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar"><div class="brand">🏁 <span>ShowsSpeed: F1 Data Science Project</span></div></div>
<div class="blockpad"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="big-text">

### Exploring all things F1 through data science!  

Documenting my journey in:  
- scraping lap-by-lap telemetry  
- cleaning, organizing, & synthesizing 40+ datasets  
- exploratory data analysis  
- engineering new features  
- building models that predict lap times and pit stop strategies  
- **2 Polished ML Models**:  
  - Lap Time Predictor (baseline → ML variants)  
  - Pit Stop Strategist (classify best windows/strategies)  

---

### Repo Guide  
- **ShowsSpeed.ipynb** – EDA + models  
- **FastF1_Scraper.ipynb** – data acquisition recipe  
- **data/** – raw/interim/processed (gitignored)  
- **models/** – saved artifacts (gitignored)  

---

### Data Sources  
- [f1db](https://github.com/f1db/f1db) – general, 40+ datasets on every Grand Prix since 1950  
- [FastF1](https://theoehrly.github.io/Fast-F1/) – for lap-by-lap telemetry, stints, and timing data  

---

### Contact  
<div class="contact-links">
<a href="tel:6266770875">626 677 0875</a>  
<a href="mailto:showhq2@gmail.com">showhq2@gmail.com</a>  
<a href="mailto:tian.ruy@northeastern.edu">tian.ruy@northeastern.edu</a>  
<a href="https://github.com/showssteamrolls" target="_blank">github.com/showssteamrolls</a>  
</div>

</div>
""", unsafe_allow_html=True)

st.info("All analysis is experimental, not official FIA stats.")
