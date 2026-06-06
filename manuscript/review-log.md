# Review Log

Use this file for actual review passes and resulting decisions.

## Review Passes

| Date | Pass | Reviewer | Outcome | Follow-up tasks |
|---|---|---|---|---|
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
