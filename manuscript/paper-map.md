# Paper Map

Purpose: compact macro control surface for the manuscript. Read this before
changing section structure or drafting substantial prose.

## One-Sentence Claim

Sign-restricted SVARs with idiosyncratic residual noise rotate a noisy
covariance factor rather than the structural covariance, so no-noise
independence refinements can create false finite-sample precision; the
constructive claim is a to-be-verified Bonhomme-Robin-style profiled cumulant
inversion, not a direct import of the full Bonhomme-Robin quasi-JADE theorem.

## Paper Contract

- Paper type: short theory-and-simulation note.
- Scope: bivariate diagonal-normalized impact model in the main text, with
  dynamic signs and `K > 2` treated as appendix/follow-up.
- Benchmark or setting: standard sign-restricted covariance rotations and
  Drautzburg-Wright-style no-noise independence refinement.
- Evidence: formal results plus deterministic geometry and Monte Carlo figures,
  with the BR-style result gated by independent derivation, population checks,
  finite-sample simulations, and adversarial reviews.
- Excluded: first-version empirical application, correlated or serially
  dependent noise, common stochastic volatility, nonlinear shock models, and a
  full reusable package implementation.

## Reader Path

1. The reader knows that sign restrictions filter orthogonal rotations of a
   reduced-form covariance factor and usually leave an admissible set.
2. The problem appears when observed residuals are `B0 epsilon_t + eta_t`:
   the covariance factor is built from `B0 B0' + V`, so even economically
   correct signs are imposed on a noisy pseudo-object.
3. Adding no-noise independence tests helps diagnose misspecification when
   powerful, but under residual noise the recovered shocks are mixtures of
   more primitive sources than the model allows; finite samples can leave a
   narrow least-rejected set.
4. The paper's move is to separate labeling from denoising, but to verify the
   denoising logic itself: derive the bivariate cumulant equations, profile
   nuisance structural and noise cumulants, use signs only to label columns,
   then map accepted matrices into implied diagonal noise.
5. The limitation is part of the result: high-order moments can be weak, the
   diagnostic is conditional on diagonal-noise and normalization assumptions,
   and honest weak sets are preferable to pseudo-precision.

## Section Jobs

| Section | Job | Status |
|---|---|---|
| Abstract | State the pseudo-set warning, false-precision channel, BR fix, and limitation. | planned |
| 1. Introduction | Motivate why sign restrictions are qualitative but their covariance factor is not; preview the fair critique and constructive fix. | planned |
| 2. Noisy Sign Sets | Define the diagonal-noise SVAR and prove the noisy pseudo-set and rescaling obstruction. | planned |
| 3. No-Noise Independence Refinement | Explain generic failure of recovered-shock independence and the finite-sample least-rejected-region risk. | planned |
| 4. BR-Style Profiled Inversion | Correct the BR analogy, derive the bivariate cumulant system, classify clean versus nuisance moments, and state only verified rank/consistency claims. | planned |
| 5. Verification And Evidence | Use analytic checks, population grids, finite-sample simulations, and adversarial DGPs before interpreting the noise diagnostic. | planned |
| 6. Conclusion | State what the paper teaches and what remains outside the maintained model. | planned |

## Core Formal Objects

- `def:diagonal-noise-svar`
- `def:noisy-sign-pseudo-set`
- `def:no-noise-independence-refined-set`
- `def:br-sign-inverted-set`
- `def:br-profiled-cumulant-system`
- `def:mapped-noise-set`
- `def:restricted-no-noise-j-test`
- `ass:diagonal-idiosyncratic-noise`
- `ass:unit-variance-normalization`
- `ass:br-local-rank`
- `audit:br-applicability`
- `audit:br-derivation-adversarial-review`
- `audit:br-simulation-adversarial-review`
- `prop:noisy-sign-pseudo-set`
- `prop:generic-empty-independence-refinement`
- `prop:robust-sign-inversion`
- `prop:consistent-noise-diagnostic`
- `fig:sign-noise-geometry`
- `fig:independence-refinement-noise`
- `fig:br-robust-set-and-noise-map`
- `fig:noise-path-diagnostic`

See `formal-object-registry.json` for exact labels, dependencies, locations, and
proof or output status.

## Main Evidence

- Proof of the covariance pseudo-set and generic column-rescaling obstruction.
- Bivariate Darmois-Skitovich-style proof sketch for generic no-noise
  independence-refinement failure under extra diagonal noise sources.
- Self-derived BR-style profiled cumulant map, determinant condition, and local
  rank condition; do not cite the original BR theorem as the proof.
- Deterministic sign-noise geometry figure from
  `replications/svar-noise-recursive-sign-visualization/`.
- Independence-refinement/noise path figure showing empty-set and
  noise-dominated reopening behavior.
- Rebuilt BR-style accepted-set and implied-noise map after symbolic,
  population, and finite-sample verification.
- Weak-cumulant or small-sample stress figure/table to prevent the simulation
  section from reading as a victory lap.

## Current Bottlenecks

- The next writing pass should not start with prose polish. It should first
  derive and adversarially review the BR-style cumulant system, because the
  corrected KnowledgeVault notes show that the earlier BR summary was too
  simple.
