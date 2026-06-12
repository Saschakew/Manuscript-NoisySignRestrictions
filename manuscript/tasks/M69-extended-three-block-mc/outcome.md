# M69 Task Outcome

Status: done.

Completed: 2026-06-12.

Correction note, 2026-06-12: M71 supersedes these original outputs for draft
interpretation. The original M69 run inherited the M68 \(B_{21}\ge0\) sign
restriction and true-point fixed weights. Use the M71 outcome and regenerated
`m69_extended_three_block_mc` outputs for current extended-MC diagnostics.

## Short Answer

M69 implemented and ran an extended three-block Monte Carlo matching the three
active figures: residual-noise variation, structural non-Gaussianity variation,
and sample-size variation. The output reports true-\(B_0\) inclusion as
counts/rates and measures inverted-set size as the accepted share of the
displayed \((B_{11},B_{21})\) projection grid, summarized by mean and median.
The results remain pointwise chi-square diagnostics; M70 should interpret them
in the draft, with M65's projected-critical-value caveat kept visible.

## What Changed

- Added `../../simulations/m69_extended_three_block_mc.py`.
- Generated `../../simulations/m69_extended_three_block_mc.md`.
- Generated `../../simulations/output/m69_extended_three_block_mc.json`.
- Added an explicit `extended-mc` stage to `../../replication/run_all.py`.
- Updated `../../replication/README.md` and `../../simulations/README.md`.
- Updated planning, log, question-index, and transparency surfaces.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| How should the extended MC be organized? | Planned as three blocks matching Figure 1 residual noise, Figure 2 structural non-Gaussianity, and Figure 3 sample size. | `task.md` |
| How is inverted-set size measured? | By accepted projection share on the displayed \((B_{11},B_{21})\) grid; the output reports mean and median shares for standard DW and robust DW. | `../../simulations/m69_extended_three_block_mc.md` |
| How is true-\(B_0\) inclusion reported? | As counts and rates for the standard-DW and robust-DW inverted sets in every scenario cell. | `../../simulations/m69_extended_three_block_mc.md` |

## Output Snapshot

The canonical run used 24 replications per scenario, a `17 x 17` projection
grid, a `7 x 7` profile grid, and a `5 x 5` lambda grid.

| Block | Scenario | Standard truth | Robust truth | Standard size mean/median | Robust size mean/median |
|---|---|---:|---:|---:|---:|
| Residual noise | `V=(0,0)` | 16/24 | 14/24 | 0.032 / 0.035 | 0.031 / 0.035 |
| Residual noise | `V=(0.2,0.2)` | 7/24 | 16/24 | 0.080 / 0.079 | 0.080 / 0.085 |
| Residual noise | `V=(0.5,0.5)` | 0/24 | 19/24 | 0.214 / 0.215 | 0.180 / 0.184 |
| Non-Gaussianity | `w=1` | 0/24 | 15/24 | 0.079 / 0.079 | 0.079 / 0.085 |
| Non-Gaussianity | `w=0.25` | 0/24 | 23/24 | 0.113 / 0.114 | 0.167 / 0.167 |
| Non-Gaussianity | `w=0` | 0/24 | 18/24 | 0.114 / 0.116 | 0.164 / 0.177 |
| Sample size | `T=500` | 2/24 | 14/24 | 0.075 / 0.077 | 0.071 / 0.077 |
| Sample size | `T=1000` | 0/24 | 20/24 | 0.032 / 0.035 | 0.053 / 0.056 |
| Sample size | `T=2000` | 0/24 | 21/24 | 0.012 / 0.012 | 0.034 / 0.034 |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Task contract and MC setup plan. |
| `../../simulations/m69_extended_three_block_mc.md` | Human-readable extended MC output. |
| `../../simulations/output/m69_extended_three_block_mc.json` | Machine-readable records, configuration, summaries, counts, and size measures. |
| `../../replication/README.md` | Rebuild command through the replication wrapper. |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the M69 set-size/truth-inclusion answer.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed unless a legacy MC task is reopened.

## Checks

- `python -m py_compile manuscript\simulations\m69_extended_three_block_mc.py manuscript\replication\run_all.py`: passed.
- `python manuscript\simulations\m69_extended_three_block_mc.py --quick --block noise_grid`: passed.
- `python manuscript\replication\run_all.py --stage extended-mc --quick`: passed.
- `python manuscript\replication\run_all.py --stage extended-mc`: passed.
- `python -m json.tool manuscript\replication\output\quick\m69_extended_three_block_mc.json`: passed.
- `python -m json.tool manuscript\simulations\output\m69_extended_three_block_mc.json`: passed.
- Final manuscript and diff checks are recorded in the milestone closeout.

## Open Questions Or Follow-Up

- M70 should interpret and document the checked M69 output in the draft.
- M65 still owns final projected critical values; the M69 output is diagnostic
  pointwise chi-square evidence until that inference route is settled.
