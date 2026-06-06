# Session Log

Record meaningful work blocks. Avoid duplicating every detail already visible in
Git history or the task board.

For traceable work blocks, pair this human-readable note with a closed
`transparency/milestones/*.json` manifest and a Git milestone tag.

## Entries

### 2026-06-06 - Derive DW-like Gaussian-noise higher moments

- Request or goal: create a new derivation file for a
  Drautzburg-Wright-like approach robust to additive noise.
- Files changed: `manuscript/derivations/dw-noise-robust-moments.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/paper-plan.md`,
  `manuscript/paper-map.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, logs, and M0010 transparency files.
- Summary of work: derived a Gaussian-noise higher-cumulant system that
  searches over normalized impact matrices rather than covariance-whitened
  rotations, writes the third and fourth cumulant restrictions as
  GMM-style moment equations, shows why second moments remain contaminated by
  noise, and gives bivariate local-rank conditions.
- Next recommended action: run an adversarial audit of the DW-like route before
  deciding whether it simplifies the paper structure or remains a restricted
  benchmark beside the BR-style route.

### 2026-06-05 - Formal object typography rule

- Request or goal: revise the manuscript writing rules for formal statements
  and proofs.
- Files changed: `manuscript/manuscript-rules.md`,
  `manuscript/user-input-log.md`, `manuscript/decision-log.md`,
  `manuscript/session-log.md`, `manuscript/codex-log.md`.
- Summary of work: replaced visible formal-object end markers with full-block
  italics for assumptions, definitions, propositions, lemmas, corollaries, and
  theorems; set proofs to start with `Proof:` and end with `□`.
- Next recommended action: apply the rule when formal objects are added to
  `draft.md`.

### 2026-06-05 - Initialize manuscript repository

- Request or goal: initialize a standalone manuscript from the KnowledgeVault
  proposal on noise-robust sign-restricted SVARs and prepare a careful writing
  plan and task sequence.
- Files changed: `knowledge-vault-link.json`, `bibliography/references.bib`,
  `manuscript/source-packet.md`, `manuscript/paper-plan.md`,
  `manuscript/paper-map.md`, `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/literature-search.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`, and logs.
- Summary of work: validated the KnowledgeVault checkout, initialized metadata,
  read the proposal and related source cluster, revised the initial structure
  into a shorter theory-and-simulation plan, listed core formal objects, copied
  a first verified bibliography snapshot, and created next tasks.
- Next recommended action: write exact formal statements and proof obligations
  for the noisy pseudo-set, no-noise independence refinement failure, the
  profiled cumulant inversion, and mapped noise diagnostic.

### 2026-06-05 - Revise Bonhomme-Robin verification plan

- Request or goal: update the manuscript plan after corrected KnowledgeVault
  notes on Bonhomme-Robin and noisy ICA.
- Files changed: `knowledge-vault-link.json`, `manuscript/source-packet.md`,
  `manuscript/paper-plan.md`, `manuscript/paper-map.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/literature-search.md`,
  `manuscript/replication/README.md`, `manuscript/draft.md`, and logs.
- Summary of work: revised the plan so the constructive BR component is a
  verified bivariate profiled cumulant inversion rather than a direct import
  of the original BR theorem; added analytic derivation, simulation
  verification, and adversarial review tasks.
- Next recommended action: write the bivariate cumulant derivation and run the
  first adversarial derivation audit before drafting Section 4.

### 2026-06-05 - Close stale M0005 task state

- Request or goal: complete the next open project task by finishing the stale
  M21 transparency cleanup.
- Files changed: `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/session-log.md`,
  `manuscript/codex-log.md`, and M0006 transparency files.
- Summary of work: verified that M0005 is closed, committed, tagged at
  `manuscript-milestones/M0005-revise-br-verification-plan`, aligned with
  remote `main`, and closed on GitHub; marked M21 done and cleared the stale
  active milestone note.
- Next recommended action: open a substantive milestone for M05 and derive the
  corrected bivariate cumulant map from scratch.

### 2026-06-05 - Derive bivariate cumulant map

- Request or goal: continue to the next project task, M05.
- Files changed: `manuscript/derivations/bivariate-cumulant-map.md`,
  `manuscript/formal-object-registry.json`, `manuscript/project-dashboard.md`,
  `manuscript/task-board.md`, `manuscript/workplan.md`,
  `manuscript/session-log.md`, `manuscript/codex-log.md`, and M0007
  transparency files.
- Summary of work: derived the full second-, third-, and fourth-order cumulant
  map for `u_t = B(a,b) epsilon_t + eta_t`, including nuisance diagonal noise
  cumulants and clean-versus-nuisance moment classifications.
- Next recommended action: run the M06 adversarial derivation audit before
  using the cumulant map in a draft result or local identification proof.

### 2026-06-05 - Audit bivariate cumulant map

- Request or goal: continue with M06.
- Files changed: `manuscript/derivations/bivariate-cumulant-map.md`,
  `manuscript/review-log.md`, `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/session-log.md`,
  `manuscript/codex-log.md`, and M0008 transparency files.
- Summary of work: adversarially checked the cumulant derivation for indices,
  cumulant definitions, normalization, missing moments, and clean-versus-
  nuisance classifications. No coefficient/index errors were found; the audit
  corrected wording so clean third mixed cumulants are not overstated as
  identifying restrictions after unrestricted `gamma` profiling.
- Next recommended action: start M07 by documenting what the Bonhomme-Robin
  analogy does and does not justify for the bivariate `L=K=2` case.

### 2026-06-05 - Clarify Bonhomme-Robin applicability

- Request or goal: continue with M07.
- Files changed: `manuscript/derivations/br-applicability.md`,
  `manuscript/formal-object-registry.json`,
  `manuscript/project-dashboard.md`, `manuscript/task-board.md`,
  `manuscript/workplan.md`, `manuscript/paper-map.md`,
  `manuscript/review-log.md`, `manuscript/session-log.md`,
  `manuscript/codex-log.md`, and M0009 transparency files.
- Summary of work: documented why the original Bonhomme-Robin quasi-JADE
  theorem does not directly apply to the bivariate `L=K=2` SVAR: independent
  bivariate errors provide only one clean pair, so the all-kurtotic rank
  condition cannot hold, and the skewness route does not cover two factors
  when `L=2`. Defined the manuscript object as a BR-style profiled inversion.
- Next recommended action: run M08 by attacking this applicability argument
  before deriving profiled criteria in M09.
