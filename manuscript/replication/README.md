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

Initial source assets to wrap:

```powershell
python replications/bonhomme-robin-noise-robust-svar/br_noise_robust_svar.py --figures --test
python replications/svar-noise-recursive-sign-visualization/noisy_svar_visuals.py --figures --test
```

Those commands currently live in KnowledgeVault and should become
manuscript-local wrappers or copied release scripts before this repository is
shared.

## `svar-python` Dependency

- Package source: `C:\Users\smsakewe\Documents\GitHub\KnowledgeVault\svar-toolkit`
- Import name: `svar_toolkit`
- Version, wheel, Git URL, or commit: `knowledge-vault-svar-toolkit
  0.1.0.dev0` at KnowledgeVault commit
  `c213b4c7564657d84c647588c5a21e00ba1b0365`
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
