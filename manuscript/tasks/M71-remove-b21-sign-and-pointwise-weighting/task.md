# M71 Remove B21 Sign And Use Pointwise Weighting

## Status And Routing

Status: `todo`

Priority: 1

Task-board row: `M71`

Transparency milestone: pending

Outcome note: `outcome.md`

Blocks: M70 draft interpretation and any long M69 500-replication run.

## Original User Prompt

"i stoped you beause we have to make some adjustments. we have to do the long
mc run later. first plan a task to fix the following issues: 1) Do not impose
sign restriction on b21 in the figures 1,2,3 or the MCs. only on b11, b22 and
b12. 2) THe inversion of the J statistic seems to use like an oracle efficient
weighting? like computed at the true B_0? simply for every B and v grid point
compute the efficien W at this point to compute the j statistic."

The user then specified the intended inversion:

For each candidate \(\theta=(B,\nu)\), compute \(g_T(B,\nu)\),
\(\widehat\Omega(B,\nu)=\widehat{\operatorname{Var}}\{\sqrt T
g_T(B,\nu)\}\), and
\[
J_T(B,\nu)
=
T g_T(B,\nu)'\widehat\Omega(B,\nu)^{-1}g_T(B,\nu).
\]

For a fixed true point and consistently estimated moment covariance,
\(J_T(B,\nu)\Rightarrow\chi^2_q\), where \(q\) is the number of tested moment
rows. For the projected \(B\) set, accept \(B\) if there exists \(\nu\) or
\(\lambda\) such that \(J_T(B,\nu)\le\chi^2_{q,1-\alpha}\). This should be
described as pointwise confidence-set or S-statistic inversion, not the
overidentifying-restrictions GMM \(J\)-test at an estimated minimizer.

## Why This Task Exists

M68 and M69 implemented the first-shock projection and extended Monte Carlo,
but two parts of that implementation are not the intended object:

1. The current sign screen imposes \(B_{21}\ge0\). The intended maintained
   sign restrictions are only \(B_{11}>0\), \(B_{22}>0\), and \(B_{12}\le0\).
2. The current figure/MC evaluators build efficient weights once at the true
   DGP point and reuse those weights across the grid. That is useful as an
   oracle diagnostic, but it is not the intended pointwise inversion. Each
   candidate \((B,\nu)\) or \((B,\lambda)\) must carry its own estimated
   covariance matrix and weight.

The interrupted 500-replication M69 run should not be restarted until this
task completes and the corrected quick diagnostics are checked.

## Do Not Trust Without Rechecking

- M68 and M69 output as final evidence. They are now historical diagnostics
  until regenerated under this task.
- Any code path, JSON note, caption, task outcome, or draft wording that treats
  \(B_{21}\ge0\) as a maintained sign restriction.
- `scenario_weights(...)` in
  `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` as the
  intended weighting route. It computes weights at the true point.
- `evaluate_standard_projection(...)`, `evaluate_robust_projection(...)`,
  `standard_truth_j(...)`, and `robust_truth_j(...)` until they are audited for
  candidate-specific covariance estimation.
- Any use of \(q-p\) critical values for fixed candidate inversion. The
  intended cutoff for a fixed tested stack is \(\chi^2_q\), with \(q\) equal
  to the number of tested moment rows.
- Any draft terminology that calls the projected set an overidentifying
  restrictions \(J\)-test at the GMM minimizer.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm KnowledgeVault and package context. | any source or package claim |
