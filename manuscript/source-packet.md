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
  bootstrap utilities where possible; keep manuscript-specific simulations as
  thin wrappers.

Use this package as the default computational foundation for SVAR estimation,
identification, inference, simulations, and replication code. Record any
missing routine as package follow-up before implementing local manuscript code.

## Manuscript Question

How should applied sign-restricted SVAR researchers diagnose whether
Drautzburg-Wright-style higher-moment refinement is sharpening a valid
structural set or merely sharpening a misspecified noisy-covariance target?

Scope note: the first paper studies the simultaneous SVAR impact problem only.
It treats the reduced-form residual `u_t` as the object to be decomposed and
does not model VAR lags, dynamic impulse responses, or horizon-specific sign
restrictions.

## Orientation Searches

| Query or entry point | Vault area | Result | Follow-up |
|---|---|---|---|
| User proposal note | `vault/syntheses/` | Located the original proposal on noise-robust sign-restricted SVARs. | Use only the noisy sign-set warning, DW misspecification channel, and simulation motivation for the active paper. |
| `noise`, `sign`, `SVAR` | `vault/syntheses/` | Located `Noisy residuals in recursive and sign-restricted SVARs.md`. | Use for covariance pseudo-set algebra, sign-boundary movement, and intuitive figures. |
| sign restrictions and independence refinement | `vault/overview/`, `vault/papers/` | Located sign-restriction overview, Kilian-Lutkepohl Chapter 13, ARRW sign-zero inference, and Drautzburg-Wright independence refinement. | Keep DW framed as valid under its maintained no-noise null; the paper studies residual-noise robustness. |
| higher moments and GMM | `vault/papers/`, `vault/overview/` | Located higher-moment SVAR identification, GMM, and cautionary weak-moment sources. | Use for the robust higher-moment stack, moment-selection warnings, and simulation stress cases. |
| existing evidence assets | `replications/` | Located `svar-noise-recursive-sign-visualization/` with sign-noise and independence-refinement visuals. | Rebuild or wrap only the figures that support the new DW-versus-robust-DW paper. |

## Core Source Set

Keep this list small enough to fit in active manuscript context. Prefer the
notes that directly shape the new paper.

| Priority | Vault path | Role in manuscript | Citation key | Status |
|---:|---|---|---|---|
| 1 | `vault/syntheses/Research proposal - noise-robust sign-restricted SVARs.md` | Originating idea record: noisy sign pseudo-set, DW false-precision risk, and simulation motivation. | n/a | source-backed |
| 2 | `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md` | Algebraic and visual source for noisy covariance factors, sign-set geometry, column-rescaling obstruction, and independence-test failure modes. | n/a | source-backed |
| 3 | `vault/papers/Refining set-identification in VARs through independence.md` | Main comparator: sign restrictions refined through no-noise higher-moment independence tests. | `drautzburg2023RefiningSetIdentificationVars` | source-backed |
| 4 | `vault/overview/Sign and narrative restrictions in SVARs.md` | Method overview for admissible rotations, accepted-set interpretation, and set reporting. | n/a | source-backed |
| 5 | `vault/papers/Structural Vector Autoregressive Analysis - Chapter 13 - Identification by Sign Restrictions.md` | Book-level sign-restriction geometry and reporting warnings. | `kilian2016StructuralVectorAutoregressiveAnalysis93b03b` | source-backed |
| 6 | `vault/papers/Inference Based on Structural Vector Autoregressions Identified With Sign and Zero Restrictions - Theory and Applications.md` | Inferential warning that single optimized rotations can understate set uncertainty. | `arias2018InferenceBasedStructuralVector` | source-backed |
| 7 | `vault/overview/Non-Gaussian and higher-moment SVAR identification.md` | Higher-moment method map and weak-identification cautions. | n/a | source-backed |
| 8 | `vault/papers/Identification of structural vector autoregressions through higher unconditional moments.md` | Reduced-form higher-moment rank logic and finite-sample warning. | `guay2020IdentificationStructuralVectorAutoregressions` | source-backed |
| 9 | `vault/papers/A Generalized Method of Moments Estimator for Structural Vector Autoregressions Based on Higher Moments.md` | GMM moment-stack comparator and computational caution. | `paper2020GeneralizedMethodMomentsEstimator` | source-backed |
| 10 | `vault/papers/SVAR Identification from Higher Moments - Has the Simultaneous Causality Problem Been Solved.md` | Cautionary source: higher moments buy identification with substantive, testable assumptions. | `olea2022SvarIdentificationHigherMoments` | source-backed |
| 11 | `vault/papers/Identification Based on Higher Moments in Macroeconometrics.md` | Review-level taxonomy for weak higher moments and shock labeling. | `lewis2025IdentificationBasedHigherMoments` | source-backed |

Statuses: `candidate`, `source-backed`, `needs-verification`, `dropped`.

## Relevant Replications Or Code

