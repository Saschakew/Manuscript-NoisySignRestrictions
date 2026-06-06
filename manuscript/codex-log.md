# Codex Log

Purpose: shareable milestone-level transparency log for Codex work on this
manuscript.

Do not record every micro-edit here. Use this file for substantial Codex-led
work, visible milestones, checks run, and open uncertainties.

Every entry that closes a substantive work block should correspond to a
machine-readable milestone in `transparency/milestones/`.

## Entries

### 2026-06-06 - DW-like Gaussian-noise higher moments

- Request: create a derivation file for a Drautzburg-Wright-like
  higher-moment approach robust to additive noise, contrasting it with the
  invalid no-noise second-moment system.
- Actions taken: created
  `manuscript/derivations/dw-noise-robust-moments.md`; derived why Gaussian
  noise drops out of higher cumulants of `B^{-1}u` but not second moments;
  wrote third and fourth cumulants as moment equations suitable for GMM; and
  recorded the local bivariate rank condition and efficiency tradeoff.
- Files changed: `manuscript/derivations/dw-noise-robust-moments.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/paper-plan.md`,
  `manuscript/paper-map.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, logs, and the M0010 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed, with the expected
  warning that M0010 was still open before milestone closure.
- Open uncertainties: the derivation still needs adversarial audit for
  cumulant-to-moment algebra, normalization, local and global identification,
  and whether the Gaussian-noise route should replace or accompany the broader
  BR-style observed-residual route.

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

### 2026-06-05 - M0005 task-state cleanup

- Request: complete the next open project task, which resolved to stale M21
  transparency cleanup.
- Actions taken: verified that M0005 is closed, committed, tagged at
  `manuscript-milestones/M0005-revise-br-verification-plan`, aligned with
  remote `main`, and closed on GitHub; updated the dashboard and task board so
  the next open research task is M05.
- Files changed: `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/session-log.md`,
  `manuscript/codex-log.md`, and the M0006 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed.
- Open uncertainties: M05 still needs the actual bivariate cumulant derivation
  before any Section 4 claims can be drafted.

### 2026-06-05 - Bivariate cumulant-map derivation

- Request: continue to the next project task, M05.
- Actions taken: created `manuscript/derivations/bivariate-cumulant-map.md`
  with the complete second-, third-, and fourth-order cumulant map for the
  diagonal-normalized bivariate SVAR; classified clean mixed moments separately
  from nuisance pure own moments and mapped noise cumulants.
- Files changed: `manuscript/derivations/bivariate-cumulant-map.md`,
  `manuscript/formal-object-registry.json`, `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`, logs, and the M0007
  transparency files.
- Checks run: `python scripts/check_manuscript.py` passed.
- Open uncertainties: M06 must audit the algebra, notation, and
  clean-versus-nuisance classifications before this map can support Section 4
  claims.

### 2026-06-05 - Bivariate cumulant-map audit

- Request: continue with M06.
- Actions taken: independently checked the coefficient/index pattern for all
  distinct second-, third-, and fourth-order bivariate cumulants; recorded the
  adversarial audit in `manuscript/review-log.md`; updated the derivation note
  to distinguish clean observed equations from restrictions that survive
  nuisance profiling.
- Files changed: `manuscript/derivations/bivariate-cumulant-map.md`,
  `manuscript/review-log.md`, `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, logs, and the M0008 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed.
- Open uncertainties: the map still needs M07 BR applicability work, M09
  profiled criteria and local rank derivation, and M12 symbolic/population
  verification before supporting manuscript result claims.

### 2026-06-05 - Bonhomme-Robin applicability clarification

- Request: continue with M07.
- Actions taken: created `manuscript/derivations/br-applicability.md` to pin
  the BR analogy to the paper's clean-pair and rank conditions; showed why the
  bivariate `L=K=2` SVAR is not covered by full quasi-JADE; defined the
  manuscript object as a low-dimensional BR-style profiled inversion.
- Files changed: `manuscript/derivations/br-applicability.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/paper-map.md`,
  `manuscript/review-log.md`, logs, and the M0009 transparency files.
- Checks run: `python scripts/check_manuscript.py` passed.
- Open uncertainties: M08 must still attack the applicability argument, and
  M09/M12 must derive and verify the profiled criteria before any robust
  inversion claim is draftable.
