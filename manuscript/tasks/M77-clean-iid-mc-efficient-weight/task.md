# M77 Clean IID MC Efficient Weight

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M77`

Transparency milestone: `M0072-clean-iid-mc-efficient-weight`

Outcome note: `outcome.md`

## Original User Prompt

"Then plan a task to update mc accordingly. Use the simple formula to compute W.
For the time being, let's not use a large sample to compute W. Just use the
inverse of E(f f)  , that's a simplification to our previous mc, correct?"

## Why This Task Exists

The M74/M75/M76 sample-size Monte Carlo reports `nrDW` truth inclusion below
the nominal 90 percent level. The discussion after M76 identified a likely
finite-sample weighting problem: the current code sample-standardizes primitive
draws, demeans residuals and recovered shocks, and then uses sample-specific
covariance estimates in the quadratic statistic.

This task should build a cleaner size diagnostic. The new MC should use iid
population-normalized shocks and iid Gaussian residual noise directly, so the
per-period moment vector \(f_t(B,\lambda)\) is iid. Under that design, the
efficient GMM weight is the sample-size-invariant object
\[
W(B,\lambda)=\left(E[f_t(B,\lambda)f_t(B,\lambda)']\right)^{-1}.
\]
For this task, compute this object by formula from the assumed shock and noise
distributions, not from a large auxiliary simulation.

The user's question should be answered precisely: this is a simplification of
the previous MC's weighting route because it replaces sample-specific estimated
weights with analytic population weights. It is also a DGP/statistic cleanup,
because the MC should remove within-sample standardization and demeaning.

## Do Not Trust Without Rechecking

- Do not reuse M74 truth-inclusion numbers as evidence for the cleaned iid MC;
  M74 used sample-standardized primitive draws, residual demeaning, recovered
  shock demeaning, and sample-specific pointwise covariance weights.
- Do not call \(E[f_t f_t']^{-1}\) valid if the implemented \(f_t\) still
  depends on sample means, sample variances, or other full-sample
  transformations.
- Do not compute \(W\) from a large auxiliary Monte Carlo for this task. The
  task is specifically to use the formula \(W=(E[f_t f_t'])^{-1}\), with exact
  or explicitly derived distributional moments.
- Do not silently change the sign screen, \(\lambda_i=\nu_i/(BB')_{ii}\)
  convention, displayed projection, or `Sign`/`DW`/`nrDW` table naming unless a
  recheck shows those choices conflict with the cleaned iid design.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm repository/package context. | task execution |
| `manuscript/project-dashboard.md` | Confirm active evidence route and M77 priority. | task execution |
| `manuscript/task-board.md` | Confirm M77 row and dependencies. | task execution |
| `manuscript/source-packet.md` | Confirm active M71-M76 evidence route and caveats. | evidence interpretation |
| `manuscript/draft.md#55-detailed-sample-size-monte-carlo` | Locate Table 2 and current M74 interpretation. | manuscript update work |
| `manuscript/formal-object-registry.json` | Locate affected table/evidence formal objects. | registry edits |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` | Reuse active moment definitions, sign screen, and grid conventions. | code work |
| `manuscript/simulations/m68_first_shock_evidence.py` | Reuse truth-inclusion metric structure. | code work |
| `manuscript/simulations/m69_extended_three_block_mc.py` | Reuse M74 sample-size MC runner structure. | code work |
| `manuscript/simulations/m74_sample_size_mc_500_grid27.md` | Compare old and cleaned MC designs. | interpretation |
| `manuscript/simulations/output/m74_sample_size_mc_500_grid27.json` | Recover old rates and seeds only as historical comparison. | interpretation |
| `manuscript/derivations/m56-robust-cumulant-gmm-generated-moment-audit.md` | Recheck generated-moment and weighting caveats before revising prose. | theory wording |
| `manuscript/derivations/m66-noise-ratio-bound-grid-algorithm.md` | Confirm \(\lambda\)-bound convention. | code and prose |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| With iid per-period moments and \(E[f_t]=0\), the efficient GMM weight is \(W=(E[f_t f_t'])^{-1}\), independent of sample size. | `derived`, `user-decision` | M77 output note and script formula section. | satisfied |
| Removing sample standardization and demeaning makes the MC moment rows iid over time under the stated DGP. | `derived`, `code-implemented` | `m77_clean_iid_mc_efficient_weight.py` uses population-normalized iid draws and no demeaning in residuals or recovered shocks. | satisfied |
| The cleaned MC is a simplification of M74's weighting route. | `derived`, `code-implemented`, `user-decision` | M77 replaces sample-specific estimated weights with analytic population weights. | satisfied |
| The cleaned MC replaces, rather than merely reinterprets, M74 as a size diagnostic. | `derived`, `code-implemented` | M77 is only truth-at-\(B_0\); it supplements rather than replaces M74's full-grid set-size table. | revised: supplement |

## Required Work

1. Derivation work:
   - Write the cleaned iid DGP explicitly:
     \[
     \varepsilon_{it}=(\chi^2_\nu-\nu)/\sqrt{2\nu},\qquad
     \eta_{it}\sim N(0,1),
     \]
     with \(u_t=B_0\varepsilon_t+(\sqrt{\nu_1}\eta_{1t},\sqrt{\nu_2}\eta_{2t})'\).
   - Define the per-period robust moment vector \(f_t(B,\lambda)\) used by the
     active nrDW statistic.
   - Derive or mechanically generate the exact entries of
     \(E[f_t(B,\lambda)f_t(B,\lambda)']\) from independent univariate moments of
     population-normalized chi-square and Gaussian draws.
2. Code or simulation work:
   - Add a cleaned iid MC path that does not sample-standardize primitive draws,
     does not demean residuals, and does not demean recovered shocks.
   - Add analytic efficient-weight computation for \(W(B,\lambda)\). The first
     implementation may support the active bivariate moment stack only.
   - Run a truth-at-\(B_0\) pointwise size check first for `nrDW`; then compare
     `Sign`, `DW`, and `nrDW` if the pointwise diagnostic passes.
   - Preserve the M74 `T=500,1000,2000`, \(V=\operatorname{diag}(0.2,0.2)\),
     strong non-Gaussianity, and `27/7/5` grid comparison unless a stop
     condition is triggered.
3. Manuscript update work:
   - If the cleaned MC supersedes Table 2 as the preferred size diagnostic,
     update `draft.md`, `formal-object-registry.json`,
     `citation-provenance.md`, `source-packet.md`, dashboard, task board, and
     question index as needed.
   - Keep the old M74/M75/M76 result visible as historical or diagnostic if it
     remains useful for explaining the weighting issue.
4. Outcome note work:
   - Answer whether \(E[f f']^{-1}\) is the valid efficient iid GMM weight.
   - Answer whether the cleaned MC is a simplification of the previous MC.
   - Report the cleaned size diagnostic and whether Table 2 should be replaced
     or supplemented.

## Stop Conditions

- Stop if the implemented moment rows still depend on sample means,
  sample variances, or recovered-shock demeaning.
- Stop if \(E[f_t f_t']\) is singular or numerically ill-conditioned at relevant
  candidates and no defensible regularization rule has been specified.
- Stop if the analytic \(E[f f']\) formula disagrees with a small independent
  simulation check beyond Monte Carlo error.
- Stop before replacing Table 2 if the cleaned MC changes the estimand or DGP
  enough that both old and new tables need separate interpretation.

## Acceptance Criteria

- The cleaned DGP uses population-normalized iid shocks/noise and contains no
  sample standardization or demeaning in the MC statistic.
- The nrDW statistic uses \(W(B,\lambda)=(E[f_t(B,\lambda)f_t(B,\lambda)'])^{-1}\),
  computed by formula rather than by a large auxiliary sample.
- A pointwise truth-at-\(B_0\) size diagnostic is reported for
  \(T=500,1000,2000\).
- Any full-grid set-size table clearly labels whether it is the old M74 design
  or the cleaned iid analytic-weight design.
- `python scripts/check_manuscript.py` passes after substantive edits.
- `outcome.md` records the short answer, files changed, questions answered,
  checks, and whether `manuscript/QUESTION-INDEX.md` was updated.

## Expected Outputs

- A cleaned MC script or option under `manuscript/simulations/`.
- A JSON and Markdown output for the cleaned iid analytic-weight MC.
- If results are promoted, revised Table 2 prose or a new table in `draft.md`.
- Updated registry/provenance/planning surfaces and task outcome after
  execution.
