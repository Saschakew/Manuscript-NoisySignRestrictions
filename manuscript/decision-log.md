# Decision Log

Use this file for durable research, scope, notation, evidence, and workflow
decisions.

## Entries

### 2026-06-09 - Make next-task prompts packet-aware

- Origin: user asked whether prompts like "work on next task" and "plan next
  tasks" would actually use the new task-packet structure, then asked to
  improve the workflow.
- User input id: U0047
- Decision: The manuscript skill must explicitly handle next-task execution
  and task planning. For `work on next task` style prompts, select the task
  from the dashboard and task board, then read any linked task packet before
  source work, derivations, edits, or simulations. For `plan next tasks` style
  prompts, classify each new task as routine or fragile and create linked
  packets immediately for fragile or priority-1 scientific tasks.
- Rationale: A packet workflow that exists only as a general rule can still be
  skipped by a future agent. The user's common prompts need an explicit
  algorithm in the skill.
- Consequence for next work: M49 remains the next scientific task, and it must
  be executed from
  `manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md`.

### 2026-06-09 - Use task packets for fragile scientific hand-offs

- Origin: user concern that compressed or poorly specified tasks may have
  contributed to prior scientific mistakes, especially M48.
- User input id: U0046
- Decision: Keep `manuscript/task-board.md` as a compact index, but require
  durable task packets under `manuscript/tasks/` for priority-1 or fragile
  scientific tasks involving long prompts, source verification, derivations,
  code-to-theory comparisons, normalization decisions, simulation rebuilds, or
  prior failed work.
- Required packet contents: original user prompt, why the task exists,
  untrusted prior artifacts, required reads, scientific claim ledger, required
  work, stop conditions, acceptance criteria, expected outputs, and an outcome
  log.
- Rationale: A task-board row compresses too much context and can turn
  scientific uncertainty into a vague implementation task. A packet preserves
  the user's concern and gives future agents a contract for evidence,
  derivation, and stopping.
- Consequence for next work: M49 must be executed from
  `manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md`, not from the
  task-board row alone. Future fragile tasks should receive packets before
  execution.

### 2026-06-09 - Require source and derivation gates for scientific claims

- Origin: user criticism after M48 produced an incorrect or insufficient
  standard-DW moment stack and overconfident normalization conclusion.
- User input id: U0045
- Decision: Future mathematical, source-sensitive, and code-sensitive claims
  must be classified as `raw-source`, `vault-source`, `derived`,
  `code-implemented`, `conjectural`, or `user-decision` before entering
  polished manuscript prose. Only `raw-source`, `vault-source`, `derived`, or
  explicit `user-decision` claims can be stated as settled. Code behavior can
  describe implementation behavior only unless the source-to-code mapping is
  separately verified.
- Rationale: The M48 work treated a local Figure 1 implementation and a broad
  memory of DW co-moments as enough to write a source-level manuscript claim.
  That failed the standard needed for a scientific paper.
- Consequence for next work: M48 is quarantined as partial and
  source-insufficient. M49 must redo the DW source and noisy moment audit from
  the user's original comments, raw DW source or KnowledgeVault note, and
  explicit derivations before M47 or final Section 3/4 claims proceed.

### 2026-06-09 - Keep standard co-moments separate from robust cumulants

- Origin: M48 audit of the user's DW fourth-order moment and normalization
  comments.
- User input id: U0044
- Status after M0045: superseded as a closure decision. The broad warning that
  fourth-order raw products and fourth cumulants are different remains useful,
  but M48 did not source-verify the exact bivariate DW GMM moment menu, did
  not fully derive the requested noisy product moments, and did not justify the
  normalization/no-rebuild conclusion.
- Decision retained only as provisional: do not describe standard-DW fourth
  products as robust fourth cumulants without source and derivation support.
- Consequence for next work: do not treat M48 as done. Run M49 before M47 and
  before any final figure/Monte Carlo rebuild decision.

### 2026-06-08 - Use residual-noise-to-signal wording for the variance-ratio screen

- Origin: M34 adversarial scope, logic, and style review.
- User input id: U0042
- Decision: In reader-facing prose, describe \(\rho\) as a maximum
  residual-noise-to-signal variance ratio, or more generally as the
  variance-ratio screen, rather than as a maximum information/noise ratio.
- Rationale: The maintained condition is \(\nu_i\le \rho s_i\), so \(\rho\)
  caps residual-noise variance relative to structural-shock variance. Calling
  it a maximum information/noise ratio is directionally confusing and risks
  making the identifying information look automatic.
- Consequence for next work: Keep using variance-ratio or
  residual-noise-to-signal language in draft prose, captions, abstracts, and
  future replication notes. Older logs may retain historical terminology.

### 2026-06-08 - Rewrite front half for SVAR-reader formulation

- Origin: user instruction to incorporate the revision branch comments.
- User input id: U0041
- Codex role: read GitHub issue #1 and revision branch
  `Revision-20260608-070142`, extracted the inline comments, rewrote the
  abstract, introduction, and Sections 2-4, and updated registry/planning
  surfaces.
