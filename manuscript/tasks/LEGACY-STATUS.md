# Legacy Task Status

Purpose: make old flat task packets easier to scan without migrating them into
folders. This file labels legacy artifacts by current use.

## Status Labels

- `current-reference`: completed work that is still part of the active
  manuscript state.
- `superseded-reference`: completed or partial work that remains useful for
  history, but another task is the current authority.
- `template-historical`: an old template retained for provenance; use the new
  folder template instead.

## Legacy Flat Packets

| File | Status | Current use | First place to read now |
|---|---|---|---|
| `_template.md` | `template-historical` | Old flat packet template. Keep for provenance only. | `_folder-template/task.md` and `_folder-template/outcome.md` |
| `M47-standard-dw-proof-gate-audit.md` | `current-reference` | Completed standard-DW proof gate audit; supports Proposition 2 caveats. | `../derivations/m47-standard-dw-proof-gate-audit.md` |
| `M49-dw-source-and-noisy-moment-audit.md` | `current-reference` | Completed source-backed DW moment-menu and noisy-product audit. | `../derivations/m49-dw-source-and-noisy-moment-audit.md` |
| `M52-standard-dw-source-correct-rebuild.md` | `current-reference` | Completed source-correct evidence rebuild task. | `../simulations/m52_source_correct_evidence.md` |
| `M53-dw-and-robust-moment-notation-rewrite.md` | `current-reference` | Completed notation rewrite for DW recovered shocks and robust moment equations. | `../draft.md` |
| `M54-stepwise-moment-derivation-and-normalization-audit.md` | `current-reference` | Completed stepwise transformed-noise derivation and normalization audit. | `../derivations/m54-stepwise-transformed-noise-moments.md` |
| `M55-main-text-robust-moment-explanation.md` | `current-reference` | Completed Section 4 explanation task. | `../draft.md` |
| `M56-robust-cumulant-gmm-generated-moment-audit.md` | `current-reference` | Completed generated-moment audit for robust cumulant GMM. | `../derivations/m56-robust-cumulant-gmm-generated-moment-audit.md` |

## Related Historical Artifact

| File | Status | Current use | First place to read now |
|---|---|---|---|
| `../derivations/m48-dw-moment-normalization-audit.md` | `superseded-reference` | Historical partial audit. It should not be used as the source-correct DW authority. | `../derivations/m49-dw-source-and-noisy-moment-audit.md` |

## Rule

Do not migrate these files unless a legacy task is reopened or the user asks
for an archival pass. When a legacy task is reopened, create a new folder and
link the old packet from the new `task.md` or `outcome.md`.

