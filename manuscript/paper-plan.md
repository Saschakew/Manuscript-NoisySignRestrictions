# Paper Plan

## Working Title

Noise-Robust Sign-Restricted SVARs

## Main Idea

The paper studies the simultaneous SVAR impact problem that arises after a
reduced-form residual has been obtained: what happens when applied researchers
combine sign restrictions with Drautzburg-Wright-style higher-moment
refinements while those residuals contain additive noise. The paper does not
model VAR lag dynamics. The standard sign-restricted set rotates a factor of
the noisy covariance, so it targets a pseudo-set. Standard
Drautzburg-Wright refinement then appears to sharpen that pseudo-set, but the
smaller accepted set can be an artifact of misspecification rather than more
efficient structural learning.

The constructive contribution is a robustness check: compute the standard
Drautzburg-Wright set and compute a noise-robust higher-moment set that drops
second-moment restrictions. When the two sets agree, the usual refinement is
less suspicious. When they diverge, residual noise or another covariance-target
misspecification is indicated, and the robust set is the safer object.

The paper's visual spine is now the M0020 grid pair. The first grid varies
residual noise and shows the main warning: noisy covariance moves the sign set,
standard DW can reject the true normalized `B0`, and robust DW remains wider
and contains it. The companion grid fixes residual noise and weakens structural
non-Gaussianity, showing the honest limitation: robust DW is not magic; when
higher moments carry little information, the robust set becomes wide.
The first M28 validation pass supports this grid-pair story with exact
population moment diagnostics, grid-boundary checks, repeated finite-sample
seeds, and pointwise critical-value sensitivity. M27 now fixes the comparison
language: standard-DW accepted mass outside the robust-DW set is the
directional warning metric, while robust-DW mass outside standard DW mainly
records the information lost by dropping second moments. M29 has added an
expanded calibrated Monte Carlo pass; it supports the high-noise divergence
story, shows the standard-DW cutoff inflation required to cover the truth, and
shows that truth-point residual bootstrap restores truth inclusion only by
widening the reported sets. It is not yet the final manuscript table.

## Why It Matters

Sign restrictions are qualitative, but the object being rotated is not. In the
usual no-noise model, the reduced-form covariance equals `B0 B0'`, so a
covariance factor can be rotated into candidate structural impacts. With
additive residual noise,

```text
Sigma_u = B0 B0' + V,
```

so the standard sign-restricted set is built from the wrong covariance object.
This can move sign boundaries, deform accepted regions, and make economically
meaningful columns disappear from the reported set.

Higher moments do not automatically fix the problem. The usual
Drautzburg-Wright procedure refines sign-admissible no-noise candidates by
testing independence of recovered shocks. Under residual noise, those recovered
objects are not the true structural shocks. Asymptotically, the no-noise DW set
may become empty; in finite samples, it can become small and look precise
because the least-misspecified candidates are being selected.

The robust alternative keeps the useful higher-moment idea but removes the
fragile covariance step. It searches over normalized impact matrices, imposes
economic signs directly on those matrices, and uses higher-order cumulants of
candidate transformed residuals written as GMM-style moment equations. The
robust set deliberately gives up second-moment information, so it should often
be wider than the standard DW set. That width is the price of not pretending
that the noisy covariance is structural.

## Proposed Structure

1. Introduction: present the puzzle that sign restrictions can look more
   precise after higher-moment refinement even when residual noise has
   misspecified the no-noise target. State the robustness-check idea.
2. Noisy sign-restricted sets: define the additive-noise SVAR, show that the
   standard sign set rotates a factor of `B0 B0' + V`, and give an intuitive
   visual figure of sign-boundary movement or set deformation.
3. Standard DW under residual noise: explain the no-noise DW refinement, show
   why the recovered shocks are contaminated under noise, and state the
   planned result that the population DW set should generally be empty under
   misspecification, with finite-sample regions shrinking around
   least-rejected pseudo-candidates.
4. Robust DW higher-moment set: define the normalized robust candidate space,
   write the higher-cumulant restrictions as moment equations, and explain why
   second moments are excluded as structural restrictions. State the local
   identification and consistency claims only after audit.
5. Figure-led evidence and Monte Carlo robustness check: use the M0020 grid
   pair as the reader's main visual guide. First show the residual-noise grid
   that moves the sign set, makes standard DW reject the truth in the high-noise
   column, and leaves robust DW wider. Then show the non-Gaussianity grid that
   makes weak higher moments visible. Use population-grid and Monte Carlo
   checks to validate, calibrate, and summarize the same story.
6. Conclusion: recommend reporting the robust DW set beside the standard DW
   set as a diagnostic for covariance-target misspecification. Defer empirical
   applications.

## Key Model Or Notation

- Observed residual model:
  `u_t = B0 epsilon_t + eta_t`, `E[epsilon_t epsilon_t'] = I`,
  `E[epsilon_t eta_t'] = 0`, and `E[eta_t eta_t'] = V`.
- Scope convention:
  treat `u_t` as the simultaneous residual/impact object. The first paper does
  not specify or estimate lag matrices, dynamic responses, or horizon-specific
  sign restrictions.
- Standard sign set:
  `B_*(Q) = P_* Q`, where `P_* P_*' = Sigma_u = B0 B0' + V` and
  `R(P_* Q) >= 0`.
- No-noise economic sign set:
  `P_0 P_0' = B0 B0'`, with `R(P_0 Q) >= 0`.
- Standard DW set:
  sign-admissible covariance-factor rotations whose recovered shocks pass
  no-noise higher-moment independence restrictions.
