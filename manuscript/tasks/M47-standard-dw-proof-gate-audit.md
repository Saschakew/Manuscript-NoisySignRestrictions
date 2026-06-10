# M47 Standard-DW Proof Gate Audit

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M47`

Transparency milestone: `M0058-m47-standard-dw-proof-gate-audit`

GitHub milestone: `53` (`https://github.com/Saschakew/Manuscript-NoisySignRestrictions/milestone/53`)

## Original User Prompt

User resumed the manuscript goal: "go on. afterwards, go on with the nex topen
task in /goal mode". The dashboard-selected next open task after M52 is M47:
audit the M25 standard-DW proof gate.

## Why This Task Exists

The draft's standard-DW misspecification result still rests on the M25 working
derivation. M49 repaired the source menu for the DW moment stack and M52 rebuilt
the evidence path, so the remaining proof gate is no longer a code/menu issue.
The manuscript now needs a direct mathematical audit of the M25 claims before
Proposition 2 can be promoted beyond sketch language.

## Do Not Trust Without Rechecking

- The M25 derivation is a working proof artifact, not yet audited for theorem
  language.
- Any claim that a "rich" DW stack generically empties under residual noise
  must be checked against structural-coordinate rescaling exceptions.
- Any finite-stack statement must keep finite-moment aliases visible rather
  than smoothing them into a generic population claim.
- Compactness and bounded-away-from-singularity steps must be stated explicitly
  if fixed-critical-value J-test inversion is said to empty asymptotically.
- The source-correct bivariate DW GMM1 menu from M49/M52 is now the active
  comparator; older hybrid standard-DW evidence is historical only.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm vault and source paths. | any source-sensitive claim |
| `manuscript/source-packet.md` | Locate source packet and active evidence status. | audit framing |
| `manuscript/project-dashboard.md` | Confirm current stage and next action. | task execution |
| `manuscript/paper-map.md` | Confirm where the proof fits the argument. | draft or registry edits |
| `manuscript/task-board.md` | Confirm M47 status and dependencies. | task execution |
| `manuscript/draft.md` | Locate Proposition 2 and Section 3 language. | draft edits |
| `manuscript/formal-object-registry.json` | Locate formal objects and open audit state. | registry edits |
| `manuscript/derivations/standard-dw-j-test-under-noise.md` | M25 working derivation to audit. | proof audit |
| `manuscript/derivations/m49-dw-source-and-noisy-moment-audit.md` | Source-correct DW moment menu and noisy products. | source-to-proof mapping |
| `manuscript/tasks/M52-standard-dw-source-correct-rebuild.md` | Active evidence rebuild outcome. | evidence references |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The no-noise covariance restriction generally fails at `B0` when residual noise is added. | `derived` | Direct covariance expansion under the active `diag(B)=1` chart. | passed: `Omega0_12` is the obstruction |
| A rich enough no-noise DW moment stack generically has no population zero under residual noise except structural-coordinate rescaling or finite-moment alias cases. | `derived` | Audit of M25 with explicit exceptional sets and maintained assumptions. | conditionally passed for rich-stack/ICA wording |
| Fixed-critical-value J-test inversion empties asymptotically when the population criterion is bounded away from zero on the admissible compact set. | `derived` | Compactness and lower-bound argument, with singular chart exclusions stated. | passed with compactness and nonsingularity stated |
| Finite bivariate GMM1 can miss generic violations through finite-moment aliases. | `derived` plus `raw-source`/`vault-source` for the GMM1 menu | M49 source menu plus audit of finite-moment limitations. | passed as limitation: keep alias caveat |

## Required Work

1. Source work: confirm the active DW GMM1/GMM2 menu from M49 and whether M25
   uses source-correct or deliberately richer moment stacks.
2. Derivation work: audit the covariance failure, rich-stack generic emptying,
   structural-rescaling exception, finite-moment aliases, and compactness/
   bounded-away-from-zero step.
3. Code or simulation work: none required unless the proof audit needs a quick
   symbolic or numerical sanity check; code output cannot replace derivation.
4. Manuscript update work: write an audit note, update the packet ledger,
   formal registry, task board, dashboard/map/plan/source packet, and draft
   language only to the level supported by the audit.

## Stop Conditions

- Stop if the proof needs a source object that cannot be found in M49, the raw
  source, or the vault source packet.
- Stop if the rich-stack claim requires a stronger distributional assumption
  than the manuscript currently states.
- Stop if the compactness step fails unless the admissible parameter set is
  narrowed or the singular boundary is excluded.
- Stop if finite GMM1 aliases prevent any theorem-level finite-stack claim;
  weaken the draft and record the limitation instead.

## Acceptance Criteria

- The audit note states assumptions, normalization, and exceptions explicitly.
- Each claim ledger row is resolved as pass, weakened, failed, or follow-up.
- Draft and registry changes do not promote claims beyond the audit result.
- M47 is marked done only if the proof gate has a clear pass or a safe
  weakened replacement.
- `python scripts/check_manuscript.py` passes after substantive edits.

## Expected Outputs

- `manuscript/derivations/m47-standard-dw-proof-gate-audit.md`
- Updated `manuscript/draft.md` Section 3 and/or proof wording if supported.
- Updated `manuscript/formal-object-registry.json`, task board, dashboard,
  paper map/plan, source packet, provenance if needed, and logs.

## Outcome Log

### 2026-06-10

- Outcome: completed `manuscript/derivations/m47-standard-dw-proof-gate-audit.md`.
- Result: conditional pass. Proposition 2 can be stated as a proof-audited
  rich-stack misspecification result if it keeps Gaussian residual noise, the
  ICA/rich-moment condition, structural-coordinate rescaling exceptions,
  finite-GMM alias caveats, compactness, and nonsingularity visible.
- Draft consequence: Section 3 now states Proposition 2 with compactness and
  finite-alias caveats and removes the stale unaudited TODO.
- Registry consequence: `prop:standard-dw-misspecification` is
  `proof-audited-after-m47`, and the open standard-DW proof audit gate is
  cleared.
- Next task: M33 replication wrapper.
