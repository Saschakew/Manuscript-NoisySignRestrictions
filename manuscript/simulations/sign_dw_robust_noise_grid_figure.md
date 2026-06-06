# Sign, Standard DW, And Robust DW Noise Grid

Status: corrected exploratory manuscript-local figure candidate.

This is the corrected version of the KnowledgeVault B-plane figure requested in
M0017. It uses the two-by-three sign/DW layout from the synthesis and adds a
third robust-DW row. The M0019 correction is that the bottom row now uses the
pure robust-DW higher-cumulant population set: it does not use cross covariance
or any other second-moment restriction. The top and middle rows still use
finite-sample pointwise N-test statistics.

Source context:

- KnowledgeVault synthesis:
  `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md`
- KnowledgeVault B-plane visualization lab:
  `replications/svar-noise-recursive-sign-visualization/noisy_svar_visuals.py`
- KnowledgeVault robust inversion lab:
  `replications/bonhomme-robin-noise-robust-svar/br_noise_robust_svar.py`
- Manuscript script:
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`
- Output figure:
  `manuscript/figures/fig_sign_dw_robust_noise_grid.png`

Command:

```powershell
python manuscript\simulations\sign_dw_robust_noise_grid_figure.py
```

## DGP And Grid

The figure uses the diagonal-normalized B-plane calibration

```text
B0 = [[1, -0.45],
      [0.70, 1]]
```

and evaluates the same three diagonal-noise columns as the KnowledgeVault
figure:

```text
V = (0, 0), (0.3, 0.3), (1, 1).
```

The structural shocks are standardized chi-square shocks with `df=5`. The
additive residual noise is Gaussian and standardized before applying the
diagonal noise variance. This keeps the residual-noise covariance distortion in
the sign and standard-DW rows, while ensuring that the pure robust-DW
higher-cumulant row is not contaminated by non-Gaussian transformed noise.

The grid is `B(b12,b21) = [[1,b12],[b21,1]]`, with the sign restriction
`b21 >= 0`.

## Test Cutoffs

The top and middle rows use the finite-sample statistic

```text
J(B) = N mean(f(B))' S(B)^(-1) mean(f(B))
```

with `N=500`.

- Top row: sign/covariance row, testing `e1*e2`; cutoff
  `chi2_1(0.95) = 3.84`.
- Middle row: standard DW row, testing covariance, two co-skewness moments,
  and one fourth cross moment; cutoff `chi2_4(0.95) = 9.49`.
- Bottom row: pure robust-DW row, using the population mixed third and fourth
  cumulant score only. It uses no covariance restriction and no covariance
  target. The visual cutoff is `chi2_5(0.95)/N`, applied to the normalized
  higher-cumulant score.

## Interpretation

The top row shows the sign/covariance accepted B-plane band. The middle row
shows how standard DW refines that band using recovered-shock independence
moments under the no-noise two-shock representation. The accepted region moves
away from the true no-noise `B0` as the covariance target becomes noisy.

The bottom row shows the pure robust-DW higher-cumulant set. Because the row
uses only structural higher cumulants and the residual noise is Gaussian, it is
invariant across the three noise columns. It remains wider than the standard-DW
row and continues to contain the true `B0` in this design.

This is still a candidate figure. The top and middle rows use chi-square
reference cutoffs from the KnowledgeVault synthesis, while the bottom row is a
population-score visualization. Final evidence should still check bootstrap or
repeated-sample critical values and weak-moment behavior in M28 and M29.
