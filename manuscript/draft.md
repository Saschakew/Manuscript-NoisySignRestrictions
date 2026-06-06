# Noise-Robust Sign-Restricted SVARs

Author: TODO

Date: 2026-06-05

## Abstract

TODO: State the noisy sign-set bias, the false-precision risk in standard
Drautzburg-Wright refinement, the robust higher-moment comparison set, the
Monte Carlo evidence, and the no-application scope in one compact paragraph.

## 1. Introduction

TODO: Motivate why sign restrictions can be qualitatively agnostic but still
depend on a fragile covariance target. Present the paper as a robustness-check
proposal: compute the standard DW set and a robust higher-moment set that drops
second-moment restrictions.

<!-- SOURCE-TRAIL: Use sign-restriction overview sources, Drautzburg-Wright, and the noisy-residual synthesis. -->
<!-- CONTRIBUTION-NOTE: The original contribution is the noise-bias warning plus the standard-DW versus robust-DW comparison. -->

## 2. Noisy Sign Sets

TODO: Define the additive-noise SVAR, the standard sign-restricted covariance
rotation set, and the no-noise economic sign set. State and prove the noisy
pseudo-set result and the column-rescaling obstruction. Include an intuitive
figure that shows how residual noise moves or deforms the sign set.

<!-- SOURCE-TRAIL: Use the proposal note and `Noisy residuals in recursive and sign-restricted SVARs.md`. -->
<!-- TODO-NOTE: Make this section visual and intuitive before the algebra. -->

## 3. Standard DW Under Residual Noise

TODO: Explain the standard no-noise Drautzburg-Wright refinement, why it is
well motivated under its maintained null, and why residual noise contaminates
the recovered-shock object. State the planned misspecification result: the
population refined set should generally be empty under noise, while finite
samples can still return a falsely small least-rejected set.

<!-- SOURCE-TRAIL: Use Drautzburg-Wright, higher-moment SVAR caution sources, and the noisy-residual synthesis. -->
<!-- TODO-NOTE: Be fair: the target is not to criticize DW under its own null, but to show what changes under residual noise. -->
<!-- TODO-NOTE: The asymptotic-empty claim still needs proof or careful weakening. -->

## 4. Robust DW Higher-Moment Set

TODO: Define the robust normalized candidate space, candidate transformed
residuals `z_t(B)=B^{-1}u_t`, and the higher-moment stack. Explain that the
fourth-order restrictions are cumulants written as moment equations, so second
moments are used only as nuisance covariance products and not as structural
restrictions.

<!-- SOURCE-TRAIL: Use `derivations/dw-noise-robust-moments.md`, Drautzburg-Wright, and higher-moment GMM sources. -->
<!-- TODO-NOTE: State the exact robust noise assumption. Gaussian residual noise is clean for transformed higher cumulants; broader noise requires another argument. -->
<!-- TODO-NOTE: Emphasize the efficiency tradeoff: the robust set should be wider because it drops second-moment restrictions. -->

## 5. Monte Carlo Robustness Check

TODO: Present the simulation design and evidence package. Show the standard
sign set, standard DW set, robust DW set, and the overlap/divergence diagnostic
under no noise, moderate noise, high noise, weak higher moments, and
misspecification cases.

<!-- SOURCE-TRAIL: Use KnowledgeVault replication assets only as starting points; final figure commands must live in `replication/README.md`. -->
<!-- TODO-NOTE: Include an intuitive first figure, a false-sharpening figure, and a robust-set comparison figure. -->
<!-- TODO-NOTE: Report inconclusive and weak cases honestly. -->

## 6. Conclusion

TODO: Restate the practical recommendation: report the robust DW set beside the
standard DW set. If they overlap, the standard refinement is less suspect; if
they diverge, treat standard DW precision as a warning sign rather than
evidence of sharper structural learning.

## References

TODO: Use the citation style chosen in `manuscript-rules.md` and the BibTeX
snapshot in `../bibliography/references.bib`.
