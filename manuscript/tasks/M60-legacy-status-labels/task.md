# M60 Legacy Status Labels

## Status And Routing

Status: `done`

Priority: 2

Task-board row: `M60`

Transparency milestone: not required; this is a planning-only navigation edit.

Outcome note: `outcome.md`

## Original User Prompt

Continuation of U0060: "implement it slowy and step by step."

Context: M57 added task folders, M58 added `START-HERE.md`, and M59 added
`QUESTION-INDEX.md`. The next low-overhead cleanup is to label legacy flat
task packets by current status without moving them.

## Why This Task Exists

The task directory now contains both new task folders and old flat task
packets. That is fine historically, but it is hard to scan. A small status
index can tell a future reader which legacy packets are current references,
which are superseded, and which templates are historical.

## Do Not Trust Without Rechecking

- Do not move or rename legacy files.
- Do not change manuscript claims, equations, simulations, figures, or formal
  objects.
- Do not reclassify scientific results by memory; use the current task board,
  question index, dashboard, and referenced notes.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/tasks/README.md` | Confirm legacy packet rule. | status index |
| `manuscript/task-board.md` | Confirm task statuses. | status labels |
| `manuscript/QUESTION-INDEX.md` | Confirm superseded M48 and current answers. | status labels |
| `manuscript/project-dashboard.md` | Confirm current manuscript state. | dashboard edits |

## Traceability Ledger

| Item | Required status | Evidence required | Result |
|---|---|---|---|
| Legacy flat packets should stay in place. | workflow decision | M57/M58/M59 outcomes and tasks README | complete |
| `_template.md` is no longer the preferred template. | workflow classification | `_folder-template/` exists and tasks README describes it | complete |
| M47 and M49-M56 flat packets are completed current references unless a later note supersedes them. | task status | task board and question index | complete |
| M48 is superseded by M49. | task status | question index and derivation notes | complete |

## Required Work

1. Add `manuscript/tasks/LEGACY-STATUS.md`.
2. Create this M60 task folder with a compact outcome note.
3. Link the legacy status index from `START-HERE.md`, `tasks/README.md`, and
   the dashboard orientation map.
4. Add M60 to the task board and update the relevant human-readable logs.
5. Run checks and record the results in `outcome.md`.

## Stop Conditions

- Stop if status labels require a scientific re-audit.
- Stop if the task starts turning into a migration or archival pass.
- Stop if a linked file does not exist and the intended status cannot be
  verified locally.

## Acceptance Criteria

- `manuscript/tasks/LEGACY-STATUS.md` labels existing legacy flat packets.
- New navigation surfaces point to the status index.
- M60 is recorded without changing M33 as the next manuscript task.
- `outcome.md` answers what was labeled and what remains open.
- `python scripts/check_manuscript.py` passes.

## Expected Outputs

- `manuscript/tasks/LEGACY-STATUS.md`
- `manuscript/tasks/M60-legacy-status-labels/task.md`
- `manuscript/tasks/M60-legacy-status-labels/outcome.md`
- Updates to navigation, task, and log surfaces.
