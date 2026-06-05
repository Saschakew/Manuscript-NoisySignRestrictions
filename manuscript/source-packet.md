# Source Packet

Purpose: curated KnowledgeVault context for this manuscript. Build this before
drafting prose, then keep it compact and source-backed.

## Vault Connection

- KnowledgeVault link: `../knowledge-vault-link.json`
- Local path: `C:\Users\smsakewe\Documents\GitHub\KnowledgeVault`
- Repository: `https://github.com/Saschakew/KnowledgeVault.git`
- Commit: `83a30daf4794aef2eb85ae99fe52574114dba063`
- Validated on: 2026-06-05
- Status: validated

Required surfaces to validate:

- `vault/_index.md`
- `vault/_paper_registry.json`
- `vault/_replication_registry.json`
- `vault/papers/`
- `vault/syntheses/`
- `vault/citations/references.bib`
- `replications/`

## Computational Package

- Package: `svar-python`
- Import name: `svar_toolkit`
- Resolved KnowledgeVault path: `svar-toolkit/`
- Version, wheel, or commit: `knowledge-vault-svar-toolkit 0.1.0.dev0` at
  KnowledgeVault commit `83a30daf4794aef2eb85ae99fe52574114dba063`
- Validation status: validated from `pyproject.toml` and vault orientation
- Manuscript use: reuse existing sign-restriction draws, structural-output
  helpers, non-Gaussian cross-moment diagnostics, GMM primitives, plotting, and
  bootstrap utilities where possible; keep manuscript-specific robust
  Bonhomme-Robin inversion as a thin wrapper until it justifies promotion.

Use this package as the default computational foundation for SVAR estimation,
identification, inference, simulations, and replication code. Record any missing
routine as package follow-up before implementing local manuscript code.

## Manuscript Question

How should sign-restricted SVAR inference be interpreted when reduced-form
residuals contain diagonal idiosyncratic noise, and can a carefully verified
Bonhomme-Robin-style profiled cumulant inversion combine economic sign labels
with higher-moment information without pretending the noisy covariance is
structural?

## Orientation Searches

| Query or entry point | Vault area | Result | Follow-up |
|---|---|---|---|
| User proposal note | `vault/syntheses/` | Located `Research proposal - noise-robust sign-restricted SVARs.md`; contains four proposed results and simulation design. | Treat as originating research idea and revise into a short theory-and-simulation paper plan. |
| `noise`, `sign`, `SVAR` | `vault/syntheses/` | Located the two closest supporting syntheses: `Noisy residuals in recursive and sign-restricted SVARs.md` and `Bonhomme-Robin noise-robust SVAR moment inversion.md`. | Use them as the source trail for the failure geometry and the constructive inversion. |
| sign restrictions and independence refinement | `vault/overview/`, `vault/papers/` | Located sign-restriction overview, Kilian-Lutkepohl Chapter 13, ARRW sign-zero inference, and Drautzburg-Wright independence refinement. | Keep the critique fair: target the no-noise population null and finite-sample interpretation, not test inversion itself. |
| higher moments, noisy ICA, GMM | `vault/papers/`, `vault/overview/` | Located Bonhomme-Robin noisy ICA, Guay higher unconditional moments, Keweloh SVAR-GMM, Lewis review, and Montiel Olea-Plagborg-Moller-Qian caution. | Use them to state moment relevance, weak-identification risk, and diagnostic burden. |
| existing evidence assets | `replications/` | Located `svar-noise-recursive-sign-visualization/` and `bonhomme-robin-noise-robust-svar/` with figures and tests. | Promote or wrap these assets under `manuscript/replication/` before final sharing. |
| corrected Bonhomme-Robin reading | `vault/syntheses/`, `vault/papers/` | Reread updated `Bonhomme-Robin noise-robust SVAR moment inversion.md` and `Consistent noisy independent component analysis.md` after user correction. The corrected reading says BR first identifies/subtracts error cumulants from clean-pair restrictions; the bivariate `L=K=2` SVAR is not directly covered by the BR quasi-JADE theorem. | Revise the plan to require our own analytic derivation and simulation verification before claiming the BR-style result. |

## Core Source Set

Keep this list small enough to fit in active manuscript context. Prefer the
5-20 notes that will actually shape the paper.

