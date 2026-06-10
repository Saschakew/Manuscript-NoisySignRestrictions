# Paper Map

Purpose: compact macro control surface for the manuscript. Read this before
changing section structure or drafting substantial prose.

## One-Sentence Claim

Residual noise can bias standard sign-restricted SVAR sets and make
Drautzburg-Wright-style higher-moment refinement look falsely precise; a
variance-ratio robust DW comparison can use Gaussian-noise-blind higher-moment
conditions plus an explicit residual-noise-to-signal variance bound to recover
precision without reusing invalid covariance anchors.

## Paper Contract

- Paper type: short theory-and-simulation note.
- Scope: bivariate simultaneous impact model in the main text. Treat the
  reduced-form residual `u_t` as given; omit VAR lag dynamics, dynamic impulse
  responses, horizon-specific sign restrictions, and `K > 2` extensions.
- Benchmark: standard sign-restricted covariance rotations and a
  Drautzburg-Wright-style no-noise higher-moment refinement. M49 source-audited
  the bivariate DW moment menu: GMM1 uses `112`, `122`, `1112`, `1122`, and
  `1222`, while GMM2 drops only `1122`. M52 implements GMM1 in the common
  B-plane chart, with the no-noise covariance restriction as a separate screen.
- Constructive object: robust DW-style set over normalized impact matrices
  using mixed higher-moment equations for `B^{-1}u`, including the required
  fourth-order covariance-product subtractions, while avoiding recovered-shock
  zero-covariance targets. M0053 adds a prose gate: Section 4 must distinguish
  transformed-noise covariance `Omega(B)=Var(B^{-1}eta_t)` from full
  transformed-residual covariance `S(B)=Var(B^{-1}u_t)` and explain that the
  implementable fourth-order subtractions use `S(B)`. M55 now supplies the
  reader-facing explanation, and M56 completes the inference gate: sample
  fourth-cumulants are generated smooth moments that can be handled by
  primitive-moment delta-method weighting or an equivalent augmented
  nuisance-covariance GMM system. M52 implements the full central-delta route
  for the generated robust rows. M0036 is now the
  variance-ratio robust DW proposal: add the covariance-decomposition screen
  `0 <= nu_i <= 0.5 Var(epsilon_i)`.
- Evidence: the M0034 pure Figure 1 variant shows the honest cost of dropping
  invalid second-order information. M52 rebuilt Figure 1, Figure 2, Figure 3,
  and the active Monte Carlo table with a source-correct GMM1 standard-DW row
  and full central-delta robust weighting.
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
   restrictions, use robust higher-moment restrictions on normalized candidate
   impacts, and add a variance-ratio covariance-decomposition screen that
   profiles structural-shock and residual-noise variances. Section 4 must make
   the moment computation transparent: for each candidate `B`, compute
   `z_t(B)=B^{-1}u_t`, estimate `S_{ij}(B)` from those transformed residuals,
   and use those nuisance entries in the fourth-order cumulant-style
   subtractions. M56 now says those sample entries are generated smooth
   moments. Section 4 now explains the primitive/delta or augmented-nuisance
   route and avoids calling the concentrated expression one ordinary row-level
   moment.
5. The companion non-Gaussianity grid now uses the variance-ratio proposal and
   states the limitation honestly: robust DW depends on informative higher
   moments and becomes wide when the shocks are close to Gaussian.
6. The sample-size grid shows whether the variance-ratio robust set tightens
   as `T` increases from 500 to 1000 to 2000 with non-Gaussianity and noise
   held fixed.
7. The practical recommendation is simple: report both the standard DW set and
   the robust DW set in the same normalized chart. Standard-DW mass outside the
   robust set is the warning object; robust mass outside the standard set often
   just records the information lost by profiling diagonal noise and dropping
   recovered-shock covariance restrictions.

## Section Jobs

| Section | Job | Status |
|---|---|---|
| Abstract | State sign-restricted set identification, residual-noise bias, false DW sharpening, the variance-ratio robust refinement, and simulation evidence. | revised after M34 claim-tightening |
| 1. Introduction | Motivate sign restrictions through signs plus uncorrelated recovered shocks, explain why residual noise breaks that robustness, position DW as an efficiency refinement, introduce the robust residual-noise-to-signal fix, and preview the evidence. | revised after M34 claim-tightening; literature positioning retained |
| 2. Sign Restrictions And Noisy SVARs | Introduce the no-noise SVAR first, explain sign restrictions as signs plus recovered-shock orthogonality, add residual noise, derive the noisy covariance pseudo-set and J-test view, and state the rescaling exception. | rewritten after revision comments; proof polish pending |
| 3. Drautzburg-Wright Refinement Under Noise | Explain no-noise DW refinement from uncorrelated-but-dependent recovered shocks, define the source-correct DW GMM1/GMM2 higher-moment menus, then show how noise can make refinement falsely precise. | M49 source audit complete; M0050 displays the menu with \(e_t(B)\); M52 rebuilt the source-correct GMM1 evidence row; M47 conditionally clears the M25 proof gate |
| 4. Noise-Robust Sign And DW Sets | Start with the variance-ratio residual-noise-to-signal screen, then add Gaussian-noise-blind higher-moment conditions to regain efficiency without imposing invalid recovered-shock covariance. The main text explains why the moment conditions hold at `B0`, why raw fourth moments need covariance-product subtractions, how `S_{ij}(B)` is computed from candidate transformed residuals, and how the resulting generated sample moments are handled in inference. | M49 noisy product derivations complete; M0050 rewrote the display as explicit moment equations with fourth-order covariance-product subtractions; M54 completed the step-by-step transformed-noise derivation and confirmed the retained `diag(B)=1` chart; M56 completed the generated-moment audit; M55 completed the reader-facing Section 4 explanation; M52 implemented the central-delta robust statistic; final proof and replication still pending |
| 5. Figure-Led Evidence And Monte Carlo Check | Use M52 Figure 1, Figure 2, Figure 3, and source-correct Monte Carlo evidence. | source-correct lightweight evidence rebuilt after M52; still needs replication wrapper |
| 6. Conclusion | Recommend the DW-versus-robust-DW comparison as a robustness check and state limitations. | drafted after M34; needs final citation/export cleanup |

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
- `fig:sample-size-robust-grid`
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
  pure higher-moment row intersected with `0 <= nu_i <= 0.5`
  recovered-covariance feasibility; high-noise accepted share falls to 0.066
  while true `B0` remains included. This is now a comparison because the
  absolute variance cap is scale-arbitrary.
