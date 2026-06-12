# M70 Extended MC Draft Documentation

## Status And Routing

Status: `todo`

Priority: 2

Task-board row: `M70`

Transparency milestone: pending

Outcome note: `outcome.md`

Ready after: M69 extended three-block Monte Carlo outputs.

## Original User Prompt

"Plan an extension of our MC along the three dgp and variation of our three
figures. First plan  the mc setups and coding and so on. Second task will be
interpretation and documentation of the MC in the draft."

## Why This Task Exists

The interpretation should not be written before the extended MC exists. This
task is the second step: read the checked M69 outputs, decide what the Monte
Carlo actually supports, and document it in the draft without overstating
pointwise chi-square diagnostics as final projected confidence-set evidence.

## Do Not Trust Without Rechecking

- Any M69 result before its output note, JSON, and checks exist.
- Any interpretation that treats pointwise chi-square cutoffs as final
  projected inference unless M65 has supplied that route.
- Any result that aggregates across the three blocks without preserving the
  reader distinction between residual-noise, weak-higher-moment, and
  sample-size variation.
- Any prose that says robust DW is always tighter, always valid, or solves
  non-Gaussian residual noise.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `manuscript/tasks/M69-extended-three-block-mc/outcome.md` | Confirm what was run and checked. | any draft edit |
| `manuscript/simulations/m69_extended_three_block_mc.md` | Human-readable MC output. | draft edit |
| `manuscript/simulations/output/m69_extended_three_block_mc.json` | Machine-readable MC output and configuration. | draft edit |
| `manuscript/tasks/M65-unit-variance-gmm-evidence-rebuild/task.md` | Preserve the projected-inference caveat. | interpretation |
| `manuscript/draft.md` | Section 5 and source-trail locations. | draft edit |
| `manuscript/formal-object-registry.json` | Table and evidence-object status. | registry edit |
| `manuscript/paper-map.md` | Keep the reader path aligned with Figures 1-3. | planning edit |
| `manuscript/citation-provenance.md` | Record code-backed evidence claims. | provenance edit |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| The extended MC supports a specific pattern across the three figure blocks. | `code-implemented` | M69 note and JSON. | pending |
| The robust row is valid under the maintained Gaussian residual-noise assumptions. | `derived` plus `code-implemented` | M66/M68 derivations and M69 implementation. | pending |
| Any projected confidence-set statement is final. | `derived` or `raw-source` | M65 projected-inference note. | pending |

## Required Work

1. Read M69 outputs and classify each result as:
   - main diagnostic evidence;
   - limitation evidence;
   - runtime/noise artifact;
   - not stable enough to draft.
2. Build a compact draft-facing summary table or replace the existing Table 1
   only if the M69 output is more informative than the M68 six-scenario table.
3. Interpret the three MC blocks separately:
   - Figure 1 block: how finite-sample truth inclusion changes with residual
     noise.
   - Figure 2 block: how robust and standard sets behave as structural higher
     moments weaken.
   - Figure 3 block: how the comparison changes with sample size.
4. Keep the M65 caveat visible wherever pointwise chi-square cutoffs are used.
5. Update `draft.md` Section 5, including source trails to the M69 note and
   JSON.
6. Update `formal-object-registry.json` for
   `table:monte-carlo-coverage-width` if the active table changes.
7. Update `paper-map.md`, `project-dashboard.md`, and
   `citation-provenance.md` only where the interpretation changes the active
   evidence map.
8. Complete `outcome.md` and update `manuscript/QUESTION-INDEX.md` if the task
   answers a durable question about the MC design or results.

## Stop Conditions

- Stop if M69 has not produced checked outputs.
- Stop if MC output contradicts a figure in a way that has not been audited.
- Stop if the desired interpretation depends on projected critical values that
  M65 has not supplied.
- Stop if the evidence is too unstable to support draft prose; record that
  conclusion in the outcome instead of polishing around it.

## Acceptance Criteria

- Draft interpretation is source-trailed to checked M69 outputs.
- The table/prose distinguishes the three figure blocks.
- Any pointwise chi-square evidence is explicitly described as diagnostic if
  M65 remains unresolved.
- Registry and planning surfaces match the active MC table status.
- `python -m json.tool manuscript\formal-object-registry.json` passes after
  registry edits.
- `python scripts/check_manuscript.py` passes after manuscript edits.
- `outcome.md` states what changed, which questions were answered, checks, and
  whether `QUESTION-INDEX.md` was updated.

## Expected Outputs

- Updated Section 5 in `manuscript/draft.md`
- Updated table/source trails if M69 replaces or extends the active MC table
- Updated registry and planning surfaces where needed
- Completed `outcome.md`
