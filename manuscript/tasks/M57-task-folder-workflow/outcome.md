# M57 Task Folder Workflow Outcome

Status: complete.

Completed: 2026-06-11.

## Short Answer

Yes. The project is traceable, but it has become harder to navigate because
task answers are spread across the task board, flat task packets, derivation
notes, session logs, Codex logs, and transparency files. The new rule keeps the
existing traceability but gives each future substantial task one home:
`task.md` for the contract and `outcome.md` for the short answer trail.

## What Changed

- Updated the manuscript skill and task workflow reference to prefer task
  folders for new fragile, source-sensitive, mathematical, code-sensitive, or
  priority-1 tasks.
- Updated `manuscript/manuscript-rules.md` with the same rule.
- Added `manuscript/tasks/README.md` as the task-folder overview.
- Added `manuscript/tasks/_folder-template/task.md` and
  `manuscript/tasks/_folder-template/outcome.md`.
- Dogfooded the new layout with `manuscript/tasks/M57-task-folder-workflow/`.
- Fixed stale overview lines that still described the M25/M47 proof audit as
  pending.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Can we streamline task documentation without adding much overhead? | Yes. Future substantial tasks should use a folder with `task.md` and a compact `outcome.md`. The outcome note should be short and should point to detailed evidence instead of duplicating it. | `manuscript/tasks/README.md`; `.codex/skills/write-standalone-manuscript/SKILL.md` |
| Where were answers to recent task questions written before this change? | Mostly in the flat task packet outcome logs, derivation notes, `session-log.md`, `codex-log.md`, and source trails. The answers existed, but there was no single per-task answer page. | Legacy flat packets in `manuscript/tasks/`; `manuscript/derivations/`; `manuscript/session-log.md`; `manuscript/codex-log.md` |
| Is the project getting messy and hard to overview? | My impression: yes, mildly. It is not untracked chaos; it is over-documented across too many surfaces. The main fix is not deleting logs, but adding clearer entry points and per-task outcome notes. | `manuscript/tasks/README.md`; `manuscript/project-dashboard.md`; `manuscript/paper-map.md` |

## Files To Read

| Path | Why |
|---|---|
| `manuscript/tasks/M57-task-folder-workflow/task.md` | Task contract |
| `manuscript/tasks/README.md` | New task-folder overview |
| `manuscript/tasks/_folder-template/task.md` | Future task contract template |
| `manuscript/tasks/_folder-template/outcome.md` | Future outcome note template |
| `.codex/skills/write-standalone-manuscript/SKILL.md` | Active skill behavior |

## Checks

- `python scripts/check_manuscript.py` passed before close with only the
  expected open M0059 warning.
- `git diff --check` reported only line-ending normalization warnings.
- After closing M0059, `python scripts/check_manuscript.py` passed cleanly.

## Open Questions Or Follow-Up

- Do not migrate old flat task packets unless a legacy task is reopened or the
  user explicitly asks for cleanup.
- M33 remains the next manuscript task after this workflow maintenance block.
