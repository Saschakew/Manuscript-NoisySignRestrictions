# Manuscript Repository Agent Guide

This repository is one standalone research manuscript. It is linked to
KnowledgeVault for source material, but it should remain shareable without being
viewed inside the vault.

## Start Here

Before manuscript work, read:

1. `knowledge-vault-link.json`
2. `manuscript/source-packet.md`
3. `manuscript/project-dashboard.md`
4. `manuscript/paper-map.md`
5. `manuscript/task-board.md`

Read `manuscript/draft.md` before drafting or revising prose. Read
`manuscript/formal-object-registry.json` before changing assumptions,
definitions, propositions, proofs, equations, figures, tables, simulations, or
dependencies.

## Workflows

### discuss-with-me

Use this workflow when the user asks to `discuss-with-me`, or otherwise clearly
asks for a discussion-only content conversation.

- Goal: think through manuscript content with the user without changing the
  manuscript.
- Do not edit files, open transparency milestones, update logs, create GitHub
  milestones, commit, tag, or push.
- Do not treat the discussion itself as a durable decision or work block.
- It is fine to ask questions, test ideas, outline possible arguments, and
  explain tradeoffs conversationally.
- Read repository files only when needed for context, and do not write back any
  notes from the discussion.
- If the user asks to turn the discussion into manuscript edits, leave this
  workflow and follow the normal manuscript, logging, milestone, and check
  rules before editing.

## Relationship To KnowledgeVault

- Treat KnowledgeVault as the source memory for absorbed papers, syntheses,
  replications, and citation metadata.
- Treat this repository as the manuscript source of truth.
- If `knowledge-vault-link.json` is still in template mode, or if the local
  KnowledgeVault path is missing or invalid, ask the user for the local vault
  checkout before doing substantive manuscript work.
- Validate the local vault checkout by checking the required surfaces listed in
  `knowledge-vault-link.json`, especially `vault/papers/`,
  `vault/syntheses/`, `vault/citations/references.bib`, and replication
  registry files.
- Before drafting, build a compact manuscript-specific source packet in
  `manuscript/source-packet.md`: search the vault, identify the 5-20 most
  relevant notes, cite their vault paths, and record citation or replication
  follow-up.
- Do not create new manuscript project folders inside KnowledgeVault.
- Do not require Obsidian wikilinks for this manuscript. Use ordinary Markdown
  links or explicit vault paths in working notes.
- Copy needed BibTeX entries into `bibliography/references.bib`; do not make a
  shareable manuscript depend on a relative path into KnowledgeVault.
- Record source paths, citation keys, and verification status in
  `manuscript/citation-provenance.md`.

## Computational Package

- Treat KnowledgeVault's `svar-python` package as the default computational
  foundation for SVAR estimation, identification, inference, simulations, and
  replication code.
- Validate the package during vault orientation using the
  `computational_package.path_candidates` entries in
  `knowledge-vault-link.json`. Record the resolved path, version, commit, or
  validation status there and in `manuscript/source-packet.md`.
- Do not reimplement SVAR routines that exist in `svar-python` unless the user
  explicitly asks for a methodological comparison or a from-scratch derivation.
  Prefer thin manuscript-specific wrappers under `manuscript/replication/`.
- Final shareable replication code may not depend on an untracked local vault
  path. Pin an installable `svar-python` version, wheel, Git URL, or copied
  release artifact in `manuscript/replication/requirements.txt` and document
  the provenance in `manuscript/replication/README.md`.

## Writing Rules

- Keep one manuscript focused on one research idea.
- Prefer a short, easy-to-understand paper unless the user asks otherwise.
- Write the paper plan before drafting polished prose.
- Maintain two zoom levels:
  - `manuscript/paper-map.md` for the macro argument and reader path.
  - `manuscript/formal-object-registry.json` for assumptions, propositions,
    proofs, equations, figures, tables, and dependencies.
- Treat `manuscript/draft.md` as the source of manuscript prose.
- Use `manuscript/manuscript-rules.md` for numbering, labels, object boundaries,
  citation style, hidden comments, and export discipline.
- Keep evidence honest. Show favorable cases and limitations when simulations
  or empirical evidence are part of the paper.

## Attribution And Logs

- Record durable user ideas and decisions in `manuscript/user-input-log.md`.
- Record durable research, scope, notation, evidence, and workflow decisions in
  `manuscript/decision-log.md`.
- Record meaningful work blocks in `manuscript/session-log.md`.
- Use `manuscript/codex-log.md` for shareable milestone-level Codex
  transparency, not every micro-edit.
- Also maintain the machine-readable transparency stream in
  `manuscript/transparency/`. The Markdown logs are for people; the JSON and
  JSONL files are for the external `Manuscript-Timeline` viewer.

## Transparency And GitHub Milestones

- For every new substantive user request, open a transparency milestone before
  editing files:

```powershell
python scripts/transparency_milestone.py begin --title "Short title" --request "User request or close paraphrase"
```

- Close the milestone after the work block, checks, and log updates:

```powershell
python scripts/transparency_milestone.py close --summary "What changed" --action "Concrete action" --check "python scripts/check_manuscript.py: passed"
```

- Create or update a GitHub issue milestone with the same title whenever
  GitHub access is available. Prefer the Codex GitHub app/connector when it is
  available; otherwise use `gh api "repos/OWNER/REPO/milestones"` to create it
  and `gh api -X PATCH "repos/OWNER/REPO/milestones/NUMBER"` to update or close
  it. Record the GitHub milestone URL or number in the transparency manifest.
- Commit the closed milestone and tag that commit with its `snapshot_ref`, for
  example `manuscript-milestones/M0001-short-title`. Push both the branch and
  tag when GitHub access is available.
- The Git tag is the repository snapshot; the GitHub issue milestone is the
  public coordination object.
- Start a new progress milestone when the manuscript reaches a meaningful new
  state even if the user has not issued a new request: source packet complete,
  paper map stable, first draft complete, evidence package complete, or
  shareable draft ready.
- Purely conversational turns that do not change durable manuscript state do
  not need a milestone unless the user makes a durable decision.

## Checks

Run this after substantive edits:

```powershell
python scripts/check_manuscript.py
```

Validate `manuscript/formal-object-registry.json` after registry edits. Run
replication-specific commands from `manuscript/replication/README.md` when code
or generated outputs change.
