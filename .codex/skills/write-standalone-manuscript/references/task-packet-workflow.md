# Task Folder Workflow

Use this reference when creating, updating, selecting, or executing manuscript
tasks that are fragile, source-sensitive, mathematical, code-sensitive, or
priority 1.

## Rule

`manuscript/task-board.md` is an index, not the full hand-off. For fragile
scientific work, create a task folder under `manuscript/tasks/` and link its
`task.md` from the board. Each completed task folder should also contain a
short `outcome.md`.

Use a task folder when a task involves:

- a long or nuanced user prompt;
- prior failed or contaminated work;
- claims about what a paper or source does;
- mathematical derivations or proof gates;
- code-to-theory comparisons;
- figure, simulation, or Monte Carlo rebuild decisions;
- normalization or identification choices;
- any task where a future agent could plausibly over-compress the request.

## Folder Path

For new tasks, use:

```text
manuscript/tasks/Mxx-short-slug/task.md
manuscript/tasks/Mxx-short-slug/outcome.md
```

Keep the task title and task-board title aligned. The board row should point
to `task.md` in the next-action field. Legacy flat packets such as
`manuscript/tasks/Mxx-short-slug.md` remain valid historical artifacts.

## Required `task.md` Sections

Every `task.md` for scientific work should include:

1. `Status And Routing`
2. `Original User Prompt`
3. `Why This Task Exists`
4. `Do Not Trust Without Rechecking`
5. `Required Reads`
6. `Scientific Claim Ledger`
7. `Required Work`
8. `Stop Conditions`
9. `Acceptance Criteria`
10. `Expected Outputs`

## Required `outcome.md` Sections

Keep this file compact. It is the place a reader should open first when they
want the answer without reconstructing the entire milestone.

1. `Status`
2. `Short Answer`
3. `What Changed`
4. `Questions Answered`
5. `Files To Read`
6. `Checks`
7. `Open Questions Or Follow-Up`

## Scientific Claim Ledger

Use the claim statuses from `scientific-claim-audit.md`:

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| Exact claim text | `raw-source`, `vault-source`, `derived`, `code-implemented`, `conjectural`, or `user-decision` | Source path, equation, code path, or derivation | pending |

Code behavior can only establish `code-implemented`. It cannot establish a
paper's theoretical object unless the source-to-code mapping is separately
verified.

## Task Board Contract

When a task folder exists, the task-board row should be short:

- task title;
- status;
- priority;
- path to `task.md`;
- one-sentence next action.

Do not squeeze the full user prompt or derivation checklist into the board row.
The task folder is the contract and answer trail.

## Selecting The Next Task

For prompts such as `work on next task`, `pick next task`, or `continue`:

1. Read the project dashboard and task board.
2. Prefer the dashboard's `Next recommended action` unless the user named a
   task.
3. Skip `done`, `deferred`, and superseded tasks.
4. If the selected task row links a task folder, read `task.md` before opening
   sources, writing derivations, editing prose, or running simulations. If the
   task is being resumed or audited, read `outcome.md` first when it exists.
5. If the selected task row links a legacy flat packet, read that packet.
6. If the selected task is fragile or priority 1 and has no folder or packet,
   create a folder first and link `task.md` from the board.
7. Execute the task contract's required reads, required work, stop conditions, and
   acceptance criteria.

Do not infer a fragile task's full meaning from the task-board row alone.

## Planning Tasks

For prompts such as `plan next tasks`, `insert a task`, or `update tasks`:

1. Preserve the original user prompt in the user-input log.
2. Identify dependencies and blocked-before relationships.
3. Classify each task as routine or fragile.
4. Create task folders immediately for fragile or priority-1 scientific tasks.
5. Link each folder's `task.md` from the task-board row.
6. Make the folder before marking the planning task complete.

Routine tasks can remain board-only when they are narrow, low-risk, and do not
depend on source interpretation or derivations. If a routine task answers a
user question that will be hard to find later, use a folder anyway.

## Working From A Task Folder

When executing a task folder:

1. Read `task.md` before trusting the task-board summary.
2. Read all `Required Reads` before drafting source-sensitive claims.
3. Fill or update the claim ledger while working.
4. Do source and derivation work before editing `draft.md`.
5. If a stop condition is triggered, mark the task blocked or create a new
   follow-up rather than smoothing uncertainty into prose.
6. Update `outcome.md` with the short answer, questions answered, evidence
   paths, checks, and open issues before marking the task done.

## Completion Rule

A fragile scientific task is not done merely because prose changed. It is done
only when the task's acceptance criteria are satisfied, checks pass, the
outcome note is written, and any remaining uncertainty is visible in the task
board, task folder, registry, or draft TODO notes.
