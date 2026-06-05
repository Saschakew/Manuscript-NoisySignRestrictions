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
| `draft.md#1-introduction` | This paper's original contribution is to study residual-noise contamination of the sign-restricted covariance target and propose a BR-style robust alternative. | our-contribution | `vault/syntheses/Research proposal - noise-robust sign-restricted SVARs.md`; `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md`; `vault/syntheses/Bonhomme-Robin noise-robust SVAR moment inversion.md` | n/a |
| `draft.md#2-noisy-sign-sets` | The standard sign set rotates a factor of `Sigma_u`; with diagonal noise this becomes a pseudo-set based on `B0 B0' + V`. | our-contribution | `vault/syntheses/Noisy residuals in recursive and sign-restricted SVARs.md`; proposal note | n/a |
| `draft.md#3-no-noise-independence-refinement` | Drautzburg-Wright use no-noise higher-moment independence tests as a weak-identification-robust refinement of sign-restricted sets. | source-backed | `vault/papers/Refining set-identification in VARs through independence.md` | `drautzburg2023RefiningSetIdentificationVars` |
| `draft.md#3-no-noise-independence-refinement` | Higher-moment SVAR identification rests on substantive and testable shock-process assumptions; weak higher moments are a central finite-sample risk. | source-backed | `vault/overview/Non-Gaussian and higher-moment SVAR identification.md`; `vault/papers/SVAR Identification from Higher Moments - Has the Simultaneous Causality Problem Been Solved.md`; `vault/papers/Identification Based on Higher Moments in Macroeconometrics.md` | `olea2022SvarIdentificationHigherMoments`; `lewis2025IdentificationBasedHigherMoments` |
| `draft.md#4-robust-sign-inversion` | Clean mixed cumulants under idiosyncratic noise follow the Bonhomme-Robin noisy ICA logic. | source-backed | `vault/papers/Consistent noisy independent component analysis.md`; `vault/syntheses/Bonhomme-Robin noise-robust SVAR moment inversion.md` | `bonhomme2009ConsistentNoisyIndependentComponent` |
| `draft.md#4-robust-sign-inversion` | Moment-based SVAR identification and GMM provide the higher-moment comparator but are not automatically noise robust. | source-backed | `vault/papers/Identification of structural vector autoregressions through higher unconditional moments.md`; `vault/papers/A Generalized Method of Moments Estimator for Structural Vector Autoregressions Based on Higher Moments.md` | `guay2020IdentificationStructuralVectorAutoregressions`; `paper2020GeneralizedMethodMomentsEstimator` |
| `draft.md#5-noise-diagnostic-and-evidence` | The mapped diagonal-noise diagnostic is original and conditional on the robust moment model and unit-variance normalization. | our-contribution | proposal note; `vault/syntheses/Bonhomme-Robin noise-robust SVAR moment inversion.md` | n/a |

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
| `vault/papers/Consistent noisy independent component analysis.md` | `bonhomme2009ConsistentNoisyIndependentComponent` | `vault/citations/bibtex/bonhomme-2009-consistent-noisy-independent-component-analysis-6833beff.bib` | verified | Positive noisy-ICA ancestor. |
| `vault/papers/Refining set-identification in VARs through independence.md` | `drautzburg2023RefiningSetIdentificationVars` | `vault/citations/bibtex/drautzburg-2023-refining-set-identification-vars-through-independence-2f06cfb0.bib` | verified | Closest no-noise sign-plus-independence comparator. |
| `vault/papers/Structural Vector Autoregressive Analysis - Chapter 13 - Identification by Sign Restrictions.md` | `kilian2016StructuralVectorAutoregressiveAnalysis93b03b` | `vault/citations/bibtex/kilian-2016-structural-vector-autoregressive-analysis-chapter-identification-sign-restrictions-93b03bf7.bib` | verified | Sign-restriction geometry and reporting warnings. |
| `vault/papers/Inference Based on Structural Vector Autoregressions Identified With Sign and Zero Restrictions - Theory and Applications.md` | `arias2018InferenceBasedStructuralVector` | `vault/citations/bibtex/arias-2018-inference-based-structural-vector-autoregressions-identified-sign-zero-6ba3d417.bib` | verified | Set-inference caution and penalty-function critique. |
| `vault/papers/Identification of structural vector autoregressions through higher unconditional moments.md` | `guay2020IdentificationStructuralVectorAutoregressions` | `vault/citations/bibtex/guay-2020-identification-structural-vector-autoregressions-through-higher-unconditional-moments-620d4a1c.bib` | verified | Higher-moment rank diagnostics. |
| `vault/papers/A Generalized Method of Moments Estimator for Structural Vector Autoregressions Based on Higher Moments.md` | `paper2020GeneralizedMethodMomentsEstimator` | `vault/citations/bibtex/paper-2020-generalized-method-moments-estimator-structural-vector-autoregressions-based-55c13e37.bib` | verified | Higher-moment GMM comparator. |
| `vault/papers/SVAR Identification from Higher Moments - Has the Simultaneous Causality Problem Been Solved.md` | `olea2022SvarIdentificationHigherMoments` | `vault/citations/bibtex/olea-2022-svar-identification-higher-moments-simultaneous-causality-problem-been-21666567.bib` | verified | Cautionary higher-moment assumption source. |
| `vault/papers/Identification Based on Higher Moments in Macroeconometrics.md` | `lewis2025IdentificationBasedHigherMoments` | `vault/citations/bibtex/lewis-2025-identification-based-higher-moments-macroeconometrics-77da8cb2.bib` | verified | Review-level taxonomy. |
| `vault/papers/Uncertain Short-Run Restrictions and Statistically Identified Structural Vector Autoregressions.md` | `keweloh2025UncertainShortRunRestrictions` | `vault/citations/bibtex/keweloh-2025-uncertain-short-run-restrictions-statistically-identified-structural-vector-351c1d2e.bib` | verified | Candidate extension source; not yet required in draft prose. |
