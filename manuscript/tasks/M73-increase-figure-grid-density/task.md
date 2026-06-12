# M73 Increase Figure Grid Density

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M73`

Transparency milestone: `M0069-increase-figure-1-3-grid-density`

GitHub milestone: `#64`

Outcome note: `outcome.md`

## Original User Prompt

"plan and execute a task:first figure 1,2,3 with more grid points."

## Why This Task Exists

Figures 1-3 currently use the corrected M71/M72 first-shock chart and layout,
but the default grid remains relatively coarse for the final-looking figure
panels. This task refreshes the active figures with a denser diagnostic grid
while preserving the existing sign restrictions, profiled coordinates,
candidate-specific pointwise weighting, and pointwise chi-square caveat.

## Do Not Trust Without Rechecking

- Do not change the M71 sign screen: keep `B11>0`, `B22>0`, `B12<=0`, and no
  sign restriction on `B21`.
- Do not change the M71 pointwise-weighting route.
- Do not treat the pointwise chi-square cutoff as a final projected
  confidence-set critical value; M65 remains open for that.
- Do not interpret visual smoothness as new Monte Carlo evidence.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm repository and computational package context. | task execution |
| `manuscript/source-packet.md` | Confirm active evidence route and historical/superseded outputs. | task execution |
| `manuscript/project-dashboard.md` | Confirm current M71/M72 status and next action. | task execution |
| `manuscript/paper-map.md` | Confirm Figure 1-3 roles and caveats. | task execution |
| `manuscript/task-board.md` | Confirm task routing. | task execution |
| `manuscript/formal-object-registry.json` | Confirm affected figure objects. | registry/log edits |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` | Locate grid defaults and diagnostics output. | code edits |
| `manuscript/replication/run_all.py` | Confirm Figure 1-3 wrapper commands. | figure regeneration |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| Figures 1-3 use a denser grid than M71/M72. | `code-implemented` | Generator defaults and diagnostics JSON configuration. | passed: defaults and diagnostics record `41 x 41`, `11 x 11`, and `7 x 7` grids. |
| The denser-grid rebuild preserves M71 restrictions and pointwise weighting. | `code-implemented`, `user-decision` | Generator code, task outcome, diagnostics notes. | passed: sign screen, profiled coordinates, and pointwise weighting text are unchanged. |
| The denser-grid figures are final projected confidence sets. | `conjectural` | M65 projected-inference task. | quarantined |

## Required Work

1. Source work: none beyond active manuscript context; no new external source
   claim is introduced.
2. Derivation work: none; this is a numerical grid-resolution refinement.
3. Code or simulation work: raise the active figure grid defaults and
   regenerate Figures 1-3 plus Markdown/JSON diagnostics.
4. Manuscript update work: update registry/planning/log surfaces only where
   they need to record the denser-grid output status.
5. Outcome note work: answer what changed, record checks, and state whether
   `manuscript/QUESTION-INDEX.md` needs a row.

## Stop Conditions

- Stop if denser grids make the figure rebuild infeasible in the current work
  block.
- Stop if the denser-grid output changes the M71 methodological object rather
  than only the numerical mesh.
- Stop if diagnostics JSON does not record the requested denser configuration.

## Acceptance Criteria

- Figure generator defaults are denser than the M71/M72 defaults.
- `python manuscript/replication/run_all.py --stage figures` regenerates
  Figures 1-3 and their diagnostics successfully.
- Diagnostics JSON files record the denser projection/profile/lambda grid
  settings.
- Task outcome, task board, dashboard, registry/log surfaces, and transparency
  milestone are updated.
- `python scripts/check_manuscript.py` passes after edits.

## Expected Outputs

- `manuscript/figures/fig_sign_dw_unit_variance_noise_grid.png`
- `manuscript/figures/fig_sign_dw_unit_variance_nongaussianity_grid.png`
- `manuscript/figures/fig_sign_dw_unit_variance_sample_size_grid.png`
- `manuscript/simulations/sign_dw_unit_variance_*_grid_figure.md`
- `manuscript/simulations/output/sign_dw_unit_variance_*_grid_figure.json`
- `manuscript/tasks/M73-increase-figure-grid-density/outcome.md`
