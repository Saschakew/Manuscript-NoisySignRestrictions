# M49 DW Source And Noisy Moment Audit

Status: source and derivation audit complete; evidence rebuild required before
the current figures or Monte Carlo table can be called source-correct
standard-DW evidence.

Audit date: 2026-06-09.

Task packet: `manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md`.

## 1. Claim Ledger Outcome

| Claim | Status | Evidence |
|---|---|---|
| DW fourth-order GMM entries are standardized raw product moments with Gaussian two-pair targets, not fourth cumulants. | `raw-source` | Drautzburg and Wright, Section 2.2.1, equations (2.6)-(2.9), and the moment vector on Journal of Econometrics p. 1832; raw path `C:\Users\smsakewe\Documents\GitHub\KnowledgeVault\raw\drautzburg-2023-refining-set-identification\Refining_set-identification_in_VARs_through_independence.md`. |
| In the bivariate case, DW GMM1 includes `112`, `122`, `1112`, `1122`, and `1222`; DW GMM2 drops the symmetric `1122` kurtosis condition. | `raw-source` plus `derived` translation | Source counts `binom(p+2,3)-p` third products and `binom(p+3,4)-p` fourth products, with the later GMM2 drop of `p(p-1)/2` symmetric kurtosis conditions; bivariate specialization below. |
| Figure 1's current standard-DW code is source-correct. | `code-implemented`, source comparison failed | `sign_dw_robust_noise_grid_figure.py` uses covariance, `112`, `122`, and `1122`; it omits `1112` and `1222`, so it is not DW GMM1 or GMM2. |
| Third-order robust cumulants equal centered raw third product moments and are unaffected by additive independent Gaussian residual noise at `B=B0`. | `derived` | Section 4 below. |
| Fourth-order robust cumulants differ from DW fourth raw-product moments by covariance-product subtractions that matter under residual noise and in finite samples. | `derived` plus `raw-source` comparison | Sections 3-5 below. |
| Switching all manuscript figures from `diag(B)=1` to `Var(epsilon)=1` is required by DW source alignment. | `conjectural/user-decision gate` | DW's source-native parameter is a unit-variance covariance-rotation chart. The manuscript may still use a common normalized B-plane if it states this as a reporting chart and implements source-correct standardized moments. A full chart switch is a major user decision and rebuild task. |

## 2. Source Extraction

Drautzburg and Wright define the standard VAR impact model as

```text
u_t = A epsilon_t,    Cov(u_t) = A A' = Sigma,
epsilon_t has independent components with mean zero and unit variances.
```

The candidate impact matrix is `A_tilde = Sigma^tr Q`, with `Q` orthonormal,
and the recovered shocks are `epsilon_hat_t(A_tilde)=A_tilde^{-1}u_t`
(equations (2.1)-(2.2)). Thus the source-native candidate space is already
covariance-normalized: equation (2.8) shows that
`Var(A_tilde^{-1}u_t)=I_p` for every candidate rotation.

In Section 2.2.1, equations (2.6)-(2.7), co-skewness and co-kurtosis are
standardized raw products of recovered shocks. They are not cumulants. Remark
2, equation (2.9), gives the Gaussian co-kurtosis target:

```text
CK_ijkl = CR_ij CR_kl + CR_jk CR_il + CR_ki CR_jl.
```

Because cross-correlations are zero in the source-native rotation chart,
the fourth product target is `1` for two distinct equal pairs, `3` for four
equal indices, and `0` otherwise.

On Journal of Econometrics p. 1832, the moment-based test defines a vector
`f(y_t,Q,phi)` containing:

- all third standardized raw products with at least two distinct indices, and
- all fourth standardized raw products with at least two distinct indices,
  subtracting the indicator that the indices form two distinct pairs.

The source then distinguishes:

- GMM1: the full moment vector under strong independence;
- GMM2: the same vector after dropping the symmetric kurtosis conditions
  `E[epsilon_i^2 epsilon_k^2]=1`, `i<k`, to accommodate common stochastic
  volatility under the weaker Assumption 2.

## 3. Bivariate Translation

Let `h_i(Q)` denote the centered, standardized recovered shock in coordinate
`i`. For `p=2`, the unordered third products with at least two distinct
indices are

```text
E[h_1^2 h_2] = 0,
E[h_1 h_2^2] = 0.
```

The unordered fourth products with at least two distinct indices are

