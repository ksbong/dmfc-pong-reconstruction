# DMFC Pong Reconstruction

Independent reconstruction workspace for studying and reproducing the analysis pipeline of the published MentalPong / DMFC paper.

This repository is used to organize paper-reading notes, data-structure inspection, reconstruction notebooks, and analysis questions related to neural population dynamics during the MentalPong task.

## Original Work

This repository is based on the following published work:

Rajalingham, R., Sohn, H. & Jazayeri, M.  
**Dynamic tracking of objects in the macaque dorsomedial frontal cortex.**  
*Nature Communications* 16, 346 (2025).  
https://doi.org/10.1038/s41467-024-54688-y

Original code repository:  
https://github.com/jazlab/MentalPong

Original data archive:  
https://doi.org/10.5281/zenodo.13952210

This repository is not an official repository of the original authors.  
It is an independent study and reconstruction workspace.

## Purpose

This repository is used to:

- inspect the structure of the released MentalPong dataset
- reconstruct the paper's analysis flow figure by figure
- distinguish figure recreation from analysis-level reconstruction
- document preprocessing, behavioral analysis, neural response analysis, decoding, and model-comparison steps
- record questions that arise during reconstruction
- maintain a reproducible workflow without redistributing original data files

## Reconstruction Policy

This project separates the work into three levels:

1. **Figure recreation**  
   Replotting final values from `Source_Data.xlsx`.

2. **Analysis reconstruction**  
   Recomputing figure values from released metadata, behavioral data, neural responses, or precomputed analysis files.

3. **Extension analysis**  
   Modifying the original analysis to ask additional questions after the original pipeline is understood.

The current priority is **analysis reconstruction**, not simply replotting final source-data values.

## Repository Policy

Original raw data, processed data archives, large `.pkl` / `.mat` files, source-data spreadsheets, PDFs, and other external materials are **not included** in this repository.

The original data should be obtained from the official Zenodo archive or the article's source data.

The local `data/` directory is used only as a placeholder and is excluded from version control.

Expected local structure:

```text
data/
└── external/
    └── MentalPong/
        ├── analyses/
        ├── code/
        ├── data/
        └── README.md
```

## Environment

This project uses [`uv`](https://docs.astral.sh/uv/) for Python environment and dependency management.

Install dependencies:

```bash
uv sync
```

Run scripts:

```bash
uv run python scripts/check_data_structure.py
```

Start Jupyter:

```bash
uv run jupyter notebook
```

## Current Focus

Current reconstruction focus:

1. Inspect released data files and identify their roles
2. Reconstruct Figure 2B trajectories from condition metadata
3. Identify the 79 neurophysiology task-condition subset used in the paper
4. Map Figure 1C behavioral tracking analysis to required variables
5. Inspect neural-response files for Figure 2C reconstruction
6. Treat `Source_Data.xlsx` as a validation reference, not as the primary reconstruction source

## Current Findings

- `valid_meta_sample_full.pkl` contains 200 task conditions with `x0`, `y0`, `dx`, `dy`, and `n_bounce`.
- These variables are sufficient to reconstruct task-coordinate ball trajectories with wall reflection.
- The released DMFC 50 ms dataset contains a 79-condition neurophysiology subset in `dmfc_50ms["meta"]`.
- `behavioral_responses` contains visible and occluded behavioral arrays with shape `(79, 100)`.
- Figure 1C right-panel tracking errors can be recomputed from:
  - `ball_pos_x`, `ball_pos_y`
  - `eye_h`, `eye_v`
  - `paddle_pos_y`
  - `target_y`
  - `t_from_occ`
- The published Figure 1C example conditions were matched to DMFC condition indices:
  - Condition #1 → `24`
  - Condition #2 → `73`
  - Condition #3 → `51`
- `Source_Data.xlsx` is useful as a validation reference and for identifying published example conditions, but analysis reconstruction should rely on released metadata and behavioral/neural arrays whenever possible.

## Directory Structure

```text
notes/       Reading notes, figure mapping, questions, and experiment logs
notebooks/   Jupyter notebooks for data inspection and reconstruction
src/         Reusable Python utilities
scripts/     Small executable scripts
data/        Local-only data directory, not tracked by Git
outputs/     Local-only figures and logs, not tracked by Git
```

## Notebooks

| Notebook | Purpose |
|---|---|
| `00_data_inspection.ipynb` | Initial environment and data-path check |
| `01_source_data_inspection.ipynb` | Workbook-level inspection of `Source_Data.xlsx` |
| `02_fig1_fig2_analysis_reconstruction_map.ipynb` | Metadata and behavior-based reconstruction planning for Figure 1 and Figure 2 |
| `03_fig2c_neural_response_inspection.ipynb` | Initial inspection of neural response arrays for Figure 2C |

## Progress Log

| Date | Progress | Notes |
|---|---|---|
| 2026-05-22 | Initialized repository | Set up uv-based reconstruction workspace |
| 2026-05-23 | Organized local MentalPong data | Stored external files locally under `data/external/MentalPong/` without tracking data files in Git |
| 2026-05-24 | Inspected `Source_Data.xlsx` | Confirmed workbook is organized by figure panels |
| 2026-05-25 | Reconstructed Figure 1C behavior components | Recomputed tracking-error summary and matched example conditions to DMFC indices `[24, 73, 51]` |

## Next Steps

- Polish Figure 1C visualization:
  - time-colored eye points
  - time-colored eye-ball tracking lines
  - black eye-trajectory line
  - correct paddle y-position overlay
- Finalize Figure 1C notes and save the matched condition indices.
- Continue Figure 2C neural-response inspection:
  - response matrix shape
  - neuron axis
  - condition axis
  - time axis
  - example neuron selection
- Map Figure 2E/F to GLM and variance-partitioning outputs before attempting full reconstruction.