- M52 relative-noise residual grid: high-noise fixed-grid diagnostics have
  source-correct standard DW missing true `B0`, while relative robust DW
  includes it; standard share is 0.026 and robust share is 0.051 on the M52
  diagnostic grid.
- M52 Figure 2 varies structural-shock non-Gaussianity with the same
  source-correct standard-DW and robust rows.
- M52 Figure 3 varies `T=500`, `T=1000`, and `T=2000`, holding the Figure 1
  non-Gaussianity and Figure 2 noise calibration fixed; the robust row remains
  truth-containing in the rendered fixed draw.
- Algebraic proof of the covariance pseudo-set and column-rescaling
  obstruction.
- M47-audited M25 derivation showing that standard DW recovered-shock
  restrictions are misspecified under residual noise, with the J-test
  inversion stated as conditional rich-stack generic emptying plus explicit
  structural-rescaling and finite-stack pseudo-zero exceptions.
- Derivation of the pure higher-moment robust moment stack from
  `derivations/dw-noise-robust-moments.md`; the post-M0030 diagonal-anchor
  estimator audit is superseded by the M0034 scale correction.
- M52 fixed-grid diagnostics rebuild the M28-style checks for the
  variance-ratio robust row and source-correct standard-DW row, including
  Figure 1, Figure 2, and Figure 3 scenarios.
- M27 formal diagnostic note defining the reported standard-DW set, robust-DW
  set, critical-value convention, directional overlap metric, and interpretation
  boundaries.
- M52 refreshed chi-square-primary Monte Carlo evidence for the
  source-correct GMM1 standard-DW row and the variance-ratio robust row. In the
  high-noise row, standard-DW truth inclusion is 0.000 and robust-DW truth
  inclusion is 0.833. The historical M45 and M29 passes remain superseded for
  active evidence.
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
  boundaries. M47 clears the direct M25 proof audit at conditional rich-stack
  strength. The next bottlenecks are adversarial review of the new M52
  evidence and moving figure/table code into `manuscript/replication/` before
  sharing.
- M0041 rewrote the abstract, introduction, and Sections 2-4 in response to
  the revision comments. The front half now starts from SVAR-reader language:
  standard no-noise sign restrictions, recovered-shock orthogonality, the
  noise-induced failure, DW's no-noise higher-moment logic, and then the
  variance-ratio robust construction. M34 conditionally passed the revised
  draft after tightening terminology and evidence claims. Remaining bottlenecks
  are proof audit, final replication packaging, and final export cleanup.
- M52 completes the source-correct evidence rebuild. The current Section 3
  records the source-correct GMM1/GMM2 menus, and Figures 1-3 plus Table 1 now
  implement GMM1 with a separate B-plane covariance screen. The manuscript
  stays in the `diag(B)=1` common chart; the DW source-native unit-variance
  scaling is internal to recovered-shock standardization and does not force a
  manuscript-wide redesign.
- M47 completes the standard-DW proof gate audit. Proposition 2 can now be
  treated as proof-audited conditional prose, provided the draft keeps the
  Gaussian-noise, rich-stack/ICA, compactness, nonsingularity, structural-
  rescaling, and finite-GMM alias caveats visible.
- M54 is complete. It derived the Section 4 transformed-noise moment
  conditions step by step at \(B=B_0\), distinguished independent residual
  components from Gaussian transformed-noise simplifications, and retained the
  `diag(B)=1` chart so no separate unit-variance/rotation-chart update task is
  needed for the first paper.
- M55 completed the main-text explanation gate after M54. Section 4 now
  clarifies that `Omega(B)` is the unobserved transformed-noise covariance
  while `S(B)` is the observed candidate transformed-residual covariance used
  in the robust fourth-order moment equations; it shows representative
  fourth-order algebra and states the practical computation of the moment
  plug-ins.
- M52 implements the generated-moment inference route selected after M56. The
  robust fourth-cumulant sample entries are products of sample averages after
  plugging in `S_{ij}(B)`; the active code now uses full central-moment
  delta-method influence rows with mean-centering nuisance terms.
