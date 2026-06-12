# M66 Noise-Ratio Bound And Grid Algorithm

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M66`

Transparency milestone: `M0062-execute-m66-noise-ratio-bound`; GitHub
milestone #57

Outcome note: `outcome.md`

## Original User Prompt

"plan a follow up task: in setion 4 you write
0<v_i<rho(BB')_ii. but istn the variance of the structural shock one by
construction when we use Sigma_u = BB' -V? So for a 0<rho<1 rho will
automaticall be the noise information ratio? so we can use 0<v<rho directly?
second, when you write the set R_T(c,rho), you write R(B)>=0 as a restriction
and in the same way, we can write 0<v<rho as a restriction, cant we? and
practically, when we try to find the set R_T we whould build a grid over B and
rho, for each B and vcheck the restriction, then compute J_T(B,v) and check if
it is <c from chi2. thats our inverted set? if this is correct, update the
section 4 and also update the figures 1,2,3 to use this algorithm."

## Why This Task Exists

M64 rewrote Section 4 as a unit-variance GMM route over \((B,\nu)\), but the
noise-bound interpretation needs one more derivation before M65 rebuilds
figures. The core ambiguity is not whether the nuisance bound belongs in the
set definition. It does. The ambiguity is whether \(\nu_i\) is measured in the
observed residual coordinate or in a unit structural-shock coordinate. That
choice determines whether the correct restriction is
\(0\le\nu_i\le\rho(BB')_{ii}\), \(0\le\nu_i\le\rho\), or a reparameterized
share \(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\).

## Do Not Trust Without Rechecking

- Section 4's current bound \(0\le\nu_i\le\rho(BB')_{ii}\) as final wording.
- Any shortcut saying \(0\le\nu_i\le\rho\) is automatically a
  noise-information ratio just because \(E[\varepsilon_i^2]=1\).
- Any figure code that grids only over the old normalized B-plane.
- Any caption that still says \(0\le\nu_i\le0.5\operatorname{Var}(\varepsilon_i)\)
  without specifying which coordinate carries the noise variance.
- The user's sign convention \(\Sigma_u=BB'-V\) as written. The maintained
  model is \(\Sigma_u=BB'+V\); after rearranging, \(V=\Sigma_u-BB'\).

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/draft.md` | Locate Section 4 and figure-caption language. | derivation and prose edits |
| `manuscript/tasks/M64-revision-20260610-unit-variance-gmm/outcome.md` | Confirm the unit-variance normalization decision. | task execution |
| `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/task.md` | Update the evidence rebuild dependency and algorithm. | M65 edits |
| `manuscript/formal-object-registry.json` | Locate affected definitions, equations, figures, and table objects. | registry edits |
| `manuscript/simulations/sign_dw_robust_noise_grid_figure.py` | Current Figure 1 generator. | figure algorithm edits |
| `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py` | Current Figure 2 generator. | figure algorithm edits |
| `manuscript/simulations/sign_dw_sample_size_robust_grid_figure.py` | Current Figure 3 generator. | figure algorithm edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| Under the maintained additive model, \(\Sigma_u=BB'+V\), while \(V=\Sigma_u-BB'\) is the implied leftover covariance. | `derived` | `manuscript/derivations/m66-noise-ratio-bound-grid-algorithm.md` | passed |
| Because \(E[\varepsilon_i^2]=1\), a direct cap \(0\le\nu_i\le\rho\) is valid only if \(\nu_i\) is defined in a structural-unit coordinate or the residual coordinate is otherwise standardized. | `derived` | Coordinate-scale derivation in `manuscript/derivations/m66-noise-ratio-bound-grid-algorithm.md`. | passed |
| If \(\nu_i\) remains observed-coordinate residual-noise variance, the scale-invariant residual-noise-to-structural-signal bound is \(0\le\nu_i\le\rho(BB')_{ii}\), equivalently \(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\). | `derived` | Ratio definition and dimension check in the M66 derivation note. | passed |
| The robust accepted set can write nuisance bounds beside \(R(B)\ge0\) as maintained restrictions. | `derived` | Revised Section 4 set definition. | passed |
| The practical inversion for fixed \(\rho\) accepts \(B\) if there exists admissible \(\nu\) such that all restrictions hold and \(J_T(B,\nu)\le c\). | `derived`; figure code historical | Algorithm note and draft update. Existing Figure 1-3 scripts are marked historical and must be replaced in M65. | passed with M65 follow-up |

## Required Work

1. Write the coordinate-scale derivation that decides whether the manuscript
   should keep \(0\le\nu_i\le\rho(BB')_{ii}\), switch to
   \(0\le\nu_i\le\rho\), or use \(\lambda_i\in[0,\rho]\) notation.
2. Rewrite Section 4 so the bound appears as a restriction in
   \(\mathcal R_T(c;\rho)\) beside \(R(B)\ge0\), with the chosen coordinate
   interpretation stated before the set display.
3. State the computational algorithm explicitly: for each fixed \(\rho\), grid
   over \(B\) and over admissible \(\nu\) or \(\lambda\), check the sign,
   covariance-feasibility, and nuisance-bound restrictions, compute
   \(J_T(B,\nu)\), and accept \(B\) when at least one nuisance value satisfies
   \(J_T(B,\nu)\le c\). If multiple \(\rho\) values are shown, repeat this
   inversion for each sensitivity value.
4. Update M65's figure algorithm so Figures 1, 2, and 3 use the same
   restriction and projection rule as Section 4.
5. Rebuild Figures 1, 2, and 3 only after the derivation and Section 4 wording
   are aligned.
6. Update the formal registry, paper map, source packet, dashboard, task board,
   and question index if the task settles the notation or algorithm.
7. Complete `outcome.md` with the short answer to the user's questions.

## Stop Conditions

- Stop before changing figures if the task cannot define the coordinate of
  \(\nu_i\) unambiguously.
- Stop before adopting \(0\le\nu_i\le\rho\) if it would make the bound depend
  on arbitrary residual-unit scaling.
- Stop before using a chi-square cutoff if the projection over nuisance
  variances changes the intended pointwise critical-value interpretation.
- Stop if the old figure parameterization cannot represent the revised
  unit-variance \(B\) grid without a new visual design.

## Acceptance Criteria

- Section 4 and the figure code use the same nuisance-bound convention.
- The task outcome answers the user's three questions: direct \(v<\rho\),
  writing the nuisance bound in \(\mathcal R_T\), and the grid/J-test inversion.
- Figures 1, 2, and 3 are either rebuilt with the new algorithm or explicitly
  kept historical with a follow-up reason.
- M65 is unblocked only after the algorithm is settled.
- `python scripts/check_manuscript.py` passes.

## Expected Outputs

- A compact derivation or outcome note on the noise-ratio bound.
- Updated Section 4 notation and set definition.
- Updated Figure 1, Figure 2, and Figure 3 algorithms and outputs if the
  derivation clears the change.
- Updated M65 packet and planning surfaces.
