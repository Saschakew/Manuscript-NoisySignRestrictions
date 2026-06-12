# Replication Package

Purpose: final shareable code, environment notes, and outputs needed to
reproduce manuscript figures and tables.

This folder should become self-contained before the manuscript is shared.
Exploratory code can start elsewhere, but final paper evidence should be
rebuildable from here. Before building a polished evidence package, run a small
Monte Carlo triage after the analytical J-test inversion result; the point is
to decide whether the comparison behaves well enough to justify deeper work.

Computational SVAR work should use KnowledgeVault's existing `svar-python`
package whenever the needed routine exists there. Do not reimplement
package-covered SVAR estimation, identification, inference, or simulation
routines inside this manuscript repository. Add only thin wrappers, manuscript
parameters, scripts, and output handling here.

## Current M71 Wrapper

M33 added a manuscript-local wrapper. M71 updates it for the active
unit-variance first-shock evidence package with the corrected sign screen and
candidate-specific pointwise weighting:

```powershell
python manuscript\replication\run_all.py --dry-run
python manuscript\replication\run_all.py --stage all
```

The full command rebuilds:

- Figure 1:
  `manuscript/figures/fig_sign_dw_unit_variance_noise_grid.png`
- Figure 2:
  `manuscript/figures/fig_sign_dw_unit_variance_nongaussianity_grid.png`
- Figure 3:
  `manuscript/figures/fig_sign_dw_unit_variance_sample_size_grid.png`
- M71 corrected Table 1 note and JSON:
  `manuscript/simulations/m68_first_shock_evidence.md` and
  `manuscript/simulations/output/m68_first_shock_evidence.json`
- M71 corrected extended MC note and JSON:
  `manuscript/simulations/m69_extended_three_block_mc.md` and
  `manuscript/simulations/output/m69_extended_three_block_mc.json`

The active stages display first-shock coordinates `(B11,B21)`, profile `B12`,
`B22`, and `lambda`, impose `B11>0`, `B22>0`, and `B12<=0`, use the M66 route
`nu_i=lambda_i(BB')_ii`, and compute candidate-specific pointwise covariance
weights for the displayed quadratic criteria.

For a quick operational smoke check that does not overwrite canonical evidence
outputs, run:

```powershell
python manuscript\replication\run_all.py --stage evidence --quick
```

Quick outputs are written under `manuscript/replication/output/quick/` and are
not manuscript evidence. Use them only to verify that the wrapper, imports,
and small grids work.

Optional staged commands:

```powershell
python manuscript\replication\run_all.py --stage figure1
python manuscript\replication\run_all.py --stage figures
python manuscript\replication\run_all.py --stage evidence
python manuscript\replication\run_all.py --stage extended-mc
```

M69 added the explicit `extended-mc` stage; M71 corrects its sign screen and
weighting. It does not replace the existing `evidence` stage. The extended MC
mirrors the three active figure blocks, reports true-\(B_0\) inclusion
counts/rates, and reports mean and median accepted projection shares as
inverted-set size measures. M70 owns draft interpretation after the corrected
M71 outputs are checked. The long 500-replication run remains deferred.

The current wrapper calls scripts under `manuscript/simulations/`; it does not
import from a local KnowledgeVault checkout. A later release-hardening step can
copy or package the script source directly under `manuscript/replication/src/`
if the paper needs a standalone archive layout.

## Suggested Layout

```text
replication/
  README.md
  requirements.txt
  run_all.py
  src/
  output/
```

## Planned Final Command

```powershell
python manuscript\replication\run_all.py --stage all
```

Optional staged commands:

```powershell
python manuscript\replication\run_all.py --stage figure1
python manuscript\replication\run_all.py --stage figures
python manuscript\replication\run_all.py --stage evidence
```

## Evidence To Build

The active paper first needs a quick evidence gate, then a three-layer evidence
package if the gate is informative:

0. Early MC triage: a small simultaneous-SVAR Monte Carlo comparing
   standard-DW and robust-DW J-test inversion behavior under no noise,
   moderate noise, and weak higher moments.
1. Geometry: a bivariate figure showing how additive residual noise changes
   the covariance ellipse, shifts sign boundaries, and biases the standard
   sign-restricted set.
2. Population grids: deterministic checks comparing the standard sign set,
   standard DW refined set, and robust DW higher-moment set under no-noise and
   noisy DGPs.
3. Monte Carlo: finite-sample repeated-sample or bootstrap evidence showing
   coverage, width, empty-set frequency, and standard-DW versus robust-DW
   overlap or divergence.

Initial KnowledgeVault asset to inspect, but not yet trust as final evidence:

```powershell
python replications/svar-noise-recursive-sign-visualization/noisy_svar_visuals.py --figures --test
```

That command currently lives in KnowledgeVault and should become a
manuscript-local wrapper or copied release script before this repository is
shared.

## Planned Checks

- verify the noisy sign-set geometry against analytic covariance formulas;
- verify standard DW population moments at truth under no noise and under
  residual noise;
- verify robust DW higher-cumulant moments at truth under the maintained
  robust-noise condition;
- verify that the robust DW set widens or remains honest under weak higher
  moments;
- stress DGPs with high noise, near-Gaussian structural shocks, non-diagonal
  noise, non-Gaussian residual noise if the robust route assumes Gaussian
  noise, near-boundary signs, and small macro samples;
- audit seeds, normalization, cumulant estimators, objective scaling, grids,
  critical values, and interpretation before figures move into `draft.md`.

## `svar-python` Dependency

- Package source: `C:\Users\smsakewe\Documents\GitHub\KnowledgeVault\svar-toolkit`
- Import name: `svar_toolkit`
- Version, wheel, Git URL, or commit: `knowledge-vault-svar-toolkit
  0.1.0.dev0` at KnowledgeVault commit
  `83a30daf4794aef2eb85ae99fe52574114dba063`
- Verification command: final package validation should run
  `python -m unittest discover -s svar-toolkit/tests -v` or an installable
  wheel check before release.
- Relevant APIs used: sign-restriction draws and filters, structural-output
  helpers, non-Gaussian cross-moment diagnostics, GMM utilities, plotting, and
  bootstrap utilities where useful.

Final shareable code must not import from the local KnowledgeVault checkout.
Before release, pin one of:

- an installable wheel copied into this repository or an artifact store;
- a Git URL and commit;
- a package release version if available.

## Reproducibility Rules

- Every manuscript figure/table should identify its source command, seed, and
  output file when applicable.
- Pin an installable `svar-python` dependency in `requirements.txt` before
  final sharing.
- Do not depend on KnowledgeVault-relative paths for final shared runs.
- Record non-public data requirements or external downloads clearly.
