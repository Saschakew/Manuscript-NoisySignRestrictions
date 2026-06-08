# Noise-Robust Sign-Restricted SVARs

Author: TODO

Date: 2026-06-05

## Abstract

\comment{I will leave the old abstract below and sketch a new abstract here:
Sign restrictions allow to set identify the impact of structural shocks. In a  non-Gaussian SVAR, the identified set can be sharpened by using information in higher-moments.
This paper shows that that idiosyncratic noise in the SVAR can lead to a bias, such that the identified set no longer contains the true impact matrix.
Without accounting for the noise, refinments based on non-Gaussianity worsen the problem, sharpen the wrong target, and return a
small accepted set that looks more informative than it is.
We propose a novel refinement of sign restricted SVARs, which seperates non-Gaussian structural shocks from Gaussian noise. 
...we still need to mention that the user can specify the max information noise ratio to sharpen the idenfied set...we also need to preview the performance gains of our methods based on our simulation...
}

Sign-restricted SVARs are usually presented as qualitative restrictions, but
the set they report is built from a covariance target. This paper studies the
simultaneous impact problem when the reduced-form residual is contaminated by
additive residual noise. In that case the usual sign-restricted set rotates a
factor of \(B_0B_0' + V\), not a factor of the structural covariance \(B_0B_0'\), so
the population sign set becomes a noisy pseudo-set. Drautzburg-Wright-style
higher-moment refinement remains well motivated under its no-noise maintained
null, but under residual noise it can sharpen the wrong target and return a
small accepted set that looks more informative than it is. The paper proposes a
validity-first robust comparison set that drops invalid zero-covariance
anchors and uses mixed higher-cumulant moments of normalized candidate shocks.
The M0034 scale correction supersedes the earlier diagonal-anchor evidence;
the M0036 relative-noise variant shows that explicit upper bounds on residual
noise variances relative to structural-shock variances can recover precision.
The recommendation is therefore
diagnostic: report standard DW and robust DW together, and treat standard-DW
precision unsupported by the robust set as a warning rather than as evidence of
sharper structural learning.

<!-- SOURCE-TRAIL: Use the M0036 relative-noise Figure 1 candidate, the M40 screen audit, the M0035 absolute-bound comparison, the M0034 pure robust variant, and the M24 higher-cumulant derivation. Treat M0030/M37/M28/M29 diagonal-anchor evidence as superseded until M43-M45 rebuilds the evidence package. -->
<!-- CONTRIBUTION-NOTE: The abstract's original contribution is the residual-noise pseudo-set warning and the DW-versus-robust-DW comparison diagnostic. -->

## 1. Introduction

\comment{Maybe we can start with an introduction like this: The underlying idea of a sign restricted SVAR is to find the set of impact matrices which is in line with economically motivated sign restrictions on the impact matrix and uncorrelated structural shocks (the sentence is not good...but i hope you get the idea, to state intuitively what sign restrictions do. important, explaint that it relies on finding uncorrelated structural shocks, because thats the thing which leads to a bias once we allow for noise but dont take care of it in the sign restriction step). 
In contrast to other identification approaches like zero-restrictions or proxy variables, sign restrictions impose very little structure, the sign of the shock's impact and the assumption of uncorrelated shocks, and are thus regarded as robust, because they leave little room for misspecification (again, the sentence is not good but i hope you get the point).
 } 

