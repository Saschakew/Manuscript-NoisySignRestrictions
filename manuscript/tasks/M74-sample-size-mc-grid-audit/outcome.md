# M74 Sample-Size MC Grid Audit Outcome

Status: done.

Completed: 2026-06-14.

## Short Answer

The requested 500-replication sample-size Monte Carlo completed successfully.
It ran the Figure 3 `sample_size_grid` block only, using the intermediate
`27/7/5` grid, 500 replications for each of `T=500`, `T=1000`, and `T=2000`,
candidate-specific pointwise covariance weights, and pointwise chi-square
diagnostic cutoffs. M75 has now interpreted the completed output in
`../../draft.md#55-detailed-sample-size-monte-carlo`.

## What Changed

- Added monitorable progress support to
  `../../simulations/m69_extended_three_block_mc.py`.
- Added `../../../scripts/launch_m74_sample_size_mc.py`, a detached launcher
  for the exact M74 command.
- Ran a one-replication smoke check for `sample_size_grid`.
- Launched the full background run:
  `--block sample_size_grid --evaluation-reps 500 --projection-points 27 --profile-points 7 --lambda-points 5`.
- Confirmed the progress manifest reached `1500/1500` completed replications
  at `2026-06-14T14:02:18+02:00` and that the error log is empty.
- Verified the generated Markdown result rows against the JSON summaries.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Can we run the T-changing MC on an intermediate grid and monitor progress? | Yes. The run completed and wrote progress, launch, log, JSON, and Markdown output files. | `task.md`; `../../simulations/output/m74_sample_size_mc_500_grid27.progress.json`; `../../simulations/output/m74_sample_size_mc_500_grid27.log` |
| What happened in the completed T-changing MC? | Standard DW becomes more precisely wrong under the noisy DGP: full-\(B_0\) truth inclusion is `0.110`, `0.000`, `0.000` as \(T\) rises, while robust truth inclusion is `0.750`, `0.842`, `0.872`. | `../../draft.md#55-detailed-sample-size-monte-carlo`; `../../simulations/m74_sample_size_mc_500_grid27.md` |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Task contract. |
| `../../../scripts/launch_m74_sample_size_mc.py` | Detached-launch helper and exact command construction. |
| `../../simulations/output/m74_sample_size_mc_500_grid27.launch.json` | PID, command, grid, and output paths. |
| `../../simulations/output/m74_sample_size_mc_500_grid27.progress.json` | Completed progress manifest. |
| `../../simulations/output/m74_sample_size_mc_500_grid27.log` | Human-readable progress log. |
| `../../simulations/output/m74_sample_size_mc_500_grid27.err.log` | Error log; empty at completion inspection. |
| `../../simulations/output/m74_sample_size_mc_500_grid27.json` | Machine-readable MC records and summaries. |
| `../../simulations/m74_sample_size_mc_500_grid27.md` | Generated human-readable MC output. |
| `../M75-detailed-sample-size-mc-section/outcome.md` | Draft interpretation and closeout. |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated through M75 because the completed
  MC answers a durable question about the DGP, estimator computation, coverage,
  set size, and power/warning behavior.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python -m py_compile manuscript\simulations\m69_extended_three_block_mc.py scripts\launch_m74_sample_size_mc.py`: passed during launch work.
- Smoke command with `--block sample_size_grid --evaluation-reps 1 --projection-points 7 --profile-points 5 --lambda-points 3` and progress outputs: passed during launch work.
- Background launch command `python scripts\launch_m74_sample_size_mc.py --force`: returned PID `10256` and wrote the launch manifest.
- Progress completion check: `m74_sample_size_mc_500_grid27.progress.json` reports `completed=1500`, `total=1500`, and `status=completed`.
- Error-log check: `m74_sample_size_mc_500_grid27.err.log` is empty.
- M75 JSON/Markdown row comparison: passed.
- `python -m json.tool manuscript\simulations\output\m74_sample_size_mc_500_grid27.json`: passed.
- `python scripts/check_manuscript.py`: passed with only the expected warning that M0070 was still open before closeout.
- `python scripts/check_manuscript.py` after closing M0070: passed.

## Open Questions Or Follow-Up

- M65 still owns projected critical values and final confidence-set wording.
- M70 can still refine the broader extended-MC narrative, but M75 has completed
  the detailed sample-size interpretation requested for M74.
