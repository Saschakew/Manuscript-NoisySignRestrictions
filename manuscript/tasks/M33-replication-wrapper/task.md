# M33 Replication Wrapper

## Status And Routing

Status: `done`

Priority: 2

Task-board row: `M33`

Transparency milestone: `M0060-m33-replication-wrapper`

GitHub milestone: `#55`

Outcome note: `outcome.md`

## Original User Prompt

"i justfinished Revision-20260610-190805. work on it. first get an overview what needs to get done and work in a structured way"

Follow-up after interruption: "go on"

## Why This Task Exists

The post-revision overview routes the next substantive manuscript task to
M33: build a manuscript-local replication wrapper so the active M52 figures
and table can be rebuilt from `manuscript/replication/` without depending on a
local KnowledgeVault checkout. The remote branch
`Revision-20260610-190805` only added revision metadata, so it should be
preserved without displacing the current `main` cleanup and M33 routing.

## Do Not Trust Without Rechecking

- Historical M29 output used the superseded diagonal-anchor robust row.
- Historical M45 output predates the M52 source-correct standard-DW and
  central-delta robust evidence rebuild.
- Quick or smoke replication outputs are operational checks only, not evidence
  for manuscript claims.
- A wrapper that calls manuscript-local scripts is not yet the same as a fully
  standalone release package with copied source code and pinned external
  artifacts.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm vault/package status and no local-vault dependency in final wrapper. | task execution |
| `manuscript/source-packet.md` | Confirm active evidence and package provenance. | task execution |
| `manuscript/project-dashboard.md` | Confirm M33 is the next recommended action. | task execution |
| `manuscript/paper-map.md` | Confirm active figures, table, and bottlenecks. | task execution |
| `manuscript/task-board.md` | Confirm M33 row and dependencies. | task execution |
| `manuscript/replication/README.md` | Current replication package plan. | wrapper design |
| `manuscript/simulations/README.md` | Active script commands and historical/superseded outputs. | wrapper design |
| `manuscript/simulations/sign_dw_relative_noise_robust_grid_figure.md` | Figure 1 source command and diagnostics. | figure wrapper |
| `manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.md` | Figure 2 source command and diagnostics. | figure wrapper |
| `manuscript/simulations/sign_dw_sample_size_robust_grid_figure.md` | Figure 3 source command and diagnostics. | figure wrapper |
| `manuscript/simulations/m52_source_correct_evidence.md` | Active Table 1 evidence note and configuration. | evidence wrapper |
| `manuscript/formal-object-registry.json` | Figure/table object source references. | registry updates |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The M33 wrapper rebuilds the active Figure 1, Figure 2, Figure 3, and M52 evidence outputs by calling manuscript-local scripts. | `code-implemented` | `manuscript/replication/run_all.py`; dry-run and quick smoke command output | complete |
| The M33 wrapper does not depend on a local KnowledgeVault checkout. | `code-implemented` | Imports and subprocess commands in `run_all.py`; requirements file | complete |
| Quick-mode outputs are smoke checks only and do not replace the canonical M52 evidence outputs. | `user-decision` / `code-implemented` | `run_all.py` output routing and README wording | complete |

## Required Work

1. Preserve the `Revision-20260610-190805` metadata on current `main`.
2. Add output-path hooks to active simulation scripts where needed.
3. Add `manuscript/replication/run_all.py` with stage, quick, dry-run, and
   output-dir controls.
4. Update replication README and requirements.
5. Link M33 to this task folder from `manuscript/task-board.md`.
6. Update registry/planning/log surfaces only where the wrapper changes the
   traceability of figures or evidence.
7. Write `outcome.md` and decide whether `QUESTION-INDEX.md` needs a row.
8. Run focused smoke checks and `python scripts/check_manuscript.py`.

## Stop Conditions

- Stop if the active scripts require KnowledgeVault paths or unavailable local
  state.
- Stop if a wrapper command rewrites canonical evidence with quick settings.
- Stop if smoke outputs disagree with the intended active M52 configuration in
  a way that changes manuscript evidence claims.
- Stop if dependency installation or external package pinning becomes
  necessary and cannot be completed inside the current environment.

## Acceptance Criteria

- `manuscript/replication/run_all.py --dry-run` lists the canonical rebuild
  commands.
- A quick evidence smoke run writes to `manuscript/replication/output/quick/`
  without modifying canonical M52 evidence files.
- The active figure scripts accept explicit output paths.
- `manuscript/replication/README.md` documents full and quick commands.
- `manuscript/replication/requirements.txt` names the current wrapper
  dependencies and keeps the future `svar-python` pin visible.
- `outcome.md` summarizes what changed, checks, remaining follow-up, and the
  question-index decision.
- `python scripts/check_manuscript.py` passes after edits.

## Expected Outputs

- `manuscript/replication/run_all.py`
- Updated active simulation-script CLIs for output routing.
- Updated `manuscript/replication/README.md`
- Updated `manuscript/replication/requirements.txt`
- Updated M33 row in `manuscript/task-board.md`
- `manuscript/tasks/M33-replication-wrapper/outcome.md`
