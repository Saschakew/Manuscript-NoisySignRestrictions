# M49 DW Source And Noisy Moment Audit

Status: `todo`

Priority: 1

Task-board row: `M49`

Created after: M0045, because M48 failed as a source-complete scientific
audit.

## Original User Prompt

> insert a task to work on my comments.
>
> 1) Section 3 claims that in DW "The fourth-order entries are cumulants, so
> for example
>
> \begin{equation} \kappa_{1122}^e(B)
> =E{e_1(B)^2e_2(B)^2} -E{e_1(B)^2}E{e_2(B)^2}
> -2E{e_1(B)e_2(B)}^2 . \end{equation} "
>
> But i am not sure if this is correct. I would argue that DW have fourth order
> moments like "E{e_i(B) e_j(B) e_k(B) e_l(B)}
> - 1_{ if i j k l form two distinct pairs}". i makes a small diferences in
> finite samples. and the moment conditions like dw use it is like a standard
> gmm moment condition, whereas your condition is like a sum of three moment
> conditions. So this needs to be fixed in section 3, but i also want you to
> double check. related to this, how do you compute the dw moment conditions in
> the code (say for figure 1)? Your approach or my approach? I think we should
> use switch from diag(B) normalization to variance(epsilon)=1 normalization to
> bring us closer to DW and to the whole literature. but the we need to re-do
> the figures and mc, correct?
>
> 2) In section 4, the thrid order cumulants look just like usual gmm moment
> conditions. so they are equal to the moment conditions in DW and they are not
> affected by noise at all? The furth order cumulants now look different to the
> dw conditions you write in section 3. please carefully derive what moment
> conditions like E[z1^2 z2], E[z1 z2 z3], E[z1^3 z2],
> E[z1^2 z2^2], E[z1^2 z2 z3], E[z1 z2 z3 z4] would look like atB=B_0. like
> insert z= epsilon + B_0^-1 eta and go on, use independence of epsilon and
> eta, and independent components of epsilon1 epsilon2 and independent
> components eta1 eta2. and also, if we switch to variance(1) normalization,
> plug in variance(epsilon)=1. i need to see the derivation of these moment
> conditions when you plug in everything to be certain we are not making
> misstakes here

## Why This Task Exists

M48 attempted this audit and failed as a scientific hand-off. It inferred too
much from prior code and a partial source reading, did not establish the exact
bivariate Drautzburg-Wright GMM moment menu, did not provide the requested
step-by-step noisy moment derivations, and made a premature normalization and
no-rebuild decision.

M49 must restart from the original user prompt, source material, and explicit
derivations. The goal is not to defend M48. The goal is to find the
source-correct DW comparator, compare it to the code, and decide what the
manuscript must change.

## Do Not Trust Without Rechecking

- The current Section 3 `g_DW(B)` display in `manuscript/draft.md`.
- The M48 conclusion that Figure 1 implements the source-correct bivariate DW
  GMM menu.
- The M48 conclusion that no figure or Monte Carlo rebuild is required.
- The M48 conclusion that the manuscript should stay in the `diag(B)=1` chart.
- Any claim that code behavior proves what DW uses in the paper.
- Any claim that fourth cumulants and DW fourth product GMM moments are
  interchangeable in finite samples.

## Required Reads

Resolve the local KnowledgeVault path from `knowledge-vault-link.json` before
reading vault or raw-source files.

| Path | Purpose | Required before |
|---|---|---|
| `knowledge-vault-link.json` | Resolve KnowledgeVault path and source surfaces. | all source work |
| `manuscript/source-packet.md` | Confirm DW source role and KnowledgeVault context. | source selection |
| `manuscript/draft.md` | Inspect Sections 3 and 4 and the quarantined `g_DW` display. | draft edits |
| `manuscript/formal-object-registry.json` | Inspect affected DW definitions, equations, and open audits. | registry edits |
| `manuscript/derivations/m48-dw-moment-normalization-audit.md` | Read only as a failed/partial historical artifact and warning. | understanding what not to trust |
| `manuscript/derivations/dw-noise-robust-moments.md` | Inspect existing robust cumulant derivation. | Section 4 comparison |
| `manuscript/derivations/standard-dw-j-test-under-noise.md` | Inspect current standard-DW proof object after source moment menu is known. | M47 hand-off decision |
| `manuscript/simulations/sign_dw_robust_noise_grid_figure.py` | Determine what Figure 1 code actually computes. | code-to-source comparison |
| `manuscript/simulations/m45_variance_ratio_evidence.py` | Determine what Monte Carlo evidence would need rebuilding. | rebuild decision |
| `KnowledgeVault/vault/papers/Refining set-identification in VARs through independence.md` | Verify absorbed DW note. | any DW source claim |
| `KnowledgeVault/raw/drautzburg-2023-refining-set-identification/Refining_set-identification_in_VARs_through_independence.md` | Verify raw DW formula or equation. | any exact DW moment claim |

If the raw paper path has moved, search the local KnowledgeVault checkout and
record the resolved path before proceeding.

