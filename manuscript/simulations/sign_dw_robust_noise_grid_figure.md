# Sign, Standard DW, And Robust DW Noise Grid

Status: corrected exploratory manuscript-local figure candidate.

This is the corrected version of the KnowledgeVault B-plane figure requested in
M0017. It uses the two-by-three sign/DW layout from the synthesis and adds a
third robust-DW row. The M0020 correction is that all three rows now invert
pointwise finite-sample J statistics at the 10 percent level. The robust-DW row
uses only mixed higher cumulants as restrictions; second moments enter only as
nuisance quantities inside fourth-cumulant estimation.

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
B0 = [[1, -0.45],
      [0.70, 1]]
```

and evaluates three diagonal-noise columns:

```text
V = (0, 0), (0.3, 0.3), (2, 2).
```

The structural shocks are standardized chi-square shocks with `df=5`. The
additive residual noise is Gaussian and standardized before applying the
diagonal noise variance. This keeps the residual-noise covariance distortion in
the sign and standard-DW rows, while ensuring that the pure robust-DW
higher-cumulant row is not contaminated by non-Gaussian transformed noise.

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
- Bottom row: pure robust-DW row, testing two mixed third cumulants and three
  mixed fourth cumulants; cutoff `chi2_5(0.90) = 9.24`. Cross covariance is not
  a restriction in this row.

## Interpretation

The top row shows the sign/covariance accepted B-plane band. The middle row
shows how standard DW refines that band using recovered-shock independence
moments under the no-noise two-shock representation. The accepted region moves
away from the true no-noise `B0` as the covariance target becomes noisy.

The bottom row shows the pure robust-DW higher-cumulant J-test set. It is no
longer forced to be invariant across noise columns, because it is a finite
sample J inversion with sample weighting. In this draw, the high-noise column
shows the intended stress case: sign/covariance and standard DW reject the
true `B0`, while robust DW remains wide and contains `B0`.

Current fixed-draw diagnostics. Accepted shares are fractions of the full
plotted grid, so the largest possible share is the admissible `b21 >= 0`
portion.

| Noise `V` | Sign/cov `B0` | Standard DW `B0` | Robust DW `B0` | Robust accepted share |
|---|---:|---:|---:|---:|
| `(0,0)` | in, `J0=0.38` | in, `J0=0.87` | in, `J0=0.70` | 0.136 |
| `(0.3,0.3)` | in, `J0=0.44` | in, `J0=1.12` | in, `J0=3.33` | 0.301 |
| `(2,2)` | out, `J0=7.51` | out, `J0=10.88` | in, `J0=5.53` | 0.843 |

This is still a candidate figure. The chi-square cutoffs are pointwise guides;
final evidence should still check bootstrap or repeated-sample critical values
and weak-moment behavior in M28 and M29.