- Robust DW candidate:
  a normalized impact matrix `B` not required to satisfy `B B' = Sigma_u`.
- Robust DW transformed residual:
  `z_t(B) = B^{-1} u_t`.
- Robust DW moment stack:
  mixed third central moments and fourth cumulants of `z_t(B)`, written as raw
  moment equations with covariance products subtracted.
- Robustness check:
  compare the standard DW accepted set with the robust DW accepted set in the
  common normalized chart. Report accepted shares, overlap, standard-DW mass
  outside robust-DW, and truth inclusion in simulations. Agreement supports the
  usual refinement; standard-DW mass outside robust-DW warns that the usual
  refinement may be reacting to residual noise or covariance-target
  misspecification.

## Main Results To Prove Or Demonstrate

- Proposition 1, noisy sign pseudo-set: if `V != 0`, the population sign set
  based on `Sigma_u` generally differs from the no-noise economic sign set.
  This result should be explained visually before the algebra.
- Proposition 2, standard DW is misspecified under residual noise: recovered
  shocks from noisy covariance-factor candidates are not the structural shocks.
  The M25 derivation shows that, under a rich independence/J-test inversion and
  generic residual noise, the population accepted set is empty; with special
  structural-coordinate rescaling cases or finite-moment aliases, the set can
  instead contain pseudo-true candidates. Finite-sample inversion can still
  return a falsely narrow least-rejected region.
- Proposition 3, robust DW higher moments: under the maintained robust-noise
  conditions, the higher-cumulant moment stack for `z_t(B)` has zero
  population value at the true normalized impact matrix, while no-noise second
  moment restrictions do not.
- Proposition 4, robust set comparison: M27 formalizes the diagnostic in
  `manuscript/derivations/dw-robust-comparison-diagnostic.md`. The key warning
  is directional: standard-DW accepted mass outside robust-DW indicates that
  apparent no-noise covariance-target precision may not be robust, while
  robust-DW mass outside standard DW usually reflects the information
  deliberately lost by dropping second moments. The comparison is a warning,
  not literal proof of measurement error.
- Simulation result: the M0020 grid pair should become the main evidence
  figure package if validation passes. Monte Carlo evidence should then
  quantify the same visual story: sign-set bias, standard DW false-sharpening
  or truth rejection under residual noise, robust DW widening under noise, and
  robust DW loss of information under weak or Gaussian higher moments.

## Evidence Plan

- Main visual figure 1, residual-noise grid: show three rows
  (sign/covariance, standard DW, robust DW) across increasing Gaussian residual
  noise. The high-noise column should remain the narrative anchor where
  standard DW rejects true `B0` and robust DW contains it.
- Main visual figure 2, non-Gaussianity grid: hold residual noise fixed and
  weaken structural-shock higher moments. Use it to show that robust DW becomes
  wide as the identifying higher-moment signal weakens and becomes
  uninformative in the Gaussian limit.
- Validation grid checks: M28 reran the same story on population and
  repeated-draw grids, checking that the visual is not an artifact of one seed,
  one grid boundary, or the pointwise chi-square cutoff.
- Monte Carlo table: M29's expanded pass reports true-`B0` coverage-style
  inclusion, accepted-set share, empty-set frequency, standard-DW versus
  robust-DW overlap, the M27 directional divergence metric, and
  least-rejected candidates across no-noise, moderate-noise, high-noise,
  weak-moment, Gaussian-shock, and skewed-residual-noise stress cases. It
  compares chi-square, no-noise repeated, oracle scenario truth, and
  truth-point residual-bootstrap cutoffs. A final table still needs a larger
  run and a final calibration convention.
- Stress cases: weak higher moments, near-Gaussian structural shocks, high
  noise, non-Gaussian noise that violates the robust route if Gaussianity is
  maintained, anisotropic noise, near-boundary signs, and small macro samples.

## What Is Missing

- A final calibrated finite-sample evidence pass for the M0020 grid pair:
  M29 has repeated-sample and truth-point residual-bootstrap diagnostics, but
  final draft claims still need a larger run, a final calibration convention,
  true-`B0` coverage, accepted-set width, empty-set frequency, overlap, and
  divergence diagnostics.
- A decision on the precise robust noise assumption: Gaussian additive noise is
  clean for transformed cumulants; broader non-Gaussian noise would need a
  different argument.
- A self-contained simulation package that builds the sign-bias, DW-shrinkage,
  and robust-DW comparison figures from this repository.
- A figure-led first draft once M29 finalizes the grid-pair evidence enough to
  avoid another structural rewrite, plus a concise literature-positioning
  paragraph distinguishing the paper from
  Drautzburg-Wright, sign-restriction inference, and higher-moment SVAR GMM.

## Page Budget And Scope Exclusions

Target: short theory-and-simulation paper, about 18-24 manuscript pages before
appendix.

Excluded from the first version:

- A full empirical application.
- A general `K`-variable estimator in the main text.
- VAR lag dynamics, lag-coefficient estimation, dynamic responses, and
  horizon-specific sign restrictions.
- Correlated, serially dependent, common-factor, or stochastic-volatility noise.
- A claim that divergence between DW and robust DW proves literal measurement
  error. It is a robustness warning inside the maintained model.

## Scope Recommendation

Keep the paper as one clean robustness-check story:

1. Noise biases the standard sign-restricted set.
2. Standard DW refinement can falsely sharpen the misspecified set.
3. A robust DW higher-moment set drops second moments and should be wider.
4. Comparing the two sets gives a practical diagnostic.
5. Simulations carry the evidence burden; no application is needed yet.
