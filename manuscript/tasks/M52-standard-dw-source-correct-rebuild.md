# M52 Standard-DW Source-Correct Rebuild

Status: `todo`

Priority: 1

Task-board row: `M52`

Created after: M49, because the source audit found that the current Figure 1
and M45 standard-DW code is a simplified hybrid rather than the source-correct
bivariate Drautzburg-Wright GMM1 or GMM2 higher-moment menu.

Blocked before execution by: M54. The stepwise transformed-noise moment
derivation and normalization audit must decide whether the manuscript keeps the
`diag(B)=1` common chart or creates a separate unit-variance/rotation-chart
rewrite task before this evidence rebuild starts.

## Original User Prompt

> /goal work on manuscript go on with M49 task

This follows the earlier user comments preserved in
`manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md`, especially the
concern that the paper may need to switch from `diag(B)` normalization to
`Var(epsilon)=1` normalization and then redo the figures and Monte Carlo.

## Why This Task Exists

M49 established that Drautzburg-Wright's bivariate GMM1 higher-moment menu is
`112`, `122`, `1112`, `1122`, and `1222`, while GMM2 drops only the symmetric
`1122` kurtosis condition. The current Figure 1 and M45 evidence code uses
covariance, `112`, `122`, and `1122`, omitting `1112` and `1222`. The existing
evidence therefore cannot be described as source-correct standard-DW evidence.

## Do Not Trust Without Rechecking

- Current `MOMENTS_DW = ((1, 1), (2, 1), (1, 2), (2, 2))` as a DW source
  menu.
- Current Figure 1, Figure 2, Figure 3, and M45 truth-inclusion rows as
  source-correct standard-DW evidence.
- Any chi-square degrees of freedom tied to the old four-moment standard-DW
  hybrid statistic.
- Any silent no-rebuild conclusion from M48.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/tasks/M54-stepwise-moment-derivation-and-normalization-audit.md` | Upstream derivation and normalization gate that must be completed before M52 starts. | all work |
| `manuscript/derivations/m49-dw-source-and-noisy-moment-audit.md` | Source-correct moment menu, noisy derivations, and rebuild alternatives. | all work |
| `manuscript/tasks/M49-dw-source-and-noisy-moment-audit.md` | Original user prompt and stop conditions. | scope decisions |
| `manuscript/simulations/sign_dw_robust_noise_grid_figure.py` | Figure 1 standard-DW implementation. | code edits |
| `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py` | Figure 2 reuse of base standard-DW implementation. | code edits |
| `manuscript/simulations/sign_dw_sample_size_robust_grid_figure.py` | Figure 3 reuse of base standard-DW implementation. | code edits |
| `manuscript/simulations/m45_variance_ratio_evidence.py` | Monte Carlo reuse of base standard-DW implementation and cutoffs. | evidence rebuild |
| `manuscript/draft.md` | Captions, Section 3, and evidence claims. | draft edits |
| `manuscript/formal-object-registry.json` | Affected formal objects and figure/table statuses. | registry edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The rebuilt standard-DW row implements bivariate DW GMM1 or GMM2. | `raw-source` plus `code-implemented` | M49 source menu and exact code path. | pending |
| The chosen chart is `diag(B)=1` common-chart or unit-variance/rotation chart. | `derived` plus `user-decision` if changing chart | Normalization comparison and user approval if the full chart changes. | pending |
| The rebuilt figures and Monte Carlo evidence support the same qualitative warning. | `code-implemented` plus simulation audit | Rerun outputs, diagnostics, and updated captions. | pending |

## Required Work

1. Confirm that M54 is complete and import its normalization recommendation:
   - smaller repair: keep `diag(B)=1`, add/source-correct the standard-DW
     higher menu in the common chart, and treat covariance as a separate
     no-noise B-plane screen;
   - larger rebuild: switch to the unit-variance/orthogonal-rotation chart and
     redesign the robust comparison in that chart.
2. Patch the standard-DW moment menu, targets, cutoffs, and labels.
3. Rerender Figure 1, Figure 2, and Figure 3 if the plotted accepted sets
   change.
4. Rerun an M45-style evidence table with the rebuilt standard-DW statistic.
5. Update draft captions, Section 3, citation provenance, formal registry,
   task board, dashboard, paper map, workplan, and logs.

## Stop Conditions

- Stop if the normalization choice requires a user decision not already given.
- Stop if M54 is not complete.
- Stop if the source-correct GMM1/GMM2 implementation cannot be mapped cleanly
  into the selected chart.
- Stop if old and rebuilt evidence diverge enough that the manuscript's
  Figure 1/Monte Carlo narrative needs redesign rather than local updating.

## Acceptance Criteria

- The chosen moment menu is named as GMM1, GMM2, or a clearly labeled
  manuscript hybrid.
- The code implements that menu explicitly and no longer calls the old hybrid
  source-correct DW.
- Figure/table captions state the chart, moment menu, and cutoff degrees of
  freedom.
- Rebuilt outputs are recorded in simulation notes and the formal registry.
- `python scripts/check_manuscript.py` passes after substantive edits.

## Expected Outputs

- Patched simulation/evidence scripts and regenerated outputs if needed.
- Updated draft/captions and evidence table.
- Updated planning, provenance, registry, and logs.

## Outcome Log

Pending.
