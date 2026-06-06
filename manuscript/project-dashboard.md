# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: initialized, scoped, and comparing constructive routes.

Current focus: adversarially audit the new Gaussian-noise DW-like
higher-moment route and compare it with the broader BR-style
observed-residual route before changing the paper structure.

Next recommended action: start M23 by attacking
`manuscript/derivations/dw-noise-robust-moments.md`, especially the
cumulant-to-moment algebra, the claim that second moments are only nuisance
ingredients, the scale normalization, and the local-rank argument. Then run M08
on the BR applicability argument so the manuscript can choose the right
constructive route.

Active milestone: none. M0010 is closed, committed, tagged, pushed, and its
GitHub milestone is closed.

Active blockers:

- Proposition 2 needs a careful genericity statement and explicit special
  cases.
- Proposition 3 needs exact regularity conditions, critical-value choice, and
  proof target.
- The corrected KnowledgeVault notes show that the original Bonhomme-Robin
  theorem does not mechanically cover the bivariate `L=K=2` SVAR; the
  applicability note documents this boundary, but it still needs adversarial
  attack before M09 builds criteria on it.
- The Gaussian-noise DW-like route is only a working derivation. It must be
  audited before the paper treats it as a cleaner replacement for the BR-style
  observed-residual route.
- Evidence scripts must be wrapped under `manuscript/replication/` before the
  paper is shareable.
- The first draft should wait until formal statements and source trails are
  stable enough to prevent later rewrites.

Last substantive session: 2026-06-06, derived a Gaussian-noise
Drautzburg-Wright-like higher-cumulant route that avoids no-noise covariance
restrictions, writes fourth cumulants as moment equations with nuisance
covariance products, and records local bivariate rank conditions.

Last maintenance session: 2026-06-05, cleared the stale M21 task state after
verifying the M0005 transparency snapshot and GitHub milestone closure.

## Orientation Map

- `paper-plan.md`: scope, contribution, structure, missing pieces, and page
  budget.
- `source-packet.md`: curated KnowledgeVault context for this manuscript.
- `paper-map.md`: compact macro argument and reader path.
- `manuscript-rules.md`: numbering, labels, object boundaries, hidden comments,
  citations, and export discipline.
- `formal-object-registry.json`: assumptions, propositions, equations, figures,
  tables, proofs, and dependencies.
- `workplan.md`: milestones and review plan.
- `task-board.md`: open tasks and next actions.
- `citation-provenance.md`: section-level source map and contribution boundary.
- `literature-search.md`: search questions, citation gaps, and BibTeX
  verification tasks.
- `transparency/`: structured milestone data for the transparency website.
- `draft.md`: manuscript prose source of truth.
- `derivations/`: proof trails and algebra.
- `simulations/`: exploratory simulation designs.
- `replication/README.md`: final shareable reproducibility package plan.
- `decision-log.md`: durable decisions.
- `user-input-log.md`: user-originated ideas, constraints, and decisions.
- `session-log.md`: chronological work history.
- `codex-log.md`: shareable Codex transparency log.
- `review-log.md`: review passes.

## Do Not Forget

- Keep this manuscript repository self-contained for sharing.
- Keep each substantive work block traceable through `transparency/`, Git
  commits, and milestone tags.
- Keep KnowledgeVault links explicit in working notes, not hidden in prose.
- One paper should carry one central idea.
- Keep the first version bivariate and theory/simulation focused; empirical
  illustration is optional after the core is stable.
- Treat BR-style inversion claims as unverified until analytic derivations,
  simulations, and adversarial reviews support them.
- Every non-original claim needs a source trail or citation.
- Every original contribution should be marked as such in prose or provenance.
- Final figures, tables, and replication outputs should be reproducible from
  `replication/`.
