# M77 Clean IID MC Efficient Weight Outcome

Status: completed.

Completed: 2026-06-14.

## Short Answer

Yes. For the cleaned iid Monte Carlo, \(W=(E[f_t f_t'])^{-1}\) is the
pointwise efficient GMM weight and is sample-size invariant. Implementing that
design brings nrDW truth-at-\(B_0\) inclusion back to the nominal 90 percent
benchmark within Monte Carlo error: 0.884, 0.896, and 0.900 for
\(T=500,1000,2000\).

## What Changed

- Added `../../simulations/m77_clean_iid_mc_efficient_weight.py`, a cleaned iid
  truth-at-\(B_0\) MC script using analytic \(W=(E[f_t f_t'])^{-1}\).
- Generated `../../simulations/m77_clean_iid_mc_efficient_weight.md` and
  `../../simulations/output/m77_clean_iid_mc_efficient_weight.json`.
- Updated `../../draft.md#55-detailed-sample-size-monte-carlo` to add the M77
  pointwise audit and to keep M74 Table 2 as the full-grid set-size diagnostic.
- Updated registry, provenance, source packet, paper map, dashboard, task
  board, question index, and logs.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Is \(W=(E[f f'])^{-1}\) the valid efficient GMM weight for iid moments? | Yes, for iid per-period moments with \(E[f_t]=0\). M77 computes it analytically from exact univariate moments, not from an auxiliary large sample. | `../../simulations/m77_clean_iid_mc_efficient_weight.md` |
| Is the cleaned iid analytic-weight MC a simplification of the previous MC? | Yes for weighting: it replaces sample-specific covariance estimates with analytic population weights. It is also a DGP cleanup because it removes sample standardization and demeaning. | `../../draft.md#55-detailed-sample-size-monte-carlo` |
| Did the cleaned MC fix nrDW overrejection? | For the truth-at-\(B_0\) pointwise diagnostic, yes: nrDW inclusion is 0.884, 0.896, and 0.900 for \(T=500,1000,2000\). | `../../simulations/m77_clean_iid_mc_efficient_weight.md` |
| Does M77 replace M74 Table 2? | No. M77 reports truth-at-\(B_0\) only. M74 Table 2 still carries projection shares and empty-set rates. | `../../draft.md#55-detailed-sample-size-monte-carlo` |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Task contract |
| `../../simulations/m77_clean_iid_mc_efficient_weight.md` | Human-readable M77 output and formula audit |
| `../../simulations/output/m77_clean_iid_mc_efficient_weight.json` | Machine-readable M77 output |
| `../../draft.md#55-detailed-sample-size-monte-carlo` | Draft interpretation of M74 plus M77 |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the efficient-weight and nrDW
  pointwise-size answer.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python manuscript\simulations\m77_clean_iid_mc_efficient_weight.py --reps 500`: passed.
- `python -m json.tool manuscript\simulations\output\m77_clean_iid_mc_efficient_weight.json`: passed.
- `python -m py_compile manuscript\simulations\m77_clean_iid_mc_efficient_weight.py`: passed.
- Independent 200000-draw formula check at \(B_0\): max scaled robust covariance
  discrepancy about 0.070; not used to compute \(W\).
- `python -m json.tool manuscript\formal-object-registry.json`: passed.
- `python scripts\check_manuscript.py`: passed with the expected open-milestone
  warning before closeout.
- `python scripts\check_manuscript.py`: passed cleanly after closeout.
- `git diff --check`: passed with line-ending normalization warnings only.

## Open Questions Or Follow-Up

- A full-grid cleaned iid MC with accepted projection shares and empty-set
  rates remains optional. M77 deliberately stops at truth-at-\(B_0\) pointwise
  size.
- M65 still owns projected critical values and final inference wording.
