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

M0034 scale correction: the M0030/M37 diagonal-anchor robust-DW object is
superseded. Under the active diagonal-normalized chart, the covariance anchor
`Sigma_u,12=b12+b21` also assumes unit structural-shock variances. The pure
mixed higher-cumulant robust-DW set remains the validity fallback, but M0036
now supplies the active variance-ratio scale model.

M0035 candidate scale model: a bounded recovered-covariance screen can use
`E[e1 e2]=(-b21*nu_1-b12*nu_2)/(1-b12*b21)^2` with
`0 <= nu_i <= 0.5`. This is valid only as an explicit noise-bound assumption,
not as a free normalization.

M0036 scale-corrected proposal: replace the absolute bound with the relative
restriction `0 <= nu_i <= 0.5 * Var(epsilon_i)` while profiling structural
shock variances in the diagonal-normalized chart. This variance-ratio robust
DW screen is the active proposal for the manuscript. The remaining work is to
write the formulas cleanly, update the companion figures and Monte Carlo
evidence, and audit the finite-sample implementation.

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
| `manuscript/simulations/sign_dw_relative_noise_robust_grid_figure.md` | M0036 variance-ratio robust DW Figure 1 proposal: uses pure mixed higher-cumulant J inversion plus a covariance-decomposition feasibility screen with `0 <= nu_i <= 0.5 * Var(epsilon_i)`. | Active proposal visual: high-noise variance-ratio robust DW contains true `B0` and accepts 0.071 of the full plotted grid. Future work should update Figure 2, add Figure 3, and audit finite-sample behavior while presenting the signal-to-noise bound as substantive identifying information. |
| `manuscript/simulations/sign_dw_bounded_noise_robust_grid_figure.md` | M0035 bounded-noise Figure 1 comparison: uses pure mixed higher-cumulant J inversion plus a profiled recovered-covariance feasibility screen with `0 <= nu_i <= 0.5`. | Historical comparison: high-noise bounded robust DW contains true `B0` and accepts 0.066 of the full plotted grid, but the absolute variance cap is scale-arbitrary relative to the M0036 signal-to-noise screen. |
| `manuscript/simulations/sign_dw_pure_robust_noise_grid_figure.md` | M0034 scale-correction diagnostic for Figure 1: the bottom row uses only five mixed higher-cumulant moments and drops the invalid off-diagonal covariance anchor. | Current visual diagnostic: high-noise pure robust DW contains true `B0` but accepts 0.459 of the full plotted grid, showing the precision cost of validity. |
| `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py` | Manuscript-local M0030 revised companion grid: fixes residual noise and varies structural-shock non-Gaussianity. Its diagonal-anchor robust row is superseded after M0034 and must be revised in M43. | Use only as a reminder of the weak-higher-moment limitation until the robust row is rebuilt with the variance-ratio proposal. |
| `manuscript/simulations/sign_dw_robust_noise_grid_figure.py` | Manuscript-local B-plane grid generator. M0034 added `--robust-mode pure`; M0035 added `--robust-mode bounded`; M0036 added `--robust-mode relative`. The old default diagonal-anchor output is superseded for the robust row. | Use relative mode for the proposal Figure 1 and pure/bounded modes as fallback comparisons; rebuild Figure 2/Figure 3 and audit finite-sample behavior next. |
| `manuscript/simulations/sign_dw_robust_noise_figure.py` | Manuscript-local M0016 population candidate that reproduces the KnowledgeVault sign/standard-DW noise visualization and adds the robust-DW normalized higher-cumulant set. | Keep as exploratory figure support; refreshed M28 population-grid validation now favors the M0030 grid pair as the main visual spine. |
| `manuscript/simulations/m28_grid_story_validation.py` | Refreshed M28 validation pass for the superseded M0030 grid pair. | Historical for the robust row after M0034/M0035/M0036; rerun for the variance-ratio proposal after Figure 2/Figure 3 are rebuilt and M40 audit is complete. |
| `manuscript/simulations/m29_calibrated_monte_carlo.py` | Refreshed M29 finite-sample pass for the superseded M0030 robust statistic. | Historical for the robust row after M0034/M0035/M0036; reuse its reporting metrics when rebuilding the variance-ratio Monte Carlo. |
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
   geometry figure remains optional because the M0030/M28 grid pair now carries
   the main visual story.
