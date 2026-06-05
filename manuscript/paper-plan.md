# Paper Plan

## Working Title

Noise-Robust Sign-Restricted SVARs

## Main Idea

Sign restrictions are not automatically robust to residual noise: with
diagonal idiosyncratic noise, the standard sign-restricted SVAR rotates a noisy
covariance factor and targets a pseudo-set, while no-noise independence
refinements can create false finite-sample precision. The constructive part is
now a conjectured and to-be-verified Bonhomme-Robin-style profiled cumulant
inversion: stack the bivariate SVAR cumulant equations, profile structural and
diagonal-noise cumulants, use signs for labels, and test whether the resulting
diagnostics really distinguish no-noise from noisy residuals.

## Why It Matters

Sign restrictions are often treated as a relatively agnostic economic labeling
device. That agnosticism is about inequalities, not about the covariance object
being rotated. If residual noise adds diagonal variance, then the accepted
rotations are factors of `B0 B0' + V`, not factors of `B0 B0'`. Adding
higher-moment independence tests can diagnose this misspecification when they
are powerful, but a small nonempty finite-sample accepted set may be the
least-rejected region of a false no-noise model rather than evidence of sharp
structural learning.

The constructive value is that the same higher-moment idea may be redirected,
but only after verification. Bonhomme-Robin do not simply discard pure own
moments. They identify and subtract error cumulants using clean-pair
restrictions, then identify loadings from denoised cumulants. In the bivariate
`L=K=2` SVAR, the original BR theorem does not apply mechanically, so our paper
must derive the profiled bivariate moment result itself and then check it by
simulation before relying on it.

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
4. Bonhomme-Robin correction and bivariate profiled inversion: explain what BR
   actually identify, state why the bivariate SVAR is only BR-style, derive the
   cumulant map, identify which moments restrict `(a,b)` and which profile
   nuisance noise cumulants, and state the rank condition only after proof.
5. Verification, diagnostics, and evidence: map the verified robust accepted
   set into implied diagonal noise variances; compare it with a restricted
   no-noise J test; show favorable, weak-moment, Gaussian-noise, and
   misspecification/stress cases using newly checked simulations.
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
- Minimal fourth-cumulant vector:
  `h = (sigma_12, K_1112, K_1122, K_1222)'`.
- Minimal profiled robust criterion:
  `J_4(a,b) = T min_kappa (h_hat - m_4(a,b,kappa))' S_hat^{-1}
  (h_hat - m_4(a,b,kappa))`.
- Stacked profiled criterion:
  `J_stack(a,b) = T min_{gamma,kappa,xi_eta} (mu_hat -
  m(a,b,gamma,kappa,xi_eta))' W_hat (mu_hat -
  m(a,b,gamma,kappa,xi_eta))`, where `xi_eta` collects diagonal noise
  cumulants.
- Mapped noise set:
  `V_T(c) = { (sigma_11 - (1+a^2), sigma_22 - (1+b^2)) :
  B(a,b) in B_profiled+sign,T(c) }`.

## Main Results To Prove Or Demonstrate

- Proposition 1, noisy sign pseudo-set: if `V != 0`, the population
  sign-restricted object is built from the noisy covariance and generally
  contains neither `B0` nor a positive column-rescaling `B0 D`.
- Proposition 2, no-noise independence refinement can empty or mislead:
  under independent non-Gaussian structural shocks and diagonal idiosyncratic
  noise, a K-coordinate demixing generally cannot recover mutually independent
  shocks from 2K primitive sources; finite-sample inversion can still leave a
  narrow least-rejected region.
- Proposition 3, bivariate profiled cumulant inversion: after we derive it,
  show that the minimal fourth-cumulant system or the stacked profiled system
  contains `B0` under diagonal noise and locally identifies `(a0,b0)` under
  the rank condition `a0 kappa_2 != b0 kappa_1`, subject to nonsingularity
  `1-a0 b0 != 0`.
- Proposition 4, noise diagnostic: if the robust set is consistent and true
  diagonal noise is bounded away from zero, the mapped noise set excludes the
  no-noise origin with probability approaching one; under `V=0` it covers the
  origin at the intended rate. This remains a planned result until the
  derivation and simulations validate it.

## Bonhomme-Robin Verification Tasks

1. Analytic derivation: write a derivation note for the complete bivariate
   cumulant map through fourth order, including all pure and mixed cumulants.
2. Moment classification: mark each moment as clean restriction, nuisance fit,
   diagnostic, or overidentifying only under extra noise restrictions.
3. BR applicability audit: prove in writing why the original BR clean-pair
   quasi-JADE rank condition is not the theorem for `L=K=2`.
4. Local identification proof: rederive the determinant condition, tangent,
   and rank condition from the cumulant map; check every algebraic sign and
   factor.
5. Criterion audit: distinguish `J_4`, `J_stack`, mapped variance diagnostics,
   and restricted no-noise J tests; specify which statistic answers which
   question.
6. Simulation verification: implement symbolic/population/finite-sample tests
   before reusing the existing figures as manuscript evidence.
7. Adversarial result audit: run a formal review after each derivation and
   simulation stage, recording mistakes, undefined objects, and story failures
   in `review-log.md`.

## Evidence Plan

- Favorable case: after derivation, reuse or rebuild the BR replication
  calibration
  `(a0,b0)=(-0.45,0.7)` with informative fourth cumulants and diagonal
  Gaussian or skewed noise; show that the profiled sign-intersected set stays
  centered near `B0` only when the verified rank and nuisance conditions hold,
  and that the noise map tracks `V`.
- Failure geometry: reuse deterministic sign-noise figures showing sign
  boundary movement, pseudo covariance ellipses, and the full-matrix
  column-rescaling obstruction.
- Independence-refinement case: show the no-noise independence accepted region
  shrinking, emptying, or reopening around noise-dominated rotations depending
  on noise path and test power.
- Limitation/stress case: weak or near-Gaussian fourth cumulants, exact rank
  failure, small macro samples, near-boundary sign restrictions, high noise,
  negative implied variance regions, non-diagonal noise, mis-normalized shock
  variances, and noise restrictions that make pure moments misleading.

## What Is Missing

- A clean proof write-up for the generic independence-refinement result,
  including explicit special cases where it fails.
- A self-contained derivation of the BR-style bivariate result. The updated
  KnowledgeVault notes make clear that this cannot be imported directly from
  Bonhomme-Robin's full quasi-JADE theorem.
- A formal statement of the profiled inversion consistency result with exact
  regularity conditions, nuisance treatment, and finite-sample critical-value
  choice.
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
3. Use simulations as verification gates, not decoration: the BR-style result
   should not become a manuscript claim until analytic and simulation checks
   agree.
4. Treat empirical work, dynamic signs, and `K > 2` generalization as optional
   later layers rather than first-draft blockers.
