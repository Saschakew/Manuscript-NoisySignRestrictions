# Codex Log

Purpose: shareable milestone-level transparency log for Codex work on this
manuscript.

Do not record every micro-edit here. Use this file for substantial Codex-led
work, visible milestones, checks run, and open uncertainties.

Every entry that closes a substantive work block should correspond to a
machine-readable milestone in `transparency/milestones/`.

## Entries

### 2026-06-09 - M0048 M49 DW source audit

- Request: user asked Codex to continue the manuscript work and go on with M49.
- Actions taken: opened M0048; read the M49 packet, draft, registry, M48
  warning note, raw Drautzburg-Wright source, KnowledgeVault note, robust
  derivation, standard-DW proof note, and Figure 1/M45 code; created
  `manuscript/derivations/m49-dw-source-and-noisy-moment-audit.md`; corrected
  the draft's Section 3 source menu; flagged the evidence section as
  historical hybrid evidence; marked M49 done; created packet-backed M52.
- Files changed: M49 audit note, M52 task packet, draft, source packet,
  dashboard, paper map, task board, workplan, formal registry, citation
  provenance, and human-readable logs/transparency files.
- Checks run: `python -m json.tool manuscript/formal-object-registry.json`
  passed; `python scripts/check_manuscript.py` passed with the expected
  open-milestone warning before closure; `git diff --check` passed with
  line-ending warnings only. A clean post-close manuscript check also passed.
- Open uncertainties: M52 must rebuild the standard-DW figures and Monte Carlo
  with a source-correct GMM1 or GMM2 menu. A full unit-variance/rotation-chart
  migration remains a user-decision gate.

### 2026-06-09 - M0047 Clarify next-task workflow

- Request: user asked Codex to improve the task workflow so common prompts
  like "work on next task" and "plan next tasks" use task packets properly.
- Actions taken: opened M0047 and GitHub milestone 43; added explicit
  next-task selection and task-planning algorithms to the local
  `write-standalone-manuscript` skill; updated the task-packet workflow
  reference and manuscript rules; recorded M51 as a completed workflow task.
- Files changed: local manuscript skill, task-packet workflow reference,
  manuscript rules, task board, dashboard, workplan, and logs/transparency
  files.
- Checks run: skill `quick_validate.py` passed; `python
  scripts\check_manuscript.py` passed with the expected open-milestone warning
  before closure and passed cleanly after closure; `python -m json.tool
  manuscript\formal-object-registry.json`, `python -m json.tool
  manuscript\transparency\milestones\M0047-clarify-next-task-workflow.json`,
  and `python -m json.tool manuscript\transparency\timeline.json` passed; `git
  diff --check` passed with line-ending warnings only.
- Open uncertainties: M49 itself remains unexecuted; the next-task workflow
  now directs agents to execute its packet first.

### 2026-06-09 - M0046 Improve task hand-off workflow

- Request: user asked Codex to improve task creation and task management after
  discussing that bad hand-offs may have contributed to poor scientific
  performance.
- Actions taken: opened M0046 and GitHub milestone 42; added task-packet
  workflow rules to the local `write-standalone-manuscript` skill and
  manuscript rules; created
  `.codex/skills/write-standalone-manuscript/references/task-packet-workflow.md`;
  created `manuscript/tasks/_template.md`; created
  `manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md`; updated the task
  board, dashboard, paper map, workplan, and formal registry so M49 is
  executed from the packet.
- Files changed: skill files, manuscript rules, `manuscript/tasks/`, planning
  surfaces, registry, human-readable logs, and M0046 transparency files.
- Checks run: skill `quick_validate.py` passed; `python scripts\check_manuscript.py` passed with the expected open-milestone warning before closure and passed cleanly after closure; `python -m json.tool manuscript\formal-object-registry.json`, `python -m json.tool manuscript\transparency\milestones\M0046-improve-task-handoff-workflow.json`, and `python -m json.tool manuscript\transparency\timeline.json` passed; `git diff --check` passed with line-ending warnings only.
- Open uncertainties: M49 itself is still unexecuted; the packet is the
  hand-off contract for the next scientific audit.

### 2026-06-09 - M0045 Harden scientific workflow

- Request: user criticized the M48 output as insufficient and asked Codex to
  carefully update workflows and skills first.
- Actions taken: opened M0045 and GitHub milestone 41; added a scientific
  claim gate to the local `write-standalone-manuscript` skill and manuscript
  rules; created `references/scientific-claim-audit.md`; quarantined M48 in
  the dashboard, paper map, task board, formal registry, review log, draft
  TODO note, and M48 derivation note; added M49 as the required source-first
  DW audit before M47.
- Files changed: `.codex/skills/write-standalone-manuscript/SKILL.md`,
  `.codex/skills/write-standalone-manuscript/references/scientific-claim-audit.md`,
  `manuscript/manuscript-rules.md`, `manuscript/draft.md`,
  `manuscript/derivations/m48-dw-moment-normalization-audit.md`, planning
  surfaces, registry, human-readable logs, and M0045 transparency files.
- Checks run: `python C:\Users\smsakewe\.codex\skills\.system\skill-creator\scripts\quick_validate.py .codex\skills\write-standalone-manuscript` passed; `python scripts\check_manuscript.py` passed with the expected open-milestone warning before closure and passed cleanly after closure; `git diff --check` passed with line-ending warnings only.
- Open uncertainties: M49 must still read the raw DW source or KnowledgeVault
  note and derive the requested noisy product moments before Section 3/4 claims
  or figure/Monte Carlo rebuild decisions are trusted.

### 2026-06-09 - M48 DW moment-normalization audit

- Request: work on the manuscript in goal mode and pick the next task.
- Actions taken at the time: selected M48, opened M0044, created GitHub
  milestone 40, wrote
  `manuscript/derivations/m48-dw-moment-normalization-audit.md`, attempted to
  correct Section 3 away from fourth-cumulant language, and updated
  planning/provenance surfaces.
- Files changed: `manuscript/derivations/m48-dw-moment-normalization-audit.md`,
  `manuscript/draft.md`, `manuscript/project-dashboard.md`,
  `manuscript/paper-map.md`, `manuscript/task-board.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/workplan.md`, logs, and
  the M0044 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed.
- M0045 correction: this entry is now historical only. M48 is partial and
  source-insufficient; do not rely on it as a completed DW source audit, a
  Figure 1 source-match proof, or a normalization/no-rebuild decision.
- Open uncertainties: M49 must redo the DW source and noisy moment audit before
  M47 audits the standard-DW generic emptying proof.

### 2026-06-08 - M0043 Track DW moment comments

