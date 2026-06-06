# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: figure-led evidence planning after the M0020-corrected noise
and non-Gaussianity grid pair, with the first M28 validation pass complete.

Current focus: formalize the robust-DW comparison diagnostic in the same
language as the M0020/M28 grid story, then move to calibrated M29
finite-sample evidence.

Next recommended action: start M27. Define the reported standard-DW set,
robust-DW set, overlap/divergence metric, critical-value convention, and
interpretation boundaries using the M0020 figures and M28 diagnostics.

Active milestone: none. M0021 records the user decision that the M0020 grid
pair tells the paper's main story and should organize the next plan.

Active blockers:

- The robust DW derivation passed M24 only as a local normalized
  Gaussian-noise result, and M28 supports its population truth-inclusion
  behavior. It still needs M27 formal statement discipline and M29 calibrated
  finite-sample evidence before becoming final manuscript evidence.
- The M25 standard-DW J-test inversion result is only a working derivation; M28
  supports the high-noise divergence story, but the derivation still needs a
  direct audit before theorem-level prose.
- The M30 audit found that the original M35 moderate-noise scenario was near a
  structural-coordinate rescaling exception. The patched screen now includes
  an anisotropic diagonal-noise stress case, but the provisional
  scale-normalized finite-sample statistic is still too permissive for final
  evidence.
- The intuitive sign/DW/robust-DW evidence now has a selected M0020 visual
  spine, and M28 supports the story on exact population moments, grid-boundary
  checks, repeated seeds, and pointwise critical-value sensitivity. The figures
  are strong enough to organize the paper, but not final enough to skip M29
  calibrated critical values and coverage-style summaries.
- The robust-DW simulation code must be wrapped under `manuscript/replication/`
  before the paper is shareable.
- A figure-led section draft should wait until M27 formalizes the diagnostic
  language and M29 calibrates finite-sample evidence enough to avoid another
  structural rewrite.

Last substantive session: 2026-06-06, completed the first M28 validation pass
for the M0020 grid pair and promoted M27 as the next task.

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
