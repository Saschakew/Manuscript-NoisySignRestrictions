# M71 Task Outcome

Status: done.

Completed: 2026-06-12.

## Short Answer

M71 corrected the active evidence object. Figures 1-3, the Table 1 diagnostic,
and the extended MC now keep the first-shock projection \((B_{11},B_{21})\),
profile \(B_{12}\), \(B_{22}\), and \(\lambda\), impose only
\(B_{11}>0\), \(B_{22}>0\), and \(B_{12}\le0\), and compute the inverted
statistics with candidate-specific pointwise covariance weights. The outputs
remain diagnostic pointwise chi-square inversions; final projected critical
values remain M65 follow-up, and the long 500-replication MC remains deferred.

## What Changed

- Updated `../../simulations/sign_dw_unit_variance_noise_grid_figure.py` to
  remove the \(B_{21}\) sign screen, compute pointwise covariance weights at
  each tested candidate, and report regularization diagnostics in JSON.
- Updated `../../simulations/m68_first_shock_evidence.py` and
  `../../simulations/m69_extended_three_block_mc.py` to use the corrected
  evaluator and corrected metadata.
- Updated `../../replication/run_all.py` and replication/simulation READMEs for
  the M71 corrected wrapper behavior.
- Regenerated Figures 1-3, `m68_first_shock_evidence` output, and
  `m69_extended_three_block_mc` output after quick smoke checks.
- Updated the draft, formal registry, source packet, paper map, dashboard,
  task board, question index, decision/session/Codex logs, and the historical
  M68/M69 outcome notes.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Should \(B_{21}\ge0\) remain in the active sign screen? | No. Active evidence keeps only \(B_{11}>0\), \(B_{22}>0\), and \(B_{12}\le0\). | `../../simulations/sign_dw_unit_variance_noise_grid_figure.md`; `../../draft.md#5-monte-carlo-robustness-check` |
| Should the inverted statistic use a true-point fixed weight? | No. Each tested candidate estimates its own pointwise covariance matrix and uses \(Tg_T'\widehat\Omega(B,\nu)^{-1}g_T\). | `../../simulations/sign_dw_unit_variance_noise_grid_figure.py` |
| Does M70 remain blocked? | No. Corrected outputs now exist, so M70 can interpret them while keeping reduced diagnostic replication counts and pointwise-critical-value caveats visible. | `../../task-board.md`; `../../project-dashboard.md` |
| Was the 500-replication MC run? | No. M71 ran quick and normal diagnostics only; the long run remains deferred. | `task.md`; `../../replication/README.md` |

## Output Snapshot

The corrected Table 1 diagnostic used 6 replications per scenario, a
`13 x 13` projection grid, a `5 x 5` profile grid, and a `3 x 3` lambda grid.

| Scenario | Standard truth | Robust truth | Warning | Sign share | Standard share | Robust share |
|---|---:|---:|---:|---:|---:|---:|
| No noise, strong moments | 0.667 | 0.500 | 0.000 | 0.048 | 0.020 | 0.035 |
| Moderate Gaussian noise | 0.167 | 0.667 | 0.667 | 0.051 | 0.019 | 0.060 |
| High Gaussian noise | 0.000 | 0.667 | 0.667 | 0.065 | 0.023 | 0.082 |
| Weak structural higher moments | 0.000 | 0.833 | 0.833 | 0.028 | 0.016 | 0.092 |
| Gaussian structural shocks | 0.000 | 0.833 | 0.833 | 0.027 | 0.020 | 0.090 |
| Skewed residual noise | 0.333 | 0.833 | 0.667 | 0.052 | 0.020 | 0.058 |

The corrected extended MC used 8 replications per scenario, a `13 x 13`
projection grid, a `5 x 5` profile grid, and a `3 x 3` lambda grid. The
residual-noise block reports standard/robust truth rates of `0.750/0.500` at
`V=(0,0)`, `0.250/0.625` at `V=(0.2,0.2)`, and `0.000/0.750` at
`V=(0.5,0.5)`. The non-Gaussianity block reports `0.000/0.500`,
`0.000/1.000`, and `0.000/0.875` for `w=1`, `w=0.25`, and `w=0`. The
sample-size block reports `0.125/0.500`, `0.000/0.750`, and `0.000/0.625`
for `T=500`, `T=1000`, and `T=2000`.

Regularization diagnostics are recorded in the JSON outputs. Robust full-stack
regularization was not active in the quick/normal summaries examined; some
second-moment and standard-DW candidate covariances required eigenvalue
flooring.

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Original correction contract and acceptance criteria. |
| `../../simulations/sign_dw_unit_variance_noise_grid_figure.md` | Figure 1 diagnostic and corrected configuration. |
| `../../simulations/sign_dw_unit_variance_nongaussianity_grid_figure.md` | Figure 2 diagnostic and corrected configuration. |
| `../../simulations/sign_dw_unit_variance_sample_size_grid_figure.md` | Figure 3 diagnostic and corrected configuration. |
| `../../simulations/m68_first_shock_evidence.md` | Corrected Table 1 diagnostic. |
| `../../simulations/m69_extended_three_block_mc.md` | Corrected extended MC diagnostic. |
| `../../replication/README.md` | Rebuild commands. |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the M71 active chart,
  sign-screen, weighting, and extended-MC answer.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python -m py_compile manuscript\simulations\sign_dw_unit_variance_noise_grid_figure.py manuscript\simulations\m68_first_shock_evidence.py manuscript\simulations\m69_extended_three_block_mc.py manuscript\replication\run_all.py`: passed.
- Quick wrapper runs passed for `figure1`, `figure2`, `figure3`, `evidence`,
  and `extended-mc`.
- Normal wrapper runs passed for `figure1`, `figure2`, `figure3`, `evidence`,
  and `extended-mc`.
- `python -m json.tool` passed for the corrected Figure 1-3, Table 1, extended
  MC, and formal-registry JSON files.
- Boundary scans passed for the normal Figure 1-3 JSON outputs after expanding
  the plotted \(B_{21}\) range.
- Final manuscript and diff checks are recorded in the milestone closeout.

## Open Questions Or Follow-Up

- M70 should interpret the corrected extended MC output in the draft.
- M65 still owns projected critical values, final confidence-set wording, and
  release hardening.
- The long 500-replication MC remains deferred until the user asks for that
  heavier run.
