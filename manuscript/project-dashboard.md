# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: workflow hardening after the M48 failure. The first figure-led
draft remains revised around the M0036 variance-ratio robust DW proposal and
the M0041 revision comments, but M0045 marks the M48 moment-definition and
normalization audit as partial and not source-complete. Section 3's displayed
standard-DW moment stack, the exact bivariate DW GMM menu, the Figure 1
standard-DW source match, and the normalization/rebuild decision are unsettled
until M49 redoes the audit from raw source and derivation.

Current focus: prevent source-sensitive claims from entering the manuscript
without provenance. The revised draft still conditionally passes the M34
adversarial scope, logic, and style review, but M48 no longer clears the DW
moment-definition gate. The next scientific task must be M49, and it must
start from the hand-off packet
`manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md`, which preserves the
user's original comments, raw DW source requirements, and explicit noisy-moment
derivation obligations.

Next recommended action: run M49 before M47. Redo the DW source and noisy
moment audit under the scientific claim gate by executing
`manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md`; only after the
standard-DW moment object is source-verified should M47 audit the J-test proof
gate. Keep M33 queued for the manuscript-local replication wrapper.

Active milestone: none after M0047 closed. M0047 made the manuscript skill
explicitly packet-aware for `work on next task` and `plan next tasks` prompts.
M0046 added task hand-off packets so high-risk scientific tasks are no longer
stored only as compressed task-board rows. M0045 previously hardened the
scientific claim workflow, updated the local manuscript skill, quarantined
unreliable M48 conclusions, and created GitHub milestone 41 for the same work.

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
  now the manuscript proposal. M40 conditionally passed the screen algebra and
  interpretation; M45 rebuilt the lightweight validation and Monte Carlo
  evidence around this proposal.
- Sections 2-4 now have an M0041 revision-driven rewrite rather than only the
  M0038 formula sketch. The prose is deliberately SVAR-first: define the
  no-noise sign-restricted object, add residual noise, explain standard DW
  under its no-noise null, then introduce the residual-noise-to-signal robust
  construction. Proposition 2 still depends on the M25 proof audit, and
  Proposition 3 still needs final proof and heavier replication before
  theorem-level wording.
- M34 completed a full adversarial scope, logic, and style review. It tightened
  variance-ratio terminology, softened simulation claims in the abstract,
  added a visible skewed-residual-noise stress-case caveat, drafted the
  conclusion, and updated citation provenance to point the active Monte Carlo
  table at M45 rather than historical M29 evidence.
- Manuscript-wide math-format cleanup was completed under M42. Remaining
  backticks in `draft.md` are reserved for paths, citation keys, object labels,
  table labels, commands, and code identifiers.
- Figure 2 has been rebuilt with the variance-ratio robust row, and Figure 3
  now varies sample size `T=500,1000,2000`. The M45 fixed-grid diagnostics and
  Monte Carlo table support the evidence sequence, but the run is still a
  lightweight evidence gate rather than the final replication package.
- The robust-DW simulation code must be wrapped under `manuscript/replication/`
  before the paper is shareable.
- The draft now contains the M45 chi-square-primary Monte Carlo rows for the
  variance-ratio robust row. Final publication replication should still move
  the code into `manuscript/replication/` and can rerun a heavier table if
  needed.
- M48 result is quarantined. It caught the broad distinction between standard
  raw/product moments and robust cumulants, but it did not establish the exact
  bivariate Drautzburg-Wright GMM moment menu from source, did not fully
  derive the user's requested noisy product moments, and did not justify the
  normalization/no-rebuild decision. Do not rely on the current Section 3
  `g_DW` display or the Figure 1 standard-DW source claim until M49.

Last substantive session: 2026-06-09, completed M0047 to make next-task
execution and task planning explicitly packet-aware in the local manuscript
skill, the task-packet workflow reference, and manuscript rules.

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
- `tasks/`: durable hand-off packets for fragile or priority-1 scientific
  tasks; read the packet before executing the task-board row.
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