| Vault path | What it validates or illustrates | Manuscript action |
|---|---|---|
| `replications/svar-noise-recursive-sign-visualization/` | Deterministic sign-noise geometry and no-noise independence-refinement behavior under residual noise. | Use as the starting point for the intuitive figure and standard-DW false-sharpening figure. |
| `manuscript/simulations/sign_dw_robust_noise_grid_figure.py` | Manuscript-local M0017 corrected B-plane grid: sign/covariance row, standard-DW row, and robust-DW row across three noise levels, using finite-sample N-test cutoffs. | Preferred candidate visual for the user's requested sign/DW/robust-DW noise comparison; still needs M28/M29 critical-value and weak-moment checks before final evidence. |
| `manuscript/simulations/sign_dw_robust_noise_figure.py` | Manuscript-local M0016 population candidate that reproduces the KnowledgeVault sign/standard-DW noise visualization and adds the robust-DW normalized higher-cumulant set. | Keep as exploratory figure support; M28 must still verify population grids before final evidence or polished paper use. |
| `svar-toolkit/examples/howto/06_sign_restrictions.py` | Verified fixed-draw sign-restriction accepted-set workflow. | Use for baseline sign-set simulations if needed. |
| `svar-toolkit/examples/howto/12_non_gaussian_cross_moments.py` | Verified fixed-draw higher-moment cross-moment selector. | Use as a comparator or helper for robust higher-moment diagnostics, not as a final estimator without audit. |
| `svar-toolkit/docs/api/gmm.md` and GMM examples | Reusable moment quadratic engine. | Candidate for the robust DW moment criterion and Monte Carlo wrappers. |

## Relevant `svar-python` APIs

| API or module | Package path | Manuscript use | Status |
|---|---|---|---|
| `draw_orthogonal_rotations`, `rotate_impact`, `filter_sign_restrictions`, `draw_sign_restricted_models` | `svar-toolkit/src/svar_toolkit/restrictions.py` | Baseline sign-restricted candidate generation and filtering. | validated |
| `structural_irfs`, structural-output helpers | `svar-toolkit/src/svar_toolkit/` | Propagate accepted impacts into simple responses if needed for figures. | validated |
| `non_gaussian_cross_moments`, `select_non_gaussian_cross_moment_rotation` | `svar-toolkit/src/svar_toolkit/non_gaussian.py` | Comparator diagnostics for no-noise higher-moment rotation selection. | validated |
| GMM utilities | `svar-toolkit/src/svar_toolkit/gmm.py` | Candidate engine for robust DW moment criteria and bootstrap wrappers. | candidate |
| plotting helpers | `svar-toolkit/src/svar_toolkit/plotting.py` | Figure layer for accepted sets and diagnostics. | validated |

## Active Verification Plan

Before polished prose claims that the robust DW comparison works, complete
these tasks:

1. Derive and audit the noisy sign-set pseudo-object and column-rescaling
   obstruction.
2. Build the intuitive geometry figure showing covariance deformation and
   sign-set bias. M0016 created a candidate sign/standard-DW/robust-DW
   population figure from the KnowledgeVault visualization, but the full
   geometry figure and M28 validation remain open.
3. Use the M25 standard-DW J-test inversion derivation: rich stacks empty
   generically under residual noise, while structural-coordinate rescaling
   cases and finite-moment aliases can produce pseudo-zeros.
4. Use the M24 audit of
   `manuscript/derivations/dw-noise-robust-moments.md`: the local normalized
   Gaussian-noise route conditionally passed, but global aliases, scale loss,
   and finite-sample behavior still require population-grid and Monte Carlo
   checks.
5. Decide and state the maintained robust noise condition. Gaussian residual
   noise gives clean transformed higher cumulants; broader noise requires a
   different argument.
6. Completed M35 lightweight Monte Carlo overview before investing in polished
   figures or a large replication suite, then completed M30 audit. The audit
   found that the original moderate-noise case was near a
   structural-coordinate rescaling exception, added an anisotropic
   diagonal-noise stress case, and confirmed that the provisional
   finite-sample statistic is too permissive for final evidence.
7. Implement population-grid checks showing: standard DW false candidates or
   emptying under noise; robust DW zero at truth under its maintained noise
   model; weak-moment widening.
8. Run finite-sample Monte Carlo with repeated-sample or bootstrap critical
   values.
9. Report coverage, set width, empty-set frequency, overlap frequency, and
   divergence diagnostics.
10. Only after analytic and simulation checks pass, promote the robust DW
   comparison from a planned robustness check to a manuscript result.

## Gaps And Risks

- The standard DW J-test emptying statement is now a working derivation with
  explicit exceptions; M30 showed that the next evidence step must separate
  structural-rescaling exceptions from genuinely generic noisy covariance
  cases on population grids.
- The robust DW route must be explicit about its noise assumption. Gaussian
  additive residual noise is clean for transformed cumulants; non-Gaussian
  transformed noise generally is not.
- Higher moments can be weak in macro samples; the robust set may be wide or
  uninformative, and that is an honest result.
- The robust set comparison is a diagnostic, not proof of literal measurement
  error.
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
