# Bivariate Cumulant Map

Status: audited working note. M06 found no coefficient or index errors in the
expanded cumulant map, but corrected the classification language around clean
equations versus identifying restrictions after nuisance profiling. The map
still needs the M09 profiled-criterion derivation and M12 symbolic/population
verification before it can support manuscript result claims.

Purpose: derive the complete second-, third-, and fourth-order cumulant map for
the bivariate diagonal-noise SVAR used in the Bonhomme-Robin-style profiled
inversion. This note is a derivation artifact, not polished manuscript prose.

Source context:

- `vault/syntheses/Bonhomme-Robin noise-robust SVAR moment inversion.md`
- `vault/papers/Consistent noisy independent component analysis.md`
- `manuscript/source-packet.md`

## Setup

Work with the diagonal-normalized bivariate impact matrix

$$
B(a,b)=
\begin{bmatrix}
1 & a\\
b & 1
\end{bmatrix},
\qquad
u_t=B(a,b)\varepsilon_t+\eta_t.
$$

Equivalently,

$$
u_{1t}=\varepsilon_{1t}+a\varepsilon_{2t}+\eta_{1t},
\qquad
u_{2t}=b\varepsilon_{1t}+\varepsilon_{2t}+\eta_{2t}.
$$

The derivation uses zero means, finite fourth moments, mutually independent
structural shocks, mutually independent idiosyncratic noise components, and
independence between structural shocks and noise. Here "diagonal noise" means
that mixed noise cumulants vanish through the orders used below, not merely
that the noise covariance matrix is diagonal. Structural shocks are normalized
to unit variance:

$$
\operatorname{cum}_2(\varepsilon_j,\varepsilon_j)=1,
\qquad j=1,2.
$$

Let structural third and fourth cumulants be

$$
\gamma_j=\operatorname{cum}_3(\varepsilon_j,\varepsilon_j,\varepsilon_j),
\qquad
\kappa_j=\operatorname{cum}_4(\varepsilon_j,\varepsilon_j,\varepsilon_j,
\varepsilon_j),
\qquad j=1,2.
$$

Let diagonal noise cumulants be

$$
\nu_i=\operatorname{cum}_2(\eta_i,\eta_i),
\qquad
\tau_i=\operatorname{cum}_3(\eta_i,\eta_i,\eta_i),
\qquad
\rho_i=\operatorname{cum}_4(\eta_i,\eta_i,\eta_i,\eta_i),
\qquad i=1,2.
$$

All mixed cumulants across distinct primitive components vanish. In particular,
there are no mixed noise nuisance terms such as
`cum(eta_1, eta_1, eta_2)` under the maintained diagonal idiosyncratic-noise
assumption.

## Cumulant Linearity Formula

For an order `r` cumulant with indices `i_1,...,i_r in {1,2}`, multilinearity
and primitive independence give

$$
C_{i_1\cdots i_r}
=
\sum_{j=1}^2
\left(\prod_{\ell=1}^r B_{i_\ell j}\right)\chi_{rj}
+
\mathbf 1\{i_1=\cdots=i_r=1\}\zeta_{r1}
+
\mathbf 1\{i_1=\cdots=i_r=2\}\zeta_{r2},
$$

where

$$
(\chi_{21},\chi_{22})=(1,1),
\qquad
(\chi_{31},\chi_{32})=(\gamma_1,\gamma_2),
\qquad
(\chi_{41},\chi_{42})=(\kappa_1,\kappa_2),
$$

and

$$
(\zeta_{21},\zeta_{22})=(\nu_1,\nu_2),
\qquad
(\zeta_{31},\zeta_{32})=(\tau_1,\tau_2),
\qquad
(\zeta_{41},\zeta_{42})=(\rho_1,\rho_2).
$$

The indicator terms appear only for pure own residual cumulants because the
noise components are independent across residual equations.

For fourth order, `K_{ijkl}` below denotes the fourth cumulant, not the fourth
central moment. For centered residuals,

$$
K_{ijkl}
=
E[u_i u_j u_k u_l]
-\sigma_{ij}\sigma_{kl}
-\sigma_{ik}\sigma_{jl}
-\sigma_{il}\sigma_{jk}.
$$

This distinction matters in code because Gaussian components contribute to
fourth central moments but have zero fourth cumulant.

## Second Cumulants

There are three distinct second cumulants:

$$
\begin{aligned}
\sigma_{11}
&=\operatorname{cum}(u_1,u_1)
=1+a^2+\nu_1,\\
\sigma_{12}
&=\operatorname{cum}(u_1,u_2)
=b+a,\\
\sigma_{22}
&=\operatorname{cum}(u_2,u_2)
=b^2+1+\nu_2.
\end{aligned}
$$

Thus the off-diagonal covariance is clean under diagonal noise, while the two
own variances contain the nuisance noise variances.

## Third Cumulants

There are four distinct third cumulants:

$$
\begin{aligned}
T_{111}
&=\operatorname{cum}(u_1,u_1,u_1)
=\gamma_1+a^3\gamma_2+\tau_1,\\
T_{112}
&=\operatorname{cum}(u_1,u_1,u_2)
=b\gamma_1+a^2\gamma_2,\\
T_{122}
&=\operatorname{cum}(u_1,u_2,u_2)
=b^2\gamma_1+a\gamma_2,\\
T_{222}
&=\operatorname{cum}(u_2,u_2,u_2)
=b^3\gamma_1+\gamma_2+\tau_2.
\end{aligned}
$$

