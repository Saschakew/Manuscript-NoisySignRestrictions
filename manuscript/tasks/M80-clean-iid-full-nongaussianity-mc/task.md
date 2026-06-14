# M80 Clean IID Full Non-Gaussianity MC

## Status And Routing

Status: `todo`

Priority: 1

Task-board row: `M80`

Transparency milestone: pending

Outcome note: `outcome.md`

## Original User Prompt

"Plan similar full MCs but based on the dgps from fig 1 and 2"

This task covers the Figure 2 DGPs: the structural non-Gaussianity grid.

## Why This Task Exists

M78 supplies the cleaned iid full-grid Monte Carlo for the Figure 3
sample-size design. The Figure 2 evidence asks a different question: holding
\(T=500\) and residual noise \(V=\operatorname{diag}(0.2,0.2)\) fixed, how do
Sign, DW, and nrDW behave as structural higher-moment information weakens?

This task should run the same cleaned iid full-grid logic as M78, but on the
Figure 2 non-Gaussianity DGPs. It also needs one extra analytic step that M78
did not need: exact raw moments for the structural-shock mixture used in
Figure 2, so that \(W=(E[f_t f_t'])^{-1}\) remains an analytic iid weight and
not a large-sample approximation.

## Do Not Trust Without Rechecking

- Do not treat M69 as a full Monte Carlo. It was a small extended diagnostic
  and is superseded by the M77/M78 cleaned iid design.
- Do not treat the Figure 2 visual grid itself as finite-sample Monte Carlo
  evidence.
- Do not reuse the M78 sample-size scenarios; M80 must vary structural
  non-Gaussianity, not \(T\).
- Do not compute weights from a large auxiliary sample.
- Do not run or promote the weak/Gaussian-shock scenarios until exact raw
  moments for the Figure 2 mixture have been derived and checked.
- Do not sample-standardize shocks or residual noise.
- Do not demean residuals or recovered shocks in the statistic.
- Do not reintroduce a \(B_{21}\) sign restriction. The active sign screen is
  \(B_{11}>0\), \(B_{22}>0\), and \(B_{12}\le0\).

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm repository/package context. | task execution |
| `manuscript/source-packet.md` | Confirm active Figure 2 and M78 status. | interpretation |
| `manuscript/project-dashboard.md` | Confirm current blockers and next action. | task execution |
| `manuscript/paper-map.md` | Confirm evidence role of Figure 2. | draft edits |
| `manuscript/task-board.md` | Confirm task status and dependencies. | task execution |
| `manuscript/draft.md` | Locate affected evidence prose and tables. | draft edits |
| `manuscript/formal-object-registry.json` | Locate affected table/figure objects. | registry edits |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` with `--scenario-set nongaussianity` | Recover exact Figure 2 DGP, sign screen, chart, and moment definitions. | code work |
| `manuscript/simulations/sign_dw_unit_variance_nongaussianity_grid_figure.md` and `manuscript/simulations/output/sign_dw_unit_variance_nongaussianity_grid_figure.json` | Confirm the active M73 Figure 2 configuration and diagnostics. | interpretation |
| `manuscript/simulations/m78_clean_iid_full_sample_size_mc.py` | Reuse cleaned iid full-grid MC machinery. | code work |
| `manuscript/simulations/m77_clean_iid_mc_efficient_weight.py` | Reuse and extend analytic iid weight formulas. | code work |
| `manuscript/simulations/m69_extended_three_block_mc.py` | Compare old non-Gaussianity MC block and summary metrics. | code work |
| `manuscript/simulations/m78_clean_iid_full_sample_size_mc.md` | Match reporting style to M78. | interpretation |
| `.codex/skills/write-standalone-manuscript/references/scientific-claim-audit.md` | Apply claim gate before draft promotion. | prose and registry edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| M80 uses the Figure 2 DGPs: \(T=500\), \(V=(0.2,0.2)\), Gaussian residual noise, and structural non-Gaussianity weights \(w=1,0.25,0\). | `code-implemented`, `user-decision` | Script configuration and JSON output. | pending |
| The Figure 2 structural shock can be handled with exact raw moments for \(x=\sqrt{w}s+\sqrt{1-w}z\), where \(s=(\chi^2_5-5)/\sqrt{10}\) and \(z\sim N(0,1)\) are independent. | `derived`, `code-implemented` | Derivation or checked helper function for raw moments up to the order needed by \(E[f_t f_t']\). | pending |
| M80 uses the cleaned iid design: no sample standardization, no residual demeaning, and no recovered-shock demeaning. | `code-implemented`, `user-decision` | Script implementation and smoke checks. | pending |
| Sign, DW, and nrDW use analytic iid weights for their own moment stacks. | `code-implemented`, `derived` | Weight functions and raw-moment checks. | pending |
| The \(w=0\) Gaussian-shock case has ordinary strong higher-moment identifying power. | `conjectural` | It is expected to be weak or degenerate for higher-moment restrictions and must be reported cautiously. | quarantine |
| Pointwise chi-square inversion is a final projected confidence-set calibration. | `conjectural` | M65 remains open. | quarantine |

## Required Work

1. Derivation work:
   - Derive or document exact raw moments up to the maximum order needed for
     \(E[f_t f_t']\) under
     \(x=\sqrt{w}s+\sqrt{1-w}z\), with independent standardized
     chi-square and Gaussian components.
   - Use convolution/binomial expansion from known raw moments; do not use an
     auxiliary simulation as the source of \(W\).
   - Include a code check against direct observation-level moment construction
     for selected candidates and \(w\) values.
2. Code or simulation work:
   - Add a cleaned iid full-grid non-Gaussianity MC script under
     `manuscript/simulations/`.
   - Reuse the M78 full-grid logic and metric definitions.
   - Use Figure 2 scenarios:
     \(T=500\), \(V=(0.2,0.2)\), and non-Gaussianity weights
     \(w=1\), \(w=0.25\), and \(w=0\).
   - Use the active first-shock chart \((B_{11},B_{21})\), profile
     \(B_{12}\), \(B_{22}\), and \(\lambda\).
   - Keep the M78 intermediate full-MC grid unless a smoke test shows it is
     infeasible: `27/7/5`, 500 replications per scenario.
   - Report Sign, DW, and nrDW truth inclusion, accepted projection shares,
     empty-set rates, warning events, and any weight regularization or
     singularity diagnostics.
3. Manuscript update work:
   - If the full run completes and the analytic moment checks pass, update the
     evidence section with a compact table or paragraph for the Figure 2
     non-Gaussianity MC.
   - Keep the weak-identification/degenerate-higher-moment caveat visible for
     \(w=0\).
   - Keep the pointwise critical-value caveat visible.
   - Update registry, source packet, paper map, dashboard, citation provenance,
     question index, task board, and logs as needed.
4. Outcome note work:
   - Answer whether the Figure 2 full MC has been run under the cleaned iid
     analytic-weight design.
   - Report whether weaker non-Gaussianity mainly widens nrDW, raises empty
     rates, changes truth inclusion, or exposes singular-weight behavior.

## Stop Conditions

- Stop before running or promoting the \(w=0.25\) and \(w=0\) scenarios if the
  exact raw-moment formulas for the mixture are not derived and checked.
- Stop before draft promotion if the script uses sample standardization,
  residual demeaning, recovered-shock demeaning, or auxiliary-simulation
  weights.
- Stop if analytic \(E[f_t f_t']\) is singular across a material part of the
  candidate grid and only regularization drives acceptance; report this as a
  result rather than smoothing it away.
- Stop if the \(w=0\) case degenerates numerically; label it as a Gaussian or
  weak-higher-moment boundary case instead of treating it as a normal power
  comparison.
- Stop if the full 500-replication run is infeasible; in that case report a
  clearly labeled pilot and leave the full run open.
- Stop before claiming projected confidence-set validity; M65 still owns
  projected critical values.

## Acceptance Criteria

- Exact mixture raw-moment code exists and is checked against an independent
  construction.
- A cleaned iid full non-Gaussianity MC script exists and compiles.
- Output exists for all three Figure 2 non-Gaussianity scenarios; if fewer than
  500 replications are used, the reduced count is explicit and justified.
- The Markdown and JSON output report Sign, DW, and nrDW truth inclusion,
  accepted projection shares, empty rates, warning rates, and singularity or
  regularization diagnostics.
- Any draft update is backed by the completed output and preserves the
  weak-moment and pointwise-critical-value caveats.
- `outcome.md` records the short answer and index-update decision.
- `python scripts/check_manuscript.py` passes after edits.

## Expected Outputs

- `manuscript/simulations/m80_clean_iid_full_nongaussianity_mc.py`
- `manuscript/simulations/m80_clean_iid_full_nongaussianity_mc.md`
- `manuscript/simulations/output/m80_clean_iid_full_nongaussianity_mc.json`
- Optional derivation note for exact mixture raw moments if the code is not
  self-explanatory
- Possible draft evidence update for the Figure 2 non-Gaussianity MC
- Updated registry/provenance/planning/log surfaces as needed
- `manuscript/tasks/M80-clean-iid-full-nongaussianity-mc/outcome.md`
