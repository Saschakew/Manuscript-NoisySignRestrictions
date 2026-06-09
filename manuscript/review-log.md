# Review Log

Use this file for actual review passes and resulting decisions.

## Review Passes

| Date | Pass | Reviewer | Outcome | Follow-up tasks |
|---|---|---|---|---|
| 2026-06-08 | M34 adversarial scope, logic, and style review | Codex adversarial manuscript review | Conditional pass after targeted fixes. The M0041 front-half rewrite now follows the revision spirit: it starts from no-noise sign restrictions, recovered-shock orthogonality, residual-noise bias, standard DW under its maintained null, and then the variance-ratio robust construction. M34 tightened visible claims by replacing confusing information/noise wording with a residual-noise-to-signal ratio, softening abstract simulation claims to match the lightweight M45 evidence, adding an explicit skewed-residual-noise stress-case caveat, updating citation provenance from historical M29 to current M45 evidence, and drafting the conclusion. | Next gates remain M25 proof audit and M33 replication wrapper. Do not promote Proposition 2 to theorem language until the standard-DW proof audit is complete. Keep M45 as lightweight evidence until final replication packaging or a heavier run. Final shareable draft still needs references/citation cleanup and export preparation. |
| 2026-06-08 | M0041 revision-comments compliance review | Codex style/content self-review | Pass with open follow-ups. The abstract now states sign-restricted set identification, residual-noise bias, false higher-moment precision, the information/noise-ratio robust refinement, and simulation evidence. The introduction now starts from signs plus recovered-shock orthogonality, then explains how idiosyncratic residual noise breaks that robustness, then introduces DW as a no-noise efficiency refinement and the robust proposal as the fix. Section 2 now introduces every core variable in the no-noise SVAR before adding noise, states the rescaling exception, discusses possible sign-boundary movement, and adds a J-test inversion view. Section 3 now explains DW under no noise before showing how noise breaks the moment stack. Section 4 now starts with the information/noise ratio and then adds Gaussian-noise-blind higher cumulants. | Run M34 as a broader adversarial style/logic review. The optional sign-flip figure suggested in the revision comments is not generated in M0041; the mechanism is now explained in prose and Figure 1 remains the continuous set-movement visual. M25 proof audit and replication wrapper remain open. |
| 2026-06-07 | M40 variance-ratio robust DW screen audit | Codex adversarial method review | Conditional pass for proposal-level Section 4 prose. The profiled covariance-decomposition screen matches `S = B diag(s_1,s_2) B' + diag(nu_1,nu_2)` with `0 <= nu_i <= 0.5 s_i`, avoids the M0034 double-normalization error, and is implemented as the correct linear feasibility problem. The 50 percent bound is substantive signal-to-noise identifying information, not a DW moment or normalization. A small 250-draw truth-screen check was reassuring but showed the hard sample screen can still exclude truth at `T=500`. | Use `manuscript/derivations/m40-variance-ratio-robust-dw-screen-audit.md` when revising Section 4. Keep M43-M45 open: rebuild Figure 2, add Figure 3, and rerun validation/Monte Carlo evidence before final claims. |
| 2026-06-06 | M37 diagonal-noise robust estimator audit | Codex adversarial method review | Historical conditional pass, now superseded by the M0034 scale correction. The post-M0030 robust statistic was coherent only when the off-diagonal covariance anchor could be written without free structural-shock variances; M0034 showed that this double-normalized scale under the active `diag(B)=1` chart. | Use `manuscript/derivations/m37-diagonal-noise-robust-estimator-audit.md` only as the record of the retired M0030 object. Use the M40 audit for the current variance-ratio screen. |
| 2026-06-06 | M0030 high-noise power audit | User plus Codex evidence validation | The previous pure higher-cumulant robust row lost finite-sample power under very high symmetric Gaussian noise. The revised diagonal-noise robust statistic uses the valid off-diagonal covariance anchor plus mixed higher cumulants, lowers the high-noise story column to `V=(0.5,0.5)`, and avoids whole-chart robust acceptance. Refreshed M29 chi-square rows show high-noise standard DW truth inclusion 0.050 versus robust DW truth inclusion 0.900, with robust accepted share 0.117. | Treat M0030 as superseding the old `V=(2,2)` evidence for the draft. If future models allow unrestricted residual-noise covariance, drop the off-diagonal covariance anchor and report the pure higher-cumulant fallback. |
| 2026-06-06 | M29 larger chi-square-primary evidence gate | Codex evidence validation | Superseded for the current draft by the post-M0030 refreshed M29 run recorded in `manuscript/simulations/m29_calibrated_monte_carlo.md`. The current evidence uses 120 calibration replications, 60 evaluation replications, 20 truth-bootstrap replications per evaluation sample, and a 41-by-41 grid. Under primary chi-square cutoffs, high-noise standard DW includes true `B0` in 0.050 of evaluation samples, while robust DW includes it in 0.900. The weak-moment and Gaussian-shock rows keep robust DW wide, supporting the limitation story. Audit cutoffs show calibration costs and should remain secondary. | Keep the refreshed M29 note and draft Table 1 as the current evidence. |
| 2026-06-06 | M29 cutoff convention review | User plus Codex evidence review | User clarified that standard pointwise chi-square critical values are appropriate as the main benchmark because they are the values a researcher would use when applying standard DW without accounting for residual noise. This resolves the prior framing that a final calibration rule still had to be chosen. Repeated-sample, oracle truth, and truth-bootstrap cutoffs remain useful audits, but not the central applied procedure. | Run a larger chi-square-primary M29 table and report audit cutoffs only as sensitivity/calibration-cost diagnostics. |
| 2026-06-06 | M29 truth-bootstrap expansion | Codex evidence validation | Added a truth-point residual-bootstrap cutoff convention to the M29 Monte Carlo. The expanded pass keeps the high-noise divergence under chi-square and no-noise repeated cutoffs: standard DW includes true `B0` in 0.292 and 0.333 of evaluation samples, while robust DW includes it in 0.917 and 0.875. The truth bootstrap restores truth inclusion to 1.000 for both methods, but with high-noise accepted shares of 0.325 for standard DW and 1.000 for robust DW, so it mainly documents the calibration cost and loss of precision. | Do not present the truth bootstrap as an application-ready procedure. Use it as an audit row beside the primary chi-square benchmark and run a larger table before marking M29 complete. |
| 2026-06-06 | M29 calibrated Monte Carlo first pass | Codex evidence validation | First repeated-sample calibration pass completed on the M0020/M28 B-plane. In the high Gaussian-noise stress case, standard DW includes true `B0` in about one third of evaluation samples under the no-noise repeated cutoff, while robust DW includes it in most samples. The oracle high-noise standard-DW truth cutoff rises to about 31.4 versus about 8.9 under no noise, showing a large calibration cost. Weak and Gaussian higher-moment cases keep robust DW wide, as expected. | Treat as first-pass evidence only. Audit the M29 design and expand with more replications or bootstrap critical values before final coverage and table claims. |
| 2026-06-06 | M28 grid story validation | Codex evidence validation | Exact population moments, grid-boundary sensitivity, repeated seeds, and pointwise critical-value checks support the selected M0020 grid-pair story under the maintained Gaussian residual-noise condition. The high-noise standard-DW row rejects true `B0` across repeated finite-sample seeds at the 10 percent pointwise cutoff, while robust DW keeps true `B0` as a population zero and widens under weak or Gaussian higher moments. | Use this as the first validation gate, not final coverage evidence. M27 should formalize the comparison diagnostic; M29 should calibrate repeated-sample or bootstrap critical values. |
| 2026-06-06 | M0021 figure-led plan review | Codex planning review | The M0020 grid pair is now selected as the paper's visual spine: the residual-noise grid tells the main warning, and the non-Gaussianity grid tells the honest limitation. | M28 first validation is complete; run M27/M29 before treating the figures as final evidence, and use the figure language when formalizing the comparison diagnostic. |
| 2026-06-06 | M0020 J-test grid correction | Codex visual/evidence review | Corrected both grid figures so every row inverts a pointwise 10 percent finite-sample J test. The robust-DW row now uses a five-moment mixed higher-cumulant J statistic with no covariance restriction. The noise grid's high-noise column shows standard DW rejecting true `B0` while robust DW contains it. | Keep captions explicit that these are pointwise J inversions; M28/M29 still need population and calibrated finite-sample checks before final evidence. |
| 2026-06-06 | M0019 pure robust row correction | Codex visual/evidence review | Corrected both grid figures: the robust-DW rows now use only population mixed higher cumulants and no second moments. The noise-grid robust row is invariant across Gaussian residual-noise levels; the non-Gaussianity grid robust row widens as structural non-Gaussianity weakens and accepts the whole plotted admissible graph when shocks are Gaussian. | Keep this correction in the figure captions/prose; distinguish the pure robust population rows from finite-sample pointwise N-tests in the sign and standard-DW rows. |
| 2026-06-06 | M0018 non-Gaussianity grid read | Codex visual/evidence review | The companion grid fixes residual noise and weakens structural non-Gaussianity across columns. It supports the intended limitation: sign/covariance geometry is mostly unchanged, while higher-moment rows become less sharp as structural shocks approach Gaussianity. | Treat as candidate evidence only; M28/M29 still need population checks and calibrated critical values before final manuscript use. |
| 2026-06-06 | M0017 corrected grid read | Codex visual/evidence review | The corrected 3-by-3 B-plane figure matches the requested layout and replaces the artificial fixed score cutoff with finite-sample N-test statistics and chi-square cutoffs. The robust row is wider and contains the true `B0` across the three diagonal-noise columns. | Treat as candidate evidence only; M28/M29 should still check population grids, weak-moment behavior, and bootstrap or repeated-sample critical values. |
| 2026-06-06 | M0016 candidate figure read | Codex visual/evidence review | The rendered sign/DW/robust-DW figure is readable and matches the intended population intuition: standard sign and standard DW move with noisy covariance rotations, while the robust-DW panel is fixed under Gaussian residual noise because it uses higher cumulants only. It remains an exploratory fixed-cutoff visualization. | Run M28 population-grid checks before treating the visual as final evidence; decide whether a final figure also needs covariance-ellipse or pseudo-set geometry panels. |
| 2026-06-06 | M30 M35 triage audit | Codex adversarial simulation review | Conditional pass for exploratory use only. DGP normalization and cumulant formulas are acceptable for screening, but the original moderate-noise case was near a structural-coordinate rescaling exception; the statistic's weighting and chi-square critical value are not calibrated. | Run M28 population grids next; do not use M35 for polished figures or M29 tables until critical values are calibrated. |
| 2026-06-06 | M35 early MC triage read | Codex evidence-design review | The first standard-DW versus robust-DW finite-sample screen is useful but cautionary. The no-noise sanity case behaves reasonably, but the provisional statistic is permissive under moderate Gaussian residual noise and weak higher moments. | Audit the M35 script/statistic in M30; run M28 population-grid checks before polished figures or final Monte Carlo tables. |
| 2026-06-06 | M24 robust DW derivation audit | Codex adversarial self-review | Conditional pass: the Gaussian-noise higher-cumulant route is valid as a local normalized derivation, with correct cumulant algebra, fourth-cumulant covariance subtractions, second-moment exclusion, and local-rank logic. It remains non-global and scale-normalized. | M25 must prove or weaken standard-DW misspecification/emptying; M28 must run population-grid checks for robust-DW truth inclusion, global aliases, and weak-moment widening. |
| 2026-06-06 | robust DW plan pivot | Codex planning review | Active manuscript plan now centers on noisy sign-set bias, standard DW misspecification/false sharpening, robust DW higher moments that drop second moments, and Monte Carlo overlap/divergence evidence. Previous constructive-route labels were removed from active planning surfaces. | Audit the robust DW derivation; prove or weaken standard-DW asymptotic emptiness; design geometry and Monte Carlo evidence. |
| 2026-06-05 | BR correction and plan audit | Codex self-review | Earlier plan over-claimed the Bonhomme-Robin connection. Updated plan now treats the bivariate method as BR-style and unverified until derivation and simulation checks pass. | Derive cumulant map; audit derivation; build symbolic, population, and Monte Carlo verification; audit simulation interpretation. |
| 2026-06-05 | scope and contribution | Codex self-review | Revised first plan from a broader seven-section paper with optional empirical illustration into a shorter theory-and-simulation note. | Keep empirical illustration, dynamic signs, and `K > 2` generalization deferred until Propositions 1-4 and the simulation package are stable. |
| 2026-06-05 | M06 bivariate cumulant-map audit | Codex adversarial self-review | No coefficient or index errors were found in the expanded second-, third-, and fourth-order cumulant map. The audit corrected classification language so clean mixed third cumulants are not overstated as identifying restrictions after unrestricted `gamma` profiling, and clarified that inequality restrictions on noise moments are diagnostics or admissibility conditions rather than overidentifying equalities. | Use the audited map as a working input for M07 and M09; still derive profiled criteria, local rank, and symbolic/population verification before drafting BR-style result claims. |
| 2026-06-05 | M07 BR applicability clarification | Codex method review | Direct Bonhomme-Robin quasi-JADE does not cover the bivariate `L=K=2` SVAR: independent bivariate errors supply one clean pair, so the all-kurtotic `Q_J` rank condition cannot reach `K=2`, and the skewness route does not cover two factors with `L=2`. The manuscript object is a BR-style profiled inversion, not quasi-JADE. | Run M08 to attack this boundary argument before relying on it; then derive profiled criteria and local rank in M09. |

