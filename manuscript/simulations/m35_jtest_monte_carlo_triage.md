# M35 Early J-Test Monte Carlo Triage

Status: exploratory screening output, not final calibrated evidence.

## Command

```powershell
python manuscript/simulations/m35_jtest_monte_carlo_triage.py --seed 20260606 --reps 80 --sample-size 400 --angles 361 --shape-grid 51
```

## Design

- Seed: `20260606`
- Replications per scenario: `80`
- Sample size: `400`
- Standard-DW angle grid: `361` rotations
- Robust-DW shape grid: `51 x 51` before sign filtering
- Screening critical value: `11.0705` (chi-square 5, 95 percent reference)
- True normalized impact matrix: `[[1, 0.35], [-0.25, 1]]`
- Sign filter: `B11 > 0`, `B12 > 0`, `B21 < 0`, `B22 > 0`.

The statistic uses the five mixed higher-cumulant moments from the M24/M25 notes and a simple per-candidate scale normalization. It is meant to flag whether the comparison is promising enough for M28-M30, not to settle coverage.

## Scenario Notes

- `no_noise_strong`: No residual noise; shocks have strong skewness or kurtosis. Structural-coordinate off-diagonal noise norm: `0.0000`.
- `moderate_gaussian_noise`: Diagonal Gaussian residual noise in u-coordinates; for this B0 it is close to a structural-coordinate rescaling case. Structural-coordinate off-diagonal noise norm: `0.0096`.
- `anisotropic_gaussian_noise`: Diagonal Gaussian residual noise in u-coordinates with stronger structural-coordinate off-diagonal deformation. Structural-coordinate off-diagonal noise norm: `0.1285`.
- `weak_higher_moments_with_noise`: Same residual noise, but structural shocks are mostly Gaussian mixtures, weakening the higher-cumulant signal. Structural-coordinate off-diagonal noise norm: `0.0096`.

## Summary

| Scenario | Method | Nonempty rate | Nearest-shape accept rate | Mean accepted fraction | Median min J | Median least-rejected distance |
|---|---|---:|---:|---:|---:|---:|
| anisotropic_gaussian_noise | standard_dw | 0.963 | 0.938 | 0.2672 | 2.03 | 0.079 |
| anisotropic_gaussian_noise | robust_dw | 1.000 | 0.925 | 0.6997 | 0.99 | 0.141 |
| moderate_gaussian_noise | standard_dw | 0.975 | 0.963 | 0.2807 | 2.04 | 0.051 |
| moderate_gaussian_noise | robust_dw | 1.000 | 0.963 | 0.6330 | 0.94 | 0.121 |
| no_noise_strong | standard_dw | 0.963 | 0.925 | 0.2153 | 2.42 | 0.062 |
| no_noise_strong | robust_dw | 1.000 | 0.938 | 0.4838 | 1.35 | 0.095 |
| weak_higher_moments_with_noise | standard_dw | 1.000 | 0.988 | 0.9949 | 1.09 | 0.727 |
| weak_higher_moments_with_noise | robust_dw | 1.000 | 0.988 | 0.9965 | 0.59 | 0.525 |

## Triage Read

- The no-noise strong-moment scenario passes the basic sanity check: both routes are usually nonempty and their least-rejected shapes remain close to the true normalized shape.
- The original moderate-noise scenario is close to the structural-coordinate rescaling exception in the M25 derivation, so it is not a sharp test of standard-DW misspecification.
- The anisotropic-noise scenario is the relevant first stress case for generic residual-noise deformation, but the statistic is still provisional and should not be used for polished false-sharpening figures.
- The weak higher-moment scenario is almost non-discriminating for both methods. That is useful triage information: weak higher cumulants can make the robust comparison honest but very wide in macro-sized samples.
- Gate outcome: proceed to audit and population-grid verification before larger Monte Carlo work. This screen supports M28/M30 as the next evidence tasks, not M29-style final tables.

## Next Checks

- Audit this script before treating the output as evidence: moment scaling, critical values, shape normalization, sign filtering, and finite-sample size all remain provisional.
- M28 should replace this sample-screening run with population-grid checks that verify zeros and aliases directly.
- M29 should use repeated-sample or bootstrap critical values before reporting manuscript tables.
