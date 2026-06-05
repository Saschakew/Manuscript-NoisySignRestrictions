# Bonhomme-Robin Applicability

Status: M07 working note. This note documents what the Bonhomme-Robin analogy
does and does not justify for the bivariate diagonal-noise SVAR. It is not a
local identification proof; M09 still has to derive the profiled criteria and
rank condition.

Source context:

- `vault/papers/Consistent noisy independent component analysis.md`
- `vault/syntheses/Bonhomme-Robin noise-robust SVAR moment inversion.md`
- `manuscript/derivations/bivariate-cumulant-map.md`

## Question

Can the manuscript cite Bonhomme and Robin's quasi-JADE theorem as the theorem
that identifies the bivariate noisy SVAR loading matrix

$$
B(a,b)=
\begin{bmatrix}
1 & a\\
b & 1
\end{bmatrix}
$$

when

$$
u_t=B(a,b)\varepsilon_t+\eta_t,
\qquad L=K=2,
$$

and the two noise components are independent?

Answer: no. Bonhomme-Robin provide the right analogy and moment logic, but the
bivariate manuscript object is not a direct application of their full
quasi-JADE identification theorem.

## Bonhomme-Robin Sequence

Bonhomme and Robin study

$$
Y=\Lambda X+U,
\qquad \operatorname{Var}(X)=I_K,
$$

with mutually independent factors, factors independent of errors, and error
dependence restricted by a set of clean measurement pairs

$$
\mathcal J \subset \{(\ell,m):1\leq \ell<m\leq L\}.
$$

For a clean pair `(\ell,m) in mathcal J`, low-order error cumulants involving
both error coordinates vanish. In the kurtotic route, this gives clean columns

$$
\operatorname{vech}\{\Omega_Y(\ell,m)\}
=Q D_4(\Lambda_\ell\odot\Lambda_m),
\qquad (\ell,m)\in\mathcal J,
$$

and after stacking clean-pair columns,

$$
\Omega_Y=Q D_4 Q_{\mathcal J}'.
$$

Their first identification step uses the rank of this clean-pair matrix to
identify error cumulants. In the all-kurtotic route, the relevant condition is
that `Q_J` has full column rank `K`; in particular, it requires

$$
K\leq J,
\qquad J=|\mathcal J|.
$$

When this rank condition holds, the null space of `Omega_Y'` gives linear
restrictions that identify the low-order error cumulants. Only after this
error-cumulant step do Bonhomme and Robin subtract the identified error
cumulants and identify loadings from denoised cumulants by joint
diagonalization.

## Why The Direct Theorem Fails For `L=K=2`

In the manuscript's bivariate diagonal-noise SVAR, independent idiosyncratic
errors give exactly one clean measurement pair:

$$
\mathcal J=\{(1,2)\},
\qquad J=1.
$$

For `K=2`, the all-kurtotic Bonhomme-Robin rank condition cannot hold because

$$
\operatorname{rank}(Q_{\mathcal J})\leq 1 < 2 = K.
$$

Equivalently, the stacked clean-pair fourth-cumulant matrix has one column:

$$
\Omega_Y \in \mathbb R^{3\times 1},
$$

so it cannot have rank two. The null-space step used to infer all relevant
error cumulants before loading estimation is therefore unavailable.

The skewness route does not rescue the bivariate two-factor case. Bonhomme and
Robin's skewness-based route also needs enough clean information; with
independent errors it yields at most `K <= L-1` in the relevant bound. For
`L=2`, that bound permits at most one factor, not the manuscript's two
structural shocks.

Thus the manuscript must not claim:

- that Bonhomme-Robin's Theorem 2 or Theorem 3 identifies the bivariate
  diagonal-noise SVAR error cumulants;
- that their Theorem 4 can be invoked after an identified denoising step in
  the `L=K=2` SVAR;
- that quasi-JADE consistency or asymptotic normality is inherited directly by
  the manuscript's profiled inversion;
- that pure own cumulants can be ignored because Bonhomme-Robin use only clean
  mixed cumulants.

The last point matters. In Bonhomme-Robin, pure moments enter after their error
components have been identified and subtracted. In the manuscript's bivariate
case, unrestricted pure own cumulants are profiled nuisance moments or
diagnostics unless extra restrictions are placed on noise cumulants.

## What The Analogy Does Justify

The analogy still gives useful structure:

1. Cumulant decomposition applies. The noisy SVAR is a two-factor linear model
   with loadings `B(a,b)`, normalized structural shock variances, independent
   factors, and idiosyncratic errors.
2. Clean-pair logic applies locally. Under independent diagonal noise,
   off-diagonal and mixed residual cumulants are free of diagonal noise
   cumulants through fourth order.
3. The nuisance distinction applies. Pure own residual cumulants should be
   treated as error-cumulant information, diagnostics, or restrictions only
   after the paper states which noise restrictions are imposed.
4. The denoise-then-identify philosophy applies. The manuscript should not
   force noisy residuals into a false no-noise two-shock representation; it
   should separate structural loading restrictions from diagonal-noise nuisance
   moments.
5. The finite-sample caution applies. Higher-order cumulants are noisy, and
   bootstrap or repeated-sample critical values are safer than pretending
   fourth-cumulant covariance estimates are sharp in macro samples.

These are analogies and design principles, not a theorem for the bivariate
SVAR.

## Manuscript Object: BR-Style Profiled Inversion

The manuscript object is therefore a Bonhomme-Robin-style profiled inversion:

$$
J_{\mathrm{stack}}(a,b)
=
T\min_{\gamma,\kappa,\xi_\eta}
\{\hat\mu_T-m(a,b,\gamma,\kappa,\xi_\eta)\}'
\hat W_T
\{\hat\mu_T-m(a,b,\gamma,\kappa,\xi_\eta)\},
$$

where

$$
\gamma=(\gamma_1,\gamma_2),
\qquad
\kappa=(\kappa_1,\kappa_2),
\qquad
\xi_\eta=(\nu_1,\nu_2,\tau_1,\tau_2,\rho_1,\rho_2).
$$

The candidate set is an inverted profiled criterion, usually intersected with
sign and label restrictions:

$$
\mathcal B_{\mathrm{profile},T}(c)
=
\{B(a,b):J_{\mathrm{stack}}(a,b)\leq c,\; B(a,b)\text{ satisfies labels}\}.
$$

This differs from Bonhomme-Robin quasi-JADE in four ways:

1. It parameterizes the bivariate loading matrix directly as `B(a,b)` rather
   than recovering a general `Lambda` by joint diagonalization.
2. It profiles structural and noise cumulants in a low-dimensional minimum
   distance problem instead of first identifying all error cumulants from the
   clean-pair null-space equations.
3. It uses signs as economic labels after the moment target is specified, not
   as a substitute for denoising.
4. Its validity must be proven from the bivariate cumulant map, profiled
   objective, and local rank conditions, then checked by symbolic/population
   and finite-sample simulations.

## Result Boundary

M07 establishes only the applicability boundary and the manuscript object. It
does not establish that the profiled inversion identifies `(a_0,b_0)`.

The next proof obligations are:

- M08: adversarially attack this applicability argument.
- M09: derive `J_4`, `J_stack`, the determinant condition, the local tangent,
  and the rank condition.
- M12: verify the cumulant map and population criterion symbolically and on
  population grids.

Until those tasks pass, `prop:robust-sign-inversion` remains planned rather
than draftable.
