# Standalone Manuscript Repository Template

This template creates one self-contained research manuscript repository linked
back to KnowledgeVault for source notes, paper provenance, citation metadata,
and background research context.

New manuscripts should be created as separate repositories from this template,
not as new folders inside `KnowledgeVault/vault/manuscripts/`.

## Create A Manuscript Repo

1. Create a new GitHub repository from this template.
2. Clone the new repository.
3. Initialize the manuscript metadata:

```powershell
python scripts/initialize_manuscript.py --slug short-paper-slug --title "Working Paper Title" --vault-url "https://github.com/<owner>/KnowledgeVault" --vault-local-path "../KnowledgeVault" --source "vault/syntheses/example-source.md"
```

If `--vault-local-path` is omitted, the initializer tries common sibling paths
such as `../KnowledgeVault`. If Codex cannot validate the vault checkout, the
first manuscript step is to ask the user where the local KnowledgeVault lives.

4. Build `manuscript/source-packet.md`: validate the KnowledgeVault surfaces,
   search `vault/syntheses/`, `vault/papers/`, citations, and replications, and
   record the 5-20 notes that should shape this manuscript. Also validate the
   KnowledgeVault `svar-python` package and record its resolved path/version.
5. Copy only the needed verified BibTeX entries from KnowledgeVault into
   `bibliography/references.bib`.
6. Start work from `manuscript/project-dashboard.md`.
7. Run the local check:

```powershell
python scripts/check_manuscript.py
```

## Transparent Milestone Workflow

Initialized manuscripts are meant to be auditable over time. Each substantive
work block should produce a structured milestone in `manuscript/transparency/`,
a Git commit, and a Git tag that snapshots the repository at the end of that
milestone.

Open a milestone before editing:

```powershell
python scripts/transparency_milestone.py begin --title "Scope paper" --request "User asked to scope the manuscript around ..."
```

Close it after edits and checks:

```powershell
python scripts/transparency_milestone.py close --summary "Built the paper map and source packet." --action "Updated paper-map.md" --check "python scripts/check_manuscript.py: passed"
```

Then commit, tag, and push:

```powershell
git add .
git commit -m "milestone: M0001 scope paper"
git tag manuscript-milestones/M0001-scope-paper
git push
git push origin manuscript-milestones/M0001-scope-paper
```

The tag is the exact repository snapshot used by the external timeline viewer.
GitHub issue milestones should be created with the same title for coordination
when credentials are available, but the Git tag is what preserves the file
state.

## Repository Layout

```text
.
  AGENTS.md                         # Agent operating rules for this repo.
  knowledge-vault-link.json          # Link back to KnowledgeVault sources.
  bibliography/
    references.bib                  # Self-contained BibTeX snapshot.
  manuscript/
    project-dashboard.md            # Entry point and current state.
    source-packet.md                 # Curated KnowledgeVault context.
    paper-map.md                    # Macro argument map.
    task-board.md                   # Actionable tasks.
    draft.md                        # Manuscript prose source of truth.
    formal-object-registry.json     # Assumptions, propositions, figures, proofs.
    manuscript-rules.md             # Local object, citation, and export rules.
    paper-plan.md                   # Scope and contribution plan.
    workplan.md                     # Milestones and review path.
    citation-provenance.md          # Source/contribution boundary.
    literature-search.md            # Search questions and citation gaps.
    derivations/                    # Proof trails and algebra.
    simulations/                    # Exploratory designs.
    replication/                    # Final shareable reproducibility package.
    figures/                        # Manuscript figures.
    tables/                         # Manuscript tables.
    transparency/                   # Website-readable milestone data.
    *-log.md                        # Decisions, sessions, reviews, attribution.
  scripts/
    initialize_manuscript.py         # One-time template initialization.
    check_manuscript.py              # Mechanical project checks.
    transparency_milestone.py        # Begin/close structured milestones.
```

## KnowledgeVault Link

`knowledge-vault-link.json` records the vault repository, local path hint, vault
commit if known, required vault surfaces, and source material paths.
`manuscript/source-packet.md` is the working bridge: Codex uses it to keep the
relevant vault notes, syntheses, citations, and replications small enough for
reliable manuscript writing. The manuscript repository should be able to stand
on its own for sharing: cite sources through `bibliography/references.bib`,
store final replication code under `manuscript/replication/`, and keep durable
decisions in the manuscript logs.

KnowledgeVault remains the research memory. This repository is the paper.

## SVAR Python Package

Initialized manuscripts should build computational work on KnowledgeVault's
existing `svar-python` package. Use it for SVAR estimation, identification,
inference, simulations, and replication code whenever the needed routine exists
there. Avoid manuscript-local reimplementations of package-covered routines;
write thin manuscript-specific wrappers in `manuscript/replication/` instead.

Before final sharing, `manuscript/replication/requirements.txt` should pin an
installable `svar-python` source such as a versioned package, wheel, Git URL, or
copied release artifact. Do not leave final replication code dependent on an
untracked local KnowledgeVault path.

## External Timeline Viewer

This template only produces the machine-readable milestone data. The browsing
interface lives in the separate `Manuscript-Timeline` repository. That viewer
loads `manuscript/transparency/timeline.json` from an initialized manuscript
repository, shows the ordered milestones, displays captured user input and
Codex actions, and browses files at each milestone's `snapshot_ref`.
