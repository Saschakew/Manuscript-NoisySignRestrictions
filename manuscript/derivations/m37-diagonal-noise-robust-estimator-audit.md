# M37 Diagonal-Noise Robust Estimator Audit

Status: historical conditional pass, superseded by the M0034 scale correction.

M0034 later invalidated this audit's active pass judgment for the reported
six-moment diagonal-anchor object. In the `diag(B)=1` chart, the off-diagonal
covariance equation contains structural-shock variances unless unit shock
variances are imposed as an additional scale normalization. Use this note as a
record of the superseded M0030 object, not as the current Section 4 route.

Audit date: 2026-06-06.

Scope:

- `manuscript/derivations/dw-noise-robust-moments.md`
- `manuscript/derivations/dw-robust-comparison-diagnostic.md`
- `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`
- `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`
- `manuscript/simulations/m28_grid_story_validation.py`
- `manuscript/simulations/m29_calibrated_monte_carlo.py`

Question: does the post-M0030 diagonal-noise robust DW estimator survive a
direct audit strongly enough to support Section 4 theorem-level prose?

Answer: yes, conditionally. The reported robust-DW object is coherent as a
local normalized bivariate diagnostic under diagonal Gaussian residual noise.
The formal prose must not describe it as a global identification theorem, a
scale-free result for arbitrary impact matrices, a simultaneous confidence set,
or a robust procedure for correlated or non-Gaussian residual noise.

## Audited Estimator

The reported robust-DW statistic searches the common normalized chart

$$
B(b_{12},b_{21})=
\begin{bmatrix}
1 & b_{12}\\
b_{21} & 1
\end{bmatrix},
\qquad 1-b_{12}b_{21}\neq 0,
$$

after the sign screen. It stacks one diagonal-noise second-moment restriction
with five mixed higher cumulants of

$$
z_t(B)=B^{-1}u_t.
$$

The population target is

$$
G_D(B)=
\begin{bmatrix}
E(u_1u_2)-(b_{12}+b_{21})\\
\operatorname{cum}(z_1,z_1,z_2)\\
\operatorname{cum}(z_1,z_2,z_2)\\
\operatorname{cum}(z_1,z_1,z_1,z_2)\\
\operatorname{cum}(z_1,z_1,z_2,z_2)\\
\operatorname{cum}(z_1,z_2,z_2,z_2)
\end{bmatrix}.
$$

The sample implementation in `sign_dw_robust_noise_grid_figure.py` matches
this object: `offdiagonal_covariance_values` computes
`sample_cov(u1,u2) - (b12 + b21)`, and
`robust_higher_cumulant_values` computes the two mixed third central moments
and three fourth cumulants with covariance-product subtractions.

## Checklist

### 1. Off-Diagonal Covariance Anchor

Outcome: pass, conditional on the normalized bivariate chart and diagonal
noise.

If

$$
\Sigma_u=B_0B_0' + V,\qquad V=\operatorname{diag}(\nu_1,\nu_2),
$$

and

$$
B_0=
\begin{bmatrix}
1 & b_{12,0}\\
b_{21,0} & 1
\end{bmatrix},
$$

then

