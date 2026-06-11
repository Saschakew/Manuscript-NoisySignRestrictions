---
name: write-standalone-manuscript
description: Write and manage one standalone manuscript repository linked to KnowledgeVault source material. Use for manuscript planning, drafting, formal objects, simulations, citations, logs, transparency milestones, task creation and hand-off packets, and scientific-claim audits that require raw-source, vault-source, derivation, or code-provenance gates before prose changes.
---

# Write Standalone Manuscript

Use this skill for original manuscript work inside a repository created from
the KnowledgeVault manuscript template.

## Entry

1. Read `knowledge-vault-link.json`.
2. Read `manuscript/source-packet.md`.
3. Read `manuscript/project-dashboard.md`.
4. Read `manuscript/paper-map.md`.
5. Read `manuscript/task-board.md`.
6. Read `manuscript/draft.md` when drafting or revising prose.

Use KnowledgeVault only for source context, citation verification, and upstream
research memory. The manuscript itself lives in this repository.

If the vault link is still in template mode, the local path is blank, or the
required vault surfaces cannot be found, ask the user for the local
KnowledgeVault checkout path before substantive manuscript work. Validate the
path against `vault/papers/`, `vault/syntheses/`,
`vault/citations/references.bib`, and the registry files listed in
`knowledge-vault-link.json`.

Also validate KnowledgeVault's `svar-python` package using
`computational_package.path_candidates` in `knowledge-vault-link.json`. Treat
that package as the default implementation for SVAR estimation,
identification, inference, simulations, and replication code.

## discuss-with-me

When the user asks to `discuss-with-me`, treat the turn as a discussion-only
content conversation rather than manuscript work.

- Discuss ideas, structure, claims, tradeoffs, and possible arguments with the
  user.
- Do not edit files, open transparency milestones, update logs, create GitHub
  milestones, commit, tag, or push.
- Do not record the conversation as a durable user decision or work block.
- Read repository files only if needed for context.
- If the user asks to convert the discussion into edits, leave this workflow and
  resume the normal milestone, logging, editing, and checking discipline first.

## planning-only-edit

When the user asks for a narrow project-management or workflow edit, use this
lightweight path instead of the full manuscript milestone workflow. This applies
only when the edit does not change manuscript claims, prose, equations, proofs,
figures, tables, simulations, code, bibliography, or the formal object registry.
Examples include adding a task, changing a next action, recording a planning
note, updating workflow instructions, or correcting dashboard/task-board status.

- Do not open transparency milestones, create GitHub milestones, commit, tag,
  push, or start publication/progress milestones by default.
- Make the smallest durable edit that captures the planning decision.
- Update `manuscript/user-input-log.md` only when the decision should remain
  visible outside the chat.
- Run `python scripts/check_manuscript.py` after planning-file edits when
  practical, but do not treat that check as a publication snapshot.
- If the work expands into drafting, derivations, formal registry changes,
  simulation/code changes, figures, tables, bibliography changes, or
  evidence-bearing edits, leave this workflow and resume the normal substantive
  manuscript workflow before those edits.
- If the user explicitly asks to commit, tag, push, or open a milestone for a
  planning-only edit, do that requested action without inventing a milestone
  snapshot merely because files changed.

## Workflow

1. Confirm the central paper idea and source material.
2. Build or refresh `manuscript/source-packet.md` by searching the vault,
   identifying the 5-20 source notes most relevant to this manuscript, and
   recording citation, replication, and verification follow-up.
3. Keep `manuscript/paper-plan.md` current until scope and contribution are
   stable.
4. Maintain `manuscript/paper-map.md` as the compact argument map.
5. Maintain `manuscript/formal-object-registry.json` for assumptions,
   definitions, propositions, proofs, equations, figures, tables, and
   dependencies.
6. Keep `manuscript/draft.md` as the prose source of truth.
7. Copy verified BibTeX into `bibliography/references.bib` before shareable
   prose depends on it.
8. Build computational work on the existing `svar-python` package instead of
   reimplementing package-covered SVAR routines.
9. Keep final reproducibility code under `manuscript/replication/`.
10. Update only the logs that match the work performed.
11. Maintain `manuscript/transparency/` for user input, Codex actions, and
    milestone manifests that the external `Manuscript-Timeline` viewer can
    load.
12. Use task folders for fragile or priority-1 scientific tasks. Each new task
    folder should contain `task.md` for the contract and `outcome.md` for the
    short end-of-task answer note.
13. Apply the scientific claim gate before changing mathematical,
    source-sensitive, or code-sensitive claims.
14. Run `python scripts/check_manuscript.py` after substantive edits.

## Next Task Selection

When the user says `work on next task`, `pick next task`, `continue`, or
similar:

1. Read `manuscript/project-dashboard.md` and `manuscript/task-board.md`.
2. Prefer the dashboard's next recommended action unless the user named a
   different task.
3. Ignore `done`, `deferred`, and superseded tasks except as historical
   context.