## M34 Adversarial Scope, Logic, And Style Review

Scope: `manuscript/draft.md`, `manuscript/paper-map.md`,
`manuscript/project-dashboard.md`, `manuscript/task-board.md`,
`manuscript/formal-object-registry.json`, M40 screen audit, M45 evidence note,
and the M25 standard-DW derivation note.

Decision: conditional pass for the revised draft as a disciplined first-draft
manuscript, not yet as a shareable final paper.

Checklist outcome:

- Revision spirit: passed after M0041 and M34. The front half now uses the
  order requested by the revision comments: no-noise SVAR, recovered-shock
  orthogonality, noisy residuals, standard DW under the no-noise null, and the
  robust variance-ratio construction.
- One-paper scope: passed. The draft stays in a bivariate simultaneous impact
  model and does not drift into VAR lag dynamics, dynamic impulse responses,
  empirical applications, or general `K`-variable implementation.
- Variance-ratio screen: passed with caveat. The screen is now described in
  visible prose as a maximum residual-noise-to-signal ratio, not as automatic
  information or a normalization. Its precision is explicitly identifying
  information.
- Evidence language: passed after fixes. The abstract now says "current
  simulation designs" and "usually keeps" rather than making an unconditional
  coverage claim. Section 5 now states that the skewed-residual-noise row
  violates the Gaussian-noise route and is only a stress case.
