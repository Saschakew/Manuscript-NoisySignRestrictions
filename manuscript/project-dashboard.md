# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: figure-led evidence validation after the M0020-corrected noise
and non-Gaussianity grid pair, with M28 first validation, M27 diagnostic
formalization, and an M29 calibrated Monte Carlo first pass complete.

Current focus: expand M29 from the first repeated-sample calibration pass into
a final finite-sample evidence package around the M0020/M28/M27 story.

Next recommended action: audit and expand M29. The first pass uses 80
calibration replications, 24 evaluation replications, a 41-by-41 B-plane grid,
and three pointwise cutoff conventions. A final table still needs a larger
run or bootstrap-calibrated critical values before coverage claims become
draft-level evidence.

Active milestone: none. M0021 records the user decision that the M0020 grid
pair tells the paper's main story and should organize the next plan.

Active blockers:

- The robust DW derivation passed M24 only as a local normalized
  Gaussian-noise result. M27 has formalized the reported set and diagnostic
  language, M28 supports its population truth-inclusion behavior, and M29 now
  has a first calibrated finite-sample pass. Final evidence still needs a
  larger or bootstrap-calibrated run.
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
  checks, repeated seeds, and pointwise critical-value sensitivity. M29's first
  pass supports the high-noise divergence story and quantifies a large
  standard-DW cutoff inflation, but the figures are still not final evidence
  until the M29 calibration is expanded.
- The robust-DW simulation code must be wrapped under `manuscript/replication/`
  before the paper is shareable.
- A figure-led section draft should wait until M29 calibrates finite-sample
  evidence enough to avoid another structural rewrite, though the first-pass
  reading is now strong enough to outline the evidence subsection.

Last substantive session: 2026-06-06, completed a first M29 calibrated Monte
Carlo pass. The run reports chi-square, no-noise repeated, and
scenario-specific oracle truth cutoffs; the high-noise standard-DW cutoff
inflates from about 8.9 under no-noise calibration to about 31.4 under oracle
truth calibration, while robust-DW cutoffs remain near 9-10.

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