- Decision: The front half should start from the language an SVAR reader
  expects: no-noise sign restrictions identify a set of impact matrices using
  signs and recovered-shock orthogonality; residual noise breaks that
  orthogonality and shifts the covariance target; DW refinement should first
  be explained under its no-noise higher-moment logic; the robust proposal
  should start with the researcher-chosen information/noise ratio and then add
  Gaussian-noise-blind higher cumulants.
- Rationale: The revision comments identified the previous draft as too hard
  to read for an SVAR audience and too quick to introduce notation without
  explaining the standard no-noise object. The new ordering makes the failure
  mode and the proposed fix visible before the heavier formulas.
- Consequence for next work: Run M34 as an adversarial logic and style review
  of the revised draft. The M25 proof audit and final replication wrapper
  remain open before theorem-level or shareable-paper claims.

### 2026-06-07 - Treat M45 as lightweight variance-ratio evidence gate

- Origin: user instruction to run M42-M45 around the variance-ratio proposal.
- User input id: U0040
- Codex role: cleaned the draft math delimiters, rebuilt Figure 2, added
  Figure 3, created and ran the M45 evidence script, and updated the draft,
  registry, planning surfaces, and logs.
- Decision: Use the M45 chi-square-primary Monte Carlo table as the current
  draft evidence for the variance-ratio robust DW proposal, while labeling it
  a lightweight evidence gate rather than the final replication package.
- Rationale: The M45 run applies the hard variance-ratio screen in every
  accepted-set and truth-inclusion calculation. Under primary chi-square
  cutoffs, the high Gaussian-noise row gives standard-DW truth inclusion 0.000
  and variance-ratio robust-DW truth inclusion 0.875, with a robust
  truth-feasible rate of 0.958.
- Consequence for next work: Run an adversarial scope/evidence review before
  theorem-level or final evidence wording. The M25 standard-DW proof audit and
  manuscript-local replication wrapper remain open.

### 2026-06-07 - Clear variance-ratio screen for proposal prose

- Origin: Codex-selected M40 audit after the user asked to continue manuscript
  work in goal mode.
- User input id: U0039
- Codex role: audited the variance-ratio covariance screen, checked the
  implementation, ran a small repeated-draw truth-screen sanity check, and
  updated the draft, registry, planning surfaces, and logs.
- Decision: Treat the M0036 variance-ratio screen as conditionally cleared for
  careful Section 4 proposal prose. The algebra is valid for
  `S = B diag(s_1,s_2) B' + diag(nu_1,nu_2)` with
  `0 <= nu_i <= 0.5 s_i`, and the implementation matches the resulting
  linear feasibility problem.
- Rationale: The screen avoids the M0034 double-normalization error by
  profiling structural-shock variances and residual-noise variances. Its
  precision comes from explicit signal-to-noise identifying information, not
  from a DW moment or a normalization.
- Consequence for next work: Do not claim coverage or final evidence yet.
  M43-M45 still need to rebuild Figure 2, add Figure 3, and rerun validation
  and Monte Carlo evidence for the variance-ratio proposal. M42 math cleanup
  is the next low-risk draft maintenance step.

### 2026-06-06 - Adopt variance-ratio robust DW as the proposal

- Origin: user planning instruction after inspecting the M0036 relative-noise
  Figure 1.
- User input id: U0037
- Codex role: updated the project plan, paper map, workplan, task board, formal
  registry, and logs to make the variance-ratio screen the active proposal and
  to queue the next writing and evidence tasks.
- Decision: Treat the M0036 variance-ratio robust DW screen as the manuscript's
  proposal. Future work should adjust the draft around this proposal, sketch
  Sections 2-4 with the important formulas, use proper manuscript math
  delimiters instead of Markdown backtick math, update Figure 2, add Figure 3
  varying `T=500,1000,2000`, and rebuild validation/Monte Carlo evidence.
- Rationale: Bounding residual noise relative to structural-shock variance is
  scale-correct in the diagonal-normalized chart and solves the arbitrary-unit
  problem of the absolute M0035 bound while preserving useful precision.
- Consequence for next work: M41 should sketch Sections 2-4 formula-first;
  M42 should clean math delimiters; M43 should rebuild Figure 2; M44 should
  add the sample-size Figure 3; M45 should rebuild validation and Monte Carlo
  evidence; M40 remains the adversarial audit of the variance-ratio screen.

### 2026-06-06 - Use relative noise-to-shock variance screen as candidate

- Origin: user correction after the M0035 absolute bounded-noise figure.
- User input id: U0036
- Codex role: derived the candidate covariance-decomposition feasibility
  screen, rendered the Figure 1 variant, and recorded the follow-up audit
  task.
- Decision: Treat the relative screen `0 <= nu_i <= 0.5 Var(epsilon_i)` as the
  preferred Figure 1 candidate pending audit. For `B=[[1,a],[b,1]]`, sample
  covariance `S`, structural variances `s_i`, and diagonal residual-noise
  variances `nu_i`, require
  `S11=s1+a^2*s2+nu1`, `S12=b*s1+a*s2`,
  `S22=b^2*s1+s2+nu2`, and `0 <= nu_i <= 0.5*s_i`.
- Rationale: The bound is scale-correct because it restricts noise relative to
  structural-shock variance instead of imposing an arbitrary absolute cap.
  Precision still comes from substantive signal-to-noise information and must
  be presented as identifying information, not as a DW moment.
