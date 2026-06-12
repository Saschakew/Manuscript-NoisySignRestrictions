# M68 Unit-Variance First-Shock Figure Diagnostics

Status: generated first-shock impact figure for the M64/M66 unit-variance route.

The chart displays the projection of accepted matrices onto `(B11, B21)`, the impact vector of the first shock. It does not impose `diag(B)=1`: for every displayed projection point the script searches over `B12` and `B22`. The maintained sign screen is `B11>0`, `B22>0`, `B12<=0`, and `B21>=0`. The robust row also searches over `lambda in [0,rho]^2` and sets `nu_i=lambda_i (B B')_ii` before evaluating the Section 4 moment vector.

Truth markers refer to the full true matrix, not merely to whether the true `(B11,B21)` projection cell contains some other accepted profiled pair: a star means the full true `B0` passes that row's test, and an x means it does not.

The plotted J statistics use a fixed one-step GMM weight for each scenario, estimated from the fixed draw at the true parameter. The robust cutoff is a pointwise diagnostic chi-square cutoff for the eight displayed moment rows. The final projection-critical-value choice remains part of the broader M65 evidence task.

## Configuration

- Output figure: `manuscript\figures\fig_sign_dw_unit_variance_nongaussianity_grid.png`.
- Machine-readable diagnostics: `manuscript\simulations\output\sign_dw_unit_variance_nongaussianity_grid_figure.json`.
- Noise ratio bound: `rho=0.5`.
- Projection grid: `43 x 43` plus true coordinates.
- Profile grid: `11 x 11` plus true profiled coordinates.
- Lambda grid: `7 x 7` plus the true lambda values for each scenario.
- Weighting: fixed one-step GMM weights by scenario, evaluated at the fixed-draw true parameter for this diagnostic figure.

## Fixed-Draw Diagnostics

| Noise | Sign share | Standard DW share | Robust share | B0 standard | B0 robust | Robust distance | Best lambda at nearest accepted cell |
|---|---:|---:|---:|---|---|---:|---|
| w=1 | 0.220 | 0.130 | 0.100 | out | in | 0.000 | (0.188, 0.122) |
| w=0.25 | 0.123 | 0.123 | 0.166 | out | in | 0.000 | (0.167, 0.000) |
| w=0 | 0.129 | 0.129 | 0.196 | out | in | 0.000 | (0.188, 0.000) |

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| The robust row uses `nu_i=lambda_i (B B')_ii` with `lambda in [0,rho]^2`. | `code-implemented`, `derived` | `sign_dw_unit_variance_noise_grid_figure.py`; M66 derivation note. | high | promote for Figure 1 |
| The displayed chart is a projection to `(B11,B21)`, with `B12`, `B22`, and `lambda` profiled. | `code-implemented`, `user-decision` | Candidate grid construction and diagnostics JSON; M68 task. | high | promote |
| The maintained sign screen is `B11>0`, `B22>0`, `B12<=0`, and `B21>=0`. | `code-implemented`, `user-decision` | Candidate grid construction and diagnostics JSON; M68 task. | high | promote |
| The plotted J statistics use fixed one-step GMM weights for tractability and visual stability. | `code-implemented` | Scenario weight construction in the script. | high | promote as diagnostic implementation detail |
| The robust cutoff is final for projected inference. | `conjectural` | M65 still lists projection critical values as unresolved. | medium | quarantine as diagnostic |
