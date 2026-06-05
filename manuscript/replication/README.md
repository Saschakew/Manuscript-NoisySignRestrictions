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

TODO: Add commands that rebuild every manuscript figure and table.

## `svar-python` Dependency

- Package source: TODO
- Import name: `svar_toolkit`
- Version, wheel, Git URL, or commit: TODO
- Verification command: TODO
- Relevant APIs used: TODO

## Reproducibility Rules

- Every manuscript figure/table should identify its source command, seed, and
  output file when applicable.
- Pin an installable `svar-python` dependency in `requirements.txt` before
  final sharing.
- Do not depend on KnowledgeVault-relative paths for final shared runs.
- Record non-public data requirements or external downloads clearly.
