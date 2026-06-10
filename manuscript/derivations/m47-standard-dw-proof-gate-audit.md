# M47 Standard-DW Proof Gate Audit

Status: complete.

Date: 2026-06-10.

Task packet: `manuscript/tasks/M47-standard-dw-proof-gate-audit.md`.

## 1. Audit Outcome

M47 conditionally passes the M25 proof gate, with one important narrowing.
The M25 result is safe as a rich-stack benchmark under explicit ICA/rich-moment
and compactness conditions. It is not safe as an unconditional theorem about
the finite bivariate GMM1 implementation, because a finite third/fourth product
menu can have accidental aliases.

The manuscript should therefore state Proposition 2 as a conditional
misspecification result:

- in the common B-plane, the no-noise covariance screen generally rejects
  `B0` when transformed residual noise has off-diagonal covariance;
- in the source-native covariance-rotation chart, a rich no-noise independence
  stack has a population zero only when residual noise is equivalent to a
  diagonal structural-coordinate rescaling, up to sign and label conventions;
- if no population zero exists and the admissible set is compact and bounded
  away from singular matrices, fixed-critical-value inversion empties
  asymptotically;
- finite GMM1/GMM2 stacks remain source-correct diagnostics, not universal
  independence tests without an added no-alias condition.

## 2. Required Reads

| Path | Use in this audit |
|---|---|
| `knowledge-vault-link.json` | Confirmed the KnowledgeVault link and source status are initialized. |
| `manuscript/source-packet.md` | Confirmed M25 is still listed as a working derivation needing proof audit, and M52 is the active evidence gate. |
| `manuscript/project-dashboard.md` | Confirmed M47 is the next recommended action after M52. |
| `manuscript/paper-map.md` | Confirmed Section 3 is the proof bottleneck for theorem-level wording. |
| `manuscript/task-board.md` | Confirmed M47 status and next-action contract. |
| `manuscript/draft.md` | Located Proposition 2 and Section 3 source trails. |
| `manuscript/formal-object-registry.json` | Located `prop:standard-dw-misspecification` and the open M47 audit gate. |
| `manuscript/derivations/standard-dw-j-test-under-noise.md` | Audited the M25 working proof. |
| `manuscript/derivations/m49-dw-source-and-noisy-moment-audit.md` | Confirmed the source-correct bivariate GMM1/GMM2 menus and the B-plane covariance-screen distinction. |
| `manuscript/tasks/M52-standard-dw-source-correct-rebuild.md` | Confirmed M52 implemented GMM1 plus a separate covariance screen. |

## 3. Claim Audit Table

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| The no-noise covariance restriction generally fails at `B0` under residual noise. | `derived` | Section 4.1 below. | high | promote with the transformed-covariance exception visible. |
| A rich no-noise DW independence stack has no population zero under generic Gaussian residual noise except structural-coordinate rescaling cases. | `derived` | Sections 4.2 and 4.3 below, using the M25 argument and M49 source/menu clarification. | medium-high | promote only as a rich-stack/ICA benchmark, not as a finite-GMM1 theorem. |
| Fixed-critical-value inversion empties asymptotically when the population criterion is bounded away from zero on a compact admissible set. | `derived` | Section 4.4 below. | high | promote with compactness, nonsingularity, and `c_T/T -> 0` conditions. |
| Finite bivariate GMM1 can miss generic violations through finite-moment aliases. | `raw-source` plus `derived limitation` | M49 gives the finite GMM1 menu; Section 4.5 below explains why finite third/fourth moments are not a universal independence test. | high | keep alias caveat in Proposition 2 and evidence interpretation. |

## 4. Proof Audit

### 4.1 B-Plane Covariance Screen At The True Matrix

The active manuscript chart writes candidates as normalized impact matrices
`B`. At the true matrix,

```text
e_t(B0) = B0^{-1}u_t = epsilon_t + B0^{-1}eta_t.
```

Let

```text
Omega0 = B0^{-1} V B0^{-1'}.
```

Because the structural shocks are independent and have diagonal covariance,

```text
Cov(e_t(B0)) = I + Omega0.
```

The standard no-noise covariance screen requires the off-diagonal covariance
to be zero. At `B0`, that off-diagonal entry is `Omega0_12`. Therefore `B0`
fails the B-plane no-noise covariance screen unless residual noise is diagonal
in structural coordinates, up to the accepted sign and label convention. This
part of M25 passes directly.

### 4.2 Rich Higher-Moment Stack

For a general candidate,

```text
e_t(B) = B^{-1}B0 epsilon_t + B^{-1}eta_t
       = A(B) epsilon_t + xi_t(B).
```

