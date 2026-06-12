# Paper Map

Purpose: compact macro control surface for the manuscript. Read this before
changing section structure or drafting substantial prose.

## One-Sentence Claim

Residual noise can bias standard sign-restricted SVAR sets and make
Drautzburg-Wright-style higher-moment refinement look falsely precise; a
unit-variance robust DW comparison can model diagonal residual noise with
nuisance variances, use Gaussian-noise-blind higher-moment restrictions, and
report a standard GMM set over \((B,\nu)\).

## Paper Contract

- Paper type: short theory-and-simulation note.
- Scope: bivariate simultaneous impact model in the main text. Treat the
  reduced-form residual `u_t` as given; omit VAR lag dynamics, dynamic impulse
  responses, horizon-specific sign restrictions, and `K > 2` extensions.
- Benchmark: standard sign restrictions are written as the no-noise
  unit-variance set \(E[e_t(B)e_t(B)']=I\), then refined by the bivariate
  Drautzburg-Wright GMM1 menu `112`, `122`, `1112`, `1122`, and `1222`; GMM2
  drops only `1122`.
- Constructive object: robust DW-style GMM set over \((B,\nu)\). The
  second-order block imposes \(\Sigma_u=BB'+\operatorname{diag}(\nu)\). M66
  settles the nuisance bound as the dimensionless ratio
  \(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\), equivalently
  \(\nu_i(B,\lambda)=\lambda_i(BB')_{ii}\). The higher-order block uses
  recovered shocks \(e_t(B)=B^{-1}u_t\) and parameter-implied covariance terms
  \(\omega_{ij}(B,\nu)\), not sample covariance-product plug-ins.
- Evidence: M71 implements Figures 1-3, the Table 1 diagnostic, and the
  extended MC under the M66 \(\lambda\)-bounded unit-variance GMM route. The
  active chart reports first-shock coordinates \((B_{11},B_{21})\), profiles
  \(B_{12}\), \(B_{22}\), and \(\lambda\), imposes only \(B_{11}>0\),
  \(B_{22}>0\), and \(B_{12}\le0\), and uses candidate-specific pointwise
  weighting rather than true-point fixed weights. M72 fixes the panel layout,
  and M73 refreshes Figures 1-3 on denser `41/11/7` default grids. Final
  projected critical values remain a follow-up.
- Excluded: first-version empirical application and broad noise models beyond
  the maintained robust-noise assumptions.

## Reader Path

1. The reader is placed directly in the simultaneous impact problem: the VAR
   residual `u_t` is already in hand, and sign restrictions keep candidates
   whose recovered shocks have covariance \(I\).
2. Residual noise breaks that no-noise target because at the true \(B_0\),
   \(E[e_t(B_0)e_t(B_0)']=I+B_0^{-1}VB_0^{-1'}\).
3. Standard DW-style refinement does not automatically fix this. In the
   high-noise grid column, it rejects true `B0` while looking precise.
4. The paper's constructive move is to model diagonal residual noise directly:
   search over \(B\) and nuisance variances \(\nu\), impose
   \(\Sigma_u=BB'+\operatorname{diag}(\nu)\), and impose
   \(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\) as a maintained restriction.
5. Higher moments then refine this noise-robust second-order set using
   Gaussian-noise-blind rows \(G_H(B,\nu)\). The fourth-order covariance
   products use \(\omega_{ij}(B,\nu)\), so the criterion is standard GMM in
   the enlarged parameter vector.
6. Figures 1-3 use the unit-variance first-shock projected chart.
   Figure 1 varies residual noise, Figure 2 weakens structural
   non-Gaussianity, and Figure 3 varies sample size under the corrected sign
   screen and \((B,\lambda)\) search. M71 has rebuilt this evidence before
   draft interpretation.
7. The practical recommendation is simple: report both the standard DW set and
   the robust DW set in the same normalized chart. Standard-DW mass outside the
   robust set is the warning object; robust mass outside the standard set often
   just records the information lost by profiling diagonal noise and dropping
   recovered-shock covariance restrictions.

## Section Jobs

| Section | Job | Status |
|---|---|---|
| Abstract | State sign-restricted set identification, residual-noise bias, false DW sharpening, the unit-variance robust GMM route, the M71 corrected first-shock evidence rebuild, and the remaining projected-critical-value caveat. | M71 diagnostic evidence revision |
| 1. Introduction | Motivate sign restrictions through signs plus unit-variance recovered-shock covariance, explain why residual noise breaks that target, position DW as an efficiency refinement, and introduce the \((B,\nu)\) robust GMM route. | first-pass M64 revision; literature positioning retained |
| 2. Sign Restrictions And Noisy SVARs | Introduce the no-noise SVAR first, define \(\mathcal S_0\) with \(E[e_t(B)e_t(B)']=I\), add diagonal residual noise, and write the three-moment J inversion. | first-pass M64 revision; Figure 1 first row rebuilt in M71 |
| 3. Drautzburg-Wright Refinement Under Noise | Explain no-noise DW refinement as a refinement of \(\mathcal S_{J,T}(c_2)\), define the source-correct DW GMM1/GMM2 menus, then show why refinement can be falsely precise under noise. | first-pass M64 revision; Figure 1 second row rebuilt in M71 |
| 4. Noise-Robust Sign And DW Sets | Start with \(\Sigma_u=BB'+\operatorname{diag}(\nu)\), impose \(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\), and write \(G_H(B,\nu)\) with parameter-implied \(\omega_{ij}(B,\nu)\) terms inside a standard GMM criterion. | M66 revision; M71 diagnostic implementation complete; projected critical values pending |
| 5. Figure-Led Evidence And Monte Carlo Check | Report Figures 1-3 and Table 1 under the unit-variance \((B,\lambda)\) projected GMM route, using first-shock coordinates and the maintained sign screen. | M71 corrected diagnostic evidence incorporated; interpretation can be refined in M70 |
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
- M73-refresh Figure 2 varies structural-shock non-Gaussianity with the same
  first-shock chart, sign screen, and projected \((B,\lambda)\) route as
  Figure 1.
- M73-refresh Figure 3 varies `T=500`, `T=1000`, and `T=2000`, holding the Figure 1
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
- M71 fixed-grid diagnostics rebuild the M28-style checks for the
  unit-variance robust row and source-correct standard-DW row, including
  Figure 1, Figure 2, and Figure 3 scenarios.
- M27 formal diagnostic note defining the reported standard-DW set, robust-DW
  set, critical-value convention, directional overlap metric, and interpretation
  boundaries.
- M71 refreshed chi-square diagnostic Monte Carlo evidence for the
  source-correct GMM1 standard-DW row and the unit-variance robust row using
  the corrected sign screen and candidate-specific pointwise weights. In the
  high-noise row of the 6-replication Table 1 diagnostic, standard-DW truth
  inclusion is 0.000 and robust-DW truth inclusion is 0.667. The historical
  M52, M45, M29, and pre-correction M68/M69 passes remain superseded for
  active evidence.
- Final Monte Carlo comparison of standard sign, standard DW, and robust DW
  sets using the grid pair's scenarios as the main design.
- Stress cases that quantify honest widening, weak-moment uncertainty, and
  divergence diagnostics.

## Current Bottlenecks

- The standard DW J-test inversion result is now proof-audited by M47 as a
  conditional rich-stack result; finite-GMM alias caveats remain visible.
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
  are final replication packaging and final export cleanup.
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
- M71 completed the immediate evidence-correction bottleneck after M68/M69. It
  rebuilt the figure and Monte Carlo diagnostics with positive diagonal signs,
  \(B_{12}\le0\), no \(B_{21}\) sign restriction, first-shock coordinates
  \((B_{11},B_{21})\), and candidate-specific pointwise weights. The remaining
  bottlenecks are the projected critical-value route and stronger final
  replication.
- M52 implements the generated-moment inference route selected after M56. The
  robust fourth-cumulant sample entries are products of sample averages after
  plugging in `S_{ij}(B)`; the active code now uses full central-moment
  delta-method influence rows with mean-centering nuisance terms.
