# Literature Search

Purpose: durable search log for source discovery, citation gaps, and BibTeX
verification.

## Search Questions

| ID | Status | Question | Search terms or sources | Result |
|---|---|---|---|---|
| LS01 | done | What vault note contains the originating research idea? | User supplied `vault/syntheses/Research proposal - noise-robust sign-restricted SVARs.md`. | Proposal located and used as source packet priority 1. |
| LS02 | done | Which sources define standard sign-restricted SVAR geometry and reporting risks? | `Sign and narrative restrictions in SVARs`; Kilian-Lutkepohl Chapter 13; ARRW sign-zero inference. | Use for background and to avoid treating accepted shares, medians, or penalty selections as structural learning. |
| LS03 | done | What is the closest no-noise higher-moment refinement comparator? | Drautzburg-Wright note and related higher-moment cluster. | Use as the fair target: valid test inversion under its maintained no-noise null. |
| LS04 | done | Which sources provide noisy covariance/sign-set geometry? | Noisy-residual synthesis and proposal note. | Use for pseudo-set algebra, sign-boundary movement, and the intuitive first figure. |
| LS05 | done | Which sources provide higher-moment caution and finite-sample warnings? | Lewis review; Montiel Olea-Plagborg-Moller-Qian; Guay; Keweloh. | Use to frame weak moments, bootstrap/stress-case evidence, and GMM implementation choices. |
| LS07 | done | How should the first draft position the contribution relative to sign restrictions, Drautzburg-Wright, and higher-moment SVAR GMM? | Existing verified source packet and citation-provenance entries. | M32 drafted a compact introduction subsection: sign-set inference supplies the set-reporting baseline, Drautzburg-Wright supplies the no-noise comparator, and higher-moment SVAR/GMM sources supply moment-stack and weak-moment cautions. |
| LS06 | todo | Does the final paper need an empirical illustration? | Search sign-restricted applications with small data and existing vault notes. | Deferred; no application in the first version. |
| LS08 | todo | What primary source should support the standard-DW asymptotic-empty proof if Darmois-Skitovich is used? | Darmois-Skitovich theorem; higher-moment independence sources. | Needed only if Proposition 2 uses that theorem directly. |

## Candidate Sources

| Source | Why inspect it? | Status | Citation key |
|---|---|---|---|
| Research proposal - noise-robust sign-restricted SVARs | Originating plan and claims. | inspected | n/a |
| Noisy residuals in recursive and sign-restricted SVARs | Algebra for pseudo covariance target, sign geometry, and independence-refinement failure modes. | inspected | n/a |
| Refining set-identification in VARs through independence | Main no-noise comparator. | inspected | `drautzburg2023RefiningSetIdentificationVars` |
| Structural VAR Analysis Chapter 13 | Sign-restriction method and reporting cautions. | inspected | `kilian2016StructuralVectorAutoregressiveAnalysis93b03b` |
| ARRW sign-zero inference | Set-inference and penalty-function warning. | inspected | `arias2018InferenceBasedStructuralVector` |
| Guay higher unconditional moments | Rank diagnostics and higher-moment source. | inspected | `guay2020IdentificationStructuralVectorAutoregressions` |
| Keweloh higher-moment SVAR-GMM | GMM comparator and moment-stack warning. | inspected | `paper2020GeneralizedMethodMomentsEstimator` |
| Montiel Olea-Plagborg-Moller-Qian higher-moment caution | Assumption and weak-identification warning. | inspected | `olea2022SvarIdentificationHigherMoments` |
| Lewis higher-moment review | Literature taxonomy and positioning. | inspected | `lewis2025IdentificationBasedHigherMoments` |

## Citation Gaps

- Need exact primary citation for the Darmois-Skitovich theorem if the standard
  DW misspecification result uses it directly.
- Need decide whether to cite the Keweloh-Wang mean-independence extension in
  the main text or leave it as a deferred contrast.
- Need verify if a final empirical illustration adds application-specific
  sources and data provenance; first version currently excludes applications.
- Need source support or original derivation for the exact finite-sample DW
  moment stack used in the simulations.

## BibTeX Verification

| Citation key | Source checked | Status | Notes |
|---|---|---|---|
| `drautzburg2023RefiningSetIdentificationVars` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
| `kilian2016StructuralVectorAutoregressiveAnalysis93b03b` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
| `arias2018InferenceBasedStructuralVector` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
| `guay2020IdentificationStructuralVectorAutoregressions` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
| `paper2020GeneralizedMethodMomentsEstimator` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`; key is inherited from vault. |
| `olea2022SvarIdentificationHigherMoments` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
| `lewis2025IdentificationBasedHigherMoments` | Vault BibTeX and paper note | verified | Copied to `bibliography/references.bib`. |
