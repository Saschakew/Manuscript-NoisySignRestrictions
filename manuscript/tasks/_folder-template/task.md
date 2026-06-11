# Mxx Task Title

## Status And Routing

Status: `todo`

Priority: 1

Task-board row: `Mxx`

Transparency milestone: pending

Outcome note: `outcome.md`

## Original User Prompt

Paste the user's request verbatim or as a close quote. Do not smooth away
uncertainty, emphasis, typos, or methodological concerns when they matter.

## Why This Task Exists

Explain the manuscript problem, prior failure, or decision need that makes this
task necessary.

## Do Not Trust Without Rechecking

- List prior draft passages, derivation notes, code outputs, figures, or
  decisions that are provisional, contaminated, superseded, or unverified.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Resolve KnowledgeVault and package paths. | any source claim |
| `manuscript/project-dashboard.md` | Confirm current stage and next action. | task execution |
| `manuscript/task-board.md` | Confirm status, dependencies, and row wording. | task execution |
| `manuscript/draft.md` | Locate affected prose. | draft edits |
| `manuscript/formal-object-registry.json` | Locate affected formal objects. | registry edits |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| Claim to verify | `raw-source`, `vault-source`, `derived`, `code-implemented`, `conjectural`, or `user-decision` | Source path, equation, derivation, or code path | pending |

## Required Work

1. Source work:
2. Derivation work:
3. Code or simulation work:
4. Manuscript update work:
5. Outcome note work: answer user questions in `outcome.md`.

## Stop Conditions

- Stop if the required source cannot be found.
- Stop if source and code disagree and the difference cannot be resolved.
- Stop if a derivation depends on an unstated assumption.
- Stop if the task produces an answer the user is likely to look for later but
  `outcome.md` does not yet capture it.

## Acceptance Criteria

- Every source-sensitive claim in the output has `raw-source` or
  `vault-source` evidence.
- Every original mathematical claim has a written derivation.
- Code behavior is not treated as theory without a source-to-code mapping.
- Draft, registry, task board, and logs are updated only after the audit
  supports the change.
- `outcome.md` summarizes what was done, questions answered, evidence paths,
  checks, and open follow-up.
- `python scripts/check_manuscript.py` passes after substantive edits.

## Expected Outputs

- List the files or decisions the task should produce.
