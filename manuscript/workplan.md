# Workplan

## Current Stage

Initialized and scoped, with a corrected Bonhomme-Robin verification layer.
The manuscript has a validated KnowledgeVault link, source packet, revised
paper plan, paper map, first formal-object registry, first bibliography
snapshot, and an audited working bivariate cumulant map. BR-style claims still
need the applicability argument, profiled criteria, local rank derivation, and
simulation verification.

## Milestones

| Milestone | Status | Exit condition |
|---|---|---|
| M1. Initialize repository | done | Metadata, source links, package path, source packet, and first bibliography snapshot are initialized. |
| M2. Scope paper | done | One-sentence claim, paper contract, exclusions, and revised structure are stable enough for formal planning. |
| M3. Formal/evidence plan | doing | Core objects are listed and the bivariate cumulant map is audited; next exit requires the BR applicability argument, profiled criteria, local rank derivation, and a verified simulation plan. |
| M4. First complete draft | todo | All sections have coherent prose and source trails. |
| M5. Reproducibility package | todo | Final figures/tables can be regenerated. |
| M6. Shareable draft | todo | Citations, provenance, checks, and exports are clean. |

## Review Plan

1. Scope and contribution: verify that the paper is a short
   theory-and-simulation note, not a broad higher-moment SVAR survey.
2. Notation and assumptions: audit the diagonal-noise model, unit-variance
   normalization, independence assumptions, and sign-labeling conventions.
3. BR applicability review: check that the manuscript never presents the
   bivariate profiled inversion as a direct application of Bonhomme-Robin's
   full quasi-JADE theorem.
4. Theorem and derivation gaps: check the rescaling obstruction, generic
   independence-refinement failure, profiled cumulant rank condition, nuisance
   treatment, and noise diagnostic.
5. Derivation adversary: after each proposed result, deliberately search for
   undefined objects, hidden normalizations, invalid rank claims, logical
   leaps, and algebraic sign mistakes.
6. Evidence design: ensure the simulations include weak or inconclusive cases,
   not only favorable BR recoveries.
7. Simulation adversary: before accepting any figure, check whether the code,
   DGP, grids, critical values, or moment estimators could make the result look
   correct even if the theory is wrong.
8. Interpretation adversary: after every figure, ask whether the story is
   actually convincing, whether the conclusion is too strong, and whether a
   skeptical reader would see an alternative explanation.
9. Citation provenance: map every prior-work paragraph to a vault source and
   mark original contributions clearly.
10. Reproducibility package: make final figures rebuildable without a local
   KnowledgeVault dependency.
11. Literature positioning: keep Drautzburg-Wright framed as a valid
   no-noise test inversion and explain exactly where this paper differs.
12. Reader path: make sure the constructive fix arrives before the warning feels
   like a purely negative paper.

## Deferred Extensions

- Empirical illustration or diagnostic rereading of a published sign-restricted
  SVAR.
- `K > 2` general implementation of a verified BR-style profiled cumulant
  inversion.
- Dynamic sign restrictions and IRF-horizon sign sets in the main text.
- Correlated, serially dependent, or common-factor residual noise.
- Combining the robust inversion with external instruments or narrative
  restrictions.
