# M61 Question Index Maintenance Rule

## Status And Routing

Status: `done`

Priority: 2

Task-board row: `M61`

Transparency milestone: not required; this is a planning-only workflow edit.

Outcome note: `outcome.md`

## Original User Prompt

Continuation of U0060: "implement it slowy and step by step."

Context: M57 added task folders, M58 added `START-HERE.md`, M59 added
`QUESTION-INDEX.md`, and M60 labeled legacy flat task packets. The next
low-overhead step is to make sure the question index stays current during
future task closeout.

## Why This Task Exists

The question index solves a search problem only if future tasks maintain it
when they answer questions that a reader is likely to look for later. The
workflow should require a small decision at closeout: update the index, or say
that no index update is needed.

## Do Not Trust Without Rechecking

- Do not turn the question index into a full task log.
- Do not require every task to add a question-index row.
- Do not change manuscript claims, equations, figures, simulations, or the
  formal object registry.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `.codex/skills/write-standalone-manuscript/SKILL.md` | Active agent workflow. | skill edit |
| `.codex/skills/write-standalone-manuscript/references/task-packet-workflow.md` | Detailed task-folder workflow. | workflow-reference edit |
| `manuscript/tasks/_folder-template/task.md` | Future task contract template. | template edit |
| `manuscript/tasks/_folder-template/outcome.md` | Future outcome note template. | template edit |
| `manuscript/tasks/README.md` | User-facing task-folder overview. | task README edit |
| `manuscript/manuscript-rules.md` | Repository-level workflow rule. | rules edit |

## Traceability Ledger

| Item | Required status | Evidence required | Result |
|---|---|---|---|
| Future tasks should decide whether to update `QUESTION-INDEX.md`. | workflow rule | Skill, rules, workflow reference, and templates | complete |
| The decision should be low overhead. | workflow rule | Outcome template asks for update or "not needed" | complete |
| Legacy status map should update only when legacy status changes. | workflow rule | Outcome template and task README | complete |

## Required Work

1. Update the manuscript skill and task-folder workflow reference.
2. Update the folder templates so future tasks record index-maintenance
   decisions.
3. Update `manuscript/tasks/README.md` and `manuscript/manuscript-rules.md`.
4. Add M61 to the task board and logs.
5. Run checks and record the results in `outcome.md`.

## Stop Conditions

- Stop if the proposed rule requires duplicating task outcomes in
  `QUESTION-INDEX.md`.
- Stop if the workflow starts requiring question-index rows for routine tasks.
- Stop if the edit touches scientific manuscript content.

## Acceptance Criteria

- Future task closeout asks whether `QUESTION-INDEX.md` needs an update.
- Future task closeout asks whether `LEGACY-STATUS.md` changed only when
  relevant.
- M61 is recorded without changing M33 as the next manuscript task.
- `outcome.md` summarizes the maintenance rule and checks.
- `python scripts/check_manuscript.py` passes.

## Expected Outputs

- `manuscript/tasks/M61-question-index-maintenance/task.md`
- `manuscript/tasks/M61-question-index-maintenance/outcome.md`
- Updates to the skill, task workflow reference, templates, rules, task README,
  task board, and logs.
