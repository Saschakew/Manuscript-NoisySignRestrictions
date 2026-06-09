# Session Log

Record meaningful work blocks. Avoid duplicating every detail already visible in
Git history or the task board.

For traceable work blocks, pair this human-readable note with a closed
`transparency/milestones/*.json` manifest and a Git milestone tag.

## Entries

### 2026-06-09 - Complete M53 DW and robust moment notation rewrite

- Request or goal: execute M53 by replacing the Section 3 `h_i(B)` DW notation
  with recovered-shock notation and rewriting Section 4 robust conditions as
  explicit moment equations.
- Files changed: `manuscript/draft.md`,
  `manuscript/formal-object-registry.json`, `manuscript/task-board.md`,
  `manuscript/tasks/M53-dw-and-robust-moment-notation-rewrite.md`,
  `manuscript/project-dashboard.md`, `manuscript/paper-map.md`,
  `manuscript/workplan.md`, logs, and M0050 transparency files.
- Summary of work: rewrote the DW GMM1/GMM2 display to use
  \(e_t(B)=B^{-1}u_t\), stated the no-noise normalization
  \(e_t(B_0)=\varepsilon_t\), and rewrote the robust stack \(G_H(B)\) as
  explicit third- and fourth-order moment equations with covariance-product
  subtractions.
- Next recommended action: execute M52 to rebuild the standard-DW figures and
  Monte Carlo evidence with the source-correct moment menu.

### 2026-06-09 - Plan M53 DW and robust moment notation rewrite

- Request or goal: plan a new task to replace the Section 3 `h_i(B)` DW
  notation with recovered-shock notation and rewrite Section 4 robust
  conditions as moment equations rather than visible cumulant notation.
- Files changed: `manuscript/tasks/M53-dw-and-robust-moment-notation-rewrite.md`,
  `manuscript/task-board.md`, `manuscript/project-dashboard.md`,
  `manuscript/paper-map.md`, `manuscript/workplan.md`,
  `manuscript/formal-object-registry.json`, and logs/transparency files.
- Summary of work: created packet-backed M53 with the original user prompt,
  required reads, scientific claim ledger, stop conditions, and acceptance
  criteria; routed M53 before M52 so notation is cleaned before the
  source-correct evidence rebuild.
- Next recommended action: execute M53, then return to M52 for the standard-DW
  evidence rebuild.

### 2026-06-09 - Complete M49 DW source and noisy-moment audit

- Request or goal: continue the manuscript workflow by executing the M49
  hand-off packet.
- Files changed: `manuscript/derivations/m49-dw-source-and-noisy-moment-audit.md`,
  `manuscript/tasks/M52-standard-dw-source-correct-rebuild.md`,
  `manuscript/draft.md`, `manuscript/source-packet.md`,
  `manuscript/formal-object-registry.json`, planning/provenance surfaces, and
  logs.
- Summary of work: read the raw Drautzburg-Wright source and translated the
  bivariate GMM menus; derived the requested noisy product moments from
  `z=epsilon+B0^{-1}eta`; classified the existing Figure 1/M45 standard-DW
  code as a historical hybrid rather than source-correct GMM1 or GMM2; and
  created M52 as the source-correct evidence rebuild task.
- Next recommended action: run M52 before relying on the current standard-DW
  figure/Monte Carlo rows or before M47 audits the standard-DW proof gate.

### 2026-06-09 - Clarify next-task workflow

- Request or goal: improve the new task workflow so the manuscript skill
  explicitly handles common prompts like "work on next task" and "plan next
  tasks."
- Files changed: `.codex/skills/write-standalone-manuscript/SKILL.md`,
  `.codex/skills/write-standalone-manuscript/references/task-packet-workflow.md`,
  `manuscript/manuscript-rules.md`, `manuscript/task-board.md`,
  `manuscript/project-dashboard.md`, `manuscript/workplan.md`, and logs.
- Summary of work: added explicit next-task selection and task-planning
  algorithms to the local manuscript skill; clarified that linked task packets
  must be read before executing fragile tasks and that fragile or priority-1
  scientific tasks planned in the future need packets created immediately.
- Next recommended action: execute M49 from
  `manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md`.

### 2026-06-09 - Improve task hand-off workflow

- Request or goal: improve the manuscript workflow and local skill for task
  creation and task management after discussing that compressed tasks may have
  contributed to prior scientific mistakes.
- Files changed: `.codex/skills/write-standalone-manuscript/SKILL.md`,
  `.codex/skills/write-standalone-manuscript/references/task-packet-workflow.md`,
  `manuscript/manuscript-rules.md`, `manuscript/tasks/_template.md`,
  `manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md`,
  `manuscript/task-board.md`, `manuscript/project-dashboard.md`,
  `manuscript/paper-map.md`, `manuscript/workplan.md`,
  `manuscript/formal-object-registry.json`, and logs/transparency files.
- Summary of work: made the task board a compact index rather than the full
  hand-off for fragile scientific work; added a task-packet workflow and
  template; created a self-contained M49 packet preserving the original user
  prompt, source obligations, derivation obligations, stop conditions, and
  acceptance criteria.
- Next recommended action: execute M49 from
  `manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md`, not from the
  task-board row alone.

### 2026-06-09 - Harden scientific workflow after M48 failure

