# Scientific Claim Audit

Use this reference whenever manuscript work touches mathematical definitions,
moment conditions, estimators, proofs, simulations, source claims, or claims
about what another paper does.

## Non-Negotiable Rule

Do not promote a plausible memory, prior Codex output, or local implementation
into a settled manuscript claim. A settled claim needs one of:

- direct primary-source support;
- a KnowledgeVault note with source path and citation key;
- an explicit derivation written from stated assumptions;
- an explicit durable user decision.

Code behavior is evidence about the code. It is not evidence that the code
matches the cited paper unless the source-to-code mapping is separately
verified.

## Required Audit Table

For source-sensitive or mathematical edits, keep a compact working table in the
derivation note, review note, or task artifact:

| Claim | Status | Evidence | Confidence | Action |
|---|---|---|---|---|
| Exact claim text or equation | `raw-source`, `vault-source`, `derived`, `code-implemented`, `conjectural`, or `user-decision` | Path, line/page, equation, derivation step, or code path | high/medium/low | promote, revise, quarantine, or ask |

Use `low` confidence whenever the evidence is indirect, source access is
missing, notation is ambiguous, or code is being used as a proxy for theory.

## Source-First Procedure

1. Identify the paper, appendix, replication code, or vault note needed for the
   claim.
2. Read the exact relevant passage or formula before drafting the claim.
3. Extract the object in the source's own notation first.
4. Translate into manuscript notation as a separate step.
5. Record any mismatch between the source object and the manuscript object.
6. If the source is unavailable or ambiguous, mark the claim `conjectural` and
   do not settle it in prose.

## Derivation-First Procedure

For original claims, write the derivation before drafting polished prose:

1. State the assumptions and normalization being used.
2. Define the random variables and independence restrictions.
3. Expand the target object step by step.
4. Mark where zero terms vanish and why.
5. Separate raw moments, centered moments, cumulants, and GMM moment functions.
6. Check special cases and normalization changes explicitly.
7. Record which final equations are safe to promote and which remain
   unresolved.

## Prose Gate

Before editing `manuscript/draft.md`, answer these questions:

- Is this claim from the source, from a derivation, from code behavior, or from
  a user decision?
- If from a source, have I read the raw source or a vault note with enough
  provenance?
- If from code, have I separately verified that the code matches the source?
- If from a derivation, is the algebra written down with assumptions and
  normalization?
- If uncertain, have I left the uncertainty visible rather than smoothing it
  into confident prose?

## Stop Conditions

Stop and ask, or create a follow-up task instead of settling the claim, when:

- the exact source object cannot be found;
- a code implementation and cited source disagree;
- the normalization changes the object being compared;
- the derivation depends on an unstated independence, variance, or centering
  condition;
- the user has flagged the topic as previously mishandled.

## Correcting Prior Work

When a previous task is found unreliable:

1. Mark the task as partial, deferred, or superseded in the task board.
2. Add a warning to the derivation or review artifact that should not be
   trusted.
3. Quarantine draft equations or claims with a TODO note until rederived.
4. Update the decision log so old conclusions are not treated as active
   decisions.
5. Create a new task that starts from the user's original question and the raw
   source, not from the flawed output.
