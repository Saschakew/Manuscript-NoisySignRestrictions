# M58 Start-Here Navigation Outcome

Status: complete.

Completed: 2026-06-11.

## Short Answer

The cleanup is now deliberately incremental. M58 adds
`manuscript/START-HERE.md` as the repository front door and records the work in
its own task folder, but it does not migrate, archive, rename, or delete
historical material. M33 remains the next manuscript task.

## What Changed

- Added `manuscript/START-HERE.md` as the stable navigation entry point.
- Added this M58 task folder with `task.md` and `outcome.md`.
- Updated `manuscript/project-dashboard.md` so the orientation map points to
  `START-HERE.md`.
- Added M58 to `manuscript/task-board.md` without changing M33 as the next
  manuscript task.
- Recorded the user request and workflow decision in the human-readable logs.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| How should cleanup proceed slowly? | Start with navigation and traceability layers before touching old files. M58 only adds a front door and task outcome trail. | `manuscript/START-HERE.md`; this task's `task.md` |
| Where should someone start when the repository feels messy? | Open `manuscript/START-HERE.md` first, then follow its table to the dashboard, paper map, task board, or task outcome notes. | `manuscript/START-HERE.md` |
| What should wait for later cleanup? | Migration of legacy flat packets, archival of old files, and a cross-task question index should wait for separate explicit cleanup tasks. | This note |

## Files To Read

| Path | Why |
|---|---|
| `manuscript/START-HERE.md` | New front door for repository navigation |
| `manuscript/tasks/M58-start-here-navigation/task.md` | Task contract |
| `manuscript/project-dashboard.md` | Current state and orientation map |
| `manuscript/task-board.md` | Compact task index with M58 recorded |

## Checks

- `python scripts/check_manuscript.py` passed.
- `git diff --check` passed with only the repository's usual CRLF
  normalization warnings.

## Open Questions Or Follow-Up

- M59 now adds a compact question index for answers across recent tasks; extend
  it only when a question is likely to be searched for later.
- Consider a later historical-status cleanup that marks legacy flat packets as
  active, superseded, or historical without moving them.
- M33 remains the next manuscript task.
