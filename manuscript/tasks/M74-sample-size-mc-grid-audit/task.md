# M74 Sample-Size MC Grid Audit

## Status And Routing

Status: `doing`

Priority: 1

Task-board row: `M74`

Transparency milestone: `M0070-run-sample-size-mc-grid-audit`

GitHub milestone: `#65`

Outcome note: `outcome.md`

## Original User Prompt

"then lets do the MC where T changes with a grid size in between current mc and
current figure grid.mthe goal is to evaluate if the coverage size of our trest
is correct. plan the task, and start the mc as a background but in a way that
we can monitor progress. once it runs and you are sure it runs fine, you can
stop and i will let you know once it finished"

## Why This Task Exists

The corrected M71/M73 figures use a dense `41/11/7` grid, while the current
extended MC diagnostics use a much smaller `13/5/3` grid. The user wants a
heavier but still feasible 500-replication Monte Carlo for the Figure 3
sample-size block only, using an intermediate grid, so that coverage and
inverted-set-size behavior can be checked as sample size changes.

## Do Not Trust Without Rechecking

- Do not rerun all three M69 blocks; this task is only the `sample_size_grid`
  block matched to Figure 3.
- Do not use the full `41/11/7` figure grid for the 500-replication MC unless
  explicitly requested; prior timing suggests that would be too slow.
- Do not use the old `13/5/3` MC grid; the request asks for an intermediate
  grid.
- Do not treat the pointwise chi-square cutoff as final projected inference;
  M65 still owns projected critical values.
- Do not claim final results before the background process finishes and the
  JSON/Markdown outputs are inspected.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm repository/package context. | task execution |
| `manuscript/source-packet.md` | Confirm active M71/M73 evidence route. | task execution |
| `manuscript/project-dashboard.md` | Confirm current stage and blockers. | task execution |
| `manuscript/paper-map.md` | Confirm Figure 3 and MC role. | task execution |
| `manuscript/task-board.md` | Confirm task routing. | task execution |
| `manuscript/formal-object-registry.json` | Confirm affected table/figure objects. | registry/log edits |
| `manuscript/simulations/m69_extended_three_block_mc.py` | Active extended MC runner. | code edits and launch |
| `manuscript/simulations/m68_first_shock_evidence.py` | Shared MC evaluator. | code edits and launch |
| `manuscript/tasks/M69-extended-three-block-mc/outcome.md` | Existing MC output contract and caveats. | task execution |
| `manuscript/tasks/M73-increase-figure-grid-density/outcome.md` | Current figure-grid density. | grid choice |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The M74 run uses the sample-size block only. | `code-implemented`, `user-decision` | Background command and progress JSON. | verified at launch: PID `10256`, command uses `--block sample_size_grid`. |
| The M74 run uses an intermediate grid between `13/5/3` and `41/11/7`. | `code-implemented`, `user-decision` | Command and progress JSON. | verified at launch: command and progress JSON report grid `27/7/5`. |
| The M74 run evaluates coverage and set size for the T-changing scenarios. | `code-implemented` | Final JSON/Markdown summaries after process completes. | running; final evaluation pending output completion. |
| The pointwise chi-square diagnostic has correct final projected coverage. | `conjectural` | M65 projected-inference task. | quarantined |

## Required Work

1. Source work: no new external source claim.
2. Derivation work: none; this is a Monte Carlo execution/audit task.
3. Code or simulation work: add or verify progress-monitoring support, run a
   smoke/benchmark check, and launch the 500-replication `sample_size_grid`
   MC in the background with grid `27/7/5`.
4. Manuscript update work: record the task and launch state without promoting
   unfinished MC results.
5. Outcome note work: record the background command, progress file, log file,
   output paths, and the fact that final interpretation waits for completion.

## Stop Conditions

- Stop if the smoke run does not update progress.
- Stop if the background process exits immediately with an error.
- Stop if the launch command cannot be monitored from a progress file or log.
- Stop if a different Python MC process is already writing the same outputs.

## Acceptance Criteria

- Task folder exists and task-board row points to it.
- The MC runner can write a progress JSON file after each replication.
- A smoke or benchmark run verifies that progress monitoring works.
- A background process is started for:
  `--block sample_size_grid --evaluation-reps 500 --projection-points 27 --profile-points 7 --lambda-points 5`.
- The background process is confirmed alive after at least one progress update.
- The user is given the progress/log/output paths and monitor commands.
- The final task remains open until the background MC finishes and outputs are
  inspected.

## Expected Outputs

- `manuscript/simulations/output/m74_sample_size_mc_500_grid27.progress.json`
- `manuscript/simulations/output/m74_sample_size_mc_500_grid27.log`
- `manuscript/simulations/output/m74_sample_size_mc_500_grid27.err.log`
- `manuscript/simulations/output/m74_sample_size_mc_500_grid27.json`
- `manuscript/simulations/m74_sample_size_mc_500_grid27.md`
- `manuscript/tasks/M74-sample-size-mc-grid-audit/outcome.md`
