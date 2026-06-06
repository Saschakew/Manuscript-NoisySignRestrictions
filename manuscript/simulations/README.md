# Simulations

Use this folder for exploratory simulation designs and design notes.

Final shareable code that reproduces manuscript figures and tables belongs in
`../replication/`.

## M29 Calibrated Monte Carlo First Pass

- Script: `m29_calibrated_monte_carlo.py`
- Note: `m29_calibrated_monte_carlo.md`
- Machine-readable output: `output/m29_calibrated_monte_carlo.json`
- Command run:

```powershell
python manuscript\simulations\m29_calibrated_monte_carlo.py
```

Interpretation: this first M29 pass keeps the M0020/M28 B-plane and reports
the M27 metric bundle under three pointwise cutoff conventions: the
chi-square guide, a no-noise repeated-sample calibration applied to every
scenario, and an oracle scenario-specific truth calibration. The high-noise
case supports the visual warning: standard DW includes true `B0` in only about
one third of evaluation samples under the no-noise repeated calibration,
while robust DW includes it in most samples. The high-noise oracle
standard-DW cutoff rises sharply, showing the calibration cost of forcing the
misspecified statistic to cover the truth. This remains a first pass, not the
final manuscript table; M29 still needs a larger or bootstrap-calibrated
evidence run before coverage claims are final.

## M0020 Non-Gaussianity Companion Grid

- Script: `sign_dw_robust_nongaussianity_grid_figure.py`
- Note: `sign_dw_robust_nongaussianity_grid_figure.md`
- Output figure: `../figures/fig_sign_dw_robust_nongaussianity_grid.png`
- Command run:

```powershell
python manuscript\simulations\sign_dw_robust_nongaussianity_grid_figure.py
```

Interpretation: this selected companion to the M0020 noise grid fixes residual noise at
`V=(0.3,0.3)` and weakens structural-shock non-Gaussianity across columns.
All rows invert pointwise 10 percent J tests. It is meant to show the honest
limitation: robust-DW can be robust to residual noise but wide when higher
moments are weak.

## M28 Grid Story Validation

- Script: `m28_grid_story_validation.py`
- Note: `m28_grid_story_validation.md`
- Machine-readable output: `output/m28_grid_story_validation.json`
- Command run:

```powershell
python manuscript\simulations\m28_grid_story_validation.py
```

Interpretation: this first M28 validation pass keeps the M0020 figure scripts
unchanged and checks the selected grid-pair story with exact population
moments, grid-boundary sensitivity, repeated finite-sample seeds, and
pointwise critical-value sensitivity. It supports the visual spine under the
maintained Gaussian residual-noise condition: standard DW moves away from true
`B0` under high residual noise, robust DW keeps true `B0` as a population zero,
and weak or Gaussian structural higher moments widen or empty the identifying
content of the robust row. It is not final coverage evidence; M29 still needs
calibrated repeated-sample or bootstrap critical values.

## M0020 Corrected Sign/DW/Robust-DW Noise Grid

- Script: `sign_dw_robust_noise_grid_figure.py`
- Note: `sign_dw_robust_noise_grid_figure.md`
- Output figure: `../figures/fig_sign_dw_robust_noise_grid.png`
- Command run:

```powershell
python manuscript\simulations\sign_dw_robust_noise_grid_figure.py
```

Interpretation: this is the selected main story figure. All rows invert
pointwise 10 percent J tests. The robust-DW row uses only mixed higher
cumulants, and the high-noise column shows standard DW rejecting true `B0`
while robust DW contains it.

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
now favors the M0020 grid pair as the main visual spine, while M29 calibration
remains open before final manuscript evidence.

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