- Consequence for next work: M40 should audit the algebra, finite-sample
  equality-plus-inequality behavior, and interpretability of the 50 percent
  signal-to-noise bound before the relative row replaces the evidence spine or
  Section 4 prose.

### 2026-06-06 - Test bounded-noise recovered-covariance screen

- Origin: user suggestion after the pure robust Figure 1 variant.
- User input id: U0035
- Codex role: derived the candidate recovered-covariance interval, rendered
  the Figure 1 variant, and recorded the follow-up audit task.
- Decision: Treat the bounded-noise recovered-covariance screen as a promising
  candidate, not yet as the active theorem-level robust-DW object. For
  `B=[[1,a],[b,1]]`, `e(B)=B^{-1}u`, and diagonal residual noise
  `V=diag(nu_1,nu_2)`, the candidate truth satisfies
  `E[e1 e2]=(-b*nu_1-a*nu_2)/(1-ab)^2`. With `0 <= nu_i <= 0.5`, this gives
  a candidate-specific interval for `E[e1 e2]`.
- Rationale: This uses second-order information without imposing the invalid
  zero recovered-shock covariance moment or the superseded `b12+b21` anchor.
  The precision comes from explicit noise-scale information, so the upper
  bound must be defended rather than hidden as a normalization.
- Consequence for next work: M40 should audit the algebra, finite-sample
  inequality-screen behavior, and substantive interpretation of the `0.5`
  upper bound before the bounded row replaces the evidence spine or Section 4
  prose.

### 2026-06-06 - Drop the invalid diagonal-anchor robust-DW moment

- Origin: user correction during discussion of the M0030/M37 robust-DW
  moment stack.
- User input id: U0034
- Codex role: checked the moment algebra, generated the pure-cumulant Figure 1
  variant, and marked the prior diagonal-anchor evidence as superseded.
- Decision: The robust-DW object should not use the displayed
  `Cov(u1,u2)=b12+b21` anchor when the chart already normalizes
  `diag(B)=1`. That equation also requires unit shock variances; with free
  shock scales it becomes
  `Sigma_u,12=b21*sigma_1^2+b12*sigma_2^2`, so it is not a clean restriction
  on `(b12,b21)`.
- Rationale: Imposing both diagonal-normalized impacts and unit-variance
  shocks fixes scale twice. The recovered-shock covariance moment is also
  invalid under residual noise. The only currently valid robust-DW moments in
  this chart are the mixed higher cumulants of `B^{-1}u` under Gaussian
  residual noise.
- Consequence for next work: Treat the M0030/M37 six-moment diagonal-anchor
  evidence as superseded. Rebuild the visual and Monte Carlo spine around the
  pure higher-cumulant robust set, or introduce an explicitly justified scale
  model before using any second-order information.

### 2026-06-06 - Position the paper as a residual-noise robustness check

- Origin: Codex-selected M32 task after user requested manuscript work in
  goal mode.
- User input id: U0033
- Codex role: selected M32 from the task board and drafted the first
  literature-positioning pass.
- Decision: Keep the literature positioning compact and inside the
  introduction. The paper should be framed as adjacent to sign-restricted SVAR
  set inference, Drautzburg-Wright independence refinement, and higher-moment
  SVAR/GMM work, but its contribution is the residual-noise
  DW-versus-robust-DW diagnostic rather than a broad survey or a general
  higher-moment estimator.
- Rationale: The manuscript is meant to stay short and focused on one
  robustness-check idea. The positioning pass needs to be fair to
  Drautzburg-Wright under the no-noise null and honest about weak higher
  moments, while making clear that covariance-target contamination is this
  paper's new object.
- Consequence for next work: M32 is done. Sections 2-4 should now be drafted
  around the noisy sign pseudo-set, standard-DW-under-noise caveats, and M37
  robust-estimator limits.

### 2026-06-06 - Clear M37 diagonal-noise robust estimator audit

- Origin: Codex-selected next task after user requested manuscript work in
  goal mode.
- User input id: U0032
- Codex role: selected M37 from the task board and performed a direct method
  audit.
- Decision: The post-M0030 diagonal-noise robust DW estimator may support
  Section 4 theorem-level prose only as a conditional local normalized
  bivariate result under diagonal Gaussian residual noise. The reported
  six-moment object stacks the off-diagonal covariance anchor with five mixed
  higher cumulants.
- Rationale: The off-diagonal covariance anchor is valid under diagonal
  residual-noise covariance and avoids the false standard-DW recovered-shock
  covariance target. The cumulant stack remains valid under Gaussian residual
  noise because transformed Gaussian noise has no higher cumulants.
- Required caveats: state the normalized-chart scale restriction; decide
  whether formal sets include nonnegative profiled diagonal-variance
  inequalities; describe `chi2_6` as a pointwise applied benchmark, not a
  coverage theorem; and use fallback language for correlated Gaussian,
  diagonal non-Gaussian, and correlated non-Gaussian residual noise.
- Consequence for next work: M37 is done. Resume M32 literature positioning or
  run the separate M25 standard-DW proof audit before promoting Section 3
  theorem wording.

### 2026-06-06 - Add a direct post-M0030 estimator audit task

- Origin: user instruction to align the plan and next tasks with the new
  estimator