- Figure 3 interpretation: passed with caveat. The prose calls it a fixed draw
  and does not turn the sample-size grid into a coverage claim.
- Proposition 2: open. The draft properly labels the statement as a sketch and
  keeps TODO notes tied to the M25 proof audit. This must remain a blocker for
  theorem-level wording.
- Proposition 3: conditional. The population validity statement is acceptable
  under the normalized chart, Gaussian residual noise, local rank, and
  maintained variance-ratio bound, but final theorem wording still needs proof
  review and final replication treatment.
- Shareability: incomplete. The conclusion is now drafted, but the References
  section remains a TODO, `Author` is still a placeholder, and the figure/table
  rebuild path still needs the M33 replication wrapper.

Changes made during M34:

- Replaced reader-facing "information/noise ratio" language with
  residual-noise-to-signal or variance-ratio language.
- Softened abstract simulation claims to match M45's lightweight evidence and
  finite-sample hard-screen caveats.
- Added a warning that the skewed-residual-noise row violates Assumption 1.
- Replaced the conclusion TODO with a concise diagnostic conclusion.
- Updated citation provenance so the active Monte Carlo table points to M45
  rather than the superseded M29 robust row.

Next recommended work:

1. Run the M25 standard-DW proof audit before strengthening Proposition 2.
2. Build the M33 manuscript-local replication wrapper before calling the
   evidence package shareable.
