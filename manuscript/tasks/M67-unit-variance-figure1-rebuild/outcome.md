# M67 Task Outcome

Status: done.

Completed: 2026-06-12.

## Short Answer

Built the corrected Figure 1. The new image is
`manuscript/figures/fig_sign_dw_unit_variance_noise_grid.png`. It does not use
the old `diag(B)=1` B-plane. It projects accepted matrices to
\((B_{12},B_{21})\), profiles \(B_{11}\), \(B_{22}\), and
\(\lambda\in[0,\rho]^2\), and evaluates the Section 4 moment vector with
\(\nu_i=\lambda_i(BB')_{ii}\).

## What Changed

- Added `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py`.
- Generated `manuscript/figures/fig_sign_dw_unit_variance_noise_grid.png`.
- Generated `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.md`
  and `manuscript/simulations/output/sign_dw_unit_variance_noise_grid_figure.json`.
- Updated `manuscript/draft.md` so Figure 1 is no longer historical.
- Updated the replication wrapper so `python manuscript/replication/run_all.py
  --stage figure1` rebuilds the M67 figure.
- Updated the registry, source packet, paper map, dashboard, READMEs, M65
  packet, question index, and logs.

## Questions Answered

| Question | Short answer | Where |
|---|---|---|
| What is the correct updated Figure 1? | The M67 unit-variance projected residual-noise grid. | `manuscript/figures/fig_sign_dw_unit_variance_noise_grid.png` |
| Does it still impose `diag(B)=1`? | No. It profiles positive \(B_{11}\) and \(B_{22}\) for each displayed \((B_{12},B_{21})\) projection point. | `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` |
| Does the robust row use the M66 algorithm? | Yes. It searches over \(\lambda\in[0,\rho]^2\), sets \(\nu_i=\lambda_i(BB')_{ii}\), and evaluates the Section 4 moment vector. | `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.md` |
| Is M65 complete now? | No. Figure 1 is rebuilt; Figure 2, Figure 3, the Monte Carlo table, and the final projection-critical-value route remain open. | `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/task.md` |

## Files To Read

| Path | Why |
|---|---|
| `manuscript/figures/fig_sign_dw_unit_variance_noise_grid.png` | Corrected Figure 1 image. |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` | Reproducible generator. |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.md` | Diagnostics, chart interpretation, and claim audit. |
| `manuscript/simulations/output/sign_dw_unit_variance_noise_grid_figure.json` | Machine-readable diagnostics. |
| `manuscript/draft.md` | Updated Section 5.1 figure text. |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the corrected Figure 1 answer.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python -m py_compile manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py manuscript/replication/run_all.py`: passed.
- `python -m json.tool manuscript/formal-object-registry.json`: passed.
- `python -m json.tool manuscript/simulations/output/sign_dw_unit_variance_noise_grid_figure.json`: passed.
- `python manuscript/replication/run_all.py --stage figure1 --quick`: passed.
- `python scripts/check_manuscript.py`: passed.
- `git diff --check`: passed; Git reported only line-ending normalization notices.

## Open Questions Or Follow-Up

- M65 remains open for Figure 2, Figure 3, the Monte Carlo table, and the
  final projected critical-value/inference route.
