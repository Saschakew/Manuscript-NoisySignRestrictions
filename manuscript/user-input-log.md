# User Input Log

Use this file for substantive user ideas, constraints, corrections, approvals,
and decisions that should remain visible outside the chat transcript.

For website-readable provenance, also capture each substantive request in
`transparency/user-input.jsonl` through `scripts/transparency_milestone.py`.

## Entries

| ID | Date | Source type | Quote or close paraphrase | Interpretation | Downstream decisions/actions |
|---|---|---|---|---|---|
| U0010 | 2026-06-06 | direct user instruction | Switch to manuscript editing mode and create a derivation file for a Drautzburg-Wright-like approach robust to noise: show higher moments/cumulants can be written as GMM-style moment equations, second moments are not robust, and distinguish the incorrect no-noise sign-plus-higher-moment approach from a noise-robust higher-moment approach that gives up second-moment efficiency. | User wants the DW route evaluated as a serious candidate paper structure, not only discussed in chat. The route should be explicit about robustness, moment implementation, and efficiency loss. | Created `manuscript/derivations/dw-noise-robust-moments.md`; registered new formal objects and added audit tasks before changing the main paper structure. |
| U0005 | 2026-06-05 | direct user correction | The earlier Bonhomme-Robin summary was mistaken; the updated KnowledgeVault notes should be analyzed carefully, the plan should be revised, and the manuscript should include detailed analytic derivation, simulation verification, and adversarial review tasks before trusting the Bonhomme-Robin-style results. | The constructive BR part is not yet an accepted result. It needs a derive-then-simulate verification gate and repeated adversarial checks. | Updated source packet, paper plan, paper map, formal registry, task board, workplan, replication plan, review plan, and logs. |
| U0003 | 2026-06-05 | direct user instruction | Initialize a new manuscript from the KnowledgeVault proposal `vault/syntheses/Research proposal - noise-robust sign-restricted SVARs.md`, understand it carefully, and prepare a well-revised writing plan and next tasks. | User wants a durable manuscript setup and a thought-through plan, not a generic outline. | Validated KnowledgeVault, initialized metadata, built source packet, revised paper structure, and created next-task plan. |
| U0001 | 2026-06-05 | direct user instruction | Adjust the manuscript writing rules so propositions, definitions, and related formal objects are completely italicized, without visible end-proposition text; proofs should start with `Proof:` and end with a square. | Formal statement boundaries should be visually obvious through full-block italics, while proof endings should use a standard square marker. | Updated `manuscript-rules.md`; record as a durable typography and proof-formatting rule. |
