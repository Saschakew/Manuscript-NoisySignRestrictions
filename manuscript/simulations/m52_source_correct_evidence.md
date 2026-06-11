# M52 Source-Correct Variance-Ratio Robust DW Evidence

Status: completed M52 source-correct rebuild for the variance-ratio robust DW proposal.

The standard-DW set in this pass is the source-correct bivariate DW GMM1 higher-moment menu, `112`, `122`, `1112`, `1122`, and `1222`, intersected with a separate no-noise covariance screen in the common diagonal-normalized B-plane chart.

The robust set is the pure five-moment higher-cumulant J inversion with full central-moment delta weighting for generated fourth cumulants, intersected with the relative covariance-decomposition screen. The screen is applied in every grid and every truth-inclusion calculation.

## Configuration

- Base seed: `20260607`.
- Fixed-grid diagnostic grid: `61 x 61` plus the true point.
- Monte Carlo calibration replications per scenario: `60`.
- Monte Carlo evaluation replications per scenario: `24`.
- Monte Carlo grid: `41 x 41` plus the true point.
- Standard-DW primary cutoff: `9.236` for source-correct `GMM1` higher moments, plus a separate covariance-screen cutoff `2.706`.
- Robust cutoff under the primary chi-square convention: `9.236` with five generated higher-cumulant moments.

## Fixed-Grid Diagnostics

| Group | Scenario | S truth | R truth | R feasible | S share | R share | d_S_not_subset_R |
|---|---|---:|---:|---:|---:|---:|---:|
| figure1_noise | V=(0,0) | yes | yes | yes | 0.027 | 0.045 | 0.182 |
| figure1_noise | V=(0.2,0.2) | yes | yes | yes | 0.026 | 0.055 | 0.143 |
| figure1_noise | V=(0.5,0.5) | no | yes | yes | 0.026 | 0.051 | 0.524 |
| figure2_nongaussianity | w=1 | yes | yes | yes | 0.035 | 0.061 | 0.188 |
| figure2_nongaussianity | w=0.25 | yes | yes | yes | 0.105 | 0.116 | 0.524 |
| figure2_nongaussianity | w=0 | yes | yes | yes | 0.118 | 0.188 | 0.154 |
| figure3_sample_size | T=500 | yes | yes | yes | 0.026 | 0.055 | 0.143 |
| figure3_sample_size | T=1000 | no | yes | yes | 0.018 | 0.047 | 0.053 |
| figure3_sample_size | T=2000 | no | yes | yes | 0.008 | 0.017 | 0.269 |

## Monte Carlo Summary

| Scenario | Cutoff | S truth | R truth | R feasible | S share | R share | Empty S | Empty R | Jaccard | d_S_not_subset_R | Warning |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| No noise, strong moments | chi-square | 0.792 | 0.875 | 0.958 | 0.017 | 0.027 | 0.083 | 0.042 | 0.429 | 0.204 | 0.375 |
| No noise, strong moments | no-noise repeated | 0.875 | 0.875 | 0.958 | 0.023 | 0.029 | 0.083 | 0.042 | 0.441 | 0.274 | 0.500 |
| No noise, strong moments | scenario truth | 0.875 | 0.875 | 0.958 | 0.023 | 0.029 | 0.083 | 0.042 | 0.441 | 0.274 | 0.500 |
| Moderate Gaussian noise | chi-square | 0.417 | 0.875 | 1.000 | 0.027 | 0.057 | 0.042 | 0.042 | 0.345 | 0.174 | 0.583 |
| Moderate Gaussian noise | no-noise repeated | 0.500 | 0.875 | 1.000 | 0.037 | 0.061 | 0.042 | 0.042 | 0.371 | 0.249 | 0.708 |
| Moderate Gaussian noise | scenario truth | 0.625 | 0.875 | 1.000 | 0.053 | 0.062 | 0.000 | 0.000 | 0.353 | 0.416 | 0.875 |
| High Gaussian noise | chi-square | 0.000 | 0.833 | 0.958 | 0.029 | 0.062 | 0.167 | 0.042 | 0.321 | 0.161 | 0.875 |
| High Gaussian noise | no-noise repeated | 0.042 | 0.875 | 0.958 | 0.044 | 0.066 | 0.042 | 0.042 | 0.351 | 0.336 | 0.875 |
| High Gaussian noise | scenario truth | 0.042 | 0.917 | 0.958 | 0.125 | 0.105 | 0.000 | 0.000 | 0.322 | 0.548 | 1.000 |
| Weak structural higher moments | chi-square | 0.667 | 0.833 | 0.958 | 0.101 | 0.157 | 0.042 | 0.000 | 0.439 | 0.202 | 0.333 |
| Weak structural higher moments | no-noise repeated | 0.667 | 0.833 | 0.958 | 0.110 | 0.161 | 0.000 | 0.000 | 0.457 | 0.230 | 0.375 |
| Weak structural higher moments | scenario truth | 0.708 | 0.833 | 0.958 | 0.117 | 0.161 | 0.000 | 0.000 | 0.442 | 0.263 | 0.417 |
| Gaussian structural shocks | chi-square | 0.458 | 0.875 | 1.000 | 0.112 | 0.173 | 0.000 | 0.000 | 0.481 | 0.175 | 0.625 |
| Gaussian structural shocks | no-noise repeated | 0.458 | 0.875 | 1.000 | 0.118 | 0.176 | 0.000 | 0.000 | 0.494 | 0.180 | 0.583 |
| Gaussian structural shocks | scenario truth | 0.500 | 0.958 | 1.000 | 0.120 | 0.189 | 0.000 | 0.000 | 0.505 | 0.139 | 0.458 |
| Skewed residual noise | chi-square | 0.458 | 0.875 | 1.000 | 0.020 | 0.043 | 0.083 | 0.000 | 0.321 | 0.214 | 0.542 |
| Skewed residual noise | no-noise repeated | 0.500 | 0.875 | 1.000 | 0.028 | 0.046 | 0.000 | 0.000 | 0.368 | 0.287 | 0.833 |
| Skewed residual noise | scenario truth | 0.708 | 0.875 | 1.000 | 0.043 | 0.046 | 0.000 | 0.000 | 0.322 | 0.499 | 1.000 |

## Reading

- Under the primary chi-square convention, high Gaussian noise keeps the standard-DW truth-in rate at 0.000 and the variance-ratio robust truth-in rate at 0.833.
- The high-noise robust truth-feasible rate is 0.958. This records the finite-sample cost of the hard covariance-decomposition screen separately from the higher-cumulant J cutoff.
- With scenario-truth calibration, the high-noise standard-DW accepted share rises to 0.125. That is a calibration-cost diagnostic, not an application-ready correction.
- Weak and Gaussian structural-shock scenarios remain limitation cases. Under the primary chi-square convention, robust accepted shares are 0.157 and 0.173, respectively.
- The skewed-residual-noise row violates the maintained Gaussian-noise route, so it remains a stress case even when finite-sample truth inclusion is high.

Machine-readable output: `manuscript/simulations/output/m52_source_correct_evidence.json`.
