---
name: write-standalone-manuscript
description: Write and manage one standalone manuscript repository linked to KnowledgeVault source material. Use for manuscript planning, drafting, formal objects, simulations, citations, logs, transparency milestones, and scientific-claim audits that require raw-source, vault-source, derivation, or code-provenance gates before prose changes.
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
12. Apply the scientific claim gate before changing mathematical,
    source-sensitive, or code-sensitive claims.
13. Run `python scripts/check_manuscript.py` after substantive edits.

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

## Discipline

- One manuscript, one main research idea.
- Prefer short papers with clear reader paths.
- Separate prior-work claims from original contributions in
  `manuscript/citation-provenance.md`.
- Use hidden typed HTML comments for internal manuscript notes during drafting:
  `SOURCE-TRAIL`, `CONTRIBUTION-NOTE`, `TODO-NOTE`, `DESIGN-NOTE`, and
  `EXPORT-NOTE`.
- Do not make a shareable draft depend on relative paths into KnowledgeVault.
