# Figures

Store manuscript figures here when they are part of the paper.

Every final figure should have a corresponding entry in
`../formal-object-registry.json` and a reproducible source under
`../replication/` when possible.

## Candidate Figures

| File | Source | Status |
|---|---|---|
| `fig_sign_dw_robust_nongaussianity_grid.png` | `../simulations/sign_dw_robust_nongaussianity_grid_figure.py` | Selected M0030 companion story figure: fixes residual noise and varies structural-shock non-Gaussianity across columns; all rows invert pointwise 10 percent J tests, and the robust-DW row uses the off-diagonal covariance anchor plus mixed higher cumulants. |
| `fig_sign_dw_robust_noise_grid.png` | `../simulations/sign_dw_robust_noise_grid_figure.py` | Selected M0030 main story figure: reproduces the KnowledgeVault 2-by-3 sign/DW noise grid with a third diagonal-noise robust-DW row; all rows invert pointwise 10 percent J tests, and the lower high-noise column shows standard DW rejecting true `B0` while robust DW contains it. |
| `fig_sign_dw_robust_noise_comparison.png` | `../simulations/sign_dw_robust_noise_figure.py` | M0016 exploratory candidate: reproduces the KnowledgeVault sign/standard-DW noise visualization and adds a robust-DW normalized higher-cumulant panel. Not final evidence until M28 population-grid checks are complete. |
