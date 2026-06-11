# M59 Question Index Outcome

Status: complete.

Completed: 2026-06-11.

## Short Answer

Recent answers are now findable by question rather than only by task ID. M59
adds `manuscript/QUESTION-INDEX.md`, a selective map from user questions to the
task outcomes, derivation notes, draft passages, or logs where those questions
were answered. It does not migrate legacy packets or duplicate long arguments.

## What Changed

- Added `manuscript/QUESTION-INDEX.md`.
- Added this M59 task folder with `task.md` and `outcome.md`.
- Linked the question index from `manuscript/START-HERE.md` and the dashboard
  orientation map.
- Added M59 to `manuscript/task-board.md` without changing M33 as the next
  manuscript task.
- Updated M58's outcome note to mark the question-index follow-up as addressed.
- Recorded the workflow decision and work block in the human-readable logs.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| How do we make recent answers findable without adding much overhead? | Use a selective index that points to the first answer location, rather than copying task outcomes or derivations into another long document. | `manuscript/QUESTION-INDEX.md` |
| Does this migrate old task packets? | No. Legacy flat packets and derivation notes stay where they are; the index points to them. | `manuscript/QUESTION-INDEX.md`; this note |
| What remains after this cleanup slice? | Historical status labels or archive guidance could still be useful later, but only as a separate cleanup task. | This note |

## Files To Read

| Path | Why |
|---|---|
| `manuscript/QUESTION-INDEX.md` | Compact map from recent questions to answer locations |
| `manuscript/tasks/M59-question-index/task.md` | Task contract |
| `manuscript/START-HERE.md` | Front door now linked to the question index |
| `manuscript/project-dashboard.md` | Orientation map now linked to the question index |

## Checks

- Verified that every path named in `manuscript/QUESTION-INDEX.md` exists.
- `python scripts/check_manuscript.py` passed.
- `git diff --check` passed with only the repository's usual CRLF
  normalization warnings.

## Open Questions Or Follow-Up

- Add future rows only when a question is likely to be searched for later.
- M60 now labels legacy flat packets as current references, superseded
  references, or historical templates without moving them.
- M33 remains the next manuscript task.
