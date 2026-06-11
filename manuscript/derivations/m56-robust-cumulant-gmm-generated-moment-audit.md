# M56 Robust Cumulant GMM Generated-Moment Audit

Status: completed audit for manuscript routing.

Date: 2026-06-10.

Task packet:
`manuscript/tasks/M56-robust-cumulant-gmm-generated-moment-audit.md`.

## Scope And Bottom Line

The user's concern is correct. A sample fourth cumulant such as

\[
\widehat g_{1222}(B)
=\widehat\mu_{13}(B)-3\widehat\mu_{02}(B)\widehat\mu_{11}(B)
\]

is not the sample mean of a single fixed per-observation moment. It is a smooth
function of primitive sample moments. Therefore the robust row should not be
described as a standard GMM statistic whose row-level moment is simply
`z1*z2^3 - 3*s22_hat*s12_hat`.

This does not invalidate the population robust moment restrictions. Under the
maintained independent Gaussian residual-noise condition, the mixed third
moments and mixed fourth cumulants of \(z_t(B_0)=\varepsilon_t+B_0^{-1}\eta_t\)
still vanish at the true normalized impact matrix. What changes is the
finite-sample weighting and inference route:

1. the valid concentrated route is a smooth primitive-moment minimum-distance
   or GMM statistic with delta-method covariance;
2. an equivalent augmented route estimates nuisance covariance entries
   \(s_{11},s_{12},s_{22}\) with moment equations and profiles them out; and
3. for the first paper's figures and Monte Carlo, bootstrap or repeated-sample
   calibration is safer than advertising naive pointwise chi-square cutoffs as
   final inference.

The current simulation code is better than the invalid naive version: it uses
analytic influence observations for the covariance-product plug-ins. However,
it remains a lightweight/provisional evidence implementation because it omits
the full primitive vector for sample centering, uses regularized inverses, and
keeps pointwise chi-square cutoffs as a plotting benchmark.

## Claim Ledger Outcome

| Claim | Status | Evidence |
|---|---|---|
| The concentrated sample cumulants are smooth functions of primitive sample moments, not simple fixed per-observation moments. | derived | Sections 1-2 below write the primitive vector and map. |
| Standard asymptotic inference can be recovered through a primitive-moment delta-method covariance or an augmented nuisance-covariance GMM system. | derived, with source context | Sections 3-4; KnowledgeVault GMM note and `svar-toolkit` GMM docs support the row-level moment discipline but do not supply this manuscript-specific generated-moment proof. |
| The robust population restrictions remain valid under independent Gaussian residual noise. | derived | M54 plus Section 5 below: generated finite-sample covariance products change inference, not the population zero-cumulant target. |
| In the robust noisy setting, \(S_{ij}(B_0)\) cannot generally be replaced by known constants. | derived | Section 6 below. \(S_{ii}(B_0)=1+\Omega_{ii}\) and \(S_{ij}(B_0)=\Omega_{ij}\) are unknown nuisance quantities unless additional noise restrictions are imposed. |
| Current Figure 1/Figure 2/Figure 3/M45 robust rows are final chi-square GMM evidence. | failed as final claim | Section 7: current code is approximate/provisional, not final publication inference. |

## 1. Primitive Moment Vector

