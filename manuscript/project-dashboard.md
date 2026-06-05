# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: initialized and scoped.

Current focus: turn the revised paper plan into exact formal statements,
proof obligations, and a manuscript-local evidence wrapper.

Next recommended action: write the precise assumptions and statements for
Propositions 1-4, starting with the generic no-noise independence-refinement
failure and the BR+sign consistency target.

Active milestone: M0003 initialize noise-robust sign SVAR manuscript.

Active blockers:

- Proposition 2 needs a careful genericity statement and explicit special
  cases.
- Proposition 3 needs exact regularity conditions, critical-value choice, and
  proof target.
- Evidence scripts must be wrapped under `manuscript/replication/` before the
  paper is shareable.
- The first draft should wait until formal statements and source trails are
  stable enough to prevent later rewrites.

Last substantive session: 2026-06-05, initialized the manuscript, validated
KnowledgeVault, built the source packet, and revised the paper plan.

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
- Every non-original claim needs a source trail or citation.
- Every original contribution should be marked as such in prose or provenance.
- Final figures, tables, and replication outputs should be reproducible from
  `replication/`.
