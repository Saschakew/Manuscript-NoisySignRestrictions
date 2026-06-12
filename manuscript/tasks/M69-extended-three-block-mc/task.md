# M69 Extended Three-Block Monte Carlo

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M69`

Transparency milestone: `M0065-execute-m69-extended-mc`;
GitHub milestone #60

Outcome note: `outcome.md`

## Original User Prompt

"Plan an extension of our MC along the three dgp and variation of our three
figures. First plan  the mc setups and coding and so on. Second task will be
interpretation and documentation of the MC in the draft."

Follow-up: "Use /goal mode"

## Why This Task Exists

M68 rebuilt the active Figures 1-3 and the current Monte Carlo diagnostic under
the unit-variance first-shock chart. The existing MC table is still a compact
six-scenario diagnostic. The manuscript now needs an extended Monte Carlo that
is organized around the three active figure blocks, so the finite-sample table
speaks directly to the visual evidence:

1. Figure 1 residual-noise variation.
2. Figure 2 structural non-Gaussianity variation.
3. Figure 3 sample-size variation.

This task is deliberately only the setup, coding, and execution task. The
interpretation and draft documentation are deferred to M70 after the extended
MC outputs exist and have passed basic checks.

## Do Not Trust Without Rechecking

- M68 pointwise chi-square cutoffs as final projected confidence-set critical
  values. M65 still owns the final projected-inference route.
- Old M52/M45/M29 outputs as active evidence for the M64/M66 unit-variance
  GMM route.
- Any simulation path that forgets the active sign screen:
  \(B_{11}>0\), \(B_{22}>0\), \(B_{12}\le0\), and \(B_{21}\ge0\).
- Any robust accepted-set calculation that uses a direct \(0\le\nu_i\le\rho\)
  cap instead of \(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\).
- Any MC scenario whose DGP no longer matches the corresponding active figure
  scenario.
- Any draft interpretation before M70 reads the generated MC notes and JSON.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm KnowledgeVault and package context. | implementation |
| `manuscript/project-dashboard.md` | Confirm current stage and M65 caveat. | implementation |
| `manuscript/paper-map.md` | Confirm the Figure 1-3 evidence contract. | implementation |
| `manuscript/task-board.md` | Confirm task routing. | implementation |
| `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/task.md` | Keep projected-critical-value caveat visible. | implementation |
| `manuscript/tasks/M68-first-shock-impact-evidence-rebuild/outcome.md` | Confirm active chart, sign screen, and outputs. | implementation |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` | Reuse the active evaluator and figure scenario definitions. | implementation |
| `manuscript/simulations/m68_first_shock_evidence.py` | Starting point for MC loop, metrics, and output writer. | implementation |
| `manuscript/replication/run_all.py` | Add or document an extended-MC stage if outputs become active evidence. | replication edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The extended MC should mirror the three active figure blocks. | `user-decision` plus `code-implemented` | Original prompt, M68 figure scenario definitions, and new MC configuration. | passed |
| The robust row uses \(\nu_i=\lambda_i(BB')_{ii}\) with \(\lambda\in[0,\rho]^2\). | `derived` plus `code-implemented` | M66 derivation and evaluator calls. | passed |
| MC output can be interpreted as final projected confidence-set evidence. | `derived` or `raw-source` | M65 projected-inference note or explicit calibration route. | not passed; M65 remains open |
| MC output can be interpreted as diagnostic pointwise-chi-square evidence. | `code-implemented` plus caveated `user-decision` | Script configuration, notes, JSON, and retained M65 caveat. | passed |

## Required Work

1. Define a shared extended-MC scenario table with three blocks:

   | Block | Figure matched | Scenario cells | Fixed settings |
   |---|---|---|---|
   | `noise_grid` | Figure 1 | `V=(0,0)`, `V=(0.2,0.2)`, `V=(0.5,0.5)` | `T=500`, structural non-Gaussianity `w=1`, Gaussian residual noise |
   | `nongaussianity_grid` | Figure 2 | `w=1`, `w=0.25`, `w=0` | `T=500`, `V=(0.2,0.2)`, Gaussian residual noise |
   | `sample_size_grid` | Figure 3 | `T=500`, `T=1000`, `T=2000` | `V=(0.2,0.2)`, structural non-Gaussianity `w=1`, Gaussian residual noise |

   Keep any skewed-residual-noise or correlated-noise stress case outside the
   main three-block table unless the user explicitly asks to add a fourth
   stress block.

2. Implement a new script, preferably
   `manuscript/simulations/m69_extended_three_block_mc.py`, that reuses the
   M68 evaluator functions rather than duplicating GMM logic.

3. Use explicit data classes such as `MCBlock` and `MCScenario` so each record
   carries:
   block name, figure matched, label, noise tuple, sample size,
   non-Gaussianity weight, residual-noise law, seed, and note.

4. Keep outputs separate from canonical M68 evidence until reviewed:
   - `manuscript/simulations/m69_extended_three_block_mc.md`
   - `manuscript/simulations/output/m69_extended_three_block_mc.json`

5. Add command-line controls:
   - `--block all|noise_grid|nongaussianity_grid|sample_size_grid`
   - `--evaluation-reps`
   - `--projection-points`
   - `--profile-points`
   - `--lambda-points`
   - `--quick` for smoke checks that write outside canonical evidence paths
   - optional `--append` or checkpointing only if runtime makes it necessary

6. Report metrics by block and scenario cell:
   - standard-DW truth inclusion count and rate;
   - robust-DW truth inclusion count and rate;
   - warning rate where standard DW misses while robust DW contains truth;
   - sign, standard-DW, and robust-DW accepted projection shares as the main
     inverted-set size measure;
   - mean and median accepted projection shares for the standard-DW and
     robust-DW inverted sets;
   - directional standard-outside-robust share \(d_{S\not\subset R}\);
   - distance from truth to nearest accepted standard/robust projection when
     truth is missed;
   - empty-set or numerical-failure rates if they occur;
   - Monte Carlo standard errors for all rates and means.

7. Use a staged runtime plan:
   - smoke check: 1-2 reps, small grids, writes to quick output;
   - working diagnostic: 24-50 reps using the current M68 MC grid defaults
     unless runtime is too high;
   - heavier run: 100+ reps only after the working diagnostic is informative
     and runtime is acceptable.

8. Update `manuscript/replication/run_all.py` only after the new script has a
   passing quick run. Prefer an explicit stage such as `extended-mc` rather
   than silently changing the current `evidence` stage.

9. Do not update `draft.md` in this task except for a hidden TODO note if
   absolutely necessary. M70 owns interpretation and prose integration.

10. Complete `outcome.md` with the run configuration, outputs, checks, and
    whether `manuscript/QUESTION-INDEX.md` needs a row.

## Stop Conditions

- Stop if any MC block uses scenario settings that differ from the active
  figure definitions without an explicit recorded reason.
- Stop if the implementation requires changing the maintained M66 moment
  vector or sign screen.
- Stop if runtime makes the planned grid infeasible; record a smaller
  diagnostic design rather than silently reducing quality.
- Stop if projected critical values become necessary for the claimed
  interpretation; route that issue through M65 before final draft prose.
- Stop if code behavior and the Section 4 moment definition disagree.

## Acceptance Criteria

- A new extended-MC script exists and reuses the active M68 evaluator logic.
- The three MC blocks match the three active figure variations.
- Quick output is generated without overwriting canonical M68 outputs.
- JSON and Markdown outputs record configuration, seeds, grids, rates, standard
  errors, and the pointwise/projection-critical-value caveat.
- `python -m py_compile` passes for edited simulation and replication scripts.
- `python -m json.tool` passes for generated JSON.
- `python scripts/check_manuscript.py` passes after planning or code edits.
- M70 remains blocked until M69 output exists and has been checked.

## Expected Outputs

- `manuscript/simulations/m69_extended_three_block_mc.py`
- `manuscript/simulations/m69_extended_three_block_mc.md`
- `manuscript/simulations/output/m69_extended_three_block_mc.json`
- Optional replication wrapper stage for `extended-mc`
- Completed `outcome.md`
