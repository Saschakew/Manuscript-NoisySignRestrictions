# M78 Clean IID Full Sample-Size MC

Status: generated full-grid sample-size Monte Carlo output for the cleaned iid analytic-weight design.

This run extends M77 from a truth-at-B0 pointwise audit to the full accepted-set table. It keeps the M74 sample-size scenarios and intermediate grid, but removes sample standardization, residual demeaning, recovered-shock demeaning, and sample-specific covariance weights.

## Configuration

- Machine-readable output: `manuscript/simulations/output/m78_clean_iid_full_sample_size_mc.json`.
- Quick run: `False`.
- Replications per scenario: `500`.
- Projection grid: `27 x 27` plus exact true coordinates when needed.
- Profile grid: `7 x 7` plus exact true profiled coordinates when needed.
- Lambda grid: `5 x 5` plus true lambda values.
- Structural shocks: population-normalized iid chi-square.
- Residual noise: iid Gaussian.
- No sample standardization, no residual demeaning, no recovered-shock demeaning.
- Sign screen: `B11>0`, `B22>0`, `B12<=0`; `B21` is not sign-restricted.
- Sign weight: analytic no-noise three-moment weight.
- DW weight: analytic no-noise five-moment weight, after the sign screen.
- nrDW weight: candidate-specific analytic iid eight-moment weight.

## Sample-Size Table

| T | Sign truth | DW truth | nrDW truth | Sign size | DW size | nrDW size | Sign empty | DW empty | nrDW empty | Warning |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 500 | 0.124 (62/500) | 0.088 (44/500) | 0.884 (442/500) | 0.074 (0.074) | 0.028 (0.029) | 0.063 (0.065) | 0.000 (0/500) | 0.026 (13/500) | 0.000 (0/500) | 0.796 (398/500) |
| 1000 | 0.020 (10/500) | 0.010 (5/500) | 0.896 (448/500) | 0.039 (0.040) | 0.011 (0.011) | 0.035 (0.037) | 0.000 (0/500) | 0.072 (36/500) | 0.008 (4/500) | 0.886 (443/500) |
| 2000 | 0.000 (0/500) | 0.000 (0/500) | 0.900 (450/500) | 0.017 (0.017) | 0.003 (0.003) | 0.021 (0.022) | 0.000 (0/500) | 0.204 (102/500) | 0.010 (5/500) | 0.900 (450/500) |

## Truth-Statistic Quantiles

| T | Sign J q90 | DW J q90 | nrDW J q90 | nrDW prefilter mean |
|---:|---:|---:|---:|---:|
| 500 | 27.426 | 32.705 | 14.280 | 4504.4 |
| 1000 | 42.684 | 46.031 | 13.422 | 4508.2 |
| 2000 | 70.438 | 73.491 | 13.257 | 4513.1 |

## Weight Diagnostics

| Weight | Detail | Value |
|---|---|---:|
| Sign | condition number | 4.4 |
| DW | condition number | 130.444 |
| nrDW cache | computed B candidates | 9817 |
| nrDW cache | computed candidate-lambda pairs | 353412 |
| nrDW cache | max absolute analytic moment mean | 1.42e-14 |
| nrDW cache | regularized matrices | 0 |

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| The cleaned full MC uses population-normalized iid shocks/noise and no demeaning. | `code-implemented`, `user-decision` | This script and JSON configuration. | high | promote |
| The nrDW full-grid statistic uses candidate-specific analytic W(B,lambda). | `code-implemented`, `derived`, `user-decision` | Vectorized polynomial weight computation in this script. | high | promote as M78 design |
| Sign and DW use analytic no-noise weights for their own moment stacks. | `code-implemented`, `derived` | M77 standard weight functions reused here. | high | promote |
| M78 replaces M77 as a full-grid table. | `conjectural` | M77 is pointwise only; M78 is full-grid, but M77 remains the clean size audit. | high | revise: M78 replaces M74 for full-grid cleaned design and complements M77 |
| Pointwise chi-square cutoffs are final projected confidence-set critical values. | `conjectural` | M65 remains open. | medium | quarantine |
