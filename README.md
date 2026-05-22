# DMFC Pong Reconstruction

Private reconstruction workspace for organizing paper-reading notes, analysis code, and questions related to the DMFC Pong dataset and paper.

## Purpose

This repository is used to:

- inspect the structure of the shared dataset
- reconstruct the paper's analysis flow figure by figure
- document preprocessing, dimensionality reduction, decoding, and visualization steps
- record questions that arise during reconstruction
- maintain a reproducible analysis workflow without uploading private data or unpublished materials

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

## Repository Policy

Raw data, processed data, unpublished manuscripts, and other private materials are **not included** in this repository.

The `data/` directory is used only as a local placeholder and is excluded from version control.

## Current Focus

1. Inspect dataset structure
2. Map paper figures to analysis scripts or notebooks
3. Reconstruct one analysis pipeline at a time
4. Compare reproduced outputs with the paper's interpretation
5. Summarize questions for future discussion

## Directory Structure

```text
notes/       Reading notes, figure mapping, questions, and experiment logs
notebooks/   Jupyter notebooks for data inspection and reconstruction
src/         Reusable Python utilities
scripts/     Small executable scripts
data/        Local-only data directory, not tracked by Git
outputs/     Local-only figures and logs, not tracked by Git
```

## Progress Log

| Date | Progress | Notes |
|---|---|---|
| 2026-05-22 | Initialized repository | Set up private reconstruction workspace with uv |