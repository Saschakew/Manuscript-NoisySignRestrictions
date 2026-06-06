# Relative-Noise Robust DW Noise Grid Variant

Status: M0036 candidate after the M0034 scale correction and M0035 absolute
bound screen.

This note records the Figure 1 variant that bounds diagonal residual-noise
variances relative to profiled structural-shock variances. The bottom row uses
the pure five-moment higher-cumulant J statistic and intersects it with a
covariance-decomposition feasibility screen.

Command:

```powershell
python manuscript\simulations\sign_dw_robust_noise_grid_figure.py --robust-mode relative
```

Output:

- `manuscript/figures/fig_sign_dw_relative_noise_robust_grid.png`

## Algebra

For a candidate

```text
B = [[1, a],
     [b, 1]]
```

let the structural shock covariance and diagonal residual-noise covariance be

```text
Var(epsilon) = diag(s_1, s_2),
Var(eta) = diag(nu_1, nu_2).
```

The relative-noise restriction is

```text
s_i > 0,
0 <= nu_i <= rho * s_i,
rho = 0.5.
```

For the sample residual covariance `S`, the covariance screen asks whether
there exist `s_1,s_2,nu_1,nu_2` such that

```text
S_11 = s_1 + a^2 s_2 + nu_1
S_12 = b s_1 + a s_2
S_22 = b^2 s_1 + s_2 + nu_2
```

and the relative-noise bounds hold. Equivalently, after profiling
`nu_i`,

```text
s_1 + a^2 s_2 <= S_11 <= (1 + rho) s_1 + a^2 s_2,
b^2 s_1 + s_2 <= S_22 <= b^2 s_1 + (1 + rho) s_2,
S_12 = b s_1 + a s_2.
```

The plotted row accepts a candidate if this linear feasibility problem is
solvable and the pure higher-cumulant J statistic is below the pointwise
`chi2_5(0.90)` cutoff.

## Fixed-Draw Diagnostics

Accepted shares are fractions of the full plotted grid. The admissible-grid
share divides only by nonsingular grid points with `b21 >= 0`.

| Noise `V` | Relative robust `B0` | Relative accepted share | Share of admissible grid | Relative share within pure robust | Pure accepted share | Absolute-bound share |
|---|---:|---:|---:|---:|---:|---:|
| `(0,0)` | in, `J0=0.695` | 0.053 | 0.063 | 0.461 | 0.114 | 0.062 |
| `(0.2,0.2)` | in, `J0=3.233` | 0.060 | 0.071 | 0.218 | 0.274 | 0.074 |
| `(0.5,0.5)` | in, `J0=6.783` | 0.071 | 0.084 | 0.155 | 0.459 | 0.066 |

The relative screen is scale-correct: it does not require unit structural
shock variances after normalizing `diag(B)=1`. In this calibration it looks
similar to the absolute `nu_i <= 0.5` screen because the simulated structural
shocks have variance close to one, but the interpretation is different. The
precision comes from a signal-to-noise restriction, not from an arbitrary
absolute variance unit.