- Request or goal: update the manuscript workflows and local skills so future
  scientific claims require source, vault, derivation, or explicit user
  provenance instead of relying on plausible Codex memory or code behavior.
- Files changed: `.codex/skills/write-standalone-manuscript/SKILL.md`,
  `.codex/skills/write-standalone-manuscript/references/scientific-claim-audit.md`,
  `manuscript/manuscript-rules.md`, `manuscript/draft.md`,
  `manuscript/derivations/m48-dw-moment-normalization-audit.md`,
  `manuscript/project-dashboard.md`, `manuscript/paper-map.md`,
  `manuscript/task-board.md`, `manuscript/formal-object-registry.json`,
  `manuscript/workplan.md`, `manuscript/decision-log.md`,
  `manuscript/review-log.md`, and transparency/log files.
- Summary of work: added a scientific claim gate to the local manuscript skill
  and manuscript rules, created a detailed claim-audit reference, quarantined
  M48 as partial and source-insufficient, added M49 as the source-first DW
  audit, and blocked M47 on M49.
- Next recommended action: run M49 from the user's original comments, raw DW
  source or KnowledgeVault note, and explicit noisy moment derivations before
  any Section 3/4 DW claims or normalization/rebuild decisions are finalized.

### 2026-06-09 - Resolve DW moment normalization

- Request or goal: work on the manuscript in goal mode by choosing the next
  task, which resolved to M48.
- Files changed: `manuscript/derivations/m48-dw-moment-normalization-audit.md`,
  `manuscript/draft.md`, `manuscript/project-dashboard.md`,
  `manuscript/paper-map.md`, `manuscript/task-board.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/workplan.md`, and logs.
- Summary of work at the time: attempted to verify the DW comparator, match it
  to Figure 1, derive noisy truth raw-product formulas, and decide the
  normalization chart.
- M0045 correction: this work block is now marked partial and
  source-insufficient. It should not be used as the settled DW source audit or
  as a no-rebuild decision.
- Next recommended action after M0045: run M49 before M47.

### 2026-06-08 - Insert DW moment comments task

- Request or goal: insert a task to work through the user's comments on the
  standard-DW fourth-order moment definition, the Figure 1 implementation, the
  noisy Section 4 moment derivations, and a possible switch from `diag(B)=1`
  to \(\operatorname{Var}(\epsilon)=1\).
- Files changed: `manuscript/task-board.md`,
  `manuscript/project-dashboard.md`, `manuscript/paper-map.md`,
  `manuscript/user-input-log.md`, `manuscript/session-log.md`,
  `manuscript/codex-log.md`, and M0043 transparency files.
- Summary of work: opened local transparency milestone M0043, confirmed the
  Figure 1 script's standard-DW row uses raw standardized product moments with
  target \(E[e_1^2e_2^2]=1\) while the robust row computes cumulants, and
  added M48 as a priority-1 audit and derivation task.
- Next recommended action: run M48 before revising Section 3 or rebuilding
  evidence. GitHub milestone creation remains unrepaired for M0043 because
  `gh` is unavailable locally and the visible GitHub connector has no
  milestone-creation tool.

### 2026-06-08 - M34 adversarial review and GitHub milestone repair

- Request or goal: after GitHub CLI login, finish the missing GitHub milestone
  linkage and then run M34, the adversarial scope, logic, and style review of
  the revised manuscript and M45 evidence.
- Files changed: M0041 and M0042 transparency files, `manuscript/draft.md`,
  `manuscript/review-log.md`, `manuscript/task-board.md`,
  `manuscript/project-dashboard.md`, `manuscript/paper-map.md`,
  `manuscript/workplan.md`, `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/writing-feedback-log.md`,
  and human-readable logs.
- Summary of work: created and closed GitHub milestone #38 for M0041, opened
  local M0042 and GitHub milestone #39 for M34, ran the adversarial review,
  tightened the variance-ratio language, softened abstract simulation claims,
  added a skewed-residual-noise stress-case caveat, updated citation provenance
  from historical M29 to current M45 evidence, and drafted the conclusion.
- Next recommended action: run M47, the direct M25 standard-DW proof audit,
  before strengthening Proposition 2 or theorem-level language. M33 replication
  wrapping remains the next shareability gate after proof review.

### 2026-06-08 - Incorporate revision comments into front-half prose

- Request or goal: incorporate the new revision comments, rewriting the
  abstract, introduction, and Sections 2-4 carefully and then reviewing the
  result against the spirit of the comments.
- Files changed: `manuscript/draft.md`,
  `manuscript/formal-object-registry.json`, `manuscript/paper-map.md`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  human-readable logs, and M0041 transparency files.
- Summary of work: found the revision on GitHub issue #1 and branch
  `Revision-20260608-070142`. Rewrote the front half so it first explains
  no-noise sign-restricted SVARs, recovered-shock orthogonality, and J-test
  inversion; then introduces additive residual noise and the noisy covariance
  pseudo-set; then explains DW under the no-noise null and how noise creates
  false precision; and finally presents the information/noise-ratio robust DW
  construction before the evidence section.
- Next recommended action: run M34, an adversarial scope, logic, and style
  review of the revised draft and M45 evidence, while keeping the M25 proof
  audit and replication wrapper open.

### 2026-06-07 - Rebuild variance-ratio figures and evidence