- User input id: U0031
- Codex role: audited and revised planning surfaces.
- Decision: The paper plan should describe the constructive object as a
  diagonal-noise robust DW set, not merely as the older pure higher-cumulant
  route. The next method task should be M37, a direct audit of the
  off-diagonal covariance anchor, diagonal-variance profiling, mixed
  higher-cumulant stack, `chi2_6` cutoff convention, and fallback language for
  correlated or non-Gaussian residual noise before theorem-level prose.
- Rationale: M0030 modified the reported estimator by adding valid
  second-moment information under diagonal noise. That is central enough that
  the active plan should not treat the older cumulant-only audit as sufficient.
- Consequence for next work: Run M37 before promoting the robust-DW validity
  result to theorem-level text, then return to M32 literature positioning and
  the remaining drafting tasks.

### 2026-06-06 - Replace pure robust row with diagonal-noise robust statistic

- Origin: user correction and methodological suggestion
- User input id: U0030
- Codex role: investigated, implemented, validated, and aligned evidence.
- Decision: Do not use `V=(2,2)` in the residual-noise story figure. The
  reported robust-DW row should no longer be the pure higher-cumulant row for
  the diagonal-noise design. It should stack the diagonal-noise robust
  off-diagonal covariance restriction `Cov(u1,u2)=b12+b21` with the mixed
  higher-cumulant restrictions of `B^{-1}u`.
- Rationale: With the previous symmetric high-noise DGP, standard DW rejected
  true `B0` only when Gaussian noise was large enough to dilute the
  higher-cumulant signal, making the pure robust set nearly the whole chart.
  The off-diagonal covariance restriction is valid under diagonal residual
  noise because diagonal noise does not shift `Sigma_{u,12}`, but it avoids the
  false standard-DW restriction that recovered shocks must have zero
  covariance.
- Consequence for next work: The selected figures, M28 validation, M29 Monte
  Carlo table, draft prose, and registry now use the M0030 revised robust
  statistic and lower high-noise column `V=(0.5,0.5)`. If future versions allow
  unrestricted residual-noise covariance, the off-diagonal covariance anchor
  must be dropped and the pure higher-cumulant set should be reported instead.

### 2026-06-06 - Keep Figure 1 as method rows and noise columns

- Origin: user correction
- User input id: U0029
- Codex role: verified the figure orientation after an initial
  misinterpretation.
- Decision: Figure 1 should keep the residual-noise grid layout with rows for
  sign/covariance, standard DW, and robust DW; structural non-Gaussianity is
  fixed; columns increase residual noise from no noise to medium noise to
  strong noise.
- Rationale: This layout makes the main warning readable: holding the shock
  distribution fixed, the reader moves left to right as the noisy covariance
  target worsens and sees how the three methods react.
- Consequence for next work: The non-Gaussianity grid remains the separate
  Figure 2 limitation figure and should not be substituted for Figure 1.

### 2026-06-06 - Start the draft with the figure-led evidence spine

- Origin: Codex execution of user-requested next task
- User input id: U0028
- Codex role: selected M31, drafted the first figure-led prose skeleton, and
  aligned planning surfaces.
- Decision: The first draft should introduce the paper through the selected
  visual spine: Figure 1 for the residual-noise warning, Figure 2 for the
  weak-higher-moment limitation, and Table 1 for the larger M29
  chi-square-primary Monte Carlo support.
- Rationale: M28 and M29 already support the two-grid story at draft level.
  Starting with figures lets the paper make the robustness-check argument
  before moving into theorem-level prose that still needs direct proof audit.
- Consequence for next work: M32 should write the literature-positioning pass.
  Sections 2-4 still need disciplined prose, and the M25 result should not be
  promoted to theorem language until its proof audit is complete.

### 2026-06-06 - Treat larger M29 as draft evidence gate complete

- Origin: Codex execution of user-requested next task
- User input id: U0027
- Codex role: selected the active M29 follow-up, ran the larger Monte Carlo
  table, interpreted the output, and aligned planning surfaces.
- Decision: M29 is complete for the first figure-led draft. The main reported
  benchmark should be the larger chi-square-primary run with 240 calibration
  replications, 120 evaluation replications, 40 truth-bootstrap replications
  per evaluation sample, and a 41-by-41 grid. Audit cutoffs remain secondary
  calibration-cost diagnostics.
- Rationale: Under primary chi-square cutoffs, the high-noise stress case has
  standard DW including true `B0` in 0.325 of evaluation samples, while robust
  DW includes it in 0.908. Weak and Gaussian structural-shock scenarios keep
  robust DW wide, with mean accepted shares of 0.914 and 0.913, matching the
  intended limitation story.
- Consequence for next work: Move to M31 figure-led drafting. Coverage-style
  language should remain simulation-design-specific, and final sharing still
  requires a replication wrapper under `manuscript/replication/`.

### 2026-06-06 - Use chi-square cutoffs as the primary applied benchmark

- Origin: user-originated cutoff-convention decision
- User input id: U0026
- Codex role: recorded the decision and aligned evidence planning surfaces.
- Decision: M29 should use the standard pointwise chi-square critical values
  as the main applied benchmark for standard DW and robust DW. These are the
  cutoffs an applied researcher would use under the maintained no-noise DW
  null if residual noise is not considered.
