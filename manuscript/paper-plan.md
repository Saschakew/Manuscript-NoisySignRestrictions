# Paper Plan

## Working Title

Noise-Robust Sign-Restricted SVARs

## Main Idea

M0034 scale correction: the M0030/M37 diagonal-anchor robust-DW object is
superseded. In the diagonal-normalized chart `diag(B)=1`, the off-diagonal
covariance is `Sigma_u,12=b21*sigma_1^2+b12*sigma_2^2` unless unit shock
variances are imposed as an additional scale normalization. The active
constructive object is therefore the variance-ratio robust-DW set: pure
higher-cumulant moments plus the M0036 relative noise-to-shock variance
screen.

M0035 comparison candidate: the explicitly scaled alternative can use the
recovered-shock covariance equation
`E[e1 e2]=(-b21*nu_1-b12*nu_2)/(1-b12*b21)^2` with
`0 <= nu_i <= 0.5`. This absolute bounded-noise restriction is scale-arbitrary.

M0036 proposal: replace the absolute cap with a variance-ratio signal-to-noise
restriction, `0 <= nu_i <= 0.5 Var(epsilon_i)`. In the diagonal-normalized
chart, profile structural-shock variances and residual-noise variances from
the sample covariance equations for each candidate `B`. This is the paper's
current robust-DW proposal. It is still identifying information, but it is
stated relative to the structural shocks rather than in arbitrary units.

The paper studies the simultaneous SVAR impact problem that arises after a
reduced-form residual has been obtained: what happens when applied researchers
combine sign restrictions with Drautzburg-Wright-style higher-moment
refinements while those residuals contain additive noise. The paper does not
model VAR lag dynamics. The standard sign-restricted set rotates a factor of
the noisy covariance, so it targets a pseudo-set. Standard
Drautzburg-Wright refinement then appears to sharpen that pseudo-set, but the
smaller accepted set can be an artifact of misspecification rather than more
efficient structural learning.

The constructive contribution is a robustness check: compute the standard
Drautzburg-Wright set and compute a Gaussian-noise robust set that drops
invalid zero-covariance restrictions, keeps mixed higher-cumulant restrictions,
and applies the explicit variance-ratio covariance-decomposition screen.
When the two sets agree, the usual refinement is less suspicious. When they
diverge, residual noise or another covariance-target misspecification is
indicated, and the robust set is the safer object.

The paper's visual spine is now rebuilt around the M52 source-correct
proposal. Figure 1 varies residual noise and shows the main warning: noisy
covariance moves the sign set, standard DW can reject the true normalized
`B0`, and variance-ratio robust DW contains it without accepting the whole
chart. Figure 2 fixes residual noise and weakens structural non-Gaussianity,
showing the honest limitation: robust DW is not magic; when higher moments
carry little information, the robust set widens even under the variance-ratio
screen. Figure 3 varies sample size `T=500,1000,2000` while holding the Figure
1 structural non-Gaussianity and Figure 2 residual noise fixed.
The old M28 validation and M29 Monte Carlo passes are now historical for the
robust row because they used the superseded diagonal-anchor statistic. Their
metric bundle remains useful: standard-DW accepted mass outside the robust-DW
set is the directional warning metric, while robust-DW mass outside standard
DW mainly records the information lost by profiling diagonal noise and dropping
recovered-shock covariance restrictions. The rebuilt M52 table keeps standard
pointwise chi-square critical values as the main applied reading, with
repeated-sample and oracle truth cutoffs as secondary audits of finite-sample
size and calibration cost.

## Why It Matters

Sign restrictions are qualitative, but the object being rotated is not. In the
usual no-noise model, the reduced-form covariance equals `B0 B0'`, so a
covariance factor can be rotated into candidate structural impacts. With
additive residual noise,

```text
Sigma_u = B0 B0' + V,
```

so the standard sign-restricted set is built from the wrong covariance object.
This can move sign boundaries, deform accepted regions, and make economically
meaningful columns disappear from the reported set.

Higher moments do not automatically fix the problem. The usual
Drautzburg-Wright procedure refines sign-admissible no-noise candidates by
testing independence of recovered shocks. Under residual noise, those recovered
objects are not the true structural shocks. Asymptotically, the no-noise DW set
may become empty; in finite samples, it can become small and look precise
because the least-misspecified candidates are being selected.

