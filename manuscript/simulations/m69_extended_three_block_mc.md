# M69 Extended Three-Block Monte Carlo

Status: generated extended MC output aligned with the three active M68 figure blocks.

The set-size measure is the accepted share of the displayed `(B11,B21)` projection grid. The table reports both mean and median set size for the standard-DW and robust-DW inverted sets. Truth inclusion is reported as counts and rates.

The cutoffs are pointwise chi-square diagnostics for the displayed moment rows. Final projected confidence-set critical values remain M65 follow-up.

## Configuration

- Machine-readable output: `manuscript/simulations/output/m69_extended_three_block_mc.json`.
- Quick run: `False`.
- Replications per scenario: `24`.
- Projection grid: `17 x 17`.
- Profile grid: `7 x 7`.
- Lambda grid: `5 x 5`.
- Sign screen: `B11>0`, `B22>0`, `B12<=0`, `B21>=0`.
- Robust route: `nu_i=lambda_i(BB')_ii`, `lambda in [0,rho]^2`.

## Residual-noise grid

Matched figure: Figure 1. Matches Figure 1: residual-noise variance varies while T=500 and structural non-Gaussianity is strong.

| Scenario | S truth | R truth | Warning | S size mean | S size median | R size mean | R size median | S empty | R empty |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V=(0,0) | 16/24 (0.667; se 0.098) | 14/24 (0.583; se 0.103) | 0/24 (0.000; se 0.000) | 0.032 (se 0.004) | 0.035 | 0.031 (se 0.004) | 0.035 | 2/24 (0.083; se 0.058) | 4/24 (0.167; se 0.078) |
| V=(0.2,0.2) | 7/24 (0.292; se 0.095) | 16/24 (0.667; se 0.098) | 12/24 (0.500; se 0.104) | 0.080 (se 0.005) | 0.079 | 0.080 (se 0.005) | 0.085 | 0/24 (0.000; se 0.000) | 0/24 (0.000; se 0.000) |
| V=(0.5,0.5) | 0/24 (0.000; se 0.000) | 19/24 (0.792; se 0.085) | 19/24 (0.792; se 0.085) | 0.214 (se 0.006) | 0.215 | 0.180 (se 0.007) | 0.184 | 0/24 (0.000; se 0.000) | 0/24 (0.000; se 0.000) |

## Structural non-Gaussianity grid

Matched figure: Figure 2. Matches Figure 2: residual noise is fixed and structural higher moments weaken.

| Scenario | S truth | R truth | Warning | S size mean | S size median | R size mean | R size median | S empty | R empty |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| w=1 | 0/24 (0.000; se 0.000) | 15/24 (0.625; se 0.101) | 15/24 (0.625; se 0.101) | 0.079 (se 0.004) | 0.079 | 0.079 (se 0.005) | 0.085 | 0/24 (0.000; se 0.000) | 0/24 (0.000; se 0.000) |
| w=0.25 | 0/24 (0.000; se 0.000) | 23/24 (0.958; se 0.042) | 23/24 (0.958; se 0.042) | 0.113 (se 0.002) | 0.114 | 0.167 (se 0.004) | 0.167 | 0/24 (0.000; se 0.000) | 0/24 (0.000; se 0.000) |
| w=0 | 0/24 (0.000; se 0.000) | 18/24 (0.750; se 0.090) | 18/24 (0.750; se 0.090) | 0.114 (se 0.004) | 0.116 | 0.164 (se 0.008) | 0.177 | 0/24 (0.000; se 0.000) | 0/24 (0.000; se 0.000) |

## Sample-size grid

Matched figure: Figure 3. Matches Figure 3: residual noise and structural non-Gaussianity are fixed while T varies.

| Scenario | S truth | R truth | Warning | S size mean | S size median | R size mean | R size median | S empty | R empty |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T=500 | 2/24 (0.083; se 0.058) | 14/24 (0.583; se 0.103) | 13/24 (0.542; se 0.104) | 0.075 (se 0.006) | 0.077 | 0.071 (se 0.007) | 0.077 | 0/24 (0.000; se 0.000) | 2/24 (0.083; se 0.058) |
| T=1000 | 0/24 (0.000; se 0.000) | 20/24 (0.833; se 0.078) | 20/24 (0.833; se 0.078) | 0.032 (se 0.002) | 0.035 | 0.053 (se 0.003) | 0.056 | 0/24 (0.000; se 0.000) | 0/24 (0.000; se 0.000) |
| T=2000 | 0/24 (0.000; se 0.000) | 21/24 (0.875; se 0.069) | 21/24 (0.875; se 0.069) | 0.012 (se 0.001) | 0.012 | 0.034 (se 0.002) | 0.034 | 1/24 (0.042; se 0.042) | 0/24 (0.000; se 0.000) |

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| Extended MC mirrors the three active figure blocks. | `code-implemented`, `user-decision` | Scenario block configuration in this script and JSON. | high | promote as M69 setup result |
| Inverted-set size is measured by accepted projection share on `(B11,B21)`. | `code-implemented`, `user-decision` | `size` summaries in JSON and table. | high | promote as diagnostic size metric |
| Truth inclusion is counted for standard-DW and robust-DW sets. | `code-implemented`, `user-decision` | `truth_inclusion` count/rate summaries in JSON and table. | high | promote as MC diagnostic |
| Robust MC uses `nu_i=lambda_i(BB')_ii` and profiles `lambda in [0,rho]^2`. | `code-implemented`, `derived` | M66 route reused through M68 evaluator calls. | high | promote |
| The chi-square cutoffs are final projected confidence-set critical values. | `conjectural` | M65 remains open for projected critical values. | medium | quarantine as diagnostic |