- Request or goal: run M42 math-delimiter cleanup, rebuild Figure 2 with the
  variance-ratio robust row, add the Figure 3 sample-size grid, and rebuild
  validation/Monte Carlo evidence around the same proposal.
- Files changed: `manuscript/draft.md`, Figure 2 and Figure 3 scripts and
  notes, M45 evidence script and outputs, `manuscript/formal-object-registry.json`,
  planning/control surfaces, logs, and M0040 transparency files.
- Summary of work: completed M42-M45. Cleaned remaining draft math backticks,
  regenerated `fig_sign_dw_robust_nongaussianity_grid.png`, created
  `fig_sign_dw_sample_size_robust_grid.png`, and ran
  `m45_variance_ratio_evidence.py`. The primary high-noise Monte Carlo row now
  reports standard-DW truth inclusion 0.000 and variance-ratio robust-DW truth
  inclusion 0.875.
- Next recommended action: run M34, a full adversarial scope and logic review
  of the rebuilt figure-led draft and M45 evidence, while keeping the M25 proof
  audit and replication wrapper open.

### 2026-06-07 - Audit variance-ratio robust DW screen

- Request or goal: work on the manuscript in goal mode, choose the next task,
  and complete a substantive manuscript work block.
- Files changed: `manuscript/derivations/m40-variance-ratio-robust-dw-screen-audit.md`,
  `manuscript/derivations/dw-noise-robust-moments.md`,
  `manuscript/draft.md`, `manuscript/formal-object-registry.json`,
  planning/control surfaces, logs, and M0039 transparency files.
- Summary of work: selected M40 and completed the adversarial audit of the
  M0036 variance-ratio robust DW covariance screen. The audit conditionally
  passes the algebra and implementation, records that `rho=0.5` is substantive
  signal-to-noise information, and documents a small repeated-draw check of the
  hard finite-sample screen at the true `B0`.
- Next recommended action: run M42, the manuscript-wide math delimiter
  cleanup, then rebuild Figure 2, add Figure 3, and rerun M28/M29-style
  evidence under M43-M45.

### 2026-06-07 - Sketch Sections 2-4 with formulas

- Request or goal: work on the manuscript in goal mode, choose the next task,
  and complete a substantive manuscript work block.
- Files changed: `manuscript/draft.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/paper-map.md`,
  `manuscript/paper-plan.md`, `manuscript/source-packet.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`, logs, and M0038
  transparency files.
- Summary of work: selected M41 and replaced the Section 2-4 TODO stubs with
  formula-first skeletons for the noisy sign pseudo-set, standard-DW
  misspecification under residual noise, and the variance-ratio robust DW
  proposal. The new draft uses `\(...\)` and
  `\begin{equation}...\end{equation}` delimiters in these sections and keeps
  M25/M40 audit caveats visible.
- Next recommended action: run M40 to audit the variance-ratio covariance
  screen before theorem-level Section 4 prose or Figure 2/Figure 3 evidence
  rebuilds.

### 2026-06-06 - Plan variance-ratio robust DW proposal

- Request or goal: update the paper plan and future tasks so the
  variance-ratio robust DW bound is the proposal, while not yet drafting
  Sections 2-4 or generating the next figures.
- Files changed: planning/control surfaces, formal registry, decision and user
  input logs, and M0037 transparency files.
- Summary of work: opened local transparency milestone M0037 and GitHub
  milestone #34; updated the source packet, dashboard, paper plan, paper map,
  workplan, task board, and registry so M0036 variance-ratio robust DW is the
  active proposal; added future tasks for Section 2-4 formula sketches, math
  delimiter cleanup, Figure 2 rebuild, Figure 3 sample-size grid, and
  validation/Monte Carlo rebuild.
- Next recommended action: start M41, sketching Sections 2-4 with the
  important formulas and proper manuscript math delimiters.

### 2026-06-06 - Render relative-noise covariance Figure 1

- Request or goal: replace the absolute residual-noise variance bound with a
  scale-correct restriction that noise variance is at most 50 percent of the
  corresponding structural-shock variance, and show Figure 1.
- Files changed: `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/figures/fig_sign_dw_relative_noise_robust_grid.png`, the new
  relative-figure note, planning/control surfaces, logs, and M0036
  transparency files.
- Summary of work: opened local transparency milestone M0036 and GitHub
  milestone #33; added `--robust-mode relative`; implemented a profiled
  covariance-decomposition screen over shock variances `s_i` and noise
  variances `nu_i`; rendered the relative-noise robust row; and recorded that
  the candidate restores precision only by adding explicit signal-to-noise
  information.
- Next recommended action: run M40 to audit the relative covariance screen
  before replacing the evidence spine or drafting theorem-level Section 4
  prose.

### 2026-06-06 - Test bounded-noise covariance Figure 1

- Request or goal: consider a new covariance anchor based on `E[e1 e2]` with
  unknown diagonal residual-noise variances bounded above by 0.5, and show the
  resulting Figure 1.
- Files changed: `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/figures/fig_sign_dw_bounded_noise_robust_grid.png`, the new
  bounded-figure note, planning/control surfaces, logs, and M0035 transparency
  files.
- Summary of work: opened local transparency milestone M0035 and GitHub
  milestone #32; derived the recovered-covariance interval
  `E[e1 e2]=(-b*nu_1-a*nu_2)/(1-ab)^2`; added `--robust-mode bounded`; rendered
  the bounded-noise robust row; and recorded that the candidate restores
  precision only by adding explicit noise-scale information.
