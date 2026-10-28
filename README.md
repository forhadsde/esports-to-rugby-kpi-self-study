# From esports to rugby: explainable KPI discovery for team sports

**Author:** Md Forhadul Islam, London

**Status:** project set up, work not started. Results tables below will be filled in from `outputs/results/`.

This is a short independent study that builds on the work of **Dr Fazilat Hojaji** and colleagues at the University of Limerick Esports Science Research Lab, in particular:

* F. Hojaji, R. E. Mcilroy, A. Dupuy, G. Pedroni, A. J. Toth and M. J. Campbell, "Deep learning techniques for identifying KPIs in League of Legends: Win prediction, map navigation, and vision control", *Computers in Human Behavior Reports*, 19, 100718, 2025.
* F. Hojaji, R. E. McIlroy, B. Majeed, A. Dupuy, A. J. Toth and M. J. Campbell, "Understanding Competitive Skill in League of Legends: A Team Rank Based Analysis of Behaviour, Communication, and Spatial Decision Making in European Ranked Play", *Frontiers in Sports and Active Living*, 8, 2026.
* F. Hojaji, A. J. Toth, J. M. Joyce and M. J. Campbell, "AI enabled prediction of sim racing performance using telemetry data", *Computers in Human Behavior Reports*, 14, 100414, 2024.

## Questions

1. **Part A:** Can her KPI pipeline be reproduced on public League of Legends data, and does it still hold with a leakage safe split, uncertainty across seeds, and explanations over game time?
2. **Part B:** Does the same pipeline find meaningful, stable KPIs for winning in elite rugby union, and do they differ between competitions?
3. **Part C (stretch):** Can a small detector find tackles or players in rugby video from very few labelled frames, and still work at 8 bit?

## Structure

| Folder | What goes there |
|---|---|
| `docs/` | Brief, tasks, data sources, background, progress log, email draft |
| `data/raw/` | Downloaded data (not committed unless the licence allows) |
| `data/processed/` | Cleaned tables |
| `notebooks/` | Numbered notebooks, run top to bottom with outputs saved |
| `src/` | Shared code |
| `outputs/` | `figures/`, `results/` (JSON with every number), `models/` |
| `report/` | IEEE style LaTeX report |
| `papers/` | PDFs of the papers being reproduced (not committed) |

## Results

To be filled in.

## Limitations

To be filled in.

## Credits

The method follows Dr Hojaji and colleagues (University of Limerick). Datasets are credited in `docs/DATA_SOURCES.md`.
