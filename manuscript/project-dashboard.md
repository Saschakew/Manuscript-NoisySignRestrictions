# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: early evidence gate after the M35 Monte Carlo triage and the
M0019-corrected noise and non-Gaussianity grid pair.

Current focus: run population-grid verification before promoting the
M0019-corrected candidate grid figures or investing in a larger replication
suite.

Next recommended action: start M28 population-grid checks for
structural-rescaling exceptions, generic anisotropic-noise pseudo-zeros,
robust-DW truth inclusion, finite-stack aliases, and weak-moment widening.

Active milestone: none. M0019 records the correction that both grid figures'
robust-DW rows use only higher cumulants and no second moments.

Active blockers:

- The robust DW derivation passed M24 only as a local normalized
  Gaussian-noise result; it still needs population-grid checks before becoming
  final manuscript evidence.
- The M25 standard-DW J-test inversion result is only a working derivation; it
  still needs audit and population-grid triage.
- The M30 audit found that the original M35 moderate-noise scenario was near a
  structural-coordinate rescaling exception. The patched screen now includes
  an anisotropic diagonal-noise stress case, but the provisional
  scale-normalized finite-sample statistic is still too permissive for final
  evidence.
- The intuitive sign/DW/robust-DW evidence now has an M0019-corrected candidate
  grid pair. The sign and standard-DW rows use N-test cutoffs; the robust-DW
  rows are pure population higher-cumulant sets. They are not final evidence
  until M28/M29 check critical values, weak moments, and standard-DW pseudo-set
  behavior.
- The robust-DW simulation code must be wrapped under `manuscript/replication/`
  before the paper is shareable.
- The first draft should wait until the new formal statements and evidence plan
  are stable enough to prevent another structural rewrite.

Last substantive session: 2026-06-06, corrected both grid figures so the
robust-DW rows remove second moments; the noise grid now uses a pure
higher-cumulant robust row and the non-Gaussianity grid expands to the whole
admissible graph under Gaussian shocks.

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
