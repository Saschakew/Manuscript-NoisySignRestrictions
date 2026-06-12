# Noise-Robust Sign-Restricted SVARs

Author: TODO

Date: 2026-06-05

## Abstract

Sign restrictions set-identify structural impact matrices by combining
economically motivated signs with the requirement that recovered structural
shocks are mutually uncorrelated. In non-Gaussian SVARs, this set can be
sharpened by imposing higher-order independence restrictions in the spirit of
Drautzburg and Wright. This paper shows that idiosyncratic residual noise can
break both steps. If the observed residual is
\(u_t=B_0\varepsilon_t+\eta_t\), a standard no-noise sign-restricted SVAR
matches the covariance of \(u_t\), not the covariance of the structural signal
\(B_0\varepsilon_t\). The resulting identified set can be biased and need not
contain the true impact matrix. Higher-moment refinement can then sharpen the
wrong target, producing a small accepted set that looks precise while moving
further away from the structural object of interest. This paper proposes a
noise-robust refinement that separates non-Gaussian structural shocks from
Gaussian residual noise under the unit-variance normalization
\(E[\varepsilon_t\varepsilon_t']=I\). The researcher states a maximum ratio of
residual-noise variance to structural-signal variance, treats residual-noise
variances as nuisance parameters, and uses higher-moment restrictions in a
standard GMM criterion over \((B,\nu)\). Figure 1 has been regenerated under
this unit-variance projected GMM implementation. The companion figures and
Monte Carlo table remain rebuild targets before final evidence claims are
made.

<!-- SOURCE-TRAIL: Use the M67 unit-variance Figure 1 rebuild, the M66 noise-ratio derivation, M49 for the source-correct GMM1 menu, M56 for generated-moment inference, and M52 only as historical evidence. -->
<!-- CONTRIBUTION-NOTE: The abstract's original contribution is the residual-noise pseudo-set warning and the DW-versus-robust-DW comparison diagnostic. -->

## 1. Introduction

Sign-restricted SVARs are popular because they identify structural shocks with
relatively little economic structure. Once the reduced-form residual \(u_t\) is
available, the researcher searches for impact matrices \(B\) such that the
recovered shocks \(e_t(B)=B^{-1}u_t\) have covariance \(I\) and the entries of
\(B\) satisfy economically motivated sign restrictions. Compared with
recursive zero restrictions or external instruments, this looks robust: the
researcher does not choose a recursive ordering or a single proxy, but reports
the set of impact matrices consistent with signs and orthogonality.

<!-- SOURCE-TRAIL: Use sign-restriction overview sources, `kilian2016StructuralVectorAutoregressiveAnalysis93b03b`, and `arias2018InferenceBasedStructuralVector`. -->

This paper shows that the same orthogonality requirement becomes fragile when
the observed residual contains idiosyncratic noise. In the simultaneous
impact model
\[
u_t=B_0\varepsilon_t+\eta_t,
\]
\(B_0\varepsilon_t\) is the structural signal and \(\eta_t\) is residual noise.
A standard sign-restricted SVAR that ignores \(\eta_t\) treats \(u_t\) as if it
were entirely structural signal. Even at the true impact matrix, the recovered
object \(B_0^{-1}u_t=\varepsilon_t+B_0^{-1}\eta_t\) need not have uncorrelated
components. Equivalently, the usual covariance factor is a factor of
\(B_0B_0' + V\), not a factor of \(B_0B_0'\). The sign-restricted set is then
identified from the wrong covariance object and may no longer contain the true
impact matrix, even in population.

<!-- SOURCE-TRAIL: Use `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md` and the M25 column-rescaling obstruction. -->

The problem becomes sharper once higher moments are used for refinement. The
motivation for Drautzburg-Wright-style refinement is clear in a no-noise SVAR:
sign restrictions often leave a wide set, while non-Gaussian structural shocks
carry additional information about independence beyond zero covariance. A
researcher can therefore discard sign-admissible impact matrices whose
recovered shocks are uncorrelated but still dependent at third or fourth
order. Under residual noise, however, the refinement is applied to shocks
recovered from a misspecified no-noise model. It can reject the true impact
matrix and select a small region around a noisy pseudo-target. The visual
danger is a false sense of precision: the accepted set gets smaller, but the
target being sharpened is no longer the structural target.

<!-- SOURCE-TRAIL: Use `drautzburg2023RefiningSetIdentificationVars` for the maintained-null comparator and `manuscript/derivations/standard-dw-j-test-under-noise.md` for the M25 working misspecification result. -->
<!-- TODO-NOTE: Do not promote the generic emptying result to theorem wording until the M25 proof audit is complete. -->

The proposed solution keeps the logic of sign restrictions but changes the
maintained model. Instead of pretending that all variation in \(u_t\) is
structural signal, the researcher reports impact matrices that are compatible
with signs, with diagonal Gaussian residual noise, and with an explicit
residual-noise-to-signal bound. In the bivariate version used here, the
dimensionless bound is written as
\(\lambda_i=\nu_i/(BB')_{ii}\le\rho\): residual-noise variance in coordinate
\(i\) can be at most a fraction \(\rho\) of the corresponding structural-signal
variance. This bound makes the sign-restricted set robust to noise up to the
specified ratio. It also makes the cost transparent. A larger allowed noise
ratio gives a more robust but wider set; a smaller ratio gives more precision
but requires a stronger signal-to-noise assumption.

The higher-moment part of the solution exploits a simple cumulant fact. If
residual noise is Gaussian and independent of the structural shocks, it changes
second moments but has no cumulants above order two. Mixed third and fourth
cumulants of \(B^{-1}u_t\) can therefore be used to refine the noise-robust
sign set without reusing the invalid no-noise covariance restriction. This is
the sense in which the robust DW refinement separates non-Gaussian structural
shocks from Gaussian residual noise. It does not claim that higher moments
always give a sharp estimator. When structural shocks are nearly Gaussian, the
robust set widens, and that widening is part of the diagnostic.

<!-- SOURCE-TRAIL: Use `manuscript/derivations/dw-noise-robust-moments.md`, `manuscript/derivations/dw-robust-comparison-diagnostic.md`, and higher-moment SVAR caution sources. -->

The current simulation evidence starts with the rebuilt Figure 1, which varies
Gaussian residual noise under the unit-variance projected GMM route. The
standard no-noise and standard-DW screens can reject the full true impact
matrix once residual noise is present, while the robust projected set remains
truth-containing in the displayed fixed draw. Figure 2, Figure 3, and Table 1
still need the same unit-variance rebuild before they can support final
evidence claims. The recommendation is diagnostic: report the standard DW set
and the robust DW set together, and treat standard DW precision unsupported by
the robust set as a warning sign.

<!-- SOURCE-TRAIL: Use M67 for the rebuilt Figure 1, M66 for the lambda-bound algorithm, and M52 only as historical evidence for the remaining pre-M64 figures/table. -->

### 1.1 Literature Positioning

This paper is closest to three literatures, but it uses them for a narrow
robustness question rather than for a broad survey. The first is the
sign-restricted SVAR literature. In that literature, sign restrictions describe
sets of admissible rotations, and careful reporting matters because selected
rotations or point summaries can understate set uncertainty. This paper accepts
that set-based starting point. Its additional question comes one step earlier:
if the covariance factor being rotated is a factor of \(B_0B_0' + V\), then even
the population sign set is already a noisy pseudo-set.

<!-- SOURCE-TRAIL: Use `kilian2016StructuralVectorAutoregressiveAnalysis93b03b` for sign-restriction geometry and `arias2018InferenceBasedStructuralVector` for set-inference and reporting cautions. -->
<!-- CONTRIBUTION-NOTE: The covariance-target contamination question is this manuscript's contribution, not a claim inherited from standard sign-restriction inference. -->

The second comparator is Drautzburg and Wright's independence refinement. Their
procedure is the right benchmark because it takes a sign-restricted set and
uses higher-moment independence restrictions to refine it under a maintained
no-noise model. This paper does not claim that refinement is invalid under
that model. It asks what the same researcher-facing refinement reports when
the reduced-form residual includes additive noise and the no-noise covariance
target is misspecified. The standard-DW set is therefore used as a
maintained-null comparator, while the robust set is a diagnostic object to
report beside it.

<!-- SOURCE-TRAIL: Use `drautzburg2023RefiningSetIdentificationVars` for the no-noise comparator and `manuscript/derivations/standard-dw-j-test-under-noise.md` for the manuscript's residual-noise misspecification route. -->
<!-- TODO-NOTE: Keep theorem-level claims about generic standard-DW emptying conditional on the M25 proof audit. -->

The third connection is the higher-moment SVAR and GMM literature. Those papers
show that non-Gaussian moments can carry structural information, but they also
make the assumptions and weak-moment risks explicit. The robust DW set follows
that discipline: it writes mixed higher cumulants as moment restrictions, uses
a GMM-style inversion language, and treats weak or Gaussian structural shocks
as an honest widening case. The robust set is not advertised as a uniformly
sharper estimator. It is meant to reveal when standard-DW precision depends on
a noisy covariance target that the robust moments do not support.

<!-- SOURCE-TRAIL: Use `guay2020IdentificationStructuralVectorAutoregressions`, `paper2020GeneralizedMethodMomentsEstimator`, `olea2022SvarIdentificationHigherMoments`, and `lewis2025IdentificationBasedHigherMoments`. -->
<!-- CONTRIBUTION-NOTE: The original contribution is the DW-versus-robust-DW comparison under residual noise, not the general idea that higher moments can identify SVARs. -->

The paper is organized around this comparison. Figure 1 varies Gaussian
residual noise and shows the main warning with the unit-variance projected
implementation: the no-noise and standard-DW rows reject the full true impact
matrix once residual noise is present, while the robust projected row remains
truth-containing after profiling admissible \(\lambda\). Figure 2 should hold
residual noise fixed and weaken structural non-Gaussianity, showing the
limitation that robust DW's higher-cumulant component needs informative higher
moments. Figure 3 should ask whether the comparison tightens with sample size,
and Table 1 must be rebuilt under the same unit-variance route.

<!-- SOURCE-TRAIL: Use M67 for the current Figure 1 and M65 for the remaining Figure 2/Figure 3/table rebuild. -->

<!-- SOURCE-TRAIL: Use sign-restriction overview sources, Drautzburg-Wright, and the noisy-residual synthesis. -->
<!-- CONTRIBUTION-NOTE: The original contribution is the noise-bias warning plus the standard-DW versus robust-DW comparison. -->

## 2. Sign Restrictions and Noisy SVARs

This section starts with the standard object and then adds noise. The main text
uses a bivariate simultaneous impact model. There are no VAR lags, dynamic
impulse responses, or horizon-specific restrictions in the first version of
the paper. The residual \(u_t\) is already in hand, and the question is which
impact matrices can be reported from it.

In the no-noise benchmark,

\begin{equation}
u_t = B_0\varepsilon_t,\qquad
E(\varepsilon_t)=0,\qquad
E(\varepsilon_t\varepsilon_t')=I .
\end{equation}

The matrix \(B_0\) is the structural impact matrix. The vector
\(\varepsilon_t=(\varepsilon_{1t},\varepsilon_{2t})'\) contains structural
shocks normalized to have unit variances and zero covariance. For any candidate
impact matrix \(B\), the recovered shocks are

\begin{equation}
e_t(B)=B^{-1}u_t .
\end{equation}

A sign-restricted SVAR keeps candidates whose recovered shocks have the same
unit-variance covariance matrix as the structural shocks and whose impact
matrix satisfies the chosen sign restrictions. If \(R(B)\ge0\) denotes the sign
screen, the population no-noise set is

\begin{equation}
\mathcal S_0 =
\{B:\ R(B)\ge0,\quad E[e_t(B)e_t(B)']=I\}.
\label{eq:no-noise-sign-j-set}
\end{equation}

If \(B_0\) satisfies the sign restrictions, then \(B_0\in\mathcal S_0\)
because \(e_t(B_0)=\varepsilon_t\) and the normalization above gives
\(E[\varepsilon_t\varepsilon_t']=I\). This J-test representation is the object
we will invert in finite samples.

Now suppose the observed residual contains additive residual noise:

\begin{equation}
u_t = B_0\varepsilon_t+\eta_t,\qquad
E(\eta_t)=0,\qquad
E(\eta_t\eta_t')=V=\operatorname{diag}(\nu_1,\nu_2).
\end{equation}

The residual noise is independent of the structural shocks. The diagonal
matrix \(V\) records idiosyncratic residual-noise variances in the coordinates
of \(u_t\).

The covariance of the observed residual is

\begin{equation}
\Sigma_u=E(u_tu_t')=B_0B_0'+V .
\end{equation}

If the researcher ignores \(\eta_t\), the standard sign-restricted SVAR treats
\(\Sigma_u\) as if it were generated only by structural shocks. That changes
the object being identified. At the true impact matrix,

\begin{equation}
e_t(B_0)=B_0^{-1}u_t
=\varepsilon_t+B_0^{-1}\eta_t ,
\end{equation}

so the recovered-shock covariance is

\begin{equation}
E[e_t(B_0)e_t(B_0)']
= I+B_0^{-1}VB_0^{-1'} .
\end{equation}

Consequently \(B_0\) generally fails the no-noise condition in
\eqref{eq:no-noise-sign-j-set}. Any nonzero diagonal element of
\(B_0^{-1}VB_0^{-1'}\) violates the unit-variance part of
\(\mathcal S_0\), and any nonzero off-diagonal element also makes the recovered
components correlated. The issue is not that the noisy model is incoherent.
The issue is that \(\mathcal S_0\) is constructed to find candidates whose
recovered residuals look like unit-variance, mutually uncorrelated structural
shocks. Under residual noise, \(e_t(B_0)\) no longer has that covariance
matrix.

Thus, without modeling residual noise, the reported sign-restricted set is
shifted away from the structural impact matrix. In extreme cases the shift can
cross a sign boundary: the noisy covariance may make every candidate satisfying
the no-noise unit-variance and zero-covariance target put a disputed entry on
the wrong side of zero.

In finite samples the same idea can be written as a J-test inversion. For a
candidate \(B\), let

\begin{equation}
\widehat m_{2,T}(B)=
\begin{bmatrix}
T^{-1}\sum_{t=1}^T e_{1t}(B)^2-1\\
T^{-1}\sum_{t=1}^T e_{2t}(B)^2-1\\
T^{-1}\sum_{t=1}^T e_{1t}(B)e_{2t}(B)
\end{bmatrix}.
\end{equation}

These are the two unit-variance moments and the covariance moment implied by
\eqref{eq:no-noise-sign-j-set}. A no-noise sign-restricted inversion
accepts candidates satisfying

\begin{equation}
\mathcal S_{J,T}(c_2)=
\left\{
B:\ R(B)\ge0,\quad
J_{2,T}(B)=T\widehat m_{2,T}(B)'\widehat W_{2,T}\widehat m_{2,T}(B)\le c_2
\right\}.
\end{equation}

With the usual efficient weighting matrix and standard regularity conditions,
the statistic evaluated at the true \(B_0\) under the no-noise null has the
pointwise limit \(\chi^2_3\), one degree for each moment in
\(\widehat m_{2,T}\). For a level-\(\alpha\) inversion, \(c_2\) can therefore
be taken as the \(1-\alpha\) quantile of \(\chi^2_3\). The J-test view makes
the source of bias explicit: in the noisy model, the no-noise vector
\(E[e_t(B_0)e_t(B_0)']-I\) is generally not zero. The first row of Figure 1
shows this unit-variance version of the bias: the no-noise sign/covariance
target rejects the full true \(B_0\) once residual noise is present, before
higher moments are used.

<!-- SOURCE-TRAIL: Use the proposal note, `Noisy residuals in recursive and sign-restricted SVARs.md`, and the M25 column-rescaling obstruction. -->
<!-- DESIGN-NOTE: Keep the paper simultaneous and impact-only. Treat \(u_t\) as given; do not introduce VAR lag equations, dynamic IRFs, or horizon-specific sign restrictions in this version. -->
<!-- SOURCE-TRAIL: Use M67 for the rebuilt unit-variance residual-noise Figure 1. -->

## 3. Drautzburg-Wright Refinement Under Noise

The previous section used only second moments. Drautzburg-Wright-style
refinement adds higher moments to exploit non-Gaussian structural shocks. The
logic in the no-noise case is easiest to see from the recovered shocks
\(e_t(B)=B^{-1}u_t\). A candidate can satisfy the second-moment restrictions in
\(\mathcal S_0\), so that the recovered shocks have covariance \(I\), while
still mixing the independent structural shocks. DW refinement keeps the
second-moment sign set but removes candidates whose recovered shocks are
uncorrelated and dependent.

<!-- SOURCE-TRAIL: M52 rebuilt the simulation code with the M49 source-correct bivariate Drautzburg-Wright GMM1 higher-moment menu plus a separate B-plane covariance screen. -->

DW measures this remaining dependence with third- and fourth-order
co-moments of the recovered shocks. With the same recovered-shock notation as
Section 2, the bivariate GMM1 higher-moment menu is

\begin{equation}
g_{DW,1}(B)=
\begin{bmatrix}
E\{e_{1t}(B)^2e_{2t}(B)\}\\
E\{e_{1t}(B)e_{2t}(B)^2\}\\
E\{e_{1t}(B)^3e_{2t}(B)\}\\
E\{e_{1t}(B)^2e_{2t}(B)^2\}-1\\
E\{e_{1t}(B)e_{2t}(B)^3\}
\end{bmatrix}.
\end{equation}

The corresponding GMM2 menu drops only the symmetric fourth product
\(E\{e_{1t}(B)^2e_{2t}(B)^2\}-1\), which allows the two structural shocks to be
driven by the same volatility process.

In the no-noise model, \(g_{DW,1}(B_0)=0\). A sample DW inversion refines the
second-moment set by keeping candidates that pass both the unit-variance
second-moment test and the higher-moment test:

\begin{equation}
\mathcal D_T(c_2,c_S)=
\left\{
B\in\mathcal S_{J,T}(c_2):\quad
J_{S,T}(B)=T\widehat g_{DW,T}(B)'\widehat W_{S,T}
\widehat g_{DW,T}(B)\le c_S
\right\}.
\label{eq:standard-dw-j-test-inversion}
\end{equation}

With the usual efficient weighting matrix, \(J_{S,T}(B_0)\) has a pointwise
\(\chi^2_5\) limit under the no-noise GMM1 null, so \(c_S\) can be chosen as a
chi-square critical value for the five higher-moment entries. The important
object is the refinement: \(\mathcal D_T(c_2,c_S)\) is a subset of
\(\mathcal S_{J,T}(c_2)\) that discards candidates whose recovered shocks are
uncorrelated but still dependent.

This is useful under the maintained no-noise null. Under residual noise, it can
produce a narrow and misleading set. Section 2 already showed why \(B_0\) is
generally shifted out of \(\mathcal S_0\) when the no-noise unit-variance
moments are applied to noisy residuals. Since DW refinement is a refinement of
that second-moment set, the refined set can become smaller while still missing
\(B_0\). The second row of Figure 1 shows this warning in the unit-variance
projection: in the no-noise column, non-Gaussianity sharpens the sign set;
once residual noise is added, the standard-DW projection can remain visually
sharp while the full true impact matrix fails the standard no-noise test.

<!-- SOURCE-TRAIL: Use Drautzburg-Wright, higher-moment SVAR caution sources, and the noisy-residual synthesis. -->
<!-- SOURCE-TRAIL: Use `derivations/standard-dw-j-test-under-noise.md` for the M25 J-test inversion result: rich-stack generic emptying, structural-rescaling exceptions, finite-moment aliases, and least-rejected pseudo-candidates. -->
<!-- SOURCE-TRAIL: Use `derivations/m47-standard-dw-proof-gate-audit.md` for the M47 conditional pass: rich-stack/ICA proof gate, compactness condition, structural-coordinate rescaling exception, and finite-GMM1 alias limitation. -->
<!-- SOURCE-TRAIL: Use `derivations/m49-dw-source-and-noisy-moment-audit.md` for the source-correct bivariate GMM1/GMM2 moment menus and `simulations/m52_source_correct_evidence.md` for the implemented GMM1 rebuild. -->

## 4. Noise-Robust Sign and DW Sets

The robust construction begins by changing the null model for sign
restrictions. Instead of requiring the residual covariance to be explained
entirely by structural shocks, the researcher allows part of each residual
variance to be idiosyncratic noise. The normalization remains
\(E[\varepsilon_t\varepsilon_t']=I\). We do not impose
\(\operatorname{diag}(B)=1\).

Let \(\Sigma_u=E[u_tu_t']\), with entries \(\sigma_{ij}\). Under the model
\(u_t=B_0\varepsilon_t+\eta_t\) and diagonal residual noise,

\begin{equation}
\Sigma_u = B_0B_0' + V,\qquad
V=\operatorname{diag}(\nu_1,\nu_2).
\end{equation}

For a candidate \(B\), introduce candidate residual-noise variances
\(\nu=(\nu_1,\nu_2)'\) and \(V(\nu)=\operatorname{diag}(\nu_1,\nu_2)\). These
variances are measured in the coordinates of the reduced-form residual
\(u_t\). The structural shocks have unit variances, but the structural signal
in residual coordinate \(i\) is \((B\varepsilon_t)_i\), whose variance is
\((BB')_{ii}\). The dimensionless noise share is therefore

\begin{equation}
\lambda_i(B,\nu)=\frac{\nu_i}{(BB')_{ii}}.
\end{equation}

The noise-robust second-order restriction is

\begin{equation}
\Psi_2(B,\nu)
=\operatorname{vech}\{\Sigma_u-BB'-V(\nu)\}=0,
\qquad
0\le \lambda_i(B,\nu)\le \rho,\quad i=1,2.
\label{eq:relative-noise-covariance-screen}
\end{equation}

Equivalently, write \(\nu_i(B,\lambda)=\lambda_i(BB')_{ii}\) with
\(\lambda_i\in[0,\rho]\). This is the clean derivation of the
residual-noise-to-signal screen. The matrix \(\Sigma_u-BB'\) is the residual
covariance left over after candidate structural signal \(BB'\) is removed. In
the diagonal-noise model, that leftover covariance must be diagonal and
nonnegative; the ratio bound is entrywise. A direct absolute cap
\(0\le\nu_i\le\rho\) would be a different restriction unless the residual
coordinates were separately standardized. The sample version replaces
\(\Sigma_u\) by \(\widehat\Sigma_u=T^{-1}\sum_t u_tu_t'\).

The next step is to regain some of the efficiency lost by allowing noise. Keep
the same recovered-shock notation as before:

\begin{equation}
e_t(B)=B^{-1}u_t
=B^{-1}B_0\varepsilon_t+B^{-1}\eta_t .
\end{equation}

For a candidate pair \((B,\nu)\) satisfying the second-order model, the
covariance of the recovered residual is the parameter-implied matrix

\begin{equation}
\Omega_e(B,\nu)
=E[e_t(B)e_t(B)']
=I+B^{-1}V(\nu)B^{-1'} .
\end{equation}

Write its entries as \(\omega_{ij}(B,\nu)\). These entries are not estimated as
separate sample plug-ins inside the fourth-order moments. They are smooth
functions of the candidate impact matrix and residual-noise variances.

The robust higher-moment route uses the following maintained condition.

*Assumption 1 (`ass:gaussian-residual-noise`, robust-noise condition). The
residual noise is independent of the structural shocks and Gaussian. Therefore
every linear transform \(B^{-1}\eta_t\) contributes only through first and
second moments. This assumption makes the displayed transformed higher-order
moment conditions robust to Gaussian noise; it does not make recovered-shock
variances or recovered-shock covariances equal to their no-noise targets.*

Under Assumption 1, \(B_0^{-1}\eta_t\) is Gaussian. Gaussian variables have no
cumulants above order two, and cumulants of independent sums add. Since the
structural shocks are mutually independent, every mixed higher cumulant of
\(e_t(B_0)=\varepsilon_t+B_0^{-1}\eta_t\) vanishes. This is the population
reason the robust higher-moment restrictions hold at \(B_0\).

For third-order entries, the mixed cumulants are just centered third moments,
so the restrictions can be written as \(E\{e_1(B)^2e_2(B)\}=0\) and
\(E\{e_1(B)e_2(B)^2\}=0\). Fourth-order entries subtract the covariance
products implied by \(\Omega_e(B,\nu)\). The Gaussian-noise-blind moment stack
is

\begin{equation}
G_H(B,\nu)=
\begin{bmatrix}
E\{e_1(B)^2e_2(B)\}\\
E\{e_1(B)e_2(B)^2\}\\
E\{e_1(B)^3e_2(B)\}-3\omega_{11}(B,\nu)\omega_{12}(B,\nu)\\
E\{e_1(B)^2e_2(B)^2\}
-\omega_{11}(B,\nu)\omega_{22}(B,\nu)-2\omega_{12}(B,\nu)^2\\
E\{e_1(B)e_2(B)^3\}-3\omega_{22}(B,\nu)\omega_{12}(B,\nu)
\end{bmatrix}.
\label{eq:dw-higher-cumulant-moment-stack}
\end{equation}

The first two entries are centered third-product conditions. The last three
entries are fourth-order conditions with covariance-product subtractions. The
important change is that the covariance terms are parameter-implied functions
of \((B,\nu)\), not sample averages multiplied after the fact. This makes the
sample criterion a standard GMM criterion in the enlarged parameter vector.
For example, the \(1222\) row becomes

\begin{equation}
\widehat g_{1222,T}(B,\nu)
=T^{-1}\sum_t \widetilde e_{1t}(B)\widetilde e_{2t}(B)^3
-3\omega_{12}(B,\nu)\omega_{22}(B,\nu),
\end{equation}

where tildes denote sample-centering of the recovered residuals.

Combine the second-order and higher-order restrictions in one moment vector

\begin{equation}
\psi_t(B,\nu)=
\begin{bmatrix}
\operatorname{vech}\{u_tu_t'-BB'-V(\nu)\}\\
e_{1t}(B)^2e_{2t}(B)\\
e_{1t}(B)e_{2t}(B)^2\\
e_{1t}(B)^3e_{2t}(B)-3\omega_{11}(B,\nu)\omega_{12}(B,\nu)\\
e_{1t}(B)^2e_{2t}(B)^2
-\omega_{11}(B,\nu)\omega_{22}(B,\nu)-2\omega_{12}(B,\nu)^2\\
e_{1t}(B)e_{2t}(B)^3-3\omega_{22}(B,\nu)\omega_{12}(B,\nu)
\end{bmatrix}.
\end{equation}

Let \(\widehat g_T(B,\nu)=T^{-1}\sum_t\psi_t(B,\nu)\). A standard efficient
GMM inversion uses

\begin{equation}
J_T(B,\nu)
=T\widehat g_T(B,\nu)'\widehat W_T\widehat g_T(B,\nu),
\end{equation}

where \(\widehat W_T\) is the inverse of the estimated covariance matrix of
\(\psi_t(B,\nu)\), usually obtained from a preliminary GMM step. The reported
noise-robust set projects this enlarged GMM confidence set onto \(B\):

\begin{equation}
\mathcal R_T(c;\rho)=
\left\{
B:\ \exists \lambda\in[0,\rho]^2\ \text{such that}\ R(B)\ge0,
J_T(B,\nu(B,\lambda))\le c
\right\}.
\end{equation}

This display treats the sign screen and the noise-share bound as hard
maintained restrictions. Computationally, for a fixed \(\rho\), the researcher
searches over \(B\) and over admissible \(\lambda\), sets
\(\nu_i(B,\lambda)=\lambda_i(BB')_{ii}\), computes the full GMM criterion, and
keeps \(B\) if at least one admissible \(\lambda\) has
\(J_T(B,\nu(B,\lambda))\le c\). Showing several values of \(\rho\) means
repeating this projected inversion as a sensitivity exercise.

At the true parameter \((B_0,\nu_0)\), the second-order block is zero by
\(\Sigma_u=B_0B_0'+V(\nu_0)\), and the higher-order block is zero by the
Gaussian-noise cumulant argument. This construction is not a no-noise
covariance factorization and not a diagonal impact normalization. It is a
standard GMM formulation of the noise-robust null, with residual-noise
variances treated as nuisance parameters and projected out when reporting the
set for \(B\).

<!-- SOURCE-TRAIL: Use `derivations/dw-noise-robust-moments.md`, `derivations/m40-variance-ratio-robust-dw-screen-audit.md`, `derivations/m66-noise-ratio-bound-grid-algorithm.md`, Drautzburg-Wright, and higher-moment GMM sources. -->
<!-- TODO-NOTE: M67 rebuilds Figure 1 under the unit-variance projected GMM algorithm. Figure 2, Figure 3, and the Monte Carlo code remain historical until M65 rebuilds them. -->
<!-- TODO-NOTE: The exact projection critical value for \(\mathcal R_T(c;\rho)\) needs a compact inference note after the enlarged GMM implementation is audited. -->

## 5. Monte Carlo Robustness Check

This section is partly rebuilt. Figure 1 now uses the unit-variance projected
GMM route from Section 4. Figures 2-3 and Table 1 still record the pre-M64
evidence path, which used the old normalized B-plane chart. Before this
section is shareable as a complete evidence package, the non-Gaussianity grid,
the sample-size grid, and the Monte Carlo table must be regenerated under the
same unit-variance implementation.

<!-- SOURCE-TRAIL: Use M27 for the common reporting chart, accepted shares, overlap, warning-rate, and truth-inclusion diagnostics. -->

### 5.1 Residual-Noise Grid

Figure 1 keeps the reader job of the old residual-noise grid: residual noise
increases across columns. The chart is now the projection to
\((B_{12},B_{21})\), while \(B_{11}\), \(B_{22}\), and
\(\lambda\in[0,\rho]^2\) are searched internally. A star means the full true
\(B_0\) passes that row's test; an x means the true projected coordinate may
sit in a shaded cell only because another diagonal pair at that projection is
accepted.

![Figure 1. Unit-variance projected residual-noise grid.](figures/fig_sign_dw_unit_variance_noise_grid.png)

**Figure 1. Unit-variance residual-noise grid.** The robust row uses the M66
restriction \(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\) and reports the
projection of accepted \((B,\lambda)\) pairs. The plotted \(J\) statistics use
fixed one-step GMM weights for this diagnostic figure; the final projected
critical-value choice remains part of M65.

<!-- SOURCE-TRAIL: Figure file `figures/fig_sign_dw_unit_variance_noise_grid.png`; generator `simulations/sign_dw_unit_variance_noise_grid_figure.py`; diagnostic note `simulations/sign_dw_unit_variance_noise_grid_figure.md`; machine-readable output `simulations/output/sign_dw_unit_variance_noise_grid_figure.json`; M66 derivation `derivations/m66-noise-ratio-bound-grid-algorithm.md`; M49 source audit `derivations/m49-dw-source-and-noisy-moment-audit.md`; M56 generated-moment audit `derivations/m56-robust-cumulant-gmm-generated-moment-audit.md`. -->

M52 checked the finite-sample logic for the old source-correct statistic. Its
numbers remain useful for audit history, but they are not final evidence for
the M66 unit-variance GMM object.

### 5.2 Non-Gaussianity Grid

The displayed Figure 2 is also historical after M64 and M66. The M65
replacement should keep the same limitation check--residual noise fixed,
structural non-Gaussianity weakened across columns--but the robust row must use
the same projected \((B,\lambda)\) set as Figure 1.

![Figure 2. Non-Gaussianity grid.](figures/fig_sign_dw_robust_nongaussianity_grid.png)

**Figure 2. Historical pre-M64 non-Gaussianity grid.** The current image is
retained only as an audit diagnostic. The active replacement must use the M66
\(\lambda\)-bounded projected GMM algorithm.

<!-- SOURCE-TRAIL: Figure file `figures/fig_sign_dw_robust_nongaussianity_grid.png`; generator `simulations/sign_dw_robust_nongaussianity_grid_figure.py`; M52 validation note `simulations/m52_source_correct_evidence.md`. -->

This limitation matters for the paper's recommendation. A wide robust set is
not a failed diagnostic by itself. It records the information deliberately lost
by dropping the noisy recovered-shock covariance target and profiling diagonal
noise variances. The warning object is directional: standard-DW accepted mass
outside the robust-DW set, or standard-DW rejection of the truth in simulations
when robust DW still contains it.

<!-- SOURCE-TRAIL: Use `manuscript/derivations/dw-robust-comparison-diagnostic.md` for the directional interpretation rule. -->

### 5.3 Sample-Size Grid

The displayed Figure 3 is historical after M64 and M66. The M65 replacement
should keep the same finite-sample question--residual noise and structural
non-Gaussianity fixed while \(T\) varies--but the robust row must again report
the projection of accepted \((B,\lambda)\) pairs.

![Figure 3. Sample-size grid.](figures/fig_sign_dw_sample_size_robust_grid.png)

**Figure 3. Historical pre-M64 sample-size grid.** The current image is
retained only as an audit diagnostic. The active replacement must use the M66
\(\lambda\)-bounded projected GMM algorithm.

<!-- SOURCE-TRAIL: Figure file `figures/fig_sign_dw_sample_size_robust_grid.png`; generator `simulations/sign_dw_sample_size_robust_grid_figure.py`; M52 validation note `simulations/m52_source_correct_evidence.md`. -->

### 5.4 Monte Carlo Table

Table 1 reports the M52 source-correct Monte Carlo evidence under the primary
researcher-facing chi-square cutoffs. The standard row uses the bivariate DW
GMM1 higher-moment menu and the separate no-noise covariance screen. The robust
row uses the variance-ratio proposal, and the covariance-decomposition screen
is applied both to accepted grid points and to the truth-inclusion calculation.
`S truth` and `R truth` are true-\(B_0\) inclusion rates for standard DW and
robust DW. `R feasible` is the fraction of evaluation samples in which the
hard variance-ratio screen is feasible at the true \(B_0\). `S share` and
`R share` are accepted-set shares on the normalized grid.
`d_S_not_subset_R` is the directional share of standard-DW accepted mass not
supported by robust DW.

**Table 1. M52 chi-square-primary Monte Carlo comparison.** Entries are
evaluation averages from 24 replications per scenario on a \(41\times 41\)
grid, with 60 truth-calibration replications retained as audit output. The
standard-DW chi-square cutoff is \(9.236\) for five GMM1 higher moments, plus
the separate covariance-screen cutoff \(2.706\). The robust cutoff is \(9.236\)
for five generated higher-cumulant moments with central-delta weighting.

| Scenario | S truth | R truth | R feasible | S share | R share | d_S_not_subset_R | Warning rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| No noise, strong moments | 0.792 | 0.875 | 0.958 | 0.017 | 0.027 | 0.204 | 0.375 |
| Moderate Gaussian noise | 0.417 | 0.875 | 1.000 | 0.027 | 0.057 | 0.174 | 0.583 |
| High Gaussian noise | 0.000 | 0.833 | 0.958 | 0.029 | 0.062 | 0.161 | 0.875 |
| Weak structural higher moments | 0.667 | 0.833 | 0.958 | 0.101 | 0.157 | 0.202 | 0.333 |
| Gaussian structural shocks | 0.458 | 0.875 | 1.000 | 0.112 | 0.173 | 0.175 | 0.625 |
| Skewed residual noise | 0.458 | 0.875 | 1.000 | 0.020 | 0.043 | 0.214 | 0.542 |

<!-- SOURCE-TRAIL: M52 rebuilt run in `simulations/m52_source_correct_evidence.md` and machine-readable output `simulations/output/m52_source_correct_evidence.json`. Historical M45 outputs remain in `simulations/m45_variance_ratio_evidence.md` and `simulations/output/m45_variance_ratio_evidence.json` but used the old standard-DW hybrid and approximate robust weighting. Historical M29 outputs remain in `simulations/m29_calibrated_monte_carlo.md` but used the superseded diagonal-anchor robust row. -->

The skewed-residual-noise row is a stress case, not validation of the robust
Gaussian-noise route. It violates Assumption 1, so its favorable truth-inclusion
numbers should not be read as evidence that the same cumulant argument covers
non-Gaussian residual noise without additional restrictions.

The audit rows stay secondary. The no-noise repeated calibration is a size
check, while the scenario-truth calibration is an oracle diagnostic. In the
high-noise case, scenario-truth calibration raises the standard-DW accepted
share to \(0.125\), showing the calibration cost of forcing the misspecified
standard statistic to cover the truth. These audit rows are not the applied
procedure being critiqued.

<!-- SOURCE-TRAIL: Use KnowledgeVault replication assets only as starting points; final figure commands must live in `replication/README.md`. -->
<!-- SOURCE-TRAIL: Use `derivations/dw-robust-comparison-diagnostic.md` for the M27 definitions of the reported standard-DW set, robust-DW set, critical-value convention, directional overlap metric, and interpretation boundaries. -->
<!-- DESIGN-NOTE: M52 keeps standard pointwise chi-square critical values as the primary applied benchmark; the robust row now uses full central-moment delta weighting for generated cumulants. Repeated-sample and oracle cutoffs remain audit rows only. -->
<!-- TODO-NOTE: In future simulation tables, report accepted shares, empty-set frequencies, Jaccard overlap, standard-DW mass outside robust-DW, truth inclusion, and least-rejected candidates. -->
<!-- TODO-NOTE: Report inconclusive and weak cases honestly. -->

## 6. Conclusion

This paper studies a narrow robustness problem in sign-restricted SVARs. If the
observed reduced-form residual contains additive idiosyncratic noise, the usual
covariance factor is a factor of \(B_0B_0'+V\), not \(B_0B_0'\). The standard
sign-restricted set can therefore be a noisy pseudo-set, and a
Drautzburg-Wright-style higher-moment refinement can sharpen that pseudo-set
instead of the structural impact matrix.

The proposed response is diagnostic. Report the standard DW set beside a
variance-ratio robust DW set that allows diagonal Gaussian residual noise,
uses only Gaussian-noise-blind higher cumulants for refinement, and adds
second-moment precision only through an explicit residual-noise-to-signal
bound. Agreement between the two sets makes the standard refinement less
suspect. Divergence, especially standard-DW precision that is not supported by
the robust set, should be read as a warning about covariance-target
misspecification rather than as evidence of sharper structural learning.

The first version deliberately keeps the scope small: a bivariate simultaneous
impact model, no empirical application, no dynamic impulse responses, and no
claim that the robust comparison proves literal measurement error. The next
step is to audit the standard-DW proof and move the figure and table code into
a self-contained replication package.

## References

TODO: Use the citation style chosen in `manuscript-rules.md` and the BibTeX
snapshot in `../bibliography/references.bib`.
