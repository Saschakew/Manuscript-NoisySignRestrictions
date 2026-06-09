# M54 Stepwise Transformed-Noise Moment Derivation And Normalization Audit

Status: audited working derivation for manuscript design.

Date: 2026-06-09.

Task packet: `manuscript/tasks/M54-stepwise-moment-derivation-and-normalization-audit.md`.

## Scope And Notation

This note derives the transformed-noise moments requested in M54 at the truth
\(B=B_0\), where

\[
z_t(B_0)=B_0^{-1}u_t=\varepsilon_t+\xi_t,
\qquad
\xi_t=B_0^{-1}\eta_t.
\]

The main manuscript remains bivariate, but the requested labels \(z_3\) and
\(z_4\) are best read as generic distinct indices for the moment algebra.

Assumptions used below:

\[
E(\varepsilon_t)=0,
\qquad
E(\varepsilon_t\varepsilon_t')=I,
\qquad
E(\eta_t)=0,
\qquad
\eta_t\perp \varepsilon_t.
\]

When residual noise is Gaussian, \(\xi_t\) is Gaussian for every linear
transform \(B_0^{-1}\), and every cumulant of \(\xi_t\) above order two
vanishes. When residual noise is only independent but not Gaussian, the
transformed-noise third and fourth moments remain as nuisance terms.

## 1. Why Independent Residual Components Do Not Stay Independent After Transformation

Write \(C=B_0^{-1}\), so \(\xi_t=C\eta_t\). Then

\[
\xi_i=\sum_a c_{ia}\eta_a,
\qquad
\operatorname{Cov}(\xi_i,\xi_j)
=\sum_{a,b} c_{ia}c_{jb}\operatorname{Cov}(\eta_a,\eta_b).
\]

If the residual components are independent in residual coordinates and
\(\operatorname{Var}(\eta)=\operatorname{diag}(\nu_1,\nu_2,\ldots)\), then

\[
\operatorname{Cov}(\xi_i,\xi_j)
=\sum_a c_{ia}c_{ja}\nu_a.
\]

This is generally nonzero when \(C\) mixes coordinates. So independence of the
\(\eta_a\) does not imply independence of the transformed components \(\xi_i\).
The Gaussian simplification used later is stronger: it kills higher cumulants
of \(\xi_t\), but it does not make \(\xi_t\) componentwise independent.

## 2. Requested Moments At \(B=B_0\)

The table below separates the raw transformed-noise remainder from the
Gaussian special case.

| Requested moment | Stepwise result at \(B=B_0\) | Gaussian residual-noise simplification |
|---|---|---|
| \(E[z_i^2z_j]\), \(i\neq j\) | Expanding \((\varepsilon_i+\xi_i)^2(\varepsilon_j+\xi_j)\) leaves only \(E[\xi_i^2\xi_j]\). | If \(\xi\) is Gaussian, \(E[\xi_i^2\xi_j]=0\), so \(E[z_i^2z_j]=0\). |
| \(E[z_i z_j z_k]\), distinct \(i,j,k\) | Expanding \((\varepsilon_i+\xi_i)(\varepsilon_j+\xi_j)(\varepsilon_k+\xi_k)\) leaves only \(E[\xi_i\xi_j\xi_k]\). | If \(\xi\) is Gaussian, \(E[\xi_i\xi_j\xi_k]=0\), so \(E[z_i z_j z_k]=0\). |
| \(E[z_i^3z_j]\), \(i\neq j\) | Expanding \((\varepsilon_i+\xi_i)^3(\varepsilon_j+\xi_j)\) leaves \(3E[\xi_i\xi_j]+E[\xi_i^3\xi_j]\). | If \(\xi\) is Gaussian, \(E[\xi_i^3\xi_j]=3\Omega_{ii}\Omega_{ij}\), so \(E[z_i^3z_j]=3(1+\Omega_{ii})\Omega_{ij}\). |
| \(E[z_i^2z_j^2]\), \(i\neq j\) | Expanding \((\varepsilon_i+\xi_i)^2(\varepsilon_j+\xi_j)^2\) leaves \(1+\Omega_{ii}+\Omega_{jj}+E[\xi_i^2\xi_j^2]\). | If \(\xi\) is Gaussian, \(E[\xi_i^2\xi_j^2]=\Omega_{ii}\Omega_{jj}+2\Omega_{ij}^2\), so \(E[z_i^2z_j^2]=(1+\Omega_{ii})(1+\Omega_{jj})+2\Omega_{ij}^2\). |
| \(E[z_i^2z_jz_k]\), distinct \(i,j,k\) | Expanding \((\varepsilon_i+\xi_i)^2(\varepsilon_j+\xi_j)(\varepsilon_k+\xi_k)\) leaves \(\Omega_{jk}+E[\xi_i^2\xi_j\xi_k]\). | If \(\xi\) is Gaussian, \(E[\xi_i^2\xi_j\xi_k]=\Omega_{ii}\Omega_{jk}+2\Omega_{ij}\Omega_{ik}\), so \(E[z_i^2z_jz_k]=(1+\Omega_{ii})\Omega_{jk}+2\Omega_{ij}\Omega_{ik}\). |
| \(E[z_i z_j z_k z_l]\), distinct \(i,j,k,l\) | Expanding \((\varepsilon_i+\xi_i)(\varepsilon_j+\xi_j)(\varepsilon_k+\xi_k)(\varepsilon_l+\xi_l)\) leaves \(E[\xi_i\xi_j\xi_k\xi_l]\). | If \(\xi\) is Gaussian, \(E[\xi_i\xi_j\xi_k\xi_l]=\Omega_{ij}\Omega_{kl}+\Omega_{ik}\Omega_{jl}+\Omega_{il}\Omega_{jk}\). |

Here \(\Omega=E(\xi_t\xi_t')=CB_\eta C'\) with \(B_\eta=\operatorname{Var}(\eta_t)\).
When the residual-noise covariance is diagonal in residual coordinates,
\(\Omega_{ij}=\sum_a c_{ia}c_{ja}\nu_a\).

### 2.1 \(E[z_i^2z_j]\)

For \(i\neq j\),

\[
(\varepsilon_i+\xi_i)^2(\varepsilon_j+\xi_j)
=\varepsilon_i^2\varepsilon_j
+\varepsilon_i^2\xi_j
+2\varepsilon_i\xi_i\varepsilon_j
+2\varepsilon_i\xi_i\xi_j
+\xi_i^2\varepsilon_j
+\xi_i^2\xi_j.
\]

Every term except the last has an unmatched centered structural shock, so

\[
E[z_i^2z_j]=E[\xi_i^2\xi_j].
\]

Under Gaussian residual noise, \(E[\xi_i^2\xi_j]=0\), so this is a valid zero
restriction at \(B=B_0\).

### 2.2 \(E[z_i z_j z_k]\)

For distinct \(i,j,k\),

\[
(\varepsilon_i+\xi_i)(\varepsilon_j+\xi_j)(\varepsilon_k+\xi_k)
\]

expands into eight terms. Every term containing at least one structural shock
vanishes after taking expectations, so only the pure transformed-noise term
remains:

\[
E[z_i z_j z_k]=E[\xi_i\xi_j\xi_k].
\]

Under Gaussian residual noise, this is zero.

### 2.3 \(E[z_i^3z_j]\)

For \(i\neq j\),

\[
(\varepsilon_i+\xi_i)^3(\varepsilon_j+\xi_j)
=(\varepsilon_i^3+3\varepsilon_i^2\xi_i+3\varepsilon_i\xi_i^2+\xi_i^3)
(\varepsilon_j+\xi_j).
\]

The only surviving terms are the one with \(3\varepsilon_i^2\xi_i\xi_j\) and
the pure transformed-noise term:

\[
E[z_i^3z_j]=3E[\xi_i\xi_j]+E[\xi_i^3\xi_j].
\]

Because \(E(\varepsilon_i^2)=1\), the structural variance contributes only the
factor \(3\) above. If \(\xi\) is Gaussian, Isserlis' formula gives

\[
E[\xi_i^3\xi_j]=3\Omega_{ii}\Omega_{ij},
\]

so

\[
E[z_i^3z_j]=3(1+\Omega_{ii})\Omega_{ij}.
\]

Since \(S_{ii}=1+\Omega_{ii}\) and \(S_{ij}=\Omega_{ij}\) for \(i\neq j\), this
can also be written as \(3S_{ii}S_{ij}\).

### 2.4 \(E[z_i^2z_j^2]\)

For \(i\neq j\), after deleting terms with an unmatched centered structural
shock,

\[
E[z_i^2z_j^2]
=E[\varepsilon_i^2\varepsilon_j^2]
+E[\varepsilon_i^2]E[\xi_j^2]
+E[\varepsilon_j^2]E[\xi_i^2]
+E[\xi_i^2\xi_j^2].
\]

Because the structural shocks are independent and unit variance,
\(E[\varepsilon_i^2\varepsilon_j^2]=1\). Hence

\[
E[z_i^2z_j^2]
=1+\Omega_{ii}+\Omega_{jj}+E[\xi_i^2\xi_j^2].
\]

If \(\xi\) is Gaussian, then

\[
E[\xi_i^2\xi_j^2]=\Omega_{ii}\Omega_{jj}+2\Omega_{ij}^2,
\]

so

\[
E[z_i^2z_j^2]
=(1+\Omega_{ii})(1+\Omega_{jj})+2\Omega_{ij}^2
=S_{ii}S_{jj}+2S_{ij}^2.
\]

This is the key distinction from the raw DW fourth-product target: the raw
moment is not a zero restriction under residual noise; the covariance-product
subtraction is.

### 2.5 \(E[z_i^2z_jz_k]\)

For distinct \(i,j,k\), the surviving terms are

\[
E[z_i^2z_jz_k]
=E[\varepsilon_i^2]E[\xi_j\xi_k]
+E[\xi_i^2\xi_j\xi_k].
\]

So

\[
E[z_i^2z_jz_k]=\Omega_{jk}+E[\xi_i^2\xi_j\xi_k].
\]

If \(\xi\) is Gaussian, Isserlis' formula gives

\[
E[\xi_i^2\xi_j\xi_k]
=\Omega_{ii}\Omega_{jk}+2\Omega_{ij}\Omega_{ik},
\]

hence

\[
E[z_i^2z_jz_k]=(1+\Omega_{ii})\Omega_{jk}+2\Omega_{ij}\Omega_{ik}.
\]

### 2.6 \(E[z_i z_j z_k z_l]\)

For distinct \(i,j,k,l\), every term involving a structural shock vanishes,
so

\[
E[z_i z_j z_k z_l]=E[\xi_i\xi_j\xi_k\xi_l].
\]

If \(\xi\) is Gaussian, Isserlis' formula gives

\[
E[z_i z_j z_k z_l]
=\Omega_{ij}\Omega_{kl}+\Omega_{ik}\Omega_{jl}+\Omega_{il}\Omega_{jk}.
\]

## 3. What This Means For The Robust Moment Stack

The third-order robust conditions in Section 4 are valid zero restrictions
under Gaussian residual noise because the transformed-noise third moments
vanish:

\[
E[z_1^2z_2]=0,
\qquad
E[z_1z_2^2]=0.
\]

They are not robust if residual noise is merely independent but non-Gaussian,
because \(E[\xi_1^2\xi_2]\) and \(E[\xi_1\xi_2^2]\) then remain as nuisance
terms.

The fourth-order DW raw products are not zero restrictions under residual
noise. The correct Gaussian-noise-robust conditions are cumulant-style moment
equations with covariance-product subtractions:

\[
g_{1112}(B)
=E[z_1(B)^3z_2(B)]-3s_{11}(B)s_{12}(B)=0,
\]

\[
g_{1122}(B)
=E[z_1(B)^2z_2(B)^2]
-s_{11}(B)s_{22}(B)-2s_{12}(B)^2=0,
\]

\[
g_{1222}(B)
=E[z_1(B)z_2(B)^3]-3s_{22}(B)s_{12}(B)=0,
\]

where \(s_{ij}(B)=E[z_i(B)z_j(B)]\) is a nuisance covariance used only to
form the fourth-order conditions.

If residual noise is non-Gaussian, then the transformed-noise third and fourth
cumulants must either be modeled explicitly or assumed to vanish. Otherwise
the robust DW stack is contaminated by additional nuisance cumulants such as
\(\operatorname{cum}_3(\xi_i,\xi_j,\xi_k)\) and
\(\operatorname{cum}_4(\xi_i,\xi_j,\xi_k,\xi_l)\).

## 4. Normalization Audit And Recommendation

The audit supports keeping the manuscript in the common `diag(B)=1` chart.
That is the chart already used for the residual-noise covariance screen in
Section 4, where the structural variances \(s_i\) and residual-noise
variances \(\nu_i\) are profiled explicitly. The stepwise moment derivation
above does not force a switch to DW's covariance-normalized
`Var(\varepsilon)=I` rotation chart.

Section 2 already states the structural no-noise normalization
\(E(\varepsilon\varepsilon')=I\), which is enough for the current paper
because the source-correct DW standardization is handled inside the recovered-
shock moment menu, not by changing the manuscript-wide plotting chart. In
other words, the source-native unit-variance scaling is internal to the DW
moment display, while the manuscript's common B-plane stays on `diag(B)=1`.

So the recommendation is:

1. keep `diag(B)=1` for the first paper;
2. treat the DW unit-variance standardization as an internal moment-menu
   feature rather than a manuscript-wide reparameterization;
3. let M52 rebuild the source-correct standard-DW evidence in the retained
   common chart; and
4. defer any unit-variance/rotation-chart rewrite as a separate user-decision
   task unless a later revision explicitly asks for it.

That is the smallest consistent path through Sections 2-5, the figures, and
the Monte Carlo evidence.
