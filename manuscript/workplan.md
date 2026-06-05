# Workplan

## Current Stage

Initialized and scoped. The manuscript has a validated KnowledgeVault link,
source packet, revised paper plan, paper map, first formal-object registry, and
first bibliography snapshot.

## Milestones

| Milestone | Status | Exit condition |
|---|---|---|
| M1. Initialize repository | done | Metadata, source links, package path, source packet, and first bibliography snapshot are initialized. |
| M2. Scope paper | done | One-sentence claim, paper contract, exclusions, and revised structure are stable enough for formal planning. |
| M3. Formal/evidence plan | doing | Core objects are listed; next exit requires exact formal statements and proof obligations for Propositions 1-4. |
| M4. First complete draft | todo | All sections have coherent prose and source trails. |
| M5. Reproducibility package | todo | Final figures/tables can be regenerated. |
| M6. Shareable draft | todo | Citations, provenance, checks, and exports are clean. |

## Review Plan

1. Scope and contribution: verify that the paper is a short
   theory-and-simulation note, not a broad higher-moment SVAR survey.
2. Notation and assumptions: audit the diagonal-noise model, unit-variance
   normalization, independence assumptions, and sign-labeling conventions.
3. Theorem and derivation gaps: check the rescaling obstruction, generic
   independence-refinement failure, BR rank condition, and noise diagnostic.
4. Evidence design: ensure the simulations include weak or inconclusive cases,
   not only favorable BR recoveries.
5. Citation provenance: map every prior-work paragraph to a vault source and
   mark original contributions clearly.
6. Reproducibility package: make final figures rebuildable without a local
   KnowledgeVault dependency.
7. Literature positioning: keep Drautzburg-Wright framed as a valid
   no-noise test inversion and explain exactly where this paper differs.
8. Reader path: make sure the constructive fix arrives before the warning feels
   like a purely negative paper.

## Deferred Extensions

- Empirical illustration or diagnostic rereading of a published sign-restricted
  SVAR.
- `K > 2` general implementation of the BR-style clean-moment inversion.
- Dynamic sign restrictions and IRF-horizon sign sets in the main text.
- Correlated, serially dependent, or common-factor residual noise.
- Combining the robust inversion with external instruments or narrative
  restrictions.
