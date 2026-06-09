# M48 DW Moment Definition And Normalization Audit

Status: partial and not source-complete after M0045. Do not treat this file as
a completed audit or as a reliable source for the bivariate DW GMM moment menu.
It caught the broad fourth-product-versus-cumulant distinction, but it did not
study DW carefully enough to settle the exact bivariate moment stack, did not
derive the user's requested noisy product moments step by step, and made a
premature normalization/no-rebuild decision. M49 must redo this audit from the
user's original comments, raw DW source or KnowledgeVault notes, and explicit
derivations.

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

Answer status: superseded by M0045. The broad point that fourth-order raw
products differ from fourth cumulants remains useful, but the exact DW
moment menu, the Figure 1 source match, and the normalization/rebuild decision
are not settled by this file.

## 1. DW Source Moment Definition

M48 read the absorbed DW note and raw markdown as defining co-skewness through
standardized third products and co-kurtosis through standardized fourth
products. M0045 marks this as a partial reading that must be verified again in
M49 before it supports manuscript prose. The broad fourth-product targets read
in M48 were:

- `1` when the four indices consist of two distinct equal pairs;
- `3` when all four indices are equal;
- `0` otherwise.

Thus the standard-DW comparator should not be called a fourth-cumulant test
without qualification. The exact source-correct bivariate GMM stack, however,
remains for M49.

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

This records code behavior only. M0045 rejects the earlier inference that this
implementation proves the source-correct bivariate DW GMM menu. M49 must
compare the script to the source and decide whether omitted moments such as
`E(e_1^3 e_2)` and `E(e_1 e_2^3)` are legitimate omissions, simplifications,
or errors for the paper's stated comparator.

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

## 4. Normalization Status After M0045

No normalization decision is settled by M48. The manuscript currently uses the
common B-plane chart:

```text
B(a,b) = [[1, a],
          [b, 1]]
```

with structural-shock variances profiled in the robust covariance screen. The
user explicitly asked whether the paper should switch to
`Var(epsilon_i)=1`. M48 did not answer that carefully enough.

M49 must decide this after the source and noisy-moment audit:

- define precisely which normalization DW uses in the source;
- distinguish standardization of recovered shocks from normalization of `B`;
- state what changes under `diag(B)=1` versus `Var(epsilon)=1`;
- list all figure, Monte Carlo, caption, and registry rebuilds implied by any
  switch.

## 5. Rebuild Status After M0045

No no-rebuild conclusion is settled by M48. M49 must enumerate rebuild
requirements after it establishes the source-correct moment menu and
normalization.

Possible rebuild triggers include:

- the standard-DW row omits moments required by the source-correct bivariate
  DW stack;
- the paper switches from the `diag(B)=1` chart to a
  `Var(epsilon)=1` normalization;
- Section 4's robust cumulant stack changes after the requested noisy-moment
  derivations;
- the comparison metric or critical-value degrees of freedom change.

Affected surfaces would include Figure 1, Figure 2, Figure 3, M45-style Monte
Carlo evidence, captions, formal registry entries, and replication notes.

## 6. Manuscript Consequence After M0045

M48 does not resolve the user's comment enough for the current draft gate.

Do now:

- keep the Section 3 `g_DW` display behind a TODO note;
- keep M48 marked partial in planning and review surfaces;
- run M49 before M47 or any final Section 3/4 prose;
- treat this file as historical evidence of the failure mode, not as the
  source of settled manuscript claims.
