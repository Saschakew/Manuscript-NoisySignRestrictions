# Task Board

Statuses: `todo`, `doing`, `blocked`, `done`, `deferred`.

| ID | Status | Priority | Area | Task | Next action |
|---|---|---:|---|---|---|
| M01 | done | 1 | setup | Initialize the repository metadata and KnowledgeVault link. | Vault path, repository, commit, source note, and package path are recorded. |
| M02 | done | 1 | source | Build the manuscript source packet from KnowledgeVault. | Keep packet compact; add sources only when a draft claim needs them. |
| M03 | done | 1 | scope | Identify the one central paper idea. | Use the revised paper contract in `paper-plan.md` and `paper-map.md`. |
| M04 | done | 1 | citation | Create a first self-contained bibliography snapshot. | Add or clean BibTeX only when prose depends on new citation keys. |
| M05 | todo | 1 | derivation | Derive the corrected bivariate cumulant map from scratch. | Write all second-, third-, and fourth-cumulant equations for `u_t = B(a,b) epsilon_t + eta_t`, including nuisance noise cumulants. |
| M06 | todo | 1 | adversarial-review | Audit the cumulant derivation before using it. | Check indices, cumulant definitions, normalization, missing pure/mixed moments, and whether any moment is incorrectly called clean. |
| M07 | todo | 1 | method | Prove what the BR analogy does and does not justify. | Show why full BR quasi-JADE does not apply directly for `L=K=2`; document the manuscript object as a BR-style profiled inversion. |
| M08 | todo | 1 | adversarial-review | Attack the BR applicability argument. | Try to falsify the claim that the bivariate case needs its own derivation; record any missing rank assumptions or hidden restrictions. |
| M09 | todo | 1 | method | Derive the profiled criteria and local identification result. | Derive `J_4`, `J_stack`, determinant condition, tangent equations, rank condition, and the role of `1-a0 b0 != 0`. |
| M10 | todo | 1 | adversarial-review | Audit the local identification proof. | Check algebra signs/factors, nuisance profiling, boundary cases, weak cumulants, sign/permutation ambiguity, and compactness assumptions. |
| M11 | todo | 1 | diagnostic | Derive the noise diagnostics separately from identification. | Specify mapped variance set, restricted no-noise J test, and which extra noise restrictions make pure moments overidentifying. |
| M12 | todo | 1 | simulation | Build symbolic and population verification tests. | Use analytic cumulants to verify the moment map, population zeros at truth, false-candidate separation, and rank-failure behavior. |
| M13 | todo | 1 | adversarial-review | Review simulation code before trusting outputs. | Check DGP normalization, cumulant estimators, seeds, grids, objective scaling, critical values, and whether code can pass for wrong reasons. |
| M14 | todo | 2 | simulation | Run finite-sample and adversarial Monte Carlo checks. | Include favorable cases, weak/zero fourth cumulants, rank failure, Gaussian structural shocks, high noise, non-diagonal noise, negative implied variances, and mis-normalized shocks. |
| M15 | todo | 2 | adversarial-review | Review result interpretation and story credibility. | Ask whether figures support the claims, whether failures are honestly reported, and whether the diagnostic is overinterpreted as measurement-error proof. |
| M16 | todo | 2 | derivation | Prove the no-noise independence-refinement failure carefully. | Write a bivariate Darmois-Skitovich-style proof sketch and list special alignments where the result does not apply. |
| M17 | todo | 2 | evidence | Build a manuscript-local replication wrapper. | Promote or wrap the two vault replication assets only after the new verification tasks pass. |
| M18 | todo | 2 | writing | Draft the section skeleton with source trails. | Add concise prose placeholders and typed comments in `draft.md`; do not polish before formal statements stabilize. |
| M19 | todo | 2 | literature | Write the first literature-positioning pass. | Distinguish the paper from Drautzburg-Wright, the original Bonhomme-Robin theorem, Keweloh/GMM, and sign-set inference. |
| M20 | todo | 3 | review | Run a full adversarial scope and logic review. | Stress-test whether the paper is still one short idea, whether objects are defined, and whether the story is convincing. |
| M21 | doing | 1 | transparency | Close the current traceable manuscript milestone. | Run checks, close M0005, commit the closed manifest, tag the snapshot, and push if available. |
