# Paper Plan

## Working Title

Noise-Robust Sign-Restricted SVARs

## Main Idea

The paper studies what happens when applied researchers combine sign
restrictions with Drautzburg-Wright-style higher-moment refinements while the
VAR residuals contain additive noise. The standard sign-restricted set rotates
a factor of the noisy covariance, so it targets a pseudo-set. Standard
Drautzburg-Wright refinement then appears to sharpen that pseudo-set, but the
smaller accepted set can be an artifact of misspecification rather than more
efficient structural learning.

The constructive contribution is a robustness check: compute the standard
Drautzburg-Wright set and compute a noise-robust higher-moment set that drops
second-moment restrictions. When the two sets agree, the usual refinement is
less suspicious. When they diverge, residual noise or another covariance-target
misspecification is indicated, and the robust set is the safer object.

## Why It Matters

Sign restrictions are qualitative, but the object being rotated is not. In the
usual no-noise model, the reduced-form covariance equals `B0 B0'`, so a
covariance factor can be rotated into candidate structural impacts. With
additive residual noise,

```text
Sigma_u = B0 B0' + V,
```

so the standard sign-restricted set is built from the wrong covariance object.
This can move sign boundaries, deform accepted regions, and make economically
meaningful columns disappear from the reported set.

Higher moments do not automatically fix the problem. The usual
Drautzburg-Wright procedure refines sign-admissible no-noise candidates by
testing independence of recovered shocks. Under residual noise, those recovered
objects are not the true structural shocks. Asymptotically, the no-noise DW set
may become empty; in finite samples, it can become small and look precise
because the least-misspecified candidates are being selected.

The robust alternative keeps the useful higher-moment idea but removes the
fragile covariance step. It searches over normalized impact matrices, imposes
economic signs directly on those matrices, and uses higher-order cumulants of
candidate transformed residuals written as GMM-style moment equations. The
robust set deliberately gives up second-moment information, so it should often
be wider than the standard DW set. That width is the price of not pretending
that the noisy covariance is structural.

## Proposed Structure

1. Introduction: present the puzzle that sign restrictions can look more
   precise after higher-moment refinement even when residual noise has
   misspecified the no-noise target. State the robustness-check idea.
2. Noisy sign-restricted sets: define the additive-noise SVAR, show that the
   standard sign set rotates a factor of `B0 B0' + V`, and give an intuitive
   visual figure of sign-boundary movement or set deformation.
3. Standard DW under residual noise: explain the no-noise DW refinement, show
   why the recovered shocks are contaminated under noise, and state the
   planned result that the population DW set should generally be empty under
   misspecification, with finite-sample regions shrinking around
   least-rejected pseudo-candidates.
4. Robust DW higher-moment set: define the normalized robust candidate space,
   write the higher-cumulant restrictions as moment equations, and explain why
   second moments are excluded as structural restrictions. State the local
   identification and consistency claims only after audit.
5. Monte Carlo evidence and robustness check: simulate no-noise, moderate
   noise, high noise, weak-moment, and near-Gaussian cases. Show the standard
   sign set, standard DW set, robust DW set, and their overlap/divergence.
6. Conclusion: recommend reporting the robust DW set beside the standard DW
   set as a diagnostic for covariance-target misspecification. Defer empirical
   applications.

## Key Model Or Notation

- Observed residual model:
  `u_t = B0 epsilon_t + eta_t`, `E[epsilon_t epsilon_t'] = I`,
  `E[epsilon_t eta_t'] = 0`, and `E[eta_t eta_t'] = V`.
- Standard sign set:
  `B_*(Q) = P_* Q`, where `P_* P_*' = Sigma_u = B0 B0' + V` and
  `R(P_* Q) >= 0`.
- No-noise economic sign set:
  `P_0 P_0' = B0 B0'`, with `R(P_0 Q) >= 0`.
- Standard DW set:
  sign-admissible covariance-factor rotations whose recovered shocks pass
  no-noise higher-moment independence restrictions.
- Robust DW candidate:
  a normalized impact matrix `B` not required to satisfy `B B' = Sigma_u`.