- Request: user asked Codex to insert a task for comments questioning the
  Section 3 standard-DW fourth-order cumulant wording, asking how Figure 1
  computes DW moments, suggesting possible unit structural-shock variance
  normalization, and requesting explicit noisy Section 4 moment derivations.
- Actions taken: opened local transparency milestone M0043; checked the Figure
  1 script enough to see that the standard-DW row uses raw standardized product
  moments through `MOMENTS_DW = ((1,1),(2,1),(1,2),(2,2))`, while the robust row
  computes mixed cumulants; added M48 to the task board; and updated the
  dashboard, paper map, and user-input log to keep the issue visible.
- Files changed: `manuscript/task-board.md`,
  `manuscript/project-dashboard.md`, `manuscript/paper-map.md`,
  `manuscript/user-input-log.md`, human-readable logs, and M0043 transparency
  files.
- Checks run: `python scripts/check_manuscript.py` passed.
- Open uncertainties: M48 still needs the actual DW source check, full noisy
  moment derivations, normalization decision, and any figure or Monte Carlo
  rebuilds. The GitHub issue milestone was not created because `gh` is not
  available locally and the visible GitHub connector has no milestone tool.

### 2026-06-08 - M0042 M34 adversarial review

- Request: user logged in to GitHub CLI, asked Codex to finish the GitHub
  milestone issue, and then proceed with M34.
- Actions taken: created closed GitHub milestone #38 for the previously closed
  M0041 revision-comments work; opened local transparency milestone M0042 and
  GitHub milestone #39 for M34; reviewed the revised draft, M40 screen audit,
  M45 evidence, formal registry, and planning surfaces; tightened visible
  variance-ratio terminology; softened simulation claims in the abstract;
  added a skewed-residual-noise stress-case caveat; updated citation
  provenance to M45; drafted the conclusion; and recorded M34 findings in the
  review log.
- Files changed: `manuscript/draft.md`, `manuscript/review-log.md`,
  `manuscript/task-board.md`, `manuscript/project-dashboard.md`,
  `manuscript/paper-map.md`, `manuscript/workplan.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`,
  `manuscript/writing-feedback-log.md`, human-readable logs, and M0041/M0042
  transparency files.
- Checks run: final manuscript checks are run before closing M0042.
- Open uncertainties: Proposition 2 still depends on the M25 proof audit; M45
  remains lightweight evidence; the final figure/table rebuild path still
  needs M33; References and export cleanup remain open.

### 2026-06-08 - M0041 Incorporate revision comments

- Request: user asked Codex to inspect the new revision, address many comments
  on formulation and writing style, rewrite the abstract, introduction, and
  Sections 2-4 step by step, and review the result against the spirit of the
  comments.
- Actions taken: opened local transparency milestone M0041; found the revision
  via GitHub issue #1 and branch `Revision-20260608-070142`; extracted the
  inline comments from the branch draft; rewrote the abstract, introduction,
  and Sections 2-4 around SVAR-reader language; added the explicit no-noise
  sign-set J-test equation `eq:no-noise-sign-j-set`; updated the formal
  registry, paper map, dashboard, task board, and human-readable logs.
- Files changed: `manuscript/draft.md`,
  `manuscript/formal-object-registry.json`, `manuscript/paper-map.md`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/user-input-log.md`, `manuscript/decision-log.md`,
  `manuscript/session-log.md`, `manuscript/codex-log.md`, and M0041
  transparency files.
- Checks run: final manuscript checks are run before closing M0041.
- Open uncertainties: the M25 standard-DW proof audit remains open, and the
  final shareable replication wrapper is still needed. The revision also
  suggested a possible separate sign-flip figure; the current draft addresses
  the sign-flip mechanism in prose and uses Figure 1 for continuous set
  movement, leaving the standalone sign-flip design as future optional work.

### 2026-06-07 - M0040 Rebuild variance-ratio figures and evidence

- Request: user asked Codex to follow the proposed next actions: M42 math
  cleanup, M43 Figure 2 update, M44 Figure 3 sample-size grid, and M45
  validation/Monte Carlo rebuild for the variance-ratio proposal.
- Actions taken: opened local transparency milestone M0040 and GitHub
  milestone #37; cleaned math delimiters in `manuscript/draft.md`; patched and
  regenerated Figure 2 with the `relative` robust row; added and rendered the
  Figure 3 sample-size grid; created and ran
  `manuscript/simulations/m45_variance_ratio_evidence.py`; updated the draft,
  formal registry, planning surfaces, source packet, and logs.
- Files changed: `manuscript/draft.md`, figure scripts and notes,
  `manuscript/figures/fig_sign_dw_robust_nongaussianity_grid.png`,
  `manuscript/figures/fig_sign_dw_sample_size_robust_grid.png`,
  `manuscript/simulations/m45_variance_ratio_evidence.md`,
  `manuscript/simulations/output/m45_variance_ratio_evidence.json`,
  planning/control files, logs, and M0040 transparency files.
- Checks run: figure scripts completed; M45 evidence script completed;
  `python -m json.tool manuscript/formal-object-registry.json` passed. Final
  manuscript checks are run before milestone closure.
- Open uncertainties: M45 is a lightweight evidence gate, not the final
  replication package. M25 still needs proof audit, and M34 should review the
  full figure-led logic before polishing final theorem/evidence wording.

### 2026-06-07 - M0039 Audit variance-ratio robust DW screen

- Request: user asked Codex to work on the manuscript in goal mode, pick the
  next task, and complete a substantive manuscript work block.
- Actions taken: selected M40; opened local transparency milestone M0039 and
  GitHub milestone #36; created
  `manuscript/derivations/m40-variance-ratio-robust-dw-screen-audit.md`;
  checked the relative covariance-screen algebra and implementation; ran a
  250-draw repeated-screen sanity check at the true `B0`; updated the draft,
  formal registry, planning surfaces, and logs.
- Files changed: the new M40 audit note,
  `manuscript/derivations/dw-noise-robust-moments.md`,
  `manuscript/simulations/sign_dw_relative_noise_robust_grid_figure.md`,
  `manuscript/draft.md`, `manuscript/formal-object-registry.json`, project
  planning/control files, logs, and M0039 transparency files.
- Checks run: `python -m json.tool manuscript/formal-object-registry.json`
  passed; `git diff --check` passed with line-ending warnings only;
  `python scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning and passed cleanly after closure.
- Open uncertainties: M25 still needs to audit the standard-DW proof gate, and
  M43-M45 still need to rebuild Figure 2, add Figure 3, and rerun validation
  and Monte Carlo evidence for the variance-ratio robust DW proposal.

