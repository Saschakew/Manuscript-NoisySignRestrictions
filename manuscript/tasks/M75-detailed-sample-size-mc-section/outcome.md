# M75 Detailed Sample-Size MC Section Outcome

Status: done.

Completed: 2026-06-14.

## Short Answer

`draft.md` now contains a detailed sample-size Monte Carlo subsection for the
completed M74 run. The new section states the exact DGP, grid ranges, appended
true coordinates and true \(\lambda\) values, sign screen, profiled
coordinates, moment rows, pointwise J distributions and cutoffs, efficient
weight construction, and the coverage/set-size/warning results for
`T=500`, `T=1000`, and `T=2000`.

## What Changed

- Added `../../draft.md#55-detailed-sample-size-monte-carlo`.
- Added Table 2 with M74 500-replication truth-inclusion, accepted projection
  size, empty-set, and warning rates.
- Verified the generated M74 Markdown table against the JSON summaries before
  drafting.
- Added a formal registry object
  `table:sample-size-mc-coverage-size-power`.
- Updated `../../citation-provenance.md`, `../../source-packet.md`,
  `../../paper-map.md`, `../../project-dashboard.md`, `../../task-board.md`,
  and `../../QUESTION-INDEX.md`.
- Updated the M74 outcome to mark the background run complete and interpreted.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| What exactly is the M74 DGP and estimator computation? | The DGP uses \(B_0=[[1,-0.25],[0.80,1]]\), standardized \(\chi^2_5\) structural shocks, Gaussian residual noise with \(V=\operatorname{diag}(0.2,0.2)\), and de-meaned observed residuals. The estimators use the M71 first-shock chart, the `27/7/5` grid, candidate-specific pointwise weights, and chi-square diagnostic cutoffs for the displayed moment rows. | `../../draft.md#55-detailed-sample-size-monte-carlo` |
| What do the T-changing MC results say about coverage, set size, and power? | Standard DW becomes more precise but loses the truth under residual noise; robust DW is wider but usually truth-containing and tightens with \(T\). The warning event rises from `0.676` to `0.872`, which is the honest power-like diagnostic for this noisy-covariance design. | `../../draft.md#55-detailed-sample-size-monte-carlo`; `../../simulations/m74_sample_size_mc_500_grid27.md` |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Task contract and acceptance criteria. |
| `../../draft.md#55-detailed-sample-size-monte-carlo` | Main manuscript result. |
| `../../simulations/m74_sample_size_mc_500_grid27.md` | Generated human-readable MC table. |
| `../../simulations/output/m74_sample_size_mc_500_grid27.json` | Machine-readable records and summaries. |
| `../../simulations/m69_extended_three_block_mc.py` | Runner, scenario block, seeds, summaries, and progress support. |
| `../../simulations/m68_first_shock_evidence.py` | Shared MC evaluator and metrics. |
| `../../simulations/sign_dw_unit_variance_noise_grid_figure.py` | DGP simulator, candidate grid, moments, J statistics, weights, and masks. |
| `../../formal-object-registry.json` | New table registry object. |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the M74/M75 DGP, estimator
  computation, and results question.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- M74 Markdown rows matched JSON summaries exactly after applying the generator
  formatting.
- `python -m json.tool manuscript\formal-object-registry.json`: passed.
- `python -m json.tool manuscript\simulations\output\m74_sample_size_mc_500_grid27.json`: passed.
- `python scripts/check_manuscript.py`: passed with only the expected warning
  that M0070 was still open before closeout.
- `python scripts/check_manuscript.py` after closing M0070: passed.

## Open Questions Or Follow-Up

- M65 still owns projected critical values and final confidence-set wording.
- M70 can still refine the broader extended-MC narrative, but M75 completes
  the detailed sample-size MC section requested by the user.
