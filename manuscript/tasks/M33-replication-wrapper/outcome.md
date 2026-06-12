# M33 Replication Wrapper Outcome

Status: completed.

Completed: 2026-06-12.

## Short Answer

M33 is complete at wrapper strength. The pre-M64 Figure 1, Figure 2, Figure 3,
and M52 evidence note/JSON have a manuscript-local entry point at
`manuscript/replication/run_all.py`, with full canonical rebuild commands and
quick smoke mode routed to ignored files under
`manuscript/replication/output/quick/`. The wrapper does not import from a
local KnowledgeVault checkout.

M64 supersession note: these are now the pre-M64 evidence outputs. M65 must
update the wrapper for the unit-variance GMM route before it is again the
active evidence rebuild entry point.

## What Changed

- Added `manuscript/replication/run_all.py` with `--stage`, `--quick`,
  `--output-dir`, and `--dry-run` controls.
- Added output-path hooks to the pre-M64 Figure 1, Figure 2, Figure 3, and M52
  evidence scripts so smoke checks can avoid canonical outputs.
- Updated `manuscript/replication/README.md` and
  `manuscript/replication/requirements.txt` with current commands and
  dependencies.
- Preserved `Revision-20260610-190805` metadata on current `main`.
- Updated task-board, registry, dashboard, workplan, logs, and question index
  so the next work is findable.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Can the pre-M64 figures and evidence be rebuilt from `manuscript/replication/`? | Yes. Run `python manuscript\replication\run_all.py --stage all` for the historical rebuild, or `--stage evidence --quick` for a smoke check that writes under `manuscript/replication/output/quick/`. M65 must update this for active unit-variance GMM evidence. | `manuscript/replication/README.md`; `manuscript/replication/run_all.py`; `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/task.md` |
| Did the revision branch contain manuscript edits that needed integration before M33? | No. `Revision-20260610-190805` contained revision metadata and a placeholder revision note; those files were carried forward onto current `main`. | `manuscript/revisions/Revision-20260610-190805/revision.md`; `manuscript/transparency/revision.json` |

## Files To Read

| Path | Why |
|---|---|
| `manuscript/tasks/M33-replication-wrapper/task.md` | Task contract |
| `manuscript/replication/README.md` | User-facing replication commands |
| `manuscript/replication/run_all.py` | Wrapper implementation |
| `manuscript/simulations/m52_source_correct_evidence.md` | Canonical pre-M64 evidence note; quick smoke outputs do not replace it |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the replication rebuild answer.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed; no legacy packet status changed.

## Checks

- `python manuscript\replication\run_all.py --dry-run`: passed.
- `python manuscript\replication\run_all.py --stage evidence --quick`: passed.
- `python manuscript\replication\run_all.py --stage figures --quick`: passed.
- `python manuscript\replication\run_all.py --stage figure1 --quick`: passed after the Figure 1 output-directory patch.
- `python -m py_compile manuscript\replication\run_all.py manuscript\simulations\sign_dw_robust_noise_grid_figure.py manuscript\simulations\sign_dw_robust_nongaussianity_grid_figure.py manuscript\simulations\sign_dw_sample_size_robust_grid_figure.py manuscript\simulations\m45_variance_ratio_evidence.py`: passed.
- `python scripts\check_manuscript.py`: passed with the expected open-milestone warning before closeout, then passed cleanly after the milestone was closed.
- `git diff --check`: passed with the repository's usual CRLF normalization warnings.

## Open Questions Or Follow-Up

- The full canonical `python manuscript\replication\run_all.py --stage all`
  command was not run in this M33 closeout because the smoke path already
  verified routing without overwriting canonical outputs.
- A later release-hardening step can copy/package simulation source under
  `manuscript/replication/src/` and pin exact dependency artifacts if the
  paper needs a standalone archive layout.
- Original next recommendation was M63 citation/export cleanup, but M64
  supersedes that routing. Current next task is M65.