3. Use the M25 standard-DW J-test inversion derivation: rich stacks empty
   generically under residual noise, while structural-coordinate rescaling
   cases and finite-moment aliases can produce pseudo-zeros.
4. Use the M24 audit of
   `manuscript/derivations/dw-noise-robust-moments.md`: the local normalized
   Gaussian-noise route conditionally passed, but global aliases, scale loss,
   and finite-sample behavior still require M27 formalization and M29
   calibrated Monte Carlo checks.
5. Decide and state the maintained robust noise condition. Gaussian residual
   noise gives clean transformed higher cumulants; broader noise requires a
   different argument.
6. Completed M35 lightweight Monte Carlo overview before investing in polished
   figures or a large replication suite, then completed M30 audit. The audit
   found that the original moderate-noise case was near a
   structural-coordinate rescaling exception, added an anisotropic
   diagonal-noise stress case, and confirmed that the provisional
   finite-sample statistic is too permissive for final evidence.
7. Completed and refreshed the M28 validation pass for the M0030 figure pair:
   population moments, repeated seeds, grid-boundary sensitivity, true-`B0` J
   diagnostics, and pointwise critical-value sensitivity support the selected
    visual spine under the maintained diagonal Gaussian residual-noise condition.
8. Completed M27 comparison-diagnostic formalization in the same language as
   the figures: reported standard-DW set, robust-DW set, critical-value
   convention, accepted shares, Jaccard overlap, directional
   standard-outside-robust warning metric, truth-inclusion simulation
   diagnostics, and interpretation boundaries.
9. Completed the expanded M29 finite-sample Monte Carlo pass and user decision
   U0026: standard pointwise chi-square critical values are the primary applied
   benchmark because they are what a standard-DW researcher would use under the
   no-noise null.
10. Completed the refreshed M29 chi-square-primary run with 120 calibration
    replications, 60 evaluation replications, 20 truth-bootstrap replications
    per evaluation sample, and a 41-by-41 grid. Under the primary cutoffs,
    high-noise standard DW includes true `B0` in 0.050 of evaluation samples,
    while robust DW includes it in 0.900. Weak and Gaussian structural-shock
    cases widen robust DW toward the covariance anchor, with mean robust
    accepted shares of 0.172 and 0.158.
11. The robust DW comparison is ready for a figure-led draft as a
    robustness-check result, with audit cutoffs described as calibration-cost
    diagnostics rather than application-ready procedures.
12. M0034 supersedes the M37 pass judgment for the six-moment
    diagonal-anchor robust DW object. The pure higher-cumulant component
    remains valid under Gaussian residual noise, but the off-diagonal
    covariance anchor double-normalizes scale in the `diag(B)=1` chart unless
    unit shock variances are also imposed. M0036 supplies the active
    variance-ratio scale model; M41-M45 should now draft formulas, clean math
    formatting, update Figure 2, add Figure 3, and rebuild evidence.

## Gaps And Risks

- The standard DW J-test emptying statement is now a working derivation with
  explicit exceptions; M28 supports the selected high-noise grid story, but
  M25 still needs a direct proof audit before theorem-level prose.
- The robust DW route is now conditionally audited for diagonal Gaussian
  residual noise. Correlated Gaussian noise requires dropping the
  off-diagonal covariance anchor and using the pure higher-cumulant fallback;
  non-Gaussian transformed residual noise generally invalidates the
  higher-cumulant interpretation unless extra residual-noise cumulant
  restrictions are modeled.
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