```text
E[h_1^3 h_2] = 0,
E[h_1^2 h_2^2] - 1 = 0,
E[h_1 h_2^3] = 0.
```

Thus the source-correct bivariate GMM1 higher-moment menu is

```text
g_DW,GMM1(Q) =
[
  E[h_1^2 h_2],
  E[h_1 h_2^2],
  E[h_1^3 h_2],
  E[h_1^2 h_2^2] - 1,
  E[h_1 h_2^3]
]'.
```

The bivariate GMM2 menu drops only the symmetric kurtosis condition:

```text
g_DW,GMM2(Q) =
[
  E[h_1^2 h_2],
  E[h_1 h_2^2],
  E[h_1^3 h_2],
  E[h_1 h_2^3]
]'.
```

The covariance moment `E[h_1 h_2]=0` is not part of DW's higher-moment vector
because the source searches over covariance-normalized rotations. In the
manuscript's `diag(B)=1` B-plane, a covariance moment may be needed to mimic
the standard no-noise covariance restriction, but it is a manuscript chart
addition, not a DW higher-moment entry.

## 4. Figure 1 Code Audit

`manuscript/simulations/sign_dw_robust_noise_grid_figure.py` implements the
current standard-DW row as code behavior:

```text
MOMENTS_DW = ((1, 1), (2, 1), (1, 2), (2, 2))
moment_target((2, 2)) = 1
moment_target(other powers) = 0
```

The function `standardized_candidate_shocks` first centers and standardizes
the two recovered-shock columns. The statistic then applies `j_statistic` to
the four raw product moments:

```text
E[h_1 h_2] = 0,
E[h_1^2 h_2] = 0,
E[h_1 h_2^2] = 0,
E[h_1^2 h_2^2] - 1 = 0.
```

`m45_variance_ratio_evidence.py` imports this base module and uses the same
`MOMENTS_DW` object for truth checks, grid metrics, and Monte Carlo rows.

Classification:

- `code-implemented`: Figure 1 and M45 use a four-moment standardized product
  stack with covariance, two third products, and the symmetric fourth product.
- `raw-source`: DW GMM1 in the bivariate case uses five higher product
  moments, including `1112` and `1222`, and does not include covariance inside
  the higher-moment vector.
- `raw-source`: DW GMM2 drops `1122` and keeps `1112` and `1222`.
- `audit outcome`: the current standard-DW row is not source-correct GMM1 or
  GMM2. It is a historical simplified hybrid. Any source-correct evidence
  claim must rebuild the standard-DW statistic.

## 5. Noisy Moment Derivations At `B=B0`

At the true impact matrix, write

```text
z = B0^{-1}u = epsilon + xi,
xi = B0^{-1} eta.
```

Assumptions for this derivation:

- `epsilon` has independent centered components with
  `Var(epsilon_i)=s_i`.
- `eta` is centered Gaussian, independent of `epsilon`, and has independent
  components in the residual coordinates.
- Therefore `xi` is centered Gaussian with covariance
  `Omega = B0^{-1} Var(eta) B0^{-1'}`. The components of `xi` need not be
  independent after the `B0^{-1}` transformation.
- Define `S_ij = Cov(z_i,z_j) = 1{i=j}s_i + Omega_ij`.

The requested formulas are for mixed indices. When the display uses
`i,j,k,l`, read the indices as distinct unless powers show otherwise.

### 5.1 `E[z_i^2 z_j]`, `i != j`

Expand:

```text
E[(epsilon_i + xi_i)^2 (epsilon_j + xi_j)]
= E[epsilon_i^2 epsilon_j]
  + E[epsilon_i^2 xi_j]
  + 2 E[epsilon_i xi_i epsilon_j]
  + 2 E[epsilon_i xi_i xi_j]
  + E[xi_i^2 epsilon_j]
  + E[xi_i^2 xi_j].
```

Every term is zero: the structural terms have an unmatched centered structural
shock, the mixed structural-noise terms factor into a zero mean, and the
centered Gaussian third moment is zero. Hence

```text
E[z_i^2 z_j] = 0.
```

### 5.2 `E[z_i z_j z_k]`, distinct `i,j,k`

Each term in the expansion of
`(epsilon_i+xi_i)(epsilon_j+xi_j)(epsilon_k+xi_k)` contains either an
unmatched centered structural shock or a centered Gaussian third product.
Thus

