### 2026-05-23

**Goal**

Download and organize the MentalPong repository/data locally without tracking private or large data files in Git.

**What I tried**

- Downloaded the full MentalPong archive.
- Extracted the contents under `data/external/MentalPong/`.
- Removed unnecessary macOS metadata/cache files when applicable.
- Confirmed that local data files are excluded from version control.
- Ran the initial data structure check script.

**Result**

The external MentalPong files are available locally, while raw data and large files remain untracked by Git.

**What I learned**

The repository contains figure-level notebooks/scripts, analysis utilities, and multiple large `.pkl` / `.mat` files.  
The next step should be figure mapping and lightweight metadata inspection rather than immediately loading all large data files.

**Next step**

Start from `Source_Data.xlsx`, `valid_meta_sample_full.pkl`, and the figure notebooks in `code/`.