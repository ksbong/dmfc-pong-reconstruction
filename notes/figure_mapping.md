# Figure Mapping

## Goal

Map each paper figure to the corresponding data, script, notebook, and analysis logic.

| Paper Figure | Analysis Goal | Data Used | Code / Notebook | Current Status |
|---|---|---|---|---|
| Figure 1 | Reconstruct behavioral task structure and Figure 1C tracking analysis | `Source_Data.xlsx`, `valid_meta_sample_full.pkl`, `dmfc_50ms["meta"]`, `behavioral_responses` | `02_fig1_fig2_analysis_reconstruction_map.ipynb` | In progress — Figure 1C mostly reconstructed |
| Figure 2 | Reconstruct task-condition trajectories and inspect neural response examples | `valid_meta_sample_full.pkl`, `dmfc_50ms["meta"]`, `neural_responses_reliable` | `02_fig1_fig2_analysis_reconstruction_map.ipynb`, `03_fig2c_neural_response_inspection.ipynb` | In progress — Figure 2B/2C inspection started |
| Figure 3 | Map population-level analyses and latent dynamics reconstruction | TBD | TBD | Not started |
| Figure 4 | Map decoding / model comparison analyses | TBD | TBD | Not started |

## Notes

## Figure 1C — Behavioral reconstruction

### Panel meaning

Figure 1C consists of two parts:

1. **Left panels**
   - Three example task conditions.
   - Ball trajectory.
   - Eye positions over time.
   - Eye-ball tracking-error lines.
   - Paddle y-position drawn at the corresponding ball x-position.

2. **Right panel**
   - Tracking error over time from occlusion start.
   - Eye-ball tracking error.
   - Paddle-target tracking error.
   - Mean ± SEM across task conditions.

### Data dependency

| Component | Data source | Variables |
|---|---|---|
| Example condition identity | `Source_Data.xlsx` + `dmfc_50ms["meta"]` | ball trajectory |
| Ball trajectory | `dmfc_50ms["meta"]` / behavioral responses | `x0`, `y0`, `dx`, `dy`, wall reflection |
| Eye position | `behavioral_responses` | `eye_h`, `eye_v` |
| Paddle position | `behavioral_responses` | `paddle_pos_y` |
| Tracking-error summary | `behavioral_responses` | `ball_pos_x`, `ball_pos_y`, `eye_h`, `eye_v`, `paddle_pos_y`, `target_y`, `t_from_occ` |

### Current reconstruction status

- The right-panel tracking-error summary was reconstructed from `behavioral_responses`.
- The left-panel example conditions were identified by matching SourceData ball trajectories against trajectories reconstructed from `dmfc_50ms["meta"]`.
- Matched condition indices:
  - Condition #1 → dmfc condition `24`
  - Condition #2 → dmfc condition `73`
  - Condition #3 → dmfc condition `51`

### Notes

The left-panel example reconstruction should avoid plotting all behavioral time bins.  
Only time points corresponding to the published SourceData ball trajectory should be used; otherwise unrelated behavioral samples are mixed into the panel.