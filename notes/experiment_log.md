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

### 2026-05-24

**Goal**

Inspect the structure of `Source_Data.xlsx`.

**What I tried**

- Opened the workbook with pandas.
- Listed all sheet names.
- Previewed `Figure 2C` with `header=None`.
- Built a sheet-level summary table with shape, non-empty cell count, and preview values.

**Result**

The workbook contains 44 sheets organized by figure panels.  
It appears to be figure-level source data rather than raw neural recording data.

**Next step**

Classify sheets by analysis type and map them to the corresponding figure notebooks/scripts.


### 2026-05-25 — Figure 1C behavior reconstruction

**Goal**

Reconstruct Figure 1C at the analysis level rather than simply replotting final SourceData values.

**Progress**

- Located Figure 1C-related behavioral arrays inside the DMFC 50 ms dataset.
- Confirmed that `behavioral_responses` contains visible and occluded behavioral dictionaries.
- Recomputed the right-panel tracking-error summary:
  - eye-ball error
  - paddle-target error
  - mean ± SEM over conditions
- Parsed the Figure 1C example-condition ball trajectories from `Source_Data.xlsx`.
- Matched those trajectories against trajectories reconstructed from `dmfc_50ms["meta"]`.
- Identified the three example-condition indices:
  - `[24, 73, 51]`

**Important debugging notes**

- Directly matching SourceData trajectories to `bh_occ` or `bh_vis` arrays was misleading because those arrays are epoch-aligned behavioral samples.
- The correct condition identity matching was performed using metadata-reconstructed ball trajectories.
- Plotting all valid eye samples from a condition mixes unrelated time bins into the left panel.
- The left panel should use only time indices corresponding to the SourceData trajectory points.

**Current result**

Figure 1C is mostly reconstructed:
- right tracking-error panel: working
- left example-condition panel: working, needs visual polishing

**Next**

- Finalize Figure 1C plotting style.
- Add color-matched tracking-error lines.
- Add eye trajectory line.
- Then continue to Figure 2C neural-response inspection.

### 2026-05-26 — Figure 2C neural response traces

Reconstructed the visible and occluded epoch response traces for four example units:
- P305
- M39
- P113
- M294

The labels correspond to subject-specific reliable neuron indices:
- P: Perle
- M: Mahler

The response traces were drawn from `neural_responses_reliable["occ"]`.
Visible and occluded epoch masks were reconstructed from behavioral time variables:
- visible: `t_from_start >= 0` and `t_from_occ <= 0`
- occluded: `t_from_occ >= 0` and `t_from_end <= 0`

Current status:
- Figure 2C trace columns reconstructed.
- Spatial modulation heatmap column remains.