| Priority | Vault path | Role in manuscript | Citation key | Status |
|---:|---|---|---|---|
| 1 | `vault/syntheses/Research proposal - noise-robust sign-restricted SVARs.md` | Originating paper design: pseudo-set warning, independence-refinement misspecification, robust inversion, noise diagnostic, simulation plan. | n/a | source-backed |
| 2 | `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md` | Algebraic source for noisy covariance factors, sign-set geometry, column-rescaling obstruction, and independence-test failure modes. | n/a | source-backed |
| 3 | `vault/syntheses/Bonhomme-Robin noise-robust SVAR moment inversion.md` | Corrected constructive source: the bivariate object is a BR-style profiled cumulant inversion, not a direct application of the full BR quasi-JADE theorem. Pure moments are nuisance/diagnostic unless extra noise restrictions are imposed. | n/a | source-backed |
| 4 | `vault/papers/Consistent noisy independent component analysis.md` | Positive ancestor and caution: BR identify error cumulants using clean measurement pairs, subtract them, then identify loadings from denoised cumulants; the `L=K=2` SVAR needs extra derivation. | `bonhomme2009ConsistentNoisyIndependentComponent` | source-backed |
| 5 | `vault/papers/Refining set-identification in VARs through independence.md` | Closest target/comparator: sign restrictions plus inverted independence tests under no-noise recovered shocks. | `drautzburg2023RefiningSetIdentificationVars` | source-backed |
| 6 | `vault/overview/Sign and narrative restrictions in SVARs.md` | Method overview for admissible rotations, set reporting, accepted-set interpretation, and code entry points. | n/a | source-backed |
| 7 | `vault/papers/Structural Vector Autoregressive Analysis - Chapter 13 - Identification by Sign Restrictions.md` | Book-level sign-restriction geometry and warnings about acceptance rates, pointwise summaries, penalties, and priors. | `kilian2016StructuralVectorAutoregressiveAnalysis93b03b` | source-backed |
| 8 | `vault/papers/Inference Based on Structural Vector Autoregressions Identified With Sign and Zero Restrictions - Theory and Applications.md` | Inferential warning that single optimized rotations can understate set uncertainty. | `arias2018InferenceBasedStructuralVector` | source-backed |
| 9 | `vault/overview/Non-Gaussian and higher-moment SVAR identification.md` | Higher-moment method map and warnings about independence, weak shape, and economic labeling. | n/a | source-backed |
| 10 | `vault/papers/Identification of structural vector autoregressions through higher unconditional moments.md` | Reduced-form coskewness/cokurtosis rank logic and finite-sample bootstrap warning. | `guay2020IdentificationStructuralVectorAutoregressions` | source-backed |
| 11 | `vault/papers/A Generalized Method of Moments Estimator for Structural Vector Autoregressions Based on Higher Moments.md` | GMM moment-stack comparator and computational/moment-selection caution. | `paper2020GeneralizedMethodMomentsEstimator` | source-backed |
| 12 | `vault/papers/SVAR Identification from Higher Moments - Has the Simultaneous Causality Problem Been Solved.md` | Cautionary source: higher moments buy identification by adding substantive, testable shock-process assumptions. | `olea2022SvarIdentificationHigherMoments` | source-backed |
| 13 | `vault/papers/Identification Based on Higher Moments in Macroeconometrics.md` | Literature-review anchor for weak identification, shock labeling, and combining statistical and economic information. | `lewis2025IdentificationBasedHigherMoments` | source-backed |
| 14 | `vault/papers/Uncertain Short-Run Restrictions and Statistically Identified Structural Vector Autoregressions.md` | Useful extension boundary: mean-independence and higher moments can test/soften economic restrictions, but this paper should not absorb that estimator. | `keweloh2025UncertainShortRunRestrictions` | candidate |

Statuses: `candidate`, `source-backed`, `needs-verification`, `dropped`.

## Relevant Syntheses

| Vault synthesis path | Why it matters | Manuscript use |
|---|---|---|
| `vault/syntheses/Research proposal - noise-robust sign-restricted SVARs.md` | Already contains the proposed paper's claims, formal model, simulation design, and limits. | Treat as the manuscript's initial idea record and revise it into a tighter paper contract. |
| `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md` | Shows why the usual covariance factor is a noisy pseudo-structural object. | Use for Sections 2 and 3, especially rescaling obstruction and independence-test failure. |
| `vault/syntheses/Bonhomme-Robin noise-robust SVAR moment inversion.md` | Gives the corrected profiled cumulant interpretation, the bivariate cumulant equations, and the warning that the original BR theorem does not apply mechanically when `L=K=2`. | Use for Sections 4 and 5 only after deriving the bivariate results ourselves. |
| `vault/syntheses/Non-Gaussian and higher-moment identification of SVARs.md` | Places the paper in the non-Gaussian/higher-moment shelf. | Use for concise background and limitations. |
| `vault/syntheses/Proxy-SVAR shock recovery under noisy residuals.md` | Analogy for residual noise creating pseudo-targets in another identification design. | Mention only if introduction needs a neighboring motivation; otherwise defer. |

