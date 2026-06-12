# M72 Task Outcome

Status: done.

Completed: 2026-06-12.

## Short Answer

The figures looked weird because M71 widened the unrestricted \(B_{21}\)
candidate range while the renderer still forced equal data-unit aspect. That
made each panel a tall skinny tower with large unused space. M72 fixes only
the figure presentation: the renderer now chooses shared display limits from
the accepted regions plus \(B_0\) and the \(B_{21}=0\) line, and draws square
panel boxes. The M71 sign screen, candidate-specific pointwise weights, masks,
and cutoffs are unchanged.

## What Changed

- Updated `../../simulations/sign_dw_unit_variance_noise_grid_figure.py` so
  plotted limits are data-driven from the evaluated masks rather than the full
  widened candidate range.
- Replaced equal data-unit aspect with square panel boxes and added subtle
  white backing to panel annotations.
- Regenerated:
  - `../../figures/fig_sign_dw_unit_variance_noise_grid.png`
  - `../../figures/fig_sign_dw_unit_variance_nongaussianity_grid.png`
  - `../../figures/fig_sign_dw_unit_variance_sample_size_grid.png`
- Updated the formal registry, simulation README, dashboard, task board,
  question index, user log, and Codex/session logs.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Why did the figures look weird? | The widened M71 \(B_{21}\) candidate span plus `aspect="equal"` compressed each subplot into a narrow tower. | `../../simulations/sign_dw_unit_variance_noise_grid_figure.py` |
| Did the figure fix change the M71 evidence object? | No. It changed only display limits, panel aspect, and annotation readability; the masks, weights, sign screen, and cutoffs are unchanged. | `task.md`; `../M71-remove-b21-sign-and-pointwise-weighting/outcome.md` |
| Are negative \(B_{21}\) values still visibly allowed? | Yes. The shared display limits include the \(B_{21}=0\) line and keep a small negative strip visible while avoiding large empty space. | regenerated figure PNGs |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Task contract |
| `../../simulations/sign_dw_unit_variance_noise_grid_figure.py` | Layout implementation |
| `../../figures/fig_sign_dw_unit_variance_noise_grid.png` | Main fixed figure |
| `../../figures/fig_sign_dw_unit_variance_nongaussianity_grid.png` | Figure 2 fixed layout |
| `../../figures/fig_sign_dw_unit_variance_sample_size_grid.png` | Figure 3 fixed layout |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the figure-layout answer.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python -m py_compile manuscript\simulations\sign_dw_unit_variance_noise_grid_figure.py`: passed.
- `python manuscript\replication\run_all.py --stage figure1 --quick`: passed.
- `python manuscript\replication\run_all.py --stage figure1`: passed.
- `python manuscript\replication\run_all.py --stage figure2`: passed.
- `python manuscript\replication\run_all.py --stage figure3`: passed.
- `python -m json.tool` passed for the three active figure JSON outputs.
- Manual visual inspection passed for the quick Figure 1 render and the
  regenerated canonical Figures 1-3.
- Final manuscript and diff checks are recorded in the milestone closeout.

## Open Questions Or Follow-Up

- M70 remains the next writing task for interpreting the corrected extended MC.
- M65 still owns projected critical values and release hardening.
