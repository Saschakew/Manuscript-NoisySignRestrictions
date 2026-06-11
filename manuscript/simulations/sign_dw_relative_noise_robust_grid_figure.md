# Relative-Noise Robust DW Noise Grid Variant

Status: M52 source-correct rebuild of the M0036/M40 variance-ratio proposal.

This note records the Figure 1 variant that bounds diagonal residual-noise
variances relative to profiled structural-shock variances. The middle row uses
the source-correct bivariate DW GMM1 higher-moment menu, intersected with the
separate no-noise covariance screen in the common B-plane chart. The bottom row
uses the pure five-moment higher-cumulant J statistic with central-moment delta
weighting and intersects it with a covariance-decomposition feasibility screen.

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

The plotted robust row accepts a candidate if this linear feasibility problem
is solvable and the generated higher-cumulant J statistic is below the
pointwise `chi2_5(0.90)` cutoff. The standard-DW row uses the source-correct
GMM1 higher products `112`, `122`, `1112`, `1122`, and `1222`, with the same
`chi2_5(0.90)` cutoff, and intersects that higher-moment screen with the
separate covariance screen using `chi2_1(0.90)`.

## Fixed-Draw Diagnostics

M52 fixed-grid diagnostics use a `61 x 61` grid plus the true point and match
the rendered Figure 1 draw.

| Noise `V` | Standard DW truth | Robust DW truth | Robust feasible | Standard share | Robust share | `d_S_not_subset_R` |
|---|---:|---:|---:|---:|---:|---:|
| `(0,0)` | yes | yes | yes | 0.027 | 0.045 | 0.182 |
| `(0.2,0.2)` | yes | yes | yes | 0.026 | 0.055 | 0.143 |
| `(0.5,0.5)` | no | yes | yes | 0.026 | 0.051 | 0.524 |

The relative screen is scale-correct: it does not require unit structural
shock variances after normalizing `diag(B)=1`. In this calibration it looks
similar to the absolute `nu_i <= 0.5` screen because the simulated structural
shocks have variance close to one, but the interpretation is different. The
precision comes from a signal-to-noise restriction, not from an arbitrary
absolute variance unit.

## M40 Audit Note

M40 conditionally passed the relative screen as a population
covariance-decomposition restriction. The audit confirmed that the implemented
linear feasibility problem matches the displayed equations and that the
`rho=0.5` bound is scale-correct relative to profiled structural-shock
variances. It must still be presented as substantive identifying information.

A small repeated-draw screen check at the true `B0` gave the following pass
rates over 250 draws:

| Sample size | `V=(0,0)` | `V=(0.2,0.2)` | `V=(0.5,0.5)` |
|---:|---:|---:|---:|
| `T=500` | 0.916 | 0.992 | 0.944 |
| `T=1000` | 0.988 | 1.000 | 0.972 |
| `T=2000` | 1.000 | 1.000 | 1.000 |

This is reassuring for the current calibration, but it is not a coverage
result. The M52 Monte Carlo evidence is recorded in
`manuscript/simulations/m52_source_correct_evidence.md`.
