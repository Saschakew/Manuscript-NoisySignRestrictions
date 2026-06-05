# Paper Plan

## Working Title

Noise-Robust Sign-Restricted SVARs

## Main Idea

Sign restrictions are not automatically robust to residual noise: with
diagonal idiosyncratic noise, the standard sign-restricted SVAR rotates a noisy
covariance factor and targets a pseudo-set, while no-noise independence
refinements can create false finite-sample precision. A
Bonhomme-Robin-style inversion that uses clean cross covariance and mixed
higher cumulants gives the right target and turns the contaminated own
variances into a noise diagnostic.

## Why It Matters

Sign restrictions are often treated as a relatively agnostic economic labeling
device. That agnosticism is about inequalities, not about the covariance object
being rotated. If residual noise adds diagonal variance, then the accepted
rotations are factors of `B0 B0' + V`, not factors of `B0 B0'`. Adding
higher-moment independence tests can diagnose this misspecification when they
are powerful, but a small nonempty finite-sample accepted set may be the
least-rejected region of a false no-noise model rather than evidence of sharp
structural learning.

The constructive value is that the same higher-moment idea can be redirected:
use the mixed cumulants that diagonal idiosyncratic noise cannot contaminate,
profile structural cumulants, impose signs only as labels, and report weakness
honestly when the clean moments are weak.

## Proposed Structure

1. Introduction: qualitative sign restrictions are not enough if the covariance
   factor itself is noisy; state the warning, the fair interpretation of
   independence refinement, and the robust alternative.
2. Noisy sign-restricted population object: define the diagonal-noise SVAR and
   prove that the sign-only set is a pseudo-set built from `B0 B0' + V`;
   include the positive column-rescaling obstruction.
3. No-noise independence refinement under residual noise: explain why recovered
   shocks are mixtures of more primitive sources than observed coordinates;
   state a generic emptiness result and the finite-sample false-precision
   channel.
4. Noise-robust sign inversion: define the bivariate diagonal-normalized
   Bonhomme-Robin-style moment set using `sigma_12` and mixed fourth cumulants,
   profile structural cumulants, intersect with signs, and state consistency
   under the local rank condition.
5. Noise diagnostic and evidence: map the robust accepted set into implied
   diagonal noise variances; show favorable, weak-moment, Gaussian-noise, and
   misspecification/stress cases using the existing vault simulations.
6. Conclusion: sign restrictions still label shocks, but the covariance and
   moment target must match the residual-noise model.

## Key Model Or Notation

- Observed residual model:
  `u_t = B0 epsilon_t + eta_t`, `E[epsilon_t epsilon_t'] = I`,
  `E[eta_t eta_t'] = V = diag(nu_1,...,nu_K)`, and
  `E[epsilon_t eta_t'] = 0`.
- Standard sign set:
  `B_*(Q) = P_* Q`, where `P_* P_*' = B0 B0' + V` and `R(P_* Q) >= 0`.
- No-noise economic sign set:
  `P_0 P_0' = B0 B0'`, `R(P_0 Q) >= 0`.
- Independence-refined no-noise set:
  accepted rotations for which `B^{-1} u_t` appears mutually independent.
- Bivariate robust normalized matrix:
  `B(a,b) = [[1, a], [b, 1]]`.
- Clean moment vector:
  `h = (sigma_12, K_1112, K_1122, K_1222)'`.
- Profiled robust criterion:
  `J_BR(a,b) = T min_lambda (h_hat - m(a,b,lambda))' S_hat^{-1}
  (h_hat - m(a,b,lambda))`.
- Mapped noise set:
  `V_T(c) = { (sigma_11 - (1+a^2), sigma_22 - (1+b^2)) :
  B(a,b) in B_BR+sign,T(c) }`.

## Main Results To Prove Or Demonstrate

- Proposition 1, noisy sign pseudo-set: if `V != 0`, the population
  sign-restricted object is built from the noisy covariance and generally
  contains neither `B0` nor a positive column-rescaling `B0 D`.
- Proposition 2, no-noise independence refinement can empty or mislead:
  under independent non-Gaussian structural shocks and diagonal idiosyncratic
  noise, a K-coordinate demixing generally cannot recover mutually independent
  shocks from 2K primitive sources; finite-sample inversion can still leave a
  narrow least-rejected region.
- Proposition 3, robust sign inversion: under diagonal noise, correct signs,
  compactness, nonzero mixed cumulant relevance, and the bivariate local rank
  condition `a0 kappa_42 != b0 kappa_41`, the BR-style sign-intersected
  inversion targets the robust population set and contains `B0`.
- Proposition 4, noise diagnostic: if the robust set is consistent and true
  diagonal noise is bounded away from zero, the mapped noise set excludes the
  no-noise origin with probability approaching one; under `V=0` it covers the
  origin at the intended rate.

## Evidence Plan

- Favorable case: reuse the BR replication calibration
  `(a0,b0)=(-0.45,0.7)` with informative fourth cumulants and diagonal
  Gaussian or skewed noise; show that BR+sign stays centered near `B0` and the
  noise map tracks `V`.
- Failure geometry: reuse deterministic sign-noise figures showing sign
  boundary movement, pseudo covariance ellipses, and the full-matrix
  column-rescaling obstruction.
- Independence-refinement case: show the no-noise independence accepted region
  shrinking, emptying, or reopening around noise-dominated rotations depending
  on noise path and test power.
- Limitation/stress case: weak or near-Gaussian fourth cumulants, small macro
  samples, near-boundary sign restrictions, high noise, and negative implied
  variance regions that indicate the maintained diagonal-noise model may be
  wrong.

## What Is Missing

- A clean proof write-up for the generic independence-refinement result,
  including explicit special cases where it fails.
- A formal statement of the BR consistency result with exact regularity
  conditions and the finite-sample critical-value choice.
- A decision on whether the main text reports only bivariate impact signs or
  also an appendix for dynamic signs and `K > 2`.
- A manuscript-local replication wrapper that rebuilds the selected figures
  without depending on the vault path.
- A first literature-positioning paragraph that distinguishes this paper from
  Drautzburg-Wright, Keweloh higher-moment GMM, and Bonhomme-Robin noisy ICA.

## Page Budget And Scope Exclusions

Target: short theory-and-simulation paper, about 18-24 manuscript pages before
appendix.

Excluded:

- A full empirical application in the first version. Add only after the theory,
  simulation, and diagnostic sections are stable.
- A general `K`-variable estimator in the main text. Keep main exposition
  bivariate and diagonal-normalized; record `K`-variable extension as appendix
  or follow-up.
- Correlated measurement error, common stochastic volatility, serially
  dependent noise, nonlinear shock transformations, and noise in observed VAR
  variables that changes reduced-form slope estimates.
- Treating no-noise independence refinement as wrong. The paper should say it
  is a valid test inversion for its maintained null; the new issue is the
  null's mismatch under residual noise.
- Claiming the noise diagnostic proves literal measurement error. It rejects
  the no-noise SVAR within the maintained robust moment model.

## Scope Recommendation

Revise the first plan down to the narrowest coherent paper:

1. Keep the main text bivariate and impact-oriented.
2. Make the central contribution a three-part sequence: pseudo-set warning,
   false-precision channel for no-noise independence refinement, and
   BR-style sign inversion with a mapped noise diagnostic.
3. Use simulations only to make those three claims legible and falsifiable.
4. Treat empirical work, dynamic signs, and `K > 2` generalization as optional
   later layers rather than first-draft blockers.
