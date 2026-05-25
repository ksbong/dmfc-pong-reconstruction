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
- The reconstructed full 200-condition trajectory set qualitatively matches the structure of Figure 2B.
- The paper's neurophysiology figures use a 79-condition subset, so the exact subset index still needs to be identified.
- `Source_Data.xlsx` appears to be figure-panel-level source data and is useful for validation / answer-checking rather than primary reconstruction.

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
| `02_fig1_fig2_analysis_reconstruction_map.ipynb` | Metadata-based reconstruction planning for Figure 1 and Figure 2 |

## Progress Log

| Date | Progress | Notes |
|---|---|---|
| 2026-05-22 | Initialized repository | Set up uv-based reconstruction workspace |
| 2026-05-23 | Organized local MentalPong data | Stored external files locally under `data/external/MentalPong/` without tracking data files in Git |
| 2026-05-24 | Inspected `Source_Data.xlsx` | Confirmed workbook is organized by figure panels |
| 2026-05-25 | Started analysis-level reconstruction | Loaded metadata, resolved pandas/pickle compatibility, and reconstructed 200-condition ball trajectories from `x0`, `y0`, `dx`, `dy`, and `n_bounce` |

## Next Steps

- Identify the exact 79-condition subset used for neurophysiology analyses.
- Compare reconstructed trajectories against Figure 2B reference values.
- Search for behavioral variables required for Figure 1C:
  - ball position
  - eye position
  - paddle position
  - target endpoint
  - occlusion timing
- Inspect neural-response files for Figure 2C:
  - response matrix shape
  - condition axis
  - time axis
  - neuron/session metadata
- Map Figure 2E/F to GLM and variance-partitioning outputs before attempting full reconstruction.