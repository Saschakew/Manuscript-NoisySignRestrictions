# Simulations

Use this folder for exploratory simulation designs and design notes.

Final shareable code that reproduces manuscript figures and tables belongs in
`../replication/`.

## M29 Refreshed Chi-Square-Primary Monte Carlo Pass

- Script: `m29_calibrated_monte_carlo.py`
- Note: `m29_calibrated_monte_carlo.md`
- Machine-readable output: `output/m29_calibrated_monte_carlo.json`
- Command run:

```powershell
python manuscript\simulations\m29_calibrated_monte_carlo.py --calibration-reps 120 --evaluation-reps 60 --bootstrap-reps 20 --grid-points 41
```

Interpretation: this refreshed M29 pass keeps the M0030 revised B-plane and reports
the M27 metric bundle under four pointwise cutoff conventions. The chi-square
rows are the primary applied benchmark because they match the critical values a
standard-DW researcher would use when unaware of residual noise. The high-noise
case supports the visual warning: standard DW includes true `B0` in only 0.050
of evaluation samples under the chi-square guide, while robust DW includes it
in 0.900. No-noise repeated, oracle scenario truth, and truth-point residual
bootstrap cutoffs are calibration audits. The high-noise oracle standard-DW
cutoff rises sharply, and the truth-bootstrap convention restores truth
inclusion only by widening accepted sets. Weak and Gaussian structural-shock
cases show robust DW widening toward its covariance anchor, which supports the
limitation story rather than a sharp higher-moment identification claim.

## M0030 Non-Gaussianity Companion Grid

- Script: `sign_dw_robust_nongaussianity_grid_figure.py`
- Note: `sign_dw_robust_nongaussianity_grid_figure.md`
- Output figure: `../figures/fig_sign_dw_robust_nongaussianity_grid.png`
- Command run:

```powershell
python manuscript\simulations\sign_dw_robust_nongaussianity_grid_figure.py
```

Interpretation: this selected companion to the M0030 noise grid fixes residual
noise at `V=(0.2,0.2)` and weakens structural-shock non-Gaussianity across
columns. All rows invert pointwise 10 percent J tests. It is meant to show the
honest limitation: the robust-DW higher-cumulant component loses power when
higher moments are weak, leaving the off-diagonal covariance anchor to carry
the row.

## M28 Grid Story Validation

- Script: `m28_grid_story_validation.py`
- Note: `m28_grid_story_validation.md`
- Machine-readable output: `output/m28_grid_story_validation.json`
- Command run:

```powershell
python manuscript\simulations\m28_grid_story_validation.py
```

Interpretation: this refreshed M28 validation pass checks the M0030 revised
grid-pair story with exact population
moments, grid-boundary sensitivity, repeated finite-sample seeds, and
pointwise critical-value sensitivity. It supports the visual spine under the
maintained diagonal Gaussian residual-noise condition: standard DW moves away
from true `B0` under high residual noise, robust DW keeps true `B0` as a
population zero, and weak or Gaussian structural higher moments widen the row
toward the covariance anchor. It is not final coverage evidence; after U0026,
M29 uses chi-square cutoffs as the primary applied benchmark and
repeated/bootstrap cutoffs as calibration audits.

## M0030 Corrected Sign/DW/Robust-DW Noise Grid

- Script: `sign_dw_robust_noise_grid_figure.py`
- Note: `sign_dw_robust_noise_grid_figure.md`
- Output figure: `../figures/fig_sign_dw_robust_noise_grid.png`
- Command run:

```powershell
python manuscript\simulations\sign_dw_robust_noise_grid_figure.py
```

Interpretation: this is the selected main story figure. All rows invert
pointwise 10 percent J tests. The robust-DW row uses the diagonal-noise
off-diagonal covariance restriction plus mixed higher cumulants, and the
lower high-noise column `V=(0.5,0.5)` shows standard DW rejecting true `B0`
while robust DW contains it without accepting the whole chart.

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
now favors the M0030 revised grid pair as the main visual spine, and M29
supplies the refreshed finite-sample evidence gate for drafting.

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