For a fixed candidate \(B\), let \(z_t(B)=(x_t,y_t)'\) after centering. With
known zero means, the primitive moment vector needed for the bivariate robust
stack can be written as

\[
p(B)=
\begin{bmatrix}
\mu_{21}\\
\mu_{12}\\
\mu_{31}\\
\mu_{22}\\
\mu_{13}\\
\mu_{20}\\
\mu_{11}\\
\mu_{02}
\end{bmatrix}
=
\begin{bmatrix}
E[x^2y]\\
E[xy^2]\\
E[x^3y]\\
E[x^2y^2]\\
E[xy^3]\\
E[x^2]\\
E[xy]\\
E[y^2]
\end{bmatrix}.
\]

The robust concentrated moment map is

\[
h(p)=
\begin{bmatrix}
\mu_{21}\\
\mu_{12}\\
\mu_{31}-3\mu_{20}\mu_{11}\\
\mu_{22}-\mu_{20}\mu_{02}-2\mu_{11}^2\\
\mu_{13}-3\mu_{02}\mu_{11}
\end{bmatrix}.
\]

The sample robust vector is therefore \(\widehat G_H(B)=h(\widehat p_T(B))\).
This is a generated sample moment. It is still a regular smooth statistic when
the primitive moments have a central limit theorem and the derivative below
has stable rank.

If sample means are estimated rather than known to be zero, the fully general
primitive vector should add the first moments and define the central moments as
a smooth function of raw moments. The current code de-means candidate residuals
but does not include the additional first-moment influence terms in the
reported covariance matrix. That omission is negligible only under a
known-zero-mean convention or as a plotting approximation; final evidence
should either include the mean terms in the primitive vector or use a bootstrap
that automatically captures demeaning.

## 2. Delta-Method Jacobian

For the known-zero-mean primitive ordering above, the Jacobian
\(D(p)=\partial h(p)/\partial p'\) is

\[
D(p)=
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 1 & 0 & 0 & -3\mu_{11} & -3\mu_{20} & 0\\
0 & 0 & 0 & 1 & 0 & -\mu_{02} & -4\mu_{11} & -\mu_{20}\\
0 & 0 & 0 & 0 & 1 & 0 & -3\mu_{02} & -3\mu_{11}
\end{bmatrix}.
\]

Let

\[
q_t(B)=
\begin{bmatrix}
x_t^2y_t\\
x_ty_t^2\\
x_t^3y_t\\
x_t^2y_t^2\\
x_ty_t^3\\
x_t^2\\
x_ty_t\\
y_t^2
\end{bmatrix},
\qquad
\widehat p_T(B)=T^{-1}\sum_t q_t(B).
\]

If
\(\sqrt{T}\{\widehat p_T(B)-p(B)\}\Rightarrow N(0,\Sigma_p(B))\), then

\[
\sqrt{T}\{\widehat G_H(B)-G_H(B)\}
\Rightarrow
N\{0,\Sigma_G(B)\},
\qquad
\Sigma_G(B)=D(p)\Sigma_p(B)D(p)'.
\]

The pointwise concentrated statistic is then

\[
J_{H,T}(B)
=T\widehat G_H(B)'\widehat\Sigma_G(B)^{-1}\widehat G_H(B).
\]

At a fixed candidate satisfying \(G_H(B)=0\), and under full-rank
\(\Sigma_G(B)\), the reference degrees of freedom are the rank of
\(\Sigma_G(B)\), usually five for the full bivariate robust stack. The degrees
of freedom are not the primitive dimension eight and do not subtract the
three covariance nuisance entries in the concentrated representation; those
nuisance entries have already been profiled through the smooth map. In the
augmented representation below, the same count appears as eight moment
equations minus three nuisance covariance parameters.

This chi-square statement is pointwise and asymptotic. Weak higher moments,
near-singular \(\Sigma_G(B)\), many grid searches, regularized inverses, and
the hard variance-ratio feasibility screen can all make bootstrap or
simulation calibration preferable for the paper's evidence section.

## 3. Equivalent Augmented Nuisance-Covariance System

The same object can be written with nuisance covariance parameters

\[
s=(s_{11},s_{12},s_{22})'
\]

and augmented moments

\[
\begin{aligned}
E[x^2y]&=0,\\
E[xy^2]&=0,\\
E[x^3y]-3s_{11}s_{12}&=0,\\
E[x^2y^2]-s_{11}s_{22}-2s_{12}^2&=0,\\
E[xy^3]-3s_{22}s_{12}&=0,\\
E[x^2]-s_{11}&=0,\\
E[xy]-s_{12}&=0,\\
E[y^2]-s_{22}&=0.
\end{aligned}
\]

For a fixed \(B\), profiling the last three equations gives
\(\widehat s_{11}=\widehat\mu_{20}\),
\(\widehat s_{12}=\widehat\mu_{11}\), and
\(\widehat s_{22}=\widehat\mu_{02}\). Substituting those values yields the
concentrated map \(h(\widehat p_T)\).

The augmented and concentrated routes are first-order equivalent only when the
concentrated covariance matrix is built by the corresponding delta method, or
when the augmented criterion uses a weight whose profiled Schur-complement
information matches that delta covariance. Simply computing the covariance of
the five concentrated scalar values as if they were primitive observations is
not the same object.

## 4. What The Current Code Does

The active figures and M45 evidence call
`robust_higher_cumulant_values` in
`manuscript/simulations/sign_dw_robust_noise_grid_figure.py`. That function
computes the five concentrated sample cumulants and also returns influence
observations. For the fourth entries, the influence columns are:

\[
x^3y-3(\widehat\mu_{11}x^2+\widehat\mu_{20}xy),
\]

\[
x^2y^2-\widehat\mu_{02}x^2-\widehat\mu_{20}y^2
-4\widehat\mu_{11}xy,
\]

\[
xy^3-3(\widehat\mu_{11}y^2+\widehat\mu_{02}xy).
\]

These are exactly the known-zero-mean delta-method rows \(D(\widehat p)q_t\),
up to constants that disappear when the sample covariance is centered. The
code then estimates a covariance matrix from these influence rows and uses

\[
T\widehat G_H(B)'\widehat\Sigma_G(B)^{-1}\widehat G_H(B).
\]

So the current robust implementation is not the invalid naive statistic that
ignores generated covariance products. It is an approximate delta-method
implementation for known-zero-mean centered moments.

The current evidence is nevertheless not final:

- the demeaning step is handled by centering \(z_t(B)\), but the influence
  matrix does not include first-moment nuisance terms;
- the inverse covariance is regularized, which is reasonable for plotting but
  changes exact test calibration;
- the same data select candidate-specific covariance plug-ins and test the
  generated moments, so small-sample calibration can be poor;
- the hard variance-ratio covariance screen is an inequality feasibility
  screen with its own finite-sample false-exclusion risk; and
- M52 still needs to rebuild the standard-DW comparator with the source-correct
  moment menu, so the joint figure/table evidence path remains historical.

Classification:

| Artifact | Robust-row classification after M56 |
|---|---|
| Figure 1 robust row | approximate/provisional generated-moment criterion; visually useful but not final chi-square evidence |
| Figure 2 robust row | same classification through reuse of the base robust statistic |
| Figure 3 robust row | same classification through reuse of the base robust statistic |
| M45 Monte Carlo robust row | lightweight/provisional; records the current approximate generated-moment statistic plus hard covariance screen |

## 5. Population Validity Versus Finite-Sample Inference

M56 does not change the M54 population result. At \(B=B_0\),

\[
z_t(B_0)=\varepsilon_t+\xi_t,
\qquad
\xi_t=B_0^{-1}\eta_t.
\]

If \(\eta_t\) is independent Gaussian residual noise, then \(\xi_t\) is
Gaussian and has no cumulants above order two. Because cumulants of
independent sums add, mixed higher cumulants of \(z_t(B_0)\) equal mixed higher
cumulants of the independent structural shocks and vanish. The fourth raw
moments need covariance-product subtractions because Gaussian noise changes
second moments even while higher cumulants vanish.

Thus the robust stack remains a valid population restriction. The M56
correction is about how to estimate the covariance of
\(\widehat G_H(B)\), how to calibrate \(J_{H,T}(B)\), and how strongly the
paper can word finite-sample evidence.

## 6. Why \(S_{ij}(B_0)\) Cannot Be Replaced By Known Constants

The user's analogy to no-noise standardized shocks is useful but does not
carry over unchanged. In a no-noise standardized chart,

\[
E[\varepsilon_i^2]=1,
\qquad
E[\varepsilon_i\varepsilon_j]=0
\quad (i\neq j),
\]

so Gaussian fourth-product targets can include known constants such as one.

In the robust noisy model,

\[
S(B_0)=\operatorname{Var}\{z_t(B_0)\}
=I+\Omega(B_0),
\qquad
\Omega(B_0)=\operatorname{Var}(B_0^{-1}\eta_t).
\]

Therefore

\[
S_{ii}(B_0)=1+\Omega_{ii}(B_0),
\qquad
S_{ij}(B_0)=\Omega_{ij}(B_0)\quad(i\neq j).
\]

These entries are generally unknown, nonzero, and candidate-dependent. They
are not normalization constants unless the manuscript adds a new assumption
that fixes the transformed-noise covariance. The correct robust route is to
estimate them as nuisance covariance entries of \(z_t(B)\), or to augment the
GMM system with nuisance covariance parameters, not to set them equal to
their no-noise values.

## 7. Manuscript And Implementation Route

The recommended route is:

1. Keep the robust population moment stack.
2. In M55, explain that the sample fourth-cumulant entries are generated
   smooth moments. State that \(S_{ij}(B)\) is estimated from candidate
   transformed residuals and used as a nuisance plug-in, not imposed as a
   zero-covariance restriction.
3. In M52, while rebuilding the source-correct standard-DW comparator, also
   upgrade the robust-row implementation to one of:
   - full primitive-moment delta-method weighting, including sample-mean
     nuisance terms; or
   - augmented nuisance-covariance GMM with profiled \(s_{ij}\); or
   - bootstrap/repeated-sample calibration for the reported accepted sets.
4. Until that rebuild is complete, call the current robust evidence
   lightweight/provisional and avoid final claims that the plotted robust row
   is a fully calibrated standard GMM J-test.

No separate task is needed unless M52 becomes too large. The implementation
change belongs naturally with the figure and Monte Carlo rebuild because it
uses the same scripts and outputs.

## Outcome

M56 unblocks M55's writing route: Section 4 can say the robust fourth-order
conditions are valid generated moments, but it must not describe them as
ordinary fixed row-level sample moments. It also sharpens M52: final evidence
must rebuild the standard-DW comparator and either upgrade or calibrate the
robust generated-moment statistic before the figures and table are treated as
publication-ready inference.