### 2026-06-07 - M0038 Sketch Sections 2-4 formulas

- Request: user asked Codex to work on the manuscript in goal mode, pick the
  next task, and complete a substantive work block.
- Actions taken: selected M41; opened local transparency milestone M0038 and
  GitHub milestone #35; drafted formula-first Sections 2-4 for the noisy sign
  pseudo-set, standard-DW misspecification sketch, and variance-ratio robust DW
  proposal; updated the formal registry, planning surfaces, and logs.
- Files changed: `manuscript/draft.md`,
  `manuscript/formal-object-registry.json`, project planning/control files,
  logs, and M0038 transparency files.
- Checks run: `python -m json.tool manuscript/formal-object-registry.json`
  passed; `git diff --check` passed with line-ending warnings only;
  `python scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning and passed cleanly after closure.
- Open uncertainties: the M25 standard-DW proof audit and M40 variance-ratio
  screen audit still block theorem-level prose and evidence rebuilds.

### 2026-06-06 - M0037 Plan variance-ratio proposal

- Request: user accepted the variance-ratio bound as the good solution and
  asked to update only the paper plan and future tasks, not to draft Sections
  2-4 or generate figures yet.
- Actions taken: opened local transparency milestone M0037 and GitHub
  milestone #34; updated the project dashboard, source packet, paper plan,
  paper map, workplan, task board, formal registry, decision log, user input
  log, and session log so M0036 variance-ratio robust DW is the active
  proposal.
- Files changed: planning/control surfaces, formal registry, human-readable
  logs, and M0037 transparency files.
- Checks run: `git diff --check` passed with line-ending warnings only;
  `python scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning and passed cleanly after closure; `python -m
  json.tool manuscript/formal-object-registry.json` passed.
- Open uncertainties: M40 still needs to audit the variance-ratio screen; M41
  must sketch Sections 2-4 with formulas; M42 must clean manuscript math
  delimiters; M43/M44 must rebuild Figure 2 and add Figure 3; M45 must rebuild
  validation and Monte Carlo evidence.

### 2026-06-06 - M0036 Relative-noise covariance figure

- Request: user corrected the absolute bounded-noise screen and asked to bound
  residual noise relative to structural-shock variance, then show Figure 1.
- Actions taken: opened local transparency milestone M0036 and GitHub
  milestone #33; added `--robust-mode relative` to the Figure 1 script;
  implemented the profiled covariance-decomposition screen
  `0 <= nu_i <= 0.5 Var(epsilon_i)`; rendered
  `fig_sign_dw_relative_noise_robust_grid.png`; documented fixed-draw
  diagnostics; updated draft, registry, planning surfaces, provenance, figure
  indexes, simulation notes, and logs; and made M40 the audit gate for the
  signal-to-noise restriction.
- Files changed: `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/simulations/sign_dw_relative_noise_robust_grid_figure.md`,
  `manuscript/figures/fig_sign_dw_relative_noise_robust_grid.png`, manuscript
  control surfaces, logs, and M0036 transparency files.
- Checks run: rendered default, pure, bounded, and relative Figure 1 modes;
  visually inspected the relative image; `git diff --check` passed with
  line-ending warnings only; `python scripts/check_manuscript.py` passed before
  closure with the expected open-milestone warning and passed cleanly after
  closure; `python -m json.tool manuscript/formal-object-registry.json` passed.
- Open uncertainties: the relative row is scale-correct compared with the
  absolute M0035 bound, but its precision still depends on the substantive 50
  percent signal-to-noise bound. M40 must audit the algebra, finite-sample
  screen, and interpretability before M28/M29 are rebuilt.

### 2026-06-06 - M0035 Bounded-noise covariance figure

- Request: user suggested profiling unknown diagonal residual-noise variances
  in `E[e1 e2]` with an upper bound of 0.5 and asked how Figure 1 looks.
- Actions taken: opened local transparency milestone M0035 and GitHub
  milestone #32; derived the bounded recovered-covariance screen; added
  `--robust-mode bounded` to the Figure 1 script; rendered
  `fig_sign_dw_bounded_noise_robust_grid.png`; documented fixed-draw
  diagnostics; updated planning surfaces, registry, provenance, and logs; and
  added M40 as the audit gate.
- Files changed: `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/simulations/sign_dw_bounded_noise_robust_grid_figure.md`,
  `manuscript/figures/fig_sign_dw_bounded_noise_robust_grid.png`, manuscript
  control surfaces, logs, and M0035 transparency files.
- Checks run: rendered default, pure, and bounded Figure 1 modes; `git diff
  --check` passed with line-ending warnings only; `python
  scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning and passed cleanly after closure; `python -m
  json.tool manuscript/formal-object-registry.json` passed.
- Open uncertainties: the bounded row is promising but depends on a
  substantive `0 <= nu_i <= 0.5` assumption; M40 must audit the algebra,
  finite-sample inequality screen, and interpretability before M28/M29 are
  rebuilt.

### 2026-06-06 - M0034 Pure robust Figure 1

- Request: user corrected the robust-DW moment algebra and asked to see Figure
  1 without the invalid covariance anchor.
- Actions taken: opened local transparency milestone M0034 and GitHub
  milestone #31; added a `--robust-mode pure` option to the Figure 1 script;
  rendered `fig_sign_dw_pure_robust_noise_grid.png`; computed fixed-draw
  diagnostics; updated planning surfaces, registry entries, provenance, and
  logs so M0030/M37 diagonal-anchor evidence is marked superseded.
- Files changed: `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/simulations/sign_dw_pure_robust_noise_grid_figure.md`,
  `manuscript/figures/fig_sign_dw_pure_robust_noise_grid.png`, manuscript
  control surfaces, logs, and M0034 transparency files.
- Checks run: rendered both the pure and default Figure 1 modes; `git diff
  --check` passed with line-ending warnings only; `python
  scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning and passed cleanly after closure; `python -m
  json.tool manuscript/formal-object-registry.json` passed.
- Open uncertainties: M39 must decide whether the paper uses the pure
  higher-cumulant robust set, a valid explicit scale model, or a narrower
  diagnostic claim, and then rerun the visual/Monte Carlo evidence.

### 2026-06-06 - M0033 M32 literature positioning

- Request: user asked Codex to work on the manuscript, pick the next task, and
  work in goal mode.
- Actions taken: selected M32 from the task board; opened local transparency
  milestone M0033 and GitHub milestone #30; drafted introduction subsection
  1.1; updated citation provenance, literature-search status, dashboard,
  paper plan, paper map, workplan, task board, user input log, decision log,
  and session log.
