# M77 Clean IID MC Efficient Weight

Status: generated truth-at-B0 pointwise size diagnostic for the cleaned iid sample-size design.

The run removes the M74 sample-standardization and demeaning steps. Structural shocks are drawn as population-normalized iid chi-square variables, residual noise is iid Gaussian, residuals are not demeaned, and recovered shocks are not sample-centered. The pointwise weights are analytic iid efficient GMM weights, \(W=(E[f_t f_t'])^{-1}\), computed by polynomial expansion from the assumed univariate moments.

This output reports truth-at-\(B_0\) pointwise inclusion only. It does not report accepted projection shares or empty-set rates.

## Configuration

- Machine-readable output: `manuscript/simulations/output/m77_clean_iid_mc_efficient_weight.json`.
- Replications per scenario: `500`.
- Structural shock: `(chi2_5 - 5) / sqrt(2*5)`.
- Residual noise: iid Gaussian.
- Weighting: analytic \(W=(E[f_t f_t'])^{-1}\), no auxiliary large-sample weight simulation.
- Diagnostic scope: truth-at-\(B_0\) pointwise size only.

## Analytic Weight Formula

Let \(q_t=(\varepsilon_{1t},\varepsilon_{2t},\zeta_{1t},\zeta_{2t})\), where the first two entries are independent population-normalized chi-square variables and the last two entries are independent standard normals. For each tested candidate, the script writes every moment row as a polynomial \(f_j(q_t)\). It computes

\[
\Omega_f=E[f(q_t)f(q_t)']-E[f(q_t)]E[f(q_t)]',
\qquad
W=\Omega_f^{-1}.
\]

The expectations are evaluated from exact univariate raw moments up to order eight. No auxiliary sample is used to estimate \(W\).

## Truth-Inclusion Table

| T | Sign truth | DW truth | nrDW truth | Warning | Sign J q90 | DW J q90 | nrDW J q90 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 500 | 0.124 (62/500) | 0.088 (44/500) | 0.884 (442/500) | 0.796 (398/500) | 27.426 | 32.705 | 14.280 |
| 1000 | 0.020 (10/500) | 0.010 (5/500) | 0.896 (448/500) | 0.886 (443/500) | 42.684 | 46.031 | 13.422 |
| 2000 | 0.000 (0/500) | 0.000 (0/500) | 0.900 (450/500) | 0.900 (450/500) | 70.438 | 73.491 | 13.257 |

## Weight Diagnostics

| Weight | Dimension | Min eigenvalue | Max eigenvalue | Condition number | Max absolute moment mean |
|---|---:|---:|---:|---:|---:|
| sign_second | 3 | 1 | 4.4 | 4.4 | 2.22e-16 |
| standard_dw_higher | 5 | 1.01705 | 132.668 | 130.444 | 4.44e-16 |
| robust_full_truth | 8 | 0.69838 | 180.395 | 258.305 | 8.88e-16 |

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| With iid per-period moments and \(E[f_t]=0\), \(W=(E[f_t f_t'])^{-1}\) is the pointwise efficient GMM weight. | `derived`, `user-decision` | GMM variance of the sample mean under iid moments; M77 task prompt. | high | promote as cleaned MC design |
| The cleaned MC is a simplification of the M74 weighting route. | `code-implemented`, `derived`, `user-decision` | This script removes sample-specific covariance weights and computes analytic population weights. | high | promote with DGP-change caveat |
| This output replaces M74 Table 2 set-size evidence. | `conjectural` | M77 is truth-at-B0 only and reports no accepted projection shares. | high | quarantine; supplement M74 unless full-grid cleaned MC is run |
