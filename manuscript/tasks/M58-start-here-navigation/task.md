# M58 Start-Here Navigation

## Status And Routing

Status: `done`

Priority: 2

Task-board row: `M58`

Transparency milestone: not required; this is a planning-only navigation edit.

Outcome note: `outcome.md`

## Original User Prompt

"implement it slowy and step by step."

Context: the user had just asked how to further clean up and improve the
project structure so it remains traceable in a large manuscript project.

## Why This Task Exists

M57 created task folders and compact outcome notes. The remaining problem is
that the whole repository still lacks one obvious front door. A user or future
agent can still start from the dashboard, task board, paper map, logs, or
transparency files and be unsure which surface answers which question.

This task implements the smallest cleanup step: add a single navigation entry
point and register the work as its own task folder. It deliberately avoids
moving, archiving, renaming, or deleting older material.

## Do Not Trust Without Rechecking

- Do not assume older task packets have been migrated into folders.
- Do not treat historical logs as disorganized enough to delete or archive.
- Do not change the next scientific manuscript task unless the navigation
  update uncovers a true planning inconsistency.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/project-dashboard.md` | Confirm current stage, next action, and orientation map. | navigation edits |
| `manuscript/task-board.md` | Confirm M57 status and next open task. | task-board edits |
| `manuscript/tasks/README.md` | Reuse the task-folder convention. | task-folder edits |
| `manuscript/tasks/M57-task-folder-workflow/outcome.md` | Preserve the previous cleanup decision and open follow-up. | outcome wording |

## Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The project needs a clearer front door, not a bulk migration, as the next cleanup step. | workflow decision | M57 outcome plus current dashboard/task-board inspection | complete |
| M33 remains the next manuscript task after the navigation cleanup. | planning state | Dashboard and task board | complete |
| The new entry point should preserve existing specialized files rather than merging logs. | workflow decision | M57 decision and current file roles | complete |

## Required Work

1. Add `manuscript/START-HERE.md` as the repository front door.
2. Create this M58 task folder with a compact outcome note.
3. Update the task board and project dashboard to point to the new front door.
4. Record the user request and workflow decision in the human-readable logs.
5. Run the manuscript check and update `outcome.md`.

## Stop Conditions

- Stop if creating a front-door page requires moving or rewriting historical
  artifacts.
- Stop if the dashboard and task board disagree on the next open manuscript
  task in a way that cannot be resolved locally.
- Stop if the cleanup starts changing scientific claims, equations, figures,
  or formal objects.

## Acceptance Criteria

- `manuscript/START-HERE.md` tells a future reader where to begin.
- The dashboard orientation map includes `START-HERE.md`.
- `task-board.md` includes M58 without changing M33 as the next manuscript
  task.
- `outcome.md` answers what this cleanup step did and what should wait.
- `python scripts/check_manuscript.py` passes.

## Expected Outputs

- `manuscript/START-HERE.md`
- `manuscript/tasks/M58-start-here-navigation/task.md`
- `manuscript/tasks/M58-start-here-navigation/outcome.md`
- Updates to planning and log surfaces.
