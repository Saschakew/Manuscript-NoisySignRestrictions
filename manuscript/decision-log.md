# Decision Log

Use this file for durable research, scope, notation, evidence, and workflow
decisions.

## Entries

### 2026-06-05 - Formal object typography and proof endings

- Origin: user-originated
- User input id: U0001
- Codex role: implemented and logged
- Decision: In Markdown drafts, assumptions, definitions, propositions, lemmas,
  corollaries, and theorems should be italicized in full, and should not carry
  visible end-marker text. Proofs should start with `Proof:` and end with `□`.
- Rationale: Full-statement italics make the start and end of formal objects
  visually clear without adding artificial closing text.
- Alternatives considered: retaining visible `End of Proposition` markers.
- Consequence for next work: Future draft revisions should format formal
  statements with full italics and proof blocks with the square terminator.

### {{TODAY}} - Initialize standalone manuscript repository

- Origin: user-originated
- User input id: TODO
- Codex role: logged only
- Decision: Create this manuscript as a standalone repository linked to
  KnowledgeVault.
- Rationale: Manuscript work should be shareable and versioned independently
  while retaining source links to the vault.
- Alternatives considered: keeping the manuscript inside `vault/manuscripts/`.
- Consequence for next work: Use this repository as the paper workspace and
  KnowledgeVault as source memory.
