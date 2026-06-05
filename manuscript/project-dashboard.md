# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: initialized and scoped.

Current focus: verify the corrected Bonhomme-Robin-style profiled cumulant
inversion before drafting it as a result.

Next recommended action: derive the bivariate cumulant map and run the first
adversarial derivation review before accepting any BR-style rank or diagnostic
claim.

Active milestone: none. M0005 is closed, committed, tagged, and its GitHub
milestone is closed.

Active blockers:

- Proposition 2 needs a careful genericity statement and explicit special
  cases.
- Proposition 3 needs exact regularity conditions, critical-value choice, and
  proof target.
- The corrected KnowledgeVault notes show that the original Bonhomme-Robin
  theorem does not mechanically cover the bivariate `L=K=2` SVAR; the paper
  must derive and simulate its own profiled cumulant result.
- Evidence scripts must be wrapped under `manuscript/replication/` before the
  paper is shareable.
- The first draft should wait until formal statements and source trails are
  stable enough to prevent later rewrites.

Last substantive session: 2026-06-05, revised the Bonhomme-Robin plan after
corrected KnowledgeVault notes and added analytic, simulation, and adversarial
review gates.

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
