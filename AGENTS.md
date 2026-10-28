# Instructions for any agent working in this folder

Read this file first, then `README.md`, then `docs/TASKS.md`. Work through the tasks in order and tick them off in `docs/TASKS.md` as you finish each one. Log every working session in `docs/PROGRESS_LOG.md`.

## Who this is for

Md Forhadul Islam (Forhad), AI Engineer in London, applying for a PhD with **Dr Fazilat Hojaji**, Associate Professor, Department of Computer Science and Information Systems and Lero, University of Limerick. Forhad had a good interview with her on 28 October 2026. She suggested he strengthen his statistics and data analysis, and her new PhD is expected to be on **AI for rugby**.

This is a self study, like his two earlier ones:
* FPFLI 4 bit study on Dr David Li's code (University of Strathclyde): https://github.com/forhadsde/fpfli-32bit-to-4bit-weights-near-full-precision
* THz MIMO SAR warm start study on Prof Andreas Kolb's code (University of Siegen): https://github.com/forhadsde/THz_MIMO_SAR

Use those two repositories as the model for structure, honesty and the report style.

## The goal

1. **Part A, reproduce her method:** reproduce Dr Hojaji's esports KPI work (League of Legends win prediction and KPI identification) on public data, then improve it.
2. **Part B, transfer it to rugby:** apply the same KPI pipeline to public rugby union match statistics.
3. **Part C (optional stretch):** a small rugby tackle or player detector on a few labelled video frames, then compress it (INT8) for edge use.
4. Deliver a public GitHub repository and a 4 to 6 page IEEE style report (LaTeX, `report/`), so Forhad can send it to Dr Hojaji and reuse it with other supervisors.

## Hard rules

* **Writing style:** never use a dash or long dash as punctuation in any text Forhad will send or publish (README, report, emails, slides). Write in a polite, warm, human tone. Use British spelling.
* **Honesty:** every number in the README and report must come from a file in `outputs/results/` produced by code in this folder. Never invent results, accuracy figures or citations. State limitations plainly.
* **Credit:** always name and cite Dr Hojaji and her coauthors for the method you reproduce, and the owners of every dataset.
* **Licences:** only use data whose licence allows research use. Record the source, licence and download date of every dataset in `docs/DATA_SOURCES.md`. Do not commit raw data to GitHub unless the licence clearly allows redistribution; otherwise commit a download script.
* **Evaluation:** split by game or match and, where possible, by player or team or season, so no leakage. Use a held out test set touched only once. Report spread across at least 3 random seeds.
* **Git author:** commits must be authored by `Md Forhadul Islam <forhadreza1596@gmail.com>`. Do not add any AI co author lines.
* **Ask before sending:** never send an email, post publicly or publish a repository without Forhad confirming. Drafts are fine.
* Do not edit files outside this folder.

## Environment

* Forhad's PC: Windows 11, NVIDIA RTX 3090, Anaconda. Create the env with `environment.yml`.
* Keep notebooks runnable top to bottom, with outputs saved. Shared code goes in `src/`.
* Seeds fixed in `src/common.py`.

## Definition of done

* All tasks in `docs/TASKS.md` ticked.
* `README.md` updated with results tables and figures.
* `report/main.tex` compiles to a PDF of 4 to 6 pages.
* A short draft email to Dr Hojaji in `docs/EMAIL_DRAFT.md`, modelled on Forhad's email to Prof Kolb (summarised in `docs/BACKGROUND.md`).
