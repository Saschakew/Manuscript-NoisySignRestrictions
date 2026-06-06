# M28 Grid Story Validation

Status: completed first M28 validation pass for the selected M0020 grid pair.

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
| noise_grid / V=(0,0) | 1.715e-17 | 2.886e-17 | 0 | 0 | truth compatible |
| noise_grid / V=(0.3,0.3) | 0.035 | 2.886e-17 | 0 | 0 | supports divergence |
| noise_grid / V=(2,2) | 0.116 | 2.886e-17 | 0 | 0 | supports divergence |
| nongaussianity_grid / w=1 | 0.035 | 2.886e-17 | 0 | 0 | supports divergence |
| nongaussianity_grid / w=0.25 | 0.035 | 2.318e-18 | 0 | 0 | supports divergence |
| nongaussianity_grid / w=0 | 0.035 | 0.000 | 63 | 8264 | robust all-null expected |

Population reading: robust-DW is exactly zero at the true normalized `B0` under Gaussian residual noise whenever structural higher moments are present, while the standard DW population moments become nonzero when the noisy covariance target moves away from the no-noise impact matrix. With Gaussian structural shocks, the robust higher-cumulant stack is all-null by design.

## Boundary Sensitivity

| Scenario | Window | Standard min distance | Robust min distance | Standard remote near-zeros | Robust remote near-zeros |
|---|---|---:|---:|---:|---:|
| noise_grid / V=(2,2) | base | 0.100 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0.25 | base | 0.050 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0 | base | 0.507 | 1.137 | 63 | 8264 |
| noise_grid / V=(2,2) | expanded | 0.107 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0.25 | expanded | 0.035 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0 | expanded | 1.120 | 1.564 | 62 | 7827 |
| noise_grid / V=(2,2) | narrow | 0.100 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0.25 | narrow | 0.036 | 0.000 | 0 | 0 |
| nongaussianity_grid / w=0 | narrow | 0.222 | 0.820 | 83 | 9071 |

Boundary reading: the high-noise standard-DW population minimum is not at the true `B0`; robust-DW keeps the true point as an exact population zero. The Gaussian-shock column correctly has remote robust near-zeros because there is no higher-moment information to identify the impact shape.

## Repeated Finite-Sample J Checks

| Scenario | Method | Truth-in rate at 10% | Mean accepted share | Median `J(B0)` | Max `J(B0)` |
|---|---|---:|---:|---:|---:|
| nongaussianity_grid / w=0 | standard_dw | 0.833 | 0.145 | 3.085 | 8.743 |
| nongaussianity_grid / w=0 | robust_dw | 0.833 | 0.759 | 1.643 | 11.317 |
| noise_grid / V=(2,2) | standard_dw | 0.000 | 0.103 | 18.793 | 26.962 |
| noise_grid / V=(2,2) | robust_dw | 0.833 | 0.751 | 5.068 | 13.208 |
| noise_grid / V=(0.3,0.3) | standard_dw | 0.833 | 0.033 | 4.643 | 18.557 |
| noise_grid / V=(0.3,0.3) | robust_dw | 0.833 | 0.251 | 3.521 | 10.467 |
| noise_grid / V=(0,0) | standard_dw | 0.833 | 0.023 | 2.799 | 27.815 |
| noise_grid / V=(0,0) | robust_dw | 0.500 | 0.073 | 7.900 | 14.317 |
| nongaussianity_grid / w=1 | standard_dw | 0.833 | 0.033 | 4.643 | 18.557 |
| nongaussianity_grid / w=1 | robust_dw | 0.833 | 0.251 | 3.521 | 10.467 |
| nongaussianity_grid / w=0.25 | standard_dw | 0.833 | 0.135 | 4.202 | 12.048 |
| nongaussianity_grid / w=0.25 | robust_dw | 0.833 | 0.707 | 2.786 | 15.444 |

## Critical-Value Sensitivity

| Scenario | Method | 20% truth-in | 10% truth-in | 5% truth-in | 20% mean share | 10% mean share | 5% mean share |
|---|---|---:|---:|---:|---:|---:|---:|
| nongaussianity_grid / w=0 | robust_dw | 0.667 | 0.833 | 0.833 | 0.701 | 0.759 | 0.774 |
| noise_grid / V=(2,2) | standard_dw | 0.000 | 0.000 | 0.000 | 0.075 | 0.103 | 0.124 |
| noise_grid / V=(2,2) | robust_dw | 0.833 | 0.833 | 0.833 | 0.653 | 0.751 | 0.779 |
| nongaussianity_grid / w=0.25 | robust_dw | 0.833 | 0.833 | 0.833 | 0.705 | 0.707 | 0.711 |

## Gate Outcome

- The population diagnostics support the core visual story: residual noise moves the standard covariance/DW target, and robust-DW keeps the true normalized impact as a population zero under the maintained Gaussian-noise condition.
- The high-noise finite-sample stress case is stable enough for the selected visual spine: standard DW rejects the true point across repeated seeds at the pointwise 10 percent cutoff, while robust DW usually contains it.
- The non-Gaussianity companion behaves as intended: weakening higher moments widens the robust accepted region, and the Gaussian-shock case is an all-null population limit rather than identifying evidence.
- This is not yet final evidence. M29 still needs calibrated repeated-sample or bootstrap critical values before the manuscript reports coverage or size claims.

Machine-readable output: `manuscript/simulations/output/m28_grid_story_validation.json`.
