# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: active paper pivoted to the robust DW comparison design.

Current focus: cleanly develop the paper as a noisy sign-set warning plus a
Drautzburg-Wright versus robust-DW robustness check.

Next recommended action: start M24 by adversarially auditing
`manuscript/derivations/dw-noise-robust-moments.md`. Check the
cumulant-to-moment algebra, second-moment exclusion, normalization and scale
loss, local rank, exact Gaussian-noise condition, and finite-sample bias
wording. Then run M25 to prove or weaken the standard-DW asymptotic-empty
claim under residual-noise misspecification.

Active milestone: none. M0011 is closed, committed, tagged, pushed, and its
GitHub milestone is closed.

Active blockers:

- The robust DW derivation is a working note and needs adversarial audit before
  becoming a manuscript theorem.
- The claim that standard DW sets become asymptotically empty under residual
  noise needs proof or careful weakening.
- The intuitive sign-noise figure and Monte Carlo design are not yet specified.
- The robust-DW simulation code must be wrapped under `manuscript/replication/`
  before the paper is shareable.
- The first draft should wait until the new formal statements and evidence plan
  are stable enough to prevent another structural rewrite.

Last substantive session: 2026-06-06, pivoted the active paper plan to the
robust DW comparison design: biased noisy sign sets, standard DW
false-sharpening under residual noise, robust DW higher moments that drop
second moments, and Monte Carlo overlap/divergence evidence.

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
- The first version is theory/simulation only; no application for now.
- Treat the robust DW route as a candidate theorem until audit and simulations
  support it.
- Every non-original claim needs a source trail or citation.
- Every original contribution should be marked as such in prose or provenance.
- Final figures, tables, and replication outputs should be reproducible from
  `replication/`.
