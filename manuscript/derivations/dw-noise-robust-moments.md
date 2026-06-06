# Drautzburg-Wright-Like Higher-Moment Inversion Under Gaussian Noise

Status: working derivation for manuscript design. This note derives a
Drautzburg-Wright-like higher-moment route that is robust to additive Gaussian
residual noise. It deliberately separates this route from the no-noise
covariance-whitened independence refinement and from the more general
Bonhomme-Robin-style observed-residual cumulant route.

Purpose: answer whether sign restrictions plus higher-order moment conditions
can target the structural impact matrix when residuals contain additive noise.
The answer is yes for a Gaussian-noise higher-cumulant system, after a scale
normalization and under non-Gaussian shock-rank conditions, but not for the
standard no-noise covariance factorization.

## 1. Model And Scope

Let observed reduced-form residuals satisfy

$$
u_t=B_0\varepsilon_t+\eta_t,
$$

where `B_0` is nonsingular, the structural shocks have zero mean, mutually
independent components, and unit variances,

$$
E(\varepsilon_t)=0,\qquad
E(\varepsilon_t\varepsilon_t')=I.
$$

For this note, the noise route is:

$$
\eta_t\sim \text{Gaussian}(0,V),
\qquad
\eta_t\perp \varepsilon_t.
$$

The main sign-restricted manuscript keeps diagonal residual noise in view, so
`V` is often diagonal in the `u` coordinates. For the higher-cumulant
robustness result below, Gaussianity is the key property: any linear transform
of `eta_t` remains Gaussian and has zero cumulants above order two. Diagonality
matters for the economic interpretation of residual noise and for optional
variance diagnostics, not for the higher-cumulant cancellation itself.

For a candidate impact matrix `B`, define candidate transformed residuals

$$
z_t(B)=B^{-1}u_t
      =A(B)\varepsilon_t+\xi_t(B),
\qquad
A(B)=B^{-1}B_0,
\qquad
\xi_t(B)=B^{-1}\eta_t.
$$

Since `xi_t(B)` is Gaussian for every candidate `B`, its cumulants of order
three and above vanish.

This note works with a normalized candidate space. In the bivariate manuscript
case, a convenient normalization is

$$
B(a,b)=
\begin{bmatrix}
1 & a\\
b & 1
\end{bmatrix},
\qquad
1-ab\neq 0.
$$

Without such a normalization, higher-order independence restrictions identify
columns only up to scale, sign, and permutation. Sign restrictions can label
and orient columns, but they do not by themselves fix scale.

## 2. The No-Noise DW-Like System And Why It Fails Under Noise

The no-noise system starts from

$$
u_t=B_0\varepsilon_t,
\qquad
\Sigma_u=B_0B_0',
$$

chooses a factor `P` such that `PP'=\Sigma_u`, rotates `P` by orthogonal
matrices `Q`, filters candidates by sign restrictions, and then tests whether
the recovered shocks are independent:

$$
e_t(Q)=Q'P^{-1}u_t.
$$

At the true no-noise rotation, `e_t(Q_0)=\varepsilon_t`, so both covariance and
higher-moment independence restrictions are valid.

With additive noise,

$$
\Sigma_u=B_0B_0'+V.
$$

A factor `P_*P_*'=\Sigma_u` is a factor of the noisy covariance, not a factor
of `B_0B_0'`. In general there is no orthogonal `Q` such that `P_*Q=B_0`, and
there is usually no positive diagonal rescaling that repairs this.

Even if we evaluate the true structural impact matrix directly,

$$
z_t(B_0)=B_0^{-1}u_t
        =\varepsilon_t+B_0^{-1}\eta_t,
$$

and therefore

$$
\operatorname{Var}\{z_t(B_0)\}
=I+B_0^{-1}VB_0^{-1'}.
$$

This matrix is generally not `I` and is generally not diagonal. Thus the
following no-noise restrictions are not robust:

$$
E\{z_i(B_0)^2\}=1,
\qquad
E\{z_i(B_0)z_j(B_0)\}=0\quad (i\neq j).
$$

An estimator that builds the candidate set from the noisy covariance factor,
or that imposes no-noise covariance restrictions on `z_t(B)`, has population
moments that generally do not vanish at `B_0`. Its population target is then a
pseudo-true noisy-covariance object, not the structural impact matrix.

## 3. A Noise-Robust Higher-Moment System

The robust DW-like route drops the no-noise covariance factorization. It
searches over a normalized impact space and uses only mixed higher cumulants
of `z_t(B)=B^{-1}u_t`.

For two variables, define the population higher-cumulant vector

$$
G_H(B)=
\begin{bmatrix}
\operatorname{cum}(z_1,z_1,z_2)\\
\operatorname{cum}(z_1,z_2,z_2)\\
\operatorname{cum}(z_1,z_1,z_1,z_2)\\
\operatorname{cum}(z_1,z_1,z_2,z_2)\\
\operatorname{cum}(z_1,z_2,z_2,z_2)
\end{bmatrix}.
$$

The noise-robust higher-moment accepted set can be written as

$$
\mathcal B_H(c)
=
\{B\in\mathcal B_N:
\text{sign restrictions hold and }
T\widehat G_H(B)'\widehat W_T\widehat G_H(B)\le c\},
$$

where `mathcal B_N` is the normalized nonsingular candidate space and
`\widehat G_H(B)` is a sample higher-cumulant vector. This system does not
impose

$$
B B'=\Sigma_u,
\qquad
\operatorname{Var}\{z_t(B)\}=I,
\qquad
\operatorname{Cov}\{z_i(B),z_j(B)\}=0.
$$

It may still use second sample moments as nuisance ingredients when computing
fourth cumulants. That is different from using second moments as structural
equalities.

## 4. Higher Cumulants Are Robust, Second Moments Are Not

Cumulants are multilinear, and cumulants of independent sums add. For any
order `r`,

$$
\operatorname{cum}_r\{z_t(B)\}
=
\operatorname{cum}_r\{A(B)\varepsilon_t\}
+
\operatorname{cum}_r\{\xi_t(B)\}.
$$

For `r\ge 3`, the second term is zero because `xi_t(B)` is Gaussian. Hence

$$
\operatorname{cum}_r\{z_t(B)\}
=
\operatorname{cum}_r\{A(B)\varepsilon_t\},
\qquad r\ge 3.
$$

At the true matrix, `A(B_0)=I`. Since the structural shock components are
independent, all mixed higher cumulants vanish:

$$
G_H(B_0)=0.
$$

The same statement is false for second moments:

$$
\operatorname{cum}_2\{z_t(B_0)\}
=
I+B_0^{-1}VB_0^{-1'}.
$$

The Gaussian noise therefore creates no population bias in the higher-cumulant
restrictions, but it does bias the no-noise covariance restrictions.

## 5. Writing The Cumulants As Moment Conditions

The GMM implementation can be written in moment language. Assume zero means
or work with centered observations. Third cumulants equal third central
moments:

$$
g_{112}(B)=E\{z_1(B)^2z_2(B)\}=0,
\qquad
g_{122}(B)=E\{z_1(B)z_2(B)^2\}=0.
$$

Fourth raw moments are not themselves robust to Gaussian noise. If
`z=y+\xi`, with `xi` Gaussian and independent of `y`, then for example

$$
E(z_i^2z_j^2)
=E(y_i^2y_j^2)
 +E(y_i^2)\Omega_{jj}
 +E(y_j^2)\Omega_{ii}
 +2E(y_iy_j)\Omega_{ij}
 +\Omega_{ii}\Omega_{jj}
 +2\Omega_{ij}^2,
$$

where `Omega=Var(xi)`. The variance terms are noise terms. The fourth
cumulant subtracts exactly the covariance-product terms. Thus the robust
fourth-order restrictions are

$$
g_{1112}(B)
=E\{z_1(B)^3z_2(B)\}
-3s_{11}(B)s_{12}(B)
=0,
$$

$$
g_{1122}(B)
=E\{z_1(B)^2z_2(B)^2\}
-s_{11}(B)s_{22}(B)
-2s_{12}(B)^2
=0,
$$

and

$$
g_{1222}(B)
=E\{z_1(B)z_2(B)^3\}
-3s_{22}(B)s_{12}(B)
=0,
$$

where

$$
s_{ij}(B)=E\{z_i(B)z_j(B)\}.
$$

A sample implementation may either compute these sample cumulants directly or
augment the GMM system with nuisance covariance parameters `s_{ij}` satisfying

$$
E\{z_i(B)z_j(B)-s_{ij}\}=0.
$$

Those covariance equations define nuisance quantities used to form fourth
cumulants. They are not restrictions such as `s_{11}=1`, `s_{22}=1`, or
`s_{12}=0`.

## 6. Bivariate Local Identification

Use the normalized bivariate candidate

$$
B(a,b)=
\begin{bmatrix}
1 & a\\
b & 1
\end{bmatrix}.
$$

Let the true value be `B(a_0,b_0)`, and define

$$
A(a,b)=B(a,b)^{-1}B(a_0,b_0)
=
\frac{1}{1-ab}
\begin{bmatrix}
1-ab_0 & a_0-a\\
b_0-b & 1-ba_0
\end{bmatrix}.
$$

Write

$$
A(a,b)=
\begin{bmatrix}
\alpha & \beta\\
c & d
\end{bmatrix}.
$$

Let

$$
\gamma_j=\operatorname{cum}_3(\varepsilon_j,\varepsilon_j,\varepsilon_j),
\qquad
\kappa_j=\operatorname{cum}_4(\varepsilon_j,\varepsilon_j,\varepsilon_j,
\varepsilon_j).
$$

Because `z_1=\alpha\varepsilon_1+\beta\varepsilon_2+\xi_1` and
`z_2=c\varepsilon_1+d\varepsilon_2+\xi_2`, and because the Gaussian part drops
out of higher cumulants, the mixed third cumulants are

$$
C_{112}(a,b)=\alpha^2c\,\gamma_1+\beta^2d\,\gamma_2,
$$

$$
C_{122}(a,b)=\alpha c^2\,\gamma_1+\beta d^2\,\gamma_2.
$$

The mixed fourth cumulants are

$$
C_{1112}(a,b)=\alpha^3c\,\kappa_1+\beta^3d\,\kappa_2,
$$

$$
C_{1122}(a,b)=\alpha^2c^2\,\kappa_1+\beta^2d^2\,\kappa_2,
$$

and

$$
C_{1222}(a,b)=\alpha c^3\,\kappa_1+\beta d^3\,\kappa_2.
$$

At the true value, `alpha=d=1` and `beta=c=0`, so all five mixed cumulants
vanish.

Let

$$
D_0=1-a_0b_0\neq 0.
$$

For small deviations `\Delta a=a-a_0` and `\Delta b=b-b_0`,

$$
\beta=-\frac{\Delta a}{D_0}+O(\|\Delta\|^2),
\qquad
c=-\frac{\Delta b}{D_0}+O(\|\Delta\|^2),
$$

while `alpha=1+O(\|\Delta\|)` and `d=1+O(\|\Delta\|)`. Therefore

$$
C_{112}(a,b)
=-\frac{\gamma_1}{D_0}\Delta b+O(\|\Delta\|^2),
$$

$$
C_{122}(a,b)
=-\frac{\gamma_2}{D_0}\Delta a+O(\|\Delta\|^2),
$$

$$
C_{1112}(a,b)
=-\frac{\kappa_1}{D_0}\Delta b+O(\|\Delta\|^2),
$$

$$
C_{1222}(a,b)
=-\frac{\kappa_2}{D_0}\Delta a+O(\|\Delta\|^2),
$$

and

$$
C_{1122}(a,b)=O(\|\Delta\|^2).
$$

Thus the higher-cumulant Jacobian has full local rank for `(a,b)` if each
shock has at least one nonzero higher cumulant that appears in the stack:

$$
(\gamma_1,\kappa_1)\neq (0,0),
\qquad
(\gamma_2,\kappa_2)\neq (0,0),
\qquad
D_0\neq 0.
$$

Under these conditions, the population criterion based on `G_H(B(a,b))`
has an isolated zero at `(a_0,b_0)` in a local neighborhood, up to the chosen
normalization, sign orientation, and label convention. Global identification
can still fail through finite-order cumulant cancellations or label/symmetry
aliases, so the manuscript should treat this as a local rank derivation until
an adversarial global check is complete.

## 7. Bias, Consistency, And Efficiency

At the true normalized matrix, the robust higher-cumulant moment vector has
zero population value:

$$
G_H(B_0)=0.
$$

This is the sense in which Gaussian noise does not bias the higher-moment
target. A minimum-distance or GMM estimator based on `\widehat G_H(B)` can be
consistent for the normalized `B_0` under compactness, continuity, valid
weighting, local rank, and the absence of other population zeros.

The estimator should not be described as exactly finite-sample unbiased.
Sample cumulant estimators can have finite-sample bias unless unbiased
`k`-statistics or equivalent corrections are used, and nonlinear GMM
estimators are generally not exactly unbiased. The defensible claim is
population correctness and asymptotic centering, not finite-sample unbiasedness.

The price of robustness is efficiency and scale information. The robust system
does not use

$$
\Sigma_u=B B'
$$

or `Var\{z_t(B)\}=I`. Therefore it discards information that would be valid in
the no-noise model, and it may also discard usable information available under
additional noise restrictions. For example, if `V` is known, parametrically
restricted, or if one uses clean off-diagonal `u` covariance under diagonal
noise, second moments can add information. The pure robust DW-like route
omits those restrictions to avoid imposing a false no-noise covariance target.

## 8. Manuscript Consequence

This gives two sign-plus-higher-moment approaches:

1. Incorrect under residual noise: build candidates from a factor of
   `Sigma_u`, impose sign restrictions on noisy covariance rotations, and test
   no-noise recovered-shock independence. This approach uses second moments as
   if `Sigma_u=B_0B_0'`, so it targets a noisy pseudo-object when `V\neq 0`.

2. Noise-robust under Gaussian residual noise: search over a normalized impact
   space, impose sign restrictions directly on candidate impacts, and use
   mixed higher cumulants of `B^{-1}u` written as raw-moment/cumulant GMM
   equations. This approach does not use second moments as structural
   restrictions, so it is less efficient but robust to unknown additive
   Gaussian noise.

This route is not a replacement for the BR-style observed-residual cumulant
route under unrestricted non-Gaussian diagonal noise. If `eta_t` is
non-Gaussian, then `B^{-1}\eta_t` generally has nonzero mixed higher cumulants
after transformation, and the DW-like transformed-cumulant restrictions are
polluted. The BR-style `u`-moment route remains the better-aligned object for
that broader noise class because it keeps the residual coordinates in which
diagonal noise is diagonal.
