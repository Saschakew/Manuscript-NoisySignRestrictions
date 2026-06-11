# M60 Legacy Status Labels Outcome

Status: complete.

Completed: 2026-06-11.

## Short Answer

Legacy task packets are now labeled in place. M60 adds
`manuscript/tasks/LEGACY-STATUS.md`, which identifies the old flat template as
historical, M47 and M49-M56 flat packets as current references, and the related
M48 derivation as superseded by M49. Nothing was moved, archived, renamed, or
deleted.

## What Changed

- Added `manuscript/tasks/LEGACY-STATUS.md`.
- Added this M60 task folder with `task.md` and `outcome.md`.
- Linked the legacy status map from `manuscript/START-HERE.md`,
  `manuscript/QUESTION-INDEX.md`, `manuscript/tasks/README.md`, and the
  dashboard orientation map.
- Added M60 to `manuscript/task-board.md` without changing M33 as the next
  manuscript task.
- Updated M59's outcome note to mark the historical-status follow-up as
  addressed.
- Recorded the workflow decision and work block in the human-readable logs.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| What are the old flat task packets now? | They are labeled in place: most are current references, `_template.md` is historical, and the related M48 derivation is superseded by M49. | `manuscript/tasks/LEGACY-STATUS.md` |
| Did this migrate or archive old task files? | No. M60 only adds labels and links; the old files stay where they are. | This note |
| What remains after this cleanup slice? | Archive guidance could still be added later if old material remains noisy, but the main navigation, question index, and legacy status map now exist. | This note |

## Files To Read

| Path | Why |
|---|---|
| `manuscript/tasks/LEGACY-STATUS.md` | Status labels for old flat task packets |
| `manuscript/tasks/M60-legacy-status-labels/task.md` | Task contract |
| `manuscript/tasks/README.md` | Task-folder rules and legacy packet pointer |
| `manuscript/START-HERE.md` | Front door now linked to the status map |

## Checks

- Verified that every path named in `manuscript/tasks/LEGACY-STATUS.md`
  exists.
- `python scripts/check_manuscript.py` passed.
- `git diff --check` passed with only the repository's usual CRLF
  normalization warnings.

## Open Questions Or Follow-Up

- Add archive guidance later only if the status labels are not enough in
  practice.
- If a legacy task is reopened, create a new task folder and link the old flat
  packet from the new `task.md` or `outcome.md`.
- M33 remains the next manuscript task.
