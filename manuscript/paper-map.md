# Paper Map

Purpose: compact macro control surface for the manuscript. Read this before
changing section structure or drafting substantial prose.

## One-Sentence Claim

Residual noise can bias standard sign-restricted SVAR sets and make
Drautzburg-Wright-style higher-moment refinement look falsely precise; a
noise-robust higher-moment set that drops second-moment restrictions should be
reported beside the standard DW set as a practical robustness check.

## Paper Contract

- Paper type: short theory-and-simulation note.
- Scope: bivariate simultaneous impact model in the main text. Treat the
  reduced-form residual `u_t` as given; omit VAR lag dynamics, dynamic impulse
  responses, horizon-specific sign restrictions, and `K > 2` extensions.
- Benchmark: standard sign-restricted covariance rotations and
  Drautzburg-Wright-style no-noise higher-moment refinement.
- Constructive object: robust DW-style higher-moment set over normalized impact
  matrices, using higher cumulants written as GMM-style moment equations and
  excluding second moments as structural restrictions.
- Evidence: analytical J-test inversion result, then an early lightweight
  Monte Carlo overview before polished figures; final evidence only if useful:
  intuitive geometry figure, standard DW misspecification figure, robust-DW
  comparison figure, and Monte Carlo coverage/width/overlap tables.
- Excluded: first-version empirical application and broad noise models beyond
  the maintained robust-noise assumptions.

## Reader Path

1. The reader is placed directly in the simultaneous impact problem: the VAR
   residual `u_t` is already in hand, sign restrictions filter rotations of a
   covariance factor, and DW uses higher moments to refine a sign-admissible
   set.
2. The problem appears when observed residuals are `B0 epsilon_t + eta_t`:
   the covariance factor is built from `B0 B0' + V`, so the sign set is already
   a noisy pseudo-set.
3. DW-style refinement does not automatically fix this, because recovered
   shocks from the noisy candidate system are not the structural shocks.
   Finite samples may produce a narrow least-rejected set that looks efficient
   but is actually misspecified.
4. The paper's constructive move is to drop second-moment restrictions and use
   robust higher-moment restrictions on normalized candidate impacts.
5. The practical recommendation is simple: report both the standard DW set and
   the robust DW set. Agreement is reassuring; divergence is a warning that the
   usual covariance-target refinement should not be trusted.

## Section Jobs

| Section | Job | Status |
|---|---|---|
| Abstract | State noisy sign-set bias, false DW sharpening, robust DW comparison, and no-application scope. | planned |
| 1. Introduction | Motivate the robustness-check problem and preview the geometry plus Monte Carlo evidence. | planned |
| 2. Noisy Sign Sets | Define the additive-noise SVAR and show, visually and algebraically, how standard sign sets become biased pseudo-sets. | planned |
| 3. Standard DW Under Noise | Explain the no-noise DW refinement, why noise contaminates recovered shocks, and why the refined set can become empty or falsely small. | planned |
| 4. Robust DW Higher Moments | Define the robust normalized candidate set, write cumulant restrictions as moment equations, and explain why second moments are dropped. | planned |
| 5. Monte Carlo Robustness Check | Compare standard sign, standard DW, and robust DW sets across no-noise, noisy, weak-moment, and misspecified cases. | planned |
| 6. Conclusion | Recommend the DW-versus-robust-DW comparison as a robustness check and state limitations. | planned |

## Core Formal Objects

- `def:diagonal-noise-svar`
- `ass:gaussian-residual-noise`
- `ass:unit-variance-normalization`
- `def:noisy-sign-pseudo-set`
- `def:standard-dw-refined-set`
- `def:robust-dw-higher-moment-set`
- `eq:column-rescaling-obstruction`
- `eq:dw-higher-cumulant-moment-stack`
- `prop:noisy-sign-pseudo-set`
- `prop:standard-dw-misspecification`
- `prop:robust-dw-higher-moment-validity`
- `prop:dw-robust-comparison-diagnostic`
- `fig:sign-noise-geometry`
- `fig:standard-dw-false-sharpening`
- `fig:dw-robust-set-comparison`
- `table:monte-carlo-coverage-width`
- `audit:robust-dw-derivation`
- `audit:dw-noise-simulation-design`

See `formal-object-registry.json` for exact labels, dependencies, locations,
and proof or output status.

## Main Evidence

- Intuitive sign-noise geometry figure showing covariance deformation and
  sign-set bias.
- Algebraic proof of the covariance pseudo-set and column-rescaling
  obstruction.
- M25 working derivation showing that standard DW recovered-shock restrictions
  are misspecified under residual noise, with the J-test inversion stated as
  generic emptying plus explicit pseudo-zero exceptions.
- Derivation of the robust higher-moment stack from
  `derivations/dw-noise-robust-moments.md`.
- Early Monte Carlo overview and the M0016 candidate population figure after
  the analytical J-test result to decide whether the project is worth deeper
  figure and replication investment.
- Monte Carlo comparison of standard sign, standard DW, and robust DW sets.
- Stress cases that show honest widening, weak-moment uncertainty, and
  divergence diagnostics.

## Current Bottlenecks

- The standard DW J-test inversion result is now a working derivation; it still
  needs audit before prose promotion.
- M35/M30 and M0016 provide exploratory evidence and visuals only. M28
  population-grid checks remain the immediate gate before polished figures or
  final finite-sample Monte Carlo tables.
