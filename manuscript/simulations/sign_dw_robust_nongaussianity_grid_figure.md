# Sign, Standard DW, And Variance-Ratio Robust DW Non-Gaussianity Grid

Status: M52 source-correct rebuild of the M43 companion figure for the M0036
variance-ratio robust DW proposal.

This figure complements `fig_sign_dw_relative_noise_robust_grid.png`. The
first grid varies residual noise across columns. This grid instead fixes
residual noise at \(V=(0.2,0.2)\) and varies the strength of structural-shock
non-Gaussianity across columns.

The middle row uses the same source-correct standard-DW GMM1 screen as
Figure 1. The bottom row uses the same variance-ratio robust row as Figure 1:
generated mixed higher-cumulant J inversion with central-delta weighting plus
the covariance-decomposition screen
\(0\le \nu_i\le 0.5\operatorname{Var}(\varepsilon_i)\). The superseded
diagonal-anchor covariance restriction is not used.

Source context:

- Manuscript noise-grid script:
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`
- Manuscript companion script:
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`
- Output figure:
  `manuscript/figures/fig_sign_dw_robust_nongaussianity_grid.png`
- M52 validation and Monte Carlo note:
  `manuscript/simulations/m52_source_correct_evidence.md`

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
- Middle row: source-correct standard DW GMM1 row, testing `112`, `122`,
  `1112`, `1122`, and `1222` with cutoff `chi2_5(0.90) = 9.24`, intersected
  with the separate covariance screen.
- Bottom row: variance-ratio robust DW row, testing five generated mixed
  higher cumulants with central-delta weighting; cutoff
  `chi2_5(0.90) = 9.24`, intersected with the relative
  covariance-decomposition screen.

## Interpretation

The top sign/covariance row changes little because the second moments and
noise level are held fixed. The standard-DW row still contains the no-noise
covariance moment, so it does not become the full graph when higher moments
disappear. The robust-DW row drops recovered-shock covariance restrictions and
uses the relative noise-to-shock variance screen for scale information.

M52 fixed-grid diagnostics, computed on a `61 x 61` grid plus the true point,
give the following chi-square-primary reading:

| Structural shocks | Standard DW truth | Robust DW truth | Robust feasible | Standard share | Robust share |
|---|---:|---:|---:|---:|---:|
| Strong non-Gaussianity, `w=1` | yes | yes | yes | 0.035 | 0.061 |
| Weak non-Gaussianity, `w=0.25` | yes | yes | yes | 0.105 | 0.116 |
| Gaussian shocks, `w=0` | yes | yes | yes | 0.118 | 0.188 |

This is the visual limitation that should accompany the main story:
variance-ratio robust DW protects the target from residual-noise covariance
misspecification, but the higher-cumulant part cannot create information when
the structural shocks carry weak non-Gaussian higher moments.
