# ShowsSpeed
Exploring all things F1 through data science! Documenting my journey in:
- scraping lap-by-lap telemetry
- cleaning, organizing, & synthesizing 40+ datasets
- exploratory data analysis
- engineering new features
- building models that predict lap times and pit stop strategies.
- 2 Polished ML Models:
  - Lap Time Predictor (baseline → ML variants)
  - Pit Stop Strategist (classify best windows/strategies)

## Repo Guide
- ShowsSpeed.ipynb – EDA + models
- FastF1_Scraper.ipynb – data acquisition recipe
- data/ – raw/interim/processed (gitignored)
- models/ – saved artifacts (gitignored)

## Data Sources
- [f1db]((https://github.com/f1db/f1db)) – general, 40+ datasets on every Grand Prix since 1950
- [FastF1](https://theoehrly.github.io/Fast-F1/) – for lap-by-lap telemetry, stints, and timing data  
