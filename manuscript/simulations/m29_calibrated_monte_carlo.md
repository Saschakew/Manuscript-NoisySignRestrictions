# M29 Calibrated Monte Carlo Larger Pass

Status: larger chi-square-primary finite-sample evidence pass for M29, not the final replication package.

This pass keeps the M0020/M28 normalized B-plane. The main applied benchmark uses the standard pointwise chi-square critical values a researcher would use under the maintained no-noise DW null; repeated-sample, oracle, and truth-bootstrap cutoffs are reported as calibration audits.

## Configuration

- Calibration replications per scenario: `240`
- Evaluation replications per scenario: `120`
- Bootstrap replications per evaluation sample: `40`
- Sample size: `500`
- Evaluation grid: `41 x 41` plus the true `B0` point.
- True normalized B0: `b12=-0.45`, `b21=0.7`.

Critical-value conventions:

- `chi_square_90`: primary applied benchmark; the pointwise 90 percent chi-square guide used by a researcher who applies standard DW without accounting for residual noise.
- `no_noise_repeated_90`: calibration audit; repeated-sample true-`B0` calibration in the no-noise strong-moment DGP, then applied to every scenario.
- `scenario_truth_repeated_90`: oracle calibration audit inside each scenario. This is diagnostic only because applications do not know the true `B0` or DGP.
- `truth_residual_bootstrap_90`: sample-specific truth-point residual-bootstrap audit. This is also diagnostic only because true `B0` is known only in simulations.

## Repeated-Sample Scenario Cutoffs

| Scenario | Standard scenario cutoff | Robust scenario cutoff | Note |
|---|---:|---:|---|
| No noise, strong moments | 8.367 | 9.599 | Sanity case for standard-DW and robust-DW agreement. |
| Moderate Gaussian noise | 10.729 | 9.783 | The M0020 moderate-noise column with informative higher moments. |
| High Gaussian noise | 23.274 | 9.852 | The M0020 stress column where standard DW rejects true B0 under chi-square guides. |
| Weak structural higher moments | 8.011 | 7.976 | Companion-grid limitation case: robust DW should widen as higher moments weaken. |
| Gaussian structural shocks | 7.514 | 9.313 | All-null robust higher-cumulant population limit. |
| Skewed residual noise | 14.575 | 10.697 | Misspecified-noise stress case that violates the maintained Gaussian-noise route. |

## Monte Carlo Summary

| Scenario | Cutoff | S truth | R truth | S share | R share | Empty S | Empty R | Jaccard | d_S_not_subset_R | Warning |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| No noise, strong moments | chi-square | 0.892 | 0.917 | 0.029 | 0.102 | 0.042 | 0.050 | 0.252 | 0.107 | 0.167 |
| No noise, strong moments | no-noise repeated | 0.900 | 0.925 | 0.032 | 0.111 | 0.033 | 0.042 | 0.253 | 0.110 | 0.150 |
| No noise, strong moments | scenario truth | 0.900 | 0.925 | 0.032 | 0.111 | 0.033 | 0.042 | 0.253 | 0.110 | 0.150 |
| No noise, strong moments | truth bootstrap | 1.000 | 1.000 | 0.075 | 0.300 | 0.000 | 0.000 | 0.244 | 0.056 | 0.042 |
| Moderate Gaussian noise | chi-square | 0.825 | 0.917 | 0.043 | 0.268 | 0.042 | 0.058 | 0.144 | 0.081 | 0.217 |
| Moderate Gaussian noise | no-noise repeated | 0.867 | 0.933 | 0.047 | 0.289 | 0.042 | 0.050 | 0.148 | 0.077 | 0.175 |
| Moderate Gaussian noise | scenario truth | 0.908 | 0.933 | 0.063 | 0.300 | 0.025 | 0.033 | 0.184 | 0.096 | 0.158 |
| Moderate Gaussian noise | truth bootstrap | 1.000 | 1.000 | 0.135 | 0.604 | 0.000 | 0.000 | 0.207 | 0.031 | 0.008 |
| High Gaussian noise | chi-square | 0.325 | 0.908 | 0.132 | 0.842 | 0.025 | 0.017 | 0.142 | 0.069 | 0.658 |
| High Gaussian noise | no-noise repeated | 0.383 | 0.917 | 0.142 | 0.860 | 0.008 | 0.008 | 0.149 | 0.079 | 0.608 |
| High Gaussian noise | scenario truth | 0.933 | 0.917 | 0.287 | 0.870 | 0.000 | 0.000 | 0.282 | 0.108 | 0.175 |
| High Gaussian noise | truth bootstrap | 1.000 | 1.000 | 0.318 | 0.992 | 0.000 | 0.000 | 0.319 | 0.004 | 0.008 |
| Weak structural higher moments | chi-square | 0.833 | 0.925 | 0.164 | 0.914 | 0.000 | 0.000 | 0.166 | 0.062 | 0.225 |
| Weak structural higher moments | no-noise repeated | 0.875 | 0.925 | 0.173 | 0.925 | 0.000 | 0.000 | 0.175 | 0.056 | 0.183 |
| Weak structural higher moments | scenario truth | 0.842 | 0.883 | 0.168 | 0.862 | 0.000 | 0.000 | 0.171 | 0.095 | 0.250 |
| Weak structural higher moments | truth bootstrap | 1.000 | 1.000 | 0.246 | 0.997 | 0.000 | 0.000 | 0.246 | 0.001 | 0.000 |
| Gaussian structural shocks | chi-square | 0.867 | 0.933 | 0.165 | 0.913 | 0.000 | 0.000 | 0.171 | 0.053 | 0.183 |
| Gaussian structural shocks | no-noise repeated | 0.908 | 0.942 | 0.174 | 0.923 | 0.000 | 0.000 | 0.178 | 0.048 | 0.133 |
| Gaussian structural shocks | scenario truth | 0.858 | 0.933 | 0.161 | 0.915 | 0.000 | 0.000 | 0.167 | 0.051 | 0.192 |
| Gaussian structural shocks | truth bootstrap | 1.000 | 1.000 | 0.247 | 0.998 | 0.000 | 0.000 | 0.247 | 0.001 | 0.000 |
| Skewed residual noise | chi-square | 0.717 | 0.917 | 0.036 | 0.192 | 0.025 | 0.008 | 0.171 | 0.079 | 0.292 |
| Skewed residual noise | no-noise repeated | 0.767 | 0.925 | 0.039 | 0.208 | 0.017 | 0.008 | 0.173 | 0.075 | 0.242 |
| Skewed residual noise | scenario truth | 0.967 | 0.950 | 0.072 | 0.263 | 0.000 | 0.008 | 0.244 | 0.098 | 0.133 |
| Skewed residual noise | truth bootstrap | 1.000 | 1.000 | 0.103 | 0.475 | 0.000 | 0.000 | 0.205 | 0.044 | 0.033 |

