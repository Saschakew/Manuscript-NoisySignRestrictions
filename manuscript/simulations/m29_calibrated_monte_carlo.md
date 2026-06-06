# M29 Calibrated Monte Carlo Expanded Pass

Status: expanded calibrated finite-sample evidence pass for M29, not the final replication table.

This pass keeps the M0020/M28 normalized B-plane and reports the M27 metric bundle under repeated-sample and bootstrap critical-value conventions.

## Configuration

- Calibration replications per scenario: `80`
- Evaluation replications per scenario: `24`
- Bootstrap replications per evaluation sample: `40`
- Sample size: `500`
- Evaluation grid: `41 x 41` plus the true `B0` point.
- True normalized B0: `b12=-0.45`, `b21=0.7`.

Critical-value conventions:

- `chi_square_90`: the pointwise 90 percent chi-square guide used in the M0020 figures.
- `no_noise_repeated_90`: repeated-sample true-`B0` calibration in the no-noise strong-moment DGP, then applied to every scenario.
- `scenario_truth_repeated_90`: oracle repeated-sample true-`B0` calibration inside each scenario. This is diagnostic only because applications do not know the true `B0` or DGP.
- `truth_residual_bootstrap_90`: sample-specific residual-bootstrap true-`B0` calibration. This is also diagnostic only because true `B0` is known only in simulations.

## Repeated-Sample Scenario Cutoffs

| Scenario | Standard scenario cutoff | Robust scenario cutoff | Note |
|---|---:|---:|---|
| No noise, strong moments | 8.893 | 8.826 | Sanity case for standard-DW and robust-DW agreement. |
| Moderate Gaussian noise | 11.006 | 8.778 | The M0020 moderate-noise column with informative higher moments. |
| High Gaussian noise | 31.424 | 9.895 | The M0020 stress column where standard DW rejects true B0 under chi-square guides. |
| Weak structural higher moments | 9.423 | 8.036 | Companion-grid limitation case: robust DW should widen as higher moments weaken. |
| Gaussian structural shocks | 9.197 | 11.743 | All-null robust higher-cumulant population limit. |
| Skewed residual noise | 12.329 | 9.090 | Misspecified-noise stress case that violates the maintained Gaussian-noise route. |

## Monte Carlo Summary

| Scenario | Cutoff | S truth | R truth | S share | R share | Empty S | Empty R | Jaccard | d_S_not_subset_R | Warning |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| No noise, strong moments | chi-square | 0.917 | 0.958 | 0.027 | 0.096 | 0.042 | 0.042 | 0.258 | 0.097 | 0.125 |
| No noise, strong moments | no-noise repeated | 0.917 | 0.917 | 0.031 | 0.087 | 0.042 | 0.042 | 0.311 | 0.135 | 0.208 |
| No noise, strong moments | scenario truth | 0.917 | 0.917 | 0.031 | 0.087 | 0.042 | 0.042 | 0.311 | 0.135 | 0.208 |
| No noise, strong moments | truth bootstrap | 1.000 | 1.000 | 0.066 | 0.277 | 0.000 | 0.000 | 0.226 | 0.060 | 0.042 |
| Moderate Gaussian noise | chi-square | 0.917 | 0.958 | 0.051 | 0.298 | 0.000 | 0.042 | 0.155 | 0.076 | 0.167 |
| Moderate Gaussian noise | no-noise repeated | 0.958 | 0.958 | 0.059 | 0.272 | 0.000 | 0.042 | 0.188 | 0.097 | 0.125 |
| Moderate Gaussian noise | scenario truth | 0.958 | 0.958 | 0.074 | 0.269 | 0.000 | 0.042 | 0.227 | 0.122 | 0.125 |
| Moderate Gaussian noise | truth bootstrap | 1.000 | 1.000 | 0.120 | 0.588 | 0.000 | 0.000 | 0.195 | 0.021 | 0.000 |
| High Gaussian noise | chi-square | 0.292 | 0.917 | 0.136 | 0.842 | 0.042 | 0.042 | 0.153 | 0.055 | 0.708 |
| High Gaussian noise | no-noise repeated | 0.333 | 0.875 | 0.153 | 0.825 | 0.042 | 0.042 | 0.171 | 0.075 | 0.708 |
| High Gaussian noise | scenario truth | 0.958 | 0.917 | 0.328 | 0.863 | 0.000 | 0.000 | 0.324 | 0.114 | 0.167 |
| High Gaussian noise | truth bootstrap | 1.000 | 1.000 | 0.325 | 1.000 | 0.000 | 0.000 | 0.325 | 0.000 | 0.000 |
| Weak structural higher moments | chi-square | 0.792 | 0.917 | 0.167 | 0.923 | 0.000 | 0.000 | 0.163 | 0.068 | 0.208 |
| Weak structural higher moments | no-noise repeated | 0.917 | 0.917 | 0.183 | 0.912 | 0.000 | 0.000 | 0.176 | 0.086 | 0.125 |
| Weak structural higher moments | scenario truth | 0.958 | 0.917 | 0.190 | 0.893 | 0.000 | 0.000 | 0.183 | 0.099 | 0.167 |
| Weak structural higher moments | truth bootstrap | 1.000 | 1.000 | 0.234 | 1.000 | 0.000 | 0.000 | 0.234 | 0.000 | 0.000 |
| Gaussian structural shocks | chi-square | 0.875 | 0.917 | 0.169 | 0.903 | 0.000 | 0.000 | 0.181 | 0.054 | 0.208 |
| Gaussian structural shocks | no-noise repeated | 0.958 | 0.917 | 0.183 | 0.892 | 0.000 | 0.000 | 0.197 | 0.068 | 0.125 |
| Gaussian structural shocks | scenario truth | 0.958 | 0.958 | 0.187 | 0.949 | 0.000 | 0.000 | 0.197 | 0.014 | 0.042 |
| Gaussian structural shocks | truth bootstrap | 1.000 | 1.000 | 0.253 | 0.997 | 0.000 | 0.000 | 0.254 | 0.002 | 0.000 |
| Skewed residual noise | chi-square | 0.792 | 1.000 | 0.036 | 0.201 | 0.042 | 0.000 | 0.179 | 0.042 | 0.250 |
| Skewed residual noise | no-noise repeated | 0.875 | 1.000 | 0.042 | 0.184 | 0.000 | 0.000 | 0.226 | 0.059 | 0.167 |
| Skewed residual noise | scenario truth | 0.958 | 1.000 | 0.061 | 0.195 | 0.000 | 0.000 | 0.291 | 0.106 | 0.083 |
| Skewed residual noise | truth bootstrap | 1.000 | 1.000 | 0.099 | 0.441 | 0.000 | 0.000 | 0.216 | 0.050 | 0.000 |

