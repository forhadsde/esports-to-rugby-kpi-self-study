# Tasks

Tick each box when done and add a line to `PROGRESS_LOG.md`. Keep to the order; each step feeds the next.

## 0. Setup
- [ ] Create the conda env from `environment.yml` and check `python -c "import sklearn, xgboost, shap, torch"` works.
- [ ] Download the papers listed in `BACKGROUND.md` into `papers/` (open access where possible) and write a half page summary of each in `docs/PAPER_NOTES.md`: data, features, models, metrics, key numbers, limitations.
- [ ] Confirm each dataset in `DATA_SOURCES.md`: still online, licence, size. Record the download date. Pick the final datasets for Part A and Part B.

## Part A: reproduce and improve her League of Legends KPI work
- [ ] `notebooks/01_lol_data.ipynb`: download, clean and describe the data (games, ranks or leagues, patches, missing values). Save `data/processed/lol_*.parquet`.
- [ ] `notebooks/02_lol_reproduce.ipynb`: reproduce her setup as closely as the public data allows: win prediction at several game time points, neural network plus Random Forest, XGBoost and logistic regression baselines, KPI ranking. Compare with her reported numbers (about 97% accuracy, turrets lost, bounty, dragons, damage taken) and explain any differences honestly.
- [ ] `notebooks/03_lol_improve.ipynb`, at least three of:
  - leakage safe evaluation (split by game and by patch or league), and accuracy at 10, 15, 20 minutes rather than end of game only
  - SHAP explanations and how KPI importance changes over game time
  - calibration (reliability plot, Brier score) and uncertainty across 3 or more seeds
  - stability of KPI rankings across bootstrap samples
- [ ] Save every number to `outputs/results/A_*.json` and figures to `outputs/figures/A_*.png`.

## Part B: transfer the pipeline to rugby union
- [ ] `notebooks/04_rugby_data.ipynb`: build a match level table (team stats per match: tackles made and missed, carries, metres, line breaks, turnovers won and conceded, penalties, set piece success, kicks, possession, territory), with home or away and result.
- [ ] `notebooks/05_rugby_kpis.ipynb`: same pipeline as Part A: win prediction with differenced team stats (team minus opponent), feature selection, SHAP, stability, leakage safe split by season.
- [ ] Compare KPIs between competitions if more than one is available (for example Six Nations against club leagues), and between seasons before and after law changes if the data allows.
- [ ] Save `outputs/results/B_*.json` and `outputs/figures/B_*.png`.

## Part C (optional stretch): rugby video detection
- [ ] Only use video and labels whose licence allows research use. Label about 30 to 100 frames.
- [ ] Fine tune a small detector (for example YOLO nano), compare random against lowest confidence frame selection, as in Connors, Rushe and Ventresque (ECAI 2024).
- [ ] Quantise to INT8 and report accuracy and speed before and after.

## Write up
- [ ] Update `README.md` with tables and figures, limitations and next steps.
- [ ] Write `report/main.tex` (IEEE conference style, 4 to 6 pages): abstract, introduction, related work, method, setup, results, limitations, conclusion, references. Compile to `report/Islam_Sports_KPI_Report.pdf`.
- [ ] Check every number in the README and report against `outputs/results/`.
- [ ] Draft `docs/EMAIL_DRAFT.md` to Dr Hojaji (see `BACKGROUND.md` for tone and the Kolb email model).
- [ ] Ask Forhad before creating the public GitHub repository.
