# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: first figure-led drafting pass started, then M0034 exposed a
scale-normalization error in the M0030/M37 diagonal-anchor robust-DW object.
M0036 now gives the replacement proposal: variance-ratio robust DW, combining
valid higher-cumulant moments with a profiled covariance-decomposition screen
where residual noise variances are bounded relative to structural-shock
variances.

Current focus: align the paper plan and future task sequence around the
variance-ratio robust DW proposal. The current work block is planning only:
do not yet draft Sections 2-4, rebuild Figure 2, create Figure 3, or perform
the math-format cleanup.

Next recommended action: sketch Sections 2-4 with the important formulas using
proper manuscript math delimiters, then update Figure 2 to use the
variance-ratio robust row, add the new Figure 3 sample-size grid, and rebuild
the validation/Monte Carlo evidence around the same proposal.

Active milestone: M0037, plan variance-ratio proposal.

Active blockers:

- The M0030/M37 diagonal-anchor robust-DW estimator is superseded. With
  `diag(B)=1`, the off-diagonal covariance equation is
  `Sigma_u,12=b21*sigma_1^2+b12*sigma_2^2`, not `b12+b21`, unless unit shock
  variances are imposed as an extra scale normalization. The active robust-DW
  fallback is the pure five-moment higher-cumulant stack.
- The M25 standard-DW J-test inversion result is only a working derivation; M28
  supports the high-noise divergence story, but the derivation still needs a
  direct audit before theorem-level prose.
- The M30 audit found that the original M35 moderate-noise scenario was near a
  structural-coordinate rescaling exception. The patched screen now includes
  an anisotropic diagonal-noise stress case, but the provisional
  scale-normalized finite-sample statistic is still too permissive for final
  evidence.
- The intuitive sign/DW/robust-DW evidence is no longer settled. M0034 rendered
  `fig_sign_dw_pure_robust_noise_grid.png`; in the high-noise column the pure
  robust row contains true `B0` but accepts about 0.459 of the full plotted
  grid, showing the expected loss of precision after dropping invalid
  second-order information.
- M0035 rendered `fig_sign_dw_bounded_noise_robust_grid.png`. The high-noise
  bounded row contains true `B0` and accepts about 0.066 of the full plotted
  grid, but this precision comes from the explicit absolute `0 <= nu_i <= 0.5`
  noise bound and is now a comparison rather than the preferred candidate.
- M0036 rendered `fig_sign_dw_relative_noise_robust_grid.png`. The high-noise
  relative row contains true `B0` and accepts about 0.071 of the full plotted
  grid, or 0.084 of the sign-admissible grid. Its precision comes from the
  explicit `nu_i <= 0.5 Var(epsilon_i)` signal-to-noise restriction; this is
  now the manuscript proposal, with audit and evidence rebuild still required.
- Sections 2-4 still need a formula-first prose sketch. Future drafting should
  use inline `\(...\)` and display `\begin{equation}...\end{equation}` math,
  not Markdown backtick math.
- Figure 2 must be rebuilt so its robust row uses the variance-ratio proposal
  rather than the superseded diagonal-anchor statistic.
- A new Figure 3 should vary sample size `T=500,1000,2000`, holding the
  Figure 1 structural non-Gaussianity and Figure 2 residual-noise calibration
  fixed.
- The robust-DW simulation code must be wrapped under `manuscript/replication/`
  before the paper is shareable.
- The first figure-led skeleton now uses the refreshed M29 chi-square rows as
  draft-level evidence and reserves repeated/bootstrap rows for
  robustness-audit language. Final publication replication should still move
  the code into `manuscript/replication/` and can rerun a heavier table if
  needed.

Last substantive session: 2026-06-06, opened M0037 to update the paper plan
and next tasks around the variance-ratio robust DW proposal without yet
drafting Sections 2-4 or generating the next figures.

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
