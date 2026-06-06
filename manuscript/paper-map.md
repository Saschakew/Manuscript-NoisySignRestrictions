# Paper Map

Purpose: compact macro control surface for the manuscript. Read this before
changing section structure or drafting substantial prose.

## One-Sentence Claim

Residual noise can bias standard sign-restricted SVAR sets and make
Drautzburg-Wright-style higher-moment refinement look falsely precise; a
validity-first robust comparison can use Gaussian-noise higher cumulants, and
may regain precision only when explicit noise-scale information such as an
upper bound on diagonal residual-noise variances is defensible.

## Paper Contract

- Paper type: short theory-and-simulation note.
- Scope: bivariate simultaneous impact model in the main text. Treat the
  reduced-form residual `u_t` as given; omit VAR lag dynamics, dynamic impulse
  responses, horizon-specific sign restrictions, and `K > 2` extensions.
- Benchmark: standard sign-restricted covariance rotations and
  Drautzburg-Wright-style no-noise higher-moment refinement.
- Constructive object: robust DW-style set over normalized impact matrices
  using mixed higher cumulants of `B^{-1}u` written as GMM-style moment
  equations while avoiding recovered-shock zero-covariance targets. M0035 adds
  a candidate bounded-noise recovered-covariance screen with
  `0 <= nu_i <= 0.5`.
- Evidence: the M0034 pure Figure 1 variant shows the honest cost of dropping
  invalid second-order information. The M0035 bounded-noise variant shows that
  an explicit variance upper bound can recover precision while retaining true
  `B0`. This bounded screen needs audit before draft-level evidence claims are
  stable.
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
4. The paper's constructive move is to drop invalid zero-covariance
   restrictions and use robust higher-moment restrictions on normalized
   candidate impacts. If the researcher can bound diagonal residual-noise
   variances, the recovered-shock covariance can be used as an inequality
   screen rather than a zero moment.
5. The companion non-Gaussianity grid states the limitation honestly: robust DW
   depends on informative higher moments and becomes wide when the shocks are
   close to Gaussian.
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
| 4. Robust Higher-Cumulant DW | Define the robust normalized candidate set from mixed higher cumulants, explain why recovered-shock zero covariance and the diagonal-anchor `u` covariance moment are invalid, and derive the bounded-noise recovered-covariance screen as an optional identifying restriction. | needs M0035 audit |
| 5. Figure-Led Evidence And Monte Carlo Check | Compare the pure and bounded-noise Figure 1 variants; rerun M28/M29-style evidence after the bounded screen is audited. | needs revision |
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

- M0034 pure residual-noise grid variant showing covariance/sign-set movement,
  standard-DW truth rejection under lower high residual noise, and pure
  robust-DW truth inclusion with substantial widening.
- M0035 bounded-noise residual grid variant showing the same setting with the
  pure higher-cumulant row intersected with `0 <= nu_i <= 0.5`
  recovered-covariance feasibility; high-noise accepted share falls to 0.066
  while true `B0` remains included.
- Existing non-Gaussianity grid still illustrates the weak-higher-moment
  limitation, but its connection to the revised Figure 1 must be checked in
  M39.
- Algebraic proof of the covariance pseudo-set and column-rescaling
  obstruction.
- M25 working derivation showing that standard DW recovered-shock restrictions
  are misspecified under residual noise, with the J-test inversion stated as
  generic emptying plus explicit pseudo-zero exceptions.
- Derivation of the pure higher-cumulant robust moment stack from
  `derivations/dw-noise-robust-moments.md`; the post-M0030 diagonal-anchor
  estimator audit is superseded by the M0034 scale correction.
- M28 population-grid and repeated-draw validation of the M0030 revised grid
  pair is superseded for the robust row and must be rerun after M39.
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
- M0034 supersedes the M37 pass judgment: the off-diagonal covariance anchor
  double-normalizes scale in the `diag(B)=1` chart unless unit shock variances
  are imposed too.
- M31 has converted the figure-led evidence into a first disciplined draft
  skeleton without treating audit cutoffs as application-ready procedures.
  M32 added the first literature-positioning pass with explicit contribution
  boundaries. The next bottlenecks are M39 evidence/method rebuild, direct M25
  proof audit before theorem-level wording, and moving figure/table code into
  `manuscript/replication/` before sharing.
