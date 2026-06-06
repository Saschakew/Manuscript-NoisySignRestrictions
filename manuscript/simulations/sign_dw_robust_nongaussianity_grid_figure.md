# Sign, Standard DW, And Robust DW Non-Gaussianity Grid

Status: exploratory companion figure candidate.

This figure complements `fig_sign_dw_robust_noise_grid.png`. The first grid
varies residual noise across columns. This grid instead fixes residual noise
and varies the strength of structural-shock non-Gaussianity across columns.

M0020 correction: all three rows now invert pointwise finite-sample J
statistics at the 10 percent level. The robust-DW row is the pure
higher-cumulant J test. It does not use cross covariance or any other
second-moment restriction. When structural shocks are Gaussian, the population
robust moments vanish for every admissible normalized `B`; a finite-sample
pointwise J test can still reject at its nominal size in a particular sample.

Source context:

- Manuscript noise-grid script:
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`
- Manuscript companion script:
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`
- Output figure:
  `manuscript/figures/fig_sign_dw_robust_nongaussianity_grid.png`

Command:

```powershell
python manuscript\simulations\sign_dw_robust_nongaussianity_grid_figure.py
```

## DGP And Grid

The figure uses the same diagonal-normalized B-plane calibration as the noise
grid:

```text
B0 = [[1, -0.45],
      [0.70, 1]]
```

Residual noise is fixed at

```text
V = (0.3, 0.3)
```

and the columns vary the structural-shock mixture

```text
epsilon = sqrt(w) * skewed_chi_square + sqrt(1-w) * Gaussian,
```

where the skewed component is standardized chi-square with `df=5`. The script
then re-standardizes each structural shock to unit variance. The columns use
`w=1`, `w=0.25`, and `w=0`.

## J-Test Cutoffs

All rows use

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

The top sign/covariance row changes little because the second moments and
noise level are held fixed. The standard-DW row still contains the covariance
moment, so it does not become the full graph when higher moments disappear.
The robust-DW row uses only mixed higher cumulants. As the structural shocks
become closer to Gaussian, the robust J-test set widens. With exactly Gaussian
structural shocks, the population robust moments carry no information about
`B`; the figure labels that column as population all-null. The plotted accepted
set is still a finite-sample pointwise J-test realization.

Current fixed-draw diagnostics. Accepted shares are fractions of the full
plotted grid, so the largest possible share is the admissible `b21 >= 0`
portion.

| Structural shocks | Sign/cov `B0` | Standard DW `B0` | Robust DW `B0` | Robust accepted share |
|---|---:|---:|---:|---:|
| Strong non-Gaussianity, `w=1` | in, `J0=1.11` | in, `J0=1.99` | in, `J0=2.91` | 0.315 |
| Weak non-Gaussianity, `w=0.25` | in, `J0=0.74` | in, `J0=3.94` | in, `J0=4.13` | 0.843 |
| Gaussian shocks, `w=0` | in, `J0=0.00` | in, `J0=0.93` | in, `J0=1.03` | 0.843 |

This is the visual limitation that should accompany the main story:
robust-DW protects the target from residual-noise covariance misspecification,
but it cannot create information when the structural shocks carry weak
non-Gaussian higher moments.

This remains a candidate visual. M28/M29 should still check population grids,
weak-moment behavior, and bootstrap or repeated-sample critical values before
the paper treats this as final evidence.
