# M72 Fix Figure Layout

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M72`

Transparency milestone: `M0068-m72-fix-figure-layout`

GitHub milestone: #63

Outcome note: `outcome.md`

## Original User Prompt

"fix the figures! therx look wired"

The user attached a rendered Figure 1 screenshot showing very tall, narrow
panels with large white space and accepted regions crowded near the top.

## Why This Task Exists

M71 correctly removed the \(B_{21}\) sign restriction and widened the plotted
\(B_{21}\) range, but the figure renderer kept equal data-unit aspect. Because
the displayed \(B_{21}\) span is much larger than the \(B_{11}\) span, the
subplots became skinny towers. This is a presentation bug in the active
evidence figures, not a change to the M71 identification object.

## Do Not Trust Without Rechecking

- Do not reintroduce \(B_{21}\ge0\) as a sign restriction.
- Do not change the candidate grid, pointwise weighting, or chi-square
  cutoffs merely to make the figure prettier.
- Do not hide negative \(B_{21}\) if doing so would obscure that the sign is
  not imposed; the fix should improve layout while keeping the sign-free
  plotted coordinate visible.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm repository/vault context. | any manuscript work |
| `manuscript/project-dashboard.md` | Confirm current M71 state and next actions. | task execution |
| `manuscript/task-board.md` | Confirm task IDs and dependencies. | task execution |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` | Locate plotting layout and axis choices. | code edits |
| `manuscript/replication/run_all.py` | Confirm figure regeneration commands. | running outputs |
| `manuscript/tasks/M71-remove-b21-sign-and-pointwise-weighting/outcome.md` | Preserve M71 sign/weighting contract. | code edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The figure problem is layout/display, not the M71 model. | `code-implemented` | Plotting code and rendered output comparison. | pending |
| Active sign restrictions remain \(B_{11}>0\), \(B_{22}>0\), \(B_{12}\le0\). | `user-decision` / `code-implemented` | M71 outcome and figure JSON metadata. | pending |

## Required Work

1. Inspect the M71 figure renderer and identify why panels are tall/narrow.
2. Patch the plotting code to produce readable panels while preserving M71
   sign-screen and weighting behavior.
3. Regenerate quick or normal Figures 1-3 as needed to verify the layout.
4. Update figure notes/metadata only if needed for layout interpretation.
5. Update task board, outcome note, and logs.

## Stop Conditions

- Stop if a visually acceptable figure requires changing the M71 scientific
  object rather than display parameters.
- Stop if regenerated figures fail JSON validation or manuscript checks.
- Stop if the figure still renders with cramped/tall panels after the layout
  patch.

## Acceptance Criteria

- Figure panels are readable and no longer tall skinny towers.
- The plotted \(B_{21}\) coordinate remains sign-free; no active code path
  reintroduces \(B_{21}\ge0\).
- Figures 1-3 are regenerated through the replication wrapper or equivalent
  canonical commands.
- `python scripts/check_manuscript.py` passes.
- `outcome.md` summarizes the fix and whether `QUESTION-INDEX.md` needed an
  update.

## Expected Outputs

- Patched figure renderer.
- Regenerated active Figures 1-3.
- Updated M72 outcome and compact planning/log surfaces.
