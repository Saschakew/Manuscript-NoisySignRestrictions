# Sign, Standard DW, And Robust DW Noise Grid

Status: superseded for the robust row after the M0034 scale correction.

M0034 warning: the diagonal-anchor robust row in this note uses
`sample_cov(u1,u2) - (b12 + b21) = 0`. Under the active diagonal-normalized
chart `diag(B)=1`, that equality also requires unit structural-shock
variances. With free shock scales, the off-diagonal covariance is
`Sigma_u,12 = b21*sigma_1^2 + b12*sigma_2^2`. The active diagnostic variant is
now documented in `manuscript/simulations/sign_dw_pure_robust_noise_grid_figure.md`.

This is the corrected version of the KnowledgeVault B-plane figure requested in
M0017. It uses the two-by-three sign/DW layout from the synthesis and adds a
third robust-DW row. The M0020 correction was that all three rows invert
pointwise finite-sample J statistics at the 10 percent level. The M0030
revision fixes the high-noise power problem by replacing the pure
higher-cumulant row with a diagonal-noise robust row: it profiles out diagonal
residual-noise variances and keeps only the off-diagonal covariance restriction
that survives `Sigma_u = B B' + V` with diagonal `V`, plus mixed higher
cumulants of `B^{-1}u`.

Source context:

- KnowledgeVault synthesis:
  `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md`
- KnowledgeVault B-plane visualization lab:
  `replications/svar-noise-recursive-sign-visualization/noisy_svar_visuals.py`
- KnowledgeVault robust inversion lab:
  `replications/bonhomme-robin-noise-robust-svar/br_noise_robust_svar.py`
- Manuscript script:
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`
- Output figure:
  `manuscript/figures/fig_sign_dw_robust_noise_grid.png`

Command:

```powershell
python manuscript\simulations\sign_dw_robust_noise_grid_figure.py
```

## DGP And Grid

The figure uses the diagonal-normalized B-plane calibration

```text
B0 = [[1, -0.25],
      [0.80, 1]]
```

and evaluates three diagonal-noise columns:

```text
V = (0, 0), (0.2, 0.2), (0.5, 0.5).
```

The structural shocks are standardized chi-square shocks with `df=5`. The
additive residual noise is Gaussian and standardized before applying the
diagonal noise variance. The revised high-noise column is deliberately lower
than the discarded `V=(2,2)` stress case. The selected `B0` makes covariance
distortion visible at `V=(0.5,0.5)` without needing unrealistically large
Gaussian noise.

The grid is `B(b12,b21) = [[1,b12],[b21,1]]`, with the sign restriction
`b21 >= 0`.

## J-Test Cutoffs

All rows use the finite-sample statistic

```text
J(B) = N mean(f(B))' S(B)^(-1) mean(f(B))
```

with `N=500`, and accept `B` when `J(B) <= chi2_df(0.90)`.

- Top row: sign/covariance row, testing `e1*e2`; cutoff
  `chi2_1(0.90) = 2.71`.
- Middle row: standard DW row, testing covariance, two co-skewness moments,
  and one fourth cross moment; cutoff `chi2_4(0.90) = 7.78`.
- Bottom row: diagonal-noise robust-DW row, testing the off-diagonal
  covariance restriction
  `sample_cov(u1,u2) - (b12 + b21) = 0` and five mixed higher cumulants;
  cutoff `chi2_6(0.90) = 10.64`. This row does not impose recovered-shock
  zero covariance or unit variances.

## Interpretation

The top row shows the sign/covariance accepted B-plane band. The middle row
shows how standard DW refines that band using recovered-shock independence
moments under the no-noise two-shock representation. The accepted region moves
away from the true no-noise `B0` as the covariance target becomes noisy.

The bottom row shows the diagonal-noise robust-DW J-test set. It is no longer
the pure higher-cumulant lower-power diagnostic. Instead, it uses the part of
second moments that diagonal residual noise cannot bias and combines it with
the Gaussian-noise robust higher-cumulant stack. In this draw, the high-noise
column shows the intended stress case at the lower `V=(0.5,0.5)` level:
sign/covariance and standard DW reject the true `B0`, while robust DW remains
informative and contains `B0`.

Current fixed-draw diagnostics. Accepted shares are fractions of the full
plotted grid, so the largest possible share is the admissible `b21 >= 0`
portion.

| Noise `V` | Sign/cov `B0` | Standard DW `B0` | Robust DW `B0` | Robust accepted share |
|---|---:|---:|---:|---:|
| `(0,0)` | in, `J0=0.38` | in, `J0=0.87` | in, `J0=0.84` | 0.048 |
| `(0.2,0.2)` | in, `J0=1.70` | in, `J0=4.02` | in, `J0=3.65` | 0.079 |
| `(0.5,0.5)` | out, `J0=9.20` | out, `J0=15.49` | in, `J0=7.06` | 0.125 |

This is still a candidate figure. The chi-square cutoffs are pointwise guides;
M28/M29 must be rerun after the M0030 statistic change before the manuscript
uses coverage-style table claims.
