# Simulations

Use this folder for exploratory simulation designs and design notes.

Final shareable code that reproduces manuscript figures and tables belongs in
`../replication/`.

## M35 Early J-Test Monte Carlo Triage

- Script: `m35_jtest_monte_carlo_triage.py`
- Output note: `m35_jtest_monte_carlo_triage.md`
- Machine-readable output: `output/m35_jtest_monte_carlo_summary.json`
- Command run:

```powershell
python manuscript/simulations/m35_jtest_monte_carlo_triage.py --seed 20260606 --reps 80 --sample-size 400 --angles 361 --shape-grid 51
```

Interpretation: this is a screening run only. It passes the no-noise sanity
case, but the provisional finite-sample statistic is too permissive under
moderate Gaussian residual noise and nearly non-discriminating under weak
higher moments. Audit and population-grid checks must come before polished
figures or final Monte Carlo tables.
