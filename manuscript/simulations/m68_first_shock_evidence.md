# M71 First-Shock Monte Carlo Evidence

Status: generated Monte Carlo table for the corrected M71 first-shock impact chart.

The table uses the same sign screen as Figures 1-3: `B11>0`, `B22>0`, and `B12<=0`; `B21` is displayed but not sign-restricted. The displayed coordinates are `(B11,B21)`, while `B12`, `B22`, and `lambda` are profiled. The robust row evaluates the M66 moment vector at `nu_i=lambda_i(BB')_ii`.

The statistics use candidate-specific pointwise covariance estimates for each tested candidate. The cutoffs are pointwise chi-square diagnostics for the displayed moment rows. The final projected critical-value route remains an inference follow-up.

## Configuration

- Machine-readable output: `manuscript/simulations/output/m68_first_shock_evidence.json`.
- Replications per scenario: `6`.
- Projection grid: `13 x 13`.
- Profile grid: `5 x 5`.
- Lambda grid: `3 x 3`.

## Chi-Square Diagnostic Table

| Scenario | S truth | R truth | Warning | Sign share | S share | R share | d_S_not_subset_R | S dist | R dist |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| No noise, strong moments | 0.667 | 0.500 | 0.000 | 0.048 | 0.020 | 0.035 | 0.133 | 0.022 | 0.018 |
| Moderate Gaussian noise | 0.167 | 0.667 | 0.667 | 0.051 | 0.019 | 0.060 | 0.000 | 0.039 | 0.000 |
| High Gaussian noise | 0.000 | 0.667 | 0.667 | 0.065 | 0.023 | 0.082 | 0.222 | 0.138 | 0.000 |
| Weak structural higher moments | 0.000 | 0.833 | 0.833 | 0.028 | 0.016 | 0.092 | 0.000 | 0.208 | 0.000 |
| Gaussian structural shocks | 0.000 | 0.833 | 0.833 | 0.027 | 0.020 | 0.090 | 0.167 | 0.220 | 0.000 |
| Skewed residual noise | 0.333 | 0.833 | 0.667 | 0.052 | 0.020 | 0.058 | 0.033 | 0.054 | 0.000 |

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| Monte Carlo uses the M71 sign screen and first-shock chart. | `code-implemented`, `user-decision` | This script and JSON configuration. | high | promote for Table 1 diagnostics |
| M71 removes the `B21>=0` sign restriction from the active MC. | `code-implemented`, `user-decision` | This script and JSON configuration. | high | promote |
| M71 uses candidate-specific pointwise covariance weights. | `code-implemented`, `user-decision` | Shared evaluator calls through `j_from_observations`. | high | promote |
| Robust MC uses `nu_i=lambda_i(BB')_ii` and profiles `lambda in [0,rho]^2`. | `code-implemented`, `derived` | M66 derivation and evaluator calls. | high | promote |
| The chi-square cutoffs are final projected confidence-set critical values. | `conjectural` | M65/M68 still leave projection-critical-value inference as follow-up. | medium | quarantine as diagnostic |