## Expanded-Pass Outcome

- Under the primary chi-square benchmark, the high Gaussian-noise stress case has standard DW including true `B0` in only 0.325 of evaluation samples under the researcher-facing cutoff, while robust DW includes true `B0` in 0.908.
- The no-noise repeated audit gives the same reading: high-noise standard DW includes true `B0` in 0.383, while robust DW includes it in 0.917.
- The high-noise oracle standard-DW cutoff is `23.274`, compared with `8.367` under no noise. That is the calibration cost of forcing the misspecified standard-DW statistic to cover the truth.
- The same high-noise oracle cutoff raises the standard-DW accepted share to 0.287, so the apparent precision is not free once the cutoff is truth-calibrated.
- Weak and Gaussian structural-shock cases keep robust DW wide under the primary chi-square benchmark: mean robust shares are 0.914 and 0.913. This supports the limitation story rather than a sharp identification claim.
- The high-noise truth-residual bootstrap gives standard-DW truth inclusion 1.000 and robust-DW truth inclusion 1.000, with mean accepted shares 0.318 and 0.992; it is a calibration-cost audit, not an application-ready recipe.
- The skewed-residual-noise stress case has high robust truth inclusion in this pass, but the maintained Gaussian-noise interpretation is invalid there; it remains a stress case, not a robustness guarantee.

## Reading

- The chi-square rows are the main applied comparison because they match the critical values a standard-DW user would use when unaware of residual noise.
- The high-noise Gaussian case is the main stress case from the visual spine. Under the researcher-facing chi-square cutoffs, standard DW rejects true `B0` much more often than robust DW.
- The no-noise repeated calibration is a size-check audit for the maintained no-noise benchmark. It should preserve the no-noise sanity case while still exposing residual-noise divergence.
- The scenario-specific truth calibration is an oracle diagnostic. When its standard-DW cutoff is much larger than the no-noise cutoff, the standard DW statistic is paying a calibration cost under residual noise rather than delivering free precision.
- The truth-residual bootstrap is sample-specific and less parametric, but it still uses true `B0` and can make robust sets almost uninformative; treat it as an evidence audit rather than the final applied cutoff rule.
- The Gaussian-shock case is expected to make robust DW wide or weak because the higher-cumulant signal disappears.
- The skewed-residual-noise case is a maintained-assumption stress test. Robust DW is not expected to retain the clean Gaussian-noise interpretation there.

Machine-readable output: `manuscript/simulations/output/m29_calibrated_monte_carlo.json`.
