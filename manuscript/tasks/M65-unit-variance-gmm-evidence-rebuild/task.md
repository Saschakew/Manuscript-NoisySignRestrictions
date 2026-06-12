# M65 Unit-Variance GMM Evidence Rebuild

## Status And Routing

Status: `todo`

Priority: 1

Task-board row: `M65`

Transparency milestone: pending

Outcome note: `outcome.md`

## Original User Prompt

The M64 revision comments require the manuscript to use
\(E[\varepsilon_t\varepsilon_t']=I\), never `diag(B)=1`, and to write Section 4
as a standard GMM estimator over \(B\) and residual-noise variance parameters.

## Why This Task Exists

M64 revised the draft route, but the existing figures, Monte Carlo table,
simulation code, formal registry, and some derivation notes still reflect the
pre-M64 normalized B-plane implementation. M66 has now settled the nuisance
bound: use \(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\), set
\(\nu_i(B,\lambda)=\lambda_i(BB')_{ii}\), and report the projection of
accepted \((B,\lambda)\) pairs onto \(B\). The paper cannot make final
evidence claims until the implementation and evidence match this unit-variance
GMM object.

## Do Not Trust Without Rechecking

- M52 figures and table as evidence for the revised estimator.
- Any code path that parameterizes \(B\) as `[[1,a],[b,1]]`.
- Any robust fourth-order row that uses sample covariance products as generated
  plug-ins rather than parameter-implied \(\omega_{ij}(B,\nu)\), unless it is
  explicitly retained as a comparison.
- Any direct \(0\le\nu_i\le\rho\) bound unless \(\nu_i\) has been redefined in
  structural-unit coordinates. M66 keeps \(\nu_i\) in residual coordinates and
  uses the ratio \(\lambda_i=\nu_i/(BB')_{ii}\).
- The existing Figure 1-3 scripts as active evidence. They are old
  diagonal-normalized B-plane implementations and are historical after M64/M66.
- Any chi-square cutoff for a profiled-\(\nu\) projection before the inference
  route is chosen.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/tasks/M64-revision-20260610-unit-variance-gmm/outcome.md` | Short answer for the repair block. | task execution |
| `manuscript/tasks/M66-noise-ratio-bound-grid-algorithm/outcome.md` | Short answer for the settled nuisance-bound convention. | any figure rebuild |
| `manuscript/derivations/m66-noise-ratio-bound-grid-algorithm.md` | Derivation and algorithm for the \(\lambda\)-bounded projected set. | any implementation |
| `manuscript/draft.md` | Current unit-variance draft route. | code or prose edits |
| `manuscript/formal-object-registry.json` | Formal objects requiring rebuild. | registry edits |
| `manuscript/simulations/sign_dw_robust_noise_grid_figure.py` | Current Figure 1 implementation. | figure rebuild |
| `manuscript/simulations/m45_variance_ratio_evidence.py` | Current evidence implementation. | Monte Carlo rebuild |
| `manuscript/replication/run_all.py` | Replication wrapper to update after scripts change. | replication edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The unit-variance GMM implementation matches Section 4. | `code-implemented` plus `derived` | Code-to-equation audit against draft Section 4. | pending |
| The reported figures/table support the revised estimator. | `code-implemented` | Regenerated outputs and diagnostics. | pending |
| The projected critical value is appropriate for reporting \(B\). | `derived` or `raw-source` | Inference note or source-backed GMM confidence-set argument. | pending |

## Required Work

1. Design the visual chart for the unit-variance \(B\) projection. Do not reuse
   the old \(B=[[1,a],[b,1]]\) chart unless it is explicitly labeled as a
   comparison rather than the active estimator.
2. For each fixed \(\rho\), implement the projected inversion:
   grid/optimize over \(B\), discard singular matrices and sign violations,
   grid/optimize over \(\lambda\in[0,\rho]^2\), set
   \(\nu_i(B,\lambda)=\lambda_i(BB')_{ii}\), compute
   \(J_T(B,\nu(B,\lambda))\), and accept \(B\) if some admissible \(\lambda\)
   gives \(J_T\le c\).
3. Implement the second-order block
   \(\widehat\Sigma_u-BB'-\operatorname{diag}(\nu(B,\lambda))\).
4. Implement \(G_H(B,\nu)\) using parameter-implied \(\omega_{ij}(B,\nu)\).
5. Choose and document the efficient weighting and projection-critical-value route.
6. Regenerate Figure 1, Figure 2, Figure 3, and the Monte Carlo table or mark any output dropped.
7. Update `manuscript/replication/run_all.py`, registry, source packet, paper map, dashboard, and draft evidence text.
8. Complete `outcome.md` and update `QUESTION-INDEX.md` if the task answers a durable implementation or inference question.

## Stop Conditions

- Stop if the unit-variance parameterization makes the current grid incomparable to old figures and no replacement visual design has been selected.
- Stop if the GMM criterion can be implemented only by changing the maintained model.
- Stop if the projection critical value remains unresolved after implementation.

## Acceptance Criteria

- Code and Section 4 use the same \((B,\nu)\) moment vector.
- Figures and table are regenerated or explicitly removed from active evidence.
- Registry statuses distinguish active unit-variance objects from historical M52 outputs.
- `python scripts/check_manuscript.py` passes.

## Expected Outputs

- Updated simulation and replication scripts.
- Regenerated figures/table or an explicit evidence-drop decision.
- Updated draft evidence section and formal registry.
- Completed `outcome.md`.