- Next recommended action: run M40 to audit the bounded screen before
  replacing the evidence spine or drafting theorem-level Section 4 prose.

### 2026-06-06 - Generate pure robust Figure 1 after scale correction

- Request or goal: show how Figure 1 looks when robust DW drops the invalid
  covariance anchor.
- Files changed: `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/figures/fig_sign_dw_pure_robust_noise_grid.png`, the new pure
  figure note, planning/control surfaces, logs, and M0034 transparency files.
- Summary of work: opened local transparency milestone M0034 and GitHub
  milestone #31; parameterized the Figure 1 generator with `--robust-mode
  pure`; rendered the pure five-moment higher-cumulant robust row; recorded
  that the M0030/M37 diagonal-anchor robust statistic is superseded because
  `diag(B)=1` and unit shock variances cannot both be used as free scale
  normalizations.
- Next recommended action: run M39 to rebuild the method/evidence spine around
  the pure robust set or an explicitly justified scale model before drafting
  Section 4.

### 2026-06-06 - Draft M32 literature positioning

- Request or goal: work on the manuscript in goal mode by picking the next
  task.
- Files changed: `manuscript/draft.md`, `manuscript/citation-provenance.md`,
  literature/planning surfaces, logs, and M0033 transparency files.
- Summary of work: selected M32 from the task board, opened local
  transparency milestone M0033 and GitHub milestone #30, and drafted
  introduction subsection 1.1. The new prose positions the paper relative to
  sign-restricted SVAR set inference, Drautzburg-Wright's no-noise
  independence refinement, and higher-moment SVAR/GMM work while marking the
  residual-noise DW-versus-robust-DW comparison as the original contribution.
- Next recommended action: start M38, drafting Sections 2-4 without promoting
  the M25 standard-DW generic-emptying result to theorem language before its
  proof audit.

### 2026-06-06 - Audit diagonal-noise robust estimator

- Request or goal: work on the manuscript in goal mode by picking the next
  task.
- Files changed: `manuscript/derivations/m37-diagonal-noise-robust-estimator-audit.md`,
  robust-DW derivation notes, planning/control surfaces, logs, and M0032
  transparency files.
- Summary of work: selected M37 from the task board, opened local transparency
  milestone M0032 and GitHub milestone #29, and completed the direct
  post-M0030 estimator audit. The audit conditionally clears the six-moment
  diagonal-noise robust DW statistic for local theorem-level prose under
  diagonal Gaussian residual noise, while requiring caveats about normalized
  scale, profiled diagonal variances, pointwise `chi2_6` cutoffs, and fallback
  noise cases.
- Next recommended action: start M32 literature positioning with explicit
  citation trails and contribution boundaries.

### 2026-06-06 - Align plan with the diagonal-noise robust estimator

- Request or goal: ensure the paper plan and next tasks match the M0030
  diagonal-noise robust DW estimator; leave files unchanged if everything is
  already aligned.
- Files changed: `manuscript/paper-plan.md`, `manuscript/paper-map.md`,
  `manuscript/project-dashboard.md`, `manuscript/workplan.md`,
  `manuscript/task-board.md`, logs, and M0031 transparency files.
- Summary of work: audited the active planning surfaces against the modified
  robust-DW estimator. Most surfaces already used the M0030 object, but the
  plan and review checklist still over-emphasized the older pure
  higher-cumulant route. Revised the active section/result language to the
  diagonal-noise robust DW set and added M37 as the direct estimator audit
  before theorem-level prose.
- Next recommended action: run M37, then return to M32 literature positioning.

### 2026-06-06 - Solve high-noise robust-DW power problem

- Request or goal: investigate why the high-noise robust-DW row lost power,
  avoid `V=(2,2)`, and consider a robust-DW modification that can use valid
  second-moment information.
- Files changed: robust-DW derivation and diagnostic notes, residual-noise and
  non-Gaussianity figure generators and PNGs, M28 and M29 simulation scripts
  and outputs, draft evidence prose, planning/control surfaces, logs, and
  M0030 transparency files.
- Summary of work: diagnosed the pure higher-cumulant finite-sample power
  failure under large symmetric Gaussian noise. Implemented the
  diagonal-noise robust statistic that stacks `Cov(u1,u2)=b12+b21` with mixed
  higher cumulants, lowered the selected high-noise scenario to `V=(0.5,0.5)`,
  regenerated the two grid figures, reran M28 validation, and refreshed the
  M29 Monte Carlo pass. Under primary chi-square cutoffs, the refreshed
  high-noise row has standard DW truth inclusion `0.050` and robust DW truth
  inclusion `0.900`.
- Next recommended action: continue with M32 literature positioning after the
  M0030 milestone is closed, committed, tagged, and pushed.

### 2026-06-06 - Verify Figure 1 residual-noise orientation

- Request or goal: respond to the user's correction about the first
  figure-led draft.
- Files changed: transparency files and logs only; the residual-noise figure
  and generator were restored to the committed intended layout after a brief
  mistaken transpose.
- Summary of work: opened M0029, checked the actual residual-noise and
  non-Gaussianity figures, initially misread the requested orientation, then
  restored and verified Figure 1 as method rows and noise columns:
  sign/covariance, standard DW, and robust DW by row; no, medium, and strong
  residual noise by column; fixed structural non-Gaussianity.
- Next recommended action: continue with M32 literature positioning after the
  figure-layout clarification is committed.

### 2026-06-06 - Draft M31 figure-led skeleton

- Request or goal: work on the manuscript in goal mode by picking the next
  task.
- Files changed: `manuscript/draft.md`, `manuscript/citation-provenance.md`,
  planning surfaces, logs, and M0028 transparency files.
- Summary of work: selected M31, opened local transparency milestone M0028 and
  GitHub milestone #25, and replaced the TODO-only abstract, introduction, and
  evidence section with a figure-led skeleton. The draft now presents the
  residual-noise pseudo-set warning, the standard-DW false-sharpening problem,
  the robust higher-cumulant comparison set, Figure 1 for the residual-noise
  grid, Figure 2 for the non-Gaussianity grid, and Table 1 for the M29
  chi-square-primary evidence.
- Next recommended action: start M32 by drafting the literature-positioning
  pass with explicit citation trails and contribution boundaries.

### 2026-06-06 - Run larger M29 chi-square-primary table

- Request or goal: work on the manuscript in goal mode by picking the next
  task.
- Files changed: `manuscript/simulations/m29_calibrated_monte_carlo.py`,
  `manuscript/simulations/m29_calibrated_monte_carlo.md`,
  `manuscript/simulations/output/m29_calibrated_monte_carlo.json`, planning
  surfaces, logs, and M0027 transparency files.
- Summary of work: selected the active M29 evidence follow-up, opened local
  transparency milestone M0027 and GitHub milestone #24, ran the larger
  chi-square-primary Monte Carlo table with 240 calibration replications, 120
  evaluation replications, 40 truth-bootstrap replications per evaluation
  sample, and a 41-by-41 grid. Under the primary chi-square cutoffs,
  high-noise standard DW includes true `B0` in 0.325 of evaluation samples,
  while robust DW includes it in 0.908. Weak and Gaussian structural-shock
  cases keep robust DW wide, matching the limitation story.
- Next recommended action: start M31 by drafting the figure-led introduction
  and evidence-section skeleton with source trails.

### 2026-06-06 - Record M29 chi-square cutoff convention

- Request or goal: respond to the user's cutoff-convention correction.
- Files changed: M29 simulation note generator and output note, planning
  surfaces, registry, draft notes, user/decision/review/session/Codex logs,
  and M0026 transparency files.
- Summary of work: recorded the user decision that standard pointwise
  chi-square critical values should be the primary applied M29 benchmark,
  because those are the values a researcher would use when applying standard
  DW without accounting for residual noise. Repeated-sample, oracle, and
  truth-bootstrap cutoffs are retained as calibration audits.
- Next recommended action: run a larger chi-square-primary M29 table before
  marking M29 complete or drafting final coverage-style claims.

### 2026-06-06 - Expand M29 calibrated Monte Carlo evidence

- Request or goal: work on the manuscript in goal mode by picking the next
  task.
- Files changed: `manuscript/simulations/m29_calibrated_monte_carlo.py`,
  `manuscript/simulations/m29_calibrated_monte_carlo.md`,
  `manuscript/simulations/output/m29_calibrated_monte_carlo.json`, planning
  surfaces, logs, and M0025 transparency files.
- Summary of work: selected the active M29 follow-up, added a
  truth-point residual-bootstrap cutoff convention, reran the expanded
  calibrated Monte Carlo, and recorded that bootstrap truth inclusion is bought
  by much wider accepted sets. The high-noise standard-DW truth-inclusion rate
  remains about 0.333 under no-noise repeated calibration, while robust DW
  remains about 0.875; under the truth bootstrap both reach 1.000, but the
  high-noise robust set covers essentially the full plotted chart.
- Next recommended action: audit the truth-bootstrap design, choose a final
  calibration convention, and run a larger final M29 table before drafting
  coverage-style evidence claims.

### 2026-06-06 - M29 calibrated Monte Carlo first pass

- Request or goal: work on the manuscript in goal mode by picking the next
  task.
- Files changed: `manuscript/simulations/m29_calibrated_monte_carlo.py`,
  `manuscript/simulations/m29_calibrated_monte_carlo.md`,
  `manuscript/simulations/output/m29_calibrated_monte_carlo.json`, planning
  surfaces, logs, and M0024 transparency files.
- Summary of work: selected M29, created a first calibrated finite-sample
  Monte Carlo pass on the M0020/M28 B-plane, and reported the M27 metric bundle
  under chi-square, no-noise repeated, and oracle scenario truth cutoff
  conventions. The high-noise standard-DW truth cutoff inflates sharply when
  oracle-calibrated, while robust DW remains wide and truth-compatible under
  Gaussian residual noise.
- Next recommended action: audit and expand M29 with more replications or
  bootstrap critical values before treating coverage-style summaries as final
  manuscript evidence.

### 2026-06-06 - Formalize robust DW comparison diagnostic

- Request or goal: work on the manuscript in goal mode by picking the next
  task.
- Files changed: `manuscript/derivations/dw-robust-comparison-diagnostic.md`,
  planning surfaces, draft notes, provenance, logs, and M0023 transparency
  files.
- Summary of work: selected M27, defined the reported standard-DW set,
  robust-DW set, critical-value convention, accepted-share and overlap
  measures, the directional standard-outside-robust warning metric,
  truth-inclusion simulation diagnostics, and interpretation boundaries. M27
  is now complete and M29 is the next recommended task.
- Next recommended action: start M29 calibrated finite-sample Monte Carlo
  evidence using the M27 metric bundle.

### 2026-06-06 - Validate M0020 grid-pair story

- Request or goal: pick the next manuscript task and work on it in goal mode.
- Files changed: `manuscript/simulations/m28_grid_story_validation.py`,
  `manuscript/simulations/m28_grid_story_validation.md`,
  `manuscript/simulations/output/m28_grid_story_validation.json`, planning
  surfaces, logs, and M0022 transparency files.
- Summary of work: selected M28, created a separate validation script for the
  M0020 grid pair, ran exact population moment checks, boundary sensitivity,
  repeated finite-sample seeds, true-`B0` diagnostics, and pointwise
  critical-value sensitivity. The first validation pass supports the visual
  spine while leaving calibrated coverage and critical values to M29.
- Next recommended action: run M27 by formalizing the standard-DW versus
  robust-DW comparison diagnostic in the same language as the M0020/M28
  evidence.

### 2026-06-06 - Update figure-led paper plan

- Request or goal: update the paper plan and next steps because the corrected
  figures now tell the paper's main story well.
- Files changed: `manuscript/paper-plan.md`, `manuscript/paper-map.md`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/source-packet.md`,
  `manuscript/formal-object-registry.json`, figure/simulation indexes, logs,
  and M0021 transparency files.
