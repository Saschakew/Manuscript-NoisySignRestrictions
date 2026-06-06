# Sign, Standard DW, And Robust DW Non-Gaussianity Grid

Status: revised exploratory companion figure candidate after the M0030 power audit.

This figure complements `fig_sign_dw_robust_noise_grid.png`. The first grid
varies residual noise across columns. This grid instead fixes residual noise
and varies the strength of structural-shock non-Gaussianity across columns.

M0020 correction: all three rows invert pointwise finite-sample J statistics
at the 10 percent level. The M0030 revision changes the robust-DW row from the
pure higher-cumulant J test to the diagonal-noise robust J test. It uses the
off-diagonal residual covariance restriction that survives diagonal residual
noise, plus mixed higher cumulants. When structural shocks are Gaussian, the
higher-cumulant substack is population all-null, but the covariance anchor
still restricts the normalized chart.

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
B0 = [[1, -0.25],
      [0.80, 1]]
```

Residual noise is fixed at

```text
V = (0.2, 0.2)
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
- Bottom row: diagonal-noise robust-DW row, testing the off-diagonal residual
  covariance restriction and five mixed higher cumulants; cutoff
  `chi2_6(0.90) = 10.64`. Recovered-shock cross covariance is not a
  restriction in this row.

## Interpretation

The top sign/covariance row changes little because the second moments and
noise level are held fixed. The standard-DW row still contains the covariance
moment, so it does not become the full graph when higher moments disappear.
The robust-DW row uses the off-diagonal covariance anchor plus mixed higher
cumulants. As the structural shocks become closer to Gaussian, the
higher-cumulant part loses identifying content and the robust J-test set
widens toward the covariance band. With exactly Gaussian structural shocks,
the higher-cumulant substack carries no information about `B`; the plotted set
is then driven by the covariance anchor and finite-sample pointwise variation.

Current fixed-draw diagnostics. Accepted shares are fractions of the full
plotted grid, so the largest possible share is the admissible `b21 >= 0`
portion.

| Structural shocks | Sign/cov `B0` | Standard DW `B0` | Robust DW `B0` | Robust accepted share |
|---|---:|---:|---:|---:|
| Strong non-Gaussianity, `w=1` | in, `J0=2.15` | in, `J0=3.88` | in, `J0=2.34` | 0.087 |
| Weak non-Gaussianity, `w=0.25` | in, `J0=2.07` | in, `J0=5.97` | in, `J0=5.08` | 0.142 |
| Gaussian shocks, `w=0` | in, `J0=0.46` | in, `J0=1.74` | in, `J0=1.46` | 0.184 |

This is the visual limitation that should accompany the main story:
robust-DW protects the target from residual-noise covariance misspecification,
but the higher-cumulant part cannot create information when the structural
shocks carry weak non-Gaussian higher moments.

This remains a candidate visual. M28/M29 should still check population grids,
weak-moment behavior, and bootstrap or repeated-sample critical values before
the paper treats this as final evidence.
