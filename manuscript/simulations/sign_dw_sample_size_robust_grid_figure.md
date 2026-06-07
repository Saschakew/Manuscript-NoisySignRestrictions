# Sign, Standard DW, And Variance-Ratio Robust DW Sample-Size Grid

Status: created M44 companion figure for the M0036 variance-ratio robust DW
proposal.

This figure fixes the Figure 1 structural non-Gaussianity calibration and the
Figure 2 residual-noise calibration, then varies only sample size. It is meant
to show whether the standard-DW and variance-ratio robust-DW sets tighten
differently as finite-sample noise falls.

Source context:

- Figure script:
  `manuscript/simulations/sign_dw_sample_size_robust_grid_figure.py`
- Output figure:
  `manuscript/figures/fig_sign_dw_sample_size_robust_grid.png`
- M45 validation and Monte Carlo note:
  `manuscript/simulations/m45_variance_ratio_evidence.md`

Command:

```powershell
python manuscript\simulations\sign_dw_sample_size_robust_grid_figure.py
```

## DGP And Grid

The figure uses the diagonal-normalized B-plane:

```text
B0 = [[1, -0.25],
      [0.80, 1]]
```

The structural shocks use the strong non-Gaussian chi-square calibration from
Figure 1. Residual noise is fixed at:

```text
V = (0.2, 0.2)
```

The columns use `T=500`, `T=1000`, and `T=2000`.

## J-Test Cutoffs

All rows invert pointwise 10 percent J tests.

- Top row: sign/covariance row, testing `e1*e2`; cutoff
  `chi2_1(0.90) = 2.71`.
- Middle row: standard DW row, testing covariance, two co-skewness moments,
  and one fourth cross moment; cutoff `chi2_4(0.90) = 7.78`.
- Bottom row: variance-ratio robust DW row, testing five mixed higher
  cumulants; cutoff `chi2_5(0.90) = 9.24`, intersected with the relative
  covariance-decomposition screen \(0\le \nu_i\le
  0.5\operatorname{Var}(\varepsilon_i)\).

## Interpretation

In the rendered fixed draw, the standard-DW set shrinks and misses the true
normalized impact at the larger sample sizes. The variance-ratio robust row
keeps the true point in all three sample-size columns and becomes visibly
tighter by `T=2000`.

M45 fixed-grid diagnostics, computed on a `61 x 61` grid plus the true point,
give:

| Sample size | Standard DW truth | Robust DW truth | Robust feasible | Robust accepted share |
|---|---:|---:|---:|---:|
| `T=500` | yes | yes | yes | 0.089 |
| `T=1000` | no | yes | yes | 0.028 |
| `T=2000` | no | yes | yes | 0.042 |

The last column is not monotone in this single fixed draw because the hard
screen and finite-sample higher-cumulant statistic move together. The figure
should be read with the repeated-sample M45 Monte Carlo table, not as a
coverage claim by itself.
