# M68 First-Shock Impact Evidence Rebuild

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M68`

Transparency milestone: `M0064-rebuild-first-shock-impact-figures-and-mc`;
GitHub milestone #59

Outcome note: `outcome.md`

## Original User Prompt

"We should always impose that the diag(B) is positive. thats a sign
restrictions. and, instead of reporting b12 and b21 in the figure, lets start
reporting b11 and b21 so its the impact of the first shock. lets impose a sign
restriction on b12. update the figures and mc. create a task, then work on the
task"

## Why This Task Exists

M67 rebuilt Figure 1 as a projection to \((B_{12},B_{21})\) while profiling
\(B_{11}\) and \(B_{22}\). That projection hid part of the intended
first-shock impact story: accepted projection cells could contain the true
off-diagonal coordinate even when the full true \(B_0\) failed the no-noise
standard restriction. The user now selects a better reporting chart for the
evidence package: always impose positive diagonal entries as sign restrictions,
impose a sign restriction on \(B_{12}\), and display first-shock impact
coordinates \((B_{11},B_{21})\). This task updates Figures 1-3 and the Monte
Carlo table under that chart.

## Do Not Trust Without Rechecking

- M67 Figure 1 as the final evidence chart; it projects to \((B_{12},B_{21})\)
  and can visually mask full-\(B_0\) rejection.
- Old M52 Figure 1-3 scripts as active evidence; they use the pre-M64
  diagonal-normalized B-plane.
- Any code path that treats `B11 > 0` and `B22 > 0` as merely grid
  orientation rather than maintained sign restrictions.
- Any chart that reports \((B_{12},B_{21})\) instead of first-shock impact
  coordinates \((B_{11},B_{21})\).
- Any accepted-set or Monte Carlo truth-inclusion calculation that forgets the
  added sign restriction on \(B_{12}\).
- Any direct residual-coordinate \(0\le\nu_i\le\rho\) cap; M66 keeps the
  dimensionless share \(\lambda_i=\nu_i/(BB')_{ii}\in[0,\rho]\).

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm source and package context. | implementation |
| `manuscript/project-dashboard.md` | Confirm current stage. | implementation |
| `manuscript/paper-map.md` | Confirm evidence contract. | implementation |
| `manuscript/task-board.md` | Confirm task routing. | implementation |
| `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/task.md` | Broader unit-variance evidence rebuild contract. | implementation |
| `manuscript/tasks/M66-noise-ratio-bound-grid-algorithm/outcome.md` | Settled \(\lambda\)-bound algorithm. | implementation |
| `manuscript/tasks/M67-unit-variance-figure1-rebuild/outcome.md` | What M68 supersedes in Figure 1. | implementation |
| `manuscript/draft.md` | Affected Sections 2-5. | draft edits |
| `manuscript/formal-object-registry.json` | Affected formal figure/table statuses. | registry edits |
| `manuscript/simulations/sign_dw_unit_variance_noise_grid_figure.py` | Current unit-variance Figure 1 implementation to adapt or replace. | implementation |
| `manuscript/simulations/m45_variance_ratio_evidence.py` | Historical Monte Carlo implementation to replace or supersede. | MC rebuild |
| `manuscript/replication/run_all.py` | Replication wrapper to update. | replication edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The evidence chart should report first-shock impact coordinates \((B_{11},B_{21})\). | `user-decision` | Original user prompt and M68 task. | passed |
| Positive diagonal entries are maintained sign restrictions. | `user-decision` plus `code-implemented` | Code sign screen and diagnostics. | passed |
| \(B_{12}\) has its own sign restriction in all figure and MC accepted sets. | `user-decision` plus `code-implemented` | Code sign screen and diagnostics. | passed |
| Figures 1-3 and Table 1 use the same unit-variance \((B,\lambda)\) GMM route. | `code-implemented` plus `derived` | M66 derivation and regenerated outputs. | passed as diagnostic evidence |

## Required Work

1. Create a shared unit-variance evidence implementation or update the M67
   script so the maintained sign screen is \(B_{11}>0\), \(B_{22}>0\),
   \(B_{12}\) on the chosen sign side, and \(B_{21}\) on the chosen sign side.
2. Change the displayed grid to \((B_{11},B_{21})\), profiling \(B_{12}\),
   \(B_{22}\), and \(\lambda\).
3. Rebuild Figure 1 residual-noise columns under this chart.
4. Rebuild Figure 2 non-Gaussianity columns under this chart.
5. Rebuild Figure 3 sample-size columns under this chart.
6. Rebuild the Monte Carlo table using the same sign screen, chart, and
   \((B,\lambda)\) criterion.
7. Update `manuscript/replication/run_all.py` so `--stage figures`,
   `--stage figure1`, `--stage figure2`, `--stage figure3`, and
   `--stage evidence` call the active M68 implementation.
8. Update the draft, registry, source packet, paper map, dashboard,
   simulations README, figures README, task board, logs, and question index.
9. Complete `outcome.md` with outputs, diagnostics, checks, and remaining
   inference caveats.

## Stop Conditions

- Stop if the first-shock chart cannot be implemented without reintroducing
  `diag(B)=1`.
- Stop if the added \(B_{12}\) sign restriction makes the chosen true \(B_0\)
  violate the maintained sign screen.
- Stop if Figures 1-3 and the Monte Carlo table would silently use different
  sign screens or different moment criteria.
- Stop if the robust row cannot compute \(J_T(B,\nu(B,\lambda))\) with the M66
  \(\lambda\)-bounded moment vector.

## Acceptance Criteria

- Task folder exists and is linked from `manuscript/task-board.md`.
- Figures 1-3 are regenerated under the \((B_{11},B_{21})\) first-shock chart.
- The Monte Carlo table is regenerated under the same sign restrictions and
  moment criterion.
- Replication wrapper stages rebuild the active M68 outputs.
- Draft and registry no longer present the M67 \((B_{12},B_{21})\) chart as
  active evidence.
- `python scripts/check_manuscript.py` passes.

## Expected Outputs

- Active Figure 1, Figure 2, Figure 3 PNGs under `manuscript/figures/`.
- Active simulation diagnostics and machine-readable JSON outputs under
  `manuscript/simulations/`.
- Active Monte Carlo Markdown and JSON output under `manuscript/simulations/`.
- Updated replication wrapper.
- Completed `outcome.md`.
