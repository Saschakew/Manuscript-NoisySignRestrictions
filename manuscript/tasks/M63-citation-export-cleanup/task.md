# M63 Citation And Export Cleanup

## Status And Routing

Status: `todo`

Priority: 2

Task-board row: `M63`

Transparency milestone: pending

Outcome note: `outcome.md`

## Original User Prompt

M33 closeout after the request to continue from `Revision-20260610-190805`
identified references cleanup and export preparation as the next remaining
shareable-draft bottleneck.

## Why This Task Exists

After M64, this task is deferred. M33 wrapped the pre-M64 figures and M52
evidence, but Revision-20260610-190805 changed the active normalization and
estimator. M65 must rebuild the unit-variance GMM evidence before
citation/source cleanup and export readiness can be audited.

## Do Not Trust Without Rechecking

- `draft.md` still contains TODO/export notes, including author and citation
  style placeholders.
- `bibliography/references.bib` may need cleanup before a shareable export.
- Internal source trails are useful for manuscript work but must not leak into
  final visible prose.
- M33 wrapper strength is enough for local rebuilds, but a standalone archive
  may still need exact dependency pins and copied/package source.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/draft.md` | Locate TODO/export notes, citations, and final prose issues. | edits |
| `manuscript/manuscript-rules.md` | Citation, internal-note, numbering, and export discipline. | edits |
| `manuscript/citation-provenance.md` | Verify source trails and contribution boundaries. | citation cleanup |
| `bibliography/references.bib` | Confirm self-contained BibTeX entries. | citation cleanup |
| `manuscript/formal-object-registry.json` | Check figure/table/proposition labels and source paths. | registry edits |
| `manuscript/replication/README.md` | Confirm final figure/table rebuild commands. | export readiness |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| All non-original shareable prose has a citation or source trail. | `raw-source` / `vault-source` | `citation-provenance.md`; BibTeX entries; draft citations | pending |
| Final visible export does not expose internal TODO, SOURCE-TRAIL, or EXPORT-NOTE comments. | `code-implemented` | export/check command or text audit | pending |

## Required Work

1. Audit `draft.md` for visible TODOs, citation placeholders, and internal
   comments that need export handling.
2. Audit `citation-provenance.md` and `bibliography/references.bib` against
   cited keys in the draft.
3. Decide whether to clean only references/export notes or create separate
   follow-up tasks for larger prose/citation problems.
4. Update dashboard, task board, outcome, and question index only as needed.
5. Run `python scripts/check_manuscript.py`.

## Stop Conditions

- Stop if a prose claim lacks source support and cannot be verified in the
  current source packet or bibliography.
- Stop if export cleanup would require changing substantive claims.
- Stop if a missing citation requires KnowledgeVault/raw-source work beyond a
  narrow cleanup pass.

## Acceptance Criteria

- Remaining export blockers are resolved or explicitly listed as follow-up.
- Bibliography and citation provenance are consistent enough for a shareable
  draft pass.
- Internal manuscript notes are either cleaned or accounted for by the export
  process.
- `outcome.md` records checks and the question-index decision.

## Expected Outputs

- Updated `draft.md`, `citation-provenance.md`, `bibliography/references.bib`,
  and/or export notes if cleanup proceeds.
- `manuscript/tasks/M63-citation-export-cleanup/outcome.md`
