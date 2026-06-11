# Task Folder Index

Purpose: keep task work findable without turning `task-board.md` into a long
memory dump.

## Current Rule

For new fragile, source-sensitive, mathematical, code-sensitive, or priority-1
tasks, create a folder:

```text
manuscript/tasks/Mxx-short-slug/
  task.md
  outcome.md
```

- `task.md` is the contract: prompt, scope, required reads, claim ledger, stop
  conditions, and acceptance criteria.
- `outcome.md` is the short answer trail: what changed, questions answered,
  files to read, checks, and follow-up.
- `task-board.md` stays a compact index and should link to `task.md`.

Routine low-risk tasks can remain board-only. Use a folder anyway when the
task answers a user question that will be difficult to find later.

## Where To Look

| Need | Open |
|---|---|
| What is the next task? | `manuscript/project-dashboard.md`, then `manuscript/task-board.md` |
| What exactly was this task supposed to do? | `manuscript/tasks/Mxx-short-slug/task.md` |
| What was actually done and what questions were answered? | `manuscript/tasks/Mxx-short-slug/outcome.md` |
| What changed in the manuscript argument? | `manuscript/paper-map.md` and `manuscript/formal-object-registry.json` |
| Where is the full proof, audit, or simulation note? | The paths listed in `outcome.md` |
| What was committed and tagged? | `manuscript/transparency/milestones/` and Git tags |

## Legacy Packets

Older task packets are flat files such as
`manuscript/tasks/M47-standard-dw-proof-gate-audit.md`. They remain valid
historical artifacts and do not need migration. If a legacy task is reopened,
create a folder and link the legacy file from the new `task.md` or
`outcome.md`.