3. Clean References, author/date metadata, and export-facing source trails.
4. Consider a separate sign-flip visual only if a later reader pass still
   finds the continuous Figure 1 movement too indirect.

## M06 Bivariate Cumulant-Map Audit

Scope: `manuscript/derivations/bivariate-cumulant-map.md`.

Checklist outcome:

- Indices: passed. Independent coefficient enumeration gave the monomial
  pattern `(1,a^r)`, `(b,a^{r-1})`, ..., `(b^r,1)` for bivariate multisets,
  matching all displayed second-, third-, and fourth-order equations.
- Cumulant definitions: passed. The fourth-order object is explicitly a
  cumulant, with covariance-product subtractions shown for centered residuals.
- Normalization: passed. The second-cumulant equations rely on
  `cum_2(epsilon_j, epsilon_j)=1`, which is stated in the setup.
- Missing moments: passed. The note lists all `r+1` distinct bivariate
  cumulants for orders `r=2,3,4`.
- Clean versus nuisance classification: corrected. The audit changed the note
  to distinguish clean observed equations from restrictions that survive
  unrestricted profiling of nuisance structural or noise cumulants.

Decision: the cumulant map is an audited working object, not yet a draftable
identification result. It can support M07 and M09, but M09 must still derive
the profiled `J_4`/`J_stack` restrictions and M12 must verify the map
symbolically and on population grids.