- Summary of work: promoted the M0020 residual-noise and non-Gaussianity grids
  to the selected visual spine; marked M26 complete; reordered next work around
  M28 validation, M27 diagnostic formalization, M29 Monte Carlo, and then
  figure-led drafting.
- Next recommended action: begin M28 validation of the selected grid pair.

### 2026-06-06 - Convert grid figures to J-test inversions

- Request or goal: make both grid figures invert J tests in all rows, clarify
  the cutoff language, and address the fact that the previous noise-grid
  standard-DW row still contained true `B0` under noise.
- Files changed:
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.md`,
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.md`, both
  rendered figure PNGs, planning surfaces, logs, and M0020 transparency files.
- Summary of work: replaced the robust population-score row with a
  finite-sample five-moment higher-cumulant J statistic, used 10 percent
  chi-square cutoffs in every row, added true-`B0` inclusion labels, and changed
  the noise-grid high-noise column to `V=(2,2)` so standard DW rejects true
  `B0` while robust DW contains it.
- Next recommended action: keep these as candidate visuals and run M28/M29
  validation before using them as final manuscript evidence.

### 2026-06-06 - Correct pure robust rows in grid figures

- Request or goal: check whether the earlier noise-grid figure used the
  correct robust DW without second moments, and correct the robust rows after
  the user pointed out the Gaussian-shock limit.
