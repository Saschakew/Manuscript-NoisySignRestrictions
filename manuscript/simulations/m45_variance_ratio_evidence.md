# M45 Variance-Ratio Robust DW Evidence

Status: completed lightweight validation and Monte Carlo rebuild for the M0036 variance-ratio robust DW proposal.

The robust set in this pass is the pure five-moment higher-cumulant J inversion intersected with the relative covariance-decomposition screen. The screen is applied in every grid and every truth-inclusion calculation, so the numbers are no longer using the superseded diagonal-anchor statistic.

## Configuration

- Base seed: `20260607`.
- Fixed-grid diagnostic grid: `61 x 61` plus the true point.
- Monte Carlo calibration replications per scenario: `60`.
- Monte Carlo evaluation replications per scenario: `24`.
- Monte Carlo grid: `41 x 41` plus the true point.
- Robust cutoff under the primary chi-square convention: `9.236` with five higher-cumulant moments.

## Fixed-Grid Diagnostics

| Group | Scenario | S truth | R truth | R feasible | S share | R share | d_S_not_subset_R |
|---|---|---:|---:|---:|---:|---:|---:|
| figure1_noise | V=(0,0) | yes | yes | yes | 0.031 | 0.069 | 0.172 |
| figure1_noise | V=(0.2,0.2) | yes | yes | yes | 0.042 | 0.089 | 0.254 |
| figure1_noise | V=(0.5,0.5) | no | yes | yes | 0.047 | 0.107 | 0.276 |
| figure2_nongaussianity | w=1 | yes | yes | yes | 0.042 | 0.089 | 0.254 |
| figure2_nongaussianity | w=0.25 | yes | yes | yes | 0.108 | 0.196 | 0.233 |
| figure2_nongaussianity | w=0 | yes | yes | yes | 0.177 | 0.188 | 0.318 |
| figure3_sample_size | T=500 | yes | yes | yes | 0.042 | 0.089 | 0.254 |
| figure3_sample_size | T=1000 | no | yes | yes | 0.017 | 0.028 | 0.352 |
| figure3_sample_size | T=2000 | no | yes | yes | 0.014 | 0.042 | 0.182 |

## Monte Carlo Summary

| Scenario | Cutoff | S truth | R truth | R feasible | S share | R share | Empty S | Empty R | Jaccard | d_S_not_subset_R | Warning |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| No noise, strong moments | chi-square | 0.917 | 0.917 | 0.958 | 0.023 | 0.040 | 0.042 | 0.042 | 0.417 | 0.202 | 0.375 |
| No noise, strong moments | no-noise repeated | 0.917 | 0.875 | 0.958 | 0.027 | 0.038 | 0.042 | 0.042 | 0.478 | 0.221 | 0.417 |
| No noise, strong moments | scenario truth | 0.917 | 0.875 | 0.958 | 0.027 | 0.038 | 0.042 | 0.042 | 0.478 | 0.221 | 0.417 |
| Moderate Gaussian noise | chi-square | 0.708 | 0.958 | 1.000 | 0.037 | 0.081 | 0.000 | 0.042 | 0.359 | 0.142 | 0.417 |
| Moderate Gaussian noise | no-noise repeated | 0.792 | 0.958 | 1.000 | 0.044 | 0.078 | 0.000 | 0.042 | 0.410 | 0.173 | 0.375 |
| Moderate Gaussian noise | scenario truth | 0.958 | 0.917 | 1.000 | 0.074 | 0.077 | 0.000 | 0.042 | 0.506 | 0.293 | 0.583 |
| High Gaussian noise | chi-square | 0.000 | 0.875 | 0.958 | 0.036 | 0.097 | 0.083 | 0.042 | 0.329 | 0.069 | 0.875 |
| High Gaussian noise | no-noise repeated | 0.125 | 0.875 | 0.958 | 0.044 | 0.091 | 0.083 | 0.042 | 0.396 | 0.127 | 0.833 |
| High Gaussian noise | scenario truth | 0.958 | 0.917 | 0.958 | 0.286 | 0.128 | 0.000 | 0.042 | 0.425 | 0.572 | 1.000 |
| Weak structural higher moments | chi-square | 0.792 | 0.875 | 0.958 | 0.152 | 0.170 | 0.000 | 0.000 | 0.498 | 0.293 | 0.625 |
| Weak structural higher moments | no-noise repeated | 0.792 | 0.833 | 0.958 | 0.168 | 0.166 | 0.000 | 0.042 | 0.502 | 0.329 | 0.708 |
| Weak structural higher moments | scenario truth | 0.958 | 0.833 | 0.958 | 0.234 | 0.163 | 0.000 | 0.042 | 0.515 | 0.422 | 1.000 |
| Gaussian structural shocks | chi-square | 0.500 | 0.958 | 1.000 | 0.163 | 0.183 | 0.000 | 0.000 | 0.546 | 0.251 | 0.750 |
| Gaussian structural shocks | no-noise repeated | 0.583 | 0.958 | 1.000 | 0.177 | 0.181 | 0.000 | 0.000 | 0.553 | 0.282 | 0.833 |
| Gaussian structural shocks | scenario truth | 1.000 | 0.958 | 1.000 | 0.237 | 0.190 | 0.000 | 0.000 | 0.594 | 0.329 | 0.958 |
| Skewed residual noise | chi-square | 0.583 | 1.000 | 1.000 | 0.027 | 0.064 | 0.125 | 0.000 | 0.323 | 0.171 | 0.667 |
| Skewed residual noise | no-noise repeated | 0.625 | 1.000 | 1.000 | 0.032 | 0.061 | 0.125 | 0.000 | 0.367 | 0.205 | 0.625 |
| Skewed residual noise | scenario truth | 0.917 | 0.917 | 1.000 | 0.066 | 0.058 | 0.000 | 0.000 | 0.440 | 0.426 | 0.917 |

## Reading

- Under the primary chi-square convention, high Gaussian noise keeps the standard-DW truth-in rate at 0.000 and the variance-ratio robust truth-in rate at 0.875.
- The high-noise robust truth-feasible rate is 0.958. This records the finite-sample cost of the hard covariance-decomposition screen separately from the higher-cumulant J cutoff.
- With scenario-truth calibration, the high-noise standard-DW accepted share rises to 0.286. That is a calibration-cost diagnostic, not an application-ready correction.
- Weak and Gaussian structural-shock scenarios remain limitation cases. Under the primary chi-square convention, robust accepted shares are 0.170 and 0.183, respectively.
- The skewed-residual-noise row violates the maintained Gaussian-noise route, so it remains a stress case even when finite-sample truth inclusion is high.

Machine-readable output: `manuscript/simulations/output/m45_variance_ratio_evidence.json`.
