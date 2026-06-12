# M66 Task Outcome

Status: done.

Completed: 2026-06-12.

## Short Answer

Use \(\lambda_i=\nu_i/(BB')_{ii}\) as the dimensionless nuisance share. The
direct bound \(0\le\nu_i\le\rho\) is not automatic from
\(E[\varepsilon_i^2]=1\), because \(\nu_i\) is residual-coordinate noise
variance while \((BB')_{ii}\) is the structural-signal variance in that
coordinate. Section 4 now writes the projected set as a search over
\(\lambda\in[0,\rho]^2\); M65 must rebuild Figures 1-3 with that projected
\((B,\lambda)\) GMM algorithm.

## What Changed

- `manuscript/derivations/m66-noise-ratio-bound-grid-algorithm.md`: added the
  coordinate-scale derivation and computational algorithm.
- `manuscript/draft.md`: rewrote Section 4 to use
  \(\lambda_i=\nu_i/(BB')_{ii}\), put the nuisance bound inside
  \(\mathcal R_T(c;\rho)\), and marked Figures 1-3 historical until M65.
- Historical Figure 1-3 scripts: updated docstrings to say they are pre-M64
  B-plane implementations, not the active M66 algorithm.
- Planning, registry, and logs: updated to unblock M65 with the M66 algorithm.

## Questions Answered

| Question | Short answer | Where to read more |
|---|---|---|
| Can Section 4 replace \(0\le\nu_i\le\rho(BB')_{ii}\) with \(0\le\nu_i\le\rho\)? | Not for \(\nu_i\) as observed-coordinate residual-noise variance. The clean direct bound is on \(\lambda_i=\nu_i/(BB')_{ii}\): \(0\le\lambda_i\le\rho\). | `manuscript/derivations/m66-noise-ratio-bound-grid-algorithm.md`; `manuscript/draft.md`, Section 4 |
| Can the nuisance bound be written like \(R(B)\ge0\) inside \(\mathcal R_T(c;\rho)\)? | Yes. Section 4 now treats \(R(B)\ge0\) and \(\lambda\in[0,\rho]^2\) as maintained restrictions and reports the projection onto \(B\). | `manuscript/draft.md`, Section 4 |
| Is the practical inversion a grid over \(B\) and nuisance variances followed by a \(J_T(B,\nu)\le c\) check? | Yes for fixed \(\rho\), but grid over \(\lambda\) or \(\nu(B,\lambda)\), not over \(\rho\) as a nuisance. Repeat over several \(\rho\)'s only for sensitivity figures. | `manuscript/derivations/m66-noise-ratio-bound-grid-algorithm.md` |
| Did M66 rebuild Figures 1-3? | No. It triggered the stop condition: the current scripts are old diagonal-normalized B-plane scripts. They are marked historical, and M65 must rebuild the figures with a new unit-variance \((B,\lambda)\) implementation. | `manuscript/draft.md`, Section 5; historical script docstrings |

## Files To Read

| Path | Why |
|---|---|
| `task.md` | Task contract and stop conditions. |
| `manuscript/derivations/m66-noise-ratio-bound-grid-algorithm.md` | Short derivation and algorithm. |
| `manuscript/draft.md` | Current Section 4 and figure-caption language. |
| `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/task.md` | Evidence rebuild that M66 gates. |

## Index Updates

- `manuscript/QUESTION-INDEX.md`: updated with the M66 answer.
- `manuscript/tasks/LEGACY-STATUS.md`: not needed.

## Checks

- `python -m json.tool manuscript/formal-object-registry.json`: passed.
- `python -m py_compile manuscript/simulations/sign_dw_robust_noise_grid_figure.py manuscript/simulations/sign_dw_robust_nongaussianity_grid_figure.py manuscript/simulations/sign_dw_sample_size_robust_grid_figure.py`: passed.
- `python scripts/check_manuscript.py`: passed before closure with the expected
  open-milestone warning and passed cleanly after closure.
- `git diff --check`: passed with line-ending warnings only.

## Open Questions Or Follow-Up

- Execute M65 next: rebuild the unit-variance GMM figures, Monte Carlo table,
  and replication wrapper using the M66 \(\lambda\)-bounded projected set.