Applied sign-restricted SVAR work often begins after the reduced-form residual
\(u_t\) has already been estimated. The next step is usually an impact
decomposition: find candidate structural impact matrices whose implied signs
match the researcher's qualitative restrictions. Under the no-noise benchmark,
the reduced-form covariance is \(\Sigma_u=B_0B_0'\), so rotating a covariance
factor is a natural way to explore observationally equivalent structural
models. This paper asks what happens when the residual being decomposed is not
only structural signal but also contains additive residual noise.

<!-- SOURCE-TRAIL: Use sign-restriction overview sources, `kilian2016StructuralVectorAutoregressiveAnalysis93b03b`, and `arias2018InferenceBasedStructuralVector`. -->

The issue is not that sign restrictions are quantitative after all. The issue
is that the qualitative filter is applied to a covariance object. With
\(u_t=B_0\varepsilon_t+\eta_t\) and \(E(\eta_t\eta_t')=V\), the covariance factor
being rotated solves \(P_*P_*'=B_0B_0' + V\). Unless the noise happens to be
absorbed by a harmless structural-coordinate rescaling, the resulting sign set
is a pseudo-set: it is internally coherent for the noisy covariance, but it is
not the no-noise economic set one would have reported from \(B_0B_0'\).

<!-- SOURCE-TRAIL: Use `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md` and the M25 column-rescaling obstruction. -->

Drautzburg-Wright-style refinement then creates a sharper version of the same
problem. Under its maintained no-noise null, independence restrictions on
recovered shocks are a useful way to refine a sign-admissible set. Under
residual noise, however, the recovered shocks from a noisy covariance-factor
candidate are not the structural shocks. A higher-moment test can therefore
reject the true normalized impact matrix while accepting a small region around
a least-rejected noisy target. The paper treats this as a robustness problem,
not as a criticism of the no-noise DW procedure on its own terms.

<!-- SOURCE-TRAIL: Use `drautzburg2023RefiningSetIdentificationVars` for the maintained-null comparator and `manuscript/derivations/standard-dw-j-test-under-noise.md` for the M25 working misspecification result. -->
<!-- TODO-NOTE: Do not promote the generic emptying result to theorem wording until the M25 proof audit is complete. -->

The constructive move is to report a second, deliberately more conservative
set. In a common normalized impact chart, the robust DW set applies the same
sign screen but drops the recovered-shock zero-covariance moment and the
superseded diagonal-anchor \(u\) covariance moment. It keeps mixed
higher-cumulant restrictions of \(z_t(B)=B^{-1}u_t\). If the researcher is
willing to bound diagonal residual-noise variances, the recovered-shock
covariance can enter as an inequality screen rather than as a zero moment.
Under the maintained Gaussian residual-noise route, additive Gaussian noise
changes contaminated second moments but not the higher cumulants used in the
pure robust stack. The price is explicit: precision comes either from higher
moments or from substantive noise-scale bounds.

<!-- SOURCE-TRAIL: Use `manuscript/derivations/dw-noise-robust-moments.md`, `manuscript/derivations/dw-robust-comparison-diagnostic.md`, and higher-moment SVAR caution sources. -->

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
residual noise and shows the main warning: the sign/covariance set moves,
standard DW can exclude the true normalized impact matrix, and robust DW
remains wider while containing it once explicit relative noise-scale
information is added. Figure 2 holds residual noise fixed and weakens
structural non-Gaussianity, showing the limitation that robust DW's
higher-cumulant component needs informative higher moments. Table 1 must be
rebuilt after the Figure 2/Figure 3 and M28/M29-style evidence rebuild.

<!-- SOURCE-TRAIL: Use M0036 and the M40 audit for the current Figure 1 candidate, plus M45 for the rebuilt Figure 2/Figure 3 and Monte Carlo evidence. -->

<!-- SOURCE-TRAIL: Use sign-restriction overview sources, Drautzburg-Wright, and the noisy-residual synthesis. -->
<!-- CONTRIBUTION-NOTE: The original contribution is the noise-bias warning plus the standard-DW versus robust-DW comparison. -->

## 2. Noisy Sign Sets

The first object is the residual being decomposed. The paper does not model
VAR lag estimation, dynamic responses, or horizon-specific signs in the main
text. It starts from an already obtained reduced-form residual and asks which
impact matrices can be reported from it. The maintained simultaneous model is

\begin{equation}
u_t = B_0\varepsilon_t+\eta_t,\qquad
E(\varepsilon_t)=0,\qquad
E(\varepsilon_t\varepsilon_t')=I,
\qquad
E(\eta_t\eta_t')=V .
\end{equation}

The structural shocks and residual noise are uncorrelated, and the first
version keeps diagonal residual noise as the economic interpretation used in
the figures. The observed covariance is therefore

\begin{equation}
\Sigma_u = E(u_tu_t') = B_0B_0' + V .
\end{equation}

*Definition 1 (`def:diagonal-noise-svar`, additive-noise impact model).* *The
first-version model is the bivariate simultaneous residual system
\(u_t=B_0\varepsilon_t+\eta_t\), where \(B_0\) is nonsingular, the structural
shocks have zero mean, unit variances, and mutually independent components,
and the additive residual noise is mean zero, independent of the structural
shocks, and has covariance \(V\). The main figures use diagonal \(V\), but the
impact-only scope does not include VAR lag dynamics or impulse-response
horizons.*

Under the no-noise benchmark, a sign-restricted SVAR rotates a factor of
\(B_0B_0'\). Let \(P_0P_0'=B_0B_0'\) and let \(R(B)\ge 0\) denote the chosen
sign screen in the normalized impact chart. The no-noise economic set is

\begin{equation}
\mathcal S_0 =
\{P_0Q: Q'Q=I,\ R(P_0Q)\ge 0\}.
\end{equation}

With residual noise, the standard procedure instead rotates a factor of the
observed covariance. If \(P_*P_*'=\Sigma_u=B_0B_0'+V\), the reported
population sign set is

\begin{equation}
\mathcal S_* =
\{P_*Q: Q'Q=I,\ R(P_*Q)\ge 0\}.
\end{equation}

*Definition 2 (`def:noisy-sign-pseudo-set`, noisy sign pseudo-set).* *The
noisy sign pseudo-set is the population sign-restricted set \(\mathcal S_*\)
obtained by rotating a factor of \(B_0B_0'+V\) rather than a factor of
\(B_0B_0'\). It is a valid set for the noisy covariance target and generally
not the same object as the no-noise economic sign set \(\mathcal S_0\).*

The distinction is mechanical but consequential. If the noisy factor could be
interpreted as harmless structural-column rescaling, there would be a positive
diagonal matrix \(D\) such that

\begin{equation}
B_0D^2B_0' = B_0B_0' + V .
\end{equation}

Equivalently, residual noise would have to satisfy the structural-coordinate
rescaling condition

\begin{equation}
B_0(D^2-I)B_0' = V,
\qquad
D^2-I = B_0^{-1}VB_0^{-1'} .
\label{eq:column-rescaling-obstruction}
\end{equation}

For generic residual noise this transformed matrix is not diagonal and cannot
be absorbed by column scales. The sign screen is then applied to the wrong
covariance shape. This is why the first row of Figure 1 is already informative:
before higher moments enter, residual noise moves the set being filtered.

*Proposition 1 (`prop:noisy-sign-pseudo-set`, noisy sign pseudo-set).* *If
\(V\neq 0\), the standard population sign-restricted set \(\mathcal S_*\)
rotates a factor of \(B_0B_0'+V\). Except in special cases where
\(B_0^{-1}VB_0^{-1'}\) is diagonal up to the accepted column-label convention,
\(\mathcal S_*\) differs from the no-noise economic set \(\mathcal S_0\).
Thus the reported sign set is generally a noisy covariance pseudo-set rather
than the structural set one would have obtained from \(B_0B_0'\).*

This proposition is intentionally modest. It does not say sign restrictions
are conceptually wrong. It says that the qualitative sign filter inherits the
covariance target supplied to it. If that target is noisy, the population set
can be biased before any finite-sample uncertainty is considered.

<!-- SOURCE-TRAIL: Use the proposal note, `Noisy residuals in recursive and sign-restricted SVARs.md`, and the M25 column-rescaling obstruction. -->
<!-- DESIGN-NOTE: Keep the paper simultaneous and impact-only. Treat \(u_t\) as given; do not introduce VAR lag equations, dynamic IRFs, or horizon-specific sign restrictions in this version. -->
<!-- TODO-NOTE: Later polish should decide whether Proposition 1 receives a short proof in the main text or a proof sketch in an appendix. -->

## 3. Standard DW Under Residual Noise

The standard Drautzburg-Wright-style refinement is best understood as a
maintained-null procedure. Under the no-noise model, a covariance factor
\(P_0\) can be rotated into a candidate impact matrix, and the recovered shocks
at the correct rotation are the structural shocks. Higher-moment independence
restrictions are then a meaningful way to refine a sign-admissible set.

With residual noise, the same recovered object is different. A standard
candidate uses \(P_*P_*'=\Sigma_u\), so for each orthogonal \(Q\),

\begin{equation}
B(Q)=P_*Q,
\qquad
e_t(Q)=B(Q)^{-1}u_t=Q'P_*^{-1}u_t .
\end{equation}

These recovered shocks are normalized for the noisy covariance:

\begin{equation}
\operatorname{Var}\{e_t(Q)\}=I .
\end{equation}

That normalization is exactly the problem. It is true because \(P_*P_*'\)
factors \(B_0B_0'+V\), not because \(B(Q)\) is a structural impact matrix.
Substituting the additive-noise model gives

\begin{equation}
e_t(Q)=M(Q)\varepsilon_t+\zeta_t(Q),
\qquad
M(Q)=Q'P_*^{-1}B_0,\qquad
\zeta_t(Q)=Q'P_*^{-1}\eta_t .
\end{equation}

If the residual noise is Gaussian, it does not add higher cumulants, but the
mixing matrix \(M(Q)\) is generally not diagonal. A rich higher-moment
independence stack can vanish only when the candidate recovers structural
coordinates up to scale, sign, and label. This requires

\begin{equation}
M(Q)=D\Pi,
\end{equation}

where \(D\) is nonsingular diagonal and \(\Pi\) is a signed permutation matrix
consistent with the sign-label convention. Combining this with the covariance
factorization imposes

\begin{equation}
B_0^{-1}VB_0^{-1'}=\Pi'D^{-2}\Pi-I .
\end{equation}

The right side is diagonal up to labels. Hence, outside structural-coordinate
rescaling cases and finite-moment aliases, no covariance-whitened standard-DW
candidate can both factor the noisy covariance and recover independent
structural shocks.

Let \(\widehat g_{S,T}(Q)\) be the standard no-noise moment stack, including
the recovered-shock covariance moment and the finite higher-moment
independence restrictions. The sample inversion is

\begin{equation}
\mathcal Q_{DW,T}(c_S)=
\left\{
Q: R(P_*Q)\ge 0,\quad
J_{S,T}(Q)=
T\widehat g_{S,T}(Q)'\widehat W_{S,T}\widehat g_{S,T}(Q)
\le c_S
\right\}.
\label{eq:standard-dw-j-test-inversion}
\end{equation}

In population, the corresponding criterion is
\(J_{S,\infty}(Q)=g_{S,\infty}(Q)'Wg_{S,\infty}(Q)\). When the population
moment vector is bounded away from zero on the sign-admissible set, the
accepted set empties asymptotically for fixed pointwise critical values. In
finite samples, however, the researcher can still see a small accepted region
near

\begin{equation}
Q^\dagger\in\arg\min_Q J_{S,\infty}(Q),
\end{equation}

which is a least-rejected noisy pseudo-candidate, not evidence that residual
noise has been solved.

*Proposition 2 (`prop:standard-dw-misspecification`, standard DW under
residual noise).* *In the simultaneous residual model, standard DW inversion
searches over factors of \(\Sigma_u=B_0B_0'+V\). With independent Gaussian
residual noise, independent non-Gaussian structural shocks, and a rich
higher-moment independence stack, the population accepted set is generically
empty unless residual noise is equivalent to a diagonal structural-coordinate
rescaling, up to sign and label aliases. With finite moment stacks, accidental
zeros can instead produce pseudo-candidates. When no population zero exists,
finite-sample inversion can still look falsely precise by concentrating near a
least-rejected noisy target \(Q^\dagger\).*

The proposition should remain at this sketch level until the M25 proof audit
is complete. The important reader-facing point is already available: standard
DW is not being criticized under its own no-noise null. The misspecification
comes from applying that null to residuals whose covariance target is
\(B_0B_0'+V\).

<!-- SOURCE-TRAIL: Use Drautzburg-Wright, higher-moment SVAR caution sources, and the noisy-residual synthesis. -->
<!-- SOURCE-TRAIL: Use `derivations/standard-dw-j-test-under-noise.md` for the M25 J-test inversion result: rich-stack generic emptying, structural-rescaling exceptions, finite-moment aliases, and least-rejected pseudo-candidates. -->
<!-- TODO-NOTE: Do not promote Proposition 2 beyond sketch wording until the M25 assumptions and exceptions are audited directly. -->

## 4. Robust DW Higher-Moment Set

The robust set changes the search space before it changes the moments. Instead
of rotating a factor of \(\Sigma_u\), it reports candidates in a fixed
normalized impact chart,

\begin{equation}
B(a,b)=
\begin{bmatrix}
1 & a\\
b & 1
\end{bmatrix},
\qquad
1-ab\neq 0 .
\end{equation}

The sign screen is imposed directly on \(B(a,b)\). For each candidate, define
transformed residuals

\begin{equation}
z_t(B)=B^{-1}u_t
=B^{-1}B_0\varepsilon_t+B^{-1}\eta_t .
\end{equation}

The maintained route is Gaussian residual noise.

*Assumption 1 (`ass:gaussian-residual-noise`, robust-noise condition).* *The
residual noise is independent of the structural shocks and Gaussian. Therefore
every linear transform \(B^{-1}\eta_t\) has zero cumulants above order two.
This assumption is what makes transformed higher cumulants robust; it does not
make recovered-shock variances or cross-covariances equal to their no-noise
targets.*

Let \(s_{ij}(B)=E\{z_i(B)z_j(B)\}\). The pure robust moment stack uses the
mixed third cumulants and mixed fourth cumulants of \(z_t(B)\):

\begin{equation}
G_H(B)=
\begin{bmatrix}
\kappa_{112}(B)\\
\kappa_{122}(B)\\
\kappa_{1112}(B)\\
\kappa_{1122}(B)\\
\kappa_{1222}(B)
\end{bmatrix}.
\label{eq:dw-higher-cumulant-moment-stack}
\end{equation}

With centered observations, the third cumulants are

\begin{equation}
\kappa_{112}(B)=E\{z_1(B)^2z_2(B)\},
\qquad
\kappa_{122}(B)=E\{z_1(B)z_2(B)^2\}.
\end{equation}

The fourth restrictions must be cumulants, not raw fourth moments:

\begin{equation}
\begin{aligned}
\kappa_{1112}(B)
&=E\{z_1(B)^3z_2(B)\}-3s_{11}(B)s_{12}(B),\\
\kappa_{1122}(B)
&=E\{z_1(B)^2z_2(B)^2\}
-s_{11}(B)s_{22}(B)-2s_{12}(B)^2,\\
\kappa_{1222}(B)
&=E\{z_1(B)z_2(B)^3\}-3s_{22}(B)s_{12}(B).
\end{aligned}
\end{equation}

The covariance terms \(s_{ij}(B)\) are nuisance ingredients needed to compute
fourth cumulants. They are not restrictions such as
\(s_{11}(B)=1\), \(s_{22}(B)=1\), or \(s_{12}(B)=0\). This is the main
difference from the standard DW recovered-shock covariance target.

The pure robust higher-cumulant set is

\begin{equation}
\mathcal R_{H,T}(c_H)=
\left\{
B\in\mathcal B_N:
R(B)\ge 0,\quad
T\widehat G_H(B)'\widehat W_{H,T}\widehat G_H(B)\le c_H
\right\},
\end{equation}

where \(\mathcal B_N\) is the nonsingular normalized chart after sign and label
conventions. Under Assumption 1, \(G_H(B_0)=0\) at the true normalized impact
matrix. This validity comes from cumulants of order three and higher. It does
not recover scale by itself and can be wide when the structural shocks have
weak higher moments.

*Definition 3 (`def:robust-dw-higher-moment-set`, robust DW higher-moment
set).* *The pure robust DW set is the sign-admissible inversion of the mixed
higher-cumulant statistic \(T\widehat G_H(B)'\widehat W_{H,T}\widehat G_H(B)\)
over the normalized candidate space \(\mathcal B_N\). It deliberately drops
the no-noise covariance factorization \(BB'=\Sigma_u\), the unit-variance
recovered-shock restrictions, and the recovered-shock zero-covariance moment.*

The M0034 scale correction matters here. In the diagonal-normalized chart,
writing the off-diagonal covariance as \(a+b\) is only valid if the structural
shock variances are fixed at one after normalization. That is a second scale
normalization. The variance-ratio proposal instead profiles the structural
shock variances and residual-noise variances for each candidate. Let
\(S\) denote the sample residual covariance and let
\(\operatorname{Var}(\varepsilon)=\operatorname{diag}(s_1,s_2)\) and
\(\operatorname{Var}(\eta)=\operatorname{diag}(\nu_1,\nu_2)\). For
\(B(a,b)\), the covariance-decomposition screen asks whether there exist
\(s_1,s_2,\nu_1,\nu_2\) such that

\begin{equation}
\begin{aligned}
S_{11} &= s_1+a^2s_2+\nu_1,\\
S_{12} &= bs_1+as_2,\\
S_{22} &= b^2s_1+s_2+\nu_2,\\
s_i &>0,\qquad 0\le \nu_i\le \rho s_i,\qquad \rho=0.5 .
\end{aligned}
\label{eq:relative-noise-covariance-screen}
\end{equation}

Equivalently, the diagonal covariance equations can be written as inequalities
after profiling \(\nu_i\):

\begin{equation}
\begin{aligned}
s_1+a^2s_2 &\le S_{11}\le (1+\rho)s_1+a^2s_2,\\
b^2s_1+s_2 &\le S_{22}\le b^2s_1+(1+\rho)s_2,\\
S_{12} &= bs_1+as_2 .
\end{aligned}
\end{equation}

The variance-ratio robust set intersects the pure higher-cumulant inversion
with this feasibility screen:

\begin{equation}
\mathcal R_{\rho,T}(c_H)=
\{B\in\mathcal R_{H,T}(c_H):
\eqref{eq:relative-noise-covariance-screen}\ \text{is feasible}\}.
\end{equation}

The bound \(\nu_i\le 0.5s_i\) is not a normalization. It is identifying
information: residual-noise variance in each coordinate is assumed to be at
most one half of the corresponding structural-shock variance after the
candidate impact normalization. That is why the robust row can regain
precision relative to the pure higher-cumulant fallback.

*Proposition 3 (`prop:robust-dw-higher-moment-validity`, robust higher-moment
validity).* *Under the normalized bivariate chart, independent structural
shocks, Assumption 1, and the local higher-cumulant rank condition that each
shock has at least one nonzero third or fourth cumulant in the stack, the true
normalized impact matrix has \(G_H(B_0)=0\). The variance-ratio set
\(\mathcal R_{\rho,T}\) adds the covariance-decomposition feasibility screen
as extra signal-to-noise information; it does not impose recovered-shock zero
covariance or the superseded \(S_{12}=a+b\) diagonal-anchor restriction.*

This proposition is the current constructive sketch, not a finished theorem.
The M40 audit conditionally clears the relative screen algebra and the
interpretation of the 50 percent noise-to-shock bound as identifying
information. It also warns that the hard equality-plus-inequality screen can
exclude the true candidate in finite samples, so M43-M45 still have to rebuild
the evidence before the paper treats this as a final robust-DW object.

<!-- SOURCE-TRAIL: Use `derivations/dw-noise-robust-moments.md`, `derivations/m40-variance-ratio-robust-dw-screen-audit.md`, `simulations/sign_dw_relative_noise_robust_grid_figure.md`, Drautzburg-Wright, and higher-moment GMM sources. -->
<!-- TODO-NOTE: Do not promote the M0036 relative-noise screen to final theorem or evidence language until M43-M45 rebuild the figures and Monte Carlo checks. The 50 percent noise-to-shock variance bound is identifying information, not a normalization. -->

## 5. Monte Carlo Robustness Check

This section should be read as the evidence map for the first draft. The two
figures give the reader the geometry first; the Monte Carlo table then checks
whether the same comparison survives repeated finite-sample draws. All three
objects use the same normalized bivariate impact chart and the same sign
screen, so the standard-DW and robust-DW accepted sets can be compared directly.

<!-- SOURCE-TRAIL: Use M27 for the common reporting chart, accepted shares, overlap, warning-rate, and truth-inclusion diagnostics. -->

### 5.1 Residual-Noise Grid

Figure 1 is the main story figure. Each column increases Gaussian residual
noise. The first row shows the standard sign/covariance set. The second row
adds the standard DW moment stack, including the no-noise covariance moment.
The third row uses the robust DW stack, which keeps the sign screen and mixed
higher cumulants while replacing invalid zero-covariance anchors with a
relative-noise covariance screen. The high-noise column is the narrative
anchor: standard DW looks sharp but rejects the true normalized \(B_0\), while
relative robust DW contains it with a visibly smaller set than the pure
higher-cumulant fallback.

![Figure 1. Relative-noise robust residual-noise grid.](figures/fig_sign_dw_relative_noise_robust_grid.png)

**Figure 1. Residual-noise grid.** Rows report the sign/covariance set,
standard-DW set, and robust-DW set in the common normalized \(B(b_{12},b_{21})\) chart.
Columns increase Gaussian residual noise from \(V=(0,0)\) to \(V=(0.5,0.5)\).
All rows invert pointwise 10 percent J tests for their displayed moment
stacks. The robust-DW row uses the pure mixed higher-cumulant J statistic and
adds the covariance-decomposition feasibility screen implied by
\(0\le \nu_i \le 0.5\operatorname{Var}(\varepsilon_i)\) for diagonal residual-noise variances. The
high-noise column shows the paper's main warning: standard DW rejects true
\(B_0\) under the researcher-facing cutoff, while relative robust DW contains it.

<!-- SOURCE-TRAIL: Figure file `figures/fig_sign_dw_relative_noise_robust_grid.png`; generator `simulations/sign_dw_robust_noise_grid_figure.py --robust-mode relative`; diagnostic note `simulations/sign_dw_relative_noise_robust_grid_figure.md`; audit note `derivations/m40-variance-ratio-robust-dw-screen-audit.md`; M45 validation note `simulations/m45_variance_ratio_evidence.md`. -->

M45 checks the figure's finite-sample logic before the draft leans on it. In
the fixed-grid diagnostics, the high-noise column has standard DW missing true
\(B_0\), while relative robust DW contains it and passes the variance-ratio
screen. In the repeated-sample Monte Carlo, the high-noise chi-square row gives
standard-DW truth inclusion of \(0.000\) and robust-DW truth inclusion of
\(0.875\).

### 5.2 Non-Gaussianity Grid

Figure 2 states the main limitation immediately after the main warning. It
holds residual noise fixed and weakens the structural shocks' higher moments
across columns. The robust-DW set stays noise-robust because the maintained
diagonal Gaussian residual-noise condition leaves higher cumulants unshifted,
and it regains precision only through the explicit variance-ratio screen. It is
not a free source of identification. When structural higher moments weaken,
robust DW widens toward the covariance-decomposition band; in the
Gaussian-shock limit, the higher-cumulant substack is all-null and the screen
does the remaining work.

![Figure 2. Non-Gaussianity grid.](figures/fig_sign_dw_robust_nongaussianity_grid.png)

**Figure 2. Non-Gaussianity grid.** Rows match Figure 1, but residual noise is
fixed while structural-shock non-Gaussianity weakens across columns. All rows
invert pointwise 10 percent J tests. The robust row uses the same
variance-ratio proposal as Figure 1: pure mixed higher-cumulant J inversion
plus the screen \(0\le \nu_i\le 0.5\operatorname{Var}(\varepsilon_i)\). The
figure explains why the robust set is a robustness check rather than a
uniformly sharper estimator.

<!-- SOURCE-TRAIL: Figure file `figures/fig_sign_dw_robust_nongaussianity_grid.png`; generator `simulations/sign_dw_robust_nongaussianity_grid_figure.py`; M45 validation note `simulations/m45_variance_ratio_evidence.md`. -->

This limitation matters for the paper's recommendation. A wide robust set is
not a failed diagnostic by itself. It records the information deliberately lost
by dropping the noisy recovered-shock covariance target and profiling diagonal
noise variances. The warning object is directional: standard-DW accepted mass
outside the robust-DW set, or standard-DW rejection of the truth in simulations
when robust DW still contains it.

<!-- SOURCE-TRAIL: Use `manuscript/derivations/dw-robust-comparison-diagnostic.md` for the directional interpretation rule. -->

### 5.3 Sample-Size Grid

Figure 3 asks whether the same comparison tightens as the sample grows. It
holds the Figure 1 structural non-Gaussianity calibration and Figure 2 residual
noise fixed, then varies \(T=500,1000,2000\). In this fixed draw, the standard
DW set becomes smaller and misses the true \(B_0\) at the larger sample sizes,
while the variance-ratio robust row keeps the true point and shrinks around
the covariance-decomposition band.

![Figure 3. Sample-size grid.](figures/fig_sign_dw_sample_size_robust_grid.png)

**Figure 3. Sample-size grid.** Rows match Figures 1 and 2. Columns vary the
sample size with strong structural higher moments and fixed residual noise
\(V=(0.2,0.2)\). The robust row again uses pure mixed higher-cumulant J
inversion plus the variance-ratio covariance-decomposition screen.

<!-- SOURCE-TRAIL: Figure file `figures/fig_sign_dw_sample_size_robust_grid.png`; generator `simulations/sign_dw_sample_size_robust_grid_figure.py`; M45 validation note `simulations/m45_variance_ratio_evidence.md`. -->

### 5.4 Monte Carlo Table

Table 1 reports the rebuilt M45 Monte Carlo evidence under the primary
researcher-facing chi-square cutoffs. The robust row is now the variance-ratio
proposal, and the covariance-decomposition screen is applied both to accepted
grid points and to the truth-inclusion calculation. `S truth` and `R truth`
are true-\(B_0\) inclusion rates for standard DW and robust DW. `R feasible`
is the fraction of evaluation samples in which the hard variance-ratio screen
is feasible at the true \(B_0\). `S share` and `R share` are accepted-set
shares on the normalized grid. `d_S_not_subset_R` is the directional share of
standard-DW accepted mass not supported by robust DW.

**Table 1. M45 chi-square-primary Monte Carlo comparison.** Entries are
evaluation averages from 24 replications per scenario on a \(41\times 41\)
grid, with 60 truth-calibration replications retained as audit output.

| Scenario | S truth | R truth | R feasible | S share | R share | d_S_not_subset_R | Warning rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| No noise, strong moments | 0.917 | 0.917 | 0.958 | 0.023 | 0.040 | 0.202 | 0.375 |
| Moderate Gaussian noise | 0.708 | 0.958 | 1.000 | 0.037 | 0.081 | 0.142 | 0.417 |
| High Gaussian noise | 0.000 | 0.875 | 0.958 | 0.036 | 0.097 | 0.069 | 0.875 |
| Weak structural higher moments | 0.792 | 0.875 | 0.958 | 0.152 | 0.170 | 0.293 | 0.625 |
| Gaussian structural shocks | 0.500 | 0.958 | 1.000 | 0.163 | 0.183 | 0.251 | 0.750 |
| Skewed residual noise | 0.583 | 1.000 | 1.000 | 0.027 | 0.064 | 0.171 | 0.667 |

<!-- SOURCE-TRAIL: M45 rebuilt run in `simulations/m45_variance_ratio_evidence.md` and machine-readable output `simulations/output/m45_variance_ratio_evidence.json`. Historical M29 outputs remain in `simulations/m29_calibrated_monte_carlo.md` but used the superseded diagonal-anchor robust row. -->

The audit rows stay secondary. The no-noise repeated calibration is a size
check, while the scenario-truth calibration is an oracle diagnostic. In the
high-noise case, scenario-truth calibration raises the standard-DW accepted
share to \(0.286\), showing the calibration cost of forcing the misspecified
standard statistic to cover the truth. These audit rows are not the applied
procedure being critiqued.

<!-- SOURCE-TRAIL: Use KnowledgeVault replication assets only as starting points; final figure commands must live in `replication/README.md`. -->
<!-- SOURCE-TRAIL: Use `derivations/dw-robust-comparison-diagnostic.md` for the M27 definitions of the reported standard-DW set, robust-DW set, critical-value convention, directional overlap metric, and interpretation boundaries. -->
<!-- DESIGN-NOTE: Use standard pointwise chi-square critical values as the primary applied M45 benchmark; repeated-sample and oracle cutoffs are audit rows only. -->
<!-- TODO-NOTE: In future simulation tables, report accepted shares, empty-set frequencies, Jaccard overlap, standard-DW mass outside robust-DW, truth inclusion, and least-rejected candidates. -->
<!-- TODO-NOTE: Report inconclusive and weak cases honestly. -->

## 6. Conclusion

TODO: Restate the practical recommendation: report the robust DW set beside the
standard DW set. If they overlap, the standard refinement is less suspect; if
they diverge, treat standard DW precision as a warning sign rather than
evidence of sharper structural learning.

## References

TODO: Use the citation style chosen in `manuscript-rules.md` and the BibTeX
snapshot in `../bibliography/references.bib`.
