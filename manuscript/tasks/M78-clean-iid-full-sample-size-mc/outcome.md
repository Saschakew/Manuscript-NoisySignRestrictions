# M78 Clean IID Full Sample-Size MC Outcome

Status: completed.

Completed: 2026-06-14.

## Short Answer

Yes. The cleaned iid full sample-size MC has now been run for all three sample
sizes, not just at \(B_0\). M78 uses 500 replications each for
\(T=500,1000,2000\) on the same `27/7/5` projection grid, with no sample
standardization or demeaning and analytic iid weights. nrDW truth inclusion is
0.884, 0.896, and 0.900, while accepted projection shares shrink from 0.063 to
0.021.

## What Changed

- Added `../../simulations/m78_clean_iid_full_sample_size_mc.py`.
- Generated `../../simulations/m78_clean_iid_full_sample_size_mc.md`,
  `../../simulations/output/m78_clean_iid_full_sample_size_mc.json`, and the
  progress manifest.
- Updated `../../draft.md#55-detailed-sample-size-monte-carlo` so Table 2 now
  reports the M78 cleaned iid full-grid results.
- Updated the registry, source packet, paper map, dashboard, citation
  provenance, question index, task board, user input log, decision log,
  session log, and Codex log.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Has the cleaned iid full sample-size MC been run for all `T` values? | Yes. M78 runs the full projection-grid MC for \(T=500,1000,2000\) with 500 replications each. | `../../simulations/m78_clean_iid_full_sample_size_mc.md` |
| Is M78 only a \(B_0\) size test? | No. M78 computes accepted projection shares, empty-set rates, and warning rates on the full `27/7/5` grid. | `../../draft.md#55-detailed-sample-size-monte-carlo` |
| What happens to nrDW after the cleaned iid analytic-weight update? | nrDW truth inclusion is at nominal sampling error: 0.884, 0.896, and 0.900; its accepted projection share shrinks from 0.063 to 0.021 as \(T\) grows. | `../../simulations/output/m78_clean_iid_full_sample_size_mc.json` |
| What happens to Sign and DW? | They still reject the truth as \(T\) grows because they test the no-noise covariance target under residual noise. DW truth inclusion is 0.088, 0.010, and 0.000. | `../../draft.md#55-detailed-sample-size-monte-carlo` |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Task contract |
| `../../simulations/m78_clean_iid_full_sample_size_mc.md` | Human-readable M78 output |
| `../../simulations/output/m78_clean_iid_full_sample_size_mc.json` | Machine-readable M78 output |
| `../../draft.md#55-detailed-sample-size-monte-carlo` | Draft interpretation and Table 2 |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the cleaned full-MC answer.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python -m py_compile manuscript\simulations\m78_clean_iid_full_sample_size_mc.py`: passed.
- Smoke run with `--quick --evaluation-reps 2`: passed.
- Raw-moment formula check against observation-built means: max absolute
  difference `3.126388037344441e-13`.
- Full run:
  `python manuscript\simulations\m78_clean_iid_full_sample_size_mc.py --evaluation-reps 500 --projection-points 27 --profile-points 7 --lambda-points 5`: passed.
- JSON validation for M78 output and formal registry: passed.
- `python scripts\check_manuscript.py`: passed with expected open-milestone
  warning before closeout.
- `git diff --check`: passed with line-ending normalization warnings only.
- `python scripts\check_manuscript.py`: passed cleanly after closeout.

## Open Questions Or Follow-Up

- M65 still owns projected critical values and final projected-inference
  wording. M78 remains a pointwise chi-square diagnostic table, not a final
  projected confidence-set calibration.