The robust alternative keeps the useful higher-moment idea but replaces the
fragile no-noise covariance step. It searches over normalized impact matrices,
imposes economic signs directly on those matrices, profiles diagonal
residual-noise variances and structural-shock variances when a relative
noise-scale bound is imposed, and uses higher-order cumulants of candidate
transformed residuals written as GMM-style moment equations. The robust set
deliberately gives up contaminated diagonal variance targets and recovered-
shock zero covariance, so it should often be wider than the standard DW set
unless the researcher adds defensible signal-to-noise information. That width
is the price of not pretending that the noisy covariance is structural.

## Proposed Structure

1. Introduction: present the puzzle that sign restrictions can look more
   precise after higher-moment refinement even when residual noise has
   misspecified the no-noise target. State the robustness-check idea and
   position the contribution relative to sign-set inference,
   Drautzburg-Wright's no-noise comparator, and higher-moment SVAR/GMM work.
2. Noisy sign-restricted sets: define the additive-noise SVAR, show that the
   standard sign set rotates a factor of `B0 B0' + V`, and give an intuitive
   visual figure of sign-boundary movement or set deformation.
3. Standard DW under residual noise: explain the no-noise DW refinement, show
   why the recovered shocks are contaminated under noise, and state the
   planned result that the population DW set should generally be empty under
   misspecification, with finite-sample regions shrinking around
   least-rejected pseudo-candidates.
4. Robust higher-cumulant DW set: define the normalized robust candidate space,
   write the mixed higher-cumulant restrictions as moment equations, explain
   why they hold at `B0` under Gaussian residual noise, explain why recovered-
   shock zero covariance and the old off-diagonal `u` covariance anchor are not
   imposed, and present the variance-ratio covariance screen as the proposal's
   identifying restriction. The main text should not reproduce every M54
   expansion, but it must distinguish transformed-noise covariance
   `Omega(B)=Var(B^{-1}eta_t)` from full transformed-residual covariance
   `S(B)=Var(B^{-1}u_t)` and show how the `S_{ij}(B)` nuisance plug-ins enter
   the fourth-order conditions. M55 now supplies this explanation in the draft.
   M56 shows that those plug-in covariance products are generated smooth
   moments: use primitive-moment delta-method covariance, an equivalent
   augmented nuisance-covariance GMM system, or bootstrap/repeated-sample
   calibration rather than treating the concentrated expression as one
   ordinary row-level moment. State claims with the M0034/M0036 caveats:
   normalized bivariate chart, diagonal Gaussian residual noise, explicit
   signal-to-noise bound, and pointwise critical values under the M52
   central-delta generated-moment route.
5. Figure-led evidence and Monte Carlo robustness check: use the rebuilt
   Figure 1/Figure 2/Figure 3 sequence as the reader's main visual guide. First
   show the residual-noise grid that moves the sign set, makes standard DW
   reject the truth in the high-noise column, and leaves variance-ratio robust
   DW informative. Then show the updated non-Gaussianity grid that makes weak
   higher moments visible. Then add the sample-size grid to show how the
   variance-ratio robust set changes from `T=500` to `T=1000` to `T=2000`.
   Use population-grid and Monte Carlo checks to validate, calibrate, and
   summarize the same story.
6. Conclusion: recommend reporting the robust DW set beside the standard DW
   set as a diagnostic for covariance-target misspecification. Defer empirical
   applications.

## Key Model Or Notation

- Observed residual model:
  `u_t = B0 epsilon_t + eta_t`, `E[epsilon_t epsilon_t'] = I`,
  `E[epsilon_t eta_t'] = 0`, and `E[eta_t eta_t'] = V`.
- Scope convention:
  treat `u_t` as the simultaneous residual/impact object. The first paper does
  not specify or estimate lag matrices, dynamic responses, or horizon-specific
  sign restrictions.
- Standard sign set:
  `B_*(Q) = P_* Q`, where `P_* P_*' = Sigma_u = B0 B0' + V` and
  `R(P_* Q) >= 0`.
- No-noise economic sign set:
  `P_0 P_0' = B0 B0'`, with `R(P_0 Q) >= 0`.
- Standard DW set:
  sign-admissible candidates whose standardized recovered shocks pass the
  source-correct bivariate GMM1 higher-moment menu, with covariance imposed as
  a separate B-plane screen in the retained common chart.
- Robust DW candidate:
  a normalized impact matrix `B` not required to satisfy `B B' = Sigma_u`.
- Superseded diagonal-noise covariance anchor:
  `Cov(u_1,u_2) = b12 + b21` is invalid in the diagonal-normalized chart unless
  unit shock variances are imposed as an additional scale normalization.
- Relative-noise covariance screen:
  for `B=[[1,b12],[b21,1]]`, find shock variances `s_i` and residual-noise
  variances `nu_i` satisfying the sample covariance decomposition and
  `0 <= nu_i <= 0.5 s_i`.
