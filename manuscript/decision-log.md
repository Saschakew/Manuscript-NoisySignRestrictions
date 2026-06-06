# Decision Log

Use this file for durable research, scope, notation, evidence, and workflow
decisions.

## Entries

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
