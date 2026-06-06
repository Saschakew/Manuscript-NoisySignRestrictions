# M30 Audit of M35 J-Test Monte Carlo Triage

Status: completed M30 audit of the exploratory M35 screen. This audit does not
make the M35 output final evidence. It decides whether the script is safe to
use as a diagnostic input for the next evidence tasks.

## Scope

Audited files:

- `manuscript/simulations/m35_jtest_monte_carlo_triage.py`
- `manuscript/simulations/m35_jtest_monte_carlo_triage.md`
- `manuscript/simulations/output/m35_jtest_monte_carlo_summary.json`

Audit question: can the M35 script be trusted as an early screen for
standard-DW versus robust-DW behavior before population-grid and final
Monte Carlo work?

Answer: only as a cautionary screen. It is useful for discovering weak
designs and obvious non-discrimination, but it is not a calibrated J-test
inversion and should not be used for manuscript figures or tables.

## Findings

### 1. DGP Normalization

Outcome: pass for the intended exploratory design.

The structural shock generator combines independent unit-variance non-Gaussian
draws with independent Gaussian draws using square-root weights. In population
this preserves zero means, unit variances, and mutual independence across the
two shocks. The weak-moment case correctly shrinks higher cumulants through
the mixture weight.

Remaining caveat: sample cumulants are centered but not unbiased
`k`-statistics, so finite-sample size and coverage claims remain out of scope.

### 2. Noise Design

Outcome: corrected during M30.

The original moderate Gaussian noise case used diagonal residual noise

```text
V = [[0.20, 0.00],
     [0.00, 0.12]]
```

For the chosen `B0`, this is very close to a structural-coordinate rescaling
exception from the M25 derivation:

```text
||offdiag(B0^{-1} V B0^{-1'})|| = 0.0096
```

That made it a weak stress case for generic standard-DW misspecification.
The script now reports this structural-coordinate off-diagonal norm and adds
an anisotropic diagonal-noise case:

```text
V = [[0.50, 0.00],
     [0.00, 0.05]]
```

with

```text
||offdiag(B0^{-1} V B0^{-1'})|| = 0.1285
```

This makes the triage design more honest, but it still does not replace the
M28 population-grid check.

### 3. Candidate Spaces And Normalization

Outcome: conditional pass.

The standard-DW candidate set correctly searches rotations of a factor of
`Sigma_u = B0 B0' + V`. The robust-DW candidate set searches the normalized
chart

```text
B(a,b) = [[1, a],
          [b, 1]]
```

and includes the true normalized shape `(a0, b0) = (0.35, -0.25)` on the grid.
The shape-distance metric is consistent across the two methods.

Remaining caveat: the standard-DW simulation uses the population covariance
factor rather than a sample covariance estimate. This isolates higher-moment
screening behavior, but final finite-sample evidence must either use sample
covariances or clearly separate population-grid and sample-noise experiments.

### 4. Cumulant Formulas

Outcome: pass for centered exploratory moments.

The implemented stack matches the M24/M25 moment list:

- `E[z1^2 z2]`
- `E[z1 z2^2]`
- `E[z1^3 z2] - 3 s11 s12`
- `E[z1^2 z2^2] - s11 s22 - 2 s12^2`
- `E[z1 z2^3] - 3 s22 s12`

The fourth-order entries are cumulants, not raw fourth moments, so Gaussian
noise variance terms are not mistakenly imposed as structural restrictions.

Remaining caveat: final inference should use either valid influence-function
standard errors, bootstrap/repetition critical values, or a package-backed GMM
implementation. The current scale normalization is only a rough screen.

### 5. Weighting And Critical Values

Outcome: fail for evidence, acceptable for triage.

The current statistic uses diagonal per-candidate raw-product standardization
and compares the sum of squared standardized moments with a chi-square(5)
reference value. That is not a valid calibrated J-test inversion because it
does not estimate the full covariance of the cumulant moment vector, does not
account for covariance-product nuisance terms through the delta method, and
does not account for grid search or repeated candidate testing.

This explains why accepted fractions are high, especially in the weak-moment
case. Final M29 evidence must use repeated-sample or bootstrap critical values.

### 6. Interpretation

Outcome: pass after M30 correction.

The generated M35 note now says that:

- the original moderate-noise scenario is close to a rescaling exception;
- the anisotropic scenario is a better first stress case;
- weak higher moments make both screens nearly non-discriminating;
- the output supports M28/M30, not polished M29 tables.

This is the right level of interpretation for the current evidence stage.

## Decision

M30 passes the M35 script only as an exploratory triage tool. The audit found
and corrected the weak moderate-noise stress case, but the weighting and
critical-value machinery remain too provisional for manuscript evidence.

Next work:

1. Run M28 population-grid checks for exact or near population zeros, standard
   DW pseudo-zeros, robust-DW truth inclusion, and weak-moment widening.
2. Use M29 only after M28 and after replacing the current screening critical
   value with repeated-sample or bootstrap critical values.
3. Keep the final reproducibility code under `manuscript/replication/`, not in
   this exploratory simulations folder.