Suggested passes:

- Scope and contribution.
- Citation provenance.
- Notation and assumptions.
- Theorem or derivation gaps.
- Adversarial derivation audit.
- Robust DW route audit.
- Adversarial simulation audit.
- Adversarial interpretation/story audit.
- Simulation or empirical design.
- Reproducibility package.
- Literature positioning.
- Reader path.

## M48 DW Moment Definition And Normalization Audit

Scope: `manuscript/derivations/m48-dw-moment-normalization-audit.md`,
`manuscript/draft.md`, the Drautzburg-Wright vault note/raw markdown, and the
Figure 1/M45 simulation code.

Detailed audit: `manuscript/derivations/m48-dw-moment-normalization-audit.md`.

Checklist outcome:

- DW source moment definition: corrected. DW's GMM comparator uses
  standardized co-skewness and co-kurtosis product moments with
  Gaussian-Isserlis fourth-product targets, not fourth cumulants.
- Figure 1 implementation: passed. The standard-DW row uses demeaned and
  standardized recovered shocks with moment powers `(1,1)`, `(2,1)`, `(1,2)`,
  and `(2,2)`, targeting `1` only for `(2,2)`.
- Noisy raw-product formulas: derived. At `B=B0`, mixed third raw products
  remain zero under independent Gaussian residual noise, while fourth raw
  products are shifted by covariance products such as `3 S_ii S_ij` and
  `S_ii S_jj + 2 S_ij^2`.
- Robust cumulant route: reaffirmed. Section 4's cumulants subtract these
  covariance-product terms and therefore remain the Gaussian-noise-blind
  higher-moment object.
- Normalization: passed with decision. Keep the `diag(B)=1` common B-plane and
  profile structural variances in the variance-ratio screen; do not migrate
  the current evidence spine to a unit-variance impact chart.

Decision: M48 is complete for the draft gate. M47 remains open because this
audit fixes moment definitions and normalization, not the rich-stack
misspecification proof.

## M24 Robust DW Derivation Audit

Scope: `manuscript/derivations/dw-noise-robust-moments.md`.

Checklist outcome:

- Gaussian-noise condition: passed. Gaussianity and independence are the clean
  sufficient conditions for transformed higher-cumulant cancellation; diagonal
  `V` is not needed for the cumulant result itself.
- Cumulant-to-moment algebra: passed for centered observations. Third
  cumulants equal third central moments, and fourth restrictions must be fourth
  cumulants with covariance-product subtractions.
- Second-moment exclusion: passed. Covariances may enter as nuisance quantities
  inside fourth cumulants, but the robust set must not impose no-noise
  restrictions such as `Var{z_i}=1` or `Cov{z_i,z_j}=0`.
- Normalization: conditional pass. The bivariate `B(a,b)` parameterization is a
  normalized local chart for impact shape, not full scale recovery. It requires
  nonzero normalizing entries plus sign and label conventions.
