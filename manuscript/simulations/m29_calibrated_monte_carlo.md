# M29 Calibrated Monte Carlo Larger Pass

Status: larger chi-square-primary finite-sample evidence pass for M29, not the final replication package.

This pass keeps the M0030 revised normalized B-plane. The main applied benchmark uses the standard pointwise chi-square critical values a researcher would use under the maintained no-noise DW null; repeated-sample, oracle, and truth-bootstrap cutoffs are reported as calibration audits.

## Configuration

- Calibration replications per scenario: `120`
- Evaluation replications per scenario: `60`
- Bootstrap replications per evaluation sample: `20`
- Sample size: `500`
- Evaluation grid: `41 x 41` plus the true `B0` point.
- True normalized B0: `b12=-0.25`, `b21=0.8`.

Critical-value conventions:

- `chi_square_90`: primary applied benchmark; the pointwise 90 percent chi-square guide used by a researcher who applies standard DW without accounting for residual noise.
- `no_noise_repeated_90`: calibration audit; repeated-sample true-`B0` calibration in the no-noise strong-moment DGP, then applied to every scenario.
- `scenario_truth_repeated_90`: oracle calibration audit inside each scenario. This is diagnostic only because applications do not know the true `B0` or DGP.
- `truth_residual_bootstrap_90`: sample-specific truth-point residual-bootstrap audit. This is also diagnostic only because true `B0` is known only in simulations.

## Repeated-Sample Scenario Cutoffs

| Scenario | Standard scenario cutoff | Robust scenario cutoff | Note |
|---|---:|---:|---|
| No noise, strong moments | 7.604 | 9.799 | Sanity case for standard-DW and robust-DW agreement. |
| Moderate Gaussian noise | 15.697 | 9.698 | The M0030 moderate-noise column with informative higher moments. |
| High Gaussian noise | 35.423 | 10.507 | The M0030 lower high-noise stress column where standard DW rejects true B0 under chi-square guides. |
| Weak structural higher moments | 11.987 | 8.641 | Companion-grid limitation case: robust DW should widen toward the covariance-anchor band as higher moments weaken. |
| Gaussian structural shocks | 13.534 | 12.193 | Higher-cumulant all-null limit; diagonal-noise covariance anchor remains. |
| Skewed residual noise | 17.557 | 11.378 | Misspecified-noise stress case that violates the maintained Gaussian-noise route. |

## Monte Carlo Summary

| Scenario | Cutoff | S truth | R truth | S share | R share | Empty S | Empty R | Jaccard | d_S_not_subset_R | Warning |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| No noise, strong moments | chi-square | 0.883 | 0.900 | 0.024 | 0.040 | 0.033 | 0.017 | 0.420 | 0.166 | 0.283 |
| No noise, strong moments | no-noise repeated | 0.883 | 0.867 | 0.023 | 0.035 | 0.033 | 0.033 | 0.436 | 0.192 | 0.333 |
| No noise, strong moments | scenario truth | 0.883 | 0.867 | 0.023 | 0.035 | 0.033 | 0.033 | 0.436 | 0.192 | 0.333 |
| No noise, strong moments | truth bootstrap | 1.000 | 1.000 | 0.063 | 0.099 | 0.000 | 0.000 | 0.479 | 0.114 | 0.167 |
| Moderate Gaussian noise | chi-square | 0.583 | 0.933 | 0.032 | 0.072 | 0.017 | 0.017 | 0.371 | 0.103 | 0.433 |
| Moderate Gaussian noise | no-noise repeated | 0.550 | 0.850 | 0.031 | 0.063 | 0.017 | 0.050 | 0.381 | 0.144 | 0.450 |
| Moderate Gaussian noise | scenario truth | 0.933 | 0.850 | 0.074 | 0.062 | 0.000 | 0.050 | 0.508 | 0.372 | 0.783 |
| Moderate Gaussian noise | truth bootstrap | 1.000 | 1.000 | 0.122 | 0.191 | 0.000 | 0.000 | 0.497 | 0.087 | 0.100 |
| High Gaussian noise | chi-square | 0.050 | 0.900 | 0.040 | 0.117 | 0.100 | 0.033 | 0.214 | 0.242 | 0.850 |
| High Gaussian noise | no-noise repeated | 0.050 | 0.833 | 0.038 | 0.102 | 0.117 | 0.067 | 0.218 | 0.286 | 0.833 |
| High Gaussian noise | scenario truth | 0.917 | 0.867 | 0.271 | 0.115 | 0.000 | 0.033 | 0.280 | 0.691 | 1.000 |
| High Gaussian noise | truth bootstrap | 1.000 | 1.000 | 0.288 | 0.269 | 0.000 | 0.000 | 0.497 | 0.338 | 0.750 |
| Weak structural higher moments | chi-square | 0.617 | 0.933 | 0.153 | 0.172 | 0.000 | 0.000 | 0.415 | 0.379 | 0.767 |
| Weak structural higher moments | no-noise repeated | 0.600 | 0.883 | 0.150 | 0.159 | 0.000 | 0.000 | 0.399 | 0.416 | 0.817 |
| Weak structural higher moments | scenario truth | 0.867 | 0.833 | 0.203 | 0.139 | 0.000 | 0.033 | 0.384 | 0.534 | 0.983 |
| Weak structural higher moments | truth bootstrap | 1.000 | 1.000 | 0.257 | 0.256 | 0.000 | 0.000 | 0.545 | 0.276 | 0.583 |
| Gaussian structural shocks | chi-square | 0.667 | 0.967 | 0.153 | 0.158 | 0.000 | 0.000 | 0.409 | 0.405 | 0.917 |
| Gaussian structural shocks | no-noise repeated | 0.650 | 0.950 | 0.150 | 0.144 | 0.000 | 0.000 | 0.387 | 0.450 | 0.967 |
| Gaussian structural shocks | scenario truth | 0.967 | 0.967 | 0.218 | 0.182 | 0.000 | 0.000 | 0.478 | 0.408 | 0.967 |
| Gaussian structural shocks | truth bootstrap | 1.000 | 1.000 | 0.256 | 0.255 | 0.000 | 0.000 | 0.559 | 0.271 | 0.500 |
| Skewed residual noise | chi-square | 0.600 | 0.950 | 0.029 | 0.069 | 0.083 | 0.000 | 0.355 | 0.085 | 0.383 |
| Skewed residual noise | no-noise repeated | 0.567 | 0.900 | 0.028 | 0.061 | 0.083 | 0.000 | 0.368 | 0.117 | 0.417 |
| Skewed residual noise | scenario truth | 0.933 | 0.950 | 0.075 | 0.077 | 0.000 | 0.000 | 0.572 | 0.252 | 0.400 |
| Skewed residual noise | truth bootstrap | 1.000 | 1.000 | 0.093 | 0.164 | 0.000 | 0.000 | 0.492 | 0.060 | 0.050 |

