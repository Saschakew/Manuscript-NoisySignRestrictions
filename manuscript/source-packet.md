# Source Packet

Purpose: curated KnowledgeVault context for this manuscript. Build this before
drafting prose, then keep it compact and source-backed.

## Vault Connection

- KnowledgeVault link: `../knowledge-vault-link.json`
- Local path: `{{KNOWLEDGE_VAULT_LOCAL_PATH}}`
- Repository: `{{KNOWLEDGE_VAULT_REPOSITORY_URL}}`
- Commit: `{{KNOWLEDGE_VAULT_COMMIT}}`
- Validated on: {{TODAY}}
- Status: {{KNOWLEDGE_VAULT_ORIENTATION_STATUS}}

Required surfaces to validate:

- `vault/_index.md`
- `vault/_paper_registry.json`
- `vault/_replication_registry.json`
- `vault/papers/`
- `vault/syntheses/`
- `vault/citations/references.bib`
- `replications/`

## Computational Package

- Package: `svar-python`
- Import name: `svar_toolkit`
- Resolved KnowledgeVault path: TODO
- Version, wheel, or commit: TODO
- Validation status: TODO
- Manuscript use: TODO

Use this package as the default computational foundation for SVAR estimation,
identification, inference, simulations, and replication code. Record any missing
routine as package follow-up before implementing local manuscript code.

## Manuscript Question

TODO: State the research question or idea used to search the vault.

## Orientation Searches

| Query or entry point | Vault area | Result | Follow-up |
|---|---|---|---|
| TODO | `vault/syntheses/` | TODO | TODO |
| TODO | `vault/papers/` | TODO | TODO |
| TODO | `replications/` | TODO | TODO |

## Core Source Set

Keep this list small enough to fit in active manuscript context. Prefer the
5-20 notes that will actually shape the paper.

| Priority | Vault path | Role in manuscript | Citation key | Status |
|---:|---|---|---|---|
| 1 | TODO | TODO | TODO | todo |

Statuses: `candidate`, `source-backed`, `needs-verification`, `dropped`.

## Relevant Syntheses

| Vault synthesis path | Why it matters | Manuscript use |
|---|---|---|
| TODO | TODO | TODO |

## Relevant Replications Or Code

| Vault path | What it validates or illustrates | Manuscript action |
|---|---|---|
| TODO | TODO | TODO |

## Relevant `svar-python` APIs

| API or module | Package path | Manuscript use | Status |
|---|---|---|---|
| TODO | TODO | TODO | todo |

## Citation Snapshot Plan

| Citation key | Vault BibTeX path | Verification status | Copy to bibliography? |
|---|---|---|---|
| TODO | TODO | needs-verification | TODO |

## Gaps And Risks

- TODO: Important missing source, ambiguous claim, or unverified citation.

## Transfer Rules

- Use this packet to decide what Codex should read before drafting.
- Record section-level claims in `citation-provenance.md`.
- Copy only needed verified BibTeX entries into `../bibliography/references.bib`.
- Prefer `svar-python` APIs over manuscript-local implementations for SVAR
  computation.
- Do not make shareable prose depend on readers having KnowledgeVault access.
