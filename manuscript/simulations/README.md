# Simulations

Use this folder for exploratory simulation designs and design notes.

Final shareable code that reproduces manuscript figures and tables belongs in
`../replication/`.

## M68 First-Shock Unit-Variance Evidence Rebuild

- Figure script: `sign_dw_unit_variance_noise_grid_figure.py`
- Monte Carlo script: `m68_first_shock_evidence.py`
- Figure 1 note: `sign_dw_unit_variance_noise_grid_figure.md`
- Figure 2 note: `sign_dw_unit_variance_nongaussianity_grid_figure.md`
- Figure 3 note: `sign_dw_unit_variance_sample_size_grid_figure.md`
- Monte Carlo note: `m68_first_shock_evidence.md`
- Machine-readable outputs:
  - `output/sign_dw_unit_variance_noise_grid_figure.json`
  - `output/sign_dw_unit_variance_nongaussianity_grid_figure.json`
  - `output/sign_dw_unit_variance_sample_size_grid_figure.json`
  - `output/m68_first_shock_evidence.json`
- Output figures:
  - `../figures/fig_sign_dw_unit_variance_noise_grid.png`
  - `../figures/fig_sign_dw_unit_variance_nongaussianity_grid.png`
  - `../figures/fig_sign_dw_unit_variance_sample_size_grid.png`
- Commands run:

```powershell
python manuscript\simulations\sign_dw_unit_variance_noise_grid_figure.py --scenario-set noise
python manuscript\simulations\sign_dw_unit_variance_noise_grid_figure.py --scenario-set nongaussianity --output manuscript\figures\fig_sign_dw_unit_variance_nongaussianity_grid.png --note-output manuscript\simulations\sign_dw_unit_variance_nongaussianity_grid_figure.md --json-output manuscript\simulations\output\sign_dw_unit_variance_nongaussianity_grid_figure.json
python manuscript\simulations\sign_dw_unit_variance_noise_grid_figure.py --scenario-set sample_size --output manuscript\figures\fig_sign_dw_unit_variance_sample_size_grid.png --note-output manuscript\simulations\sign_dw_unit_variance_sample_size_grid_figure.md --json-output manuscript\simulations\output\sign_dw_unit_variance_sample_size_grid_figure.json
python manuscript\simulations\m68_first_shock_evidence.py
```

Interpretation: this is the active diagnostic evidence package after M68. It
uses the unit-variance route with `nu_i=lambda_i(BB')_ii`, displays
first-shock coordinates `(B11,B21)`, profiles `B12`, `B22`, and `lambda`, and
imposes `B11>0`, `B22>0`, `B12<=0`, and `B21>=0` as maintained sign
restrictions. The figure and Monte Carlo cutoffs are pointwise chi-square
diagnostics, not final projected confidence-set critical values.

## M45 Variance-Ratio Evidence Rebuild

- Script: `m45_variance_ratio_evidence.py`
- Note: `m45_variance_ratio_evidence.md`
- Machine-readable output: `output/m45_variance_ratio_evidence.json`
- Command run:

```powershell
python manuscript\simulations\m45_variance_ratio_evidence.py
```

Interpretation: this is historical after M64/M68. It was the lightweight
evidence gate for the M0036 variance-ratio robust DW proposal. It applies the hard relative
covariance-decomposition screen in every accepted-set and truth-inclusion
calculation. Under the primary chi-square convention, the high Gaussian-noise
row gives standard-DW truth inclusion 0.000 and variance-ratio robust-DW truth
inclusion 0.875, with robust truth-feasible rate 0.958.

## M29 Refreshed Chi-Square-Primary Monte Carlo Pass

Historical note: M29 used the superseded diagonal-anchor robust row. The active
variance-ratio evidence gate is M45 above.

- Script: `m29_calibrated_monte_carlo.py`
- Note: `m29_calibrated_monte_carlo.md`
- Machine-readable output: `output/m29_calibrated_monte_carlo.json`
- Command run:

```powershell
python manuscript\simulations\m29_calibrated_monte_carlo.py --calibration-reps 120 --evaluation-reps 60 --bootstrap-reps 20 --grid-points 41
```

Interpretation: this refreshed M29 pass keeps the M0030 revised B-plane and
reports the M27 metric bundle under four pointwise cutoff conventions. It is
historical for the current robust row because M0034-M0036 superseded the
diagonal-anchor statistic. M45 reuses the reporting metrics for the
variance-ratio Monte Carlo rebuild.

## M67 Unit-Variance Projected Figure 1

- Script: `sign_dw_unit_variance_noise_grid_figure.py`
- Note: `sign_dw_unit_variance_noise_grid_figure.md`
- Machine-readable output: `output/sign_dw_unit_variance_noise_grid_figure.json`
- Output figure: `../figures/fig_sign_dw_unit_variance_noise_grid.png`
- Command run:

```powershell
python manuscript\simulations\sign_dw_unit_variance_noise_grid_figure.py
```

Interpretation: this is historical after M68. M67 projected accepted
candidates onto `(B12,B21)` while profiling positive `B11`, `B22`, and
`lambda in [0,rho]^2`; the robust row set `nu_i=lambda_i (B B')_ii` and
evaluated the Section 4 moment vector. M68 keeps the same unit-variance route
but changes the active chart to first-shock coordinates `(B11,B21)`, profiles
`B12`, `B22`, and `lambda`, and adds the maintained `B12<=0` sign restriction.

## M0036 Relative-Noise Robust Figure 1 Candidate

- Script: `sign_dw_robust_noise_grid_figure.py`
- Note: `sign_dw_relative_noise_robust_grid_figure.md`
- Output figure: `../figures/fig_sign_dw_relative_noise_robust_grid.png`
- Command run:

```powershell
python manuscript\simulations\sign_dw_robust_noise_grid_figure.py --robust-mode relative
```

Interpretation: this is now historical after M64/M66/M68. The robust-DW row uses the pure five-moment
higher-cumulant J statistic and adds a candidate-specific
covariance-decomposition screen requiring
`0 <= nu_i <= 0.5 Var(epsilon_i)`. In the high-noise column, true `B0` remains
inside and the relative row accepts 0.071 of the full plotted grid. The
precision comes from explicit signal-to-noise information, not from a DW
moment. M45 supplies a historical lightweight validation and Monte Carlo
rebuild; active unit-variance diagnostics now use M68 Figures 1-3 and Table 1.

## M0035 Absolute-Bound Robust Figure 1 Comparison

- Script: `sign_dw_robust_noise_grid_figure.py`
- Note: `sign_dw_bounded_noise_robust_grid_figure.md`
- Output figure: `../figures/fig_sign_dw_bounded_noise_robust_grid.png`
- Command run:

```powershell
python manuscript\simulations\sign_dw_robust_noise_grid_figure.py --robust-mode bounded
```

Interpretation: this comparison uses the absolute `0 <= nu_i <= 0.5` noise
variance cap. It is no longer the preferred candidate because the cap is
scale-arbitrary relative to the M0036 signal-to-noise screen.

## M0034 Pure Robust Figure 1 Diagnostic

- Script: `sign_dw_robust_noise_grid_figure.py`
- Note: `sign_dw_pure_robust_noise_grid_figure.md`
- Output figure: `../figures/fig_sign_dw_pure_robust_noise_grid.png`
- Command run:

```powershell
python manuscript\simulations\sign_dw_robust_noise_grid_figure.py --robust-mode pure
```

Interpretation: this diagnostic drops all second-order anchors from the robust
row. In the high-noise column, true `B0` remains inside but the accepted share
rises to 0.459 of the full plotted grid, showing the precision cost of using
only valid higher-cumulant moments.

## M43 Non-Gaussianity Companion Grid

- Script: `sign_dw_robust_nongaussianity_grid_figure.py`
- Note: `sign_dw_robust_nongaussianity_grid_figure.md`
- Output figure: `../figures/fig_sign_dw_robust_nongaussianity_grid.png`
- Command run:

```powershell
python manuscript\simulations\sign_dw_robust_nongaussianity_grid_figure.py
```

Interpretation: this companion grid is historical after M68. It fixes residual noise at `V=(0.2,0.2)` and
weakens structural-shock non-Gaussianity across columns. All rows invert
pointwise 10 percent J tests. Its robust row now uses the M0036 variance-ratio
proposal: pure mixed higher-cumulant J inversion plus the relative
covariance-decomposition screen.

## M44 Sample-Size Grid

- Script: `sign_dw_sample_size_robust_grid_figure.py`
- Note: `sign_dw_sample_size_robust_grid_figure.md`
- Output figure: `../figures/fig_sign_dw_sample_size_robust_grid.png`
- Command run:

```powershell
python manuscript\simulations\sign_dw_sample_size_robust_grid_figure.py
```

Interpretation: this Figure 3 is historical after M68. It fixes strong structural non-Gaussianity and
moderate residual noise, then varies `T=500`, `T=1000`, and `T=2000`. In the
rendered fixed draw, standard DW misses the true normalized impact at larger
sample sizes while variance-ratio robust DW remains truth-containing.

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

Interpretation: this is the superseded M0030 diagonal-anchor figure. All rows
invert pointwise 10 percent J tests, but M0034 invalidated the robust-row
off-diagonal covariance anchor under the old `diag(B)=1` scale. Use the M68
unit-variance script, not this script, for the active figures.

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
