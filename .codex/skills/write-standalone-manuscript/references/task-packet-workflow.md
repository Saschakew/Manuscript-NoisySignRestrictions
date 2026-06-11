# Task Packet Workflow

Use this reference when creating, updating, selecting, or executing manuscript
tasks that are fragile, source-sensitive, mathematical, code-sensitive, or
priority 1.

## Rule

`manuscript/task-board.md` is an index, not the full hand-off. For fragile
scientific work, create a task packet under `manuscript/tasks/` and link it
from the board.

Use a packet when a task involves:

- a long or nuanced user prompt;
- prior failed or contaminated work;
- claims about what a paper or source does;
- mathematical derivations or proof gates;
- code-to-theory comparisons;
- figure, simulation, or Monte Carlo rebuild decisions;
- normalization or identification choices;
- any task where a future agent could plausibly over-compress the request.

## Packet Path

Use:

```text
manuscript/tasks/Mxx-short-slug.md
```

Keep the packet title and task-board title aligned. The board row should point
to the packet path in the next-action field.

## Required Packet Sections

Every packet for scientific work should include:

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

## Scientific Claim Ledger

Use the claim statuses from `scientific-claim-audit.md`:

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| Exact claim text | `raw-source`, `vault-source`, `derived`, `code-implemented`, `conjectural`, or `user-decision` | Source path, equation, code path, or derivation | pending |

Code behavior can only establish `code-implemented`. It cannot establish a
paper's theoretical object unless the source-to-code mapping is separately
verified.

## Task Board Contract

When a packet exists, the task-board row should be short:

- task title;
- status;
- priority;
- packet path;
- one-sentence next action.

Do not squeeze the full user prompt or derivation checklist into the board row.
The packet is the contract.

## Selecting The Next Task

For prompts such as `work on next task`, `pick next task`, or `continue`:

1. Read the project dashboard and task board.
2. Prefer the dashboard's `Next recommended action` unless the user named a
   task.
3. Skip `done`, `deferred`, and superseded tasks.
4. If the selected task row links a packet, read the packet before opening
   sources, writing derivations, editing prose, or running simulations.
5. If the selected task is fragile or priority 1 and has no packet, create one
   first and link it from the board.
6. Execute the packet's required reads, required work, stop conditions, and
   acceptance criteria.

Do not infer a fragile task's full meaning from the task-board row alone.

## Planning Tasks

For prompts such as `plan next tasks`, `insert a task`, or `update tasks`:

1. Preserve the original user prompt in the user-input log.
2. Identify dependencies and blocked-before relationships.
3. Classify each task as routine or fragile.
4. Create packets immediately for fragile or priority-1 scientific tasks.
5. Link each packet from the task-board row.
6. Make the packet before marking the planning task complete.

Routine tasks can remain board-only when they are narrow, low-risk, and do not
depend on source interpretation or derivations.

## Working From A Packet

When executing a packet:

1. Read the packet before trusting the task-board summary.
2. Read all `Required Reads` before drafting source-sensitive claims.
3. Fill or update the claim ledger while working.
4. Do source and derivation work before editing `draft.md`.
5. If a stop condition is triggered, mark the task blocked or create a new
   follow-up rather than smoothing uncertainty into prose.
6. Update the packet with the outcome, evidence paths, checks, and open
   issues before marking the task done.

## Completion Rule

A fragile scientific task is not done merely because prose changed. It is done
only when the packet's acceptance criteria are satisfied, checks pass, and any
remaining uncertainty is visible in the task board, packet, registry, or draft
TODO notes.
