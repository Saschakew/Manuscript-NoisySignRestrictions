# M79 Clean IID Full Residual-Noise MC

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M79`

Transparency milestone: `M0074-m79-clean-iid-residual-noise-mc`

Outcome note: `outcome.md`

## Original User Prompt

"Plan similar full MCs but based on the dgps from fig 1 and 2"

This task covers the Figure 1 DGPs: the residual-noise grid.

## Why This Task Exists

M78 supplies the cleaned iid full-grid Monte Carlo for the Figure 3
sample-size design. It fixes \(V=\operatorname{diag}(0.2,0.2)\), uses strong
structural non-Gaussianity, and varies \(T=500,1000,2000\).

The Figure 1 evidence asks a different finite-sample question: holding
\(T=500\) and strong structural non-Gaussianity fixed, how do Sign, DW, and
nrDW behave as residual noise increases across the three Figure 1 columns?
This task should run the same cleaned iid full-grid logic as M78, but on the
Figure 1 residual-noise DGPs.

## Do Not Trust Without Rechecking

- Do not treat M69 as a full Monte Carlo. It was a small extended diagnostic
  and is superseded by the M77/M78 cleaned iid design.
- Do not treat the Figure 1 visual grid itself as finite-sample Monte Carlo
  evidence.
- Do not reuse the M78 sample-size scenarios; M79 must vary residual noise, not
  \(T\).
- Do not compute weights from a large auxiliary sample. Use the analytic iid
  rule \(W=(E[f_t f_t'])^{-1}\).
- Do not sample-standardize shocks or residual noise.
- Do not demean residuals or recovered shocks in the statistic.
- Do not reintroduce a \(B_{21}\) sign restriction. The active sign screen is
  \(B_{11}>0\), \(B_{22}>0\), and \(B_{12}\le0\).

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm repository/package context. | task execution |
| `manuscript/source-packet.md` | Confirm active Figure 1 and M78 status. | interpretation |
| `manuscript/project-dashboard.md` | Confirm current blockers and next action. | task execution |
| `manuscript/paper-map.md` | Confirm evidence role of Figure 1. | draft edits |
| `manuscript/task-board.md` | Confirm task status and dependencies. | task execution |
| `manuscript/draft.md` | Locate affected evidence prose and tables. | draft edits |
| `manuscript/formal-object-registry.json` | Locate affected table/figure objects. | registry edits |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` | Recover exact Figure 1 DGP, sign screen, chart, and moment definitions. | code work |
| `manuscript/simulations/m78_clean_iid_full_sample_size_mc.py` | Reuse cleaned iid full-grid MC machinery. | code work |
| `manuscript/simulations/m77_clean_iid_mc_efficient_weight.py` | Reuse analytic iid weight formulas and checks. | code work |
| `manuscript/simulations/m69_extended_three_block_mc.py` | Compare old residual-noise MC block and summary metrics. | code work |
| `manuscript/simulations/m78_clean_iid_full_sample_size_mc.md` | Match reporting style to M78. | interpretation |
| `.codex/skills/write-standalone-manuscript/references/scientific-claim-audit.md` | Apply claim gate before draft promotion. | prose and registry edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| M79 uses the Figure 1 DGPs: \(T=500\), strong structural non-Gaussianity, Gaussian residual noise, and \(V=(0,0),(0.2,0.2),(0.5,0.5)\). | `code-implemented`, `user-decision` | Script configuration and JSON output. | pending |
| M79 uses the cleaned iid design: no sample standardization, no residual demeaning, and no recovered-shock demeaning. | `code-implemented`, `user-decision` | Script implementation and smoke checks. | pending |
| Sign, DW, and nrDW use analytic iid weights for their own moment stacks. | `code-implemented`, `derived` | Weight functions and raw-moment checks. | pending |
| nrDW uses candidate-specific analytic \(W(B,\lambda)\). | `code-implemented`, `derived` | Script and output configuration. | pending |
| Pointwise chi-square inversion is a final projected confidence-set calibration. | `conjectural` | M65 remains open. | quarantine |

## Required Work

1. Code or simulation work:
   - Add a cleaned iid full-grid residual-noise MC script under
     `manuscript/simulations/`.
   - Reuse the M78 full-grid logic and metric definitions.
   - Use Figure 1 scenarios:
     \(T=500\), strong structural non-Gaussianity, and residual noise
     \(V=(0,0)\), \(V=(0.2,0.2)\), and \(V=(0.5,0.5)\).
   - Use the active first-shock chart \((B_{11},B_{21})\), profile
     \(B_{12}\), \(B_{22}\), and \(\lambda\).
   - Keep the M78 intermediate full-MC grid unless a smoke test shows it is
     infeasible: `27/7/5`, 500 replications per scenario.
   - Report Sign, DW, and nrDW truth inclusion, accepted projection shares,
     empty-set rates, and the DW-misses/nrDW-contains warning event.
2. Verification work:
   - Run a compile check and a small smoke run.
   - Verify the no-noise scenario has true \(\lambda=0\) on the lambda grid or
     is otherwise handled exactly.
   - Verify analytic weights are not being silently replaced by
     sample-specific covariance estimates.
3. Manuscript update work:
   - If the full run completes, update the evidence section with a compact
     table or paragraph for the Figure 1 residual-noise MC.
   - Keep the pointwise critical-value caveat visible.
   - Update registry, source packet, paper map, dashboard, citation provenance,
     question index, task board, and logs as needed.
4. Outcome note work:
   - Answer whether the Figure 1 full MC has been run under the cleaned iid
     analytic-weight design.
   - Report whether increasing residual noise mainly affects truth inclusion,
     set size, empty-set rates, or the warning event.

## Stop Conditions

- Stop before draft promotion if the script uses sample standardization,
  residual demeaning, recovered-shock demeaning, or auxiliary-simulation
  weights.
- Stop if the no-noise scenario does not evaluate the true \(\lambda=0\)
  configuration correctly.
- Stop if analytic \(E[f_t f_t']\) is singular across a material part of the
  candidate grid and only regularization drives acceptance.
- Stop if the full 500-replication run is infeasible; in that case report a
  clearly labeled pilot and leave the full run open.
- Stop before claiming projected confidence-set validity; M65 still owns
  projected critical values.

## Acceptance Criteria

- A cleaned iid full residual-noise MC script exists and compiles.
- Output exists for all three Figure 1 residual-noise scenarios; if fewer than
  500 replications are used, the reduced count is explicit and justified.
- The Markdown and JSON output report Sign, DW, and nrDW truth inclusion,
  accepted projection shares, empty rates, and warning rates.
- Any draft update is backed by the completed output and preserves the
  pointwise-critical-value caveat.
- `outcome.md` records the short answer and index-update decision.
- `python scripts/check_manuscript.py` passes after edits.

## Expected Outputs

- `manuscript/simulations/m79_clean_iid_full_residual_noise_mc.py`
- `manuscript/simulations/m79_clean_iid_full_residual_noise_mc.md`
- `manuscript/simulations/output/m79_clean_iid_full_residual_noise_mc.json`
- Possible draft evidence update for the Figure 1 residual-noise MC
- Updated registry/provenance/planning/log surfaces as needed
- `manuscript/tasks/M79-clean-iid-full-residual-noise-mc/outcome.md`