- Files changed: `manuscript/draft.md`, `manuscript/citation-provenance.md`,
  planning/literature/log surfaces, and M0033 transparency files.
- Checks run: `git diff --check` passed with line-ending warnings only;
  `python scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning; M0033 and timeline JSON validation passed; `python
  scripts/check_manuscript.py` passed after closure.
- Open uncertainties: Sections 2-4 remain TODO prose scaffolds; the M25
  standard-DW proof audit remains open before theorem-level wording; final
  sharing still requires a `manuscript/replication/` wrapper.

### 2026-06-06 - M0032 Diagonal-noise robust estimator audit

- Request: user asked Codex to work on the manuscript, pick the next task, and
  work in goal mode.
- Actions taken: selected M37 from the task board; opened local transparency
  milestone M0032 and GitHub milestone #29; audited the off-diagonal covariance
  anchor, diagonal-variance profiling, mixed higher-cumulant stack, `chi2_6`
  cutoff convention, and fallback language; created
  `manuscript/derivations/m37-diagonal-noise-robust-estimator-audit.md`;
  updated registry, planning surfaces, task board, review log, and human logs.
- Files changed: derivation/audit notes, planning/control surfaces, logs, and
  M0032 transparency files.
- Checks run: `python -m json.tool manuscript/formal-object-registry.json`
  passed; `git diff --check` passed with line-ending warnings only; `python
  scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning and passed cleanly after closure.
- Open uncertainties: M25 standard-DW proof audit remains open; final
  replication wrappers still need to move figure/table code under
  `manuscript/replication/`.

### 2026-06-06 - M0031 Plan alignment with new estimator

- Request: user asked to ensure the paper plan and next tasks are fully aligned
  with the new diagonal-noise robust DW estimator, without making unnecessary
  edits.
- Actions taken: opened M0031 and GitHub milestone #28; audited
  `paper-plan.md`, `paper-map.md`, `project-dashboard.md`, `workplan.md`, and
  `task-board.md`; corrected active wording from the older pure
  higher-cumulant route to the diagonal-noise robust DW set where needed; added
  M37 as the direct post-M0030 estimator audit before theorem-level prose.
- Files changed: planning/control surfaces, logs, and M0031 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed after edits.
- Open uncertainties: M37 still needs to audit the off-diagonal covariance
  anchor, diagonal-variance profiling, higher-cumulant stack, cutoff degrees
  of freedom, and fallback language before formal theorem wording.

### 2026-06-06 - M0030 High-noise power fix

- Request: user rejected `V=(2,2)`, asked for an investigation of the
  high-noise robust-DW power problem, and suggested considering a robust-DW
  modification that uses second moments while staying robust.
- Actions taken: opened M0030 and GitHub milestone #27; diagnosed the pure
  higher-cumulant power failure; implemented the diagonal-noise robust statistic
  using the off-diagonal covariance anchor plus mixed higher cumulants; lowered
  the high-noise grid column to `V=(0.5,0.5)`; regenerated both figures; reran
  M28 validation and a refreshed M29 Monte Carlo pass; updated draft prose,
  derivation notes, registry, source packet, dashboard, task board, paper map,
  simulation notes, and logs.
- Files changed: `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`,
  figure PNGs, M28/M29 scripts and outputs, `manuscript/draft.md`,
  derivation/diagnostic notes, planning surfaces, logs, and M0030 transparency
  files.
- Checks run: figure scripts passed; `m28_grid_story_validation.py` passed;
  `m29_calibrated_monte_carlo.py --calibration-reps 120 --evaluation-reps 60
  --bootstrap-reps 20 --grid-points 41` passed. Final manuscript checks are run
  before closing M0030.
- Open uncertainties: the diagonal-noise covariance anchor depends on diagonal
  residual-noise covariance. If the paper later allows unrestricted Gaussian
  residual-noise covariance, the reported robust row must revert to the pure
  higher-cumulant object or add new valid covariance restrictions.

### 2026-06-06 - M0029 Figure 1 orientation clarification

- Request: user corrected the Figure 1 interpretation and clarified that the
  residual-noise figure should keep method rows and increasing-noise columns.
- Actions taken: opened M0029; inspected the rendered residual-noise and
  non-Gaussianity figures; restored the residual-noise figure generator and
  PNG to the intended layout after an initial mistaken transpose; recorded the
  clarification in user input and decision logs.
