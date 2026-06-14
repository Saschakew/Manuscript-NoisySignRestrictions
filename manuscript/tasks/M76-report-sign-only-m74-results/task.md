# M76 Report Sign-Only M74 Results

## Status And Routing

Status: `done`

Priority: 1

Task-board row: `M76`

Transparency milestone: `M0071-report-sign-only-m74-results`

Outcome note: `outcome.md`

## Original User Prompt

"then plan and implement a short task to also report the sign results. i also find the names S and R confusing in the table 2. can we call the approahces Sign for sign restrictions only, DW, and nrDW for noise robust DW?"

## Why This Task Exists

M75 reported the M74 sample-size Monte Carlo mainly as a DW-versus-nrDW table.
The same run also stores the sign-only accepted projection shares, and the
truth inclusion rate can be recovered from the stored no-noise second-moment
truth statistic because the true sign restrictions hold. Reporting Sign, DW,
and nrDW side by side makes the comparison clearer and removes the confusing
`S` and `R` abbreviations in Table 2.

## Do Not Trust Without Rechecking

- Do not infer sign-only truth inclusion from the manuscript prose alone.
- Do not treat `S` as Sign; in M75 it meant standard DW. Rename explicitly.
- Do not rerun the M74 Monte Carlo for this task; use the completed JSON output.

## Required Reads

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Confirm manuscript/vault linkage. | task execution |
| `manuscript/source-packet.md` | Confirm active evidence status. | draft edits |
| `manuscript/project-dashboard.md` | Confirm current stage. | task execution |
| `manuscript/paper-map.md` | Confirm section role. | draft edits |
| `manuscript/task-board.md` | Confirm task routing. | task execution |
| `manuscript/draft.md#55-detailed-sample-size-monte-carlo` | Locate affected prose and table. | draft edits |
| `manuscript/formal-object-registry.json` | Locate affected table object. | registry edits |
| `manuscript/simulations/output/m74_sample_size_mc_500_grid27.json` | Verify sign, DW, and nrDW values. | evidence claims |

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| Table 2 should use the names Sign, DW, and nrDW. | `user-decision` | User prompt. | satisfied |
| Sign-only set sizes are available from M74. | `code-implemented` | `summaries[*].size.sign` in the M74 JSON. | satisfied |
| Sign-only truth inclusion can be reported. | `code-implemented`, `derived` | `records[*].metrics.standard_dw.truth_second_j <= chi2_3(0.90)` and true signs hold. | satisfied |
| The M74 warning event remains DW misses truth while nrDW contains it. | `code-implemented`, `user-decision` | M75 decision and `summaries[*].warning`. | satisfied |

## Required Work

1. Source work: verify M74 JSON fields for sign size, sign emptiness, DW truth,
   nrDW truth, and warning.
2. Derivation work: state why sign truth follows from the stored second-moment
   truth statistic and the true sign screen.
3. Code or simulation work: no rerun; compute the sign truth rates from the
   existing output.
4. Manuscript update work: revise Table 2 and local explanation to use Sign,
   DW, and nrDW.
5. Outcome note work: answer the naming/sign-reporting question and decide
   whether `manuscript/QUESTION-INDEX.md` needs a row.

## Stop Conditions

- Stop if the M74 JSON does not contain the needed sign-size or truth-statistic
  fields.
- Stop if sign-only truth cannot be derived from stored diagnostics without a
  rerun.
- Stop if the draft table and simulation note disagree.

## Acceptance Criteria

- Table 2 reports Sign, DW, and nrDW truth inclusion and set size.
- Table 2 reports Sign, DW, and nrDW empty-set rates.
- The local prose explains what the three approach names mean.
- `S` and `R` table labels are removed from the M74/M75 table discussion.
- The simulation note and formal registry match the revised table.
- `outcome.md` summarizes what changed, questions answered, evidence paths,
  checks, and open follow-up.
- `QUESTION-INDEX.md` is updated because the user asked a searchable
  interpretation question.
- `python scripts/check_manuscript.py` passes after edits.

## Expected Outputs

- Revised `manuscript/draft.md` Table 2.
- Revised `manuscript/simulations/m74_sample_size_mc_500_grid27.md`.
- Updated registry, planning, logs, and outcome note.
