# Workplan

## Current Stage

M0034 scale correction: the M0030/M37 diagonal-anchor robust-DW evidence is
superseded. M0036 supplied the pre-M64 replacement: variance-ratio robust DW.
M64 then switched the active manuscript to unit structural-shock variances, M66
clarified the active ratio notation as
`lambda_i = nu_i / (B B')_ii in [0,rho]`, and M68 rebuilt Figures 1-3 plus
the Monte Carlo diagnostic on the first-shock chart `(B11,B21)` with positive
diagonal signs and the maintained `B12<=0`, `B21>=0` restrictions.

M0040 update: the variance-ratio robust DW screen is now the paper's active
proposal with rebuilt first-pass evidence. Sections 2-4 have formula-first
skeletons, manuscript math delimiters have been cleaned, Figure 2 uses the
variance-ratio robust row, Figure 3 adds the `T=500,1000,2000` sample-size
grid, and M45 supplies lightweight validation and Monte Carlo evidence.

M0038/M0040/M0042/M0044/M0045/M0046/M0047/M0048/M0049 drafting update: Sections 2-4 now have
formula-first skeletons using proper manuscript math delimiters, and M0042
completed the M34 adversarial scope, logic, and style review after the M0041
revision rewrite. M0045 marks M48 as partial and not source-complete, and M49
now supplies the source-complete replacement: the bivariate DW GMM1 menu is
`112`, `122`, `1112`, `1122`, `1222`, GMM2 drops only `1122`, and the current
Figure 1/M45 standard-DW code is a historical hybrid rather than source-correct
DW evidence. M0046 introduces durable task hand-off packets under
`manuscript/tasks/`; M0047 makes the skill explicitly packet-aware for
`work on next task` and `plan next tasks` prompts; M0049 planned M53 and M0050
completed it by replacing the Section 3 `h_i(B)` display with `e_t(B)` and
rewriting Section 4 robust conditions as moment equations before the paper
returns to evidence work. M0051 inserted M54 before M52 so the transformed-
noise moment derivation and normalization choice could be audited before the
source-correct evidence rebuild; M54 is now complete and keeps the manuscript
in the common `diag(B)=1` chart. M0054 inserted M56 before M55 because the
sample fourth-cumulant entries use products of sample averages; M56 is now
complete. M0056 completed M55 by translating the M54/M56 result into
reader-facing Section 4 prose, including the `Omega(B)` versus `S(B)`
distinction, representative fourth-order algebra, and the generated sample
moment recipe. M0057 completed M52 by rebuilding the source-correct evidence
path with bivariate DW GMM1 higher moments plus a separate covariance screen
and full central-delta robust generated-moment weighting. M0058 completed M47
by auditing the M25 standard-DW proof gate; Proposition 2 is now safe as a
conditional rich-stack/ICA statement with structural-rescaling, finite-alias,
compactness, and nonsingularity caveats.

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
| M4. Formal result package | doing | M64 supersedes the retained `diag(B)=1` route and switches the active formal route to unit-variance GMM over `(B, nu)`. M66 settles the nuisance bound as `lambda_i = nu_i / (B B')_ii in [0,rho]`. M68 implements diagnostic evidence; M65 still owns the projection critical value before theorem-level wording. |
| M5. Evidence package | doing | M68 rebuilds Figures 1-3 and the Monte Carlo diagnostic under the unit-variance `(B,lambda)` projected GMM estimator and first-shock chart. Final evidence status still needs the projected critical-value note. |
| M6. First complete draft | doing | M64 recovered the real revision comments and rewrote Sections 2-4 around unit variance and standard GMM. M68 updates Section 5 around the active first-shock evidence. Remaining draft gates are projected-critical-value wording, references cleanup, and export preparation. |
| M7. Reproducibility package | doing | M33 added `manuscript/replication/run_all.py`; M68 updates its Figure 1-3 and evidence commands for the active first-shock unit-variance outputs. Release hardening can still package source and pin dependencies. |
| M8. Shareable draft | todo | Citations, provenance, checks, and exports are clean. |

## Review Plan

1. Scope and contribution: verify that the paper is a robustness-check note,
   not a broad higher-moment SVAR survey.
2. Notation and assumptions: audit the additive-noise model, scale
   normalization, relative noise-to-shock covariance screen, Gaussian-noise
   condition for robust transformed cumulants, and sign-labeling conventions.
3. Noisy sign-set review: check the covariance pseudo-set, column-rescaling
   obstruction, and intuition in the first figure.
4. Standard-DW misspecification review: M49 recovered the exact DW GMM1/GMM2
   moment object from raw source and derived the requested noisy product
   moments. M0050 cleaned the Section 3-4 notation. M54 completed the
   stepwise transformed-noise moment derivation and confirmed the retained
   `diag(B)=1` chart. M52 repaired the standard-DW evidence path. M47
   conditionally passed the M25 proof gate for rich-stack generic emptying,
   structural-coordinate rescaling exceptions, finite-GMM aliases,
   compactness, and nonsingularity.
5. Robust-DW derivation review: M40 conditionally passed the pre-M64 M0036 relative
   covariance-decomposition screen, including algebra, finite-sample
   equality-plus-inequality behavior, and the substantive interpretation of
    the 50 percent noise-to-shock variance bound. M66 updates this route for
   the unit-variance manuscript by using the dimensionless share
   `lambda_i=nu_i/(B B')_ii`, and M68 implements it in the first-shock figure
   and Monte Carlo diagnostics. M0050 made the robust
   restrictions read as moment conditions rather than visible cumulant notation
   while preserving the fourth-order covariance-product subtractions. M54
   completed the intermediate expansion steps and kept the current
   `diag(B)=1` chart. M55 completed the draft-level explanation of
   `Omega(B)`, `S(B)`, and candidate-by-candidate moment computation. M56
   supplied the generated-moment GMM route, and M52 implemented the full
   central-delta weighting. Future review should also focus on final-claim
   wording for the hard finite-sample screen.
6. Diagnostic interpretation review: use the M27 directional metric and verify
   that DW-versus-robust-DW divergence is described as a warning, not proof of
   literal measurement error.
7. Evidence design: treat the M68 Figure 1/Figure 2/Figure 3 sequence and
   Table 1 as the current diagnostic visual spine for the source-correct
   standard-DW GMM1 statistic and unit-variance robust generated-moment
   statistic. Final evidence still requires the projected critical-value note
   and replication hardening before confidence-set claims.
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
