# M76 Report Sign-Only M74 Results Outcome

Status: completed.

Completed: 2026-06-14.

## Short Answer

Table 2 now reports the three approaches as `Sign`, `DW`, and `nrDW`. The M74
run shows that the Sign baseline already fails under the noisy covariance
target: truth inclusion is 0.112, 0.000, and 0.000 for \(T=500,1000,2000\).
DW mostly sharpens that misspecified sign object, while nrDW is wider but
usually truth-containing.

## What Changed

- `../../draft.md#55-detailed-sample-size-monte-carlo`: renamed Table 2
  columns and added Sign truth, Sign size, and Sign empty rates.
- `../../simulations/m74_sample_size_mc_500_grid27.md`: updated the output note
  to report Sign, DW, and nrDW values side by side.
- `../../formal-object-registry.json`: marked the sample-size MC table revised
  after M76 and recorded the sign-only baseline source.
- Planning, provenance, and log surfaces were updated so M76 is traceable.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Did the M74 MC also compare DW and noise-robust DW against sign restrictions only? | Yes. The run evaluated the sign-only screen and stored its accepted shares; sign truth inclusion can be recovered from the stored second-moment truth statistic. Table 2 now reports Sign, DW, and nrDW together. | `../../draft.md#55-detailed-sample-size-monte-carlo`; `../../simulations/m74_sample_size_mc_500_grid27.md` |
| Should `S` and `R` be renamed? | Yes. M76 uses `Sign` for sign restrictions only, `DW` for the standard no-noise DW refinement, and `nrDW` for noise-robust DW. | `../../draft.md#55-detailed-sample-size-monte-carlo` |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Task contract and claim ledger. |
| `../../draft.md#55-detailed-sample-size-monte-carlo` | Revised manuscript table and interpretation. |
| `../../simulations/m74_sample_size_mc_500_grid27.md` | Output note with counts and rates. |
| `../../simulations/output/m74_sample_size_mc_500_grid27.json` | Machine-readable source output. |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated the M74 row to mention Sign, DW, and
  nrDW.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python -m json.tool manuscript/formal-object-registry.json`: passed.
- Sign-only truth/size/empty rates were recomputed from
  `simulations/output/m74_sample_size_mc_500_grid27.json` and matched the
  revised Table 2 values.
- `python scripts/check_manuscript.py`: passed with the expected warning that
  M0071 was still open before closeout.
- `git diff --check`: passed, with only line-ending normalization warnings.

## Open Questions Or Follow-Up

- M65 still owns projected critical values and final confidence-set wording.
