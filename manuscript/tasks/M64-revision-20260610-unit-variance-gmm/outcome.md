# M64 Task Outcome

Status: done.

Completed: 2026-06-12.

## Short Answer

The real `Revision-20260610-190805` was recovered and used. The draft now
switches to the unit-variance normalization \(E[\varepsilon_t\varepsilon_t']=I\),
removes the old `diag(B)=1` Section 4 route, and sketches a standard GMM
criterion over \((B,\nu)\). The old M52 figures and table are now historical
until M65 rebuilds them under the new estimator.

## What Changed

- `manuscript/revisions/Revision-20260610-190805/revision.md`: restored the live general revision comments.
- `manuscript/transparency/revision.json`: restored submitted revision metadata and issue link.
- `manuscript/draft.md`: implemented the unit-variance and standard-GMM revision pass across Sections 2-4 and marked Section 5 evidence as a rebuild target.
- `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/`: added the next task contract.
- Planning, registry, logs, and question index: updated to route work to M65.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Was the revision branch substantive? | Yes. The live remote branch had real `revision.md` comments, `draft.md` edits, and inline comments; the local placeholder was stale. | `manuscript/revisions/Revision-20260610-190805/revision.md` |
| Should the manuscript use `diag(B)=1`? | No. M64 accepts the revision decision to use \(E[\varepsilon_t\varepsilon_t']=I\) and not `diag(B)=1`. | `manuscript/draft.md`, Sections 2 and 4 |
| Can the fourth-order covariance-product terms be made standard GMM? | Yes as a draft route: treat residual-noise variances \(\nu\) as nuisance parameters and use \(\omega_{ij}(B,\nu)\) inside \(G_H(B,\nu)\). | `manuscript/draft.md`, Section 4 |
| What happens to the old figures and table? | They are historical diagnostics until the unit-variance GMM implementation is rebuilt. | `manuscript/draft.md`, Section 5; M65 task |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Full repair contract and extracted revision agenda. |
| `manuscript/draft.md` | First-pass revised Sections 2-4. |
| `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/task.md` | Next required scientific task. |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated for the normalization and standard-GMM questions.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python scripts/check_manuscript.py`: passed before close, with only the expected open-milestone warning.
- `git diff --check`: passed after removing two trailing spaces; remaining output was line-ending normalization notices.
- `python -m json.tool manuscript/formal-object-registry.json`: passed.
- `python -m json.tool manuscript/transparency/revision.json`: passed.

## Open Questions Or Follow-Up

- M65 must rebuild the estimator implementation, figures, Monte Carlo evidence, and registry details under the unit-variance GMM route.
- The projected critical value for reporting only \(B\) after profiling \(\nu\) needs a compact inference note before final evidence claims.