## Relevant Replications Or Code

| Vault path | What it validates or illustrates | Manuscript action |
|---|---|---|
| `replications/svar-noise-recursive-sign-visualization/` | Deterministic geometry for recursive noise, sign boundary movement, no-noise independence refinement, and B-plane moment tests. | Reuse for failure-mode figures after deciding which panels belong in main text versus appendix. |
| `replications/bonhomme-robin-noise-robust-svar/` | Existing bivariate robust inversion and implied diagonal-noise map under no, Gaussian, and skewed noise. | Treat as a starting diagnostic, not proof. Rebuild after analytic derivation and add adversarial DGPs, population checks, and finite-sample Monte Carlo. |
| `svar-toolkit/examples/howto/06_sign_restrictions.py` | Verified fixed-draw sign-restriction accepted-set workflow. | Use for standard sign-set simulations if needed; do not treat acceptance rates as tests. |
| `svar-toolkit/examples/howto/12_non_gaussian_cross_moments.py` | Verified fixed-draw higher-moment cross-moment selector. | Use only for diagnostics or comparator figures; not a full ICA estimator. |
| `svar-toolkit/docs/api/gmm.md` and GMM examples | Reusable moment quadratic engine. | Candidate for implementing the BR criterion as a thin manuscript-specific moment stack. |

## Relevant `svar-python` APIs

| API or module | Package path | Manuscript use | Status |
|---|---|---|---|
| `draw_orthogonal_rotations`, `rotate_impact`, `filter_sign_restrictions`, `draw_sign_restricted_models` | `svar-toolkit/src/svar_toolkit/restrictions.py` | Baseline sign-restricted candidate generation and filtering. | validated |
| `structural_irfs`, structural-output helpers | `svar-toolkit/src/svar_toolkit/` | Propagate candidate impacts into IRFs if dynamic signs enter. | validated |
| `non_gaussian_cross_moments`, `select_non_gaussian_cross_moment_rotation` | `svar-toolkit/src/svar_toolkit/non_gaussian.py` | Comparator diagnostics for no-noise higher-moment rotation selection. | validated |
| GMM utilities | `svar-toolkit/src/svar_toolkit/gmm.py` | Candidate engine for pointwise BR moment criterion and bootstrap wrappers. | candidate |
| plotting helpers | `svar-toolkit/src/svar_toolkit/plotting.py` | Figure layer for accepted sets, IRFs, and diagnostics if reused. | validated |

## Bonhomme-Robin Verification Plan

This paper must not rely on the earlier, too-simple summary of Bonhomme-Robin.
Before any prose claims that the robust inversion works, complete these tasks:

1. Derive the bivariate cumulant map from scratch for
   `u_t = B(a,b) epsilon_t + eta_t`, including second cumulants, all distinct
   third cumulants, all distinct fourth cumulants, and nuisance noise cumulants
   `(nu_i, tau_i, rho_i)`.
2. Separate population restrictions from nuisance fitting:
   `sigma_12`, `T_112`, `T_122`, `K_1112`, `K_1122`, and `K_1222` are clean
   under diagonal independent noise; pure own moments estimate or test
   nuisance noise cumulants unless extra restrictions are imposed.
3. Prove that the original BR clean-pair quasi-JADE theorem is not the theorem
   used in the bivariate manuscript case, because independent errors provide
   only one clean pair when `L=K=2`.
4. Derive the minimal fourth-cumulant profiled criterion `J_4(a,b)`, the
   determinant condition, the local tangent, and the rank condition
   `a0 kappa_2 != b0 kappa_1`, checking the `(1-a0 b0)` nonsingularity factor.
5. Derive the stacked profiled criterion with unrestricted diagonal noise
   cumulants and specify exactly which extra restrictions would turn pure
   moments into overidentifying tests: no noise, Gaussian noise, zero skewness,
   zero fourth cumulant, nonnegative variances, or sign restrictions on noise
   moments.