- Files changed: transparency files and logs.
- Checks run: rendered and visually inspected
  `figures/fig_sign_dw_robust_noise_grid.png`; `python
  scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning; `git diff --check` passed with line-ending
  normalization warnings only.
- Open uncertainties: none for Figure 1 orientation. The non-Gaussianity grid
  remains the separate limitation figure.

### 2026-06-06 - M0028 M31 figure-led skeleton

- Request: work on the manuscript in goal mode by picking the next task.
- Actions taken: selected M31 from the task board; opened local transparency
  milestone M0028 and GitHub milestone #25; drafted the abstract,
  introduction, and evidence section around the selected residual-noise grid,
  non-Gaussianity grid, and M29 chi-square-primary Monte Carlo table; updated
  citation provenance, dashboard, paper plan, paper map, task board, workplan,
  user input log, decision log, session log, and Codex log.
- Files changed: `manuscript/draft.md`, planning/provenance surfaces, logs,
  and M0028 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed before closure with
  the expected open-milestone warning and passed again after closure; `git diff
  --check` passed with line-ending normalization warnings only.
- Open uncertainties: sections 2-4 remain prose skeletons, M25 still needs a
  direct proof audit before theorem-level wording, and final sharing still
  requires a `manuscript/replication/` wrapper for figures and tables.

### 2026-06-06 - M0027 larger M29 chi-square-primary table

- Request: work on the manuscript in goal mode by picking the next task.
- Actions taken: selected the active M29 follow-up; opened local transparency
  milestone M0027 and GitHub milestone #24; benchmarked the M29 simulation
  functions; ran the larger M29 Monte Carlo with 240 calibration replications,
  120 evaluation replications, 40 truth-bootstrap replications per evaluation
  sample, and a 41-by-41 grid; updated the M29 note labels, simulation index,
  dashboard, paper plan, paper map, source packet, task board, workplan,
  formal registry, user input log, decision log, review log, session log, and
  Codex log.
- Files changed: M29 simulation script and outputs, planning surfaces, logs,
  and M0027 transparency files.
- Checks run: M29 function timing smoke checks passed; larger M29 command
  passed; `python -m py_compile
  manuscript\simulations\m29_calibrated_monte_carlo.py` passed; formal
  registry and M29 output JSON parse passed; `python scripts/check_manuscript.py`
  passed with the expected open-milestone warning before closure; `git diff
  --check` passed with line-ending normalization warnings only.
- Open uncertainties: the evidence is ready for a first figure-led draft, but
  final sharing still requires a `manuscript/replication/` wrapper and the M25
  standard-DW derivation still needs direct proof audit before theorem-level
  prose.

### 2026-06-06 - M0026 M29 chi-square cutoff convention

- Request: user clarified that standard DW should use the standard chi-square
  critical values because those are the values an applied researcher would use
  if unaware of residual noise.
- Actions taken: opened local transparency milestone M0026 and GitHub
  milestone #23; updated the M29 note generator and regenerated the M29
  Markdown/JSON outputs so chi-square rows are the primary applied benchmark;
  updated the dashboard, task board, paper plan, paper map, source packet,
  workplan, formal registry, simulation index, draft notes, user input log,
  decision log, review log, session log, and Codex log.
- Files changed: M29 simulation script and outputs, planning surfaces, logs,
  draft notes, and M0026 transparency files.
- Checks run: `python -m py_compile
  manuscript\simulations\m29_calibrated_monte_carlo.py` passed;
  `python manuscript\simulations\m29_calibrated_monte_carlo.py` passed;
  formal registry JSON parse passed; `python scripts\check_manuscript.py`
  passed.
- Open uncertainties: M29 still needs a larger chi-square-primary run before
  final coverage-style table values are draft-level evidence.

### 2026-06-06 - M0025 M29 truth-bootstrap expansion

- Request: work on the manuscript in goal mode by picking the next task.
- Actions taken: selected the active M29 follow-up; opened local transparency
  milestone M0025 and GitHub milestone #22; added a truth-point
  residual-bootstrap cutoff convention to
  `manuscript/simulations/m29_calibrated_monte_carlo.py`; ran a smoke test and
  the default expanded Monte Carlo; regenerated
  `manuscript/simulations/m29_calibrated_monte_carlo.md` and
  `manuscript/simulations/output/m29_calibrated_monte_carlo.json`; updated the
  dashboard, paper plan, paper map, source packet, task board, workplan,
  formal registry, simulation index, review log, decision log, session log,
  and Codex log.
- Files changed: M29 simulation script, M29 Markdown and JSON outputs,
  planning surfaces, logs, and M0025 transparency files.
- Checks run: `python -m py_compile
  manuscript\simulations\m29_calibrated_monte_carlo.py` passed; smoke test
  passed; `python manuscript\simulations\m29_calibrated_monte_carlo.py`
  passed with 80 calibration replications, 24 evaluation replications, 40
  truth-bootstrap replications per evaluation sample, and a 41-by-41 grid;
  formal registry JSON parse passed; `python scripts/check_manuscript.py`
  passed.
- Open uncertainties: M29 is still not final. The truth bootstrap is an oracle
  calibration-cost audit because it uses true `B0` and can make robust sets
  nearly uninformative. The next M29 step is a larger final run and a defensible
  calibration convention.

### 2026-06-06 - M0024 M29 calibrated Monte Carlo first pass

- Request: work on the manuscript in goal mode by picking the next task.
- Actions taken: selected M29 from the task board; opened local transparency
  milestone M0024 and GitHub milestone #21; implemented
  `manuscript/simulations/m29_calibrated_monte_carlo.py`; ran a smoke test and
  the default first-pass Monte Carlo; wrote
  `manuscript/simulations/m29_calibrated_monte_carlo.md` and
  `manuscript/simulations/output/m29_calibrated_monte_carlo.json`; updated the
  simulation index, dashboard, paper plan, paper map, source packet, task
  board, workplan, formal registry, review log, decision log, session log, and
  Codex log.
- Files changed: M29 simulation script, M29 Markdown and JSON outputs,
  planning surfaces, logs, and M0024 transparency files.
- Checks run: `python -m py_compile
  manuscript\simulations\m29_calibrated_monte_carlo.py` passed; smoke test
  passed; `python manuscript\simulations\m29_calibrated_monte_carlo.py`
  passed with 80 calibration replications, 24 evaluation replications, and a
  41-by-41 grid.
- Open uncertainties: this is a first calibrated pass. M29 still needs design
  audit and a larger or bootstrap-calibrated run before final coverage, width,
  empty-set, overlap, and divergence claims.

### 2026-06-06 - M0023 M27 diagnostic formalization

- Request: work on the manuscript in goal mode by picking the next task.
- Actions taken: selected M27 from the task board; opened local transparency
  milestone M0023 and GitHub milestone #20; created
  `manuscript/derivations/dw-robust-comparison-diagnostic.md`; formalized the
  reported standard-DW set, robust-DW set, critical-value convention, accepted
  shares, Jaccard overlap, directional standard-outside-robust warning metric,
  truth-inclusion simulation diagnostics, and interpretation boundaries;
  updated the registry, paper plan, paper map, dashboard, task board, source
  packet, workplan, draft notes, citation provenance, decision log, session
  log, and Codex log.
- Files changed: `manuscript/derivations/dw-robust-comparison-diagnostic.md`,
  planning surfaces, draft notes, provenance, logs, and M0023 transparency
  files.
- Checks run: formal registry and M0023 manifest JSON parse passed; `python
  scripts/check_manuscript.py` passed with the expected open-milestone warning
  before closure; `git diff --check` passed with line-ending normalization
  warnings only; `python scripts/check_manuscript.py` passed again after
  closing M0023.
- Open uncertainties: M29 still needs calibrated repeated-sample or bootstrap
  critical values before reporting final coverage, width, empty-set, overlap,
  or divergence evidence.

### 2026-06-06 - M0022 M28 grid story validation

- Request: pick the next manuscript task and work on it in goal mode.
- Actions taken: selected M28 from the task board; opened local transparency
  milestone M0022 and GitHub milestone #19; implemented
  `manuscript/simulations/m28_grid_story_validation.py`; ran the M28
  validation; wrote Markdown and JSON outputs; updated the simulation index,
  dashboard, paper map, paper plan, source packet, task board, workplan,
  formal registry, review log, decision log, session log, and Codex log.
- Files changed: `manuscript/simulations/m28_grid_story_validation.py`,
  `manuscript/simulations/m28_grid_story_validation.md`,
  `manuscript/simulations/output/m28_grid_story_validation.json`, planning
  surfaces, logs, and M0022 transparency files.
- Checks run: `python manuscript\simulations\m28_grid_story_validation.py`
  passed. The generated diagnostics support the M0020 visual spine at the
  population/repeated-seed gate: high-noise standard DW rejects true `B0`
  across repeated seeds at the pointwise 10 percent cutoff, robust DW keeps
  true `B0` as a population zero under Gaussian residual noise, and weak or
  Gaussian structural higher moments widen the robust row.
- Open uncertainties: M29 still needs calibrated repeated-sample or bootstrap
  critical values before the manuscript reports coverage, size, width, or
  empty-set frequencies as final evidence.

### 2026-06-06 - M0021 figure-led paper plan

- Request: update the paper plan and next steps because the corrected M0020
  figures tell the paper's main story well.
- Actions taken: promoted the M0020 residual-noise grid and non-Gaussianity
  grid to the selected visual spine; revised the paper plan, paper map,
  dashboard, task board, workplan, source packet, formal registry, figure and
  simulation indexes, and durable logs; reordered next work around M28
  validation, M27 diagnostic formalization, M29 Monte Carlo, and figure-led
  drafting.
- Files changed: `manuscript/paper-plan.md`, `manuscript/paper-map.md`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/source-packet.md`,
  `manuscript/formal-object-registry.json`, `manuscript/figures/README.md`,
  `manuscript/simulations/README.md`, logs, and M0021 transparency files.
