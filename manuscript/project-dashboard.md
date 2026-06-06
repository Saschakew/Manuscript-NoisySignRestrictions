# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: first figure-led drafting pass started, then revised after the
M0030 high-noise power audit and M37 estimator audit. The abstract,
introduction, and evidence section now use the M0030 diagonal-noise robust
grid pair, refreshed M28 validation, M27 diagnostic formalization, the
refreshed M29 chi-square-primary Monte Carlo pass, and the M37 caveats as the
manuscript spine.

Current focus: write the literature-positioning pass that distinguishes this
paper from Drautzburg-Wright under the no-noise null, sign-set inference, and
higher-moment SVAR GMM.

Next recommended action: start M32 with explicit citation trails and clear
contribution boundaries. Keep the M37 estimator caveats visible when drafting
Section 4 theorem-level prose.

Active milestone: none. M0032 records the post-M0030 estimator audit.

Active blockers:

- The robust DW derivation passed M24 as a local normalized Gaussian-noise
  result and was revised in M0030 to use diagonal-noise second-moment
  information. M37 now conditionally clears the post-M0030 estimator for
  theorem-level prose as a local normalized bivariate diagnostic under
  diagonal Gaussian residual noise. Section 4 must still state the normalized
  scale caveat, optional nonnegative profiled-variance screen, pointwise
  `chi2_6` status, and fallback language for correlated or non-Gaussian
  residual noise.
- The M25 standard-DW J-test inversion result is only a working derivation; M28
  supports the high-noise divergence story, but the derivation still needs a
  direct audit before theorem-level prose.
- The M30 audit found that the original M35 moderate-noise scenario was near a
  structural-coordinate rescaling exception. The patched screen now includes
  an anisotropic diagonal-noise stress case, but the provisional
  scale-normalized finite-sample statistic is still too permissive for final
  evidence.
- The intuitive sign/DW/robust-DW evidence now has a selected M0030 visual
  spine with lower high noise `V=(0.5,0.5)`. M28 supports the story on exact
  population moments, grid-boundary checks, repeated seeds, and pointwise
  critical-value sensitivity. M29's refreshed pass supports the high-noise
  divergence story under the same chi-square cutoffs applied researchers would
  use. The audit cutoffs quantify the calibration cost; the truth-bootstrap
  convention restores truth inclusion by widening the reported sets.
- The robust-DW simulation code must be wrapped under `manuscript/replication/`
  before the paper is shareable.
- The first figure-led skeleton now uses the refreshed M29 chi-square rows as
  draft-level evidence and reserves repeated/bootstrap rows for
  robustness-audit language. Final publication replication should still move
  the code into `manuscript/replication/` and can rerun a heavier table if
  needed.

Last substantive session: 2026-06-06, completed M37, the direct post-M0030
audit of the diagonal-noise robust estimator. The audit conditionally cleared
the six-moment robust object for disciplined Section 4 prose and recorded
caveats about normalized scale, profiled diagonal variances, pointwise
`chi2_6` cutoffs, and correlated or non-Gaussian residual-noise fallbacks.

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
