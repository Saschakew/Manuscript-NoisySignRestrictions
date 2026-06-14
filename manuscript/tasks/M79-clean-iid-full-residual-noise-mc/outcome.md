# M79 Clean IID Full Residual-Noise MC Outcome

Status: completed.

Completed: 2026-06-14.

## Short Answer

Yes. The cleaned iid full Monte Carlo has now been run for all three Figure 1
residual-noise DGPs. M79 uses 500 replications each for
\(V=(0,0),(0.2,0.2),(0.5,0.5)\) at \(T=500\), with strong structural
non-Gaussianity, the `27/7/5` grid, no sample standardization or demeaning, and
analytic iid weights. As residual noise rises, Sign truth inclusion is 0.924,
0.140, and 0.000; DW truth inclusion is 0.846, 0.102, and 0.000; nrDW truth
inclusion is 0.888, 0.880, and 0.886.

## What Changed

- Added `../../simulations/m79_clean_iid_full_residual_noise_mc.py`.
- Generated `../../simulations/m79_clean_iid_full_residual_noise_mc.md`,
  `../../simulations/output/m79_clean_iid_full_residual_noise_mc.json`, and
  the progress manifest.
- Updated `../../draft.md#56-detailed-residual-noise-monte-carlo` with Table 3
  and the residual-noise interpretation.
- Updated the registry, source packet, paper map, citation provenance,
  question index, task board, dashboard, user input log, decision log, session
  log, and Codex log.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Has the cleaned iid full MC been run for the Figure 1 residual-noise DGPs? | Yes. M79 runs the full projection-grid MC for all three residual-noise scenarios with 500 replications each. | `../../simulations/m79_clean_iid_full_residual_noise_mc.md` |
| What happens as residual noise increases? | Sign and DW truth inclusion collapse, while nrDW remains near the 0.90 pointwise benchmark. | `../../draft.md#56-detailed-residual-noise-monte-carlo` |
| Does residual noise mainly affect truth inclusion, set size, empty sets, or the warning event? | The main effect is false rejection by the no-noise Sign/DW targets and a sharp increase in the DW-misses/nrDW-contains warning rate; robust set size also widens as noise rises. | `../../simulations/output/m79_clean_iid_full_residual_noise_mc.json` |
| Did the no-noise scenario evaluate true lambda zero correctly? | Yes. The JSON lambda checks confirm true lambda `(0,0)` is on the grid. | `../../simulations/output/m79_clean_iid_full_residual_noise_mc.json` |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Task contract |
| `../../simulations/m79_clean_iid_full_residual_noise_mc.md` | Human-readable M79 output |
| `../../simulations/output/m79_clean_iid_full_residual_noise_mc.json` | Machine-readable M79 output |
| `../../draft.md#56-detailed-residual-noise-monte-carlo` | Draft interpretation and Table 3 |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the cleaned residual-noise
  full-MC answer.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python -m py_compile manuscript\simulations\m79_clean_iid_full_residual_noise_mc.py`: passed.
- Quick smoke run with `--quick --evaluation-reps 2`: passed.
- Full-grid pilot with canonical `27/7/5` dimensions: passed.
- Full run:
  `python manuscript\simulations\m79_clean_iid_full_residual_noise_mc.py --evaluation-reps 500 --projection-points 27 --profile-points 7 --lambda-points 5`: passed.
- M79 JSON lambda checks confirmed true lambda values for all scenarios,
  including `(0,0)` in the no-noise scenario.
- M79 robust analytic weights required no regularization in the full run.
- Final repository checks are recorded in the closing milestone.

## Open Questions Or Follow-Up

- M80 remains the matching cleaned iid full-grid MC for the Figure 2
  non-Gaussianity DGPs.
- M65 still owns projected critical values and final projected-inference
  wording. M79 remains a pointwise chi-square diagnostic table, not a final
  projected confidence-set calibration.
