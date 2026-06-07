# Workplan

## Current Stage

M0034 scale correction: the M0030/M37 diagonal-anchor robust-DW evidence is
superseded. M0036 supplies the replacement: variance-ratio robust DW, which
uses valid higher-cumulant moments plus an explicit signal-to-noise covariance
screen with `0 <= nu_i <= 0.5 Var(epsilon_i)`.

M0040 update: the variance-ratio robust DW screen is now the paper's active
proposal with rebuilt first-pass evidence. Sections 2-4 have formula-first
skeletons, manuscript math delimiters have been cleaned, Figure 2 uses the
variance-ratio robust row, Figure 3 adds the `T=500,1000,2000` sample-size
grid, and M45 supplies lightweight validation and Monte Carlo evidence.

M0038/M0040 drafting update: Sections 2-4 now have formula-first skeletons
using proper manuscript math delimiters. The Section 3 statement remains
conditional on the M25 standard-DW proof audit, and the Section 4
variance-ratio robust DW statement has a conditional M40 screen audit pass and
M45 lightweight evidence.

Initialized, scoped, and pivoted to the robust DW comparison paper. The
manuscript has a validated KnowledgeVault link, a refreshed source packet, a
new paper plan/map, an audited working robust-DW derivation, a working
standard-DW J-test inversion derivation, a first M35 early Monte Carlo triage,
and an M30 audit of that triage. M0030 revised the residual-noise grid and
non-Gaussianity grid into the former visual spine, but M0034/M0036 superseded
the robust rows: the new visual spine should use variance-ratio robust DW in
  Figure 1, rebuilt Figure 2, and added the Figure 3 sample-size grid.
M28 completed a refreshed validation pass for the old grid story, and M29
completed a chi-square-primary Monte Carlo pass, but both are historical for
the current robust row because M0034-M0036 superseded the diagonal-anchor
statistic. M27/M0030 formalized the reported standard-DW set, robust-DW set,
critical-value convention, directional overlap/divergence metric, and
  interpretation boundaries; M45 reuses that metric bundle. User
decision U0026 still makes standard pointwise chi-square rows the primary
applied benchmark; the other cutoffs are calibration audits. M31 started the
first figure-led draft by
replacing the TODO-only abstract, introduction, and evidence section with a
source-traced skeleton around the residual-noise grid, the non-Gaussianity
  grid, and the historical M29 chi-square-primary table. M37 directly audited the
post-M0030 robust estimator, but M0034 later superseded that pass judgment
under the active scale normalization. M32 added the first literature-positioning
pass inside the introduction, distinguishing the paper from sign-set
inference, Drautzburg-Wright's no-noise comparator, and higher-moment SVAR/GMM
sources.

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
| M4. Formal result package | doing | Noisy sign-set proposition, standard-DW J-test result, robust-DW validity result, and comparison diagnostic are stated and audited. M0036 variance-ratio robust DW is now the proposal; M40 conditionally passed its covariance screen; the M25 standard-DW proof audit remains open. |
| M5. Evidence package | doing | M0040 rebuilt the immediate evidence package around the variance-ratio proposal: Figure 2, Figure 3, and M45 validation/Monte Carlo. Remaining work is adversarial evidence review and final replication packaging. |
| M6. First complete draft | doing | M31 drafted the abstract, introduction, and evidence section; M32 added the first literature-positioning pass; M0038 drafted formula-first Sections 2-4; M40 conditionally passed the variance-ratio screen; M0040 updated figures and evidence. Remaining draft gates are the M25 proof audit, M34 logic review, and replication wrapper. |
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
5. Robust-DW derivation review: M40 conditionally passed the M0036 relative
   covariance-decomposition screen, including algebra, finite-sample
   equality-plus-inequality behavior, and the substantive interpretation of
    the 50 percent noise-to-shock variance bound. Future review should focus on
    final-claim wording for the hard finite-sample screen.
6. Diagnostic interpretation review: use the M27 directional metric and verify
   that DW-versus-robust-DW divergence is described as a warning, not proof of
   literal measurement error.
7. Evidence design: treat the Figure 1/Figure 2/Figure 3 sequence and M45
   table as the current visual spine; run an adversarial review before turning
   lightweight evidence into final evidence claims.
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
