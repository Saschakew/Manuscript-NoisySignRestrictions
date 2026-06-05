# Manuscript Transparency Data

This directory is the machine-readable companion to the manuscript logs. It is
designed for the separate `Manuscript-Timeline` viewer, which can load an
initialized manuscript repository from GitHub and reconstruct what happened at
each saved milestone.

## Snapshot Rule

Each substantive work block gets a transparency milestone. A milestone covers
one user request, one Codex-led progress checkpoint, or one review/release
checkpoint. Its final repository state is identified by `snapshot_ref`.

Use a Git tag for `snapshot_ref`:

```text
manuscript-milestones/M0001-short-title
```

The tag should point to the commit that contains the closed milestone manifest.
The external viewer uses that ref to browse the repository exactly as it looked
at the end of the milestone, right before the next milestone begins.

## Files

- `timeline.json`: compact ordered index for the external viewer.
- `milestones/*.json`: full manifest for each milestone.
- `user-input.jsonl`: append-only user input events.
- `agent-actions.jsonl`: append-only Codex action events.
- `schema/milestone.schema.json`: expected per-milestone shape.

The Markdown logs in `manuscript/` remain the human-readable record. These JSON
files are the stable exchange format for the external timeline viewer.

## Local Workflow

Begin a milestone before substantive edits:

```powershell
python scripts/transparency_milestone.py begin --title "Scope paper" --request "User asked to scope the manuscript around ..."
```

Close it after edits and checks, before committing:

```powershell
python scripts/transparency_milestone.py close --summary "Built the paper map and source packet." --action "Updated paper-map.md" --check "python scripts/check_manuscript.py: passed"
```

Then commit and tag the closed milestone:

```powershell
git add .
git commit -m "milestone: M0001 scope paper"
git tag manuscript-milestones/M0001-scope-paper
git push
git push origin manuscript-milestones/M0001-scope-paper
```

When GitHub credentials are available, create or update a GitHub issue
milestone with the same title and record its URL or number in the
per-milestone JSON when closing. The GitHub milestone is for coordination; the
Git tag is the snapshot.
