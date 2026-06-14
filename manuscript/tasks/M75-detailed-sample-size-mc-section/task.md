# M75 Detailed Sample-Size MC Section

## Status And Routing

Status: `todo`

Priority: 1

Task-board row: `M75`

Transparency milestone: pending

Outcome note: `outcome.md`

## Original User Prompt

"then plan a new task: Write a detailed section for this mc in the draft.md. I
want to see the exact dgp and the details on the exact computation of the sets
of each estimator (like grid size, what moment conditions does each estimator
have, what is the distribution of each J, what is the cutoff, how do we compute
the efficient W). I need to be able to understand all details and potentially
spot errors. Then i need a nice representation of the results of our T MC. I
want to see if the size of our esimated set is correct and i want to see the
power."

## Why This Task Exists

M74 produced the long 500-replication sample-size Monte Carlo on the
intermediate `27/7/5` grid. The existing output note gives a compact result
table, but the draft needs a self-auditing section that makes the simulation
design and set computation transparent enough for the user to check for
mistakes. The section must separate three objects that are easy to conflate:
truth-inclusion/coverage of the inverted set, the geometric size of the
estimated set, and power or exclusion strength as sample size grows.

## Do Not Trust Without Rechecking

- Do not copy the M74 table into the draft without verifying it against the
  JSON output and the code path that generated it.
- Do not call the pointwise chi-square cutoffs final projected
  confidence-set critical values; M65 still owns projected inference.
- Do not treat code behavior as source-correct theory. Source-sensitive
  statements about Drautzburg-Wright moments need the M49/source audit.
- Do not blur "test size" or "coverage" with "estimated-set size." Coverage
  is truth inclusion; set size is accepted projection share; power needs an
  explicit diagnostic definition.
- Do not assert power from visual narrowing alone. Define the power metric used
  in the section and explain what current outputs can and cannot identify.
- Do not assume the efficient weighting matrix is global or fixed at the true
  point; M71 changed the implementation to candidate-specific pointwise
  covariance weights.
- Do not ignore empty-set frequencies, because empty standard-DW sets at large
  `T` are a substantive warning for the size/power interpretation.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm repository/package context. | task execution |
