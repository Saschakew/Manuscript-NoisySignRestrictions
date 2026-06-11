# M56 Robust Cumulant GMM Generated-Moment Audit

Status: `done`

Priority: 1

Task-board row: `M56`

Transparency milestone: M0055

Created after: M55 planning. This task must run before M55 writes the main
text explanation and before M52 rebuilds evidence, because it can change the
valid finite-sample criterion, weighting matrix, degrees of freedom, and
interpretation of the robust DW row.

## Original User Prompt

> plan another task to evaulate and take care of the following problem: If
> s22_hat(B) = (1/T) sum_t ztilde_2t(B)^2,
>
> s12_hat(B) = (1/T) sum_t ztilde_1t(B) ztilde_2t(B), and
>
> g1222_hat(B)
> = (1/T) sum_t ztilde_1t(B) ztilde_2t(B)^3
>   - 3 * s22_hat(B) * s12_hat(B). this means that the moment g1222_hat(B)
> = (1/T) sum_t ztilde_1t(B) ztilde_2t(B)^3
>   - 3 * (1/T) sum_t ztilde_2t(B)^2 * (1/T) sum_t ztilde_1t(B) ztilde_2t(B).
> But, this is not a standard GMM moment condition!! its like a sum of three
> moment conditoins! i think we cant apply standard gmm theory to this moment
> conditions, can we? it would be possible if we can replace s22_hat(B) and
> s12_hat(B) by numbers or so, but it it is a moment condition itself...i dont
> know... but if at B_0 it holds that s_11(B0) = E[z_1^2] = 1 + Omega_11, then
> we could just replace the s11 by E[z_1^2], and similar for the other s? i
> mean thats what we do for moment slike
> E[eps1(B)^2eps2(B)^2]=E[eps1(B)^2][eps2(B)^2], we replace the right side with
> a one because at B_0 its a one.

## Why This Task Exists

The robust fourth-order conditions are written as cumulant-style equations, for
example

```text
g1222(B) = E[z1(B) z2(B)^3] - 3 S22(B) S12(B) = 0.
```

The current sample implementation naturally concentrates out `S22(B)` and
`S12(B)` by replacing them with sample second moments. That gives a smooth
function of several sample averages, not a simple sample average of one
fixed per-observation moment. The manuscript must determine whether the
existing robust DW J-statistic and chi-square cutoffs are theoretically valid,
or whether the robust statistic must be rebuilt as:

- a smooth minimum-distance/GMM criterion over a primitive moment vector, with
  variance computed by the delta method;
- an augmented GMM system with nuisance covariance parameters `S_{ij}` and
  moment equations such as `E[z_i z_j - S_ij]=0`;
- a bootstrap or simulation-calibrated inversion that avoids unsupported
  chi-square claims; or
- a narrower population-only diagnostic with no final GMM inference claim yet.

This task should also evaluate the user's proposed analogy to standard DW
unit-variance products. In the robust noisy setting, `S_{ii}(B0)=1+Omega_ii`
and `S_{ij}(B0)=Omega_ij` are generally unknown nuisance quantities, not fixed
normalization constants like `E[epsilon_i^2]=1` under a no-noise standardized
shock chart.

## Do Not Trust Without Rechecking

- Any current code or prose that treats
  `mean(z1*z2^3)-3*mean(z2^2)*mean(z1*z2)` as an ordinary one-line GMM moment
  without accounting for generated covariance plug-ins.
- Any chi-square degrees of freedom for the robust row that ignore the
  covariance-product estimation step.
- Any weight matrix computed from only the concentrated cumulant values rather
  than from the primitive moment vector or an equivalent augmented system.
- Any statement that `S_{11}`, `S_{22}`, or `S_{12}` can be replaced by known
  constants in the robust noisy setting without adding a new normalization or
  noise assumption.