- Robust DW transformed residual:
  `z_t(B) = B^{-1} u_t`.
- Transformed-noise covariance:
  `Omega(B)=Var(B^{-1}eta_t)`. This object is useful for deriving the
  Gaussian-noise simplification at `B0`, but it is not directly observed in
  applications.
- Full transformed-residual covariance:
  `S(B)=Var(z_t(B))=Var(B^{-1}u_t)`. The fourth-order robust moment equations
  use entries of `S(B)`, estimated from candidate transformed residuals, as
  nuisance plug-ins. They do not impose `S_{12}(B)=0`.
- Robust DW moment stack:
  mixed third central moments and fourth cumulants of `z_t(B)`, written as raw
  moment equations with covariance products subtracted; optional second-order
  information enters only through the explicit variance-ratio covariance
  screen.
- Robust DW sample criterion:
  implemented in M52 using the M56 generated-moment route. The sample
  fourth-cumulant entries are concentrated smooth functions of primitive
  sample moments, for example
  `mean(z1*z2^3)-3 mean(z2^2) mean(z1*z2)`. The valid route is
  primitive-moment delta-method weighting or an equivalent augmented nuisance
  covariance GMM system. The active code uses full central-moment delta
  influence rows, including sample-mean nuisance terms; bootstrap or heavier
  repeated-sample calibration remains a possible final replication add-on.
- Robustness check:
  compare the standard DW accepted set with the robust DW accepted set in the
  common normalized chart. Report accepted shares, overlap, standard-DW mass
  outside robust-DW, and truth inclusion in simulations. Agreement supports the
  usual refinement; standard-DW mass outside robust-DW warns that the usual
  refinement may be reacting to residual noise or covariance-target
  misspecification.

## Main Results To Prove Or Demonstrate

- Proposition 1, noisy sign pseudo-set: if `V != 0`, the population sign set
  based on `Sigma_u` generally differs from the no-noise economic sign set.
  This result should be explained visually before the algebra.
- Proposition 2, standard DW is misspecified under residual noise: recovered
  shocks from noisy covariance-factor candidates are not the structural shocks.
  The M47 audit of the M25 derivation shows that, under a rich
  independence/J-test inversion, compactness, nonsingularity, and generic
  Gaussian residual noise, the population accepted set is empty; with special
  structural-coordinate rescaling cases or finite-GMM aliases, the set can
  instead contain pseudo-true candidates. Finite-sample inversion can still
  return a falsely narrow least-rejected region.
- Proposition 3, robust DW validity: under the maintained diagonal Gaussian
  residual-noise conditions, the higher-cumulant moment stack for `z_t(B)` has
  zero population value at the true normalized impact matrix. The main text
  should explain this by writing `z_t(B0)=epsilon_t+B0^{-1}eta_t`, using
  Gaussianity to kill transformed-noise cumulants above order two, and showing
  why fourth-order raw products need subtractions such as
  `E[z_1z_2^3]-3S_{22}S_{12}`. The contaminated recovered-shock zero-
  covariance restriction and superseded diagonal-anchor `u` covariance moment
  are not imposed. Optional second-order precision comes from an explicit
  relative noise-to-shock variance restriction, not from DW independence
  moments. M40 conditionally passes the covariance-screen algebra and
  interpretation for proposal prose. M56 shows the finite-sample concentrated
  cumulant statistic needs generated-moment weighting or calibration before
  final pointwise chi-square wording.
- Proposition 4, robust set comparison: M27 formalizes the diagnostic in
  `manuscript/derivations/dw-robust-comparison-diagnostic.md`. The key warning
  is directional: standard-DW accepted mass outside robust-DW indicates that
  apparent no-noise covariance-target precision may not be robust, while
  robust-DW mass outside standard DW usually reflects the information
  deliberately lost by profiling diagonal noise and dropping recovered-shock
  covariance restrictions. The comparison is a warning, not literal proof of
  measurement error.
- Simulation result: the M0036 relative-noise Figure 1, rebuilt Figure 2, new
  Figure 3, and M52 Monte Carlo table form the current proposal evidence. In
  the high-noise primary row, source-correct standard DW includes true `B0` in
  0.000 of evaluation samples and variance-ratio robust DW includes it in
  0.833. Treat the evidence as lightweight until final replication packaging.

## Evidence Plan

- Main visual figure 1, residual-noise grid: show three rows
  (sign/covariance, standard DW, robust DW) across increasing Gaussian residual
  noise. The high-noise column should remain the narrative anchor where
  standard DW rejects true `B0` and robust DW contains it.
