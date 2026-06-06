# Standard DW J-Test Inversion Under Residual Noise

Status: M25 working derivation for the simultaneous-SVAR manuscript. This note
proves a bounded version of the standard-DW misspecification claim: under
residual noise, the usual covariance-whitened J-test inversion is generically
empty in population when the higher-moment stack is rich enough to test
independence. The statement has important exceptions, so the manuscript should
not claim unconditional emptying.

Scope: this is an impact-only derivation. The residual `u_t` is the object of
interest. No VAR lags, lag estimation, dynamic impulse responses, or
horizon-specific sign restrictions are part of the argument.

## 1. Setup

Let

$$
u_t=B_0\varepsilon_t+\eta_t,
$$

where `B_0` is nonsingular, the components of `epsilon_t` are mutually
independent, `E(epsilon_t)=0`, and `E(epsilon_t epsilon_t')=I`. The residual
noise is independent of `epsilon_t` and has covariance `V`:

$$
E(\eta_t)=0,\qquad E(\eta_t\eta_t')=V.
$$

The observed residual covariance is

$$
\Sigma_u=B_0B_0'+V.
$$

Standard sign-restricted SVAR analysis builds candidates from a factor of this
observed covariance:

$$
P_*P_*'=\Sigma_u,\qquad B(Q)=P_*Q,\qquad Q'Q=I.
$$

The standard DW-style recovered shocks are

$$
e_t(Q)=B(Q)^{-1}u_t=Q'P_*^{-1}u_t.
$$

They are covariance-normalized in population:

$$
\operatorname{Var}\{e_t(Q)\}=I.
$$

This covariance normalization is exactly what makes the standard route
fragile: it is valid for the noisy covariance `Sigma_u`, not for the structural
covariance `B_0B_0'`.

## 2. Population J-Test Inversion

Let `g(e)` be the vector of no-noise DW higher-moment independence restrictions
used after sign filtering. For example, in the bivariate fourth-order route it
can contain mixed third central moments and mixed fourth cumulants. Let

$$
g_\infty(Q)=E\{g(e_t(Q))\}.
$$

The population J objective is

$$
J_\infty(Q)=g_\infty(Q)'Wg_\infty(Q),
$$

where `W` is positive definite on the moment stack. The population standard-DW
accepted set is

$$
\mathcal Q_{DW,\infty}
=
\{Q:\text{sign restrictions hold and } g_\infty(Q)=0\}.
$$

The sample J-test inversion accepts candidates satisfying

$$
J_T(Q)=T\widehat g_T(Q)'\widehat W_T\widehat g_T(Q)\le c_T.
$$

If `Q` is fixed and `g_\infty(Q)\neq 0`, then

$$
T^{-1}J_T(Q)\to J_\infty(Q)>0,
$$

so the candidate is rejected with probability approaching one for fixed or
standard slowly growing critical values.

Thus population emptiness is the right first question: does the noisy
covariance-rotation space contain any sign-admissible candidate whose
recovered shocks satisfy the no-noise higher-moment restrictions?

## 3. Gaussian Residual Noise

First suppose

$$
\eta_t\ \text{is Gaussian and independent of}\ \varepsilon_t.
$$

For any covariance-whitened candidate,

$$
e_t(Q)
=Q'P_*^{-1}B_0\varepsilon_t+Q'P_*^{-1}\eta_t
=M(Q)\varepsilon_t+\zeta_t(Q),
$$

where

$$
M(Q)=Q'P_*^{-1}B_0.
$$

The Gaussian component has zero cumulants above order two, so all higher
cumulants of `e_t(Q)` are the higher cumulants of `M(Q)epsilon_t`. Therefore
the no-noise higher-moment restrictions vanish only when the linear mixtures
in `M(Q)epsilon_t` look independent according to the chosen moment stack.

If the moment stack is rich enough to enforce independence of the recovered
components, and if the structural shocks satisfy the usual non-Gaussian ICA
rank condition, this requires

$$
M(Q)=D\Pi,
$$

where `D` is nonsingular diagonal and `Pi` is a signed permutation matrix
consistent with the sign-labeling convention. Equivalently,

$$
B(Q)=B_0\Pi'D^{-1}.
$$

But every standard candidate also satisfies `B(Q)B(Q)'=\Sigma_u`, so a
population zero can exist only if

$$
B_0\Pi'D^{-2}\Pi B_0'=B_0B_0'+V.
$$

Equivalently,

$$
B_0^{-1}VB_0^{-1'}
=
\Pi'D^{-2}\Pi-I.
$$

This is a structural-coordinate column-rescaling condition. The matrix on the
right-hand side is diagonal up to the accepted label convention. For a generic
residual-noise covariance `V`, `B_0^{-1}VB_0^{-1'}` is not diagonal. Then no
covariance-whitened candidate can both factor the noisy covariance and recover
independent structural shocks.

This proves the useful generic statement:

> In the simultaneous impact model with independent non-Gaussian structural
> shocks and independent Gaussian residual noise, a rich standard-DW J-test
> inversion is generically empty in population. Population zeros exist only in
> special cases where residual noise is observationally equivalent to a
> diagonal rescaling of structural columns, up to sign and label aliases.

The special case matters. If

$$
V=B_0\Lambda B_0',
\qquad
\Lambda=\Lambda'\ \text{diagonal and nonnegative},
$$

then `B=B_0(I+\Lambda)^{1/2}` is a factor of `Sigma_u`. The recovered shocks
are a diagonal rescaling of `epsilon_t` plus Gaussian noise in the same
structural coordinates, so mixed higher cumulants vanish even though the impact
matrix is scaled away from `B_0`. In that case the standard DW inversion need
not be empty, but it targets a covariance-noisy pseudo-candidate rather than
the unit-variance structural impact matrix.

## 4. Non-Gaussian Residual Noise

If `eta_t` is non-Gaussian, then `Q'P_*^{-1}eta_t` generally contributes
higher cumulants. Even a structural-coordinate rescaling candidate need not
satisfy the no-noise higher-moment restrictions, because transformed residual
noise can add mixed third or fourth cumulants.

Thus non-Gaussian residual noise strengthens the misspecification warning, but
it also makes the exact emptying statement depend on the residual-noise
cumulant structure. The first paper should not claim a universal theorem for
all non-Gaussian noise. It should use non-Gaussian residual noise as a stress
case in the early Monte Carlo and in later robustness checks.

## 5. Finite Moment Stacks And Aliases

The argument above uses a rich independence interpretation of the J-test stack.
Actual implementations often use a finite set of moments, for example mixed
third moments and fourth cumulants. A finite stack can have accidental zeros:

- weak or zero third/fourth cumulants for one shock;
- cancellations between the two structural shocks in the displayed cumulant
  polynomials;
- label or sign aliases not ruled out by the economic sign restrictions;
- near-boundary cases where the population criterion is small but not zero.

Therefore the manuscript should state the standard-DW result in two layers:

1. Rich-stack benchmark: under generic residual noise, the population
   covariance-whitened DW inversion is empty.
2. Finite-stack implementation: if the stack has accidental zeros, the
   inversion can contain pseudo-candidates; otherwise the population criterion
   is bounded away from zero on compact sign-admissible regions and the
   sample accepted set empties asymptotically.

## 6. Least-Rejected Interpretation

Let the sign-admissible covariance-rotation space be compact after excluding
singular or near-unlabeled regions. If

$$
\inf_Q J_\infty(Q)=\delta>0,
$$

then strict J-test inversion with fixed critical values is empty with
probability approaching one. In finite samples, however, researchers may still
report least-rejected candidates or use finite-sample critical values that
leave a small accepted region around the minimizer of `J_\infty(Q)`.

This is the false-sharpening channel:

$$
Q^\dagger\in\arg\min_Q J_\infty(Q)
$$

is a pseudo-true covariance-noisy candidate, not the structural impact matrix.
Finite-sample inversion can look precise because it concentrates around
`Q^\dagger`, not because residual noise has been solved.

## 7. Manuscript Statement

The draft should avoid the blunt sentence "standard DW is generically empty"
unless the assumptions are shown beside it. A safer proposition is:

> Under the simultaneous residual model `u_t=B_0 epsilon_t+eta_t`, standard
> DW inversion searches over factors of `Sigma_u=B_0B_0'+V`. With independent
> Gaussian residual noise and a rich higher-moment independence stack, the
> population accepted set is empty for generic `V`. Non-empty population zeros
> require residual noise to be equivalent to a diagonal structural-coordinate
> rescaling, or require finite-moment aliases. When no such zero exists, the
> sample J-test inversion empties asymptotically, while finite-sample
> least-rejected sets can still look falsely precise around pseudo-true noisy
> candidates.

This result gives the analytical idea needed before the early Monte Carlo
triage: simulate whether the finite-sample J-test inversion actually empties,
shrinks around pseudo-candidates, or becomes too noisy to support the proposed
standard-DW versus robust-DW diagnostic.
