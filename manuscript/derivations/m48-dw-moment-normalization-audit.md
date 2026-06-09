# M48 DW Moment Definition And Normalization Audit

Status: completed audit for draft correction and next-build planning.

Audit date: 2026-06-09.

Scope:

- `vault/papers/Refining set-identification in VARs through independence.md`
- `raw/drautzburg-2023-refining-set-identification/Refining_set-identification_in_VARs_through_independence.md`
- `manuscript/draft.md`
- `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`
- `manuscript/simulations/m45_variance_ratio_evidence.py`
- `manuscript/derivations/dw-noise-robust-moments.md`
- `manuscript/derivations/m40-variance-ratio-robust-dw-screen-audit.md`

Question: should the standard-DW comparator in Section 3 be described as a
fourth-cumulant stack, and should the active manuscript migrate from the
diagonal-normalized impact chart to a unit-variance structural-shock chart?

Answer: no on both. Drautzburg and Wright define standardized co-skewness and
co-kurtosis product moments. In their Gaussian benchmark, fourth product
moments take the Isserlis targets: `1` for two equal pairs, `3` for four equal
indices, and `0` otherwise once cross-correlations are zero. The Figure 1
standard-DW row implements the bivariate subset of this raw standardized
co-moment logic. The robust row must remain a cumulant stack because raw
fourth products are shifted by Gaussian residual-noise covariance terms. The
paper should keep the common `diag(B)=1` B-plane chart, profile structural
variances in the robust covariance screen, and use unit-variance language only
for the no-noise source model and standardized DW co-moment targets.

## 1. DW Source Moment Definition

The absorbed DW note and raw markdown define co-skewness as a standardized
third product and co-kurtosis as a standardized fourth product. The source then
uses Isserlis' theorem for the Gaussian case. With zero cross-correlations, the
fourth product target is:

- `1` when the four indices consist of two distinct equal pairs;
- `3` when all four indices are equal;
- `0` otherwise.

Thus the standard-DW comparator is not naturally described as a fourth
cumulant test. It is a standardized co-moment test of independence-like
restrictions. Cumulant language is still mathematically nearby, but it hides
the important target difference: the mixed pair fourth product
`E(e_i^2 e_j^2)` targets `1`, not `0`.

## 2. Figure 1 Implementation

`sign_dw_robust_noise_grid_figure.py` defines:

```text
MOMENTS_DW = ((1, 1), (2, 1), (1, 2), (2, 2))
moment_target((2, 2)) = 1.0
moment_target(other powers) = 0.0
```

Before computing these products, `standardized_candidate_shocks` demeans and
standardizes each recovered-shock column. It does not decorrelate the two
columns at arbitrary candidate `B` in the diagonal-normalized grid. The
standard-DW row therefore tests:

```text
E(e_1 e_2) = 0
E(e_1^2 e_2) = 0
E(e_1 e_2^2) = 0
E(e_1^2 e_2^2) = 1
```

This is aligned with a bivariate co-skewness/co-kurtosis product-moment
comparator, not with the six-entry cumulant stack currently described in the
old Section 3 wording. The script omits the singleton fourth products
`E(e_1^3 e_2)` and `E(e_1 e_2^3)`, which also have zero DW-style product
targets under independence and zero cross-correlation. That omission is a
finite moment-menu choice, not a cumulant/product mismatch.

## 3. Noisy Truth Moments

At the true impact matrix, write

```text
z_t(B_0) = B_0^{-1}u_t = epsilon_t + xi_t,
xi_t = B_0^{-1}eta_t.
```

Assume `epsilon_t` has independent mean-zero components with variances `s_i`,
`xi_t` is independent Gaussian with covariance `Omega`, and define

```text
S_ij = Cov(z_i,z_j) = 1{i=j} s_i + Omega_ij.
```

The mixed higher cumulants of `z_t(B_0)` vanish because structural components
are independent and Gaussian noise has no cumulants above order two. The raw
moments do not generally vanish. For distinct indices as indicated below:

```text
E(z_i^2 z_j) = 0
E(z_i z_j z_k) = 0
E(z_i^3 z_j) = 3 S_ii S_ij
E(z_i^2 z_j^2) = S_ii S_jj + 2 S_ij^2
E(z_i^2 z_j z_k) = S_ii S_jk + 2 S_ij S_ik
E(z_i z_j z_k z_l) = S_ij S_kl + S_ik S_jl + S_il S_jk
```

