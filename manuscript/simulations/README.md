# Simulations

Use this folder for exploratory simulation designs and design notes.

Final shareable code that reproduces manuscript figures and tables belongs in
`../replication/`.

## M0016 Sign, Standard DW, And Robust DW Noise Figure

- Script: `sign_dw_robust_noise_figure.py`
- Note: `sign_dw_robust_noise_figure.md`
- Output figure: `../figures/fig_sign_dw_robust_noise_comparison.png`
- Command run:

```powershell
python manuscript\simulations\sign_dw_robust_noise_figure.py
```

Interpretation: this is an exploratory population figure candidate. It
replicates the KnowledgeVault sign/standard-DW noise visualization and adds a
robust-DW normalized higher-cumulant panel under Gaussian residual noise. M28
must still run population-grid checks before the figure can be promoted to
final manuscript evidence.

## M35 Early J-Test Monte Carlo Triage

- Script: `m35_jtest_monte_carlo_triage.py`
- Output note: `m35_jtest_monte_carlo_triage.md`
- Machine-readable output: `output/m35_jtest_monte_carlo_summary.json`
- Audit note: `m30_m35_triage_audit.md`
- Command run:

```powershell
python manuscript/simulations/m35_jtest_monte_carlo_triage.py --seed 20260606 --reps 80 --sample-size 400 --angles 361 --shape-grid 51
```

Interpretation: this is a screening run only. M30 found that the original
moderate-noise case was close to a structural-coordinate rescaling exception,
added an anisotropic diagonal-noise stress case, and confirmed that the
provisional finite-sample statistic is too permissive for evidence. Population
grids and calibrated critical values must come before polished figures or
final Monte Carlo tables.
