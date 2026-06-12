# M71 Task Outcome

Status: not started.

Planned: 2026-06-12.

## Short Answer

This task is planned but not yet executed. It will remove the \(B_{21}\ge0\)
sign restriction from Figures 1-3 and the MCs, and replace true-point
oracle-style fixed weights with candidate-specific pointwise covariance
weighting for the inverted statistic.

## What Changed

- Planning only. No simulation code, figures, MC outputs, draft prose, or
  formal registry objects were changed in this planning pass.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Should the 500-replication MC run now? | No. It is deferred until M71 fixes and checks the intended figure/MC object. | `task.md` |
| Should \(B_{21}\ge0\) remain in the active sign screen? | No. M71 will remove it; the intended screen keeps only \(B_{11}>0\), \(B_{22}>0\), and \(B_{12}\le0\). | `task.md` |
| Should the inverted statistic use a true-point fixed weight? | No. M71 will compute \(\widehat\Omega(B,\nu)\) at each tested candidate and invert the pointwise statistic. | `task.md` |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Full correction contract, required reads, stop conditions, and acceptance criteria. |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: not updated in the planning pass; update it
  when M71 execution answers the implementation questions.

## Checks

- Planning check: `python scripts/check_manuscript.py` passed.

## Open Questions Or Follow-Up

- Execute M71 before M70 or any long M69 500-replication run.