- Checks run: stale-language scan of active planning surfaces passed; formal
  registry and M0021 manifest JSON validation passed; `python
  scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning.
- Open uncertainties: the figures are selected as the narrative spine, but
  M28/M29 still need to validate stability, critical values, and finite-sample
  coverage before final evidence claims.

### 2026-06-06 - M0020 J-test grid figures

- Request: make both grid figures invert J tests in all rows, clarify the
  cutoff language, and handle the fact that the previous standard-DW noise
  grid still contained true `B0` under noise.
- Actions taken: corrected
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py` and
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py` so all
  rows invert pointwise 10 percent J tests; replaced the robust population
  score with a finite-sample five-moment mixed higher-cumulant J statistic;
  added true-`B0` inclusion labels; regenerated both figures; updated
  simulation notes, registry, figure/source indexes, dashboard, task board, and
  logs.
- Files changed:
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.md`,
  `manuscript/figures/fig_sign_dw_robust_noise_grid.png`,
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.md`,
  `manuscript/figures/fig_sign_dw_robust_nongaussianity_grid.png`, planning
  surfaces, logs, and M0020 transparency files.
- Checks run: regenerated both corrected figures; `python -m py_compile
  manuscript\simulations\sign_dw_robust_noise_grid_figure.py
  manuscript\simulations\sign_dw_robust_nongaussianity_grid_figure.py`
  passed; fixed-draw diagnostics confirmed high-noise standard DW rejects true
  `B0` while robust DW contains it; formal registry and M0020 manifest JSON
  validation passed; `python scripts/check_manuscript.py` passed before
  closure with the expected open-milestone warning.
- Open uncertainties: these are still candidate visuals; M28/M29 must validate
  population behavior, finite-sample coverage, and calibrated critical values
  before final manuscript use.

### 2026-06-06 - M0019 pure robust row correction

- Request: correct the robust-DW grid rows so they use higher moments only and
  no second moments; verify whether the earlier noise-grid figure had used the
  correct pure robust DW definition.
- Actions taken: corrected
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py` and
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py` so the
  robust rows use a population mixed-higher-cumulant score only; removed the
  obsolete cross-covariance/profiling robust row from the noise grid; aligned
  the companion grid's cumulants with the standardized chi-square(5) shock
  calibration; updated simulation notes, registry, figure/source indexes, and
  logs.
- Files changed:
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.md`,
  `manuscript/figures/fig_sign_dw_robust_noise_grid.png`,
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.md`,
  `manuscript/figures/fig_sign_dw_robust_nongaussianity_grid.png`, planning
  surfaces, logs, and M0019 transparency files.
- Checks run: regenerated both corrected figures; `python -m py_compile
  manuscript\simulations\sign_dw_robust_noise_grid_figure.py
  manuscript\simulations\sign_dw_robust_nongaussianity_grid_figure.py`
  passed; formal registry and M0019 manifest JSON validation passed; numerical
  mask sanity check passed (`Gaussian shocks` robust row equals the admissible
  half-plane); `python scripts/check_manuscript.py` passed before closure with
  the expected open-milestone warning.
- Open uncertainties: the corrected robust rows are population visualizations;
  M28/M29 still need to verify aliases, weak-moment behavior, and calibrated
  critical values before final manuscript use.

### 2026-06-06 - M0018 non-Gaussianity companion grid

- Request: create a second figure like the corrected sign/DW/robust-DW grid,
  but with columns varying structural-shock non-Gaussianity to show that robust
  DW depends on informative higher moments and can be wide when they are weak.
- Actions taken: created
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`;
  rendered `manuscript/figures/fig_sign_dw_robust_nongaussianity_grid.png`;
  added an explanatory simulation note; updated figure, simulation, registry,
  source, dashboard, task, review, decision, session, and user-input logs.
- Files changed:
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.md`,
  `manuscript/figures/fig_sign_dw_robust_nongaussianity_grid.png`, planning
  surfaces, logs, and M0018 transparency files.
- Checks run: `python
  manuscript\simulations\sign_dw_robust_nongaussianity_grid_figure.py`
  passed; `python -m py_compile
  manuscript\simulations\sign_dw_robust_nongaussianity_grid_figure.py`
  passed; formal registry and M0018 manifest JSON validation passed;
  `python scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning.
- Open uncertainties: the figure is still a candidate visual; M28/M29 should
  verify weak-moment behavior and calibrated critical values before final use.

### 2026-06-06 - M0017 corrected sign/DW/robust-DW grid

- Request: correct the figure to the KnowledgeVault two-row by three-column
  B-plane layout, with sign restrictions on top, DW below, noise levels by
  column, and an added robust-DW row; use the corrected N-test cutoff instead
  of the artificial fixed J-score cutoff.
- Actions taken: inspected the synthesis sections for the finite-sample
  pointwise J/N-test cutoffs and the robust profiled moment statistic; created
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`; rendered
  `manuscript/figures/fig_sign_dw_robust_noise_grid.png`; added the
  explanatory simulation note and updated the relevant control files.
- Files changed: `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`,
  `manuscript/simulations/sign_dw_robust_noise_grid_figure.md`,
  `manuscript/figures/fig_sign_dw_robust_noise_grid.png`, planning surfaces,
  logs, and M0017 transparency files.
- Checks run: `python
  manuscript\simulations\sign_dw_robust_noise_grid_figure.py` passed;
  `python -m py_compile
  manuscript\simulations\sign_dw_robust_noise_grid_figure.py` passed; formal
  registry and M0017 manifest JSON validation passed;
  `python scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning.
