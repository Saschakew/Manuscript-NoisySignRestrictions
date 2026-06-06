# Workplan

## Current Stage

Initialized, scoped, and pivoted to the robust DW comparison paper. The
manuscript has a validated KnowledgeVault link, a refreshed source packet, a
new paper plan/map, an audited working robust-DW derivation, and a working
standard-DW J-test inversion derivation. The task queue is now centered on an
early Monte Carlo triage.

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
| M4. Formal result package | doing | Noisy sign-set proposition, standard-DW J-test result, robust-DW validity result, and comparison diagnostic are stated and audited. |
| M5. Evidence package | todo | Early Monte Carlo triage is run first; if informative, intuitive figure, population grids, and Monte Carlo figures/tables are specified and verified. |
| M6. First complete draft | todo | All sections have coherent prose and source trails. |
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
6. Diagnostic interpretation review: verify that DW-versus-robust-DW
   divergence is described as a warning, not proof of literal measurement
   error.
7. Evidence design: first run a small MC overview after the analytical J-test
   inversion result; only then expand simulations to no-noise agreement, noisy
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
12. Reader path: make sure the constructive robust set arrives before the
   warning feels like a purely negative critique.

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
