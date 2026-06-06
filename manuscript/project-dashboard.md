# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: formal result package after M24 robust-DW derivation audit.

Current focus: run an early simultaneous-SVAR Monte Carlo triage for the
standard-DW versus robust-DW J-test comparison before investing in polished
figures or a larger replication suite.

Next recommended action: start M35 by implementing a small overview Monte
Carlo for the M25 J-test inversion result and the audited robust-DW comparison.
Use it as a go/no-go check before final figure design.

Active milestone: none. M0013 records the simultaneous-SVAR scope update and
M25 standard-DW J-test derivation.

Active blockers:

- The robust DW derivation passed M24 only as a local normalized
  Gaussian-noise result; it still needs population-grid and Monte Carlo checks
  before becoming final manuscript evidence.
- The M25 standard-DW J-test inversion result is only a working derivation; it
  needs audit and early finite-sample MC triage.
- The first simulation should be a lightweight Monte Carlo overview, not a
  polished evidence package, so the project can be stopped or redirected early
  if the J-test comparison performs poorly.
- The intuitive sign-noise figure is not yet specified.
- The robust-DW simulation code must be wrapped under `manuscript/replication/`
  before the paper is shareable.
- The first draft should wait until the new formal statements and evidence plan
  are stable enough to prevent another structural rewrite.

Last substantive session: 2026-06-06, narrowed the paper to a simultaneous
SVAR impact-only scope, added an early Monte Carlo triage gate, and derived the
M25 standard-DW J-test inversion result with generic emptying plus
structural-rescaling and finite-moment-alias exceptions.

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
- Keep the model simultaneous and impact-only; do not introduce VAR lags or
  dynamic impulse-response machinery in the first paper.
- Keep each substantive work block traceable through `transparency/`, Git
  commits, and milestone tags.
- Keep KnowledgeVault links explicit in working notes, not hidden in prose.
- One paper should carry one central idea.
- The first version is theory/simulation only; no application for now.
- Treat the robust DW route as a candidate theorem until audit and simulations
  support it.
- Every non-original claim needs a source trail or citation.
- Every original contribution should be marked as such in prose or provenance.
- Final figures, tables, and replication outputs should be reproducible from
  `replication/`.