- Open uncertainties: the row cutoffs are pointwise chi-square guides; final
  evidence still needs M28/M29 checks for population behavior, weak moments,
  and bootstrap or repeated-sample critical values.

### 2026-06-06 - M0016 sign/DW/robust-DW candidate figure

- Request: check the KnowledgeVault synthesis page on sign restrictions and
  noise, replicate the single simulation figure showing sign-restricted and DW
  behavior as noise rises, add the robust-DW set, and show the new figure.
- Actions taken: inspected the KnowledgeVault synthesis and visualization
  script; created `manuscript/simulations/sign_dw_robust_noise_figure.py`;
  rendered `manuscript/figures/fig_sign_dw_robust_noise_comparison.png`;
  added `manuscript/simulations/sign_dw_robust_noise_figure.md`; updated the
  registry, figure/simulation notes, dashboard, task board, source packet, and
  logs.
- Files changed: `manuscript/simulations/sign_dw_robust_noise_figure.py`,
  `manuscript/simulations/sign_dw_robust_noise_figure.md`,
  `manuscript/figures/fig_sign_dw_robust_noise_comparison.png`, planning
  surfaces, logs, and M0016 transparency files.
- Checks run: `python manuscript\simulations\sign_dw_robust_noise_figure.py`
  passed; `python -m py_compile
  manuscript\simulations\sign_dw_robust_noise_figure.py` passed; formal
  registry JSON validation passed; `python scripts/check_manuscript.py`
  passed before closure with the expected open-milestone warning.
- Open uncertainties: the visual cutoff is illustrative; M28 still needs
  population-grid checks for standard-DW pseudo-zeros, robust-DW truth
  inclusion, global aliases, and weak-moment widening.

### 2026-06-06 - M30 audit of M35 simulation triage

- Request: go on with the next task in goal mode.
- Actions taken: selected M30 from the dashboard recommendation; audited the
  M35 triage script against DGP normalization, noise design, candidate spaces,
  cumulant formulas, weighting, critical values, and interpretation; patched
  the script to report structural-coordinate noise deformation and add an
  anisotropic diagonal-noise stress case; reran the M35 screen and recorded
  the audit.
- Files changed: `manuscript/simulations/m35_jtest_monte_carlo_triage.py`,
  `manuscript/simulations/m35_jtest_monte_carlo_triage.md`,
  `manuscript/simulations/output/m35_jtest_monte_carlo_summary.json`,
  `manuscript/simulations/m30_m35_triage_audit.md`, planning surfaces, logs,
  and M0015 transparency files.
- Checks run: `python -m py_compile
  manuscript\simulations\m35_jtest_monte_carlo_triage.py` passed;
  `python scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning.
- Open uncertainties: M28 still needs population-grid verification. Later U0026
  superseded the planned M29 cutoff framing by making chi-square cutoffs the
  primary applied benchmark and repeated/bootstrap cutoffs audit rows.

### 2026-06-06 - M35 early J-test Monte Carlo triage

- Request: pick the next open task and work on it in goal mode.
- Actions taken: selected M35 from the task board; opened local transparency
  milestone M0014 and GitHub milestone #11; implemented
  `manuscript/simulations/m35_jtest_monte_carlo_triage.py`; ran the
  standard-DW versus robust-DW screening Monte Carlo; wrote Markdown and JSON
  outputs; updated task, dashboard, source, workplan, registry, and logs.
- Files changed: `manuscript/simulations/m35_jtest_monte_carlo_triage.py`,
  `manuscript/simulations/m35_jtest_monte_carlo_triage.md`,
  `manuscript/simulations/output/m35_jtest_monte_carlo_summary.json`,
  `manuscript/simulations/README.md`, `manuscript/task-board.md`,
  `manuscript/project-dashboard.md`, `manuscript/source-packet.md`,
  `manuscript/workplan.md`, `manuscript/formal-object-registry.json`, logs,
  and M0014 transparency files.
- Checks run: `python -m py_compile
  manuscript\simulations\m35_jtest_monte_carlo_triage.py` passed;
  `python scripts/check_manuscript.py` passed before closure with the expected
  open-milestone warning and passed again after closure.
- Open uncertainties: the M35 statistic is provisional and permissive; M30
  must audit it, and M28 must verify population zeros, aliases, and
  weak-moment widening before final evidence work.

### 2026-06-06 - Scope update and M25 J-test derivation

- Request: focus the paper only on the simultaneous SVAR rather than VAR lags;
  after the analytical J-test inversion result, run an early Monte Carlo
  overview before spending too much time; update tasks and plan and continue
  with the next task.
- Actions taken: updated the active plan, map, dashboard, task board, workplan,
  source packet, replication plan, draft notes, user input log, decision log,
  and formal registry; added M35 as the early MC triage task; created
  `manuscript/derivations/standard-dw-j-test-under-noise.md` for M25.
- Files changed: `manuscript/paper-plan.md`, `manuscript/paper-map.md`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/source-packet.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/derivations/standard-dw-j-test-under-noise.md`, logs, and M0013
  transparency files.
- Checks run: `python scripts/check_manuscript.py` passed, with the expected
  warning that M0013 was still open before milestone closure.
- Open uncertainties: M25 still needs audit; M35 should test finite-sample
  behavior quickly before polished figures or a larger replication package.

### 2026-06-06 - Robust DW derivation audit

- Request: pick the next manuscript task after the updated paper plan and work
  on it.
- Actions taken: selected M24 from the task board; audited
  `manuscript/derivations/dw-noise-robust-moments.md`; recorded the
  conditional pass in the derivation note, review log, formal registry,
  dashboard, task board, workplan, decision log, and session log.
- Files changed: `manuscript/derivations/dw-noise-robust-moments.md`,
  `manuscript/review-log.md`, `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/decision-log.md`,
  `manuscript/session-log.md`, and M0012 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed, with the expected
  warning that M0012 was still open before milestone closure.
- Open uncertainties: standard-DW emptying/misspecification proof, robust-DW
  population-grid aliases, weak-moment widening, and finite-sample Monte Carlo
  performance.

### 2026-06-06 - Robust DW plan pivot

- Request: completely update the paper plan around noisy sign-set bias,
  standard DW false-sharpening under residual noise, a robust DW
  higher-moment set that drops second moments, and Monte Carlo comparison
  evidence.
- Actions taken: rewrote the active paper plan, paper map, draft skeleton,
  source packet, formal-object registry, dashboard, task board, workplan,
  citation provenance, literature search, and replication plan around the new
  robust-DW comparison structure.
