# Pure Robust DW Noise Grid Variant

Status: M0034 scale-correction diagnostic.

This note records the Figure 1 variant requested after the scale-normalization
correction. The bottom row drops the M0030 off-diagonal covariance anchor and
uses only the five mixed higher-cumulant moments of `B^{-1}u`.

Command:

```powershell
python manuscript\simulations\sign_dw_robust_noise_grid_figure.py --robust-mode pure
```

Output:

- `manuscript/figures/fig_sign_dw_pure_robust_noise_grid.png`

## Correction

In the diagonal-normalized chart

```text
B = [[1, b12],
     [b21, 1]]
```

the off-diagonal covariance under diagonal residual noise is

```text
Sigma_u,12 = b21 * sigma_1^2 + b12 * sigma_2^2
```

when structural shock variances are not separately normalized to one. Therefore
the previous anchor `Sigma_u,12 = b12 + b21` double-normalizes scale and should
not be used in the active robust-DW set.

## Fixed-Draw Diagnostics

Accepted shares are fractions of the full plotted grid. The admissible-grid
share divides only by nonsingular grid points with `b21 >= 0`.

| Noise `V` | Pure robust `B0` | Pure robust accepted share | Share of admissible grid | Pure robust min `J` |
|---|---:|---:|---:|---:|
| `(0,0)` | in, `J0=0.695` | 0.114 | 0.136 | 0.265 |
| `(0.2,0.2)` | in, `J0=3.233` | 0.274 | 0.325 | 1.726 |
| `(0.5,0.5)` | in, `J0=6.783` | 0.459 | 0.545 | 4.395 |

The high-noise pure robust set is much wider than the superseded
diagonal-anchor row. This is the honest cost of dropping invalid second-order
information in this design.
