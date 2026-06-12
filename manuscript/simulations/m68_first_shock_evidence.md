# M68 First-Shock Monte Carlo Evidence

Status: generated Monte Carlo table for the M68 first-shock impact chart.

The table uses the same sign screen as Figures 1-3: `B11>0`, `B22>0`, `B12<=0`, and `B21>=0`. The displayed coordinates are `(B11,B21)`, while `B12`, `B22`, and `lambda` are profiled. The robust row evaluates the M66 moment vector at `nu_i=lambda_i(BB')_ii`.

The cutoffs are pointwise chi-square diagnostics for the displayed moment rows. The final projected critical-value route remains an inference follow-up.

## Configuration

- Machine-readable output: `manuscript\simulations\output\m68_first_shock_evidence.json`.
- Replications per scenario: `12`.
- Projection grid: `17 x 17`.
- Profile grid: `7 x 7`.
- Lambda grid: `5 x 5`.

## Chi-Square Diagnostic Table

| Scenario | S truth | R truth | Warning | Sign share | S share | R share | d_S_not_subset_R | S dist | R dist |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| No noise, strong moments | 0.583 | 0.500 | 0.000 | 0.111 | 0.029 | 0.029 | 0.421 | 0.023 | 0.027 |
| Moderate Gaussian noise | 0.083 | 0.583 | 0.583 | 0.165 | 0.073 | 0.075 | 0.255 | 0.000 | 0.000 |
| High Gaussian noise | 0.000 | 0.750 | 0.750 | 0.248 | 0.210 | 0.186 | 0.451 | 0.082 | 0.000 |
| Weak structural higher moments | 0.000 | 0.917 | 0.917 | 0.121 | 0.118 | 0.167 | 0.173 | 0.024 | 0.000 |
| Gaussian structural shocks | 0.000 | 0.833 | 0.833 | 0.114 | 0.112 | 0.162 | 0.141 | 0.014 | 0.000 |
| Skewed residual noise | 0.167 | 0.667 | 0.583 | 0.178 | 0.075 | 0.072 | 0.286 | 0.010 | 0.007 |

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| Monte Carlo uses the M68 sign screen and first-shock chart. | `code-implemented`, `user-decision` | This script and JSON configuration. | high | promote for Table 1 diagnostics |
| Robust MC uses `nu_i=lambda_i(BB')_ii` and profiles `lambda in [0,rho]^2`. | `code-implemented`, `derived` | M66 derivation and evaluator calls. | high | promote |
| The chi-square cutoffs are final projected confidence-set critical values. | `conjectural` | M65/M68 still leave projection-critical-value inference as follow-up. | medium | quarantine as diagnostic |