- Rationale: The paper's warning is about what happens to the usual procedure
  when its no-noise target is misspecified. Recalibrating standard DW under
  the noisy DGP is an oracle audit, not the procedure being critiqued.
- Consequence for next work: Report chi-square rows as the central evidence.
  Keep no-noise repeated, oracle scenario truth, and truth-point bootstrap
  rows as finite-sample size and calibration-cost audits.

### 2026-06-06 - Treat M29 truth bootstrap as a calibration-cost audit

- Origin: Codex execution of user-requested next task
- User input id: U0025
- Codex role: selected the active M29 follow-up, added a truth-point
  residual-bootstrap cutoff convention, reran the expanded Monte Carlo pass,
  and updated planning surfaces.
- Decision: The truth-point residual bootstrap should be treated as an
  evidence audit, not as the final applied cutoff rule. It restores high-noise
  truth inclusion for both standard DW and robust DW, but only by widening
  accepted sets; in the high-noise case, the robust set covers essentially the
  full plotted chart under the bootstrap convention.
- Rationale: Under no-noise repeated calibration, the high-noise standard-DW
  truth-inclusion rate remains about 0.333 while robust DW remains about
  0.875. Under the truth bootstrap, both reach 1.000, but the high-noise
  accepted shares are about 0.325 for standard DW and 1.000 for robust DW.
- Consequence for next work: After U0026, use chi-square rows as the main M29
  evidence and keep this bootstrap as an audit row. M29 still needs a larger
  chi-square-primary final run before final coverage-style claims.

### 2026-06-06 - Treat M29 as passed first calibrated evidence gate

- Origin: Codex execution of user-requested next task
- User input id: U0024
- Codex role: selected M29, implemented the first calibrated Monte Carlo pass,
  ran it, and updated planning surfaces.
- Decision: The M29 first pass supports keeping the M0020/M28 grid pair as the
  evidence spine, but it is not yet the final manuscript table. The high
  Gaussian-noise scenario is the key result: standard DW requires a much larger
  oracle truth cutoff to cover true `B0`, while robust DW remains wide and
  truth-compatible under the maintained Gaussian residual-noise condition.
- Rationale: Under the no-noise repeated calibration, standard DW covers true
  `B0` in only about one third of high-noise evaluation samples, while robust
  DW covers it in most samples. The high-noise oracle standard-DW cutoff rises
  to about 31.4, compared with about 8.9 under no noise.
- Consequence for next work: Audit and expand M29 with more replications or
  bootstrap critical values before treating coverage, width, empty-set,
  overlap, or divergence summaries as final evidence.

### 2026-06-06 - Use a directional DW-versus-robust-DW diagnostic

- Origin: Codex execution of user-requested next task
- User input id: U0023
- Codex role: selected M27, formalized the comparison object, and updated
  planning surfaces.
- Decision: The manuscript should compare standard DW and robust DW in the
  same normalized impact chart. The main warning metric is directional:
  standard-DW accepted mass outside the robust-DW set indicates that no-noise
  covariance-target precision may not be robust. Robust-DW mass outside
  standard DW is not itself a warning because the robust set deliberately drops
  second-moment restrictions.
- Rationale: The robust set is expected to be wider, so symmetric overlap
  alone can misclassify honest widening as failure. The directional metric
  aligns the interpretation with the M0020/M28 visual story and the M24/M25
  derivations.
- Consequence for next work: M29 should use the M27 metric bundle when
  reporting accepted shares, empty-set frequencies, overlap, standard-DW mass
  outside robust-DW, truth inclusion in simulations, least-rejected candidates,
  and calibrated critical-value behavior.

### 2026-06-06 - Treat M28 as passed first validation gate

- Origin: Codex execution of user-requested next task
- User input id: U0022
- Codex role: selected M28, implemented the validation script, ran diagnostics,
  and updated planning surfaces.
- Decision: The M0020 residual-noise and non-Gaussianity grid pair may remain
  the paper's visual spine after the first M28 validation gate. The population
  robust-DW moment stack has true `B0` as a zero under the maintained Gaussian
  residual-noise condition, standard DW diverges under noisy covariance
  targets, and weak or Gaussian structural higher moments widen or empty the
  identifying content of the robust row.
- Rationale: The validation checked exact population moments, base/expanded
  grid boundaries, repeated finite-sample seeds, true-`B0` J diagnostics, and
  pointwise critical-value sensitivity. These checks support the qualitative
  figure story without making final size or coverage claims.
- Consequence for next work: M27 should formalize the standard-DW versus
  robust-DW comparison diagnostic. After U0026, M29 should retain pointwise
  chi-square guides as the primary applied benchmark and use repeated-sample or
  bootstrap critical values only as audit diagnostics.

### 2026-06-06 - Make the M0020 grid pair the paper's visual spine

- Origin: user-originated planning decision
- User input id: U0021
- Codex role: updated the plan, map, dashboard, task sequence, registry, and
  logs.
- Decision: Organize the paper around two main figures: the residual-noise
  grid and the non-Gaussianity grid. The first grid tells the main warning:
  noise moves the sign/covariance set, standard DW can reject the truth, and
  robust DW remains wider and contains it. The second grid tells the
  limitation: robust DW becomes wide when structural higher moments weaken.
