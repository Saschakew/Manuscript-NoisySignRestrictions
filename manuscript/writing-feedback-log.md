# Writing Feedback Log

Use this optional file for reusable lessons about the manuscript-writing
process.

## Lessons

- For this paper, introduce the SVAR object in the order an applied SVAR reader
  expects: no-noise residual, impact matrix, recovered shocks, uncorrelatedness,
  sign restrictions, then residual noise. Do not start with a covariance
  pseudo-set before the standard no-noise object is clear.
- When discussing sign restrictions, explicitly mention recovered-shock
  orthogonality. It is the assumption that makes residual noise visibly bias
  the standard sign-restricted set.
- Explain DW refinement first as an efficiency gain under the no-noise null:
  uncorrelated recovered shocks can remain dependent, so non-Gaussian higher
  moments sharpen the set. Only then introduce residual-noise misspecification
  and false precision.
- Present the robust proposal by starting with the researcher-chosen
  information/noise ratio, then add Gaussian-noise-blind higher cumulants as
  the efficiency-recovery step.