- Local rank: passed. The first-order expansion gives rank for `(a,b)` when
  `D_0 != 0` and each shock has at least one nonzero third or fourth cumulant.
  `C_{1122}` is second order at the truth and should not be described as
  carrying first-order local rank.
- Global identification: unresolved. Remote zeros, finite-order cumulant
  cancellations, and label/sign aliases remain possible until population-grid
  checks.
- Bias wording: passed with caveat. The result supports population correctness
  and asymptotic centering, not finite-sample unbiasedness.

Decision: use the derivation as the working Section 4 route, but state the
first formal result as a local normalized Gaussian-noise proposition. Do not
call it a global theorem or rely on it for final evidence until M28 and M29.

## M37 Diagonal-Noise Robust Estimator Audit

Scope: post-M0030 robust estimator in
`manuscript/derivations/dw-noise-robust-moments.md`,
`manuscript/derivations/dw-robust-comparison-diagnostic.md`, the two grid
figure scripts, and the M28/M29 validation scripts.

Detailed audit: `manuscript/derivations/m37-diagonal-noise-robust-estimator-audit.md`.

Checklist outcome:

- Off-diagonal covariance anchor: passed, conditional on the normalized
  bivariate chart and diagonal residual-noise covariance. The valid restriction
  is `Cov(u_1,u_2)=b12+b21`; it is not the false standard-DW restriction
  `Cov(z_1,z_2)=0`.
- Scale wording: caveat required. The anchor is tied to the diagonal-normalized
  chart. For arbitrary unknown impact scales, the off-diagonal covariance
  equation would need scale parameters.
- Diagonal-variance profiling: conditional pass. The current figures profile
  diagonal variances by dropping diagonal covariance equalities, but they do
  not impose `V_ii(B)>=0`; formal prose must either add that admissibility
  screen or state the diagnostic-row convention.
- Mixed cumulants: passed under independent Gaussian residual noise. Third
  restrictions are centered third moments, fourth restrictions are cumulants
  with covariance-product subtractions, and covariance terms are nuisance
  ingredients rather than restrictions.
- Cutoff degrees of freedom: conditional pass. `chi2_6` matches the six
  displayed moments but is only a pointwise applied benchmark, especially when
  moment covariance is estimated or higher moments are weak.
- Fallbacks: passed after clarification. Correlated Gaussian residual noise
  drops the covariance anchor and uses the pure higher-cumulant fallback;
  diagonal non-Gaussian residual noise keeps the covariance anchor but not the
  clean transformed-cumulant interpretation; correlated non-Gaussian residual
  noise is outside the current robust claim.

Decision: Section 4 may state a conditional local proposition for the
diagonal-noise robust DW set, not an unconditional theorem. Use M37's caveats
when drafting theorem text and captions.

## M30 M35 Triage Audit

Scope: `manuscript/simulations/m35_jtest_monte_carlo_triage.py` and generated
M35 outputs.

Outcome: conditional pass for exploratory screening only. The detailed audit
is in `manuscript/simulations/m30_m35_triage_audit.md`.

Main findings:

- DGP normalization: passed for exploratory use. The square-root weighted
  mixture preserves unit variances in population and weakens higher cumulants
  as intended.
- Noise design: corrected. The original moderate diagonal-noise case was close
  to a structural-coordinate rescaling exception; the script now reports the
  structural-coordinate off-diagonal noise norm and adds an anisotropic
  diagonal-noise stress case.
- Candidate spaces: conditional pass. Standard DW uses the population
  covariance factor and robust DW searches the normalized chart containing the
  true shape; final finite-sample evidence must decide whether to use sample
  covariance or keep a separate population-grid experiment.
- Cumulant formulas: passed for centered exploratory cumulants.
- Weighting and critical values: failed for evidence. The diagonal raw-product
  scaling and chi-square reference are not calibrated J-test inversion
  machinery.
- Interpretation: passed after correction. The output now points to M28
  population-grid checks, not polished M29 tables.

Decision: M35 remains a useful cautionary screen but not evidence. M28 should
be the next evidence task.