- Files changed: `knowledge-vault-link.json`, `manuscript/source-packet.md`,
  `manuscript/paper-plan.md`, `manuscript/paper-map.md`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/literature-search.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`, logs, and M0011
  transparency files.
- Checks run: `python scripts/check_manuscript.py` passed, with the expected
  warning that M0011 was still open before milestone closure.
- Open uncertainties: robust DW derivation audit, standard-DW asymptotic-empty
  proof, intuitive sign-noise figure design, and Monte Carlo implementation.

### 2026-06-06 - DW-like Gaussian-noise higher moments

- Request: create a derivation file for a Drautzburg-Wright-like
  higher-moment approach robust to additive noise, contrasting it with the
  invalid no-noise second-moment system.
- Actions taken: created
  `manuscript/derivations/dw-noise-robust-moments.md`; derived why Gaussian
  noise drops out of higher cumulants of `B^{-1}u` but not second moments;
  wrote third and fourth cumulants as moment equations suitable for GMM; and
  recorded the local bivariate rank condition and efficiency tradeoff.
- Files changed: `manuscript/derivations/dw-noise-robust-moments.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/paper-plan.md`,
  `manuscript/paper-map.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, logs, and the M0010 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed, with the expected
  warning that M0010 was still open before milestone closure.
- Open uncertainties: the derivation still needs adversarial audit for
  cumulant-to-moment algebra, normalization, local and global identification,
  and whether the Gaussian-noise route can carry the active constructive
  section.

### 2026-06-05 - Formal object typography

- Request: update manuscript writing rules for propositions, definitions, and
  proofs.
- Actions taken: added a full-block italics rule for formal statements, removed
  the visible end-marker convention, and standardized proof starts and endings.
- Files changed: `manuscript/manuscript-rules.md`,
  `manuscript/user-input-log.md`, `manuscript/decision-log.md`,
  `manuscript/session-log.md`, `manuscript/codex-log.md`.
- Checks run: `python scripts/check_manuscript.py` passed.
- Open uncertainties: KnowledgeVault link remains in template mode, but this
  work did not depend on vault source material.

### 2026-06-05 - Template initialization

- Request: initialize a standalone manuscript from the KnowledgeVault proposal
  on noise-robust sign-restricted SVARs and prepare a careful plan.
- Actions taken: validated the KnowledgeVault checkout and `svar-toolkit`
  package path; initialized manuscript metadata; built the source packet;
  revised the paper plan after a first-pass structure; updated the paper map,
  task board, workplan, formal-object registry, citation provenance,
  literature search, replication plan, draft skeleton, and logs; copied a first
  verified bibliography snapshot.
- Files changed: `knowledge-vault-link.json`, `bibliography/references.bib`,
  `manuscript/source-packet.md`, `manuscript/paper-plan.md`,
  `manuscript/paper-map.md`, `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/literature-search.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`, logs, and the
  M0003 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed, with the expected
  warning that M0003 was still open before milestone closure.
- Open uncertainties: Proposition 2 genericity conditions and Proposition 3
  regularity conditions need exact statements before drafting polished prose.

### 2026-06-05 - Bonhomme-Robin verification revision

- Request: incorporate corrected KnowledgeVault notes on Bonhomme-Robin noisy
  ICA and the BR-style SVAR inversion.
- Actions taken: reread the updated vault notes, updated the KnowledgeVault
  source commit, revised the paper plan/map/source packet, marked the BR-style
  propositions as unverified until derivation and simulation checks pass, added
  interleaved adversarial review tasks, and updated replication instructions.
- Files changed: `knowledge-vault-link.json`, `manuscript/source-packet.md`,
  `manuscript/paper-plan.md`, `manuscript/paper-map.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/literature-search.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`, logs, and the
  M0005 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed, with the expected
  warning that M0005 was still open before milestone closure.
- Open uncertainties: the BR-style cumulant map, local rank condition, and
  noise diagnostic must be derived and stress-tested before becoming manuscript
  claims.

### 2026-06-05 - M0005 task-state cleanup

- Request: complete the next open project task, which resolved to stale M21
  transparency cleanup.
- Actions taken: verified that M0005 is closed, committed, tagged at
  `manuscript-milestones/M0005-revise-br-verification-plan`, aligned with
  remote `main`, and closed on GitHub; updated the dashboard and task board so
  the next open research task is M05.
- Files changed: `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/session-log.md`,
  `manuscript/codex-log.md`, and the M0006 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed.
- Open uncertainties: M05 still needs the actual bivariate cumulant derivation
  before any Section 4 claims can be drafted.

### 2026-06-05 - Bivariate cumulant-map derivation

- Request: continue to the next project task, M05.
- Actions taken: created `manuscript/derivations/bivariate-cumulant-map.md`
  with the complete second-, third-, and fourth-order cumulant map for the
  diagonal-normalized bivariate SVAR; classified clean mixed moments separately
  from nuisance pure own moments and mapped noise cumulants.
- Files changed: `manuscript/derivations/bivariate-cumulant-map.md`,
  `manuscript/formal-object-registry.json`, `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`, logs, and the M0007
  transparency files.
- Checks run: `python scripts/check_manuscript.py` passed.
- Open uncertainties: M06 must audit the algebra, notation, and
  clean-versus-nuisance classifications before this map can support Section 4
  claims.

### 2026-06-05 - Bivariate cumulant-map audit

- Request: continue with M06.
- Actions taken: independently checked the coefficient/index pattern for all
  distinct second-, third-, and fourth-order bivariate cumulants; recorded the
  adversarial audit in `manuscript/review-log.md`; updated the derivation note
  to distinguish clean observed equations from restrictions that survive
  nuisance profiling.
- Files changed: `manuscript/derivations/bivariate-cumulant-map.md`,
  `manuscript/review-log.md`, `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, logs, and the M0008 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed.
- Open uncertainties: the map still needs M07 BR applicability work, M09
  profiled criteria and local rank derivation, and M12 symbolic/population
  verification before supporting manuscript result claims.

### 2026-06-05 - Bonhomme-Robin applicability clarification

- Request: continue with M07.
- Actions taken: created `manuscript/derivations/br-applicability.md` to pin
  the BR analogy to the paper's clean-pair and rank conditions; showed why the
  bivariate `L=K=2` SVAR is not covered by full quasi-JADE; defined the
  manuscript object as a low-dimensional BR-style profiled inversion.
- Files changed: `manuscript/derivations/br-applicability.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/paper-map.md`,
  `manuscript/review-log.md`, logs, and the M0009 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed.
- Open uncertainties: M08 must still attack the applicability argument, and
  M09/M12 must derive and verify the profiled criteria before any robust
  inversion claim is draftable.
