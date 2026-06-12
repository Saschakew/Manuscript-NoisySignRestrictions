# M67 Unit-Variance Figure 1 Diagnostics

Status: generated corrected Figure 1 for the M64/M66 unit-variance route.

The chart displays the projection of accepted matrices onto `(B12, B21)`. It does not impose `diag(B)=1`: for every displayed projection point the script searches over positive `B11` and `B22`. The robust row also searches over `lambda in [0,rho]^2` and sets `nu_i=lambda_i (B B')_ii` before evaluating the Section 4 moment vector.

Truth markers refer to the full true matrix, not merely to whether the true `(B12,B21)` projection cell contains some other accepted diagonal pair: a star means the full true `B0` passes that row's test, and an x means it does not.

The plotted J statistics use a fixed one-step GMM weight for each scenario, estimated from the fixed draw at the true parameter. The robust cutoff is a pointwise diagnostic chi-square cutoff for the eight displayed moment rows. The final projection-critical-value choice remains part of the broader M65 evidence task.

## Configuration

- Output figure: `manuscript/replication/output/quick/fig_sign_dw_unit_variance_noise_grid.png`.
- Machine-readable diagnostics: `manuscript/simulations/output/sign_dw_unit_variance_noise_grid_figure.json`.
- Sample size: `500`.
- Seed: `20260605`.
- Noise ratio bound: `rho=0.5`.
- Projection grid: `47 x 47` plus true coordinates.
- Diagonal grid: `11 x 11` plus true diagonal entries.
- Lambda grid: `7 x 7` plus the true lambda values for each scenario.
- Weighting: fixed one-step GMM weights by scenario, evaluated at the fixed-draw true parameter for this diagnostic figure.

## Fixed-Draw Diagnostics

| Noise | Sign share | Standard DW share | Robust share | B0 standard | B0 robust | Robust distance | Best lambda at nearest accepted cell |
|---|---:|---:|---:|---|---|---:|---|
| V=(0,0) | 0.161 | 0.042 | 0.043 | in | in | 0.000 | (0.000, 0.000) |
| V=(0.2,0.2) | 0.219 | 0.100 | 0.102 | out | in | 0.000 | (0.083, 0.000) |
| V=(0.5,0.5) | 0.284 | 0.265 | 0.223 | out | in | 0.000 | (0.167, 0.000) |

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| The robust row uses `nu_i=lambda_i (B B')_ii` with `lambda in [0,rho]^2`. | `code-implemented`, `derived` | `sign_dw_unit_variance_noise_grid_figure.py`; M66 derivation note. | high | promote for Figure 1 |
| The displayed chart is a projection to `(B12,B21)`, with diagonal entries profiled. | `code-implemented` | Candidate grid construction and diagnostics JSON. | high | promote |
| The plotted J statistics use fixed one-step GMM weights for tractability and visual stability. | `code-implemented` | Scenario weight construction in the script. | high | promote as diagnostic implementation detail |
| The robust cutoff is final for projected inference. | `conjectural` | M65 still lists projection critical values as unresolved. | medium | quarantine as diagnostic |
