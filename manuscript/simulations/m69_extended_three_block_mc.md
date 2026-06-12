# M71 Corrected Extended Three-Block Monte Carlo

Status: generated corrected extended MC output aligned with the three active figure blocks.

The set-size measure is the accepted share of the displayed `(B11,B21)` projection grid. The table reports both mean and median set size for the standard-DW and robust-DW inverted sets. Truth inclusion is reported as counts and rates.

The statistics use candidate-specific pointwise covariance estimates for each tested candidate. The cutoffs are pointwise chi-square diagnostics for the displayed moment rows. Final projected confidence-set critical values remain M65 follow-up.

## Configuration

- Machine-readable output: `manuscript/simulations/output/m69_extended_three_block_mc.json`.
- Quick run: `False`.
- Replications per scenario: `8`.
- Projection grid: `13 x 13`.
- Profile grid: `5 x 5`.
- Lambda grid: `3 x 3`.
- Sign screen: `B11>0`, `B22>0`, `B12<=0`; `B21` is not sign-restricted.
- Robust route: `nu_i=lambda_i(BB')_ii`, `lambda in [0,rho]^2`.

## Residual-noise grid

Matched figure: Figure 1. Matches Figure 1: residual-noise variance varies while T=500 and structural non-Gaussianity is strong.

| Scenario | S truth | R truth | Warning | S size mean | S size median | R size mean | R size median | S empty | R empty |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V=(0,0) | 6/8 (0.750; se 0.164) | 4/8 (0.500; se 0.189) | 0/8 (0.000; se 0.000) | 0.023 (se 0.004) | 0.031 | 0.031 (se 0.006) | 0.041 | 1/8 (0.125; se 0.125) | 1/8 (0.125; se 0.125) |
| V=(0.2,0.2) | 2/8 (0.250; se 0.164) | 5/8 (0.625; se 0.183) | 4/8 (0.500; se 0.189) | 0.017 (se 0.004) | 0.018 | 0.046 (se 0.009) | 0.048 | 1/8 (0.125; se 0.125) | 1/8 (0.125; se 0.125) |
| V=(0.5,0.5) | 0/8 (0.000; se 0.000) | 6/8 (0.750; se 0.164) | 6/8 (0.750; se 0.164) | 0.015 (se 0.004) | 0.018 | 0.073 (se 0.012) | 0.084 | 2/8 (0.250; se 0.164) | 1/8 (0.125; se 0.125) |

## Structural non-Gaussianity grid

Matched figure: Figure 2. Matches Figure 2: residual noise is fixed and structural higher moments weaken.

| Scenario | S truth | R truth | Warning | S size mean | S size median | R size mean | R size median | S empty | R empty |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| w=1 | 0/8 (0.000; se 0.000) | 4/8 (0.500; se 0.189) | 4/8 (0.500; se 0.189) | 0.016 (se 0.004) | 0.010 | 0.045 (se 0.008) | 0.046 | 0/8 (0.000; se 0.000) | 0/8 (0.000; se 0.000) |
| w=0.25 | 0/8 (0.000; se 0.000) | 8/8 (1.000; se 0.000) | 8/8 (1.000; se 0.000) | 0.024 (se 0.004) | 0.028 | 0.099 (se 0.005) | 0.102 | 0/8 (0.000; se 0.000) | 0/8 (0.000; se 0.000) |
| w=0 | 0/8 (0.000; se 0.000) | 7/8 (0.875; se 0.125) | 7/8 (0.875; se 0.125) | 0.011 (se 0.003) | 0.008 | 0.098 (se 0.002) | 0.099 | 1/8 (0.125; se 0.125) | 0/8 (0.000; se 0.000) |

## Sample-size grid

Matched figure: Figure 3. Matches Figure 3: residual noise and structural non-Gaussianity are fixed while T varies.

| Scenario | S truth | R truth | Warning | S size mean | S size median | R size mean | R size median | S empty | R empty |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T=500 | 1/8 (0.125; se 0.125) | 4/8 (0.500; se 0.189) | 3/8 (0.375; se 0.183) | 0.008 (se 0.003) | 0.010 | 0.036 (se 0.011) | 0.046 | 3/8 (0.375; se 0.183) | 3/8 (0.375; se 0.183) |
| T=1000 | 0/8 (0.000; se 0.000) | 6/8 (0.750; se 0.164) | 6/8 (0.750; se 0.164) | 0.000 (se 0.000) | 0.000 | 0.033 (se 0.005) | 0.041 | 8/8 (1.000; se 0.000) | 1/8 (0.125; se 0.125) |
| T=2000 | 0/8 (0.000; se 0.000) | 5/8 (0.625; se 0.183) | 5/8 (0.625; se 0.183) | 0.000 (se 0.000) | 0.000 | 0.018 (se 0.005) | 0.023 | 8/8 (1.000; se 0.000) | 2/8 (0.250; se 0.164) |

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| Extended MC mirrors the three active figure blocks. | `code-implemented`, `user-decision` | Scenario block configuration in this script and JSON. | high | promote as M69 setup result |
| Inverted-set size is measured by accepted projection share on `(B11,B21)`. | `code-implemented`, `user-decision` | `size` summaries in JSON and table. | high | promote as diagnostic size metric |
| Truth inclusion is counted for standard-DW and robust-DW sets. | `code-implemented`, `user-decision` | `truth_inclusion` count/rate summaries in JSON and table. | high | promote as MC diagnostic |
| M71 removes the `B21>=0` sign restriction from the extended MC. | `code-implemented`, `user-decision` | Scenario block configuration and shared evaluator. | high | promote |
| M71 uses candidate-specific pointwise covariance weights. | `code-implemented`, `user-decision` | Shared evaluator calls through `j_from_observations`. | high | promote |
| Robust MC uses `nu_i=lambda_i(BB')_ii` and profiles `lambda in [0,rho]^2`. | `code-implemented`, `derived` | M66 route reused through M68 evaluator calls. | high | promote |
| The chi-square cutoffs are final projected confidence-set critical values. | `conjectural` | M65 remains open for projected critical values. | medium | quarantine as diagnostic |