- Files changed:
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.md`,
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.md`, both
  rendered figure PNGs, planning surfaces, logs, and M0019 transparency files.
- Summary of work: removed the cross-covariance/profiling robust row from the
  grid scripts, replaced it with a population mixed-higher-cumulant score, made
  the residual noise Gaussian where the pure robust row is used, and aligned
  the population cumulants with the standardized chi-square(5) shock design.
- Next recommended action: use the corrected grid pair only as candidate
  evidence until M28 verifies population aliases and M29 calibrates
  finite-sample critical values for the robust set.

### 2026-06-06 - Add non-Gaussianity companion grid

- Request or goal: add a second figure like the corrected sign/DW/robust-DW
  grid, but with columns changing structural-shock non-Gaussianity.
- Files changed:
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.md`,
  `manuscript/figures/fig_sign_dw_robust_nongaussianity_grid.png`, planning
  surfaces, logs, and M0018 transparency files.
- Summary of work: fixed residual noise at `V=(0.3,0.3)`, varied the
  structural-shock non-Gaussian mixture weight across columns, reused the
  sign/covariance, standard-DW, and robust-DW pointwise N-test rows, and
  rendered the companion grid.
- Next recommended action: use M0017 and M0018 as candidate visuals while
  running M28/M29 validation before final manuscript use.

### 2026-06-06 - Rebuild requested B-plane grid with robust row

- Request or goal: correct the previous figure to match the KnowledgeVault
  two-row by three-column B-plane figure and add a robust-DW row; use the
  corrected N-test cutoff rather than the artificial fixed score cutoff.
- Files changed: `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.md`,
  `manuscript/figures/fig_sign_dw_robust_noise_grid.png`, planning surfaces,
  logs, and M0017 transparency files.
- Summary of work: rebuilt the sign/covariance and standard-DW B-plane rows
  with `N=500` pointwise chi-square cutoffs, added a robust-DW profiled moment
  row with the two-degree chi-square guide, and rendered the corrected 3-by-3
  figure.
- Next recommended action: use this as the preferred candidate visual and run
  M28/M29 before finalizing it as manuscript evidence.

### 2026-06-06 - Replicate sign/DW noise figure and add robust DW

- Request or goal: check the KnowledgeVault synthesis figure on sign
  restrictions and noise, replicate it, add the robust-DW set, and show the
  new figure.
- Files changed: `manuscript/simulations/sign_dw_robust_noise_figure.py`,
  `manuscript/simulations/sign_dw_robust_noise_figure.md`,
  `manuscript/figures/fig_sign_dw_robust_noise_comparison.png`, planning
  surfaces, logs, and M0016 transparency files.
- Summary of work: read the KnowledgeVault synthesis and visualization source,
  rebuilt the sign/standard-DW population noise visualization in the
  manuscript workspace, added a robust-DW normalized higher-cumulant panel
  under Gaussian residual noise, and recorded the output as a candidate figure.
- Next recommended action: run M28 population-grid verification before
  promoting the figure to final manuscript evidence.

### 2026-06-06 - Audit M35 simulation triage

- Request or goal: continue with the next task in goal mode after M35.
- Files changed: `manuscript/simulations/m35_jtest_monte_carlo_triage.py`,
  `manuscript/simulations/m35_jtest_monte_carlo_triage.md`,
  `manuscript/simulations/output/m35_jtest_monte_carlo_summary.json`,
  `manuscript/simulations/m30_m35_triage_audit.md`, planning surfaces, logs,
  and M0015 transparency files.
- Summary of work: selected M30, audited the M35 script and output, found that
  the original moderate-noise case was near a structural-coordinate rescaling
  exception, patched the script to report that diagnostic and add an
  anisotropic diagonal-noise stress case, and documented why the screen remains
  exploratory only.
- Next recommended action: start M28 population-grid verification before any
  final finite-sample Monte Carlo tables.

### 2026-06-06 - Run M35 early J-test Monte Carlo triage

- Request or goal: pick the next open task from the board and work on it in
  goal mode.
- Files changed: `manuscript/simulations/m35_jtest_monte_carlo_triage.py`,
  `manuscript/simulations/m35_jtest_monte_carlo_triage.md`,
  `manuscript/simulations/output/m35_jtest_monte_carlo_summary.json`,
  `manuscript/simulations/README.md`, `manuscript/task-board.md`,
  `manuscript/project-dashboard.md`, `manuscript/source-packet.md`,
  `manuscript/workplan.md`, `manuscript/formal-object-registry.json`, logs,
  and M0014 transparency files.
- Summary of work: selected M35, created a lightweight standard-DW versus
  robust-DW screening script, ran 80 replications for no-noise, moderate-noise,
  and weak-moment scenarios, and recorded that the first screen is useful but
  too permissive for polished evidence.
- Next recommended action: audit the M35 script/statistic in M30, then run M28
  population-grid checks before final finite-sample tables.

### 2026-06-06 - Update scope and derive standard DW J-test result

- Request or goal: record the new scope and evidence notes, update the plan and
  tasks, then continue with the next manuscript task.
- Files changed: `manuscript/paper-plan.md`, `manuscript/paper-map.md`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/source-packet.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/derivations/standard-dw-j-test-under-noise.md`, logs, and M0013
  transparency files.
