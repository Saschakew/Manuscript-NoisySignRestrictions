# Standard-DW Versus Robust-DW Comparison Diagnostic

Status: M27 method formalization for manuscript planning. This note defines
the reported standard-DW set, the robust-DW set, the overlap and divergence
diagnostics, and the critical-value convention used by the selected M0020 grid
pair and the M28 validation pass. It is a diagnostic object, not yet a final
coverage claim.

## 1. Common Reporting Chart

The first paper reports all accepted sets in a common normalized bivariate
impact chart,

$$
B(b_{12},b_{21})=
\begin{bmatrix}
1 & b_{12}\\
b_{21} & 1
\end{bmatrix},
\qquad
1-b_{12}b_{21}\neq 0.
$$

Let `mathcal B_N` denote this nonsingular normalized chart after the chosen
sign and label convention. In the M0020 grid figures the displayed sign
restriction is

$$
b_{21}\ge 0.
$$

More generally, write the admissible sign screen as `R(B)>=0`. Every diagnostic
below is computed after this common screen. This matters because the
standard-DW and robust-DW sets use different moment targets; the comparison is
interpretable only after both have been projected into the same normalized
impact coordinates.

## 2. Reported Standard-DW Set

For a candidate `B` in the normalized chart, define recovered candidate shocks

$$
z_t(B)=B^{-1}u_t.
$$

The standard-DW row in the current figures uses standardized recovered shocks,

$$
\tilde z_{j,t}(B)
=
\frac{z_{j,t}(B)-\bar z_j(B)}{\widehat{\operatorname{sd}}\{z_j(B)\}},
\qquad j=1,2.
$$

Its finite-sample moment stack is

$$
\widehat g_{S,T}(B)=
\begin{bmatrix}
\widehat E(\tilde z_1\tilde z_2)\\
\widehat E(\tilde z_1^2\tilde z_2)\\
\widehat E(\tilde z_1\tilde z_2^2)\\
\widehat E(\tilde z_1^2\tilde z_2^2)-1
\end{bmatrix}.
$$

The first component is the no-noise covariance/whitening restriction. The
remaining components are the finite higher-moment independence stack used in
the M0020 visual implementation. Thus the reported standard-DW set is

$$
\mathcal S_T(c_S)=
\left\{
B\in\mathcal B_N:
R(B)\ge 0,\quad
J_{S,T}(B)\le c_S
\right\},
$$

where

$$
J_{S,T}(B)
=
T\widehat g_{S,T}(B)'
\widehat W_{S,T}(B)
\widehat g_{S,T}(B).
$$

This common-chart version is the figure-level version of standard
covariance-whitened DW inversion: it retains the covariance moment and then
adds higher-moment restrictions. Under residual noise, the M25 derivation says
that this no-noise covariance target is the fragile component.

## 3. Robust-DW Higher-Moment Set

The robust-DW row uses the same normalized candidate `B`, but it does not
standardize `z_t(B)` to impose unit variances and it does not restrict cross
covariance. It uses mixed higher cumulants of the centered transformed
residuals:

$$
\widehat g_{R,T}(B)=
\begin{bmatrix}
\widehat\kappa_{112}(B)\\
\widehat\kappa_{122}(B)\\
\widehat\kappa_{1112}(B)\\
\widehat\kappa_{1122}(B)\\
\widehat\kappa_{1222}(B)
\end{bmatrix}.
$$

For centered `z_1,z_2`, the third cumulants are third central moments. The
fourth cumulants are computed with covariance-product subtractions, for
example

$$
\widehat\kappa_{1112}
=
\widehat E(z_1^3z_2)-3\widehat s_{11}\widehat s_{12},
$$

$$
\widehat\kappa_{1122}
=
\widehat E(z_1^2z_2^2)
-\widehat s_{11}\widehat s_{22}
-2\widehat s_{12}^2,
$$

and analogously for `\widehat\kappa_{1222}`. The covariance terms
`\widehat s_{ij}` are nuisance quantities used to compute cumulants. They are
not restrictions such as `s_{11}=1`, `s_{22}=1`, or `s_{12}=0`.

The robust-DW set is

$$
\mathcal R_T(c_R)=
\left\{
B\in\mathcal B_N:
R(B)\ge 0,\quad
J_{R,T}(B)\le c_R
\right\},
$$

where

$$
J_{R,T}(B)
=
T\widehat g_{R,T}(B)'
\widehat W_{R,T}(B)
\widehat g_{R,T}(B).
$$

Under the maintained Gaussian residual-noise condition and the local rank
conditions in `dw-noise-robust-moments.md`, the true normalized impact matrix
has zero population robust moments. The set may still be wide when structural
higher moments are weak, and it may fail under non-Gaussian residual noise
unless the transformed residual-noise cumulants used in the stack vanish.

## 4. Critical-Value Convention

Write the critical values generically as

$$
c_S=c_{S,T}(1-\alpha),
\qquad
c_R=c_{R,T}(1-\alpha).
$$

The M0020 grid figures and the M28 first validation pass use pointwise
chi-square guide values at `alpha=0.10`:

