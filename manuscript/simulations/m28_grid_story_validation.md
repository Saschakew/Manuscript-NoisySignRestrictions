# M28 Grid Story Validation

Status: completed validation pass for the selected M0030 revised grid pair.

This note validates the figure story without changing the figure generators. It combines exact population moment diagnostics with repeated fixed-design finite-sample J-test checks on the same B-plane.

## Configuration

- Population grid: `101 x 101` plus the true `B0` point.
- Finite grid: `51 x 51` plus the true `B0` point.
- Finite seeds: `20260605, 20260606, 20260607, 20260608, 20260609, 20260610`.
- Population near-zero tolerance: `0.005`.
- Remote-alias radius: `0.2` in `(b12,b21)` distance.

## Population Truth And Alias Diagnostics

| Scenario | Standard truth norm | Robust truth norm | Standard remote near-zeros | Robust remote near-zeros | Verdict |
|---|---:|---:|---:|---:|---|
| noise_grid / V=(0,0) | 4.165e-17 | 7.793e-17 | 0 | 0 | truth compatible |
| noise_grid / V=(0.2,0.2) | 0.065 | 7.793e-17 | 0 | 0 | supports divergence |
| noise_grid / V=(0.5,0.5) | 0.135 | 7.793e-17 | 0 | 0 | supports divergence |
| nongaussianity_grid / w=1 | 0.065 | 7.793e-17 | 0 | 0 | supports divergence |
| nongaussianity_grid / w=0.25 | 0.065 | 6.261e-18 | 0 | 0 | supports divergence |
| nongaussianity_grid / w=0 | 0.065 | 0.000 | 55 | 30 | covariance-anchor limit |

Population reading: robust-DW is exactly zero at the true normalized `B0` under Gaussian residual noise whenever structural higher moments are present, while the standard DW population moments become nonzero when the noisy covariance target moves away from the no-noise impact matrix. With Gaussian structural shocks, the robust higher-cumulant substack is all-null by design, but the off-diagonal covariance anchor remains informative under diagonal noise.

## Boundary Sensitivity

| Scenario | Window | Standard min distance | Robust min distance | Standard remote near-zeros | Robust remote near-zeros |
|---|---|---:|---:|---:|---:|
| noise_grid / V=(0.5,0.5) | base | 0.090 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0.25 | base | 0.053 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0 | base | 0.599 | 0.000 | 55 | 30 |
| noise_grid / V=(0.5,0.5) | expanded | 0.081 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0.25 | expanded | 0.078 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0 | expanded | 1.593 | 0.000 | 49 | 21 |
| noise_grid / V=(0.5,0.5) | narrow | 0.086 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0.25 | narrow | 0.057 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0 | narrow | 0.474 | 0.354 | 51 | 27 |

Boundary reading: the high-noise standard-DW population minimum is not at the true `B0`; robust-DW keeps the true point as an exact population zero. The Gaussian-shock column correctly has remote robust near-zeros because there is no higher-moment information to identify the impact shape.

## Repeated Finite-Sample J Checks

| Scenario | Method | Truth-in rate at 10% | Mean accepted share | Median `J(B0)` | Max `J(B0)` |
|---|---|---:|---:|---:|---:|
| nongaussianity_grid / w=0 | standard_dw | 0.667 | 0.136 | 4.577 | 15.007 |
| nongaussianity_grid / w=0 | robust_dw | 0.833 | 0.148 | 3.072 | 13.067 |
| noise_grid / V=(0.5,0.5) | standard_dw | 0.000 | 0.031 | 23.432 | 34.859 |
| noise_grid / V=(0.5,0.5) | robust_dw | 0.833 | 0.124 | 4.022 | 11.039 |
| noise_grid / V=(0.2,0.2) | standard_dw | 0.333 | 0.024 | 9.335 | 28.221 |
| noise_grid / V=(0.2,0.2) | robust_dw | 0.833 | 0.068 | 3.180 | 16.197 |
| noise_grid / V=(0,0) | standard_dw | 0.833 | 0.019 | 2.799 | 27.815 |
| noise_grid / V=(0,0) | robust_dw | 0.500 | 0.027 | 9.030 | 17.207 |
| nongaussianity_grid / w=1 | standard_dw | 0.333 | 0.024 | 9.335 | 28.221 |
| nongaussianity_grid / w=1 | robust_dw | 0.833 | 0.068 | 3.180 | 16.197 |
| nongaussianity_grid / w=0.25 | standard_dw | 0.667 | 0.124 | 6.657 | 17.766 |
| nongaussianity_grid / w=0.25 | robust_dw | 0.833 | 0.143 | 3.330 | 16.725 |

## Critical-Value Sensitivity

| Scenario | Method | 20% truth-in | 10% truth-in | 5% truth-in | 20% mean share | 10% mean share | 5% mean share |
|---|---|---:|---:|---:|---:|---:|---:|
| nongaussianity_grid / w=0 | robust_dw | 0.833 | 0.833 | 0.833 | 0.123 | 0.148 | 0.171 |
| noise_grid / V=(0.5,0.5) | standard_dw | 0.000 | 0.000 | 0.000 | 0.019 | 0.031 | 0.044 |
| noise_grid / V=(0.5,0.5) | robust_dw | 0.833 | 0.833 | 1.000 | 0.089 | 0.124 | 0.155 |
| nongaussianity_grid / w=0.25 | robust_dw | 0.833 | 0.833 | 0.833 | 0.121 | 0.143 | 0.163 |

## Gate Outcome

- The population diagnostics support the core visual story: residual noise moves the standard covariance/DW target, and robust-DW keeps the true normalized impact as a population zero under the maintained Gaussian-noise condition.
- The high-noise finite-sample stress case is stable enough for the selected visual spine: standard DW rejects the true point across repeated seeds at the pointwise 10 percent cutoff, while robust DW usually contains it.
- The non-Gaussianity companion behaves as intended: weakening higher moments widens the robust accepted region, and the Gaussian-shock case is a covariance-anchor limit rather than higher-moment identifying evidence.
- This is not yet final evidence. M29 still needs calibrated repeated-sample or bootstrap critical values before the manuscript reports coverage or size claims.

Machine-readable output: `manuscript/simulations/output/m28_grid_story_validation.json`.
