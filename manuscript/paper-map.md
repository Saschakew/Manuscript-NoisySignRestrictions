# Paper Map

Purpose: compact macro control surface for the manuscript. Read this before
changing section structure or drafting substantial prose.

## One-Sentence Claim

Sign-restricted SVARs with idiosyncratic residual noise rotate a noisy
covariance factor rather than the structural covariance, so no-noise
independence refinements can create false finite-sample precision, while a
Bonhomme-Robin-style clean-moment inversion restores the target and yields a
noise diagnostic.

## Paper Contract

- Paper type: short theory-and-simulation note.
- Scope: bivariate diagonal-normalized impact model in the main text, with
  dynamic signs and `K > 2` treated as appendix/follow-up.
- Benchmark or setting: standard sign-restricted covariance rotations and
  Drautzburg-Wright-style no-noise independence refinement.
- Evidence: four formal results plus deterministic geometry and Monte Carlo
  figures reusing the vault's noise and BR inversion replications.
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
4. The paper's move is to separate labeling from denoising: use signs only to
   label columns in a BR-style inversion based on clean cross covariance and
   mixed fourth cumulants, then map accepted matrices into implied diagonal
   noise.
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
| 4. Robust Sign Inversion | Define the BR+sign clean-moment criterion, local rank condition, and consistency target. | planned |
| 5. Noise Diagnostic And Evidence | Map robust sets into noise variance space and show favorable plus stress-case simulations. | planned |
| 6. Conclusion | State what the paper teaches and what remains outside the maintained model. | planned |

## Core Formal Objects

- `def:diagonal-noise-svar`
- `def:noisy-sign-pseudo-set`
- `def:no-noise-independence-refined-set`
- `def:br-sign-inverted-set`
- `def:mapped-noise-set`
- `ass:diagonal-idiosyncratic-noise`
- `ass:unit-variance-normalization`
- `ass:br-local-rank`
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
- BR moment inversion proof sketch and local rank condition.
- Deterministic sign-noise geometry figure from
  `replications/svar-noise-recursive-sign-visualization/`.
- Independence-refinement/noise path figure showing empty-set and
  noise-dominated reopening behavior.
- BR robust accepted-set and implied-noise map from
  `replications/bonhomme-robin-noise-robust-svar/`.
- Weak-cumulant or small-sample stress figure/table to prevent the simulation
  section from reading as a victory lap.

## Current Bottlenecks

- The next writing pass should not start with prose polish. It should first
  turn Proposition 2 and Proposition 3 into exact formal statements with
  assumptions, special cases, and proof obligations.
