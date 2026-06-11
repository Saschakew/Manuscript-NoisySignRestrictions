# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: M47 is complete after the M52 evidence rebuild. The stepwise M54 derivation confirms that the
requested population moments separate transformed-noise remainders from
Gaussian covariance-product simplifications, and the normalization audit keeps
the manuscript in the common `diag(B)=1` chart for the first paper. M56
establishes that the fourth-cumulant sample entries are generated smooth
moments, not ordinary fixed row-level moments. M55 has now turned those
results into reader-facing Section 4 prose: the draft distinguishes
transformed-noise covariance `Omega(B)=Var(B^{-1}eta_t)` from full
transformed-residual covariance `S(B)=Var(B^{-1}u_t)`, shows why the robust
moments hold at `B0`, gives representative fourth-order algebra, and states
the candidate-by-candidate sample recipe. M52 rebuilt the evidence path:
standard DW now uses the source-correct bivariate GMM1 higher-moment menu
`112`, `122`, `1112`, `1122`, and `1222`, intersected with a separate
no-noise covariance screen in the common B-plane, and the robust row now uses
full central-moment delta weighting for generated fourth-cumulant entries.
M47 conditionally clears the M25 standard-DW proof gate: Proposition 2 is safe
as a rich-stack/ICA misspecification result with structural-rescaling,
finite-alias, compactness, and nonsingularity caveats visible.

Current focus: replication packaging and final review. The revised draft still conditionally
passes the M34 adversarial scope, logic, and style review; M49 clears the
source-moment menu and noisy-product gate; M0050 clears the M53 notation gate;
M54 clears the transformed-noise derivation and normalization gate; M56 clears
the generated-moment routing gate; and M55 clears the main-text explanation
gate. M52 clears the source-correct evidence gate, and M47 clears the
standard-DW proof-gate audit at conditional rich-stack strength. The active
Figure 1, Figure 2, Figure 3, and Table 1 use the M52
GMM1-plus-covariance-screen standard comparator and the M56 central-delta
robust generated-moment route.

Next recommended action: execute M33, the manuscript-local replication
wrapper, so final figures and tables rebuild from `manuscript/replication/`
without a local KnowledgeVault dependency. A unit-variance/rotation-chart
rewrite remains a separate future user decision if it is ever requested.

Active milestone: M0059 completed the M57 task folder workflow; GitHub
milestone 54 tracks the same work. M58-M62 were planning-only navigation
cleanups without transparency or GitHub milestones. M0058 completed the M47
standard-DW proof gate audit and created GitHub milestone 53. M0057 completed the M52 source-correct
evidence rebuild and created GitHub milestone 52. M0056 completed the M55 execution
block and created GitHub milestone 51. M0055 completed M56 and created GitHub
milestone 50 for the generated-moment audit. M0054 planned M56 and created
GitHub milestone 49 for the robust cumulant GMM/generated-moment audit
planning block. M0053 created GitHub milestone 48 for the main-text
moment-explanation planning block. M0052 completed M54. M0051 planned
M54 and created GitHub milestone 47 for the stepwise moment derivation and
normalization audit. M0050
completed M53 and created GitHub milestone 46 for the notation rewrite work
block. M0049 planned M53 and created GitHub milestone 45 for the planning
block. M0048 closed the M49 DW source audit and created GitHub milestone 44.
M0047 made the manuscript skill explicitly packet-aware for `work on next task`
and `plan next tasks` prompts. M0046 added task hand-off packets so high-risk
scientific tasks are no longer stored only as compressed task-board rows.
M0045 previously hardened the scientific claim workflow and quarantined
unreliable M48 conclusions.

Active blockers:

- The M0030/M37 diagonal-anchor robust-DW estimator is superseded. With
  `diag(B)=1`, the off-diagonal covariance equation is
  `Sigma_u,12=b21*sigma_1^2+b12*sigma_2^2`, not `b12+b21`, unless unit shock
  variances are imposed as an extra scale normalization. The active robust-DW
  fallback is the pure five-moment higher-moment stack, and M54 keeps the
  manuscript in this common chart.
- M47 conditionally clears the M25 standard-DW J-test inversion result. The
  theorem-level version must remain a rich-stack/ICA statement with
  structural-coordinate rescaling exceptions, finite-GMM alias caveats,
  compact sign-admissible sets, and nonsingularity stated.
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
  construction. Proposition 2 has now passed the M47 conditional proof audit,
  while Proposition 3 still needs final proof and heavier replication before
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
  now varies sample size `T=500,1000,2000`. M52 refreshed Figures 1-3 and the
  active Monte Carlo table with the source-correct GMM1 standard-DW row and
  full central-delta robust weighting. This remains a first-paper evidence
  gate rather than the final self-contained replication package.
- The robust-DW simulation code must be wrapped under `manuscript/replication/`
  before the paper is shareable.
- The draft now contains the M52 chi-square-primary Monte Carlo rows for the
  source-correct GMM1 standard-DW row and the variance-ratio robust row. Final
  publication replication should still move the code into
  `manuscript/replication/` and can rerun a heavier table if needed.
- M52 result is complete. It implements the M49 source-correct bivariate DW
  GMM1 menu, treats covariance as a separate B-plane screen, regenerates
  Figure 1/Figure 2/Figure 3, and records the M52 Monte Carlo table. In the
  high-noise chi-square row, standard-DW truth inclusion is `0.000` while
  robust-DW truth inclusion is `0.833`.
- M55 is complete. Section 4 now explicitly explains why the robust
  transformed-noise moment conditions hold at `B0`, why fourth-order
  covariance-product subtractions use full transformed-residual covariances
  `S_{ij}(B)`, and how those entries are computed from
  `z_t(B)=B^{-1}u_t` rather than from unobserved residual noise.
- M56 is complete. It shows that concentrated fourth-cumulant sample moments
  are generated smooth functions of primitive sample moments, not ordinary
  fixed row-level moments. M52 implements the chosen full central-moment
  delta-weighting route with mean-centering nuisance terms. A unit-variance/
  rotation-chart switch would need a separate manuscript-wide update task if
  the user ever requests one.

Last substantive session: 2026-06-10, completed M47 by auditing the M25
standard-DW proof gate after M52 rebuilt the source-correct evidence path.

Last maintenance session: 2026-06-11, completed M62 to audit the traceability
cleanup and confirm that the workflow improvements are enough for now. M61
added a lightweight question-index closeout rule to the task workflow and templates. M60 added
`tasks/LEGACY-STATUS.md` as a status map for old flat task packets. M59 added
`QUESTION-INDEX.md` as a compact map from recent user questions to answer
locations. M58 added `START-HERE.md` as the repository front door. M57
previously streamlined task folders and outcome notes after the user flagged
that task answers were hard to find.

## Orientation Map

- `START-HERE.md`: front door for the repository; use it first when the project
  feels spread across too many files.
- `QUESTION-INDEX.md`: compact map from recent user questions to the task
  outcomes, derivation notes, or logs where they were answered.
- `tasks/LEGACY-STATUS.md`: status map for old flat task packets and the old
  flat template.
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
- `tasks/`: task folders and legacy packets for fragile or priority-1
  scientific tasks; read `task.md` before executing and `outcome.md` for the
  short answer trail.
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
