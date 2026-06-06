# Replication Package

Purpose: final shareable code, environment notes, and outputs needed to
reproduce manuscript figures and tables.

This folder should become self-contained before the manuscript is shared.
Exploratory code can start elsewhere, but final paper evidence should be
rebuildable from here.

Computational SVAR work should use KnowledgeVault's existing `svar-python`
package whenever the needed routine exists there. Do not reimplement
package-covered SVAR estimation, identification, inference, or simulation
routines inside this manuscript repository. Add only thin wrappers, manuscript
parameters, scripts, and output handling here.

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
python run_all.py
```

Optional staged commands:

```powershell
python run_all.py --stage geometry
python run_all.py --stage population
python run_all.py --stage monte-carlo
```

## Evidence To Build

The active paper needs a three-layer evidence package:

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
