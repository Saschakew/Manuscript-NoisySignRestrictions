# Sign, Standard DW, And Robust DW Non-Gaussianity Grid

Status: exploratory companion figure candidate.

This figure complements `fig_sign_dw_robust_noise_grid.png`. The first grid
varies residual noise across columns. This grid instead fixes residual noise
and varies the strength of structural-shock non-Gaussianity across columns.

Source context:

- Manuscript noise-grid script:
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`
- Manuscript companion script:
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`
- Output figure:
  `manuscript/figures/fig_sign_dw_robust_nongaussianity_grid.png`

Command:

```powershell
python manuscript\simulations\sign_dw_robust_nongaussianity_grid_figure.py
```

## DGP And Grid

The figure uses the same diagonal-normalized B-plane calibration as the noise
grid:

```text
B0 = [[1, -0.45],
      [0.70, 1]]
```

Residual noise is fixed at

```text
V = (0.3, 0.3)
```

and the columns vary the structural-shock mixture

```text
epsilon = sqrt(w) * skewed_chi_square + sqrt(1-w) * Gaussian,
```

then re-standardize each structural shock to unit variance. The columns use
`w=1`, `w=0.35`, and `w=0.04`.

## Interpretation

The top sign/covariance row changes little because the second moments and
noise level are held fixed. The standard-DW and robust-DW rows depend on
higher moments. As the structural shocks become closer to Gaussian, the
higher-moment signal weakens and the accepted sets widen or become less
informative.

This is the visual limitation that should accompany the main story:
robust-DW protects the target from residual-noise covariance misspecification,
but it cannot create information when the structural shocks carry weak
non-Gaussian higher moments.

This remains a candidate visual. M28/M29 should still check population grids,
weak-moment behavior, and bootstrap or repeated-sample critical values before
the paper treats this as final evidence.
