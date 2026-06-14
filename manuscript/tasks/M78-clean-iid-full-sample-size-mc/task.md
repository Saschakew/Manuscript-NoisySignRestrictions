# M78 Clean IID Full Sample-Size MC

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M78`

Transparency milestone: `M0073-m78-full-clean-iid-sample-size-mc`

GitHub milestone: `#68`

Outcome note: `outcome.md`

## Original User Prompt

"Next task: plan a full MC run for the T scenario MC including updating the
draft with the results. Also execute the task immediately"

## Why This Task Exists

M77 answered the cleaned iid weighting question only at the true parameter
\(B_0\). It did not compute accepted projection shares, empty-set rates, or
full-grid truth inclusion for the sample-size Monte Carlo. The user now wants
the full `T=500,1000,2000` sample-size MC to use the cleaned iid design and to
update the manuscript with the resulting table.

This task should keep the M74 table's reporting logic but replace the
contaminating pieces identified in M77: sample-standardized primitive draws,
residual demeaning, recovered-shock demeaning, and sample-specific covariance
weights. The cleaned run should use population-normalized iid shocks/noise and
analytic iid efficient weights \(W=(E[f_t f_t'])^{-1}\). For nrDW, the weight is
candidate-specific over \((B,\lambda)\).

## Do Not Trust Without Rechecking

- Do not treat M77 as a full MC. It is a truth-at-\(B_0\) pointwise size audit.
- Do not promote M74 Table 2 as the cleaned iid full-grid result. M74 used the
  old DGP/statistic cleanup state.
- Do not compute analytic \(W\) from a large auxiliary simulation. The user
  specifically asked for the simple formula \(E[f_t f_t']^{-1}\).
- Do not demean residuals or recovered shocks in the cleaned statistic.
- Do not silently change the maintained sign screen:
  \(B_{11}>0\), \(B_{22}>0\), and \(B_{12}\le0\), with no sign restriction on
  \(B_{21}\).
- Do not present pointwise chi-square inversions as final projected confidence
  sets; M65 still owns projected critical values.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm repository/package context. | task execution |
| `manuscript/source-packet.md` | Confirm active evidence route and M74/M77 status. | interpretation |
| `manuscript/project-dashboard.md` | Confirm current stage and active blockers. | task execution |
| `manuscript/paper-map.md` | Confirm sample-size evidence role. | draft edits |
| `manuscript/task-board.md` | Confirm row status and dependencies. | task execution |
| `manuscript/draft.md#55-detailed-sample-size-monte-carlo` | Locate affected prose and Table 2. | draft edits |
| `manuscript/formal-object-registry.json` | Locate affected table objects. | registry edits |
| `manuscript/simulations/m77_clean_iid_mc_efficient_weight.py` | Reuse cleaned iid DGP and analytic-weight machinery. | code work |
| `manuscript/simulations/m69_extended_three_block_mc.py` | Reuse sample-size block configuration and summary format. | code work |
| `manuscript/simulations/m68_first_shock_evidence.py` | Reuse metric definitions. | code work |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` | Reuse active grid, sign screen, and moment definitions. | code work |
| `manuscript/simulations/m74_sample_size_mc_500_grid27.md` | Compare old full-grid design and reporting. | interpretation |
| `manuscript/simulations/m77_clean_iid_mc_efficient_weight.md` | Compare cleaned pointwise audit and results. | interpretation |
| `.codex/skills/write-standalone-manuscript/references/scientific-claim-audit.md` | Apply claim gate before draft updates. | prose and registry edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The cleaned full MC uses population-normalized iid shocks/noise and no demeaning. | `code-implemented`, `user-decision` | M78 script and configuration output. | satisfied |
| The nrDW full-grid statistic uses candidate-specific analytic \(W(B,\lambda)=(E[f_t(B,\lambda)f_t(B,\lambda)'])^{-1}\). | `code-implemented`, `derived`, `user-decision` | M78 script, M77 polynomial formula route, output note. | satisfied |
| Sign and DW use analytic no-noise weights for their own moment stacks. | `code-implemented`, `derived` | M78 script and M77 standard weight functions. | satisfied |
| The M78 table supersedes M74 as the preferred full-grid sample-size table. | `code-implemented`, `user-decision` | Completed M78 full-grid output and draft update. | satisfied |
| The pointwise chi-square cutoffs are final projected confidence-set cutoffs. | `conjectural` | M65 remains open. | quarantine |

## Required Work

1. Code or simulation work:
   - Add a full-grid cleaned iid sample-size MC script under
     `manuscript/simulations/`.
   - Reuse the M74 grid and scenario block:
     `T=500,1000,2000`, \(V=\operatorname{diag}(0.2,0.2)\), strong structural
     non-Gaussianity, and the intermediate `27/7/5` grid.
   - Use population-normalized iid \(\chi^2_5\) structural shocks and iid
     Gaussian residual noise.
   - Use no residual demeaning, no recovered-shock demeaning, and no sample
     standardization.
   - Use analytic iid efficient weights. For nrDW, compute \(W(B,\lambda)\)
     candidate-by-candidate from exact univariate raw moments, preferably with
     vectorized or cached polynomial algebra so the full MC is tractable.
   - Report Sign, DW, and nrDW truth inclusion, accepted projection shares,
     empty-set rates, and the DW-misses/nrDW-contains warning event.
2. Manuscript update work:
   - Update `draft.md#55-detailed-sample-size-monte-carlo` with the M78 table.
   - Keep the old M74/M77 distinction visible: M74 is the old full-grid design;
     M77 is the pointwise audit; M78 is the cleaned full-grid run.
   - Update registry, source packet, paper map, dashboard, task board,
     citation provenance, question index, and logs as needed.
3. Outcome note work:
   - Answer whether the full MC has now been run for all sample sizes.
   - Report whether it changes the Table 2 interpretation.
   - Record checks and open follow-up.

## Stop Conditions

- Stop before draft promotion if the cleaned script still uses sample
  standardization, residual demeaning, or recovered-shock demeaning.
- Stop if analytic \(E[f_t f_t']\) is singular across a material part of the
  candidate grid and only regularization drives acceptance.
- Stop if the full `500 x 3` run is computationally infeasible; in that case,
  report a smaller run as a pilot and leave the full run explicitly open.
- Stop before claiming confidence-set validity; pointwise chi-square critical
  values remain diagnostic until M65.

## Acceptance Criteria

- A cleaned full-grid MC script exists and compiles.
- A full sample-size output exists for `T=500,1000,2000`; if not 500 reps, the
  reduced replication count is explicitly labeled and justified.
- The output Markdown and JSON report Sign, DW, and nrDW truth inclusion,
  sizes, empty rates, and warning rates.
- The draft is updated with the promoted results and caveats.
- The formal registry and planning/log surfaces point to the M78 evidence.
- `outcome.md` records the short answer and index-update decision.
- `python scripts/check_manuscript.py` passes after substantive edits.

## Expected Outputs

- `manuscript/simulations/m78_clean_iid_full_sample_size_mc.py`
- `manuscript/simulations/m78_clean_iid_full_sample_size_mc.md`
- `manuscript/simulations/output/m78_clean_iid_full_sample_size_mc.json`
- Updated `manuscript/draft.md#55-detailed-sample-size-monte-carlo`
- Updated registry/provenance/planning/log surfaces
- `manuscript/tasks/M78-clean-iid-full-sample-size-mc/outcome.md`