```text
E[z_i z_j z_k] = 0.
```

This is the general version of the bivariate robust third-moment result:
centered third cumulants equal centered raw third moments, and additive
Gaussian residual noise does not shift them at `B0`.

### 5.3 `E[z_i^3 z_j]`, `i != j`

The nonzero terms in
`(epsilon_i+xi_i)^3(epsilon_j+xi_j)` are

```text
3 E[epsilon_i^2] E[xi_i xi_j]
+ E[xi_i^3 xi_j].
```

For centered Gaussian `xi`, `E[xi_i^3 xi_j]=3 Omega_ii Omega_ij`. Therefore

```text
E[z_i^3 z_j]
= 3 s_i Omega_ij + 3 Omega_ii Omega_ij
= 3 S_ii S_ij.
```

With `Var(epsilon_i)=1`,

```text
E[z_i^3 z_j] = 3 (1 + Omega_ii) Omega_ij.
```

After standardizing `z_i` and `z_j` to unit variance, with
`R_ij=S_ij/sqrt(S_ii S_jj)`,

```text
E[tilde z_i^3 tilde z_j] = 3 R_ij.
```

DW's source target for this singleton fourth product is zero. Under residual
noise it is shifted whenever `R_ij != 0`.

### 5.4 `E[z_i^2 z_j^2]`, `i != j`

The nonzero expansion terms are

```text
E[epsilon_i^2 epsilon_j^2]
+ E[epsilon_i^2] E[xi_j^2]
+ E[epsilon_j^2] E[xi_i^2]
+ E[xi_i^2 xi_j^2].
```

Because `epsilon_i` and `epsilon_j` are independent,
`E[epsilon_i^2 epsilon_j^2]=s_i s_j`. By Isserlis' formula,
`E[xi_i^2 xi_j^2]=Omega_ii Omega_jj + 2 Omega_ij^2`. Thus

```text
E[z_i^2 z_j^2]
= s_i s_j + s_i Omega_jj + s_j Omega_ii
   + Omega_ii Omega_jj + 2 Omega_ij^2
= S_ii S_jj + 2 S_ij^2.
```

With `Var(epsilon_i)=Var(epsilon_j)=1`,

```text
E[z_i^2 z_j^2]
= (1 + Omega_ii)(1 + Omega_jj) + 2 Omega_ij^2.
```

After standardizing,

```text
E[tilde z_i^2 tilde z_j^2] = 1 + 2 R_ij^2.
```

DW's GMM1 target subtracts `1`, so the residual-noise shift is
`2 R_ij^2` after standardization.

### 5.5 `E[z_i^2 z_j z_k]`, distinct `i,j,k`

The nonzero terms are the structural variance in coordinate `i` times the
Gaussian covariance between `j` and `k`, plus the Gaussian fourth product:

```text
E[z_i^2 z_j z_k]
= s_i Omega_jk
  + E[xi_i^2 xi_j xi_k].
```

By Isserlis' formula,

```text
E[xi_i^2 xi_j xi_k]
= Omega_ii Omega_jk + 2 Omega_ij Omega_ik.
```

Hence

```text
E[z_i^2 z_j z_k]
= S_ii S_jk + 2 S_ij S_ik.
```

With `Var(epsilon_i)=1`,

```text
E[z_i^2 z_j z_k]
= (1 + Omega_ii) Omega_jk + 2 Omega_ij Omega_ik.
```

After standardizing,

```text
E[tilde z_i^2 tilde z_j tilde z_k]
= R_jk + 2 R_ij R_ik.
```

### 5.6 `E[z_i z_j z_k z_l]`, distinct `i,j,k,l`

All structural terms have unmatched centered structural shocks. The only
nonzero term is the centered Gaussian fourth product:

```text
E[z_i z_j z_k z_l]
= E[xi_i xi_j xi_k xi_l].
```

By Isserlis' formula,

```text
E[z_i z_j z_k z_l]
= S_ij S_kl + S_ik S_jl + S_il S_jk.
```

With unit structural variances, the same formula holds because all indices are
distinct and the off-diagonal `S_ab` equal `Omega_ab`. After standardization,

```text
E[tilde z_i tilde z_j tilde z_k tilde z_l]
= R_ij R_kl + R_ik R_jl + R_il R_jk.
```

## 6. Cumulants Versus DW Raw Products

For centered variables, third cumulants are third central moments. Therefore
the robust third restrictions

