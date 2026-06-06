# Codex Log

Purpose: shareable milestone-level transparency log for Codex work on this
manuscript.

Do not record every micro-edit here. Use this file for substantial Codex-led
work, visible milestones, checks run, and open uncertainties.

Every entry that closes a substantive work block should correspond to a
machine-readable milestone in `transparency/milestones/`.

## Entries

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
