# Bounded-Noise Robust DW Noise Grid Variant

Status: M0035 comparison after the M0034 scale correction; superseded as
preferred candidate by the M0036 relative-noise screen.

This note records the Figure 1 variant that adds a bounded diagonal-noise
covariance screen to the pure higher-cumulant robust-DW row. The screen is not
the superseded `Sigma_u,12 = b12 + b21` anchor. It is a profiled
recovered-shock covariance condition with diagonal residual-noise variances
bounded by `0.5`.

Command:

```powershell
python manuscript\simulations\sign_dw_robust_noise_grid_figure.py --robust-mode bounded
```

Output:

- `manuscript/figures/fig_sign_dw_bounded_noise_robust_grid.png`

## Algebra

For a candidate

```text
B = [[1, a],
     [b, 1]]
```

with `d = 1 - ab`, recovered residuals are

```text
e(B) = B^{-1} u.
```

If the candidate is the true impact shape, structural shocks are mutually
uncorrelated, and residual noise is diagonal with

```text
V = diag(nu_1, nu_2),
```

then

```text
E[e_1 e_2] = (-b * nu_1 - a * nu_2) / d^2.
```

With `0 <= nu_i <= 0.5`, this becomes a candidate-specific interval:

```text
E[e_1 e_2] in [
  0.5 * (min(-b/d^2, 0) + min(-a/d^2, 0)),
  0.5 * (max(-b/d^2, 0) + max(-a/d^2, 0))
].
```

The plotted bounded row accepts a candidate when both conditions hold:

1. the pure five-moment higher-cumulant J statistic is below the pointwise
   `chi2_5(0.90)` cutoff;
2. the sample recovered covariance `mean(e_1 e_2)` falls in the bounded-noise
   interval above.

The lower bound is implemented as closed at zero for numerical plotting and to
include the no-noise column. A strict positivity assumption has the same
closure in this grid except at boundary cases.

## Fixed-Draw Diagnostics

Accepted shares are fractions of the full plotted grid. The admissible-grid
share divides only by nonsingular grid points with `b21 >= 0`.

| Noise `V` | Bounded robust `B0` | Bounded accepted share | Share of admissible grid | Bounded share within pure robust | `mean(e1 e2)` at `B0` | Bounded interval at `B0` |
|---|---:|---:|---:|---:|---:|---:|
| `(0,0)` | in, `J0=0.695` | 0.062 | 0.073 | 0.540 | 0.029 | `[-0.278, 0.087]` |
| `(0.2,0.2)` | in, `J0=3.233` | 0.074 | 0.088 | 0.271 | -0.069 | `[-0.278, 0.087]` |
| `(0.5,0.5)` | in, `J0=6.783` | 0.066 | 0.079 | 0.144 | -0.193 | `[-0.278, 0.087]` |

This candidate recovers much of the precision lost by the pure
higher-cumulant row while preserving the scale correction from M0034. It should
still be audited before replacing the manuscript's main evidence spine: the
noise-variance bound is substantive identifying information, and finite-sample
coverage for the inequality screen has not yet been calibrated.