$$
\Sigma_{u,12}=(B_0B_0')_{12}=b_{12,0}+b_{21,0}.
$$

Thus the off-diagonal moment is zero at the true normalized point and does not
impose the false standard-DW recovered-shock restriction
`Cov(z_1(B),z_2(B))=0`.

The theorem-level caveat is scale. The equality `Cov(u_1,u_2)=b_{12}+b_{21}`
is not a harmless normalization for an arbitrary unit-variance impact matrix
with unknown diagonal scales. It is valid for the paper's diagonal-normalized
chart, or for a more general chart only after adding the relevant scale
parameters. Section 4 should therefore call the target the true normalized
impact matrix in the displayed chart.

### 2. Diagonal-Variance Profiling

Outcome: conditional pass.

The intended profiling argument is

$$
\Sigma_u-BB'=V(B),
$$

with the diagonal entries of `V(B)` treated as nuisance quantities. Retaining
only the off-diagonal equality is the right way to use second moments under
diagonal residual noise.

Current figure and Monte Carlo code do not enforce the optional admissibility
screen

$$
V_{11}(B)\ge 0,\qquad V_{22}(B)\ge 0.
$$

That is acceptable for the current diagnostic figures because the robust row
is defined as a moment-inversion comparison set, but theorem-level prose must
be explicit. Either define the formal robust set with these inequalities as an
additional admissibility screen, or state that the reported diagnostic profiles
diagonal variances without imposing nonnegativity in the plotted finite-sample
row. The latter is what the current code does.

### 3. Mixed Higher-Cumulant Stack

Outcome: pass under independent Gaussian residual noise.

The derivation and implementation use centered transformed residuals. The
third restrictions are third central moments. The fourth restrictions are
proper cumulants:

$$
\kappa_{1112}=E(z_1^3z_2)-3s_{11}s_{12},
$$

$$
\kappa_{1122}=E(z_1^2z_2^2)-s_{11}s_{22}-2s_{12}^2,
$$

$$
\kappa_{1222}=E(z_1z_2^3)-3s_{22}s_{12}.
$$

The covariance terms `s_ij` are nuisance ingredients inside the cumulants, not
structural restrictions. This is consistent across the derivation note, the
diagnostic note, the figure scripts, and M28/M29.

The result depends on Gaussian residual noise because every linear transform
of Gaussian noise has zero cumulants above order two. With non-Gaussian
residual noise, `B^{-1}eta_t` generally contributes mixed higher cumulants, so
the clean robust-DW interpretation fails unless additional restrictions on
residual-noise cumulants are imposed.

### 4. Chi-Square Degrees Of Freedom

Outcome: conditional pass for pointwise applied benchmarks.

The M0030 robust statistic has six displayed sample moments, so the
researcher-facing guide cutoff

$$
\chi^2_6(0.90)=10.64
$$

matches the implemented moment count. The standard-DW and sign/covariance rows
also use cutoffs consistent with their displayed moment counts.

This is not a simultaneous coverage statement. The statistic uses estimated
and regularized moment covariance matrices; the grid reuses data across
candidates; and the moment Jacobian can lose rank when structural higher
moments are weak or Gaussian. In the Gaussian structural-shock limit, the
higher-cumulant substack is all-null and the effective identification comes
from the covariance anchor. The manuscript should keep `chi2_6` language as a
pointwise applied benchmark and use M29's repeated, oracle, and bootstrap rows
as calibration-cost audits.

### 5. Fallback Language

Outcome: pass after making the fallback cases explicit.

- Diagonal Gaussian residual noise: use the reported six-moment diagonal-noise
  robust-DW set.
- Correlated Gaussian residual noise: drop the off-diagonal covariance anchor
  and report the pure higher-cumulant set. The higher-cumulant cancellation is
  still valid because Gaussianity is preserved under linear transforms.
- Diagonal non-Gaussian residual noise: the off-diagonal covariance anchor is
  still clean if the noise covariance is diagonal, but the transformed
  higher-cumulant stack is generally polluted. Do not call the six-moment set
  robust without modeling or subtracting residual-noise cumulants.
- Correlated non-Gaussian residual noise: neither the off-diagonal covariance
  anchor nor the transformed cumulant stack has the clean interpretation used
  in this paper.

The skewed-residual-noise row in M29 should remain a stress case. It can be
reported descriptively, but it is not evidence that the maintained Gaussian
route is valid under non-Gaussian residual noise.

## Consequence For Drafting

Section 4 can state a conditional local proposition:

*Under the diagonal-normalized bivariate chart, independent Gaussian residual
noise with diagonal covariance, and the non-Gaussian shock-rank conditions in
`dw-noise-robust-moments.md`, the diagonal-noise robust moment vector has zero
population value at the true normalized impact matrix. The off-diagonal
covariance component adds valid second-moment information, while the diagonal
variance targets and recovered-shock zero-covariance restriction are not
imposed.*

The proposition should also state the limits:

- the result identifies a normalized impact shape, not arbitrary column scales;
- global aliases and finite-order cumulant cancellations remain possible;
- nonnegative profiled variances are either an explicit admissibility screen or
  omitted from the diagnostic row;
- `chi2_6` is a pointwise finite-sample benchmark, not a coverage theorem;
- correlated or non-Gaussian residual noise requires the fallback language
  above.

M37 therefore clears the robust-DW estimator for disciplined Section 4 prose,
but not for an unconditional theorem. The next manuscript task should return
to literature positioning or to the separate M25 standard-DW proof audit.