If the variables are standardized to unit variance, replace `S_ij` by the
correlation `R_ij` in the formulas after setting diagonal entries to one:

```text
E(\tilde z_i^3 \tilde z_j) = 3 R_ij
E(\tilde z_i^2 \tilde z_j^2) = 1 + 2 R_ij^2
E(\tilde z_i^2 \tilde z_j \tilde z_k) = R_jk + 2 R_ij R_ik
E(\tilde z_i \tilde z_j \tilde z_k \tilde z_l)
  = R_ij R_kl + R_ik R_jl + R_il R_jk
```

Under the no-noise DW covariance-rotation null, cross-correlations are zero,
so these formulas collapse to the DW co-kurtosis product targets. Under
evaluation at the true structural matrix with residual noise,
`S_ij = Omega_ij` for `i != j`, and those raw fourth products are shifted when
`Omega_ij != 0`. This is why raw fourth product moments are not
Gaussian-noise-blind.

The robust Section 4 cumulants subtract exactly these covariance-product
terms:

```text
kappa_iiij = E(z_i^3 z_j) - 3 S_ii S_ij = 0
kappa_iijj = E(z_i^2 z_j^2) - S_ii S_jj - 2 S_ij^2 = 0
```

and similarly for the remaining mixed fourth cumulants.

## 4. Normalization Decision

Keep the manuscript's common B-plane chart:

```text
B(a,b) = [[1, a],
          [b, 1]]
```

with structural-shock variances profiled in the robust covariance screen. Do
not migrate the whole paper to a unit-variance structural-shock chart.

Reasons:

- The standard DW source assumes unit-variance shocks and uses standardized
  recovered shocks, but that is a comparator convention, not a reason to
  abandon the common plotted impact-shape chart.
- The robust variance-ratio screen already fixes the M0034
  double-normalization problem by profiling `s_i` and `nu_i`.
- Migrating the paper to `Var(epsilon_i)=1` as the main chart would require
  rebuilding the figures, Monte Carlo grids, captions, and comparison metrics,
  and it would make the current `diag(B)=1` visual evidence noncomparable.
- The active paper's recommendation is to compare standard DW and robust DW in
  one normalized impact-shape chart; `diag(B)=1` serves that reader path.

The draft should therefore make the split explicit:

1. Standard DW comparator: standardized raw co-skewness/co-kurtosis product
   moments with Gaussian-Isserlis fourth-product targets.
2. Robust DW construction: mixed higher cumulants of `B^{-1}u`, with
   covariance terms used only as nuisance ingredients inside fourth cumulants.
3. Scale information: variance-ratio covariance screen in the
   diagonal-normalized chart, not a free unit-variance normalization.

## 5. Rebuild Implications

No immediate Figure 1 rebuild is required from the moment-definition audit
alone because the standard-DW row already implements the raw standardized
product-moment subset. The immediate required change is prose and registry
alignment.

Future optional rebuilds:

- Add `E(e_1^3 e_2)` and `E(e_1 e_2^3)` to the standard-DW row if the paper
  wants a fuller bivariate fourth-product menu. This would change the
  standard-DW cutoff and would require rebuilding Figure 1, Figure 2,
  Figure 3, and the M45 Monte Carlo table.
- Keep the current four-moment standard-DW subset if the paper wants to
  preserve the established evidence spine. Then captions and derivation notes
  should call it a bivariate co-moment subset rather than the full DW GMM
  menu.
- Do not rebuild solely to migrate to unit-variance normalization unless a
  later scope decision abandons the common diagonal-normalized B-plane.

## 6. Manuscript Consequence

M48 resolves the comment enough for the current draft gate:

- Section 3 should replace "three mixed fourth cumulants" with standardized
  co-skewness/co-kurtosis product moments.
- Section 4 should keep the higher-cumulant stack and explain that cumulant
  subtraction is precisely what removes the Gaussian residual-noise covariance
  shifts in raw fourth products.
- The formal registry should mark the standard-DW moment-stack description as
  audited after M48 and the robust cumulant stack as still active after M48.
- M47 remains open: this audit does not prove the rich-stack generic emptying
  claim. It only fixes the moment-definition and normalization gate.