- Robust DW transformed residual:
  `z_t(B) = B^{-1} u_t`.
- Robust DW moment stack:
  mixed third central moments and fourth cumulants of `z_t(B)`, written as raw
  moment equations with covariance products subtracted.
- Robustness check:
  compare the standard DW accepted set with the robust DW accepted set. Overlap
  supports the usual refinement; divergence warns that the usual refinement is
  reacting to residual noise or covariance-target misspecification.

## Main Results To Prove Or Demonstrate

- Proposition 1, noisy sign pseudo-set: if `V != 0`, the population sign set
  based on `Sigma_u` generally differs from the no-noise economic sign set.
  This result should be explained visually before the algebra.
- Proposition 2, standard DW is misspecified under residual noise: recovered
  shocks from noisy covariance-factor candidates are not the structural shocks,
  so no-noise independence restrictions need not hold at `B0`. The population
  accepted set is expected to be generically empty; finite-sample inversion can
  still return a falsely narrow least-rejected region.
- Proposition 3, robust DW higher moments: under the maintained robust-noise
  conditions, the higher-cumulant moment stack for `z_t(B)` has zero
  population value at the true normalized impact matrix, while no-noise second
  moment restrictions do not.
- Proposition 4, robust set comparison: the robust DW set is expected to be
  weakly less sharp than the standard DW set in favorable finite samples
  because it discards second-moment restrictions; disagreement between the two
  sets is a diagnostic warning, not literal proof of measurement error.
- Simulation result: Monte Carlo evidence should show the visual sign-set
  bias, the standard DW false-sharpening channel, and the robust DW widening
  or disagreement under residual noise.

## Evidence Plan

- Intuitive geometry figure: show how adding diagonal variance changes the
  covariance ellipse, rotates/deforms sign-admissible regions, and biases the
  estimated sign set away from the no-noise economic target.
- Standard DW misspecification figure: plot accepted sets under no noise and
  under increasing noise. The noisy case should show shrinking, emptying, or
  least-rejected pseudo-precision.
- Robust DW comparison figure: overlay standard DW and robust DW accepted sets.
  In no-noise or nearly no-noise cases they should overlap; under noise they
  should diverge, with the robust set wider.
- Monte Carlo table: report coverage of the true normalized `B0`, set width,
  empty-set frequency for standard DW, overlap frequency, and rejection or
  divergence diagnostics.
- Stress cases: weak higher moments, near-Gaussian structural shocks, high
  noise, non-Gaussian noise that violates the robust route if Gaussianity is
  maintained, non-diagonal noise, near-boundary signs, and small macro samples.

## What Is Missing

- A formal proof or clear conjecture boundary for asymptotic emptiness of the
  standard DW set under residual noise.
- An adversarial audit of `derivations/dw-noise-robust-moments.md`, especially
  the cumulant-as-moment equations, local rank, normalization, and exact noise
  conditions.
- A decision on the precise robust noise assumption: Gaussian additive noise is
  clean for transformed cumulants; broader non-Gaussian noise would need a
  different argument.
- A self-contained simulation package that builds the sign-bias, DW-shrinkage,
  and robust-DW comparison figures from this repository.
- A concise literature-positioning paragraph distinguishing the paper from
  Drautzburg-Wright, sign-restriction inference, and higher-moment SVAR GMM.

## Page Budget And Scope Exclusions

Target: short theory-and-simulation paper, about 18-24 manuscript pages before
appendix.

Excluded from the first version:

- A full empirical application.
- A general `K`-variable estimator in the main text.
- Dynamic sign restrictions beyond simple impact-sign illustrations.
- Correlated, serially dependent, common-factor, or stochastic-volatility noise.
- A claim that divergence between DW and robust DW proves literal measurement
  error. It is a robustness warning inside the maintained model.

## Scope Recommendation

Keep the paper as one clean robustness-check story:

1. Noise biases the standard sign-restricted set.
2. Standard DW refinement can falsely sharpen the misspecified set.
3. A robust DW higher-moment set drops second moments and should be wider.
4. Comparing the two sets gives a practical diagnostic.
5. Simulations carry the evidence burden; no application is needed yet.
