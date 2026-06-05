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

### 2026-06-05 - Initialize standalone manuscript repository

- Origin: user-originated
- User input id: U0003
- Codex role: implemented and logged
- Decision: Create this manuscript as a standalone repository linked to
  KnowledgeVault, with `vault/syntheses/Research proposal - noise-robust
  sign-restricted SVARs.md` as the originating source.
- Rationale: Manuscript work should be shareable and versioned independently
  while retaining explicit source links to the vault.
- Alternatives considered: keeping the manuscript inside `vault/manuscripts/`
  or leaving the template placeholders until the first prose draft.
- Consequence for next work: Use this repository as the paper workspace and
  KnowledgeVault as source memory, citation store, and replication provenance.

### 2026-06-05 - Scope first version as a short theory-and-simulation note

- Origin: user-originated request plus proposal synthesis
- User input id: U0003
- Codex role: synthesized and revised
- Decision: The first version should be bivariate and impact-oriented in the
  main text, centered on the noisy sign pseudo-set, the no-noise independence
  refinement failure/false-precision channel, and the BR-style robust sign
  inversion plus noise diagnostic.
- Rationale: The proposal already has enough formal and evidence burden. Adding
  empirical work, dynamic signs, or a full `K`-variable implementation now would
  slow the core paper and blur the central contribution.
- Alternatives considered: a seven-section paper with an empirical illustration
  and a broader `K`-variable method section.
- Consequence for next work: Formalize Propositions 1-4 first; defer empirical
  illustration and general implementation until the core proof/evidence package
  is stable.

### 2026-06-05 - Treat Drautzburg-Wright as a maintained-null comparator

- Origin: source-packet review
- User input id: U0003
- Codex role: synthesized
- Decision: The paper should not claim that independence refinement is
  mechanically wrong. It should say that no-noise independence refinement is a
  valid test inversion for its maintained null, while diagonal residual noise
  changes the population null and can make finite-sample accepted regions look
  falsely precise.
- Rationale: This is more accurate, fairer, and stronger rhetorically than
  attacking higher moments in general.
- Alternatives considered: presenting the paper as a broad critique of
  higher-moment SVAR identification.
- Consequence for next work: The literature section and Proposition 2 must
  distinguish asymptotic rejection/emptiness from finite-sample
  least-rejected-region interpretation.
