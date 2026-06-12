# Start Here

Purpose: one front door for the manuscript repository. Use this file when the
project feels spread across too many logs, packets, notes, and outputs.

## Current State In One Minute

- Paper: a short theory-and-simulation note on noisy sign-restricted SVARs,
  standard Drautzburg-Wright refinement under residual noise, and a robust
  higher-moment comparison set.
- Current manuscript state: the M52 evidence rebuild, M55 main-text robust
  moment explanation, M56 generated-moment audit, and M47 standard-DW proof
  gate audit are complete.
- Next manuscript task: M63, citation/source-trail and export cleanup, now
  that M33 added the manuscript-local replication wrapper.
- Current workflow state: new substantial tasks should use a task folder with
  `task.md` for the contract and `outcome.md` for the short answer trail; use
  `QUESTION-INDEX.md` when you remember the question but not the task ID.
- Current cleanup rule: improve navigation and traceability first. Do not
  migrate, archive, rename, or delete older material until a separate cleanup
  task says to do that.

## Where To Look

| Need | Open |
|---|---|
| Current state and next action | `manuscript/project-dashboard.md` |
| Argument map and reader path | `manuscript/paper-map.md` |
| Compact task index | `manuscript/task-board.md` |
| Recent user questions and where they were answered | `manuscript/QUESTION-INDEX.md` |
| Task contracts and answer trails | `manuscript/tasks/README.md`, then the relevant task folder |
| Status of old flat task packets | `manuscript/tasks/LEGACY-STATUS.md` |
| Source and evidence context | `manuscript/source-packet.md` |
| Assumptions, propositions, equations, figures, tables, and dependencies | `manuscript/formal-object-registry.json` |
| Manuscript prose | `manuscript/draft.md` |
| Manuscript rules and workflow conventions | `manuscript/manuscript-rules.md` |
| Citation and source provenance | `manuscript/citation-provenance.md` |
| Derivations and proof trails | `manuscript/derivations/README.md` and `manuscript/derivations/` |
| Exploratory and evidence simulations | `manuscript/simulations/README.md` and `manuscript/simulations/` |
| Figures and figure notes | `manuscript/figures/README.md` and `manuscript/figures/` |
| Shareable replication package plan | `manuscript/replication/README.md` |
| Durable user inputs | `manuscript/user-input-log.md` |
| Durable decisions | `manuscript/decision-log.md` |
| Chronological work history | `manuscript/session-log.md` |
| Milestone-level Codex transparency | `manuscript/codex-log.md` |
| Machine-readable transparency stream | `manuscript/transparency/README.md` and `manuscript/transparency/` |

## How To Use A Task Folder

1. Start from `manuscript/task-board.md` or the dashboard's next action.
2. If the task has a folder, read `task.md` before doing work.
3. After the task is done, read `outcome.md` first for what changed and which
   questions were answered.
4. If you remember the question but not the task ID, use
   `manuscript/QUESTION-INDEX.md`.
5. When closing a task, update `manuscript/QUESTION-INDEX.md` only if the task
   answered a question someone is likely to search for later; otherwise say
   "not needed" in `outcome.md`.
6. Follow the paths in `outcome.md` only when you need the detailed proof,
   simulation output, draft change, or provenance trail.

## Cleanup Rule

Keep this file as the stable entry point. Keep `project-dashboard.md` as the
state-and-next-action page, `paper-map.md` as the argument page,
`task-board.md` as the compact task index, `QUESTION-INDEX.md` as the compact
cross-task answer map, `tasks/LEGACY-STATUS.md` as the status map for old flat
packets, and `tasks/*/outcome.md` as the place to recover task-specific
answers.
