# Task Board

Statuses: `todo`, `doing`, `blocked`, `done`, `deferred`.

| ID | Status | Priority | Area | Task | Next action |
|---|---|---:|---|---|---|
| M01 | done | 1 | setup | Initialize the repository metadata and KnowledgeVault link. | Vault path, repository, commit, source note, and package path are recorded. |
| M02 | done | 1 | source | Build the manuscript source packet from KnowledgeVault. | Refreshed for the robust DW comparison paper; keep compact and source-backed. |
| M03 | done | 1 | scope | Identify the one central paper idea. | Active idea: noisy sign-set bias, standard DW false-sharpening, robust DW comparison set. |
| M04 | done | 1 | citation | Create a first self-contained bibliography snapshot. | Add or clean BibTeX only when prose depends on new citation keys. |
| M22 | done | 1 | derivation | Derive a DW-like Gaussian-noise higher-moment route. | Created `manuscript/derivations/dw-noise-robust-moments.md`; it distinguishes invalid no-noise covariance whitening from a normalized sign-plus-higher-cumulant system and writes fourth cumulants as moment equations. |
| M24 | done | 1 | adversarial-review | Audit the robust DW higher-moment derivation. | Conditional pass recorded: the route is a local normalized Gaussian-noise result; global aliases, population grids, and finite-sample behavior remain for M28-M29. |
| M25 | done | 1 | derivation | Prove or weaken the standard DW misspecification result. | Created `manuscript/derivations/standard-dw-j-test-under-noise.md`: rich J-test generic emptying, structural-coordinate rescaling exceptions, finite-moment aliases, and least-rejected pseudo-candidates. |
| M35 | done | 1 | simulation | Run early J-test Monte Carlo triage. | Created `manuscript/simulations/m35_jtest_monte_carlo_triage.py` and first output summary. The screen is cautionary: the provisional statistic is permissive under moderate noise and weak moments, so audit and population-grid checks should precede polished evidence. |
| M26 | doing | 1 | figure | Design the intuitive noisy sign-set figure. | M0017 created the requested 3-by-3 sign/DW/robust-DW B-plane noise grid with finite-sample N-test cutoffs; decide after M28 whether this or an added covariance-ellipse panel should become the final figure. |
| M27 | todo | 1 | method | Formalize the robust DW accepted set and comparison diagnostic. | Define standard DW set, robust DW set, overlap/divergence metric, critical values, and interpretation boundaries. |
| M28 | todo | 1 | simulation | Build population-grid verification for standard DW and robust DW. | Use the M30 audit findings and M0016 candidate figure: verify structural-rescaling exceptions, generic anisotropic-noise pseudo-zeros, robust-DW truth inclusion, finite-stack aliases, weak-moment widening, and whether the visual cutoff is defensible. |
| M29 | todo | 1 | simulation | Build finite-sample Monte Carlo evidence. | Report coverage, width, empty-set frequency, overlap frequency, and divergence warnings across no-noise, moderate-noise, high-noise, weak-moment, and misspecified cases. |
| M30 | done | 1 | adversarial-review | Audit simulation code before trusting outputs. | Created `manuscript/simulations/m30_m35_triage_audit.md`; patched M35 to expose structural-coordinate noise diagnostics and add an anisotropic stress case. Outcome: M35 is valid only as exploratory triage; M28 population grids must come next. |
| M31 | todo | 2 | writing | Draft the section skeleton with source trails. | Use the new six-section structure in `draft.md`; do not polish before M24-M28 stabilize. |
| M32 | todo | 2 | literature | Write the first literature-positioning pass. | Distinguish this paper from Drautzburg-Wright under the no-noise null, sign-set inference, and higher-moment SVAR GMM. |
| M33 | todo | 2 | replication | Build a manuscript-local replication wrapper. | Make final figures rebuildable from `manuscript/replication/` without a local KnowledgeVault dependency. |
| M34 | todo | 3 | review | Run a full adversarial scope and logic review. | Stress-test whether the paper is one short idea, whether the robustness-check recommendation is convincing, and whether limitations are honest. |
| M21 | done | 1 | transparency | Close the current traceable manuscript milestone. | M0010 is closed, committed, tagged at `manuscript-milestones/M0010-derive-dw-noise-robust-moments`, pushed, and its GitHub milestone is closed. |
