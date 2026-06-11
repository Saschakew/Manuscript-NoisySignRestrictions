# M59 Question Index

## Status And Routing

Status: `done`

Priority: 2

Task-board row: `M59`

Transparency milestone: not required; this is a planning-only navigation edit.

Outcome note: `outcome.md`

## Original User Prompt

Continuation of U0060: "implement it slowy and step by step."

Context: M57 added task folders and M58 added `START-HERE.md`. The remaining
pain point is that answers to recent user questions are still distributed
across flat task packets, derivation notes, logs, and new outcome notes.

## Why This Task Exists

Task folders improve future traceability, but they do not fully solve the
historical search problem. Several recent questions were answered before the
folder convention existed, especially questions about generated GMM moments,
normalization, source-correct DW moments, and whether M48 could be trusted.

This task adds a compact question index that points to the first place to read
for those answers. It should remain selective, not become a second task board.

## Do Not Trust Without Rechecking

- Do not invent new scientific answers; only index answers already recorded in
  task packets, derivation notes, the draft, or logs.
- Do not migrate legacy flat packets into folders.
- Do not change manuscript claims, equations, figures, simulations, or the
  formal object registry.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/START-HERE.md` | Confirm the new front-door role. | index placement |
| `manuscript/tasks/M58-start-here-navigation/outcome.md` | Confirm the open question-index follow-up. | task scope |
| `manuscript/tasks/M57-task-folder-workflow/outcome.md` | Confirm the task-folder decision. | task scope |
| `manuscript/project-dashboard.md` | Confirm current state and next manuscript task. | dashboard edits |
| `manuscript/task-board.md` | Confirm M33 remains next and M59 row placement. | task-board edits |

## Traceability Ledger

| Indexed answer | Required status | Evidence required | Result |
|---|---|---|---|
| Cleanup should proceed through small navigation layers before migration. | recorded workflow decision | M58 outcome and dashboard | complete |
| Future substantial tasks should use `task.md` plus `outcome.md`. | recorded workflow decision | M57 outcome and tasks README | complete |
| Robust fourth-cumulant sample entries are generated smooth moments. | existing method answer | M56 derivation and M52 evidence note | complete |
| The manuscript keeps the `diag(B)=1` chart for the first paper. | existing normalization answer | M54 derivation and decision log | complete |
| M49 supersedes M48 for source-correct DW moment claims. | existing source-audit answer | M49 derivation and M48 warning | complete |

## Required Work

1. Add `manuscript/QUESTION-INDEX.md`.
2. Link it from `manuscript/START-HERE.md` and the dashboard orientation map.
3. Add M59 to the task board.
4. Record the workflow decision and work block in human-readable logs.
5. Update `outcome.md` after checks pass.

## Stop Conditions

- Stop if a row requires a new scientific judgment rather than indexing an
  existing answer.
- Stop if maintaining the question index would require duplicating long
  derivations or logs.
- Stop if the cleanup starts changing manuscript prose, formal objects,
  simulations, or evidence outputs.

## Acceptance Criteria

- `manuscript/QUESTION-INDEX.md` exists and points to real files.
- `START-HERE.md` and the dashboard point to the question index.
- M59 is recorded in the task board without changing M33 as the next
  manuscript task.
- The M59 outcome explains what was indexed and what remains open.
- `python scripts/check_manuscript.py` passes.

## Expected Outputs

- `manuscript/QUESTION-INDEX.md`
- `manuscript/tasks/M59-question-index/task.md`
- `manuscript/tasks/M59-question-index/outcome.md`
- Updates to navigation, task, and log surfaces.