If `eta_t` is Gaussian and independent of `epsilon_t`, then `xi_t(B)` is
Gaussian and independent of `A(B)epsilon_t`. Higher cumulants of `e_t(B)` are
therefore the higher cumulants of `A(B)epsilon_t`.

The rich-stack step requires an explicit condition:

```text
If the chosen no-noise higher-moment stack is rich enough to force
independence of the recovered components, and the structural shocks satisfy
the usual ICA non-Gaussian rank condition, then A(B)epsilon_t independent
component-by-component implies A(B)=D Pi.
```

Here `D` is nonsingular diagonal and `Pi` is a signed permutation matrix
consistent with the maintained labeling. This is a condition on the proof
object, not a property of every finite third/fourth GMM menu.

### 4.3 Structural-Coordinate Rescaling Exception

In the source-native covariance-rotation chart, candidates satisfy

```text
B(Q)B(Q)' = Sigma_u = B0 B0' + V.
```

If the rich stack has a zero, Section 4.2 gives

```text
B(Q)^{-1}B0 = D Pi,
```

so

```text
B(Q) = B0 Pi' D^{-1}.
```

Combining this with `B(Q)B(Q)'=Sigma_u` yields

```text
B0^{-1} V B0^{-1'} = Pi' D^{-2} Pi - I.
```

The right side is diagonal up to sign and label. Hence a source-native
population zero requires residual noise to be observationally equivalent to a
diagonal structural-coordinate rescaling. Generic residual covariance violates
this because `Omega0` has a nonzero off-diagonal entry.

In the common B-plane with a separate covariance screen, the same exception is
visible in a slightly weaker form. If the rich stack forces
`B^{-1}B0=D Pi`, then the covariance screen reduces to the off-diagonal entries
of

```text
D Pi Omega0 Pi' D.
```

Those off-diagonal entries vanish only when `Omega0` is diagonal up to the
accepted label convention. The additional `diag(B)=1` reporting chart fixes
scale further, so it does not weaken the generic-noise warning.

### 4.4 Emptying Of Fixed-Critical-Value Inversion

Let `Theta` be the reported sign-admissible candidate set after excluding
singular matrices and any unlabeled boundary region. Assume `Theta` is compact,
`g_infty(B)` is continuous, and the population weighting matrix is positive
definite on the moment stack. If there is no population zero on `Theta`, then

```text
delta = inf_{B in Theta} g_infty(B)' W g_infty(B) > 0.
```

Under a uniform law of large numbers for the sample moments and a uniformly
consistent weight estimate,

```text
sup_{B in Theta} |J_T(B)/T - J_infty(B)| -> 0
```

in probability. If the inversion uses fixed critical values, or more generally
`c_T/T -> 0`, then with probability approaching one

```text
inf_{B in Theta} J_T(B) > c_T.
```

The accepted set is therefore empty asymptotically. This part of M25 passes
only with the compactness and nonsingularity conditions stated. Without them,
a sequence near a singular boundary or outside the reported grid could defeat
the bounded-away argument.

### 4.5 Finite GMM1 Alias Caveat

M49 source-audits the bivariate finite menus:

```text
GMM1: 112, 122, 1112, 1122, 1222
GMM2: 112, 122, 1112, 1222
```

These are source-correct finite moment vectors, but finite third and fourth
standardized raw products are not a universal independence characterization.
Aliases can arise when relevant third/fourth cumulants are zero or cancel,
when the shocks differ only through higher moments not in the stack, or when
sign/label restrictions do not rule out a pseudo-rotation. The manuscript can
use GMM1 as the implemented source-correct comparator and can show its
misspecification behavior in M52 simulations, but theorem-level generic
emptying needs either the rich-stack benchmark or an explicit finite-stack
no-alias condition.

## 5. Implications For Draft Language

Proposition 2 can move from "working sketch pending M25 audit" to
"conditional proof-audited proposition" if the draft keeps the caveats in the
statement:

- Gaussian residual noise for the clean rich-stack proof;
- rich independence stack plus ICA rank condition, or else a finite-stack
  no-alias assumption;
- structural-coordinate diagonal-rescaling exception;
- compact sign-admissible set bounded away from singularity;
- finite-sample least-rejected pseudo-target interpretation.

The implemented M52 standard-DW GMM1 row should remain described as
source-correct finite-stack evidence, not as proof that finite GMM1 always
empties under generic residual noise.

## 6. Outcome Log

- Claim ledger: all four M47 packet claims resolved.
- Result: conditional pass. M25 is adequate for Proposition 2 after adding the
  compactness/nonsingularity and finite-alias caveats to the draft and formal
  registry.
- Remaining uncertainty: final publication proof may still want an appendix
  presentation, but the main-text theorem-level blocker is cleared if the
  result is kept conditional.