- Rationale: The corrected figures now communicate the complete paper story in
  a compact way, more clearly than separate isolated sign-bias, DW, and robust
  panels.
- Consequence for next work: M28 has validated the grid-pair story at the
  first gate; M27 should formalize the comparison diagnostic using the figure
  language; M29 should quantify coverage, width, overlap, and divergence;
  drafting should become figure-led after formalization and calibration.

### 2026-06-06 - Use one J-test inversion object in both grid figures

- Origin: user-originated correction
- User input id: U0020
- Codex role: corrected the simulation scripts and regenerated both figures.
- Decision: Both grid figures should show accepted sets from pointwise
  finite-sample J-test inversion at the 10 percent level in every row. The
  robust-DW row uses the five mixed higher-cumulant restrictions
  `(C112, C122, C1112, C1122, C1222)` and excludes cross covariance as a
  restriction.
- Rationale: Mixing finite-sample J-test rows with a population-score robust
  row made the cutoff interpretation unclear and weakened the visual story.
  Using one J-test object across rows makes the comparison interpretable.
- Consequence for next work: Captions must say these are pointwise J tests.
  The non-Gaussian Gaussian-shock column should be described as population
  all-null with finite-sample pointwise test noise. M28/M29 still need
  population and calibrated finite-sample checks before final paper use.

### 2026-06-06 - Define grid robust rows as pure higher-cumulant sets

- Origin: user-originated correction
- User input id: U0019
- Codex role: corrected the figure scripts and documentation.
- Decision: In both grid figures, the robust-DW row must represent the pure
  robust object: mixed higher cumulants only, no cross-covariance restriction,
  and no second-moment target. The sign and standard-DW rows can remain
  finite-sample N-test rows, but the robust row is a population
  higher-cumulant set until M29 supplies calibrated finite-sample inference.
- Rationale: The paper's main claim is that robust DW gives up second-moment
  information to avoid noisy covariance misspecification. A row that includes
  cross covariance would not show that object and would not become uninformative
  when structural shocks are Gaussian.
- Consequence for next work: Captions and prose must explicitly say that the
  robust rows are pure higher-cumulant population sets; M28/M29 still need to
  turn this visual object into audited simulation evidence.

### 2026-06-06 - Pair the noise grid with a non-Gaussianity grid

- Origin: user-originated
- User input id: U0018
- Codex role: created the companion figure and updated project controls.
- Decision: Keep M0017 as the main residual-noise grid and add M0018 as a
  companion grid that varies structural-shock non-Gaussianity at fixed
  residual noise. Together they tell the main story and its honest limitation:
  standard sign/DW can be misled by noisy covariance targets, while robust DW
  remains noise-robust but can become wide when higher moments are weak.
- Rationale: The first figure shows the noise channel. It does not show that
  robust DW depends on structural non-Gaussian information. The companion grid
  isolates that dependence by holding `V=(0.3,0.3)` fixed and weakening the
  shock higher moments across columns.
- Alternatives considered: trying to add non-Gaussianity as another dimension
  inside the already dense M0017 figure, or leaving the limitation only in
  prose.
- Consequence for next work: Treat the two-grid pair as the preferred
  candidate visual package, pending M28/M29 checks for population behavior,
  weak moments, and critical-value calibration.

### 2026-06-06 - Use N-test cutoffs for the requested grid figure

- Origin: user-originated correction
- User input id: U0017
- Codex role: rebuilt the requested B-plane grid figure and added the robust
  row.
- Decision: The preferred candidate figure for the sign/DW/robust-DW visual is
  now the M0017 3-by-3 B-plane grid, not the M0016 three-panel figure. The
  M0017 figure uses finite-sample pointwise N-test statistics with chi-square
  cutoffs, rather than the older artificial fixed population-score cutoff.
- Rationale: The KnowledgeVault synthesis explicitly distinguishes the older
  fixed-score visual from the corrected finite-sample J/N-test figure. The
  manuscript visual should use the statistic whose accepted regions have an
  inferential interpretation.
- Alternatives considered: keeping the M0016 figure as the main visual, or
  reproducing the old 2-by-3 grid with the artificial `0.02` cutoff.
- Consequence for next work: Treat `fig_sign_dw_robust_noise_grid.png` as the
  preferred candidate, while still requiring M28/M29 checks for population
  behavior, weak moments, and calibrated critical values.

### 2026-06-06 - Treat M0016 figure as intuition, not final evidence

- Origin: user-originated
- User input id: U0016
- Codex role: checked the KnowledgeVault synthesis and visualization script,
  replicated the sign/standard-DW noise figure logic, and added a robust-DW
  panel.
- Decision: Use the M0016 figure as an exploratory candidate visual. It can
  explain the difference between covariance-rotation sign/DW behavior and the
  Gaussian-noise robust-DW higher-cumulant set, but it should not be promoted
  to final evidence before M28 population-grid checks.
- Rationale: The figure is deterministic and population-level, with an
  illustrative fixed cutoff. The robust-DW panel deliberately drops
  second-moment restrictions and therefore stays fixed across Gaussian
  residual-noise variances, but the manuscript still needs grid checks for
  robust truth inclusion, remote aliases, weak moments, and defensible
  critical values.
