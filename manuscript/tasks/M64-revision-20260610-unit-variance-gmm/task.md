# M64 Revision 20260610 Unit-Variance GMM Repair

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M64`

Transparency milestone: `M0061-recover-revision-20260610-comments`

Outcome note: `outcome.md`

## Original User Prompt

"WHAT!? that was terrible! My reivion.md contained some general comments, i
made a bunch of changes in draft.md (which you should detect based on the
changes from my draft to your old draft) and i also made a bunch of comments in
my draft.md!"

Earlier request: "i justfinished Revision-20260610-190805. work on it. first
get an overview what needs to get done and work in a structured way"; then:
"go on".

## Why This Task Exists

The first attempt used a stale local view of `Revision-20260610-190805` and
treated its placeholder `revision.md` as the real revision. The live remote
branch actually contains substantive general comments, draft edits, and inline
comments. Those comments reverse the prior M54 decision to keep
`diag(B)=1`: the manuscript must use the unit structural-shock variance
normalization \(E[\varepsilon_t\varepsilon_t']=I\), and Section 4 should be
rewritten as a standard GMM problem over \(B\) and residual-noise variance
parameters.

## Do Not Trust Without Rechecking

- The stale checked-in `manuscript/revisions/Revision-20260610-190805/revision.md`
  placeholder.
- The prior dashboard statement that a unit-variance rewrite is only a future
  user decision.
- M54's retained `diag(B)=1` route.
- M52 figures and Monte Carlo evidence as final evidence for the revised
  estimator.
- Section 4's previous sample plug-in covariance-product route as the active
  final estimator.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Resolve KnowledgeVault and package paths. | source or code claims |
| `manuscript/source-packet.md` | Check active sources, code, and evidence status. | draft or registry edits |
| `manuscript/project-dashboard.md` | Confirm stale next-action state. | task routing |
| `manuscript/paper-map.md` | Confirm affected sections and formal objects. | section rewrites |
| `manuscript/task-board.md` | Confirm task sequence and superseded next action. | planning edits |
| `manuscript/draft.md` | Apply revision comments to prose. | draft edits |
| `manuscript/formal-object-registry.json` | Update affected objects. | registry edits |
| `manuscript/revisions/Revision-20260610-190805/revision.md` | Preserve general revision comments. | task execution |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The manuscript should use \(E[\varepsilon_t\varepsilon_t']=I\) and not `diag(B)=1`. | `user-decision` | Live revision branch `revision.md` and inline draft comments. | accepted for M64 |
| The no-noise sign set must impose \(E[e_t(B)e_t(B)']=I\). | `derived` and `user-decision` | Section 2 derivation from \(u_t=B_0\varepsilon_t\). | drafted |
| A noise-robust second-order screen can be written as \(\Sigma_u=BB'+\operatorname{diag}(\nu)\) with an entrywise ratio bound. | `derived` | Section 4 derivation from \(Var(\varepsilon_t)=I\). | drafted; needs M65 code/audit |
| The robust higher-moment rows can use parameter-implied \(\omega_{ij}(B,\nu)\) terms, making the criterion standard GMM in \((B,\nu)\). | `derived` | Section 4 moment vector. | drafted; needs M65 implementation/audit |
| M52 figures and table validate the new estimator. | `conjectural` | Must be rebuilt under the unit-variance GMM route. | rejected for now; marked historical |

## Required Work

1. Recover the live revision branch artifacts into the current worktree.
2. Extract the actionable inline comments into a durable task trail.
3. Revise Sections 2-4 for the unit-variance normalization and standard GMM route.
4. Mark the old M52 evidence as historical until rebuilt.
5. Update task routing so the next action is the unit-variance GMM evidence and registry rebuild, not citation/export cleanup.
6. Complete `outcome.md` and update `QUESTION-INDEX.md` because the normalization and standard-GMM answers will be searched for later.

## Stop Conditions

- Stop before final evidence claims if the figure or Monte Carlo code still uses the old `diag(B)=1` chart.
- Stop before theorem-level wording if the projected GMM critical value is not fixed.
- Stop if Section 4's proposed \((B,\nu)\) moment vector cannot be implemented without changing the simulation parameterization.

## Acceptance Criteria

- The live `revision.md`, `revision.json`, and draft revision content are recovered.
- `draft.md` no longer contains raw inline `\comment{...}` or `\commet{...}` markers from the revision.
- Section 2 contains the full unit-variance second-moment vector.
- Section 4 contains the \((B,\nu)\) standard GMM formulation.
- The evidence section clearly marks old figures and table as historical until rebuilt.
- Task board, dashboard, registry, logs, and question index route the project to M65.
- `python scripts/check_manuscript.py` passes after close.

## Expected Outputs

- Recovered revision artifacts.
- First-pass revised `manuscript/draft.md`.
- Updated planning and registry surfaces.
- `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/` as the next task.
- Completed `outcome.md`.
