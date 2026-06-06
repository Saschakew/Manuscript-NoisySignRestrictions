# Citation Provenance

Purpose: map manuscript claims to sources and distinguish prior work from this
project's original contribution.

## Citation Snapshot

- BibTeX file: `../bibliography/references.bib`
- KnowledgeVault link: `../knowledge-vault-link.json`
- Source packet: `source-packet.md`
- Last synced: 2026-06-05

## Section Source Map

| Draft location | Claim or paragraph role | Status | Source trail | Citation key |
|---|---|---|---|---|
| `draft.md#1-introduction` | Sign restrictions are set filters over covariance-equivalent rotations and require careful set reporting. | source-backed | `vault/overview/Sign and narrative restrictions in SVARs.md`; `vault/papers/Structural Vector Autoregressive Analysis - Chapter 13 - Identification by Sign Restrictions.md`; `vault/papers/Inference Based on Structural Vector Autoregressions Identified With Sign and Zero Restrictions - Theory and Applications.md` | `kilian2016StructuralVectorAutoregressiveAnalysis93b03b`; `arias2018InferenceBasedStructuralVector` |
| `draft.md#1-introduction` | This paper's original contribution is to study residual-noise contamination of sign-restricted covariance targets and propose a standard-DW versus robust-DW comparison as a robustness check. | our-contribution | `vault/syntheses/Research proposal - noise-robust sign-restricted SVARs.md`; `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md`; manuscript derivation notes | n/a |
| `draft.md#2-noisy-sign-sets` | The standard sign set rotates a factor of `Sigma_u`; with additive residual noise this becomes a pseudo-set based on `B0 B0' + V`. | our-contribution | `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md`; proposal note | n/a |
| `draft.md#3-standard-dw-under-residual-noise` | Drautzburg-Wright use no-noise higher-moment independence tests as a weak-identification-robust refinement of sign-restricted sets. | source-backed | `vault/papers/Refining set-identification in VARs through independence.md` | `drautzburg2023RefiningSetIdentificationVars` |
| `draft.md#3-standard-dw-under-residual-noise` | Under residual noise, recovered-shock independence is a misspecified no-noise target; finite samples can select least-rejected pseudo-candidates. | our-contribution | `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md`; manuscript proof task M25 | n/a |
| `draft.md#4-robust-dw-higher-moment-set` | Higher-moment SVAR identification rests on substantive and testable shock-process assumptions; weak higher moments are a central finite-sample risk. | source-backed | `vault/overview/Non-Gaussian and higher-moment SVAR identification.md`; `vault/papers/SVAR Identification from Higher Moments - Has the Simultaneous Causality Problem Been Solved.md`; `vault/papers/Identification Based on Higher Moments in Macroeconometrics.md` | `olea2022SvarIdentificationHigherMoments`; `lewis2025IdentificationBasedHigherMoments` |
| `draft.md#4-robust-dw-higher-moment-set` | The robust DW set drops second-moment restrictions and uses higher cumulants of `B^{-1}u` written as GMM-style moment equations under the maintained robust-noise condition. | our-contribution | `manuscript/derivations/dw-noise-robust-moments.md`; higher-moment GMM source | `paper2020GeneralizedMethodMomentsEstimator` |
| `draft.md#5-monte-carlo-robustness-check` | Comparing standard DW and robust DW sets is an original diagnostic: standard-DW accepted mass outside robust-DW is a warning that usual DW precision may be noise-driven, while robust-DW width records lost second-moment information. | our-contribution | `manuscript/derivations/dw-robust-comparison-diagnostic.md`; manuscript simulation design and derivation tasks | n/a |
| `draft.md#51-residual-noise-grid` | The residual-noise grid is the main visual warning: increasing Gaussian residual noise moves the sign/covariance set, can make standard DW reject true `B0`, and leaves robust DW wider and truth-compatible under the maintained Gaussian-noise route. | our-contribution | `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`; `manuscript/simulations/m28_grid_story_validation.md`; `manuscript/simulations/m29_calibrated_monte_carlo.md` | n/a |
| `draft.md#52-non-gaussianity-grid` | The non-Gaussianity grid states the limitation that robust DW becomes wide or uninformative when structural higher moments weaken or vanish. | our-contribution | `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`; `manuscript/simulations/m28_grid_story_validation.md`; higher-moment caution sources | `olea2022SvarIdentificationHigherMoments`; `lewis2025IdentificationBasedHigherMoments` |
| `draft.md#53-monte-carlo-table` | The larger M29 chi-square-primary Monte Carlo table is draft-level quantitative support, while repeated-sample, oracle, and bootstrap cutoff rows are calibration-cost audits rather than application-ready procedures. | our-contribution | `manuscript/simulations/m29_calibrated_monte_carlo.md`; `manuscript/simulations/output/m29_calibrated_monte_carlo.json`; user decision U0026 | n/a |