## Scientific Claim Ledger

| Claim | Required status | Evidence required | Result |
|---|---|---|---|
| DW fourth-order GMM entries are raw standardized product moments with two-pair indicator targets, not fourth cumulants. | `raw-source` or `vault-source` | DW equation/page/path; source notation translated to manuscript notation | pending |
| The exact bivariate DW moment menu includes or excludes `E(e_1^3 e_2)` and `E(e_1 e_2^3)`. | `raw-source` plus translation | DW source and bivariate specialization derivation | pending |
| Figure 1 standard-DW code implements the source-correct bivariate DW menu. | `code-implemented` plus source-to-code mapping | code path plus source comparison | pending |
| Third-order cumulants equal the relevant centered raw third GMM moments and are unaffected by additive independent Gaussian noise at `B=B0`. | `derived` | expansion from `z=epsilon+B0^{-1}eta` | pending |
| Fourth-order robust cumulants differ from DW fourth-product conditions by covariance-product subtractions that matter in finite samples. | `derived` plus source comparison | raw fourth expansions and cumulant formulas | pending |
| Switching from `diag(B)=1` to `Var(epsilon)=1` is required or not required for source alignment. | `derived` plus `user-decision` if adopted | normalization comparison and rebuild list | pending |

## Required Work

1. Source extraction:
   - Read the raw DW source before writing any settled DW claim.
   - Extract the exact GMM moment definition in the source's notation.
   - Translate that object into the bivariate manuscript notation.
   - Identify whether DW uses raw product moments, centered moments,
     standardized moments, cumulants, or a mix.

2. Figure 1 code audit:
   - Locate the moment powers, targets, standardization, weighting, and
     degrees of freedom used by the standard-DW row.
   - Classify each code observation as `code-implemented`.
   - Compare code to the source-derived bivariate menu.
   - Record whether the code is source-correct, a subset, a simplification, or
     wrong.

3. Noisy moment derivations at `B=B0`:
   - Set `z = epsilon + B0^{-1} eta`.
   - State all assumptions before expanding: centering, independence of
     `epsilon` and `eta`, independent components of `epsilon`, independent
     components of `eta`, Gaussian or non-Gaussian status of `eta`, and
     normalization.
   - Derive step by step:
     `E[z1^2 z2]`,
     `E[z1 z2 z3]`,
     `E[z1^3 z2]`,
     `E[z1^2 z2^2]`,
     `E[z1^2 z2 z3]`,
     `E[z1 z2 z3 z4]`.
   - Then plug in `Var(epsilon_i)=1` as a separate case.

4. Section 3 and Section 4 comparison:
   - Decide whether third-order robust cumulants coincide with DW-style raw
     third GMM moment conditions under centering and the maintained assumptions.
   - Decide exactly how fourth-order robust cumulants differ from DW
     fourth-product GMM moments.
   - State finite-sample implications of using one raw fourth-product moment
     versus cumulant subtraction as several covariance-product terms.

5. Normalization and rebuild decision:
   - Compare `diag(B)=1` and `Var(epsilon)=1` as charts/normalizations.
   - Decide whether source alignment requires a switch or only clearer
     standardization language.
   - If a switch or moment-menu change is needed, enumerate affected figures,
     Monte Carlo scripts, captions, tables, registry entries, and draft
     passages.

## Stop Conditions

- Stop if the raw DW source cannot be accessed or the exact moment definition
  cannot be located.
- Stop if source and code disagree and the discrepancy cannot be classified.
- Stop if a derivation requires an assumption not stated in the draft or task
  packet.
- Stop if the normalization decision would require a large evidence rebuild;
  record the rebuild plan before touching figures or Monte Carlo outputs.
- Stop before writing confident prose if any claim remains `conjectural`.

## Acceptance Criteria

- The exact DW source moment definition is quoted or paraphrased with path,
  equation/page, and manuscript-notation translation.
- The bivariate DW moment menu is explicitly listed.
- Figure 1's standard-DW code is classified against the source-derived menu.
- All six requested noisy moments are derived step by step from
  `z=epsilon+B0^{-1}eta`.
- The `Var(epsilon)=1` case is explicitly plugged in.
- Section 3 correction requirements are clear.
- Section 4 cumulant-versus-DW-product differences are clear.
- The `diag(B)=1` versus `Var(epsilon)=1` decision is either made with evidence
  or left as an explicit user-decision gate.
- Any required figure/Monte Carlo rebuilds are enumerated.
- Draft/registry edits happen only after the source and derivation audit.
- `python scripts/check_manuscript.py` passes after substantive edits.

## Expected Outputs

- A new derivation/audit note under `manuscript/derivations/`.
- Updates to `manuscript/draft.md` only if the audit supports them.
- Updates to `manuscript/formal-object-registry.json`,
  `manuscript/citation-provenance.md`, `manuscript/task-board.md`, and logs.
- If needed, a rebuild plan for Figure 1, Figure 2, Figure 3, and M45-style
  Monte Carlo evidence.

## Outcome Log

Pending.
