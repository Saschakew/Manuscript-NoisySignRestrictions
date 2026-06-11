# M57 Task Folder Workflow

## Status And Routing

Status: `done`

Priority: 2

Task-board row: `M57`

Transparency milestone: `M0059-m57-task-folder-workflow`

GitHub milestone: `54` (`https://github.com/Saschakew/Manuscript-NoisySignRestrictions/milestone/54`)

Outcome note: `outcome.md`

## Original User Prompt

"lets improve the skill we use to work on tasks. we already improved the tasks
with the explicit task files. but i think we should have a folder for each
task. the folder should contain the task, but also when you are done working
on the task a small note on what was done and questions asked in the task. i
think the last tasks involved some quesions of mine and it is difficult for me
to find the answer. maybe you already write down somewhere what you did and
somewhere answered my quesion.the goal is not to add overhead to our process.
i just ask if we can streamline it and better document what was done during a
task. related to this, i have the impression that our whole project became
somehat messy with many files and i feel like it is difficult to have a good
overview. what is your impression"

## Why This Task Exists

The manuscript process is traceable, but task-level answers are spread across
flat packets, derivation notes, session logs, Codex logs, transparency
manifests, and draft source trails. The user wants a low-overhead task home
that makes "what happened?" and "what questions were answered?" easy to find.

## Do Not Trust Without Rechecking

- Do not add a large migration task unless needed; historical flat packets are
  valid and should not be churned.
- Do not make outcome notes another long log stream.
- Do not replace `task-board.md`; it should remain the compact index.
- Do not hide scientific evidence in outcome notes; they should point to the
  detailed derivation, source, code, or simulation artifact.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `.codex/skills/write-standalone-manuscript/SKILL.md` | Update the active task workflow. | skill edits |
| `.codex/skills/write-standalone-manuscript/references/task-packet-workflow.md` | Update detailed task-folder workflow. | skill edits |
| `manuscript/manuscript-rules.md` | Update repository-local task rules. | rule edits |
| `manuscript/task-board.md` | Add M57 and keep the board compact. | board edits |
| `manuscript/project-dashboard.md` | Keep overview/current milestone accurate. | dashboard edits |
| `manuscript/tasks/` | Inspect existing flat task packets and add folder template. | template edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The task process is traceable but hard to navigate because task answers are split across multiple files. | `derived` | Repository inspection of task-board, flat task packets, logs, and overview files. | passed |
| A folder with `task.md` plus compact `outcome.md` can improve answer retrieval without large overhead. | `user-decision` plus workflow design | User request and implemented rule/template changes. | implemented |

## Required Work

1. Skill work: update the manuscript skill and task workflow reference.
2. Rule work: update manuscript rules to prefer task folders and outcome notes.
3. Template work: add folder templates under `manuscript/tasks/`.
4. Overview work: add `manuscript/tasks/README.md` and fix stale overview
   lines found while inspecting task navigation.
5. Task work: dogfood the folder structure for M57.
6. Outcome note work: answer the user's process and overview questions in
   `outcome.md`.

## Stop Conditions

- Stop if the proposed workflow requires migrating all historical tasks.
- Stop if the added note duplicates logs rather than summarizing them.
- Stop if the task-board row becomes a long hand-off instead of an index.

## Acceptance Criteria

- Future-task workflow names `task.md` and `outcome.md`.
- Legacy flat packets remain valid; no mass migration is required.
- `outcome.md` has a clear `Questions Answered` section.
- The current M57 task demonstrates the new folder structure.
- `python scripts/check_manuscript.py` passes.

## Expected Outputs

- Updated skill and task workflow reference.
- Updated manuscript rules.
- `manuscript/tasks/README.md`.
- `manuscript/tasks/_folder-template/task.md`.
- `manuscript/tasks/_folder-template/outcome.md`.
- `manuscript/tasks/M57-task-folder-workflow/task.md`.
- `manuscript/tasks/M57-task-folder-workflow/outcome.md`.
