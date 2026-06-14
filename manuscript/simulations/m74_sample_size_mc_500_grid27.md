# M74 Sample-Size Monte Carlo

Status: generated corrected sample-size MC output aligned with the active Figure 3 block.

The set-size measure is the accepted share of the displayed `(B11,B21)` projection grid. The table reports both mean and median set size for the Sign, DW, and nrDW inverted sets. Truth inclusion is reported as counts and rates. Sign truth is reconstructed from the stored no-noise second-moment truth statistic and the `chi2_3(0.90)` cutoff; the maintained signs hold at the true `B0`.

The statistics use candidate-specific pointwise covariance estimates for each tested candidate. The cutoffs are pointwise chi-square diagnostics for the displayed moment rows. Final projected confidence-set critical values remain M65 follow-up.

## Configuration

- Machine-readable output: `manuscript/simulations/output/m74_sample_size_mc_500_grid27.json`.
- Quick run: `False`.
- Replications per scenario: `500`.
- Projection grid: `27 x 27`.
- Profile grid: `7 x 7`.
- Lambda grid: `5 x 5`.
- Sign screen: `B11>0`, `B22>0`, `B12<=0`; `B21` is not sign-restricted.
- Robust route: `nu_i=lambda_i(BB')_ii`, `lambda in [0,rho]^2`.

## Sample-size grid

Matched figure: Figure 3. Matches Figure 3: residual noise and structural non-Gaussianity are fixed while T varies.

| Scenario | Sign truth | DW truth | nrDW truth | Warning | Sign size mean | Sign size median | DW size mean | DW size median | nrDW size mean | nrDW size median | Sign empty | DW empty | nrDW empty |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T=500 | 56/500 (0.112; se 0.014) | 55/500 (0.110; se 0.014) | 375/500 (0.750; se 0.019) | 338/500 (0.676; se 0.021) | 0.062 (se 0.000) | 0.061 | 0.022 (se 0.000) | 0.022 | 0.050 (se 0.001) | 0.052 | 0/500 (0.000; se 0.000) | 5/500 (0.010; se 0.004) | 12/500 (0.024; se 0.007) |
| T=1000 | 0/500 (0.000; se 0.000) | 0/500 (0.000; se 0.000) | 421/500 (0.842; se 0.016) | 421/500 (0.842; se 0.016) | 0.034 (se 0.000) | 0.033 | 0.009 (se 0.000) | 0.009 | 0.031 (se 0.000) | 0.033 | 0/500 (0.000; se 0.000) | 11/500 (0.022; se 0.007) | 13/500 (0.026; se 0.007) |
| T=2000 | 0/500 (0.000; se 0.000) | 0/500 (0.000; se 0.000) | 436/500 (0.872; se 0.015) | 436/500 (0.872; se 0.015) | 0.014 (se 0.000) | 0.014 | 0.003 (se 0.000) | 0.003 | 0.019 (se 0.000) | 0.022 | 0/500 (0.000; se 0.000) | 72/500 (0.144; se 0.016) | 28/500 (0.056; se 0.010) |

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| Extended MC mirrors the three active figure blocks. | `code-implemented`, `user-decision` | Scenario block configuration in this script and JSON. | high | promote as M69 setup result |
| Inverted-set size is measured by accepted projection share on `(B11,B21)`. | `code-implemented`, `user-decision` | `size` summaries in JSON and table. | high | promote as diagnostic size metric |
| Truth inclusion is counted directly for DW and nrDW sets. | `code-implemented`, `user-decision` | `truth_inclusion` count/rate summaries in JSON and table. | high | promote as MC diagnostic |
| Sign-only truth inclusion can be reported for M74. | `code-implemented`, `derived` | The JSON stores `standard_dw.truth_second_j`; because the true signs hold, `truth_second_j <= chi2_3(0.90)` gives sign-only truth inclusion. | high | promote as baseline MC diagnostic |
| M71 removes the `B21>=0` sign restriction from the extended MC. | `code-implemented`, `user-decision` | Scenario block configuration and shared evaluator. | high | promote |
| M71 uses candidate-specific pointwise covariance weights. | `code-implemented`, `user-decision` | Shared evaluator calls through `j_from_observations`. | high | promote |
| Robust MC uses `nu_i=lambda_i(BB')_ii` and profiles `lambda in [0,rho]^2`. | `code-implemented`, `derived` | M66 route reused through M68 evaluator calls. | high | promote |
| The chi-square cutoffs are final projected confidence-set critical values. | `conjectural` | M65 remains open for projected critical values. | medium | quarantine as diagnostic |
