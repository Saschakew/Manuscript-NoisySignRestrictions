# M61 Question Index Maintenance Rule Outcome

Status: complete.

Completed: 2026-06-11.

## Short Answer

The question index now has a maintenance rule. Future task outcomes must say
whether `manuscript/QUESTION-INDEX.md` was updated or not needed. The index is
updated only when a task answers a question someone is likely to search for
later, so routine tasks do not create extra index rows.

## What Changed

- Updated the manuscript skill with the question-index closeout rule.
- Updated the task workflow reference with an `Index Updates` outcome section.
- Updated the folder templates so future task outcomes record whether
  `QUESTION-INDEX.md` and `LEGACY-STATUS.md` were updated or not needed.
- Updated `manuscript/tasks/README.md` and `manuscript/manuscript-rules.md`
  with the same lightweight rule.
- Linked the rule from `manuscript/START-HERE.md` and added the M61 answer to
  `manuscript/QUESTION-INDEX.md`.
- Added M61 to `manuscript/task-board.md` without changing M33 as the next
  manuscript task.
- Recorded the workflow decision and work block in the human-readable logs.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| How will the question index stay current? | Each future task outcome records whether `QUESTION-INDEX.md` was updated or not needed. | This note; `manuscript/tasks/_folder-template/outcome.md` |
| Does every task need a question-index row? | No. Add a row only when the task answers a question someone is likely to search for later. | `manuscript/QUESTION-INDEX.md`; this note |
| Does this add heavy closeout overhead? | No. The template adds a small `Index Updates` section, usually one "not needed" line for routine tasks. | `manuscript/tasks/_folder-template/outcome.md` |

## Files To Read

| Path | Why |
|---|---|
| `manuscript/tasks/M61-question-index-maintenance/task.md` | Task contract |
| `manuscript/tasks/_folder-template/outcome.md` | Future closeout template |
| `manuscript/QUESTION-INDEX.md` | Cross-task answer map |
| `.codex/skills/write-standalone-manuscript/SKILL.md` | Active skill rule |
| `.codex/skills/write-standalone-manuscript/references/task-packet-workflow.md` | Detailed task-folder workflow |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the M61 maintenance-rule row.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- Verified that the M61-maintained paths exist.
- `python C:\Users\smsakewe\.codex\skills\.system\skill-creator\scripts\quick_validate.py .codex\skills\write-standalone-manuscript`
  passed.
- `python scripts/check_manuscript.py` passed.
- `git diff --check` passed with only the repository's usual CRLF
  normalization warnings.

## Open Questions Or Follow-Up

- Apply the updated outcome template when creating the next task folder.
- M33 remains the next manuscript task.
