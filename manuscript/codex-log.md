# Codex Log

Purpose: shareable milestone-level transparency log for Codex work on this
manuscript.

Do not record every micro-edit here. Use this file for substantial Codex-led
work, visible milestones, checks run, and open uncertainties.

Every entry that closes a substantive work block should correspond to a
machine-readable milestone in `transparency/milestones/`.

## Entries

### 2026-06-05 - Formal object typography

- Request: update manuscript writing rules for propositions, definitions, and
  proofs.
- Actions taken: added a full-block italics rule for formal statements, removed
  the visible end-marker convention, and standardized proof starts and endings.
- Files changed: `manuscript/manuscript-rules.md`,
  `manuscript/user-input-log.md`, `manuscript/decision-log.md`,
  `manuscript/session-log.md`, `manuscript/codex-log.md`.
- Checks run: `python scripts/check_manuscript.py` passed.
- Open uncertainties: KnowledgeVault link remains in template mode, but this
  work did not depend on vault source material.

### 2026-06-05 - Template initialization

- Request: initialize a standalone manuscript from the KnowledgeVault proposal
  on noise-robust sign-restricted SVARs and prepare a careful plan.
- Actions taken: validated the KnowledgeVault checkout and `svar-toolkit`
  package path; initialized manuscript metadata; built the source packet;
  revised the paper plan after a first-pass structure; updated the paper map,
  task board, workplan, formal-object registry, citation provenance,
  literature search, replication plan, draft skeleton, and logs; copied a first
  verified bibliography snapshot.
- Files changed: `knowledge-vault-link.json`, `bibliography/references.bib`,
  `manuscript/source-packet.md`, `manuscript/paper-plan.md`,
  `manuscript/paper-map.md`, `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/literature-search.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`, logs, and the
  M0003 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed, with the expected
  warning that M0003 was still open before milestone closure.
- Open uncertainties: Proposition 2 genericity conditions and Proposition 3
  regularity conditions need exact statements before drafting polished prose.

### 2026-06-05 - Bonhomme-Robin verification revision

- Request: incorporate corrected KnowledgeVault notes on Bonhomme-Robin noisy
  ICA and the BR-style SVAR inversion.
- Actions taken: reread the updated vault notes, updated the KnowledgeVault
  source commit, revised the paper plan/map/source packet, marked the BR-style
  propositions as unverified until derivation and simulation checks pass, added
  interleaved adversarial review tasks, and updated replication instructions.
- Files changed: `knowledge-vault-link.json`, `manuscript/source-packet.md`,
  `manuscript/paper-plan.md`, `manuscript/paper-map.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/literature-search.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`, logs, and the
  M0005 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed, with the expected
  warning that M0005 was still open before milestone closure.
- Open uncertainties: the BR-style cumulant map, local rank condition, and
  noise diagnostic must be derived and stress-tested before becoming manuscript
  claims.
