# Workplan

## Current Stage

M0034 scale correction: the M0030/M37 diagonal-anchor robust-DW evidence is
superseded. M0036 supplies the replacement: variance-ratio robust DW, which
uses valid higher-cumulant moments plus an explicit signal-to-noise covariance
screen with `0 <= nu_i <= 0.5 Var(epsilon_i)`.

M0037 planning update: treat the variance-ratio robust DW screen as the paper's
proposal. The next work is to sketch Sections 2-4 with the important formulas,
clean manuscript math into `\(...\)` and `\begin{equation}` form, update
Figure 2, add Figure 3 with `T=500,1000,2000`, and then rebuild validation and
Monte Carlo evidence.

Initialized, scoped, and pivoted to the robust DW comparison paper. The
manuscript has a validated KnowledgeVault link, a refreshed source packet, a
new paper plan/map, an audited working robust-DW derivation, a working
standard-DW J-test inversion derivation, a first M35 early Monte Carlo triage,
and an M30 audit of that triage. M0030 revised the residual-noise grid and
non-Gaussianity grid into the former visual spine, but M0034/M0036 superseded
the robust rows: the new visual spine should use variance-ratio robust DW in
Figure 1, rebuild Figure 2, and add the Figure 3 sample-size grid.
M28 completed a refreshed validation pass for that story with exact population
moments, grid-boundary sensitivity, repeated finite-sample seeds, and
pointwise critical-value sensitivity. M27/M0030 formalized the reported
standard-DW set, robust-DW set, critical-value convention, directional
overlap/divergence metric, and interpretation boundaries. The refreshed M29
Monte Carlo pass now uses chi-square, no-noise repeated, oracle scenario truth,
and truth-point residual-bootstrap cutoffs. User decision U0026 makes the
standard pointwise chi-square rows the primary applied benchmark; the other
cutoffs are calibration audits. M31 started the first figure-led draft by
replacing the TODO-only abstract, introduction, and evidence section with a
source-traced skeleton around the residual-noise grid, the non-Gaussianity
grid, and the M29 chi-square-primary table. M37 directly audited the
post-M0030 robust estimator and conditionally cleared it for local
theorem-level prose under diagonal Gaussian residual noise. M32 added the
first literature-positioning pass inside the introduction, distinguishing the
paper from sign-set inference, Drautzburg-Wright's no-noise comparator, and
higher-moment SVAR/GMM sources.

The active paper no longer treats the previous constructive route as part of
the main plan. The first version is a short simultaneous-SVAR
theory-and-simulation note about noisy sign-set bias, standard Drautzburg-Wright
false-sharpening, and a robust DW comparison set. It does not model VAR lags or
dynamic impulse responses.

## Milestones

| Milestone | Status | Exit condition |
|---|---|---|
| M1. Initialize repository | done | Metadata, source links, package path, source packet, and first bibliography snapshot are initialized. |
| M2. Scope paper | done | One-sentence claim, paper contract, exclusions, and revised structure are stable enough for formal planning. |
| M3. Pivot to robust DW plan | done | Active plan, map, registry, task board, source packet, draft skeleton, and replication plan all point to the robust DW comparison paper. |
| M4. Formal result package | doing | Noisy sign-set proposition, standard-DW J-test result, robust-DW validity result, and comparison diagnostic are stated and audited. M0036 variance-ratio robust DW is now the proposal; M40 must audit it before theorem-level claims; the M25 standard-DW proof audit remains open. |
| M5. Evidence package | needs-rebuild | M0036 created the variance-ratio Figure 1 proposal. Figure 2 must be updated, Figure 3 must be added, and M28/M29 evidence must be rebuilt because the old robust rows used the superseded diagonal-anchor statistic. |
| M6. First complete draft | doing | M31 drafted the abstract, introduction, and evidence section around now-superseded figures and M29 table; M32 added the first literature-positioning pass; Sections 2-4 need a formula-first sketch using proper manuscript math delimiters. |
| M7. Reproducibility package | todo | Final figures/tables can be regenerated from `manuscript/replication/`. |
| M8. Shareable draft | todo | Citations, provenance, checks, and exports are clean. |

## Review Plan

1. Scope and contribution: verify that the paper is a robustness-check note,
   not a broad higher-moment SVAR survey.
2. Notation and assumptions: audit the additive-noise model, scale
   normalization, relative noise-to-shock covariance screen, Gaussian-noise
   condition for robust transformed cumulants, and sign-labeling conventions.
3. Noisy sign-set review: check the covariance pseudo-set, column-rescaling
   obstruction, and intuition in the first figure.
4. Standard-DW misspecification review: prove or weaken the claim that the
   population DW set becomes empty under residual noise; list special cases.
5. Robust-DW derivation review: M40 should check the M0036 relative
   covariance-decomposition screen, including algebra, finite-sample
   equality-plus-inequality behavior, and the substantive interpretation of
   the 50 percent noise-to-shock variance bound.
6. Diagnostic interpretation review: use the M27 directional metric and verify
   that DW-versus-robust-DW divergence is described as a warning, not proof of
   literal measurement error.
7. Evidence design: treat the M0036 variance-ratio Figure 1 as the proposal
   visual spine; update Figure 2, add the `T=500,1000,2000` Figure 3, and then
   rebuild M28/M29-style validation.
8. Simulation adversary: before accepting any figure, check whether the DGP,
   grids, critical values, cumulant estimators, or plotting choices could make
   the result look correct even if the theory is wrong.
9. Citation provenance: map every prior-work paragraph to a vault source and
   mark original contributions clearly.
10. Reproducibility package: make final figures rebuildable without a local
   KnowledgeVault dependency.
11. Literature positioning: M32 drafted the first pass. In later revisions,
   keep Drautzburg-Wright framed as valid under its maintained no-noise null
   and define this paper as a residual-noise robustness check.
12. Reader path: make sure the residual-noise grid establishes the warning and
   the non-Gaussianity and sample-size grids immediately state the limitations
   and finite-sample behavior of the variance-ratio robust set.

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
