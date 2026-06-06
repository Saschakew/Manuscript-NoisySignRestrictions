# Figures

Store manuscript figures here when they are part of the paper.

Every final figure should have a corresponding entry in
`../formal-object-registry.json` and a reproducible source under
`../replication/` when possible.

## Candidate Figures

| File | Source | Status |
|---|---|---|
| `fig_sign_dw_robust_nongaussianity_grid.png` | `../simulations/sign_dw_robust_nongaussianity_grid_figure.py` | M0019 corrected companion candidate: fixes residual noise and varies structural-shock non-Gaussianity across columns; the robust-DW row uses only population higher cumulants and expands to the whole admissible graph under Gaussian shocks. |
| `fig_sign_dw_robust_noise_grid.png` | `../simulations/sign_dw_robust_noise_grid_figure.py` | M0019 corrected candidate: reproduces the KnowledgeVault 2-by-3 sign/DW noise grid with finite-sample N-test cutoffs in the top/middle rows and a pure robust-DW population row that uses only higher cumulants and no second moments. Preferred over the M0016 three-panel candidate for the user's requested visual. |
| `fig_sign_dw_robust_noise_comparison.png` | `../simulations/sign_dw_robust_noise_figure.py` | M0016 exploratory candidate: reproduces the KnowledgeVault sign/standard-DW noise visualization and adds a robust-DW normalized higher-cumulant panel. Not final evidence until M28 population-grid checks are complete. |
