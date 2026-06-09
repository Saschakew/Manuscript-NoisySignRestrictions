# M53 DW And Robust Moment Notation Rewrite

Status: `todo`

Priority: 1

Task-board row: `M53`

Transparency milestone: pending

## Original User Prompt

> plan a new task: Replace the notation as we just discussed. afterwards,
> extend the notation of moment conditions to section 4. that is i dont want
> to see the kumulants in section 4, but replace them using the moment
> condition notation.

Discussion immediately before this task:

> I don not like your h() notation in g_dw. Cant we use e_t(B)? I mean we now
> that at e_t(B_0)=epsilon_t at epsilon_t  has mean zero and unit variance by
> definition

## Why This Task Exists

M49 corrected the source content of the Drautzburg-Wright bivariate moment
menu, but the draft still introduces a new `h_i(B)` notation for the
centered, standardized recovered shocks in Section 3. The user wants the paper
to stay closer to the SVAR object already defined in Section 2:
`e_t(B)=B^{-1}u_t`. At the truth in the no-noise benchmark,
`e_t(B0)=epsilon_t`, and the structural shocks are mean zero with unit
variance by normalization.

The same readability issue appears in Section 4. The robust construction is
currently motivated through higher cumulants. Mathematically, the fourth-order
noise-robust restrictions still require covariance-product subtractions, but
the manuscript should present them as explicit GMM-style moment conditions
rather than foregrounding cumulant notation.

## Do Not Trust Without Rechecking

- The current Section 3 display that defines `h_i(B)` before `g_{DW,1}(B)`.
- Any rewrite that silently drops DW's source-standardization requirement.
- Any rewrite that makes Section 4 look like raw DW fourth-product moments;
  M49 showed that fourth raw products and noise-robust fourth conditions differ
  by covariance-product subtractions.
- Any global replacement of "cumulant" that would erase the mathematical
  reason the robust fourth-order conditions are Gaussian-noise-blind.
- The current Figure 1/M45 standard-DW evidence rows; M52 still owns the
  source-correct evidence rebuild.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/draft.md` | Locate Sections 3 and 4 notation and prose. | draft edits |
| `manuscript/derivations/m49-dw-source-and-noisy-moment-audit.md` | Preserve the source-correct DW GMM1/GMM2 menu and the raw-product versus robust-fourth-condition distinction. | any moment display rewrite |
| `manuscript/derivations/dw-noise-robust-moments.md` | Preserve the robust higher-order validity logic while changing notation. | Section 4 rewrite |
| `manuscript/formal-object-registry.json` | Update affected formal objects and open-audit status if the notation changes. | registry edits |
| `manuscript/paper-map.md` | Keep the reader path and Section 4 job aligned with the notation decision. | planning-surface edits |
| `manuscript/manuscript-rules.md` | Respect equation labels, object boundaries, and export discipline. | final draft edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| Section 3 should use `e_t(B)=B^{-1}u_t` rather than a new `h_i(B)` notation for the DW moment display. | `user-decision` plus `derived` | User instruction and Section 2 definition; no-noise identity `e_t(B0)=epsilon_t`. | pending |
| At the true no-noise impact matrix, `e_t(B0)=epsilon_t`, and `epsilon_t` is mean zero with unit variances by normalization. | `derived` | Section 2 model equations. | pending |
| The Section 3 DW moment display must remain source-correct: GMM1 has `112`, `122`, `1112`, `1122`, and `1222`; GMM2 drops only `1122`. | `raw-source` or `derived-from-M49` | M49 audit and Drautzburg-Wright source path recorded there. | pending |
| Section 4 can present the robust restrictions as explicit moment equations rather than visible cumulant symbols. | `user-decision` plus `derived` | User instruction plus M49/M24/M40 derivations showing which covariance-product subtractions are required. | pending |
| Replacing cumulant notation in Section 4 does not license replacing robust fourth conditions with DW raw fourth-product moments. | `derived` | M49 noisy-product derivations and `dw-noise-robust-moments.md`. | pending |

## Required Work

1. Section 3 notation rewrite:
   - Remove the `h_i(B)` display notation from the polished Section 3 text.
   - Use \(e_t(B)=B^{-1}u_t\) consistently in the DW GMM1 and GMM2 display.
   - State the normalization plainly: in the no-noise benchmark,
     \(e_t(B_0)=\varepsilon_t\), and \(\varepsilon_t\) is mean zero with unit
     variances by construction.
   - If candidate-level standardization is needed outside the source-native
     rotation chart, explain it in prose without introducing a competing
     headline notation.

2. Section 4 notation rewrite:
   - Replace visible cumulant notation in the main Section 4 display with a
     GMM-style moment vector, for example a robust vector whose entries are
     written directly as expectations and covariance-product subtractions.
   - Keep the third-order entries visually close to the DW-style raw moment
     conditions.
   - Write the fourth-order robust entries explicitly as moment conditions,
     such as raw fourth products minus the relevant covariance-product terms,
     without using `\kappa` as the displayed object.
   - Make clear that this is a notation and exposition change, not a switch
     back to DW raw fourth-product conditions.

3. Consistency pass:
   - Search `draft.md` for `h_i`, `h_1`, `h_2`, `kappa`, `cumulant`, and
     Section 4 moment labels.
   - Update the formal-object registry descriptions for the affected DW and
     robust moment-stack objects.
   - Update planning/provenance surfaces only where the notation decision
     changes reader-facing task status.

## Stop Conditions

- Stop if removing cumulant notation makes the robust fourth-order conditions
  mathematically ambiguous.
- Stop if Section 3 cannot use `e_t(B)` without losing the source-standardized
  DW interpretation; record the minimal extra notation needed instead.
- Stop if the rewrite would change the estimand or evidence code rather than
  only notation/prose.
- Stop before touching figures or Monte Carlo outputs; M52 owns the evidence
  rebuild.

## Acceptance Criteria

- Section 3 no longer introduces `h_i(B)` for the DW moment display.
- Section 3 displays the source-correct GMM1/GMM2 menus using recovered-shock
  notation based on \(e_t(B)\).
- Section 4 no longer foregrounds `\kappa` notation in the main robust moment
  display.
- Section 4 expresses robust third- and fourth-order restrictions as explicit
  moment conditions, including the necessary covariance-product subtractions
  for fourth-order terms.
- The rewrite preserves the M49 distinction between DW raw fourth products and
  robust fourth-order moment conditions.
- The formal registry and planning surfaces are updated if the displayed
  formal objects change.
- `python scripts/check_manuscript.py` passes after edits.

## Expected Outputs

- A focused edit to `manuscript/draft.md` in Sections 3 and 4.
- Registry updates for `def:standard-dw-refined-set`,
  `eq:standard-dw-j-test-inversion`, and
  `eq:dw-higher-cumulant-moment-stack` if their displayed notation changes.
- Updated planning/log surfaces marking M53 done and preserving M52 as the
  evidence rebuild gate.

## Outcome Log

Pending.
