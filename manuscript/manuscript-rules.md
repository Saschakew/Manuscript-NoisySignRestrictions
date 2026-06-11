# Manuscript Rules

Purpose: local writing rules for numbering, labels, object discipline, source
provenance, and export.

## Numbering And Labels

- Every figure must have a number, short title, and self-contained caption.
- Every figure must be referenced in the text before or near where it appears.
- Every table must have a number, short title, and self-contained caption.
- Important equations must have stable labels, such as `eq:main-moment`.
- Assumptions, definitions, propositions, lemmas, corollaries, and theorems
  must have stable labels and numbers.
- Proofs must identify the result they prove and have status `main-text`,
  `appendix`, `sketch`, or `missing`.
- Object labels must be registered in `formal-object-registry.json`.
- In Markdown drafts, each formal statement block must be italicized in full,
  including its label, number, optional title, and complete statement text. This
  applies to assumptions, definitions, propositions, lemmas, corollaries, and
  theorems.
- Do not use visible ending text for formal statements, such as `End of
  Proposition` or `End of Definition`.
- Proofs must start with `Proof:` and end with `□`. Do not add visible
  `End of proof` text.

## Object Discipline

- A definition introduces vocabulary or notation that will be used later.
- An assumption states a maintained condition and should say where it is used.
- A proposition states a result the paper contributes, adapts, or clarifies.
- A figure or table must answer a specific manuscript question.
- A key equation should be referenced by role, not only by number.
- Limitations should attach to a result, assumption, simulation design, or scope
  boundary.

## Internal Notes

Formal paper prose must not contain visible working labels such as `Source:`,
`Sources:`, `Source trail:`, `Contribution:`, `Writing warning:`, or `Final
citation keys needed`.

Use typed HTML comments for internal notes during drafting:

- `<!-- SOURCE-TRAIL: ... -->`
- `<!-- CONTRIBUTION-NOTE: ... -->`
- `<!-- TODO-NOTE: ... -->`
- `<!-- DESIGN-NOTE: ... -->`
- `<!-- EXPORT-NOTE: ... -->`

These notes are for manuscript work, not final paper prose. Clean exports should
hide them or remove them.

## Citation Discipline

- Every non-original paragraph needs a citation or source trail.
- Every original contribution should be marked in prose, object titles, or
  `citation-provenance.md`.
- Use `../bibliography/references.bib` as the self-contained BibTeX source.
- Do not make a shareable draft depend on `../KnowledgeVault` or another local
  relative path.
- When a citation comes from KnowledgeVault, record the vault paper note path,
  citation key, BibTeX path, and verification status in
  `citation-provenance.md`.

## Scientific Claim Gates

Before a mathematical, source-sensitive, or code-sensitive claim enters
polished prose, classify it as one of:

- `raw-source`: verified directly in the source paper, appendix, replication
  code, or other primary source.
- `vault-source`: verified in a KnowledgeVault note with source path and
  citation key.
- `derived`: derived in the current manuscript work from stated assumptions,
  with enough algebra to audit.
- `code-implemented`: observed in local code. Use only for code behavior unless
  the source-to-code mapping is separately verified.
- `conjectural`: plausible but not verified.
- `user-decision`: explicitly instructed or decided by the user.

Only `raw-source`, `vault-source`, `derived`, or explicit `user-decision`
claims may be written as settled manuscript statements. Keep `code-implemented`
claims about implementation behavior. Keep `conjectural` claims in TODO notes,
task artifacts, or discussion until they are verified.

When a prior artifact is found unreliable, mark it as partial or superseded in
the task board, add a warning to the artifact itself, quarantine affected draft
claims with TODO notes, and create a new source-first task.

## Task Folders And Outcome Notes

`manuscript/task-board.md` is a compact index. It must not be the only durable
hand-off for priority-1 or fragile scientific work.

Create a task folder under `manuscript/tasks/` when a task involves a long user
prompt, a prior failure, raw-source or KnowledgeVault verification,
mathematical derivation, code-to-theory comparison, normalization choices,
simulation or figure rebuild decisions, or any source-sensitive claim. Link
the folder's `task.md` from the task-board row.

For new tasks, prefer:

- `manuscript/tasks/Mxx-short-slug/task.md` for the contract.
- `manuscript/tasks/Mxx-short-slug/outcome.md` for the short answer note.

`task.md` should preserve the original user prompt, name untrusted prior
artifacts, list required source reads and derivations, include a scientific
claim ledger, define stop conditions, and state acceptance criteria.
`outcome.md` should briefly state what was done, which user questions were
answered, where the detailed evidence lives, which checks ran, and what
remains open. Keep it short; do not duplicate long derivations, simulations,
or transparency logs. It should also state whether
`manuscript/QUESTION-INDEX.md` was updated or not needed. Update that index
only when the task answers a question someone is likely to search for later.

A fragile scientific task is not complete until its acceptance criteria are
satisfied, checks pass, the outcome note is written, and unresolved points are
explicitly recorded. The outcome note should record the question-index
decision. Legacy flat task packets remain valid historical artifacts and do not
need migration unless they are reopened.

For `work on next task` style requests, select the next task from the dashboard
and task board, then read the linked `task.md` before doing source work,
derivations, draft edits, simulations, or registry edits. If the next task is
fragile or priority 1 and has no task folder or packet, create and link the
folder first.

For `plan next tasks` style requests, classify each planned task as routine or
fragile. Create and link packets immediately for fragile or priority-1
scientific tasks; keep the task-board row short and put the original prompt,
evidence obligations, stop conditions, and acceptance criteria in `task.md`.

## Source Of Truth

`draft.md` contains manuscript prose. `formal-object-registry.json` is an audit
and navigation layer unless a safe generation script exists.
