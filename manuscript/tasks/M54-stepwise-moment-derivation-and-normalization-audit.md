# M54 Stepwise Moment Derivation And Normalization Audit

Status: `todo`

Priority: 1

Task-board row: `M54`

Transparency milestone: pending

## Original User Prompt

> i think you skipped some steps in between. plan a task to derive these moment
> conditions carefully and step by step in our manuscript. the same task should
> also verify if we switch to the unit variance epsilon normalization or do we
> still use diag(B) normalization? if we switched to unit variance: do we need
> to plan a task to consitently update accross the document? like if we switched
> to unit variance, then the moment conditions in section 2 should contain unit
> variance moment conditions.

The discussion immediately before this task asked for the transformed-noise
moments at \(B=B_0\) after inserting
\[
z_t(B_0)=B_0^{-1}u_t=\varepsilon_t+B_0^{-1}\eta_t.
\]
The user specifically named moment patterns:
\[
E[z_1^2z_2],\quad
E[z_1z_2z_3],\quad
E[z_1^3z_2],\quad
E[z_1^2z_2^2],\quad
E[z_1^2z_2z_3],\quad
E[z_1z_2z_3z_4].
\]

## Why This Task Exists

M0050 rewrote Section 4 so the robust stack is displayed as moment equations,
but the draft still does not show a careful step-by-step derivation of those
conditions at the truth. The previous chat derivation skipped intermediate
expansion steps and did not fully separate three layers:

1. structural shocks \(\varepsilon_i\) are independent, mean zero, and have
   unit variance under the structural normalization;
2. residual-noise components \(\eta_i\) may be independent in the residual
   coordinates, but transformed noise
   \(\xi=B_0^{-1}\eta\) generally has correlated components;
3. Gaussian residual noise is a stronger condition than independent residual
   components and is what turns fourth transformed-noise moments into
   covariance-product terms by Isserlis' formula.

The same task must also audit the normalization decision. The active manuscript
uses a diagonal-normalized \(B\)-chart for the robust comparison and profiles
structural-shock variances in the variance-ratio screen. Drautzburg-Wright's
source-native chart instead uses unit-variance shocks and covariance-normalized
rotations. If the paper switches to a unit-variance/rotation chart, Section 2,
Section 4, figures, simulations, and registry objects must be updated
consistently; this should not happen silently inside a local derivation edit.

## Do Not Trust Without Rechecking

- The chat derivation that gave only final formulas for the requested moment
  patterns.
- Any formula that treats independent components of \(\eta\) as implying
  independent components of \(B_0^{-1}\eta\).
- Any formula that uses Gaussian fourth-moment covariance products without
  explicitly assuming Gaussian residual noise, zero fourth cumulants, or a
  modeled residual-noise fourth-cumulant correction.
- Any Section 4 moment display that looks like a raw DW fourth-product target
  rather than a robust fourth-order condition with covariance-product
  subtractions.
- Any normalization discussion that treats `diag(B)=1` and
  `Var(epsilon)=I` as simultaneously available scale restrictions.
- Any local switch to unit-variance normalization that does not also plan
  updates to Section 2 moment conditions, Section 4 covariance screen, figure
  coordinates, simulation code, captions, formal registry, and evidence tasks.
