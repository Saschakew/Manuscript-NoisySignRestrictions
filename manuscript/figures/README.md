# Figures

Store manuscript figures here when they are part of the paper.

Every final figure should have a corresponding entry in
`../formal-object-registry.json` and a reproducible source under
`../replication/` when possible.

## Candidate Figures

| File | Source | Status |
|---|---|---|
| `fig_sign_dw_unit_variance_noise_grid.png` | `../simulations/sign_dw_unit_variance_noise_grid_figure.py --scenario-set noise` | Active M68 Figure 1 diagnostic: projects accepted unit-variance candidates onto first-shock coordinates `(B11,B21)`, profiles `B12`, `B22`, and `lambda`, imposes `B11>0`, `B22>0`, `B12<=0`, and `B21>=0`, and uses the M66 bound `lambda_i=nu_i/(BB')_ii in [0,rho]`. |
| `fig_sign_dw_unit_variance_nongaussianity_grid.png` | `../simulations/sign_dw_unit_variance_noise_grid_figure.py --scenario-set nongaussianity` | Active M68 Figure 2 diagnostic: fixes residual noise, weakens structural non-Gaussianity, and uses the same first-shock chart, sign screen, and projected `(B,lambda)` search as Figure 1. |
| `fig_sign_dw_unit_variance_sample_size_grid.png` | `../simulations/sign_dw_unit_variance_noise_grid_figure.py --scenario-set sample_size` | Active M68 Figure 3 diagnostic: fixes residual noise and structural non-Gaussianity, varies `T`, and uses the same first-shock chart, sign screen, and projected `(B,lambda)` search as Figure 1. |
| `fig_sign_dw_relative_noise_robust_grid.png` | `../simulations/sign_dw_robust_noise_grid_figure.py --robust-mode relative` | Historical pre-M64/M66 Figure 1 candidate: robust row used the old diagonal-normalized B-plane and the pre-M64 variance-ratio feasibility screen. |
| `fig_sign_dw_robust_nongaussianity_grid.png` | `../simulations/sign_dw_robust_nongaussianity_grid_figure.py` | Historical Figure 2 candidate after M68: fixes residual noise, weakens structural non-Gaussianity, and still uses the pre-M64 variance-ratio robust row. |
| `fig_sign_dw_sample_size_robust_grid.png` | `../simulations/sign_dw_sample_size_robust_grid_figure.py` | Historical Figure 3 candidate after M68: varies `T=500,1000,2000` with strong structural non-Gaussianity and fixed moderate residual noise, but uses the pre-M64 chart. |
| `fig_sign_dw_bounded_noise_robust_grid.png` | `../simulations/sign_dw_robust_noise_grid_figure.py --robust-mode bounded` | M0035 comparison candidate: robust row uses pure higher cumulants plus the absolute `nu_i <= 0.5` recovered-covariance screen. Superseded as preferred candidate by the scale-correct M0036 relative screen. |
| `fig_sign_dw_pure_robust_noise_grid.png` | `../simulations/sign_dw_robust_noise_grid_figure.py --robust-mode pure` | M0034 validity diagnostic: robust row uses only five higher-cumulant moments after dropping invalid second-order anchors. |
| `fig_sign_dw_robust_noise_grid.png` | `../simulations/sign_dw_robust_noise_grid_figure.py` | M0030 diagonal-anchor figure, superseded for the robust row by M0034/M0036 scale correction. |
| `fig_sign_dw_robust_noise_comparison.png` | `../simulations/sign_dw_robust_noise_figure.py` | M0016 exploratory candidate: reproduces the KnowledgeVault sign/standard-DW noise visualization and adds a robust-DW normalized higher-cumulant panel. Not final evidence until M28 population-grid checks are complete. |
