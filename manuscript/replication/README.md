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

## Commands

Planned final command:

```powershell
python run_all.py
```

Initial source assets to inspect, but not yet trust as final evidence:

```powershell
python replications/bonhomme-robin-noise-robust-svar/br_noise_robust_svar.py --figures --test
python replications/svar-noise-recursive-sign-visualization/noisy_svar_visuals.py --figures --test
```

Those commands currently live in KnowledgeVault and should become
manuscript-local wrappers or copied release scripts before this repository is
shared.

## Bonhomme-Robin Verification Commands To Build

The corrected source packet requires a three-layer verification package before
the BR-style results are used in the manuscript:

```powershell
python run_all.py --stage symbolic
python run_all.py --stage population
python run_all.py --stage monte-carlo
```

Planned checks:

- symbolic or exact numerical checks for the bivariate cumulant equations;
- population-grid checks showing the criterion is zero at truth, separates
  false candidates under the rank condition, and becomes weak at rank failure;
- finite-sample Monte Carlo checks with repeated samples or bootstrap critical
  values;
- adversarial DGPs: weak/zero fourth cumulants, Gaussian structural shocks,
  high diagonal noise, non-diagonal noise, mis-normalized shocks, negative
  implied variance regions, and noise restrictions that make pure moments
  misleading;
- a code-review checklist that verifies seeds, normalization, cumulant
  estimators, objective scaling, grids, and interpretation before figures move
  into `draft.md`.

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