```text
cum(z_i,z_i,z_j) = E[z_i^2 z_j],
cum(z_i,z_j,z_j) = E[z_i z_j^2]
```

coincide with the corresponding raw third-product restrictions, and they are
not shifted by additive independent Gaussian residual noise at `B0`.

Fourth cumulants are different. For example,

```text
cum(z_i,z_i,z_i,z_j)
= E[z_i^3 z_j] - 3 S_ii S_ij,

cum(z_i,z_i,z_j,z_j)
= E[z_i^2 z_j^2] - S_ii S_jj - 2 S_ij^2.
```

The derivations above show exactly why those subtractions are needed under
residual noise:

```text
E[z_i^3 z_j] = 3 S_ii S_ij,
E[z_i^2 z_j^2] = S_ii S_jj + 2 S_ij^2,
```

so the corresponding mixed fourth cumulants vanish at `B0` under the Gaussian
residual-noise model. DW's raw standardized fourth products instead use the
Gaussian covariance-rotation targets. Those targets are correct in DW's
source-native no-noise covariance-normalized chart, but at the true structural
matrix under residual noise they are shifted whenever transformed residual
noise creates nonzero cross-correlation.

Finite-sample implication: a raw fourth product such as
`mean(h_1^2 h_2^2)-1` is one sample moment. A fourth cumulant estimator is a
nonlinear combination of raw product and sample covariance terms. Treating the
two as interchangeable changes both the finite-sample statistic and its
estimated influence/covariance matrix. The user's warning is correct.

## 7. Normalization And Rebuild Decision

DW's source-native normalization has two layers:

1. structural shocks have unit variances in the model; and
2. candidates are covariance-equivalent rotations `A_tilde=Sigma^tr Q`, so
   recovered shocks have unit covariance for every `Q`.

The current manuscript uses a common reporting chart

```text
B(a,b) = [[1, a],
          [b, 1]]
```

and profiles structural-shock variances in the robust covariance screen. This
chart is not DW's native parameterization, but it can still be used as a
common comparison chart if the draft is explicit that:

- the chart fixes impact-shape scale for reporting;
- the standard-DW source moments are computed on centered, standardized
  recovered shocks; and
- any added covariance moment is a no-noise covariance-screen component needed
  in the B-plane chart, not a DW higher-moment entry.

Source alignment therefore requires a standard-DW moment-menu rebuild. It does
not logically force the entire manuscript to abandon the `diag(B)=1` chart in
this audit. A full switch to a unit-variance structural-shock chart is a major
user-decision gate because it would change the plotted coordinate system, the
variance-ratio robust covariance screen, Figure 1, Figure 2, Figure 3, and the
M45-style Monte Carlo evidence.

## 8. Required Follow-Up

Do not rely on the current Figure 1 standard-DW row, Figure 2 row, Figure 3
row, or M45 table as source-correct DW evidence. They remain useful historical
diagnostics for the simplified hybrid statistic only.

The next rebuild task should decide between two implementation targets:

1. `diag(B)=1` common-chart rebuild:
   - keep the current B-plane chart;
   - use a standard no-noise covariance moment to screen the B-plane;
   - replace `MOMENTS_DW` with the source-correct GMM1 higher menu
     `112,122,1112,1122,1222` or with GMM2 `112,122,1112,1222`;
   - update chi-square degrees of freedom and captions accordingly.
2. unit-variance/rotation-chart rebuild:
   - reparameterize the standard-DW comparison in DW's native `Sigma^tr Q`
     chart;
   - redesign how the robust variance-ratio set is shown in the same chart;
   - rerender all figures and rerun M45-style evidence.

The first path is a smaller source-correct repair. The second path may be
closer to the literature's normalization, but it is larger and should be an
explicit user decision before implementation.

## 9. Outcome

M49 resolves the source and derivation questions that M48 left unsettled:

- the exact bivariate DW GMM1/GMM2 higher-moment menus are now source-backed;
- Figure 1/M45 code is classified as a simplified hybrid, not source-correct
  DW;
- the six requested noisy moments are derived from
  `z=epsilon+B0^{-1}eta`;
- third robust moments coincide with raw third products, while fourth robust
  cumulants differ from DW raw fourth products by covariance-product
  subtractions;
- normalization is not silently decided; a chart switch remains a user
  decision gate with a large rebuild cost.