- M52's evidence rebuild path until this M54 normalization audit has either
  endorsed the current chart or created the follow-up chart-switch task.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/draft.md` | Locate Sections 2-4 and the current robust moment display. | derivation and draft update planning |
| `manuscript/derivations/m49-dw-source-and-noisy-moment-audit.md` | Preserve the DW raw-product versus robust fourth-condition distinction and the normalization alternatives. | all derivations |
| `manuscript/derivations/dw-noise-robust-moments.md` | Compare against the existing robust higher-moment derivation and scale-profiled screen. | derivation work |
| `manuscript/derivations/m40-variance-ratio-robust-dw-screen-audit.md` | Check how the variance-ratio screen depends on the diagonal-normalized chart. | normalization audit |
| `manuscript/formal-object-registry.json` | Locate affected assumptions, equations, propositions, and open audits. | registry edits |
| `manuscript/paper-map.md` | Keep the reader path aligned with the normalization decision. | planning-surface edits |
| `manuscript/manuscript-rules.md` | Respect labels, formal-object boundaries, and source-gate discipline. | draft or registry edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| At \(B=B_0\), \(z_t=\varepsilon_t+\xi_t\) with \(\xi_t=B_0^{-1}\eta_t\). | `derived` | Section 2 model equation and direct substitution. | pending |
| Independent residual-noise components \(\eta_i\) do not generally imply independent transformed-noise components \(\xi_i\). | `derived` | Matrix expression \(\xi_i=\sum_a (B_0^{-1})_{ia}\eta_a\) and covariance calculation. | pending |
| The expansions for \(E[z_1^2z_2]\), \(E[z_1z_2z_3]\), \(E[z_1^3z_2]\), \(E[z_1^2z_2^2]\), \(E[z_1^2z_2z_3]\), and \(E[z_1z_2z_3z_4]\) follow by expanding products and eliminating terms with unmatched centered independent structural shocks. | `derived` | Written step-by-step derivation, not only final formulas. | pending |
| Under Gaussian residual noise, the third transformed-noise moments vanish and the fourth transformed-noise moments reduce to covariance-product terms. | `derived` | Isserlis' formula applied to \(\xi=B_0^{-1}\eta\). | pending |
| Without Gaussian residual noise, or another zero higher-cumulant condition, extra transformed-noise third/fourth cumulant terms remain. | `derived` | Expansion in transformed-noise moments or in \(B_0^{-1}\) rows and residual-noise component moments. | pending |
| The active manuscript can remain in the `diag(B)=1` common chart only if it clearly profiles structural-shock variances in second-moment screens and treats unit-variance standardization separately for DW recovered-shock products. | `derived` plus `user-decision` if retained after audit | M49 normalization audit, M40 screen audit, and draft consistency check. | pending |
| If the manuscript switches to a unit-variance/rotation chart, Section 2 must include the unit-variance recovered-shock moment conditions, not only zero covariance. | `derived` plus `user-decision` if switching | No-noise SVAR normalization and source-native DW chart. | pending |
| A full unit-variance chart switch requires a separate manuscript-wide update task. | `derived` plus `user-decision` | Dependency list across draft, figures, simulations, registry, and evidence tasks. | pending |

## Required Work

1. Set up notation carefully:
   - Write \(C=B_0^{-1}\), \(\xi=C\eta\), and
     \(z_i=\varepsilon_i+\xi_i\) at \(B=B_0\).
   - State mean, variance, and independence assumptions explicitly:
     \(E\varepsilon_i=0\), \(E\varepsilon_i^2=1\),
     independent structural components, \(E\eta_a=0\), independent residual
     components in residual coordinates, and \(\eta\perp\varepsilon\).
   - Decide whether the derivation is for general \(K\), for \(K=4\) patterns,
     or for the bivariate manuscript with repeated indices. The named
     \(z_3,z_4\) patterns require a general-index derivation even if the main
     manuscript remains bivariate.

2. Derive the requested raw moments step by step:
   - For each requested moment, expand the product fully enough to show which
     terms vanish by mean zero and independence.
   - First give the result in terms of transformed-noise raw moments such as
     \(E[\xi_i\xi_j]\), \(E[\xi_i\xi_j\xi_k]\), and
     \(E[\xi_i\xi_j\xi_k\xi_l]\).
   - Then specialize to Gaussian residual noise and write the covariance-product
     forms using \(s_{ij}=E[z_i z_j]\) or \(\Omega_{ij}=E[\xi_i\xi_j]\).
   - Include, at minimum, these patterns:
     \(E[z_1^2z_2]\), \(E[z_1z_2z_3]\),
     \(E[z_1^3z_2]\), \(E[z_1^2z_2^2]\),
     \(E[z_1^2z_2z_3]\), and \(E[z_1z_2z_3z_4]\).

3. Derive the robust moment conditions:
   - State which third-order raw moments are valid zero restrictions under
     Gaussian residual noise.
   - State which fourth-order raw moments are not zero restrictions and must be
     converted into covariance-product corrected conditions.
   - Make the distinction between DW raw fourth products and robust fourth-order
     conditions explicit.
   - If non-Gaussian residual noise is allowed, write what additional nuisance
     transformed-noise cumulants would have to be modeled or ruled out.

4. Audit normalization:
   - Compare the current `diag(B)=1` normalized chart with the
     unit-variance/rotation chart.
   - Check whether Section 2 currently states enough unit-variance moment
     conditions for the chart being used.
   - Check whether Section 4's variance-ratio covariance screen relies on the
     diagonal-normalized chart and profiled structural variances.
   - Produce a clear recommendation:
     keep `diag(B)=1` for the first paper, switch to unit-variance/rotation
     chart, or defer the chart switch as a user-decision gate.

5. Plan follow-up if needed:
   - If the recommendation is to switch to unit-variance/rotation
     normalization, do not perform the switch inside M54 unless explicitly
     requested.
   - Instead, create a separate packet-backed follow-up task for the
     manuscript-wide normalization rewrite. That follow-up must include Section
     2 unit-variance moment conditions, Section 4 covariance screen redesign,
     figure coordinate redesign, simulation code updates, captions, registry,
     and evidence rebuilds.
   - If the recommendation is to keep `diag(B)=1`, update M52's packet so the
     evidence rebuild uses that decision rather than reopening the chart choice.

6. Manuscript update work:
   - Create or update a derivation note under `manuscript/derivations/`.
   - Update `draft.md` only if the derivation supports a clear prose or display
     correction.
   - Update the formal registry and planning surfaces after the derivation
     gate is complete.

## Stop Conditions

- Stop if a formula depends on Gaussian residual noise but the derivation has
  not explicitly invoked Gaussianity or zero higher transformed-noise cumulants.
- Stop if the derivation treats \(\xi=B_0^{-1}\eta\) as componentwise
  independent merely because \(\eta\) has independent components.
- Stop if the normalization audit implies a chart switch but the user has not
  approved that switch.
- Stop before editing figures, Monte Carlo outputs, or simulation evidence;
  M52 or a new chart-switch task owns those rebuilds.
- Stop if Section 2 and Section 4 cannot be made consistent under the chosen
  normalization without a broader manuscript rewrite.

## Acceptance Criteria

- A derivation note shows the requested moment expansions step by step,
  including intermediate vanishing-term logic.
- The note separately reports general transformed-noise moment formulas and
  Gaussian-noise covariance-product special cases.
- The robust third- and fourth-order moment conditions are stated without
  confusing them with DW raw fourth-product moments.
- The normalization audit states whether the manuscript should keep the
  `diag(B)=1` chart or switch to a unit-variance/rotation chart.
- If a chart switch is recommended, a separate packet-backed follow-up task is
  created before M54 is marked done.
- If `diag(B)=1` is retained, M52 is updated to depend on the M54 decision and
  no longer reopens the same normalization question.
- `python scripts/check_manuscript.py` passes after substantive edits.

## Expected Outputs

- A derivation note, likely
  `manuscript/derivations/m54-stepwise-transformed-noise-moments.md`.
- A normalization recommendation recorded in the derivation note and planning
  surfaces.
- Updates to `manuscript/draft.md` only if supported by the derivation.
- Formal registry updates for `ass:unit-variance-normalization`,
  `eq:no-noise-sign-j-set`, `eq:dw-higher-cumulant-moment-stack`, and related
  robust-DW objects if their status or displayed interpretation changes.
- Task-board/dashboard updates that put M54 before M52.
- Optional new follow-up task if a full unit-variance chart switch is selected
  or recommended.

## Outcome Log

Pending.
