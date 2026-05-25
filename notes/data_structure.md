# Data Structure Notes

## Local data location

The MentalPong repository and data files are stored locally under:

```text
data/external/MentalPong/
```

This directory is excluded from version control through `.gitignore`.

## Initial file groups
|Group|Path|Notes|
|---|---|---|
|Repository README|`data/external/MentalPong/`README.md|Original project description|
|Figure code|`data/external/MentalPong/code/`|Figure-level notebooks and scripts|
|Analysis utilities|`data/external/MentalPong/analyses/`|Behavioral, decoding, RNN, and single-neuron analysis code|
|Shared utilities|`data/external/MentalPong/utils/`|Helper functions used across scripts|
|Data files|`data/external/MentalPong/data/`|Raw/processed data files, not tracked by Git|

## Initial observation
The dataset contains both small metadata/source files and large `.pkl` / `.mat` files.
For the next step, I will first inspect lightweight metadata and figure-level code before loading large neural response files.

## Next step
- Map paper figures to corresponding notebooks/scripts.
- Inspect `Source_Data.xlsx` and `valid_meta_sample_full.pkl`.
- Identify which data files are required for the first reconstruction target.

### 2026-05-25

**Goal**

Inspect behavioral and metadata files required for Figure 1C reconstruction.

**What I tried**

- Loaded `valid_meta_sample_full.pkl` and confirmed that it contains the full 200-condition task metadata.
- Loaded the `all_hand_dmfc_dataset_50ms.pkl`-style DMFC dataset and inspected:
  - `meta`
  - `behavioral_responses`
  - `neural_responses_reliable`
- Separated visible and occluded behavioral responses.
- Confirmed that behavioral response dictionaries contain:
  - `ball_pos_x`, `ball_pos_y`
  - `ball_pos_x_TRUE`, `ball_pos_y_TRUE`
  - `eye_h`, `eye_v`
  - `paddle_pos_y`
  - `target_y`
  - `t_from_occ`

**Result**

The behavioral response arrays are organized as `(79, 100)`, where the first axis corresponds to the 79 neurophysiology task conditions and the second axis corresponds to time bins.

**What I learned**

`Source_Data.xlsx` is useful for identifying published figure examples, but the reconstruction should use the released metadata and behavioral-response arrays whenever possible.

For Figure 1C, the published example-condition ball trajectories were first extracted from `Source_Data.xlsx`, then matched against trajectories reconstructed from `dmfc_50ms["meta"]`.

**Matched Figure 1C example conditions**

| Figure 1C panel | Matched dmfc condition index | Matching method |
|---|---:|---|
| Condition #1 | 24 | SourceData ball trajectory vs metadata-reconstructed trajectory |
| Condition #2 | 73 | SourceData ball trajectory vs metadata-reconstructed trajectory |
| Condition #3 | 51 | SourceData ball trajectory vs metadata-reconstructed trajectory |

**Next step**

- Polish Figure 1C left-panel visualization.
- Save the condition-matching result in `figure_mapping.md`.
- Move on to Figure 2C neural-response inspection.