- Any evidence table or figure caption that describes the robust row as a
  standard GMM J-test before this audit is complete.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/derivations/m54-stepwise-transformed-noise-moments.md` | Source of the transformed-noise moment expansion and `S`/`Omega` distinction. | derivation |
| `manuscript/tasks/M55-main-text-robust-moment-explanation.md` | Downstream writing task that depends on this audit. | routing decisions |
| `manuscript/derivations/dw-noise-robust-moments.md` | Original robust cumulant-to-moment construction and nuisance covariance discussion. | derivation |
| `manuscript/simulations/sign_dw_robust_noise_grid_figure.py` | Current Figure 1 robust statistic implementation. | code audit |
| `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py` | Figure 2 reuse of robust statistic implementation. | code audit |
| `manuscript/simulations/sign_dw_sample_size_robust_grid_figure.py` | Figure 3 reuse of robust statistic implementation. | code audit |
| `manuscript/simulations/m45_variance_ratio_evidence.py` | Monte Carlo and cutoff implementation for the active proposal. | code audit |
| `manuscript/draft.md` | Existing claims about moment equations, J-tests, and cutoffs. | draft edits |
| `manuscript/formal-object-registry.json` | Affected formal objects and evidence statuses. | registry edits |
| `KnowledgeVault/vault/papers/A Generalized Method of Moments Estimator for Structural Vector Autoregressions Based on Higher Moments.md` | Source context for higher-moment GMM treatment, if relevant. | source claims |
| `KnowledgeVault/svar-toolkit/docs/api/gmm.md` | Package GMM utility behavior and available weighting/inference support. | code changes |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The concentrated sample cumulant `mean(z1*z2^3)-3 mean(z2^2) mean(z1*z2)` is a smooth function of primitive sample moments, not a simple fixed per-observation sample mean. | `derived` | Wrote primitive vector and transformation explicitly in `manuscript/derivations/m56-robust-cumulant-gmm-generated-moment-audit.md`. | passed |
| Standard asymptotic inference can be recovered by applying GMM/minimum-distance theory to the primitive moment vector or by augmenting nuisance covariance moments. | `derived` plus source context | M56 derives the delta-method and augmented nuisance-covariance routes; KnowledgeVault and `svar-toolkit` GMM docs support the row-level moment discipline but not as a standalone proof for this generated statistic. | passed conditionally |
| The current robust DW simulation code uses a valid or invalid weighting/cutoff for the concentrated cumulant statistic. | `code-implemented` plus derivation | M56 shows the code uses analytic known-zero-mean delta influence rows, so it is better than the invalid naive statistic but still approximate/provisional because mean-centering terms, regularization, and finite-sample calibration remain unsettled. | approximate/provisional |
| In the robust noisy model, `S_{ij}(B0)` cannot generally be replaced by known constants without extra assumptions. | `derived` | M54 plus M56: `S(B0)=I+Omega(B0)`, so the entries are unknown nuisance covariances unless a new noise-covariance assumption fixes them. | passed |
| Any revised robust-row critical value or bootstrap calibration is valid for the reported procedure. | `derived` plus `code-implemented` | M56 recommends full primitive-moment delta weighting, augmented nuisance GMM, or bootstrap/repeated-sample calibration in M52; no new final critical value was implemented in this task. | deferred to M52 |

## Required Work

1. Derivation work:
   - write the primitive sample moment vector for each robust cumulant entry;
   - express each concentrated cumulant as a smooth map of primitive moments;
   - derive the Jacobian needed for the delta-method covariance of the
     concentrated moment stack;
   - derive the equivalent augmented nuisance-parameter GMM formulation and
     show when profiling `S_{ij}` matches the smooth-map criterion;
   - decide whether the population moment equations remain valid even if the
     naive finite-sample J-statistic must change.
2. Inference and degrees-of-freedom work:
   - determine the correct weighting matrix for the concentrated robust
     cumulant stack;
   - determine whether pointwise chi-square inversion can still be justified,
     and with which degrees of freedom, after nuisance covariance moments are
     estimated;
   - decide whether a bootstrap or simulation-calibrated cutoff is safer for
     the first paper.
3. Code audit:
   - inspect the Figure 1/Figure 2/Figure 3 and M45 code paths for robust
     moment computation, covariance estimation, weighting, and cutoffs;
   - identify whether the current outputs are population diagnostics,
     approximate finite-sample screens, or invalid J-test evidence;
   - if needed, create a follow-up implementation task or patch the code in
     this task only if the acceptance criteria can still be met cleanly.
4. Manuscript update work:
   - update M55's packet if the correct main-text explanation changes;
   - update draft claims, captions, table notes, registry, dashboard, paper
     map, source packet, workplan, task board, and logs;
   - mark any current evidence rows as historical or provisional if their
     inference was using an unsupported statistic.

## Stop Conditions

- Stop if the concentrated cumulant statistic cannot be mapped to either a
  smooth primitive-moment criterion or an augmented nuisance-parameter GMM
  system.
- Stop if valid inference requires assumptions not currently stated in the
  manuscript.
- Stop if the current evidence code and the intended theoretical statistic
  diverge enough that the Figure 1/Figure 2/Figure 3 story must be redesigned.
- Stop if source claims about GMM theory or DW practice cannot be verified from
  raw/vault sources or a self-contained derivation.

## Acceptance Criteria

- A derivation note states whether the robust fourth cumulants are valid
  moment restrictions, valid smooth functions of primitive moments, or invalid
  for standard GMM as currently used.
- The note states the correct implementation route: primitive-moment
  delta-method GMM, augmented nuisance-parameter GMM, bootstrap calibration, or
  population-only diagnostic.
- The current simulation/evidence code is classified as valid, approximate,
  or invalid for each reported robust row.
- M55 is updated or unblocked only after this audit tells it what explanation
  and computation recipe to use.
- Planning surfaces and the formal registry make any evidence or inference
  caveat visible.
- `python scripts/check_manuscript.py` passes after substantive edits.

## Expected Outputs

- New derivation/audit note, likely
  `manuscript/derivations/m56-robust-cumulant-gmm-generated-moment-audit.md`.
- Updated task-board routing so M56 runs before M55 and M52.
- Updated planning/log/registry surfaces reflecting the inference status.
- Optional code patch or follow-up implementation task if the existing robust
  statistic must be rebuilt.

## Outcome Log

Completed on 2026-06-10 in
`manuscript/derivations/m56-robust-cumulant-gmm-generated-moment-audit.md`.
Outcome: the population robust cumulant restrictions remain valid under the
maintained Gaussian residual-noise route, but the sample fourth-cumulant
entries are generated smooth moments. The current code already uses analytic
known-zero-mean delta influence rows, so it is approximate rather than the
invalid naive statistic. Final evidence should upgrade the robust row to a
full primitive-moment delta-method criterion including mean-centering nuisance
terms, an equivalent augmented nuisance-covariance GMM system, or bootstrap/
repeated-sample calibration. M55 is now unblocked for prose, and M52 must carry
the robust generated-moment implementation/calibration requirement into the
figure and Monte Carlo rebuild.