Statuses:

- `source-backed`: derived from named papers, vault notes, raw sources, or
  official documentation.
- `our-contribution`: new framing, derivation, statistic, simulation, or
  application choice from this manuscript project.
- `needs-source`: must not remain in shareable prose without a citation.

## KnowledgeVault Citation Records

When citing an absorbed vault paper, record:

| Paper note path | Citation key | BibTeX path | Citation status | Notes |
|---|---|---|---|---|
| `vault/papers/Refining set-identification in VARs through independence.md` | `drautzburg2023RefiningSetIdentificationVars` | `vault/citations/bibtex/drautzburg-2023-refining-set-identification-vars-through-independence-2f06cfb0.bib` | verified | Main no-noise sign-plus-independence comparator. |
| `vault/papers/Structural Vector Autoregressive Analysis - Chapter 13 - Identification by Sign Restrictions.md` | `kilian2016StructuralVectorAutoregressiveAnalysis93b03b` | `vault/citations/bibtex/kilian-2016-structural-vector-autoregressive-analysis-chapter-identification-sign-restrictions-93b03bf7.bib` | verified | Sign-restriction geometry and reporting warnings. |
| `vault/papers/Inference Based on Structural Vector Autoregressions Identified With Sign and Zero Restrictions - Theory and Applications.md` | `arias2018InferenceBasedStructuralVector` | `vault/citations/bibtex/arias-2018-inference-based-structural-vector-autoregressions-identified-sign-zero-6ba3d417.bib` | verified | Set-inference caution and penalty-function critique. |
| `vault/papers/Identification of structural vector autoregressions through higher unconditional moments.md` | `guay2020IdentificationStructuralVectorAutoregressions` | `vault/citations/bibtex/guay-2020-identification-structural-vector-autoregressions-through-higher-unconditional-moments-620d4a1c.bib` | verified | Higher-moment rank diagnostics. |
| `vault/papers/A Generalized Method of Moments Estimator for Structural Vector Autoregressions Based on Higher Moments.md` | `paper2020GeneralizedMethodMomentsEstimator` | `vault/citations/bibtex/paper-2020-generalized-method-moments-estimator-structural-vector-autoregressions-based-55c13e37.bib` | verified | Higher-moment GMM comparator. |
| `vault/papers/SVAR Identification from Higher Moments - Has the Simultaneous Causality Problem Been Solved.md` | `olea2022SvarIdentificationHigherMoments` | `vault/citations/bibtex/olea-2022-svar-identification-higher-moments-simultaneous-causality-problem-been-21666567.bib` | verified | Cautionary higher-moment assumption source. |
| `vault/papers/Identification Based on Higher Moments in Macroeconometrics.md` | `lewis2025IdentificationBasedHigherMoments` | `vault/citations/bibtex/lewis-2025-identification-based-higher-moments-macroeconometrics-77da8cb2.bib` | verified | Review-level taxonomy. |
| `vault/papers/Uncertain Short-Run Restrictions and Statistically Identified Structural Vector Autoregressions.md` | `keweloh2025UncertainShortRunRestrictions` | `vault/citations/bibtex/keweloh-2025-uncertain-short-run-restrictions-statistically-identified-structural-vector-351c1d2e.bib` | verified | Candidate extension source; not required in the first draft. |