- Alternatives considered: treating the replicated figure as a final paper
  figure immediately, or waiting for M28 before making any visualization.
- Consequence for next work: Use M0016 to guide M28 population-grid design and
  then decide whether the final figure needs additional covariance-ellipse or
  pseudo-set geometry panels.

### 2026-06-06 - Audit M35 before trusting simulation evidence

- Origin: Codex execution of user-requested next task
- User input id: U0015
- Codex role: selected M30, audited, patched, and logged
- Decision: The M35 triage code may be used only as an exploratory screen.
  The manuscript should move next to M28 population-grid checks, not polished
  figures or final finite-sample Monte Carlo tables.
- Rationale: The audit found that the original moderate Gaussian-noise case was
  close to a structural-coordinate rescaling exception, so it was a weak test
  of generic standard-DW misspecification. The script now reports the
  structural-coordinate off-diagonal noise norm and includes an anisotropic
  diagonal-noise stress case, but the statistic still uses provisional
  diagonal scaling and an uncalibrated chi-square critical value.
- Alternatives considered: treating the M35 output as enough to proceed to
  figures, or discarding the screen entirely.
- Consequence for next work: Run M28 population grids for structural-rescaling
  exceptions, generic noisy-covariance pseudo-zeros, robust-DW truth inclusion,
  and weak-moment widening. Defer M29 until critical values are calibrated.

### 2026-06-06 - Treat M35 as cautionary triage, not final evidence

- Origin: Codex execution of user-requested next open task
- User input id: U0014
- Codex role: selected M35, implemented the screen, and interpreted results
- Decision: The M35 early Monte Carlo output should be treated as a cautionary
  evidence gate, not as final support for polished standard-DW false-sharpening
  figures or Monte Carlo tables.
- Rationale: The no-noise strong-moment sanity case behaves reasonably, but the
  provisional scale-normalized finite-sample statistic remains frequently
  nonempty under moderate Gaussian residual noise and becomes almost
  non-discriminating under weak higher moments.
- Alternatives considered: moving directly to polished figures, or abandoning
  the robust comparison because the first finite-sample screen is not sharp.
- Consequence for next work: Audit the M35 script/statistic in M30 and run M28
  population-grid checks before expanding to final M29 Monte Carlo evidence.

### 2026-06-06 - Restrict first paper to simultaneous SVAR and add early MC gate

- Origin: user-originated
- User input id: U0013
- Codex role: implemented and continued
- Decision: The first version focuses only on the simultaneous SVAR impact
  system. The paper treats the reduced-form residual `u_t` as given and does
  not model VAR lags, lag estimation, dynamic impulse responses, or
  horizon-specific sign restrictions. After the analytical J-test inversion
  result, the next evidence step should be a lightweight Monte Carlo overview
  before investing in polished figures or a large replication suite.
- Rationale: This keeps the project small enough to evaluate quickly and makes
  the go/no-go evidence gate explicit.
- Alternatives considered: retaining language about dynamic signs and VAR
  lags as deferred but still nearby, or building final figures before checking
  whether the finite-sample J-test comparison works.
- Consequence for next work: Complete M25, then run the new M35 early MC
  triage before spending major effort on M26-M30 polish.

### 2026-06-06 - Treat robust DW derivation as a local audited route

- Origin: Codex adversarial audit of the active plan
- User input id: U0012
- Codex role: selected next task and audited
- Decision: The robust DW higher-cumulant route may remain the constructive
  method in the active paper, but only as a local normalized Gaussian-noise
  result until population-grid and Monte Carlo checks are complete.
- Rationale: The audit found no error in the higher-cumulant cancellation,
  third/fourth cumulant moment equations, second-moment exclusion, or local
  rank calculation. It did identify important boundaries: the bivariate
  `B(a,b)` chart fixes scale rather than recovering it, `C_{1122}` is second
  order at the truth, non-Gaussian residual noise is not covered by the clean
  cumulant argument, and remote finite-order aliases remain possible.
- Alternatives considered: promoting the route immediately to a global theorem,
  or abandoning it because it does not identify scale or cover non-Gaussian
  noise.
- Consequence for next work: M25 should attack the standard-DW
  misspecification/empty-set claim; M28 must check robust-DW truth inclusion,
  remote aliases, and weak-moment widening on population grids.

### 2026-06-06 - Pivot active paper to robust DW comparison

- Origin: user-originated
- User input id: U0011
- Codex role: implemented and logged
- Decision: The active manuscript plan is now a robust-DW comparison paper.
  The paper should first show noisy sign-set bias, then show how standard
  Drautzburg-Wright refinement can falsely shrink a misspecified set under
  residual noise, then propose a robust DW higher-moment set that drops
  second-moment restrictions, and finally compare the standard and robust sets
  as a practical robustness check.
- Rationale: This gives the manuscript a cleaner structure and a sharper
  applied recommendation than the previous candidate route. It also keeps the
  higher-moment idea close to the main comparator while making the efficiency
  cost of noise robustness explicit.
- Alternatives considered: retaining the previous constructive route in the
  active paper, or adding an empirical application before the formal/simulation
  package is stable.