6. Derive the mapped variance diagnostic and the restricted no-noise J test as
   separate diagnostics. Do not conflate "origin outside mapped variance set"
   with "literal measurement error proven."
7. Build verification code with three layers: symbolic/algebraic moment checks,
   population-grid checks using analytic cumulants, and finite-sample Monte
   Carlo with bootstrap or repeated-sample critical values.
8. Run adversarial simulations: weak/zero fourth cumulants, near rank failure,
   high noise, negative implied variances, Gaussian structural shocks, skewed
   and Gaussian noise, mis-normalized shocks, and non-diagonal noise to verify
   the method fails honestly.
9. Only after the derivation and simulations pass, promote `prop:robust-sign-
   inversion` and `prop:consistent-noise-diagnostic` from planned claims to
   draftable manuscript results.

## Citation Snapshot Plan

| Citation key | Vault BibTeX path | Verification status | Copy to bibliography? |
|---|---|---|---|
| `bonhomme2009ConsistentNoisyIndependentComponent` | `vault/citations/bibtex/bonhomme-2009-consistent-noisy-independent-component-analysis-6833beff.bib` | verified | yes |
| `drautzburg2023RefiningSetIdentificationVars` | `vault/citations/bibtex/drautzburg-2023-refining-set-identification-vars-through-independence-2f06cfb0.bib` | verified | yes |
| `kilian2016StructuralVectorAutoregressiveAnalysis93b03b` | `vault/citations/bibtex/kilian-2016-structural-vector-autoregressive-analysis-chapter-identification-sign-restrictions-93b03bf7.bib` | verified | yes |
| `arias2018InferenceBasedStructuralVector` | `vault/citations/bibtex/arias-2018-inference-based-structural-vector-autoregressions-identified-sign-zero-6ba3d417.bib` | verified | yes |
| `guay2020IdentificationStructuralVectorAutoregressions` | `vault/citations/bibtex/guay-2020-identification-structural-vector-autoregressions-through-higher-unconditional-moments-620d4a1c.bib` | verified | yes |
| `paper2020GeneralizedMethodMomentsEstimator` | `vault/citations/bibtex/paper-2020-generalized-method-moments-estimator-structural-vector-autoregressions-based-55c13e37.bib` | verified | yes |
| `olea2022SvarIdentificationHigherMoments` | `vault/citations/bibtex/olea-2022-svar-identification-higher-moments-simultaneous-causality-problem-been-21666567.bib` | verified | yes |
| `lewis2025IdentificationBasedHigherMoments` | `vault/citations/bibtex/lewis-2025-identification-based-higher-moments-macroeconometrics-77da8cb2.bib` | verified | yes |
| `keweloh2025UncertainShortRunRestrictions` | `vault/citations/bibtex/keweloh-2025-uncertain-short-run-restrictions-statistically-identified-structural-vector-351c1d2e.bib` | verified | maybe; include if the first literature review keeps mean-independence as a live contrast |

## Gaps And Risks

- The generic-empty independence-refinement proposition needs a clean statement
  of the allowed special cases: Gaussian noise, absorbable one-equation noise,
  noise-dominated rotations, and special loading alignments.
- The robust BR inversion depends on a unit-variance or diagonal normalization;
  the paper must not present the noise diagnostic without this scale discipline.
- The BR-style inversion is currently unverified by us. It is a planned
  contribution, not yet a manuscript result.
- Pure own moments are not clean identifying moments for `B(a,b)` under
  unrestricted diagonal noise. They are nuisance/diagnostic moments unless the
  paper imposes extra restrictions on the noise cumulants.
- Mixed fourth cumulants are statistically noisy. The evidence plan must include
  weak-cumulant and macro-sample stress cases where the robust set is wide or
  inconclusive.
- The main text should stay bivariate unless the K-variable generalization is
  needed for publication positioning. The appendix can record the extension
  target without blocking the first draft.
- The first shareable replication cannot depend on the local KnowledgeVault
  checkout; wrap or copy the necessary scripts under `manuscript/replication/`
  and pin an installable package dependency before release.

## Transfer Rules

- Use this packet to decide what Codex should read before drafting.
- Record section-level claims in `citation-provenance.md`.
- Copy only needed verified BibTeX entries into `../bibliography/references.bib`.
- Prefer `svar-python` APIs over manuscript-local implementations for SVAR
  computation.
- Do not make shareable prose depend on readers having KnowledgeVault access.