The mixed third cumulants `T_{112}` and `T_{122}` are clean restrictions. The
pure third cumulants `T_{111}` and `T_{222}` are nuisance fits or diagnostics
unless extra restrictions are imposed on noise skewness.

## Fourth Cumulants

There are five distinct fourth cumulants:

$$
\begin{aligned}
K_{1111}
&=\operatorname{cum}(u_1,u_1,u_1,u_1)
=\kappa_1+a^4\kappa_2+\rho_1,\\
K_{1112}
&=\operatorname{cum}(u_1,u_1,u_1,u_2)
=b\kappa_1+a^3\kappa_2,\\
K_{1122}
&=\operatorname{cum}(u_1,u_1,u_2,u_2)
=b^2\kappa_1+a^2\kappa_2,\\
K_{1222}
&=\operatorname{cum}(u_1,u_2,u_2,u_2)
=b^3\kappa_1+a\kappa_2,\\
K_{2222}
&=\operatorname{cum}(u_2,u_2,u_2,u_2)
=b^4\kappa_1+\kappa_2+\rho_2.
\end{aligned}
$$

The mixed fourth cumulants `K_{1112}`, `K_{1122}`, and `K_{1222}` are clean
restrictions. The pure fourth cumulants `K_{1111}` and `K_{2222}` contain the
nuisance noise fourth cumulants.

## Moment Classification

Under unrestricted diagonal idiosyncratic noise, the clean observed equations
are

$$
\sigma_{12}=a+b,
$$

$$
\begin{bmatrix}
T_{112}\\
T_{122}
\end{bmatrix}
=
\begin{bmatrix}
b & a^2\\
b^2 & a
\end{bmatrix}
\begin{bmatrix}
\gamma_1\\
\gamma_2
\end{bmatrix},
$$

and

$$
\begin{bmatrix}
K_{1112}\\
K_{1122}\\
K_{1222}
\end{bmatrix}
=
\begin{bmatrix}
b & a^3\\
b^2 & a^2\\
b^3 & a
\end{bmatrix}
\begin{bmatrix}
\kappa_1\\
\kappa_2
\end{bmatrix}.
$$

The pure own cumulants profile nuisance noise cumulants:

$$
\nu_1=\sigma_{11}-(1+a^2),
\qquad
\nu_2=\sigma_{22}-(1+b^2),
$$

$$
\tau_1=T_{111}-\gamma_1-a^3\gamma_2,
\qquad
\tau_2=T_{222}-b^3\gamma_1-\gamma_2,
$$

and

$$
\rho_1=K_{1111}-\kappa_1-a^4\kappa_2,
\qquad
\rho_2=K_{2222}-b^4\kappa_1-\kappa_2.
$$

Consequently:

| Moment | Clean under diagonal noise? | Role under unrestricted nuisance profiling |
|---|---|---|
| `sigma_12` | yes | Direct covariance restriction `a+b=sigma_12`. |
| `sigma_11`, `sigma_22` | no | Nuisance variance fit and mapped-noise diagnostic. |
| `T_112`, `T_122` | yes | Clean equations, but with unrestricted `gamma=(gamma_1,gamma_2)` they usually fit structural skewness conditional on `(a,b)` rather than overidentify `(a,b)` by themselves. |
| `T_111`, `T_222` | no | Nuisance skewness fit or diagnostic. |
| `K_1112`, `K_1122`, `K_1222` | yes | Clean fourth-cumulant equations; with two unrestricted `kappa` parameters, they provide one profiled restriction on `(a,b)` when the loading matrix has the needed rank. |
| `K_1111`, `K_2222` | no | Nuisance fourth-cumulant fit or diagnostic. |

Pure own moments become additional restrictions for `(a,b)` only after adding
restrictions on the noise cumulants. Equality restrictions include no noise,
Gaussian noise, zero noise skewness, and zero noise fourth cumulant. Inequality
restrictions such as nonnegative variances or sign restrictions on noise
moments instead define admissible nuisance regions and diagnostics; they are
not overidentifying equalities.

## M06 Audit Record

The M06 adversarial audit checked the derivation against the task-board
requirements:

- Indices: independent coefficient enumeration of
  `prod_l B_{i_l j}` for all bivariate multisets of orders two, three, and four
  matched the displayed coefficients.
- Cumulant definitions: the fourth-order object is explicitly a cumulant, with
  covariance-product subtractions shown for centered residuals.
- Normalization: the second-cumulant equations rely on
  `cum_2(epsilon_j, epsilon_j)=1`; without this normalization, the variance
  diagnostic would be unidentified.
- Missing moments: the note lists all `r+1` distinct bivariate cumulants for
  each order `r=2,3,4`.
- Clean versus nuisance: the audit corrected the original wording so clean
  mixed third cumulants are not overstated as identifying restrictions after
  unrestricted profiling of `gamma`.

Remaining checks are outside M06: derive the profiled `J_4` and stacked
criteria, prove the local rank condition, and run symbolic/population
verification.

## Handoff To Later Tasks

This note completes the map required by M05 and the first adversarial audit
required by M06. It does not yet prove the Bonhomme-Robin applicability claim,
derive the `J_4` determinant condition, establish the local rank result, or
validate the map by simulation.

The next audit should check:

- the index convention in every mixed cumulant;
- the use of fourth cumulants rather than fourth central moments;
- the unit-variance normalization in the second cumulants;
- whether any pure own moment is mistakenly described as clean;
- whether extra noise restrictions are being smuggled into the unrestricted
  diagonal-noise map.
