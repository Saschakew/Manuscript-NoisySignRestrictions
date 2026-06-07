# Sign, Standard DW, And Variance-Ratio Robust DW Non-Gaussianity Grid

Status: rebuilt M43 companion figure for the M0036 variance-ratio robust DW
proposal.

This figure complements `fig_sign_dw_relative_noise_robust_grid.png`. The
first grid varies residual noise across columns. This grid instead fixes
residual noise at \(V=(0.2,0.2)\) and varies the strength of structural-shock
non-Gaussianity across columns.

The bottom row now uses the same variance-ratio robust row as Figure 1: pure
mixed higher-cumulant J inversion plus the covariance-decomposition screen
\(0\le \nu_i\le 0.5\operatorname{Var}(\varepsilon_i)\). The superseded
diagonal-anchor covariance restriction is not used.

Source context:

- Manuscript noise-grid script:
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`
- Manuscript companion script:
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`
- Output figure:
  `manuscript/figures/fig_sign_dw_robust_nongaussianity_grid.png`
- M45 validation and Monte Carlo note:
  `manuscript/simulations/m45_variance_ratio_evidence.md`

Command:

```powershell
python manuscript\simulations\sign_dw_robust_nongaussianity_grid_figure.py
```

## DGP And Grid

The figure uses the same diagonal-normalized B-plane calibration as the noise
grid:

```text
B0 = [[1, -0.25],
      [0.80, 1]]
```

Residual noise is fixed at:

```text
V = (0.2, 0.2)
```

The columns vary the structural-shock mixture:

```text
epsilon = sqrt(w) * skewed_chi_square + sqrt(1-w) * Gaussian,
```

where the skewed component is standardized chi-square with `df=5`. The script
then re-standardizes each structural shock to unit variance. The columns use
`w=1`, `w=0.25`, and `w=0`.

## J-Test Cutoffs

All rows use:

```text
J(B) = N mean(f(B))' S(B)^(-1) mean(f(B))
```

with `N=500`, and accept `B` when `J(B) <= chi2_df(0.90)`.

- Top row: sign/covariance row, testing `e1*e2`; cutoff
  `chi2_1(0.90) = 2.71`.
- Middle row: standard DW row, testing covariance, two co-skewness moments,
  and one fourth cross moment; cutoff `chi2_4(0.90) = 7.78`.
- Bottom row: variance-ratio robust DW row, testing five mixed higher
  cumulants; cutoff `chi2_5(0.90) = 9.24`, intersected with the relative
  covariance-decomposition screen.

## Interpretation

The top sign/covariance row changes little because the second moments and
noise level are held fixed. The standard-DW row still contains the no-noise
covariance moment, so it does not become the full graph when higher moments
disappear. The robust-DW row drops recovered-shock covariance restrictions and
uses the relative noise-to-shock variance screen for scale information.

M45 fixed-grid diagnostics, computed on a `61 x 61` grid plus the true point,
give the following chi-square-primary reading:

| Structural shocks | Standard DW truth | Robust DW truth | Robust feasible | Robust accepted share |
|---|---:|---:|---:|---:|
| Strong non-Gaussianity, `w=1` | yes | yes | yes | 0.089 |
| Weak non-Gaussianity, `w=0.25` | yes | yes | yes | 0.196 |
| Gaussian shocks, `w=0` | yes | yes | yes | 0.188 |

This is the visual limitation that should accompany the main story:
variance-ratio robust DW protects the target from residual-noise covariance
misspecification, but the higher-cumulant part cannot create information when
the structural shocks carry weak non-Gaussian higher moments.
