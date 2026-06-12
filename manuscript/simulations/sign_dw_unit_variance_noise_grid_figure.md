# M73 Unit-Variance First-Shock Figure Diagnostics

Status: refreshed corrected first-shock impact figure for the M64/M66 unit-variance route with denser M73 grids; M71 method and M72 layout are preserved.

The chart displays the projection of accepted matrices onto `(B11, B21)`, the impact vector of the first shock. It does not impose `diag(B)=1`: for every displayed projection point the script searches over `B12` and `B22`. The maintained sign screen is `B11>0`, `B22>0`, and `B12<=0`; `B21` is displayed but not sign-restricted. The robust row also searches over `lambda in [0,rho]^2` and sets `nu_i=lambda_i (B B')_ii` before evaluating the Section 4 moment vector.

Truth markers refer to the full true matrix, not merely to whether the true `(B11,B21)` projection cell contains some other accepted profiled pair: a star means the full true `B0` passes that row's test, and an x means it does not.

The plotted statistics use candidate-specific pointwise covariance estimates: for each tested `B` or `(B,lambda)` candidate, the script estimates the covariance of that candidate's moment observations and computes `T g' W g`. The robust cutoff is a pointwise diagnostic chi-square cutoff for the eight displayed moment rows. The final projection-critical-value choice remains part of the broader M65 evidence task.

## Configuration

- Output figure: `manuscript/figures/fig_sign_dw_unit_variance_noise_grid.png`.
- Machine-readable diagnostics: `manuscript/simulations/output/sign_dw_unit_variance_noise_grid_figure.json`.
- Noise ratio bound: `rho=0.5`.
- Projection grid: `41 x 41` plus true coordinates.
- Profile grid: `11 x 11` plus true profiled coordinates.
- Lambda grid: `7 x 7` plus the true lambda values for each scenario.
- Weighting: candidate-specific pointwise covariance estimates for each tested candidate.
- Weight regularization: symmetric covariance eigensystem with eigenvalue floor `max(max_eigenvalue, 1) * 1e-10`.

## Fixed-Draw Diagnostics

| Noise | Sign share | Standard DW share | Robust share | B0 standard | B0 robust | Robust distance | Best lambda at nearest accepted cell |
|---|---:|---:|---:|---|---|---:|---|
| V=(0,0) | 0.066 | 0.028 | 0.045 | in | in | 0.000 | (0.000, 0.000) |
| V=(0.2,0.2) | 0.078 | 0.033 | 0.062 | out | in | 0.000 | (0.333, 0.333) |
| V=(0.5,0.5) | 0.094 | 0.049 | 0.087 | out | in | 0.000 | (0.471, 0.305) |

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| The robust row uses `nu_i=lambda_i (B B')_ii` with `lambda in [0,rho]^2`. | `code-implemented`, `derived` | `sign_dw_unit_variance_noise_grid_figure.py`; M66 derivation note. | high | promote for Figure 1 |
| The displayed chart is a projection to `(B11,B21)`, with `B12`, `B22`, and `lambda` profiled. | `code-implemented`, `user-decision` | Candidate grid construction and diagnostics JSON; M71 task. | high | promote |
| The maintained sign screen is `B11>0`, `B22>0`, and `B12<=0`; `B21` is unrestricted. | `code-implemented`, `user-decision` | Candidate grid construction and diagnostics JSON; M71 task. | high | promote |
| The plotted statistics use candidate-specific pointwise covariance weights. | `code-implemented`, `user-decision` | `j_from_observations` calls in the evaluator. | high | promote as diagnostic implementation detail |
| The robust cutoff is final for projected inference. | `conjectural` | M65 still lists projection critical values as unresolved. | medium | quarantine as diagnostic |