## Expanded-Pass Outcome

- In the high Gaussian-noise stress case, standard DW includes true `B0` in only 0.292 of evaluation samples under the chi-square guide and 0.333 under the no-noise repeated calibration; robust DW includes true `B0` in 0.917 and 0.875, respectively.
- The high-noise oracle standard-DW cutoff is `31.424`, compared with `8.893` under no noise. That is the calibration cost of forcing the misspecified standard-DW statistic to cover the truth.
- The same high-noise oracle cutoff raises the standard-DW accepted share to 0.328, so the apparent precision is not free once the cutoff is truth-calibrated.
- Weak and Gaussian structural-shock cases keep robust DW wide under the no-noise repeated cutoff: mean robust shares are 0.912 and 0.892. This supports the limitation story rather than a sharp identification claim.
- The high-noise truth-residual bootstrap gives standard-DW truth inclusion 1.000 and robust-DW truth inclusion 1.000, with mean accepted shares 0.325 and 1.000; it is a calibration-cost audit, not an application-ready recipe.
- The skewed-residual-noise stress case has high robust truth inclusion in this pass, but the maintained Gaussian-noise interpretation is invalid there; it remains a stress case, not a robustness guarantee.

## Reading

- The no-noise repeated calibration is the cleanest first size check for the maintained no-noise benchmark. It should preserve the no-noise sanity case while still exposing residual-noise divergence.
- The high-noise Gaussian case is the main stress case from the visual spine. Under the figure-style and no-noise-calibrated cutoffs, standard DW should reject true `B0` more often than robust DW.
- The scenario-specific truth calibration is an oracle diagnostic. When its standard-DW cutoff is much larger than the no-noise cutoff, the standard DW statistic is paying a calibration cost under residual noise rather than delivering free precision.
- The truth-residual bootstrap is sample-specific and less parametric, but it still uses true `B0` and can make robust sets almost uninformative; treat it as an evidence audit rather than the final applied cutoff rule.
- The Gaussian-shock case is expected to make robust DW wide or weak because the higher-cumulant signal disappears.
- The skewed-residual-noise case is a maintained-assumption stress test. Robust DW is not expected to retain the clean Gaussian-noise interpretation there.

Machine-readable output: `manuscript/simulations/output/m29_calibrated_monte_carlo.json`.
