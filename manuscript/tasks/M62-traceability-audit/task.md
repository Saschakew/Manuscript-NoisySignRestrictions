# M62 Traceability Cleanup Audit

## Status And Routing

Status: `doing`

Priority: 2

Task-board row: `M62`

Transparency milestone: not required; this is a planning-only workflow audit.

Outcome note: `outcome.md`

## Original User Prompt

Continuation of U0060: "implement it slowy and step by step."

Context: M57-M61 added task folders, a repository front door, a question index,
legacy status labels, and a maintenance rule for future task closeout. This
task audits whether the cleanup now satisfies the original workflow request.

## Why This Task Exists

The cleanup should not keep adding files merely because it can. The right next
step is to check whether the current structure actually solves the original
problems: task answers should be easy to find, future tasks should document
what was done and what was asked, the repository should have a clear overview,
and the process should remain low overhead.

## Do Not Trust Without Rechecking

- Do not mark the cleanup complete just because several files were added.
- Do not redefine success around only the newest artifact.
- Do not change manuscript claims, equations, figures, simulations, or formal
  objects.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/START-HERE.md` | Verify the front-door overview. | audit |
| `manuscript/QUESTION-INDEX.md` | Verify cross-task answer retrieval. | audit |
| `manuscript/tasks/LEGACY-STATUS.md` | Verify legacy packet status labeling. | audit |
| `manuscript/tasks/README.md` | Verify task folder conventions. | audit |
| `manuscript/tasks/_folder-template/outcome.md` | Verify future closeout fields. | audit |
| `.codex/skills/write-standalone-manuscript/SKILL.md` | Verify active agent workflow. | audit |
| `manuscript/task-board.md` | Verify M33 remains the next manuscript task. | audit |
| `manuscript/project-dashboard.md` | Verify current-state routing. | audit |

## Requirement Ledger

| Requirement | Evidence required | Result |
|---|---|---|
| Future substantial tasks have task folders with outcome notes. | Skill, task README, folder templates, task board rows M57-M61 | pending |
| Task answers and user questions are findable. | `QUESTION-INDEX.md`, task outcomes, M61 maintenance rule | pending |
| The repository has a clear front door and orientation map. | `START-HERE.md`, dashboard orientation map | pending |
| Legacy task packets are understandable without migration. | `tasks/LEGACY-STATUS.md`, task README | pending |
| The process remains low overhead. | Question-index update only when needed; no migration/archive; planning-only path | pending |
| The cleanup did not displace the manuscript next task. | Dashboard and task board still show M33 next | pending |

## Required Work

1. Audit the cleanup against the requirement ledger.
2. Create a compact outcome note with pass/follow-up status.
3. Add M62 to task board, question index, dashboard, and logs.
4. Run checks.
5. If the audit passes, leave M33 as the next manuscript task and mark the
   thread goal complete.

## Stop Conditions

- Stop if a requirement is not met and implement the missing cleanup slice
  instead.
- Stop if the audit would require changing scientific manuscript content.

## Acceptance Criteria

- The outcome note records each requirement and its evidence.
- No additional cleanup layer is introduced unless a gap requires it.
- M33 remains the next manuscript task.
- Checks pass.

## Expected Outputs

- `manuscript/tasks/M62-traceability-audit/task.md`
- `manuscript/tasks/M62-traceability-audit/outcome.md`
- Updates to task board, dashboard, question index, and logs.

