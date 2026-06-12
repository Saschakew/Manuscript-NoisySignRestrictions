# Project Dashboard

Working title: Noise-Robust Sign-Restricted SVARs

Manuscript slug: noise-robust-sign-restricted-svars

KnowledgeVault link: `../knowledge-vault-link.json`

Current stage: Revision-20260610-190805 has been recovered and M64 rewrote the
active method route. The manuscript now treats the user revision as a durable
normalization decision: use \(E[\varepsilon_t\varepsilon_t']=I\), never
`diag(B)=1`, and formulate the robust estimator as standard GMM over the
impact matrix \(B\) and residual-noise variances \(\nu\). Sections 2-4 have a
first-pass revision: \(\mathcal S_0\) imposes
\(E[e_t(B)e_t(B)']=I\), the finite-sample second-moment vector includes both
variance moments plus covariance, standard DW refines that second-moment set,
and Section 4 replaces generated sample covariance-product plug-ins with
parameter-implied \(\omega_{ij}(B,\nu)\) terms.

Current focus: M71 has corrected the active figure and Monte Carlo objects,
and M72 has fixed the rendered figure layout.
Figures 1-3, the Table 1 diagnostic, and the extended MC now use first-shock
coordinates \((B_{11},B_{21})\), profile \(B_{12}\), \(B_{22}\), and
\(\lambda\), impose \(B_{11}>0\), \(B_{22}>0\), and \(B_{12}\le0\), and use
candidate-specific pointwise covariance weights for
\(Tg_T(B,\nu)'\widehat\Omega(B,\nu)^{-1}g_T(B,\nu)\). The 500-replication run
remains deferred; the corrected normal diagnostics are reduced-size evidence
checks, not the long MC. M72 changes only the plot framing: panels are square
and use shared display limits from accepted regions, \(B_0\), and \(B_{21}=0\).

Background: M68 rebuilt Figures 1-3 and the Monte Carlo diagnostic under the
M66-settled unit-variance GMM route, and M69 extended the MC into residual
noise, structural non-Gaussianity, and sample-size blocks. M71 supersedes those
versions for draft interpretation because it removes the extra \(B_{21}\ge0\)
screen and replaces true-point fixed weights with candidate-specific pointwise
weights.

Next recommended action: use M70 to interpret the corrected M71 extended MC
diagnostics in the draft, keeping the reduced diagnostic replication count and
pointwise-critical-value caveat visible. M65 still owns final
projected-inference wording, projected critical values, and release hardening.

Active milestone: M0068 completes the M72 figure-layout polish and GitHub
milestone #63 tracks the same figure presentation fix. M0067 completes M71 and
GitHub milestone #62 tracks the same sign-screen and pointwise-weighting
correction. M0066 was opened for a
500-replication M69 run but was superseded before producing results because
M71 had to correct the implemented figure/MC object first. M0065 completed M69
and GitHub milestone #60 tracks the same extended three-block Monte Carlo
work. M0064 completed M68 and closed
GitHub milestone 59 for the
first-shock impact evidence rebuild. M0063 completed M67 and closed GitHub
milestone 58 for the unit-variance Figure 1 rebuild. M0062 completed M66 and created GitHub milestone 57 for the
noise-ratio bound and grid algorithm. M0061 recovers Revision-20260610-190805 and creates the
unit-variance GMM repair path; GitHub milestone 56 tracks the same work. M0060 completed the M33 replication wrapper and created
GitHub milestone 55. M0059 completed the M57 task folder workflow; GitHub
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

- M65 is now advanced by M71. Figures 1-3 and the Monte Carlo diagnostics are
  rebuilt with the projected \((B,\lambda)\) GMM inversion, first-shock chart,
  corrected sign screen, and candidate-specific pointwise weights. The final
  projection-critical-value route remains open.
- The M64 revision supersedes the retained `diag(B)=1` chart. The active
  manuscript normalization is now \(E[\varepsilon_t\varepsilon_t']=I\), with
  residual-noise variances handled as nuisance parameters \(\nu\). M71 updates
  the Figure 1-3 and Monte Carlo replication commands; M52 companion evidence
  is historical.
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
- M33 added the manuscript-local replication wrapper under
  `manuscript/replication/`. A later release-hardening pass can still copy or
  package source under `manuscript/replication/src/` and pin exact dependency
  artifacts if a standalone archive is required.
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

Last substantive session: 2026-06-12, completed M72 by fixing the rendered
layout of the M71 Figures 1-3 without changing the underlying masks, weights,
or cutoffs.

Prior substantive session: 2026-06-12, completed M71 by removing the
\(B_{21}\) sign restriction, implementing candidate-specific pointwise
covariance weighting, regenerating Figures 1-3 plus the corrected Table 1 and
extended MC diagnostics, and updating the manuscript surfaces.

Prior substantive session: 2026-06-12, completed M69 by implementing
`m69_extended_three_block_mc.py`, adding an explicit `extended-mc` replication
stage, and running the now-superseded extended MC across the three active
figure blocks.

Prior planning session: 2026-06-12, created M69 for the extended three-block
Monte Carlo setup/coding task and M70 for the blocked draft interpretation
task.

Prior substantive session: 2026-06-12, completed M68 by imposing positive
diagonal signs, adding the \(B_{12}\le0\) sign restriction, switching active
figures to first-shock coordinates \((B_{11},B_{21})\), and rebuilding
Figures 1-3 plus the Monte Carlo diagnostic under the M66 unit-variance route.

Prior substantive session: 2026-06-12, completed M66 by deriving that the
scale-invariant bound is \(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\), not a
direct residual-coordinate \(0\le\nu_i\le\rho\) cap, revising Section 4's
projected set and algorithm, marking old Figure 1-3 scripts historical, and
unblocking M65.

Earlier substantive session: 2026-06-12, completed M64 by recovering the live
`Revision-20260610-190805` branch content, accepting the unit-variance
normalization decision, rewriting Sections 2-4 toward a standard GMM
\((B,\nu)\) route, and routing the next work to M65.

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
