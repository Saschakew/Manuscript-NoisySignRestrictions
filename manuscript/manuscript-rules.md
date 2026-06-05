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

## Source Of Truth

`draft.md` contains manuscript prose. `formal-object-registry.json` is an audit
and navigation layer unless a safe generation script exists.