- Summary of work: narrowed the first paper to the simultaneous SVAR impact
  model, added an early Monte Carlo triage gate after analytical J-test
  inversion, and completed M25 with a working derivation of standard-DW
  covariance-whitened J-test behavior under residual noise.
- Next recommended action: run M35, a small overview Monte Carlo for
  standard-DW versus robust-DW J-test inversion behavior, before polishing
  figures or expanding the replication package.

### 2026-06-06 - Audit robust DW derivation

- Request or goal: pick the next manuscript task after the updated paper plan
  and work on it.
- Files changed: `manuscript/derivations/dw-noise-robust-moments.md`,
  `manuscript/review-log.md`, `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/decision-log.md`, logs, and M0012
  transparency files.
- Summary of work: selected M24 and audited the robust DW higher-moment
  derivation. The cumulant algebra, fourth-cumulant covariance subtractions,
  second-moment exclusion, Gaussian-noise condition, and local-rank calculation
  passed conditionally; scale normalization, global aliases, and finite-sample
  claims remain caveated.
- Next recommended action: run M25 by proving or weakening the standard-DW
  asymptotic-empty claim under residual-noise misspecification.

### 2026-06-06 - Pivot active plan to robust DW comparison

- Request or goal: completely update the manuscript plan around the new robust
  DW paper structure and remove the previous constructive route from active
  planning surfaces.
- Files changed: `knowledge-vault-link.json`, `manuscript/source-packet.md`,
  `manuscript/paper-plan.md`, `manuscript/paper-map.md`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/literature-search.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`, logs, and M0011
  transparency files.
- Summary of work: rewrote the active plan as a noisy sign-set warning plus
  standard-DW versus robust-DW robustness-check paper, with Monte Carlo
  evidence and no application in the first version.
- Next recommended action: audit the robust DW derivation and prove or weaken
  the standard-DW misspecification/empty-set claim before drafting polished
  prose.

### 2026-06-06 - Derive DW-like Gaussian-noise higher moments

- Request or goal: create a new derivation file for a
  Drautzburg-Wright-like approach robust to additive noise.
- Files changed: `manuscript/derivations/dw-noise-robust-moments.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/paper-plan.md`,
  `manuscript/paper-map.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, logs, and M0010 transparency files.
