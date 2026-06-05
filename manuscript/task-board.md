# Task Board

Statuses: `todo`, `doing`, `blocked`, `done`, `deferred`.

| ID | Status | Priority | Area | Task | Next action |
|---|---|---:|---|---|---|
| M01 | todo | 1 | setup | Initialize the repository metadata and KnowledgeVault link. | Run `python scripts/initialize_manuscript.py ...` and validate the local vault path. |
| M02 | todo | 1 | source | Build the manuscript source packet from KnowledgeVault. | Fill `source-packet.md` with the 5-20 most relevant vault notes, citations, and replications. |
| M03 | todo | 1 | scope | Identify the one central paper idea. | Fill `paper-plan.md` and `paper-map.md` from the source packet. |
| M04 | todo | 1 | citation | Create a self-contained bibliography snapshot. | Copy needed verified BibTeX entries into `../bibliography/references.bib`. |
| M05 | todo | 2 | writing | Build the first draft skeleton. | Add section jobs and placeholders in `draft.md`. |
| M06 | todo | 2 | evidence | Decide the minimal honest evidence package. | Add proof, simulation, empirical, or replication tasks. |
| M07 | todo | 2 | review | Run the first scope review. | Use `review-log.md` after the first paper plan stabilizes. |
| M08 | todo | 2 | transparency | Publish the first traceable manuscript milestone. | Close a transparency milestone, commit it, tag `manuscript-milestones/M0001-*`, and push the tag. |
