# M66 Noise-Ratio Bound And Grid Algorithm

Date: 2026-06-12

## Question

Under the M64 unit-variance normalization
\(E[\varepsilon_t\varepsilon_t']=I\), should Section 4 replace
\(0\le\nu_i\le\rho(BB')_{ii}\) by \(0\le\nu_i\le\rho\)? And should the
nuisance bound appear inside \(\mathcal R_T(c;\rho)\) beside \(R(B)\ge0\)?

## Setup

The maintained additive model is

\[
u_t = B\varepsilon_t+\eta_t,\qquad
E[\varepsilon_t\varepsilon_t']=I,\qquad
E[\eta_t\eta_t']=V=\operatorname{diag}(\nu_1,\nu_2).
\]

Thus

\[
\Sigma_u=BB'+V.
\]

The expression \(\Sigma_u-BB'\) is not a different maintained model with a
minus sign. It is the implied leftover covariance:

\[
V=\Sigma_u-BB'.
\]

The structural shocks have unit variance in shock coordinates. The structural
signal in residual coordinate \(i\), however, is the \(i\)-th entry of
\(B\varepsilon_t\), whose variance is

\[
\operatorname{Var}((B\varepsilon_t)_i)
= e_i'BB'e_i
=(BB')_{ii}.
\]

The residual-noise variance \(\nu_i\) is measured in the same residual
coordinate as \(u_i\), not in the structural-shock coordinate
\(\varepsilon_i\). Therefore a direct cap \(0\le\nu_i\le\rho\) is an absolute
variance cap unless the residual coordinate has been separately standardized
or the nuisance has been redefined in structural units. It is not automatically
a residual-noise-to-signal ratio merely because
\(\operatorname{Var}(\varepsilon_i)=1\).

## Ratio Parameter

The scale-invariant residual-noise share in residual coordinate \(i\) is

\[
\lambda_i(B,\nu)
=\frac{\nu_i}{(BB')_{ii}}.
\]

The clean restriction is

\[
0\le \lambda_i\le\rho,\qquad i=1,2.
\]

Equivalently,

\[
0\le\nu_i\le\rho(BB')_{ii}.
\]

This keeps \(\nu_i\) in observed residual coordinates while giving the user the
simple bounded nuisance parameter they wanted. In computation one can grid over
\(\lambda\in[0,\rho]^2\) and set

\[
\nu_i(B,\lambda)=\lambda_i(BB')_{ii}.
\]

## Projected GMM Set

Let \(V(B,\lambda)=\operatorname{diag}(\nu_1(B,\lambda),\nu_2(B,\lambda))\).
The finite-sample GMM moment vector is evaluated at \((B,\nu(B,\lambda))\).
For a fixed researcher-chosen \(\rho\), the projected robust set is

\[
\mathcal R_T(c;\rho)=
\left\{
B:\ \exists\lambda\in[0,\rho]^2\ \text{such that}\ 
R(B)\ge0,\quad
J_T(B,\nu(B,\lambda))\le c
\right\}.
\]

The sign restriction and nuisance bound are both maintained restrictions. The
criterion \(J_T\) contains the second-order block
\(\widehat\Sigma_u-BB'-V(B,\lambda)\) and the higher-order
Gaussian-noise-blind rows. The set reported for \(B\) is the projection of the
accepted \((B,\lambda)\) pairs.

## Computational Algorithm

For each fixed \(\rho\):

1. Choose a grid or optimizer over admissible impact matrices \(B\).
2. For each \(B\), discard singular matrices and sign violations \(R(B)<0\).
3. Grid or optimize over \(\lambda\in[0,\rho]^2\).
4. Set \(\nu_i(B,\lambda)=\lambda_i(BB')_{ii}\).
5. Compute the full GMM vector \(\widehat g_T(B,\nu(B,\lambda))\) and
   \(J_T(B,\nu(B,\lambda))\).
6. Accept \(B\) if at least one admissible \(\lambda\) gives \(J_T\le c\).
7. If the figures display several values of \(\rho\), repeat the inversion for
   each \(\rho\); \(\rho\) is a sensitivity choice, not a profiled nuisance
   unless the paper explicitly changes the inferential target.

In the population exact-covariance limit, one can equivalently profile the
leftover \(V=\Sigma_u-BB'\) and check that it is diagonal, nonnegative, and has
\(\lambda_i\in[0,\rho]\). In the finite-sample GMM version, the covariance
fit is part of \(J_T\), while the sign screen and \(\lambda\)-bounds are hard
restrictions.

## Code Consequence

The existing Figure 1-3 scripts remain historical after M64/M66. They use the
old two-dimensional chart \(B=\begin{bmatrix}1&b_{12}\\ b_{21}&1\end{bmatrix}\)
and functions such as `relative_noise_covariance_feasible`, which implement
the pre-M64 diagonal-normalized variance-ratio screen. They do not implement
the M66 projected unit-variance GMM algorithm over a general \(B\) and
\(\lambda\). M65 must rebuild the figure design and implementation around the
algorithm above before the figures can be active evidence again.

## Claim Audit

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| The maintained model is \(\Sigma_u=BB'+V\); \(V=\Sigma_u-BB'\) is the implied leftover covariance. | derived | Direct variance expansion from \(u_t=B\varepsilon_t+\eta_t\), independence, and \(E[\varepsilon_t\varepsilon_t']=I\). | high | promote |
| Direct \(0\le\nu_i\le\rho\) is not automatically a ratio bound under unit shock variances. | derived | \(\nu_i\) is in residual coordinate \(u_i\); the signal variance in that coordinate is \((BB')_{ii}\). | high | promote |
| The dimensionless nuisance restriction is \(0\le\lambda_i=\nu_i/(BB')_{ii}\le\rho\). | derived | Ratio definition above. | high | promote |
| The projected set can impose \(R(B)\ge0\) and \(\lambda\in[0,\rho]^2\) as hard restrictions while using \(J_T\) for the GMM fit. | derived | Set definition and algorithm above. | high | promote |
| The current Figure 1-3 scripts implement the M66 algorithm. | code-implemented false | `sign_dw_robust_noise_grid_figure.py` uses `TRUE_MATRIX=[[1,b12],[b21,1]]` and pre-M64 feasibility functions. | high | quarantine as historical until M65 |
