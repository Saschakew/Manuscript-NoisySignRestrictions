# Sign, Standard DW, And Robust DW Noise Figure

Status: exploratory manuscript-local figure candidate.

Source context:

- KnowledgeVault synthesis:
  `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md`
- KnowledgeVault visualization lab:
  `replications/svar-noise-recursive-sign-visualization/noisy_svar_visuals.py`
- Manuscript script:
  `manuscript/simulations/sign_dw_robust_noise_figure.py`
- Output figure:
  `manuscript/figures/fig_sign_dw_robust_noise_comparison.png`

Command:

```powershell
python manuscript\simulations\sign_dw_robust_noise_figure.py
```

## DGP

The standard sign and DW panels use the recursive bivariate calibration from
the KnowledgeVault visualization:

```text
B0 = [[1, 0],
      [0.7, 1]]
```

Residual noise varies as

```text
V = diag(nu1, 0)
```

The sign restriction is that the second response of the target rotated column
is nonnegative. The standard DW filter is a population higher-moment score over
sign-admissible covariance rotations. The score uses two co-skewness moments
and one co-kurtosis moment of the recovered shocks.

The robust-DW panel uses the normalized impact chart

```text
B(a,b) = [[1, a],
          [b, 1]]
```

with true shape `(a0, b0) = (0, 0.7)`. The robust score uses only mixed higher
cumulants of `B(a,b)^{-1}u`. Gaussian residual noise does not enter this score
because it has zero cumulants above order two after linear transformations.

## What The Panels Show

1. The left panel reproduces the standard-DW sign-restriction noise logic:
   blank regions fail the sign restriction, and the cyan contour marks the
   fixed-cutoff standard-DW higher-moment accepted set.
2. The middle panel summarizes the same object as widths: the sign-only angle
   set remains large, while the standard-DW accepted subset can empty over an
   intermediate noise range and reopen when the residuals become noise
   dominated.
3. The right panel adds the robust-DW normalized set. Under Gaussian residual
   noise, the accepted robust higher-cumulant region is unchanged by `nu1` and
   remains centered around the true normalized shape.

## Interpretation

This figure is useful for the manuscript's intuition: standard sign and
standard DW are tied to noisy covariance rotations, while robust DW gives up
second-moment restrictions and therefore does not move with Gaussian residual
noise variance in this population construction.

It is not final evidence. The robust panel is a population higher-cumulant
score with an illustrative cutoff, and the standard-DW panel is a deterministic
population score. M28 should still run formal population-grid verification for
the actual robust-DW/statistical comparison before this becomes a polished
paper figure.
