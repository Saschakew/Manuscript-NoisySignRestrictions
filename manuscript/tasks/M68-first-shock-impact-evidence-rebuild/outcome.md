# M68 Task Outcome

Status: done.

Completed: 2026-06-12.

## Short Answer

M68 replaces the M67 \((B_{12},B_{21})\) projection with the active
first-shock chart \((B_{11},B_{21})\). All active figures and the Monte Carlo
diagnostic impose \(B_{11}>0\), \(B_{22}>0\), \(B_{12}\le0\), and
\(B_{21}\ge0\), profile \(B_{12}\), \(B_{22}\), and \(\lambda\), and use the
M66 unit-variance route \(\nu_i=\lambda_i(BB')_{ii}\). The outputs are
diagnostic pointwise chi-square inversions; projected critical values remain
M65 follow-up.

## What Changed

- Added the M68 task folder and linked it from `manuscript/task-board.md`.
- Updated `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py`
  so Figures 1-3 use the first-shock projection and common sign screen.
- Added `manuscript/simulations/m68_first_shock_evidence.py` for the Monte
  Carlo diagnostic under the same chart and moment criterion.
- Regenerated:
  - `manuscript/figures/fig_sign_dw_unit_variance_noise_grid.png`
  - `manuscript/figures/fig_sign_dw_unit_variance_nongaussianity_grid.png`
  - `manuscript/figures/fig_sign_dw_unit_variance_sample_size_grid.png`
  - `manuscript/simulations/m68_first_shock_evidence.md`
  - `manuscript/simulations/output/m68_first_shock_evidence.json`
- Updated the replication wrapper so `figure1`, `figure2`, `figure3`,
  `figures`, and `evidence` rebuild the active M68 outputs.
- Updated the draft, registry, source packet, figure/simulation/replication
  READMEs, paper map, dashboard, workplan, task board, logs, and question
  index.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Which coordinates should the active figures report? | \((B_{11},B_{21})\), the first-shock impact coordinates. | `task.md`; `../../draft.md#5-monte-carlo-robustness-check` |
| Are positive diagonal entries sign restrictions? | Yes. M68 treats \(B_{11}>0\) and \(B_{22}>0\) as maintained sign restrictions. | `../../simulations/sign_dw_unit_variance_noise_grid_figure.md` |
| What is the \(B_{12}\) sign restriction? | \(B_{12}\le0\), imposed in figures and Monte Carlo along with \(B_{21}\ge0\). | `../../simulations/m68_first_shock_evidence.md` |
| What still remains open? | The projected critical-value route for the enlarged \((B,\lambda)\) inversion. | `../M65-unit-variance-gmm-evidence-rebuild/task.md` |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Task contract. |
| `../../simulations/sign_dw_unit_variance_noise_grid_figure.md` | Figure 1 diagnostic and configuration. |
| `../../simulations/sign_dw_unit_variance_nongaussianity_grid_figure.md` | Figure 2 diagnostic and configuration. |
| `../../simulations/sign_dw_unit_variance_sample_size_grid_figure.md` | Figure 3 diagnostic and configuration. |
| `../../simulations/m68_first_shock_evidence.md` | Monte Carlo diagnostic table. |
| `../../replication/README.md` | Rebuild commands. |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the active M68 chart answer.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python -m py_compile manuscript\simulations\sign_dw_unit_variance_noise_grid_figure.py manuscript\simulations\m68_first_shock_evidence.py manuscript\replication\run_all.py`: passed.
- `python -m json.tool manuscript\formal-object-registry.json`: passed.
- `python -m json.tool` on all four M68 JSON outputs: passed.
- `python manuscript\replication\run_all.py --stage figure1 --quick`: passed.
- `python manuscript\replication\run_all.py --stage evidence --quick`: passed.
- `python scripts\check_manuscript.py`: passed with the expected open-milestone warning before close.
- `git diff --check`: passed; Git reported only LF-to-CRLF normalization warnings.

## Open Questions Or Follow-Up

- M65 should write the projected critical-value or calibration route for the
  enlarged \((B,\lambda)\) inversion before these diagnostics become final
  confidence-set evidence.