| `manuscript/project-dashboard.md` | Confirm current routing and blockers. | task execution |
| `manuscript/paper-map.md` | Locate current evidence contract and stale sign-screen wording. | planning and prose edits |
| `manuscript/task-board.md` | Confirm M71 priority and blocked tasks. | task execution |
| `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/task.md` | Preserve projected-inference and final wording caveats. | inference wording |
| `manuscript/tasks/M68-first-shock-impact-evidence-rebuild/outcome.md` | Identify the current figure/MC implementation and its sign screen. | code edits |
| `manuscript/tasks/M69-extended-three-block-mc/outcome.md` | Identify the current extended MC outputs and size/inclusion metrics. | MC edits |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` | Main evaluator for Figures 1-3 and shared grid logic. | code edits |
| `manuscript/simulations/m68_first_shock_evidence.py` | Existing Monte Carlo diagnostic built on the shared evaluator. | MC edits |
| `manuscript/simulations/m69_extended_three_block_mc.py` | Extended three-block MC that must inherit corrected evaluator behavior. | MC edits |
| `manuscript/replication/run_all.py` | Replication wrapper stages for figures, evidence, and extended MC. | replication edits |
| `manuscript/draft.md` | Locate affected Section 5 and inference terminology. | draft edits |
| `manuscript/formal-object-registry.json` | Locate affected figure, table, and robust-set objects. | registry edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| \(B_{21}\) is not a maintained sign restriction in Figures 1-3 or the MCs. | `user-decision` | This task prompt and updated code/prose. | pending |
| The intended tested statistic estimates \(\widehat\Omega(B,\nu)\) at each candidate point. | `user-decision` plus `code-implemented` | This task prompt and evaluator implementation. | pending |
| Fixed candidate inversion uses \(\chi^2_q\), not \(\chi^2_{q-p}\). | `user-decision` plus `derived` | User-supplied reasoning and a short notation audit in the task outcome or derivation note. | pending |
| The projected \(B\) set accepts if some nuisance value passes the candidate statistic. | `user-decision` plus `code-implemented` | Updated evaluator and regenerated diagnostics. | pending |
| M68/M69 historical outputs remain interpretable as oracle-weight diagnostics. | `code-implemented` | Current code path and output notes, if retained as historical context. | pending |

## Required Work

1. Audit and patch the sign screen:
   - remove \(B_{21}\ge0\) from the admissibility mask in the shared grid;
   - keep \(B_{11}>0\), \(B_{22}>0\), and \(B_{12}\le0\);
   - update configuration metadata, figure notes, MC notes, captions, and
     source trails so they do not list \(B_{21}\ge0\);
   - review the \(B_{21}\) plotting range after removal and expand it if the
     corrected accepted set reaches a boundary.

2. Replace true-point fixed weights with candidate-specific pointwise weights:
   - second-moment row: compute per-candidate observations and covariance for
     the three second-order rows;
   - standard DW row: compute per-candidate observations and covariance for
     the five higher-moment rows;
   - robust row: for each \((B,\lambda)\) or \((B,\nu)\) candidate, compute the
     robust full-stack observations and their covariance, then evaluate
     \(T g'\widehat\Omega^{-1}g\);
   - retain batching so the robust grid does not allocate an infeasible
     \(T \times \#B \times \#\lambda \times q\) array;
   - keep numerical regularization explicit and report any singular-covariance
     failures.

3. Clarify statistic terminology:
   - call the object a pointwise confidence-set or S-statistic inversion;
   - reserve "overidentifying-restrictions \(J\)-test" for the GMM-minimizer
     object with different degrees of freedom;
   - keep the fixed-stack cutoffs as \(\chi^2_3\), \(\chi^2_5\), and
     \(\chi^2_8\) for the current second, standard, and robust tested stacks.

4. Regenerate only after the code path is corrected:
   - run a quick Figure 1 build first;
   - run quick Figure 2 and Figure 3 builds;
   - run quick M68 and M69 diagnostics;
   - run the normal M68/M69 diagnostics only if quick outputs pass and runtime
     is acceptable;
   - do not run the 500-replication MC in this task unless the user explicitly
     asks after the corrected normal diagnostics exist.

5. Update manuscript surfaces:
   - update the formal registry after code and regenerated outputs exist;
   - update `paper-map.md`, `project-dashboard.md`, `task-board.md`,
     simulation READMEs, replication README, and relevant task outcomes;
   - keep M70 blocked until corrected M71 outputs are available.

6. Complete `outcome.md`:
   - answer whether \(B_{21}\) is still restricted anywhere active;
   - answer whether candidate-specific weights replaced the oracle fixed
     weights;
   - state which outputs were regenerated, checks run, and whether
     `manuscript/QUESTION-INDEX.md` was updated.

## Stop Conditions

- Stop if removing the \(B_{21}\) sign restriction makes the current grid
  visibly boundary-bound and a new range decision is needed.
- Stop if candidate-specific robust weighting is too slow or memory-heavy for
  the intended grid; record a batching or approximation plan before running
  the normal MC.
- Stop if covariance estimates are systematically singular after documented
  regularization.
- Stop if the implementation has to choose between \(\nu\)-grid and
  \(\lambda\)-grid parameterization in a way that changes Section 4.
- Stop before draft interpretation if the corrected outputs contradict the
  current figure story in a way that needs user discussion.

## Acceptance Criteria

- No active figure, MC, output metadata, draft source trail, or planning
  surface lists \(B_{21}\ge0\) as a maintained sign restriction.
- The shared evaluator computes the pointwise statistic using
  \(\widehat\Omega(B,\nu)\) at each tested candidate, not a true-point oracle
  weight reused across the grid.
- The projected robust set accepts \(B\) when some profiled nuisance candidate
  satisfies \(J_T(B,\nu)\le\chi^2_{q,1-\alpha}\).
- Quick builds for Figures 1-3, M68, and M69 pass before any normal run.
- Generated JSON validates with `python -m json.tool`.
- Edited Python validates with `python -m py_compile`.
- `python scripts/check_manuscript.py` passes after planning/prose/registry
  edits.
- M70 remains blocked until corrected outputs exist.

## Expected Outputs

- Patched `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py`
- Patched `manuscript/simulations/m68_first_shock_evidence.py`
- Patched `manuscript/simulations/m69_extended_three_block_mc.py`
- Regenerated Figures 1-3 and diagnostic notes/JSON after quick checks pass
- Regenerated M68/M69 diagnostic outputs, but not the deferred 500-run unless
  separately requested
- Updated registry/planning/provenance surfaces after implementation
- Completed `outcome.md`
