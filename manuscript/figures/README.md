# Figures

Store manuscript figures here when they are part of the paper.

Every final figure should have a corresponding entry in
`../formal-object-registry.json` and a reproducible source under
`../replication/` when possible.

## Candidate Figures

| File | Source | Status |
|---|---|---|
| `fig_sign_dw_relative_noise_robust_grid.png` | `../simulations/sign_dw_robust_noise_grid_figure.py --robust-mode relative` | M0036 current Figure 1 candidate: robust row uses pure higher cumulants plus the explicit `nu_i <= 0.5 Var(epsilon_i)` covariance-decomposition screen. Needs M40 audit before final evidence claims. |
| `fig_sign_dw_bounded_noise_robust_grid.png` | `../simulations/sign_dw_robust_noise_grid_figure.py --robust-mode bounded` | M0035 comparison candidate: robust row uses pure higher cumulants plus the absolute `nu_i <= 0.5` recovered-covariance screen. Superseded as preferred candidate by the scale-correct M0036 relative screen. |
| `fig_sign_dw_pure_robust_noise_grid.png` | `../simulations/sign_dw_robust_noise_grid_figure.py --robust-mode pure` | M0034 validity diagnostic: robust row uses only five higher-cumulant moments after dropping invalid second-order anchors. |
| `fig_sign_dw_robust_nongaussianity_grid.png` | `../simulations/sign_dw_robust_nongaussianity_grid_figure.py` | M0030 companion story figure, now historical for the robust row because it used the superseded off-diagonal covariance anchor. Rebuild after M40 if the relative screen passes audit. |
| `fig_sign_dw_robust_noise_grid.png` | `../simulations/sign_dw_robust_noise_grid_figure.py` | M0030 diagonal-anchor figure, superseded for the robust row by M0034/M0036 scale correction. |
| `fig_sign_dw_robust_noise_comparison.png` | `../simulations/sign_dw_robust_noise_figure.py` | M0016 exploratory candidate: reproduces the KnowledgeVault sign/standard-DW noise visualization and adds a robust-DW normalized higher-cumulant panel. Not final evidence until M28 population-grid checks are complete. |
