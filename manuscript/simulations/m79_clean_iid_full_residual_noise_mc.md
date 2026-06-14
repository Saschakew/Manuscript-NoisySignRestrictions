# M79 Clean IID Full Residual-Noise MC

Status: generated full-grid residual-noise Monte Carlo output for the cleaned iid analytic-weight design.

This run extends the M78 cleaned iid full-grid logic to the Figure 1 residual-noise scenarios. It fixes `T=500` and strong structural non-Gaussianity, varies residual noise across `V=(0,0)`, `V=(0.2,0.2)`, and `V=(0.5,0.5)`, and keeps the active Sign/DW/nrDW reporting surface.

## Configuration

- Machine-readable output: `manuscript/simulations/output/m79_clean_iid_full_residual_noise_mc.json`.
- Quick run: `False`.
- Replications per scenario: `500`.
- Projection grid: `27 x 27` plus exact true coordinates when needed.
- Profile grid: `7 x 7` plus exact true profiled coordinates when needed.
- Nominal lambda grid: `5 x 5` plus true lambda values for all residual-noise scenarios.
- Structural shocks: population-normalized iid chi-square.
- Residual noise: iid Gaussian.
- No sample standardization, no residual demeaning, no recovered-shock demeaning.
- Sign screen: `B11>0`, `B22>0`, `B12<=0`; `B21` is not sign-restricted.
- Sign weight: analytic no-noise three-moment weight.
- DW weight: analytic no-noise five-moment weight, after the sign screen.
- nrDW weight: candidate-specific analytic iid eight-moment weight.

## Residual-Noise Table

| V | Sign truth | DW truth | nrDW truth | Sign size | DW size | nrDW size | Sign empty | DW empty | nrDW empty | Warning |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| (0,0) | 0.924 (462/500) | 0.846 (423/500) | 0.888 (444/500) | 0.060 (0.060) | 0.023 (0.023) | 0.045 (0.046) | 0.000 (0/500) | 0.004 (2/500) | 0.010 (5/500) | 0.060 (30/500) |
| (0.2,0.2) | 0.140 (70/500) | 0.102 (51/500) | 0.880 (440/500) | 0.074 (0.074) | 0.028 (0.029) | 0.063 (0.065) | 0.000 (0/500) | 0.022 (11/500) | 0.008 (4/500) | 0.778 (389/500) |
| (0.5,0.5) | 0.000 (0/500) | 0.000 (0/500) | 0.886 (443/500) | 0.094 (0.094) | 0.037 (0.038) | 0.091 (0.093) | 0.000 (0/500) | 0.054 (27/500) | 0.006 (3/500) | 0.886 (443/500) |

## Truth-Statistic Quantiles

| V | True lambda | Sign J q90 | DW J q90 | nrDW J q90 | nrDW prefilter mean |
|---:|---:|---:|---:|---:|---:|
| (0,0) | (0.000, 0.000) | 5.591 | 9.523 | 13.843 | 4273.1 |
| (0.2,0.2) | (0.188, 0.122) | 26.834 | 34.807 | 14.115 | 4502.1 |
| (0.5,0.5) | (0.471, 0.305) | 109.725 | 159.078 | 13.732 | 4559.5 |

## Weight Diagnostics

| Weight | Detail | Value |
|---|---|---:|
| Sign | condition number | 4.4 |
| DW | condition number | 130.444 |
| nrDW cache | computed B candidates | 13210 |
| nrDW cache | computed candidate-lambda pairs | 647290 |
| nrDW cache | max absolute analytic moment mean | 2.13e-14 |
| nrDW cache | regularized matrices | 0 |

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| M79 uses the Figure 1 DGPs: `T=500`, strong structural non-Gaussianity, Gaussian residual noise, and `V=(0,0),(0.2,0.2),(0.5,0.5)`. | `code-implemented`, `user-decision` | Scenario configuration in this script and JSON. | high | promote as M79 design |
| The cleaned full MC uses population-normalized iid shocks/noise and no demeaning. | `code-implemented`, `user-decision` | This script and JSON configuration. | high | promote |
| The nrDW full-grid statistic uses candidate-specific analytic W(B,lambda). | `code-implemented`, `derived`, `user-decision` | M78 vectorized polynomial weight computation reused here. | high | promote as M79 design |
| The no-noise truth is evaluated with lambda zero on the lambda grid. | `code-implemented` | Lambda-grid checks in JSON configuration. | high | promote |
| Pointwise chi-square cutoffs are final projected confidence-set critical values. | `conjectural` | M65 remains open. | medium | quarantine |