## Expanded-Pass Outcome

- Under the primary chi-square benchmark, the high Gaussian-noise stress case has standard DW including true `B0` in only 0.050 of evaluation samples under the researcher-facing cutoff, while robust DW includes true `B0` in 0.900.
- The no-noise repeated audit gives the same reading: high-noise standard DW includes true `B0` in 0.050, while robust DW includes it in 0.833.
- The high-noise oracle standard-DW cutoff is `35.423`, compared with `7.604` under no noise. That is the calibration cost of forcing the misspecified standard-DW statistic to cover the truth.
- The same high-noise oracle cutoff raises the standard-DW accepted share to 0.271, so the apparent precision is not free once the cutoff is truth-calibrated.
- Weak and Gaussian structural-shock cases show the robust set falling back toward its diagonal-noise covariance anchor under the primary chi-square benchmark: mean robust shares are 0.172 and 0.158. This supports the limitation story rather than a sharp identification claim.
- The high-noise truth-residual bootstrap gives standard-DW truth inclusion 1.000 and robust-DW truth inclusion 1.000, with mean accepted shares 0.288 and 0.269; it is a calibration-cost audit, not an application-ready recipe.
- The skewed-residual-noise stress case has high robust truth inclusion in this pass, but the maintained Gaussian-noise interpretation is invalid there; it remains a stress case, not a robustness guarantee.

## Reading

- The chi-square rows are the main applied comparison because they match the critical values a standard-DW user would use when unaware of residual noise.
- The high-noise Gaussian case is the main stress case from the visual spine. Under the researcher-facing chi-square cutoffs, standard DW rejects true `B0` much more often than robust DW.
- The no-noise repeated calibration is a size-check audit for the maintained no-noise benchmark. It should preserve the no-noise sanity case while still exposing residual-noise divergence.
- The scenario-specific truth calibration is an oracle diagnostic. When its standard-DW cutoff is much larger than the no-noise cutoff, the standard DW statistic is paying a calibration cost under residual noise rather than delivering free precision.
- The truth-residual bootstrap is sample-specific and less parametric, but it still uses true `B0` and can make robust sets almost uninformative; treat it as an evidence audit rather than the final applied cutoff rule.
- The Gaussian-shock case is expected to make the higher-cumulant substack uninformative; under the M0030 robust statistic the off-diagonal covariance anchor can still restrict the chart.
- The skewed-residual-noise case is a maintained-assumption stress test. Robust DW is not expected to retain the clean Gaussian-noise interpretation there.

Machine-readable output: `manuscript/simulations/output/m29_calibrated_monte_carlo.json`.
