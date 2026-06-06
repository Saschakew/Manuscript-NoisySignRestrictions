# Workplan

## Current Stage

Initialized, scoped, and pivoted to the robust DW comparison paper. The
manuscript has a validated KnowledgeVault link, a refreshed source packet, a
new paper plan/map, an audited working robust-DW derivation, a working
standard-DW J-test inversion derivation, a first M35 early Monte Carlo triage,
and an M30 audit of that triage. The M0020 residual-noise grid and
non-Gaussianity grid are now the selected visual spine: they show noisy
sign-set movement, standard-DW truth rejection under high residual noise,
robust-DW truth inclusion, and robust-DW widening as higher moments weaken.
M28 completed the first validation pass for that story with exact population
moments, grid-boundary sensitivity, repeated finite-sample seeds, and
pointwise critical-value sensitivity. M27 formalized the reported
standard-DW set, robust-DW set, critical-value convention, directional
overlap/divergence metric, and interpretation boundaries. M29 now has an
expanded Monte Carlo pass using chi-square, no-noise repeated, oracle scenario
truth, and truth-point residual-bootstrap cutoffs. User decision U0026 makes
the standard pointwise chi-square rows the primary applied benchmark; the other
cutoffs are calibration audits. The evidence queue is now centered on running
a larger chi-square-primary table.

The active paper no longer treats the previous constructive route as part of
the main plan. The first version is a short simultaneous-SVAR
theory-and-simulation note about noisy sign-set bias, standard Drautzburg-Wright
false-sharpening, and a robust DW higher-moment comparison set. It does not
model VAR lags or dynamic impulse responses.

## Milestones

| Milestone | Status | Exit condition |
|---|---|---|
| M1. Initialize repository | done | Metadata, source links, package path, source packet, and first bibliography snapshot are initialized. |
| M2. Scope paper | done | One-sentence claim, paper contract, exclusions, and revised structure are stable enough for formal planning. |
| M3. Pivot to robust DW plan | done | Active plan, map, registry, task board, source packet, draft skeleton, and replication plan all point to the robust DW comparison paper. |
| M4. Formal result package | doing | Noisy sign-set proposition, standard-DW J-test result, robust-DW validity result, and comparison diagnostic are stated and audited. M27 has stated the comparison diagnostic. |
| M5. Evidence package | doing | M0020 selected the figure pair as the visual spine; M28 validates the population/repeated-seed grid story and M29 now has chi-square-primary evidence plus repeated-sample and truth-bootstrap audit diagnostics using the M27 metrics. Exit still requires a larger final finite-sample table. |
| M6. First complete draft | todo | After M28 validation, all sections have figure-led prose and source trails. |
| M7. Reproducibility package | todo | Final figures/tables can be regenerated from `manuscript/replication/`. |
| M8. Shareable draft | todo | Citations, provenance, checks, and exports are clean. |

## Review Plan

1. Scope and contribution: verify that the paper is a robustness-check note,
   not a broad higher-moment SVAR survey.
2. Notation and assumptions: audit the additive-noise model, unit-variance
   normalization, Gaussian-noise condition for robust transformed cumulants,
   and sign-labeling conventions.
3. Noisy sign-set review: check the covariance pseudo-set, column-rescaling
   obstruction, and intuition in the first figure.
4. Standard-DW misspecification review: prove or weaken the claim that the
   population DW set becomes empty under residual noise; list special cases.
5. Robust-DW derivation review: check cumulant-to-moment algebra, fourth-order
   covariance subtractions, local rank, scale loss, and finite-sample bias
   wording.
6. Diagnostic interpretation review: use the M27 directional metric and verify
   that DW-versus-robust-DW divergence is described as a warning, not proof of
   literal measurement error.
7. Evidence design: use the M0020 figure pair as the visual spine; use the
   M28 population/repeated-seed validation and M29 expanded calibrated pass as
   gates before expanding simulations to final no-noise agreement, noisy
   disagreement, weak-moment widening, and misspecified robust-noise cases.
8. Simulation adversary: before accepting any figure, check whether the DGP,
   grids, critical values, cumulant estimators, or plotting choices could make
   the result look correct even if the theory is wrong.
9. Citation provenance: map every prior-work paragraph to a vault source and
   mark original contributions clearly.
10. Reproducibility package: make final figures rebuildable without a local
   KnowledgeVault dependency.
11. Literature positioning: keep Drautzburg-Wright framed as valid under its
   maintained no-noise null and define this paper as a residual-noise
   robustness check.
12. Reader path: make sure the residual-noise grid establishes the warning and
   the non-Gaussianity grid immediately states the honest limitation of the
   robust set.

## Deferred Extensions

- Empirical illustration or diagnostic rereading of a published sign-restricted
  SVAR.
- `K > 2` general implementation in the main text.
- VAR lag dynamics, dynamic sign restrictions, impulse responses, and
  IRF-horizon sign sets in the main text.
- Correlated, serially dependent, common-factor, or stochastic-volatility
  residual noise.
- Combining the robust comparison with external instruments or narrative
  restrictions.
