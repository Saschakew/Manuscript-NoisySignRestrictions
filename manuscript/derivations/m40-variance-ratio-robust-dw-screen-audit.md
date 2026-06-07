# M40 Variance-Ratio Robust DW Screen Audit

Status: conditional pass for proposal-level and disciplined Section 4 prose.

Audit date: 2026-06-07.

Scope:

- `manuscript/draft.md`
- `manuscript/derivations/dw-noise-robust-moments.md`
- `manuscript/simulations/sign_dw_robust_noise_grid_figure.py`
- `manuscript/simulations/sign_dw_relative_noise_robust_grid_figure.md`
- `manuscript/formal-object-registry.json`

Question: does the M0036 variance-ratio covariance screen correctly profile
structural-shock and residual-noise variances in the diagonal-normalized chart,
and can the 50 percent residual-noise-to-shock-variance bound support the
manuscript's robust DW comparison claim?

Answer: yes, conditionally. The screen is algebraically coherent as a
population feasibility restriction in the normalized bivariate chart, and it
avoids the M0034 double-normalization error. It is not a free normalization, a
DW moment condition, a confidence-set correction, or evidence by itself. Its
precision comes from explicit signal-to-noise identifying information, and the
finite-sample behavior still has to be rebuilt in M43-M45.

## Audited Object

For a candidate normalized impact matrix

```text
B = [[1, a],
     [b, 1]]
```

write the structural-shock covariance and residual-noise covariance as

```text
Var(epsilon) = diag(s_1, s_2),
Var(eta) = diag(nu_1, nu_2).
```

The covariance decomposition is

```text
S_11 = s_1 + a^2 s_2 + nu_1
S_12 = b s_1 + a s_2
S_22 = b^2 s_1 + s_2 + nu_2
```

with

```text
s_i > 0,
0 <= nu_i <= rho s_i,
rho = 0.5.
```

After profiling out `nu_i`, the equivalent screen is the linear feasibility
problem

```text
s_1 + a^2 s_2 <= S_11 <= (1 + rho) s_1 + a^2 s_2
b^2 s_1 + s_2 <= S_22 <= b^2 s_1 + (1 + rho) s_2
S_12 = b s_1 + a s_2
s_i > 0.
```

The robust row in Figure 1 accepts a candidate only when this feasibility
screen holds and the pure five-moment higher-cumulant J statistic is below the
pointwise `chi2_5(0.90)` guide cutoff.

## Checklist

### 1. Algebra And Scale

Outcome: pass.

The covariance equations are exactly the off-diagonal and diagonal entries of

```text
S = B diag(s_1, s_2) B' + diag(nu_1, nu_2).
```

This is the right way to use second-order information after the M0034 scale
correction. It profiles `s_i` and `nu_i` rather than imposing both
`diag(B)=1` and unit structural-shock variances. At the population true
candidate, the screen is feasible whenever the maintained diagonal
residual-noise model and `nu_i <= rho s_i` restriction are true.

The screen still relies on diagonal residual-noise covariance in the observed
residual coordinates. If residual noise is correlated, the covariance
decomposition needs an off-diagonal noise parameter, and this screen is no
longer the stated object. The pure higher-cumulant fallback remains the
validity backbone under arbitrary Gaussian residual-noise covariance.

### 2. Implementation

Outcome: pass, with finite-sample caveats.

`relative_noise_covariance_feasible` in
`sign_dw_robust_noise_grid_figure.py` parameterizes the equality
`S_12 = b s_1 + a s_2` as an affine line in `(s_1,s_2)` and intersects that
line with the six inequalities above. The signs of the implemented
inequalities match the displayed screen:

- `s_1 >= eps` and `s_2 >= eps`;
- `s_1 + a^2 s_2 <= S_11`;
- `S_11 <= (1 + rho) s_1 + a^2 s_2`;
- `b^2 s_1 + s_2 <= S_22`;
- `S_22 <= b^2 s_1 + (1 + rho) s_2`.

The special case `a=b=0` is also coherent: it requires near-zero `S_12` and
positive diagonal variances, after which feasible `s_i` exist for positive
`S_ii`.

The plotted statistic remains the pure higher-cumulant statistic, so the
current pointwise guide cutoff is `chi2_5(0.90)`. The covariance screen is an
intersection restriction, not an additional GMM moment with a `chi2`
reference distribution.

### 3. Interpretation Of The 50 Percent Bound

Outcome: conditional pass.

The bound `nu_i <= 0.5 s_i` is defensible only as explicit identifying
information. It says that, in the chosen residual coordinate and normalized
impact chart, each diagonal residual-noise variance is at most half of the
corresponding profiled structural-shock variance. That is scale-correct in a
way the M0035 absolute bound was not, but it is still substantive.

The manuscript should therefore avoid language suggesting that the bound is
automatic, implied by DW, or merely a normalization. The strongest clean claim
is a robustness-check claim: report the standard DW set beside the
variance-ratio robust set, and interpret standard-DW precision outside the
robust set as a warning under the maintained signal-to-noise bound.

### 4. Finite-Sample Behavior

Outcome: caution, not a blocking failure.

The screen is a hard equality-plus-inequality feasibility test applied to a
sample covariance matrix. At the true candidate, the population equality holds,
but finite samples contain off-diagonal sample covariance from structural
shocks, residual noise, and cross products. A hard screen can therefore
exclude the true candidate even when the DGP satisfies the population model.

A small M40 sanity check evaluated the screen at the true `B0` across 250
repeated draws using the current Figure 1 DGP:

| Sample size | `V=(0,0)` | `V=(0.2,0.2)` | `V=(0.5,0.5)` |
|---:|---:|---:|---:|
| `T=500` | 0.916 | 0.992 | 0.944 |
| `T=1000` | 0.988 | 1.000 | 0.972 |
| `T=2000` | 1.000 | 1.000 | 1.000 |

These rates are reassuring for the current calibration, but they are not a
coverage result. M45 should rerun the full validation and Monte Carlo package
for the variance-ratio proposal, including truth inclusion, accepted shares,
overlap, and sensitivity to the hard screen. A slackened or bootstrap-calibrated
version of the covariance screen may be worth reporting as an audit row if the
hard screen proves too brittle.

## Consequence For Drafting

Section 4 can state the variance-ratio screen as a conditionally audited
population restriction:

*Under the normalized bivariate chart, diagonal Gaussian residual noise,
independent structural shocks, and the maintained bound
`nu_i <= rho s_i`, the true normalized impact matrix satisfies the pure
higher-cumulant restrictions and the profiled covariance-decomposition screen.*

The statement should also retain these limits:

- it identifies a normalized impact shape, not arbitrary column scales;
- the 50 percent bound is substantive signal-to-noise information;
- correlated residual-noise covariance requires a different screen or the pure
  higher-cumulant fallback;
- the hard finite-sample screen is not a confidence correction;
- pointwise `chi2_5` language applies only to the higher-cumulant statistic;
- M43-M45 must rebuild Figure 2, Figure 3, validation, and Monte Carlo evidence
  before the paper treats variance-ratio robust DW as final evidence.

M40 therefore clears the variance-ratio screen for careful proposal prose, but
not for an unconditional theorem or a completed evidence claim.