4. If the selected row links a folder under `manuscript/tasks/`, read
   `task.md` before opening source files or editing anything. If resuming or
   auditing a completed task, read `outcome.md` first for the short answer
   trail. Legacy flat packet files under `manuscript/tasks/` are still valid.
5. If the selected task is priority 1 or fragile scientific work and has no
   folder or packet, create a folder first from
   `manuscript/tasks/_folder-template/`, link `task.md` from
   `task-board.md`, and only then execute the task.
6. Open a transparency milestone before edits, then follow the task contract's
   required reads, stop conditions, and acceptance criteria.

## Planning New Tasks

When the user says `plan next tasks`, `insert a task`, `update tasks`, or
similar:

1. Preserve the user's original prompt in `manuscript/user-input-log.md` and,
   for fragile tasks, in the task folder's `task.md`.
2. Split work into task-board rows only after identifying dependencies and
   blocked-before relationships.
3. Classify each new task as routine or fragile. Treat source verification,
   mathematical derivation, code-to-theory comparison, normalization decisions,
   simulation/figure rebuilds, and prior failed work as fragile.
4. For each fragile or priority-1 scientific task, create a task folder
   immediately under `manuscript/tasks/` and link its `task.md` from the
   task-board row.
5. Keep task-board rows compact; do not store the full scientific hand-off in a
   long table cell.
6. Add acceptance criteria and stop conditions to `task.md` before marking the
   planning task complete.

## Task Folders And Outcome Notes

Keep `manuscript/task-board.md` as a compact index. For priority-1 or fragile
scientific tasks, create a durable folder under `manuscript/tasks/` and link
its `task.md` from the task-board row.

Use a task folder when a task involves raw sources, KnowledgeVault provenance,
mathematical derivations, code-to-theory mapping, simulations, figure rebuilds,
normalization choices, prior failed work, or a long/nuanced user prompt.

Before creating or working from a task folder or legacy packet, read
`references/task-packet-workflow.md`. For new tasks, prefer:

- `manuscript/tasks/Mxx-short-slug/task.md`: the task contract.
- `manuscript/tasks/Mxx-short-slug/outcome.md`: the compact final note.

The outcome note should be short and should answer: what changed, which user
questions were answered, where the detailed evidence lives, what checks ran,
and what remains open. Do not duplicate long derivations or logs there. Legacy
flat task packets remain valid historical artifacts; do not migrate them
unless the user asks or the migration is needed for active work.

## Scientific Claim Gate

Before adding, revising, or relying on a substantive scientific claim, classify
the claim as one of:

- `raw-source`: verified directly in the paper, appendix, replication code, or
  other primary source.
- `vault-source`: verified in a KnowledgeVault note that cites the underlying
  source path and citation key.
- `derived`: proved in the current work block from stated assumptions, with
  enough algebra for audit.
- `code-implemented`: observed in repository or replication code. This can
  describe implementation behavior, but it is not evidence that the behavior is
  the source-correct theory.
- `conjectural`: plausible but not yet verified.
- `user-decision`: an explicit user instruction or durable decision.

Only `raw-source`, `vault-source`, `derived`, or explicit `user-decision`
claims may enter polished manuscript prose as settled statements.
`code-implemented` claims may describe code behavior only. `conjectural`
claims must stay in TODO notes, task boards, derivation files, or discussion
until verified.

For mathematical or source-sensitive work, read
`references/scientific-claim-audit.md` and leave a compact audit trail before
editing the draft or formal registry.

## Transparency Milestones

For every new substantive user request, open a milestone before editing:

```powershell
python scripts/transparency_milestone.py begin --title "Short title" --request "User request or close paraphrase"
```

Close it after the work block and checks:

```powershell
python scripts/transparency_milestone.py close --summary "What changed" --action "Concrete action" --check "python scripts/check_manuscript.py: passed"
```

Create or update a GitHub issue milestone with the same title whenever GitHub
access is available, preferably through the Codex GitHub app/connector and
otherwise through `gh api`. Commit the closed manifest and tag the commit with
the milestone `snapshot_ref`, usually
`manuscript-milestones/M0001-short-title`. Push the branch and tag.

Do not create automatic publication or progress milestones merely because the
manuscript reaches a named state such as source packet complete, paper map
stable, first draft complete, evidence package complete, or shareable draft
ready. Create those milestones only when the user asks for them or when they
are part of an explicit substantive work block.

## Discipline

- One manuscript, one main research idea.
- Prefer short papers with clear reader paths.
- Separate prior-work claims from original contributions in
  `manuscript/citation-provenance.md`.
- Use hidden typed HTML comments for internal manuscript notes during drafting:
  `SOURCE-TRAIL`, `CONTRIBUTION-NOTE`, `TODO-NOTE`, `DESIGN-NOTE`, and
  `EXPORT-NOTE`.
- Do not make a shareable draft depend on relative paths into KnowledgeVault.