| `manuscript/source-packet.md` | Confirm active M71/M73/M74 evidence route and source boundaries. | task execution |
| `manuscript/project-dashboard.md` | Confirm current stage, M74 status, and M65 caveat. | task execution |
| `manuscript/paper-map.md` | Place the new section in the reader path. | draft edits |
| `manuscript/task-board.md` | Confirm routing and dependencies. | task execution |
| `manuscript/draft.md` | Locate Section 5 and existing evidence wording. | draft edits |
| `manuscript/formal-object-registry.json` | Locate affected table/evidence objects. | registry edits |
| `manuscript/tasks/M74-sample-size-mc-grid-audit/task.md` | Confirm the M74 task contract. | result interpretation |
| `manuscript/tasks/M74-sample-size-mc-grid-audit/outcome.md` | Confirm M74 launch and closeout state. | result interpretation |
| `manuscript/simulations/m74_sample_size_mc_500_grid27.md` | Human-readable M74 result table. | result interpretation |
| `manuscript/simulations/output/m74_sample_size_mc_500_grid27.json` | Machine-readable M74 records and summaries. | result interpretation |
| `manuscript/simulations/m69_extended_three_block_mc.py` | M74 runner, summaries, progress support, and output construction. | code-to-prose mapping |
| `manuscript/simulations/m68_first_shock_evidence.py` | Shared MC evaluator and metrics. | estimator-set computation |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` | Candidate grid, DGP simulator, moment rows, J statistics, weights, cutoffs, and mask construction. | estimator-set computation |
| `manuscript/tasks/M71-remove-b21-sign-and-pointwise-weighting/outcome.md` | Corrected sign screen and pointwise weighting decision. | estimator-set computation |
| `manuscript/tasks/M73-increase-figure-grid-density/outcome.md` | Dense figure grid context and intermediate-grid comparison. | grid explanation |
| `manuscript/derivations/m49-dw-source-and-noisy-moment-audit.md` | Source-backed DW GMM1/GMM2 moment menu and caveats. | standard-DW source claims |
| `manuscript/derivations/m56-robust-cumulant-gmm-generated-moment-audit.md` | Generated-moment and weighting caveats. | robust GMM inference claims |
| `manuscript/derivations/m66-noise-ratio-bound-grid-algorithm.md` | `lambda_i=nu_i/(BB')_ii` route and grid algorithm. | robust-set definition |
| `manuscript/derivations/dw-robust-comparison-diagnostic.md` | Diagnostic set-size, overlap, and warning metrics. | result representation |
| `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/task.md` | Projected-inference follow-up that limits final claims. | caveat wording |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The M74 DGP fixes residual noise and structural non-Gaussianity while varying `T=500,1000,2000`. | `code-implemented`, `user-decision` | Scenario block in `m69_extended_three_block_mc.py`; M74 JSON configuration. | pending |
| The M74 run uses 500 replications per scenario and grid `27/7/5`. | `code-implemented`, `user-decision` | M74 JSON/Markdown configuration and launch manifest. | pending |
| The sign set, standard-DW set, and robust-DW set are computed by the masks in the current M71/M74 code path. | `code-implemented` | `evaluate_one`, `evaluate_standard_projection`, `evaluate_robust_projection`, and mask diagnostics. | pending |
| The standard-DW higher-moment menu described in the draft is source-backed. | `raw-source` or `vault-source` plus `code-implemented` | M49 audit and source path; code mapping. | pending |
| The robust-DW moment vector and `lambda` nuisance route match the M66/M56 derivations. | `derived`, `code-implemented` | M66 and M56 derivations; active evaluator code. | pending |
| The efficient weighting matrix is candidate-specific and computed from sample moment observations with the active regularization rule. | `code-implemented`, with GMM theory caveat | Active `j_from_observations` code and M56 caveat. | pending |
| The pointwise J statistics use chi-square diagnostic cutoffs with degrees of freedom equal to displayed moment rows. | `derived`, `code-implemented`, `conjectural` for final coverage | Active cutoff constants and M65 caveat. | pending |
| The M74 results answer coverage/truth inclusion, estimated-set size, and power or exclusion diagnostics for the T-changing MC. | `code-implemented`, with interpretation audit | M74 JSON summaries plus any additional computed representation. | pending |

## Required Work

1. Source and derivation work:
   - Audit the exact DGP used by M74: true `B0`, shock distribution,
     non-Gaussian mixture, residual-noise distribution and variance, sample
     sizes, seeds, and replication count.
   - Audit the three reported sets: sign/no-noise second-moment set,
     standard-DW refined set, and robust-DW `(B,lambda)` set.
   - Write down moment rows, J statistic dimensions, chi-square cutoffs,
     and the efficient-weight construction in draft-ready notation.
   - Explicitly mark the pointwise chi-square route as diagnostic and separate
     it from final projected-inference claims.
2. Code and result work:
   - Verify the M74 Markdown table against the JSON summaries.
   - If needed, write a small analysis helper or use an existing parser to
     extract additional result metrics from the JSON records.
   - Define result metrics for coverage/size and power. At minimum report:
     truth-inclusion rates and false-rejection rates, mean/median accepted
     projection share, empty-set rates, and a warning/exclusion metric that is
     explicitly named.
3. Manuscript update work:
   - Add a detailed M74 subsection to `manuscript/draft.md`, likely inside
     Section 5.
   - Include enough implementation detail that a reader can reproduce the
     set-membership calculations from the prose and code paths.
   - Add a clean result representation: table, compact panel, or both. The
     representation must make the `T=500,1000,2000` comparison readable and
     show coverage, set size, and power/exclusion behavior separately.
   - Update the formal registry if a table, figure, equation, or evidence
     object changes.
   - Update citation provenance if new source-sensitive DW/GMM claims enter
     the draft.
4. Task closeout work:
   - Update the M74 outcome if this task performs the final M74 result
     interpretation and closeout.
   - Write the M75 outcome note with the short answer, evidence paths, checks,
     and remaining caveats.
   - Decide whether `manuscript/QUESTION-INDEX.md` needs a row for this
     explanation and result interpretation.

## Stop Conditions

- Stop if the DGP cannot be reconstructed exactly from code and output.
- Stop if the M74 Markdown table and JSON summaries disagree.
- Stop if the active code and derivation notes imply different moment rows or
  different set-membership criteria.
- Stop if the efficient-weighting computation cannot be explained precisely
  from the code.
- Stop if "power" cannot be answered by current outputs without defining a new
  metric; define the metric explicitly or ask the user before drafting a
  strong claim.
- Stop if draft wording would imply final projected confidence-set coverage
  even though M65 remains open.

## Acceptance Criteria

- `draft.md` contains a detailed sample-size MC subsection that states the
  exact DGP, replication design, grid, sign screen, profiled coordinates, and
  set-membership rule for each estimator.
- The section states the moment conditions used by sign, standard DW, and
  robust DW, including J dimensions, chi-square cutoffs, and the pointwise
  diagnostic caveat.
- The section explains how the efficient weighting matrix is computed and
  regularized in the active implementation.
- The result representation separately reports empirical truth inclusion or
  false rejection, estimated-set size, empty-set behavior, and power/exclusion
  diagnostics across `T=500,1000,2000`.
- Every source-sensitive DW claim has source or audit evidence; every
  implementation claim has a code/output path.
- The formal registry, citation provenance, task board, and outcome note are
  updated if affected.
- `python scripts/check_manuscript.py` passes after substantive edits.

## Expected Outputs

- Revised `manuscript/draft.md` Section 5 text.
- Updated result representation, either embedded in `draft.md` or generated as
  a supporting table/figure.
- Updated `manuscript/formal-object-registry.json` if the table/evidence
  object changes.
- Updated `manuscript/citation-provenance.md` if new source-backed claims are
  added.
- Updated `manuscript/tasks/M74-sample-size-mc-grid-audit/outcome.md` if M75
  closes or interprets M74.
- `manuscript/tasks/M75-detailed-sample-size-mc-section/outcome.md`.
