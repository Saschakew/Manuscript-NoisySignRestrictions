# Paper Map

Purpose: compact macro control surface for the manuscript. Read this before
changing section structure or drafting substantial prose.

## One-Sentence Claim

Residual noise can bias standard sign-restricted SVAR sets and make
Drautzburg-Wright-style higher-moment refinement look falsely precise; a
diagonal-noise robust set that profiles diagonal noise variances, keeps the
clean off-diagonal covariance restriction, and adds higher cumulants should be
reported beside the standard DW set as a practical robustness check.

## Paper Contract

- Paper type: short theory-and-simulation note.
- Scope: bivariate simultaneous impact model in the main text. Treat the
  reduced-form residual `u_t` as given; omit VAR lag dynamics, dynamic impulse
  responses, horizon-specific sign restrictions, and `K > 2` extensions.
- Benchmark: standard sign-restricted covariance rotations and
  Drautzburg-Wright-style no-noise higher-moment refinement.
- Constructive object: robust DW-style diagonal-noise set over normalized
  impact matrices, using the off-diagonal residual covariance restriction plus
  higher cumulants written as GMM-style moment equations while avoiding the
  false recovered-shock covariance target. M37 conditionally clears this
  object for local theorem-level prose under diagonal Gaussian residual noise.
- Evidence: the M0030 revised grid pair is the visual spine. The residual-noise
  grid shows sign-set movement, standard-DW truth rejection at `V=(0.5,0.5)`,
  and robust-DW truth inclusion without whole-chart acceptance; the
  non-Gaussianity grid shows why robust DW widens toward the covariance anchor
  when higher moments weaken. M28 validates the population/repeated-seed layer
  of this story. The refreshed M29 run uses standard pointwise chi-square
  cutoffs as the primary applied benchmark, with repeated-sample and
  truth-bootstrap diagnostics kept as calibration audits.
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
4. The paper's constructive move is to profile diagonal noise variances, keep
   the off-diagonal covariance restriction, and use robust higher-moment
   restrictions on normalized candidate impacts. The same grid shows the
   robust set remains informative and contains the truth.
5. The companion non-Gaussianity grid states the limitation honestly: robust DW
   depends on informative higher moments and becomes wide when the shocks are
   close to Gaussian, falling back toward the covariance anchor.
6. The practical recommendation is simple: report both the standard DW set and
   the robust DW set in the same normalized chart. Standard-DW mass outside the
   robust set is the warning object; robust mass outside the standard set often
   just records the information lost by profiling diagonal noise and dropping
   recovered-shock covariance restrictions.

## Section Jobs

| Section | Job | Status |
|---|---|---|
| Abstract | State noisy sign-set bias, false DW sharpening, robust DW comparison, and no-application scope. | skeleton drafted |
| 1. Introduction | Motivate the robustness-check problem, position the paper relative to sign restrictions, Drautzburg-Wright, and higher-moment SVAR/GMM, and preview the geometry plus Monte Carlo evidence. | skeleton plus M32 positioning drafted |
| 2. Noisy Sign Sets | Define the additive-noise SVAR and show, visually and algebraically, how standard sign sets become biased pseudo-sets. | planned |
| 3. Standard DW Under Noise | Explain the no-noise DW refinement, why noise contaminates recovered shocks, and why the refined set can become empty or falsely small. | planned |
| 4. Diagonal-Noise Robust DW | Define the robust normalized candidate set, write the off-diagonal covariance and cumulant restrictions as moment equations, and explain why diagonal noise variances are profiled out. | planned |
| 5. Figure-Led Evidence And Monte Carlo Check | Use the two M0030 revised grids as the main visual story, then validate and quantify the same claims with population-grid and Monte Carlo checks. | skeleton drafted |
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

- M0030 residual-noise grid showing covariance/sign-set movement, standard-DW
  truth rejection under lower high residual noise, and robust-DW truth
  inclusion without whole-chart acceptance.
- M0030 non-Gaussianity grid showing robust-DW widening toward the covariance
  anchor as higher moments weaken.
- Algebraic proof of the covariance pseudo-set and column-rescaling
  obstruction.
- M25 working derivation showing that standard DW recovered-shock restrictions
  are misspecified under residual noise, with the J-test inversion stated as
  generic emptying plus explicit pseudo-zero exceptions.
- Derivation of the diagonal-noise robust moment stack from
  `derivations/dw-noise-robust-moments.md`, with the post-M0030 estimator
  audit in `derivations/m37-diagonal-noise-robust-estimator-audit.md`.
- M28 population-grid and repeated-draw validation of the M0030 revised grid pair.
- M27 formal diagnostic note defining the reported standard-DW set, robust-DW
  set, critical-value convention, directional overlap metric, and interpretation
  boundaries.
- M29 refreshed chi-square-primary Monte Carlo pass comparing standard DW and robust DW
  sets using the grid pair's scenarios plus weak-moment, Gaussian-shock, and
  skewed-residual-noise stress cases. It reports chi-square, no-noise repeated,
  oracle scenario truth, and truth-point residual-bootstrap cutoffs, with
  chi-square as the primary applied benchmark.
- Final Monte Carlo comparison of standard sign, standard DW, and robust DW
  sets using the grid pair's scenarios as the main design.
- Stress cases that quantify honest widening, weak-moment uncertainty, and
  divergence diagnostics.

## Current Bottlenecks

- The standard DW J-test inversion result is now a working derivation; it still
  needs audit before prose promotion.
- M37 conditionally cleared the diagonal-noise robust estimator for local
  theorem-level prose, but the prose must state its normalized-chart,
  diagonal-Gaussian-noise, optional profiled-variance-screen, and pointwise
  cutoff caveats.
- M31 has converted the figure-led evidence into a first disciplined draft
  skeleton without treating audit cutoffs as application-ready procedures.
  M32 added the first literature-positioning pass with explicit contribution
  boundaries. The next bottlenecks are drafting Sections 2-4, direct M25 proof
  audit before theorem-level wording, and moving figure/table code into
  `manuscript/replication/` before sharing.
