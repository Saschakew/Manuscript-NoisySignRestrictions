# M55 Main-Text Robust Moment Explanation

Status: `todo`

Priority: 1

Task-board row: `M55`

Created after: M54, because the stepwise derivation is correct enough to use
as an audit trail, but the main text still needs a reader-facing derivation
that explains why the robust moment conditions hold at `B0` and how the
moment entries are computed.

## Original User Prompt

> Update the plan: This is something we need to properly explaind and derive
> in the main text. same for the whole computation of the moments in your
> 54-stepwise-transformed.noise-moments.md. like we dont need to do show every
> single calculation for every moment, but we need to make it clear in the
> draft why the moment conditions hold at B_0 and why they make sense.

The prompt followed the user's correction that the notation can make
`s_{ij}` look like entries of the transformed-noise covariance
`Var(B^{-1} eta_t)`, whereas the implementable fourth-order cumulant
subtractions use the covariance entries of the full transformed observed
residual `z_t(B)=B^{-1}u_t`.

## Why This Task Exists

M54 derives the transformed-noise moments step by step, but the draft cannot
send readers to a long derivation note for the central validity intuition. The
main text needs a compact explanation that:

- defines the full transformed residual `z_t(B)` and the transformed-noise
  component `xi_t(B)=B^{-1}eta_t`;
- distinguishes `Omega_{ij}(B)=E[xi_i(B)xi_j(B)]` from
  `S_{ij}(B)=E[z_i(B)z_j(B)]`;
- explains that the robust fourth-order subtractions use `S_{ij}(B)`, not the
  unobserved noise covariance alone;
- shows why Gaussian transformed noise leaves higher cumulants above order two
  equal to zero at `B=B0`;
- gives enough bivariate algebra to make the displayed moment equations
  believable without expanding every product in the main text; and
- explains how the sample moments are computed for each candidate `B`.

## Do Not Trust Without Rechecking

- Any draft wording that makes `s_{ij}(B)` sound like the covariance of
  transformed noise alone.
- Any draft wording that says raw fourth products are robust under Gaussian
  residual noise without the covariance-product subtractions.
- Any notation that uses the same symbol `s_i` for structural-shock variances
  in the variance-ratio screen and `s_{ij}` for transformed-residual
  covariances without warning the reader.
- Any implementation explanation that implies `S_{12}(B)=0` is imposed as a
  robust restriction. It is only estimated as a nuisance plug-in for fourth
  cumulants.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/draft.md` | Locate and revise the Section 4 moment explanation. | draft edits |
| `manuscript/derivations/m54-stepwise-transformed-noise-moments.md` | Source derivation for the main-text explanation. | all mathematical edits |
| `manuscript/derivations/dw-noise-robust-moments.md` | Earlier robust cumulant derivation and moment stack. | all mathematical edits |
| `manuscript/formal-object-registry.json` | Affected formal objects and status wording. | registry edits |
| `manuscript/manuscript-rules.md` | Equation labels, object boundaries, and export discipline. | draft edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| At `B=B0`, `z_t(B0)=epsilon_t+xi_t` with `xi_t=B0^{-1}eta_t`. | `derived` | M54 notation and model equations. | pending |
| If residual noise is Gaussian and independent of the shocks, transformed-noise cumulants above order two vanish. | `derived` | Linear transformation of Gaussian noise plus M54. | pending |
| The fourth-order robust conditions subtract products of `S_{ij}(B)=E[z_i(B)z_j(B)]`, not products of `Omega_{ij}(B)` alone. | `derived` | M54 equations and cumulant algebra. | pending |
| The sample implementation computes `S_{ij}(B)` from centered `z_t(B)=B^{-1}u_t` for every candidate `B`. | `code-implemented` only if tied to scripts; otherwise `derived` for formula | M54 plus relevant simulation code if cited. | pending |

## Required Work

1. Draft work:
   - revise Section 4 so the reader sees the logic in text before the moment
     stack;
   - include the `Omega(B)` versus `S(B)` distinction explicitly;
   - explain at least one representative fourth-order equation, preferably
     `E[z_1z_2^3]-3S_{22}S_{12}=0`, and state that the other fourth-order
     entries follow by the same cumulant-product logic.
2. Derivation work:
   - verify the displayed equations against M54;
   - make the third-order and fourth-order cases conceptually separate:
     third moments vanish under Gaussian residual noise, while raw fourth
     moments need covariance-product subtraction.
3. Computation explanation:
   - add a concise sample recipe: transform residuals by candidate `B`, center
     them, compute sample `S_{ij}(B)`, then plug those entries into the
     moment equations;
   - avoid implying that the unobserved `eta_t` or `xi_t` must be recovered in
     applications.
4. Registry and plan updates:
   - update formal-object status if Section 4 is revised;
   - update dashboard, task board, workplan, paper map, source packet, and logs
     after the draft change.

## Stop Conditions

- Stop if the notation cannot avoid collision between structural-shock
  variances and transformed-residual covariance entries.
- Stop if the derivation would require observing or estimating `eta_t`
  directly for the robust moment stack.
- Stop if the main-text simplification hides a substantive assumption, such as
  Gaussian residual noise or independence from structural shocks.

## Acceptance Criteria

- Section 4 states why the robust moment conditions hold at `B0`.
- Section 4 distinguishes `Omega(B)=Var(B^{-1}eta_t)` from
  `S(B)=Var(B^{-1}u_t)`.
- Section 4 states that `S_{ij}(B)` is computed from candidate transformed
  residuals and is a nuisance plug-in, not a zero-covariance restriction.
- The main text gives enough algebra for at least one fourth-order moment to
  make the covariance-product subtraction intelligible.
- `python scripts/check_manuscript.py` passes after substantive edits.

## Expected Outputs

- Revised Section 4 in `manuscript/draft.md`.
- Updated formal-object registry status for the robust moment stack and
  validity proposition.
- Updated planning/log surfaces recording the completed clarification.

## Outcome Log

Pending.
