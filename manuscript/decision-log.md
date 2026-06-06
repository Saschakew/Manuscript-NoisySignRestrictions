# Decision Log

Use this file for durable research, scope, notation, evidence, and workflow
decisions.

## Entries

### 2026-06-06 - Restrict first paper to simultaneous SVAR and add early MC gate

- Origin: user-originated
- User input id: U0013
- Codex role: implemented and continued
- Decision: The first version focuses only on the simultaneous SVAR impact
  system. The paper treats the reduced-form residual `u_t` as given and does
  not model VAR lags, lag estimation, dynamic impulse responses, or
  horizon-specific sign restrictions. After the analytical J-test inversion
  result, the next evidence step should be a lightweight Monte Carlo overview
  before investing in polished figures or a large replication suite.
- Rationale: This keeps the project small enough to evaluate quickly and makes
  the go/no-go evidence gate explicit.
- Alternatives considered: retaining language about dynamic signs and VAR
  lags as deferred but still nearby, or building final figures before checking
  whether the finite-sample J-test comparison works.
- Consequence for next work: Complete M25, then run the new M35 early MC
  triage before spending major effort on M26-M30 polish.

### 2026-06-06 - Treat robust DW derivation as a local audited route

- Origin: Codex adversarial audit of the active plan
- User input id: U0012
- Codex role: selected next task and audited
- Decision: The robust DW higher-cumulant route may remain the constructive
  method in the active paper, but only as a local normalized Gaussian-noise
  result until population-grid and Monte Carlo checks are complete.
- Rationale: The audit found no error in the higher-cumulant cancellation,
  third/fourth cumulant moment equations, second-moment exclusion, or local
  rank calculation. It did identify important boundaries: the bivariate
  `B(a,b)` chart fixes scale rather than recovering it, `C_{1122}` is second
  order at the truth, non-Gaussian residual noise is not covered by the clean
  cumulant argument, and remote finite-order aliases remain possible.
- Alternatives considered: promoting the route immediately to a global theorem,
  or abandoning it because it does not identify scale or cover non-Gaussian
  noise.
- Consequence for next work: M25 should attack the standard-DW
  misspecification/empty-set claim; M28 must check robust-DW truth inclusion,
  remote aliases, and weak-moment widening on population grids.

### 2026-06-06 - Pivot active paper to robust DW comparison

- Origin: user-originated
- User input id: U0011
- Codex role: implemented and logged
- Decision: The active manuscript plan is now a robust-DW comparison paper.
  The paper should first show noisy sign-set bias, then show how standard
  Drautzburg-Wright refinement can falsely shrink a misspecified set under
  residual noise, then propose a robust DW higher-moment set that drops
  second-moment restrictions, and finally compare the standard and robust sets
  as a practical robustness check.
- Rationale: This gives the manuscript a cleaner structure and a sharper
  applied recommendation than the previous candidate route. It also keeps the
  higher-moment idea close to the main comparator while making the efficiency
  cost of noise robustness explicit.
- Alternatives considered: retaining the previous constructive route in the
  active paper, or adding an empirical application before the formal/simulation
  package is stable.
- Consequence for next work: Audit the robust DW derivation, prove or weaken
  the standard-DW asymptotic-empty claim, design the intuitive sign-noise
  figure, and build Monte Carlo comparisons before drafting polished prose.

### 2026-06-06 - Treat Gaussian-noise DW-like moments as a candidate route

- Origin: user-originated
- User input id: U0010
- Codex role: derived and logged
- Decision: Add a derivation for a Gaussian-noise
  Drautzburg-Wright-like higher-cumulant route, while keeping it as a
  candidate structure until adversarial audit. The route drops no-noise
  covariance whitening, searches over a normalized impact space, and uses
  mixed higher cumulants of `B^{-1}u` written as GMM-style moment equations.
- Rationale: Under Gaussian additive residual noise, higher cumulants of
  candidate transformed residuals are not shifted by the noise, but second
  moments are shifted. This gives a cleaner restricted route at the cost of
  assuming Gaussian noise and discarding structural second-moment information.
- Alternatives considered: continuing with the previous observed-residual
  cumulant route, or treating standard no-noise DW covariance whitening as
  valid under residual noise.
- Consequence for next work: Audit the new derivation, especially the
  cumulant-to-moment algebra, scale normalization, local rank conditions,
  finite-sample bias wording, and whether this route can carry the active
  constructive section.

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

### 2026-06-05 - Verify the Bonhomme-Robin-style result before claiming it

- Origin: user correction and updated KnowledgeVault notes
- User input id: U0005
- Codex role: analyzed and revised plan
- Decision: The paper should no longer frame the constructive method as a
  direct Bonhomme-Robin clean-moment inversion. It should call the bivariate
  method a Bonhomme-Robin-style profiled cumulant inversion, derive it
  independently, and verify it with symbolic, population, and finite-sample
  simulations before promoting it to a manuscript result.
- Rationale: The corrected vault notes clarify that Bonhomme and Robin first
  identify/subtract error cumulants using clean-pair restrictions and that the
  `L=K=2` bivariate SVAR is not directly covered by the full quasi-JADE rank
  theorem. Pure own moments are nuisance or diagnostic moments unless extra
  restrictions are placed on the noise.
- Alternatives considered: keeping the earlier plan that treated mixed
  cumulants as the BR fix and using existing figures as sufficient evidence.
- Consequence for next work: The next work block should derive the bivariate
  cumulant system, run adversarial derivation reviews, build verification
  simulations, and only then draft the BR-style result.