- Main visual figure 2, non-Gaussianity grid: rebuilt companion figure with the
  variance-ratio robust row. Hold residual noise fixed and weaken
  structural-shock higher moments. Use it to show that robust DW widens as the
  identifying higher-moment signal weakens.
- Main visual figure 3, sample-size grid: new figure with columns `T=500`,
  `T=1000`, and `T=2000`, holding the Figure 1 non-Gaussianity and Figure 2
  noise calibration fixed. Use it to show whether the variance-ratio robust set
  tightens with sample size while the maintained signal-to-noise restriction
  stays fixed.
- Validation grid checks: M52 reruns M28-style fixed-grid checks for the
  source-correct standard-DW row and variance-ratio robust row. The old M28
  pass is historical for the robust row because it used the superseded
  diagonal-anchor statistic.
- Monte Carlo table: M52 reruns M29/M45-style evidence for the variance-ratio
  robust proposal. Reuse the same reporting metrics: true-`B0` inclusion,
  accepted-set share, empty-set frequency, standard-DW versus robust-DW overlap,
  the M27 directional divergence metric, and least-rejected candidates across
  no-noise, moderate-noise, high-noise, weak-moment, Gaussian-shock, and
  skewed-residual-noise stress cases. Standard pointwise chi-square rows should
  remain the primary applied benchmark, with no-noise repeated and oracle truth
  rows as calibration audits.
- Stress cases: weak higher moments, near-Gaussian structural shocks, high
  noise, non-Gaussian noise that violates the robust route if Gaussianity is
  maintained, anisotropic noise, near-boundary signs, and small macro samples.

## What Is Missing

- Sections 2-4 now have M0038 formula-first prose sketches for the noisy
  sign-set algebra, standard-DW misspecification result, and variance-ratio
  robust DW proposal. M40 conditionally passed the variance-ratio screen; they
  now have the M47 standard-DW proof audit outcome. Remaining polish is
  adversarial review of the M52 evidence and final citation-style cleanup
  before becoming polished manuscript prose.
- M42 completed the manuscript math-delimiter cleanup. Future drafting should
  keep mathematical expressions in `\(...\)` or display equation environments
  rather than Markdown backticks.
- The first literature-positioning pass is drafted in the introduction. It
  still needs final citation-style cleanup when the References section is
  converted from TODO to shareable prose.
- Section 4 prose must incorporate the M0034/M0036 caveats: the old
  off-diagonal covariance anchor is invalid under `diag(B)=1` without fixed
  shock variances; the pure robust row uses a five-moment higher-cumulant stack;
  the relative screen adds an explicit `nu_i <= 0.5 Var(epsilon_i)` identifying
  restriction; pointwise chi-square cutoffs are only a plotted benchmark; and
  non-Gaussian residual noise generally invalidates the transformed-cumulant
  interpretation unless additional noise-cumulant restrictions are modeled.
- Section 4 now incorporates the M54/M0053/M55 explanation gate: it defines
  `Omega(B)` for transformed residual noise and `S(B)` for full transformed
  observed residuals, states that fourth-order covariance-product subtractions
  use `S(B)`, and gives a practical recipe for computing `S_{ij}(B)` from
  centered `z_t(B)=B^{-1}u_t` for each candidate `B`.
- The robust-row inference now incorporates the M56 generated-moment result:
  products of sample covariance estimates inside fourth cumulants invalidate
  naive row-level GMM wording. M52 implements full central-moment delta
  weighting, including mean-centering nuisance terms. Final replication can
  still add heavier calibration checks.
- A self-contained simulation package that builds the sign-bias, DW-shrinkage,
  and robust-DW comparison figures from this repository.

## Page Budget And Scope Exclusions

Target: short theory-and-simulation paper, about 18-24 manuscript pages before
appendix.

Excluded from the first version:

- A full empirical application.
- A general `K`-variable estimator in the main text.
- VAR lag dynamics, lag-coefficient estimation, dynamic responses, and
  horizon-specific sign restrictions.
- Correlated, serially dependent, common-factor, or stochastic-volatility noise.
- A claim that divergence between DW and robust DW proves literal measurement
  error. It is a robustness warning inside the maintained model.

## Scope Recommendation

Keep the paper as one clean robustness-check story:

1. Noise biases the standard sign-restricted set.
2. Standard DW refinement can falsely sharpen the misspecified set.
3. A variance-ratio robust DW set keeps valid higher cumulants, drops invalid
   covariance anchors, and adds an explicit signal-to-noise bound to recover
   useful precision without double-normalizing scale.
4. Comparing the two sets gives a practical diagnostic.
5. Simulations carry the evidence burden; no application is needed yet.
