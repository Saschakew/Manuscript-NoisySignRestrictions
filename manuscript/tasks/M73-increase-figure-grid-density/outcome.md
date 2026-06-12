# M73 Increase Figure Grid Density Outcome

Status: completed.

Completed: 2026-06-12.

## Short Answer

Figures 1-3 were regenerated with denser default grids: `41 x 41` projection
points, `11 x 11` profiled `B12/B22` points, and `7 x 7` lambda points, with
true coordinates and scenario-specific true lambda values still appended. The
M71 sign screen, M71 candidate-specific pointwise weighting, and M72 square
panel layout were preserved.

## What Changed

- `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py`: raised
  the active figure defaults from `31/9/5` to `41/11/7`.
- `manuscript/figures/fig_sign_dw_unit_variance_noise_grid.png`: regenerated
  Figure 1 with the denser grid.
- `manuscript/figures/fig_sign_dw_unit_variance_nongaussianity_grid.png`:
  regenerated Figure 2 with the denser grid.
- `manuscript/figures/fig_sign_dw_unit_variance_sample_size_grid.png`:
  regenerated Figure 3 with the denser grid.
- `manuscript/simulations/sign_dw_unit_variance_*_grid_figure.md` and
  `manuscript/simulations/output/sign_dw_unit_variance_*_grid_figure.json`:
  refreshed diagnostics and recorded the denser configuration.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Can Figures 1-3 be regenerated with more grid points? | Yes. All three active figures now use `41 x 41` projection, `11 x 11` profile, and `7 x 7` lambda grids. | `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.md`; `manuscript/simulations/sign_dw_unit_variance_nongaussianity_grid_figure.md`; `manuscript/simulations/sign_dw_unit_variance_sample_size_grid_figure.md` |
| Did the denser rebuild change the method? | No. It preserves the M71 sign screen and pointwise weighting and the M72 display layout; only the grid density and resulting fixed-draw masks/shares changed. | `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Task contract |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` | Active Figure 1-3 generator and grid defaults |
| `manuscript/simulations/output/sign_dw_unit_variance_noise_grid_figure.json` | Figure 1 diagnostics configuration and fixed-draw results |
| `manuscript/simulations/output/sign_dw_unit_variance_nongaussianity_grid_figure.json` | Figure 2 diagnostics configuration and fixed-draw results |
| `manuscript/simulations/output/sign_dw_unit_variance_sample_size_grid_figure.json` | Figure 3 diagnostics configuration and fixed-draw results |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: not needed; this was an execution request,
  and the outcome note plus diagnostics paths are sufficient.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python manuscript/replication/run_all.py --stage figures`: interrupted
  after Figure 1 and Figure 2 finished.
- `python manuscript/replication/run_all.py --stage figure3`: Figure 3 wrote
  successfully, but the wrapper command timed out while returning control.
- Diagnostics verification: all three JSON files report
  `projection_points=41`, `profile_points=11`, and `lambda_points=7`.
- `python scripts/check_manuscript.py`: passed, with the expected warning
  that M0069 was still open before close.

## Open Questions Or Follow-Up

- M65 still owns final projected critical values and release-hardening. The
  denser grid does not settle that inference question.
