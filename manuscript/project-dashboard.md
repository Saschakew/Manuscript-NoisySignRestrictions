# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: evidence gate complete for figure-led drafting after the
M0020-corrected noise and non-Gaussianity grid pair, with M28 first
validation, M27 diagnostic formalization, and the larger M29
chi-square-primary Monte Carlo pass complete.

Current focus: draft the figure-led section skeleton around the validated
two-grid story, using M29's chi-square rows as the main applied evidence and
audit rows only for calibration-cost language.

Next recommended action: start M31 by drafting the figure-led introduction
and evidence-section skeleton with source trails: noise grid first,
non-Gaussianity grid second, chi-square M29 table as the quantitative support.

Active milestone: none. M0021 records the user decision that the M0020 grid
pair tells the paper's main story and should organize the next plan.

Active blockers:

- The robust DW derivation passed M24 only as a local normalized
  Gaussian-noise result. M27 has formalized the reported set and diagnostic
  language, M28 supports its population truth-inclusion behavior, and the
  larger M29 run now gives draft-level chi-square-primary Monte Carlo
  evidence plus repeated-sample, oracle, and truth-point residual-bootstrap
  calibration audits.
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
  checks, repeated seeds, and pointwise critical-value sensitivity. M29's
  expanded pass supports the high-noise divergence story under the same
  chi-square cutoffs applied researchers would use. The audit cutoffs quantify
  the calibration cost; the truth-bootstrap convention restores truth
  inclusion only by widening the reported sets.
- The robust-DW simulation code must be wrapped under `manuscript/replication/`
  before the paper is shareable.
- A figure-led section draft can now use the larger M29 chi-square rows as
  draft-level evidence and reserve repeated/bootstrap rows for robustness-audit
  language. Final publication replication should still move the code into
  `manuscript/replication/` and can rerun a heavier table if needed.

Last substantive session: 2026-06-06, ran the larger M29
chi-square-primary table with 240 calibration replications, 120 evaluation
replications, 40 truth-bootstrap replications per evaluation sample, and a
41-by-41 B-plane grid. Under the primary chi-square cutoffs, high-noise
standard-DW truth inclusion is 0.325, while robust DW is 0.908. Weak and
Gaussian structural-shock cases keep robust DW wide, with mean robust accepted
shares of 0.914 and 0.913.

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
