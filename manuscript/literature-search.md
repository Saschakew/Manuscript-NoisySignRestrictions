# Literature Search

Purpose: durable search log for source discovery, citation gaps, and BibTeX
verification.

## Search Questions

| ID | Status | Question | Search terms or sources | Result |
|---|---|---|---|---|
| LS01 | done | What vault note contains the originating research idea? | User supplied `vault/syntheses/Research proposal - noise-robust sign-restricted SVARs.md`. | Proposal located and used as source packet priority 1. |
| LS02 | done | Which sources define standard sign-restricted SVAR geometry and reporting risks? | `Sign and narrative restrictions in SVARs`; Kilian-Lutkepohl Chapter 13; ARRW sign-zero inference. | Use for background and to avoid treating accepted shares, medians, or penalty selections as structural learning. |
| LS03 | done | What is the closest no-noise independence-refinement comparator? | Drautzburg-Wright note and related higher-moment cluster. | Use as the fair target: valid test inversion under its maintained no-noise null. |
| LS04 | done | Which source provides the noise-robust cumulant logic? | Bonhomme-Robin noisy ICA; BR SVAR synthesis; noisy-residual synthesis. | Use for the constructive method section. |
| LS05 | done | Which sources provide higher-moment caution and finite-sample warnings? | Lewis review; Montiel Olea-Plagborg-Moller-Qian; Guay; Keweloh. | Use to frame weak moment relevance and bootstrap/stress-case evidence. |
| LS06 | todo | Does the final paper need an empirical illustration? | Search sign-restricted applications with small data and existing vault notes. | Deferred until formal results and simulations are stable. |

## Candidate Sources

| Source | Why inspect it? | Status | Citation key |
|---|---|---|---|
| Research proposal - noise-robust sign-restricted SVARs | Originating plan and claims. | inspected | n/a |
| Noisy residuals in recursive and sign-restricted SVARs | Algebra for pseudo covariance target and sign geometry. | inspected | n/a |
| Bonhomme-Robin noise-robust SVAR moment inversion | Clean moment set and diagnostic source. | inspected | n/a |
| Consistent noisy independent component analysis | Noisy-ICA ancestor. | inspected | `bonhomme2009ConsistentNoisyIndependentComponent` |
| Refining set-identification in VARs through independence | Main no-noise comparator. | inspected | `drautzburg2023RefiningSetIdentificationVars` |
| Structural VAR Analysis Chapter 13 | Sign-restriction method and reporting cautions. | inspected | `kilian2016StructuralVectorAutoregressiveAnalysis93b03b` |
| ARRW sign-zero inference | Set-inference and penalty-function warning. | inspected | `arias2018InferenceBasedStructuralVector` |
| Guay higher unconditional moments | Rank diagnostics and higher-moment source. | inspected | `guay2020IdentificationStructuralVectorAutoregressions` |
| Keweloh higher-moment SVAR-GMM | GMM comparator and moment-stack warning. | inspected | `paper2020GeneralizedMethodMomentsEstimator` |
| Montiel Olea-Plagborg-Moller-Qian higher-moment caution | Assumption and weak-identification warning. | inspected | `olea2022SvarIdentificationHigherMoments` |
| Lewis higher-moment review | Literature taxonomy and positioning. | inspected | `lewis2025IdentificationBasedHigherMoments` |

## Citation Gaps

- Need exact primary citation for the Darmois-Skitovich theorem if Proposition
  2 uses it directly rather than through the vault's higher-moment notes.
- Need decide whether to cite the Keweloh-Wang mean-independence extension in
  the main text or leave it as a literature-search footnote/deferred contrast.
- Need verify if a final empirical illustration adds application-specific
  sources and data provenance.

## BibTeX Verification

| Citation key | Source checked | Status | Notes |
|---|---|---|---|
| `bonhomme2009ConsistentNoisyIndependentComponent` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
| `drautzburg2023RefiningSetIdentificationVars` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
| `kilian2016StructuralVectorAutoregressiveAnalysis93b03b` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
| `arias2018InferenceBasedStructuralVector` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
| `guay2020IdentificationStructuralVectorAutoregressions` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
| `paper2020GeneralizedMethodMomentsEstimator` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`; key is inherited from vault. |
| `olea2022SvarIdentificationHigherMoments` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
| `lewis2025IdentificationBasedHigherMoments` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