$$
c_S=\chi^2_4(0.90)=7.78,
\qquad
c_R=\chi^2_5(0.90)=9.24.
$$

The sign/covariance row separately uses `\chi^2_1(0.90)=2.71`. These cutoffs
are useful for a common visual language, but they are not final simultaneous
coverage or size statements. M29 should replace or supplement them with
repeated-sample or bootstrap critical values and should report which critical
value convention is used in every table or figure.

## 5. Overlap And Divergence Metrics

Let `G` be the plotted or simulated candidate grid after the common sign
screen, and let `mu(A)` denote area, grid count, or Monte Carlo mass for a set
`A`. For a continuous statement, read `mu` as Lebesgue area in the normalized
chart; for the M0020/M28 implementation, read it as grid mass.

For the accepted sets

$$
S=\mathcal S_T(c_S)\cap G,
\qquad
R=\mathcal R_T(c_R)\cap G,
$$

report the accepted shares

$$
a_S=\frac{\mu(S)}{\mu(G)},
\qquad
a_R=\frac{\mu(R)}{\mu(G)}.
$$

The symmetric overlap index is the Jaccard overlap

$$
o_{SR}=
\frac{\mu(S\cap R)}{\mu(S\cup R)}
$$

when `S union R` is nonempty. It summarizes common mass, but it is not the
main warning metric because the robust set is expected to be wider.

The directional diagnostic is

$$
q_{S|R}=
\frac{\mu(S\cap R)}{\mu(S)}
\quad\text{and}\quad
d_{S\not\subset R}=1-q_{S|R},
$$

when `S` is nonempty. The warning metric is `d_{S not subset R}`: the share of
standard-DW accepted mass that is not supported by the robust higher-moment
set. The reverse quantity

$$
q_{R|S}=\frac{\mu(S\cap R)}{\mu(R)}
$$

is useful for describing width, but a low `q_{R|S}` is not itself a warning
because robust-DW deliberately discards second-moment restrictions.

For simulation designs where the true normalized impact matrix is known,
also report

$$
I_S(B_0)=1\{B_0\in S\},
\qquad
I_R(B_0)=1\{B_0\in R\}.
$$

Truth inclusion is not available in applications, so it should be used only to
validate the diagnostic in controlled simulation designs.

## 6. Interpretation Rules

Agreement is reassuring when the standard-DW set is nonempty and mostly
contained in the robust-DW set, i.e. `d_{S not subset R}` is small. In
simulation checks, the favorable no-noise case should also have both
`I_S(B0)=1` and `I_R(B0)=1`.

Divergence is a warning when a material share of the standard-DW set lies
outside the robust-DW set, when standard DW is small or rejects the true
normalized `B0` in simulation while robust DW contains it, or when standard DW
concentrates around a least-rejected pseudo-candidate under residual noise.
The warning is about covariance-target misspecification. It is not proof that
literal measurement error is present.

A wide robust-DW set is not a failure of the diagnostic. It can mean that the
second-moment target is being avoided and that higher moments are weak. The
M0020 non-Gaussianity grid is the intended visual example: as structural
higher moments disappear, robust-DW should become wide or all-null.

An empty robust-DW set is a separate stress signal. It may reflect invalid
Gaussian-noise assumptions, non-Gaussian transformed residual noise, poor
finite-sample critical values, or a candidate grid that misses the relevant
normalized chart. It should not be folded into the same interpretation as
standard-DW false precision.

## 7. Candidate Draft Statement

*Proposition 4 (`prop:dw-robust-comparison-diagnostic`, diagnostic
interpretation).* *Fix a normalized candidate chart and a common sign screen.
Let `S` be the reported standard-DW J-test inversion that includes the
no-noise covariance moment, and let `R` be the robust-DW J-test inversion based
only on mixed higher cumulants of `B^{-1}u`. Under the maintained
Gaussian-noise route, disagreement should be interpreted directionally:
standard-DW accepted mass outside the robust set warns that no-noise
covariance-target precision may be driven by residual-noise
misspecification, while robust accepted mass outside the standard set mainly
records the information deliberately lost by dropping second moments. The
comparison is a robustness diagnostic, not a proof of residual noise, and its
finite-sample calibration must be reported with the critical-value convention
used to construct both sets.*

## 8. M29 Reporting Template

M29 should report the following quantities by DGP scenario and critical-value
convention:

- `a_S`: standard-DW accepted share or width.
- `a_R`: robust-DW accepted share or width.
- `empty_S` and `empty_R`.
- `o_SR`: symmetric Jaccard overlap when defined.
- `d_S_not_subset_R`: standard-DW mass unsupported by robust-DW.
- `q_R_given_S`: robust width relative to the standard set.
- `I_S(B0)` and `I_R(B0)` in simulation only.
- distance from `B0` to each accepted set when truth is rejected.
- least-rejected `B` and minimum `J` for empty or near-empty sets.

The main expected patterns are: no-noise agreement; high-noise standard-DW
truth rejection with robust-DW truth inclusion; robust-DW widening under weak
higher moments; all-null robust behavior under Gaussian structural shocks; and
separate stress reporting for non-Gaussian residual noise that violates the
maintained robust-noise assumption.