- Summary of work: derived a Gaussian-noise higher-cumulant system that
  searches over normalized impact matrices rather than covariance-whitened
  rotations, writes the third and fourth cumulant restrictions as
  GMM-style moment equations, shows why second moments remain contaminated by
  noise, and gives bivariate local-rank conditions.
- Next recommended action: run an adversarial audit of the DW-like route before
  promoting it from working derivation to the active constructive result.

### 2026-06-05 - Formal object typography rule

- Request or goal: revise the manuscript writing rules for formal statements
  and proofs.
- Files changed: `manuscript/manuscript-rules.md`,
  `manuscript/user-input-log.md`, `manuscript/decision-log.md`,
  `manuscript/session-log.md`, `manuscript/codex-log.md`.
- Summary of work: replaced visible formal-object end markers with full-block
  italics for assumptions, definitions, propositions, lemmas, corollaries, and
  theorems; set proofs to start with `Proof:` and end with `□`.
- Next recommended action: apply the rule when formal objects are added to
  `draft.md`.

### 2026-06-05 - Initialize manuscript repository

- Request or goal: initialize a standalone manuscript from the KnowledgeVault
  proposal on noise-robust sign-restricted SVARs and prepare a careful writing
  plan and task sequence.
- Files changed: `knowledge-vault-link.json`, `bibliography/references.bib`,
  `manuscript/source-packet.md`, `manuscript/paper-plan.md`,
  `manuscript/paper-map.md`, `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/literature-search.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`, and logs.
- Summary of work: validated the KnowledgeVault checkout, initialized metadata,
  read the proposal and related source cluster, revised the initial structure
  into a shorter theory-and-simulation plan, listed core formal objects, copied
  a first verified bibliography snapshot, and created next tasks.
- Next recommended action: write exact formal statements and proof obligations
  for the noisy pseudo-set, no-noise independence refinement failure, the
  profiled cumulant inversion, and mapped noise diagnostic.

### 2026-06-05 - Revise Bonhomme-Robin verification plan

- Request or goal: update the manuscript plan after corrected KnowledgeVault
  notes on Bonhomme-Robin and noisy ICA.
- Files changed: `knowledge-vault-link.json`, `manuscript/source-packet.md`,
  `manuscript/paper-plan.md`, `manuscript/paper-map.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/literature-search.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`, and logs.
- Summary of work: revised the plan so the constructive BR component is a
  verified bivariate profiled cumulant inversion rather than a direct import
  of the original BR theorem; added analytic derivation, simulation
  verification, and adversarial review tasks.
- Next recommended action: write the bivariate cumulant derivation and run the
  first adversarial derivation audit before drafting Section 4.

### 2026-06-05 - Close stale M0005 task state

- Request or goal: complete the next open project task by finishing the stale
  M21 transparency cleanup.
- Files changed: `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/session-log.md`,
  `manuscript/codex-log.md`, and M0006 transparency files.
- Summary of work: verified that M0005 is closed, committed, tagged at
  `manuscript-milestones/M0005-revise-br-verification-plan`, aligned with
  remote `main`, and closed on GitHub; marked M21 done and cleared the stale
  active milestone note.
- Next recommended action: open a substantive milestone for M05 and derive the
  corrected bivariate cumulant map from scratch.

### 2026-06-05 - Derive bivariate cumulant map

- Request or goal: continue to the next project task, M05.
- Files changed: `manuscript/derivations/bivariate-cumulant-map.md`,
  `manuscript/formal-object-registry.json`, `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`,
  `manuscript/session-log.md`, `manuscript/codex-log.md`, and M0007
  transparency files.
- Summary of work: derived the full second-, third-, and fourth-order cumulant
  map for `u_t = B(a,b) epsilon_t + eta_t`, including nuisance diagonal noise
  cumulants and clean-versus-nuisance moment classifications.
- Next recommended action: run the M06 adversarial derivation audit before
  using the cumulant map in a draft result or local identification proof.

### 2026-06-05 - Audit bivariate cumulant map

- Request or goal: continue with M06.
- Files changed: `manuscript/derivations/bivariate-cumulant-map.md`,
  `manuscript/review-log.md`, `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/session-log.md`,
  `manuscript/codex-log.md`, and M0008 transparency files.
- Summary of work: adversarially checked the cumulant derivation for indices,
  cumulant definitions, normalization, missing moments, and clean-versus-
  nuisance classifications. No coefficient/index errors were found; the audit
  corrected wording so clean third mixed cumulants are not overstated as
  identifying restrictions after unrestricted `gamma` profiling.
- Next recommended action: start M07 by documenting what the Bonhomme-Robin
  analogy does and does not justify for the bivariate `L=K=2` case.

### 2026-06-05 - Clarify Bonhomme-Robin applicability

- Request or goal: continue with M07.
- Files changed: `manuscript/derivations/br-applicability.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/paper-map.md`,
  `manuscript/review-log.md`, `manuscript/session-log.md`,
  `manuscript/codex-log.md`, and M0009 transparency files.
- Summary of work: documented why the original Bonhomme-Robin quasi-JADE
  theorem does not directly apply to the bivariate `L=K=2` SVAR: independent
  bivariate errors provide only one clean pair, so the all-kurtotic rank
  condition cannot hold, and the skewness route does not cover two factors
  when `L=2`. Defined the manuscript object as a BR-style profiled inversion.
- Next recommended action: run M08 by attacking this applicability argument
  before deriving profiled criteria in M09.
