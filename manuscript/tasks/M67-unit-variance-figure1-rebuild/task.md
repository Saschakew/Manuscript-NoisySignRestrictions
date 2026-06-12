# M67 Unit-Variance Figure 1 Rebuild

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M67`

Transparency milestone: `M0063-rebuild-unit-variance-figure-1`; GitHub
milestone #58

Outcome note: `outcome.md`

## Original User Prompt

"can you build the correct updated figure 1?"

## Why This Task Exists

M64 changed the active normalization to
\(E[\varepsilon_t\varepsilon_t']=I\). M66 then settled the nuisance bound as
\(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\). The existing Figure 1 script still
uses the old diagonal-normalized B-plane
\(B=\begin{bmatrix}1&b_{12}\\ b_{21}&1\end{bmatrix}\), so it cannot be the
active evidence figure for Section 4. This task builds only the corrected
Figure 1 residual-noise grid, leaving Figures 2-3 and the Monte Carlo table to
the broader M65 rebuild.

## Do Not Trust Without Rechecking

- The old `fig_sign_dw_relative_noise_robust_grid.png` as active evidence.
- Any implementation that fixes `diag(B)=1`.
- Any robust row that screens covariance outside the GMM vector instead of
  using the Section 4 second-order block.
- Any direct residual-coordinate \(0\le\nu_i\le\rho\) bound instead of
  \(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\).
- Any claim that this task completes M65; it only builds Figure 1.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/task.md` | Broader evidence-rebuild contract. | implementation |
| `manuscript/tasks/M66-noise-ratio-bound-grid-algorithm/outcome.md` | Settled nuisance-bound convention. | implementation |
| `manuscript/derivations/m66-noise-ratio-bound-grid-algorithm.md` | Projected \(B,\lambda\) algorithm. | implementation |
| `manuscript/draft.md` | Section 4 and current Figure 1 text. | draft edits |
| `manuscript/formal-object-registry.json` | Figure and robust-set object statuses. | registry edits |
| `manuscript/simulations/sign_dw_robust_noise_grid_figure.py` | Historical Figure 1 code to avoid reusing the wrong chart. | implementation |
| `manuscript/replication/run_all.py` | Figure 1 replication command. | replication edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The Figure 1 robust row uses \(\nu_i(B,\lambda)=\lambda_i(BB')_{ii}\) with \(\lambda\in[0,\rho]^2\). | `code-implemented` plus `derived` | M66 derivation and `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py`. | passed |
| The Figure 1 robust criterion stacks the Section 4 second-order block with parameter-implied higher-moment rows. | `code-implemented` plus `derived` | Code-to-equation audit against Section 4 and generated diagnostic note. | passed |
| The Figure 1 standard-DW row is still the no-noise unit-variance comparator, not a robust estimator. | `code-implemented` plus `derived` | Section 3 and new Figure 1 diagnostics. | passed |

## Required Work

1. Choose a two-dimensional visual projection for the unit-variance \(B\) set
   that does not impose `diag(B)=1`.
2. Implement the Figure 1 residual-noise grid under the M66 projected
   \((B,\lambda)\) algorithm.
3. Generate the replacement PNG and a compact simulation note with
   diagnostics and interpretation limits.
4. Update the draft, registry, figure/simulation README, replication wrapper,
   dashboard, task board, logs, and M65 packet to show Figure 1 is rebuilt but
   the remaining evidence is still pending.
5. Complete `outcome.md` and decide whether `QUESTION-INDEX.md` needs an
   update.

## Stop Conditions

- Stop if the visual chart cannot be stated without a hidden `diag(B)=1`
  normalization.
- Stop if the robust row cannot compute the Section 4 moment vector at
  \((B,\nu(B,\lambda))\).
- Stop if the generated Figure 1 does not contain the true \(B_0\) in the
  robust row for the high-noise design despite the true
  \(\lambda_i\le\rho\) condition holding.
- Stop if the projection critical value issue would make the figure appear
  more inferentially final than it is; record it as pointwise diagnostic if so.

## Acceptance Criteria

- A new active Figure 1 image is written under `manuscript/figures/`.
- The script generating it does not impose `diag(B)=1`.
- The robust row searches over admissible \(\lambda\) and uses
  \(J_T(B,\nu(B,\lambda))\).
- The draft no longer calls Figure 1 historical.
- M65 remains open for Figures 2-3 and the Monte Carlo table.
- `python scripts/check_manuscript.py` passes.

## Expected Outputs

- New Figure 1 script and output image.
- New Figure 1 simulation note.
- Updated draft Figure 1 text and registry statuses.
- Updated replication command for `--stage figure1`.
- Completed task outcome note.