- Consequence for next work: Audit the robust DW derivation, prove or weaken
  the standard-DW asymptotic-empty claim, design the intuitive sign-noise
  figure, and build Monte Carlo comparisons before drafting polished prose.

### 2026-06-06 - Treat Gaussian-noise DW-like moments as a candidate route

- Origin: user-originated
- User input id: U0010
- Codex role: derived and logged
- Decision: Add a derivation for a Gaussian-noise
  Drautzburg-Wright-like higher-cumulant route, while keeping it as a
  candidate structure until adversarial audit. The route drops no-noise
  covariance whitening, searches over a normalized impact space, and uses
  mixed higher cumulants of `B^{-1}u` written as GMM-style moment equations.
- Rationale: Under Gaussian additive residual noise, higher cumulants of
  candidate transformed residuals are not shifted by the noise, but second
  moments are shifted. This gives a cleaner restricted route at the cost of
  assuming Gaussian noise and discarding structural second-moment information.
- Alternatives considered: continuing with the previous observed-residual
  cumulant route, or treating standard no-noise DW covariance whitening as
  valid under residual noise.
- Consequence for next work: Audit the new derivation, especially the
  cumulant-to-moment algebra, scale normalization, local rank conditions,
  finite-sample bias wording, and whether this route can carry the active
  constructive section.

### 2026-06-05 - Formal object typography and proof endings

- Origin: user-originated
- User input id: U0001
- Codex role: implemented and logged
- Decision: In Markdown drafts, assumptions, definitions, propositions, lemmas,
  corollaries, and theorems should be italicized in full, and should not carry
  visible end-marker text. Proofs should start with `Proof:` and end with `□`.
- Rationale: Full-statement italics make the start and end of formal objects
  visually clear without adding artificial closing text.
- Alternatives considered: retaining visible `End of Proposition` markers.
- Consequence for next work: Future draft revisions should format formal
  statements with full italics and proof blocks with the square terminator.

### 2026-06-05 - Initialize standalone manuscript repository

- Origin: user-originated
- User input id: U0003
- Codex role: implemented and logged
- Decision: Create this manuscript as a standalone repository linked to
  KnowledgeVault, with `vault/syntheses/Research proposal - noise-robust
  sign-restricted SVARs.md` as the originating source.
- Rationale: Manuscript work should be shareable and versioned independently
  while retaining explicit source links to the vault.
- Alternatives considered: keeping the manuscript inside `vault/manuscripts/`
  or leaving the template placeholders until the first prose draft.
- Consequence for next work: Use this repository as the paper workspace and
  KnowledgeVault as source memory, citation store, and replication provenance.

### 2026-06-05 - Scope first version as a short theory-and-simulation note

- Origin: user-originated request plus proposal synthesis
- User input id: U0003
- Codex role: synthesized and revised
- Decision: The first version should be bivariate and impact-oriented in the
  main text, centered on the noisy sign pseudo-set, the no-noise independence
  refinement failure/false-precision channel, and the BR-style robust sign
  inversion plus noise diagnostic.
- Rationale: The proposal already has enough formal and evidence burden. Adding
  empirical work, dynamic signs, or a full `K`-variable implementation now would
  slow the core paper and blur the central contribution.
- Alternatives considered: a seven-section paper with an empirical illustration
  and a broader `K`-variable method section.
- Consequence for next work: Formalize Propositions 1-4 first; defer empirical
  illustration and general implementation until the core proof/evidence package
  is stable.

### 2026-06-05 - Treat Drautzburg-Wright as a maintained-null comparator

- Origin: source-packet review
- User input id: U0003
- Codex role: synthesized
- Decision: The paper should not claim that independence refinement is
  mechanically wrong. It should say that no-noise independence refinement is a
  valid test inversion for its maintained null, while diagonal residual noise
  changes the population null and can make finite-sample accepted regions look
  falsely precise.
- Rationale: This is more accurate, fairer, and stronger rhetorically than
  attacking higher moments in general.
- Alternatives considered: presenting the paper as a broad critique of
  higher-moment SVAR identification.
- Consequence for next work: The literature section and Proposition 2 must
  distinguish asymptotic rejection/emptiness from finite-sample
  least-rejected-region interpretation.

### 2026-06-05 - Verify the Bonhomme-Robin-style result before claiming it

- Origin: user correction and updated KnowledgeVault notes
- User input id: U0005
- Codex role: analyzed and revised plan
- Decision: The paper should no longer frame the constructive method as a
  direct Bonhomme-Robin clean-moment inversion. It should call the bivariate
  method a Bonhomme-Robin-style profiled cumulant inversion, derive it
  independently, and verify it with symbolic, population, and finite-sample
  simulations before promoting it to a manuscript result.
- Rationale: The corrected vault notes clarify that Bonhomme and Robin first
  identify/subtract error cumulants using clean-pair restrictions and that the
  `L=K=2` bivariate SVAR is not directly covered by the full quasi-JADE rank
  theorem. Pure own moments are nuisance or diagnostic moments unless extra
  restrictions are placed on the noise.
- Alternatives considered: keeping the earlier plan that treated mixed
  cumulants as the BR fix and using existing figures as sufficient evidence.
- Consequence for next work: The next work block should derive the bivariate
  cumulant system, run adversarial derivation reviews, build verification
  simulations, and only then draft the BR-style result.
