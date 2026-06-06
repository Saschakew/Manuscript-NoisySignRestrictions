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
- Evidence: the M0020 grid pair is the visual spine. The residual-noise grid
  shows sign-set movement, standard-DW truth rejection, and robust-DW widening;
  the non-Gaussianity grid shows why robust DW becomes wide when higher moments
  weaken. M28 validates the first population/repeated-seed layer of this story;
  M29 now adds a first calibrated finite-sample pass, while final evidence
  still needs larger or bootstrap-calibrated critical values.
- Excluded: first-version empirical application and broad noise models beyond
  the maintained robust-noise assumptions.

## Reader Path

1. The reader is placed directly in the simultaneous impact problem: the VAR
   residual `u_t` is already in hand, sign restrictions filter rotations of a
   covariance factor, and DW uses higher moments to refine a sign-admissible
   set.
2. The residual-noise grid makes the problem visual: the covariance factor is
   built from `B0 B0' + V`, so the sign set moves with noise.
3. Standard DW-style refinement does not automatically fix this. In the
   high-noise grid column, it rejects true `B0` while looking precise.
4. The paper's constructive move is to drop second-moment restrictions and use
   robust higher-moment restrictions on normalized candidate impacts. The same
   grid shows the robust set remains wider and contains the truth.
5. The companion non-Gaussianity grid states the limitation honestly: robust DW
   depends on informative higher moments and becomes wide when the shocks are
   close to Gaussian.
6. The practical recommendation is simple: report both the standard DW set and
   the robust DW set in the same normalized chart. Standard-DW mass outside the
   robust set is the warning object; robust mass outside the standard set often
   just records the information lost by dropping second moments.

## Section Jobs

| Section | Job | Status |
|---|---|---|
| Abstract | State noisy sign-set bias, false DW sharpening, robust DW comparison, and no-application scope. | planned |
| 1. Introduction | Motivate the robustness-check problem and preview the geometry plus Monte Carlo evidence. | planned |
| 2. Noisy Sign Sets | Define the additive-noise SVAR and show, visually and algebraically, how standard sign sets become biased pseudo-sets. | planned |
| 3. Standard DW Under Noise | Explain the no-noise DW refinement, why noise contaminates recovered shocks, and why the refined set can become empty or falsely small. | planned |
| 4. Robust DW Higher Moments | Define the robust normalized candidate set, write cumulant restrictions as moment equations, and explain why second moments are dropped. | planned |
| 5. Figure-Led Evidence And Monte Carlo Check | Use the two M0020 grids as the main visual story, then validate and quantify the same claims with population-grid and Monte Carlo checks. | planned |
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
- `eq:dw-robust-directional-overlap`
- `fig:sign-noise-geometry`
- `fig:standard-dw-false-sharpening`
- `fig:dw-robust-set-comparison`
- `table:monte-carlo-coverage-width`
- `audit:robust-dw-derivation`
- `audit:dw-noise-simulation-design`

See `formal-object-registry.json` for exact labels, dependencies, locations,
and proof or output status.

## Main Evidence

- M0020 residual-noise grid showing covariance/sign-set movement, standard-DW
  truth rejection under high residual noise, and robust-DW truth inclusion.
- M0020 non-Gaussianity grid showing robust-DW widening as higher moments
  weaken and the Gaussian limit becomes uninformative.
- Algebraic proof of the covariance pseudo-set and column-rescaling
  obstruction.
- M25 working derivation showing that standard DW recovered-shock restrictions
  are misspecified under residual noise, with the J-test inversion stated as
  generic emptying plus explicit pseudo-zero exceptions.
- Derivation of the robust higher-moment stack from
  `derivations/dw-noise-robust-moments.md`.
- M28 population-grid and repeated-draw validation of the M0020 grid pair.
- M27 formal diagnostic note defining the reported standard-DW set, robust-DW
  set, critical-value convention, directional overlap metric, and interpretation
  boundaries.
- M29 first calibrated Monte Carlo pass comparing standard DW and robust DW
  sets using the grid pair's scenarios plus weak-moment, Gaussian-shock, and
  skewed-residual-noise stress cases.
- Final Monte Carlo comparison of standard sign, standard DW, and robust DW
  sets using the grid pair's scenarios as the main design.
- Stress cases that quantify honest widening, weak-moment uncertainty, and
  divergence diagnostics.

## Current Bottlenecks

- The standard DW J-test inversion result is now a working derivation; it still
  needs audit before prose promotion.
- M27 has formalized the comparison diagnostic. M29's first calibrated pass
  supports the high-noise divergence story, but the remaining evidence gate is
  a larger or bootstrap-calibrated pass with coverage, width, empty-set,
  overlap, and directional divergence summaries.
