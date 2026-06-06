# Review Log

Use this file for actual review passes and resulting decisions.

## Review Passes

| Date | Pass | Reviewer | Outcome | Follow-up tasks |
|---|---|---|---|---|
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
- BR applicability and nuisance-cumulant treatment.
- Adversarial derivation audit.
- DW-like Gaussian-noise route audit.
- Adversarial simulation audit.
- Adversarial interpretation/story audit.
- Simulation or empirical design.
- Reproducibility package.
- Literature positioning.
- Reader path.
