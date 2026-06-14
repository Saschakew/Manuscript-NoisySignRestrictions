"""Clean iid pointwise MC with analytic efficient GMM weights.

M77 removes the sample-standardization and demeaning used by M74. The DGP uses
population-normalized iid chi-square structural shocks and iid Gaussian residual
noise. For the pointwise truth diagnostic, the statistic uses the analytic
iid weight W=(E[f_t f_t'])^{-1}, computed by polynomial expansion from the
assumed univariate moments rather than from an auxiliary simulation.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

try:
    from . import m69_extended_three_block_mc as m69
    from . import sign_dw_unit_variance_noise_grid_figure as fig
except ImportError:
    import m69_extended_three_block_mc as m69
    import sign_dw_unit_variance_noise_grid_figure as fig


ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = ROOT / "manuscript" / "simulations"
OUTPUT_DIR = SIM_DIR / "output"
JSON_OUTPUT = OUTPUT_DIR / "m77_clean_iid_mc_efficient_weight.json"
NOTE_OUTPUT = SIM_DIR / "m77_clean_iid_mc_efficient_weight.md"

SAMPLE_SCENARIOS = (
    m69.MCScenario("sample_t500", "T=500", (0.2, 0.2), 1.0, 500, "gaussian", "Baseline sample size."),
    m69.MCScenario("sample_t1000", "T=1000", (0.2, 0.2), 1.0, 1000, "gaussian", "Medium sample size."),
    m69.MCScenario("sample_t2000", "T=2000", (0.2, 0.2), 1.0, 2000, "gaussian", "Large sample size."),
)

Exponent = tuple[int, int, int, int]
Polynomial = dict[Exponent, float]


@dataclass(frozen=True)
class WeightBundle:
    covariance: np.ndarray
    inverse: np.ndarray
    eigenvalues: list[float]
    moment_means: list[float]
    regularization: dict[str, Any]


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def chi_square_raw_moment(df: float, order: int) -> float:
    value = 1.0
    for index in range(order):
        value *= df + 2.0 * index
    return value


def structural_raw_moments(max_order: int) -> list[float]:
    df = fig.STRUCTURAL_CHI2_DF
    scale = math.sqrt(2.0 * df)
    moments: list[float] = []
    for order in range(max_order + 1):
        total = 0.0
        for j in range(order + 1):
            total += (
                math.comb(order, j)
                * ((-df) ** (order - j))
                * chi_square_raw_moment(df, j)
            )
        moments.append(float(total / (scale**order)))
    return moments


def gaussian_raw_moments(max_order: int) -> list[float]:
    moments: list[float] = []
    for order in range(max_order + 1):
        if order % 2:
            moments.append(0.0)
            continue
        value = 1.0
        for odd in range(1, order, 2):
            value *= odd
        moments.append(float(value))
    return moments


STRUCTURAL_MOMENTS = structural_raw_moments(8)
GAUSSIAN_MOMENTS = gaussian_raw_moments(8)


def poly_constant(value: float) -> Polynomial:
    return {} if abs(value) <= 0.0 else {(0, 0, 0, 0): float(value)}


def poly_variable(index: int, coefficient: float = 1.0) -> Polynomial:
    exponent = [0, 0, 0, 0]
    exponent[index] = 1
    return {tuple(exponent): float(coefficient)}


def poly_add(*polys: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            result[exponent] = result.get(exponent, 0.0) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items() if abs(coefficient) > 1e-14}


def poly_scale(poly: Polynomial, scale: float) -> Polynomial:
    if abs(scale) <= 0.0:
        return {}
    return {exponent: coefficient * scale for exponent, coefficient in poly.items()}


def poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for exp_left, coef_left in left.items():
        for exp_right, coef_right in right.items():
            exponent = tuple(a + b for a, b in zip(exp_left, exp_right))
            result[exponent] = result.get(exponent, 0.0) + coef_left * coef_right
    return {exponent: coefficient for exponent, coefficient in result.items() if abs(coefficient) > 1e-14}


def poly_pow(poly: Polynomial, power: int) -> Polynomial:
    result = poly_constant(1.0)
    for _ in range(power):
        result = poly_mul(result, poly)
    return result


def poly_sub(left: Polynomial, right: Polynomial) -> Polynomial:
    return poly_add(left, poly_scale(right, -1.0))


def poly_expectation(poly: Polynomial) -> float:
    total = 0.0
    for exponent, coefficient in poly.items():
        moment = (
            STRUCTURAL_MOMENTS[exponent[0]]
            * STRUCTURAL_MOMENTS[exponent[1]]
            * GAUSSIAN_MOMENTS[exponent[2]]
            * GAUSSIAN_MOMENTS[exponent[3]]
        )
        total += coefficient * moment
    return float(total)


def covariance_from_polynomials(moments: list[Polynomial]) -> WeightBundle:
    means = np.array([poly_expectation(poly) for poly in moments], dtype=float)
    covariance = np.empty((len(moments), len(moments)), dtype=float)
    for i, left in enumerate(moments):
        for j, right in enumerate(moments):
            covariance[i, j] = poly_expectation(poly_mul(left, right)) - means[i] * means[j]
    covariance = 0.5 * (covariance + covariance.T)
    inverse, regularization = fig.regularized_inverse_stack(covariance[None, :, :])
    eigenvalues = np.linalg.eigvalsh(covariance)
    return WeightBundle(
        covariance=covariance,
        inverse=inverse[0],
        eigenvalues=[float(value) for value in eigenvalues],
        moment_means=[float(value) for value in means],
        regularization=regularization,
    )


def standard_second_weight() -> WeightBundle:
    e1 = poly_variable(0)
    e2 = poly_variable(1)
    moments = [
        poly_sub(poly_pow(e1, 2), poly_constant(1.0)),
        poly_mul(e1, e2),
        poly_sub(poly_pow(e2, 2), poly_constant(1.0)),
    ]
    return covariance_from_polynomials(moments)


def standard_dw_weight() -> WeightBundle:
    e1 = poly_variable(0)
    e2 = poly_variable(1)
    moments = [
        poly_mul(poly_pow(e1, 2), e2),
        poly_mul(e1, poly_pow(e2, 2)),
        poly_mul(poly_pow(e1, 3), e2),
        poly_sub(poly_mul(poly_pow(e1, 2), poly_pow(e2, 2)), poly_constant(1.0)),
        poly_mul(e1, poly_pow(e2, 3)),
    ]
    return covariance_from_polynomials(moments)


def robust_weight(
    b11: float,
    b12: float,
    b21: float,
    b22: float,
    lambda_pair: tuple[float, float],
) -> WeightBundle:
    signal_11 = b11 * b11 + b12 * b12
    signal_12 = b11 * b21 + b12 * b22
    signal_22 = b21 * b21 + b22 * b22
    nu1 = signal_11 * lambda_pair[0]
    nu2 = signal_22 * lambda_pair[1]

    eps1 = poly_variable(0)
    eps2 = poly_variable(1)
    eta1 = poly_variable(2, math.sqrt(max(nu1, 0.0)))
    eta2 = poly_variable(3, math.sqrt(max(nu2, 0.0)))
    u1 = poly_add(poly_scale(eps1, b11), poly_scale(eps2, b12), eta1)
    u2 = poly_add(poly_scale(eps1, b21), poly_scale(eps2, b22), eta2)

    determinant = b11 * b22 - b12 * b21
    inv11 = b22 / determinant
    inv12 = -b12 / determinant
    inv21 = -b21 / determinant
    inv22 = b11 / determinant
    e1 = poly_add(poly_scale(u1, inv11), poly_scale(u2, inv12))
    e2 = poly_add(poly_scale(u1, inv21), poly_scale(u2, inv22))

    omega11 = 1.0 + inv11 * inv11 * nu1 + inv12 * inv12 * nu2
    omega12 = inv11 * inv21 * nu1 + inv12 * inv22 * nu2
    omega22 = 1.0 + inv21 * inv21 * nu1 + inv22 * inv22 * nu2

    moments = [
        poly_sub(poly_pow(u1, 2), poly_constant(signal_11 + nu1)),
        poly_sub(poly_mul(u1, u2), poly_constant(signal_12)),
        poly_sub(poly_pow(u2, 2), poly_constant(signal_22 + nu2)),
        poly_mul(poly_pow(e1, 2), e2),
        poly_mul(e1, poly_pow(e2, 2)),
        poly_sub(poly_mul(poly_pow(e1, 3), e2), poly_constant(3.0 * omega11 * omega12)),
        poly_sub(
            poly_mul(poly_pow(e1, 2), poly_pow(e2, 2)),
            poly_constant(omega11 * omega22 + 2.0 * omega12 * omega12),
        ),
        poly_sub(poly_mul(e1, poly_pow(e2, 3)), poly_constant(3.0 * omega22 * omega12)),
    ]
    return covariance_from_polynomials(moments)


def cleaned_iid_draws(
    sample_size: int,
    seed: int,
    residual_noise: str = "gaussian",
) -> tuple[np.ndarray, np.ndarray]:
    if residual_noise != "gaussian":
        raise ValueError("M77 analytic weights currently support Gaussian residual noise only")
    rng = np.random.default_rng(seed)
    df = fig.STRUCTURAL_CHI2_DF
    structural = (rng.chisquare(df=df, size=(sample_size, 2)) - df) / math.sqrt(2.0 * df)
    noise = rng.normal(size=(sample_size, 2))
    return structural, noise


def cleaned_residuals(
    noise_variances: tuple[float, float],
    sample_size: int,
    seed: int,
    residual_noise: str = "gaussian",
) -> np.ndarray:
    structural, noise = cleaned_iid_draws(sample_size, seed, residual_noise)
    residuals = structural @ fig.TRUE_MATRIX.T
    residuals[:, 0] += math.sqrt(noise_variances[0]) * noise[:, 0]
    residuals[:, 1] += math.sqrt(noise_variances[1]) * noise[:, 1]
    return residuals


def recovered_shocks_no_center(
    residuals: np.ndarray,
    b11: np.ndarray,
    b12: np.ndarray,
    b21: np.ndarray,
    b22: np.ndarray,
) -> np.ndarray:
    _det, inv11, inv12, inv21, inv22 = fig.inverse_elements(b11, b12, b21, b22)
    u1 = residuals[:, 0:1]
    u2 = residuals[:, 1:2]
    e1 = u1 * inv11[None, :] + u2 * inv12[None, :]
    e2 = u1 * inv21[None, :] + u2 * inv22[None, :]
    return np.stack([e1, e2], axis=2)


def quadratic_stat(observations: np.ndarray, inverse_weight: np.ndarray) -> float:
    mean = observations.mean(axis=0)
    return float(observations.shape[0] * mean @ inverse_weight @ mean)


def true_lambda(noise_variances: tuple[float, float]) -> tuple[float, float]:
    signal = fig.TRUE_MATRIX @ fig.TRUE_MATRIX.T
    return (
        0.0 if signal[0, 0] <= 0.0 else noise_variances[0] / signal[0, 0],
        0.0 if signal[1, 1] <= 0.0 else noise_variances[1] / signal[1, 1],
    )


def truth_metrics(
    scenario: m69.MCScenario,
    seed: int,
    second_weight: WeightBundle,
    dw_weight: WeightBundle,
    robust_truth_weight: WeightBundle,
) -> dict[str, Any]:
    if abs(scenario.non_gaussian_weight - 1.0) > 1e-12:
        raise ValueError("M77 sample-size diagnostic currently supports strong non-Gaussianity only")
    residuals = cleaned_residuals(scenario.noise, scenario.sample_size, seed, scenario.residual_noise)
    shocks = recovered_shocks_no_center(
        residuals,
        np.array([fig.TRUE_B11]),
        np.array([fig.TRUE_B12]),
        np.array([fig.TRUE_B21]),
        np.array([fig.TRUE_B22]),
    )
    second_obs = fig.second_moment_observations(shocks)[:, 0, :]
    dw_obs = fig.standard_dw_observations(shocks)[:, 0, :]
    lambda_pair = true_lambda(scenario.noise)
    robust_obs = fig.robust_observations(
        residuals,
        shocks,
        np.array([fig.TRUE_B11]),
        np.array([fig.TRUE_B12]),
        np.array([fig.TRUE_B21]),
        np.array([fig.TRUE_B22]),
        np.array(lambda_pair, dtype=float)[None, :],
    )[:, 0, :]

    second_j = quadratic_stat(second_obs, second_weight.inverse)
    dw_j = quadratic_stat(dw_obs, dw_weight.inverse)
    robust_j = quadratic_stat(robust_obs, robust_truth_weight.inverse)
    sign_truth_in = second_j <= fig.CHI2_90_DF3
    standard_truth_in = sign_truth_in and dw_j <= fig.CHI2_90_DF5
    robust_truth_in = (
        lambda_pair[0] <= fig.RELATIVE_NOISE_RATIO
        and lambda_pair[1] <= fig.RELATIVE_NOISE_RATIO
        and robust_j <= fig.CHI2_90_DF8
    )
    return {
        "seed": int(seed),
        "sign": {
            "truth_in": bool(sign_truth_in),
            "truth_second_j": float(second_j),
        },
        "standard_dw": {
            "truth_in": bool(standard_truth_in),
            "truth_second_j": float(second_j),
            "truth_higher_j": float(dw_j),
        },
        "robust_dw": {
            "truth_in": bool(robust_truth_in),
            "truth_j": float(robust_j),
            "true_lambda": [float(lambda_pair[0]), float(lambda_pair[1])],
        },
        "warning": bool((not standard_truth_in) and robust_truth_in),
    }


def finite_values(values: list[Any]) -> np.ndarray:
    finite = [float(value) for value in values if value is not None and math.isfinite(float(value))]
    return np.asarray(finite, dtype=float)


def count_rate(values: list[Any]) -> dict[str, Any]:
    array = finite_values(values)
    if array.size == 0:
        return {"count": 0, "total": 0, "rate": None, "se": None}
    rate = float(np.mean(array >= 0.5))
    se = None if array.size <= 1 else float(math.sqrt(rate * (1.0 - rate) / array.size))
    return {"count": int(np.count_nonzero(array >= 0.5)), "total": int(array.size), "rate": rate, "se": se}


def numeric_summary(values: list[Any]) -> dict[str, Any]:
    array = finite_values(values)
    if array.size == 0:
        return {
            "n": 0,
            "mean": None,
            "median": None,
            "se": None,
            "min": None,
            "q75": None,
            "q90": None,
            "q95": None,
            "max": None,
        }
    return {
        "n": int(array.size),
        "mean": float(np.mean(array)),
        "median": float(np.median(array)),
        "se": None if array.size <= 1 else float(np.std(array, ddof=1) / math.sqrt(array.size)),
        "min": float(np.min(array)),
        "q75": float(np.quantile(array, 0.75)),
        "q90": float(np.quantile(array, 0.90)),
        "q95": float(np.quantile(array, 0.95)),
        "max": float(np.max(array)),
    }


def summarize(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for scenario in SAMPLE_SCENARIOS:
        subset = [record for record in records if record["scenario"] == scenario.name]
        metrics = [record["metrics"] for record in subset]
        summaries.append(
            {
                "scenario": scenario.name,
                "label": scenario.label,
                "reps": len(subset),
                "noise": list(scenario.noise),
                "non_gaussian_weight": scenario.non_gaussian_weight,
                "sample_size": scenario.sample_size,
                "residual_noise": scenario.residual_noise,
                "truth_inclusion": {
                    "sign": count_rate([m["sign"]["truth_in"] for m in metrics]),
                    "standard_dw": count_rate([m["standard_dw"]["truth_in"] for m in metrics]),
                    "robust_dw": count_rate([m["robust_dw"]["truth_in"] for m in metrics]),
                },
                "truth_j": {
                    "sign_second": numeric_summary([m["sign"]["truth_second_j"] for m in metrics]),
                    "standard_higher": numeric_summary([m["standard_dw"]["truth_higher_j"] for m in metrics]),
                    "robust_full": numeric_summary([m["robust_dw"]["truth_j"] for m in metrics]),
                },
                "warning": count_rate([m["warning"] for m in metrics]),
                "note": scenario.note,
            }
        )
    return summaries


def weight_metadata(bundle: WeightBundle) -> dict[str, Any]:
    return {
        "eigenvalues": bundle.eigenvalues,
        "moment_means": bundle.moment_means,
        "regularization": bundle.regularization,
        "condition_number": float(max(bundle.eigenvalues) / min(bundle.eigenvalues)),
    }


def fmt(value: Any, digits: int = 3) -> str:
    if value is None:
        return "n/a"
    numeric = float(value)
    if not math.isfinite(numeric):
        return "n/a"
    return f"{numeric:.{digits}f}"


def fmt_rate(item: dict[str, Any]) -> str:
    return f"{fmt(item['rate'])} ({item['count']}/{item['total']})"


def write_outputs(
    records: list[dict[str, Any]],
    summaries: list[dict[str, Any]],
    reps: int,
    weights: dict[str, WeightBundle],
    json_output: Path,
    note_output: Path,
) -> None:
    payload = {
        "schema_version": 1,
        "task": "M77 clean iid MC efficient weight",
        "description": "Truth-at-B0 sample-size diagnostic using population-normalized iid shocks/noise and analytic iid efficient GMM weights W=(E[f_t f_t'])^{-1}.",
        "configuration": {
            "reps_per_scenario": reps,
            "base_seed": fig.RANDOM_SEED,
            "rho": fig.RELATIVE_NOISE_RATIO,
            "dgp": "population-normalized iid chi-square structural shocks and iid Gaussian residual noise; no sample standardization; no residual or recovered-shock demeaning",
            "structural_shock": f"(chi2_{fig.STRUCTURAL_CHI2_DF:g} - {fig.STRUCTURAL_CHI2_DF:g}) / sqrt(2*{fig.STRUCTURAL_CHI2_DF:g})",
            "weighting": "analytic pointwise iid efficient weights W=(E[f_t f_t'])^{-1}; no auxiliary large-sample weight simulation",
            "diagnostic_scope": "truth-at-B0 pointwise size only; no accepted-set projection shares",
            "critical_values": {
                "second_moment_chi2_90_df3": fig.CHI2_90_DF3,
                "standard_dw_chi2_90_df5": fig.CHI2_90_DF5,
                "robust_full_moment_chi2_90_df8": fig.CHI2_90_DF8,
            },
            "weights": {name: weight_metadata(bundle) for name, bundle in weights.items()},
            "scenarios": [
                {
                    "name": scenario.name,
                    "label": scenario.label,
                    "noise": list(scenario.noise),
                    "non_gaussian_weight": scenario.non_gaussian_weight,
                    "sample_size": scenario.sample_size,
                    "residual_noise": scenario.residual_noise,
                    "note": scenario.note,
                }
                for scenario in SAMPLE_SCENARIOS
            ],
        },
        "summaries": summaries,
        "records": records,
    }
    json_output.parent.mkdir(parents=True, exist_ok=True)
    json_output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# M77 Clean IID MC Efficient Weight",
        "",
        "Status: generated truth-at-B0 pointwise size diagnostic for the cleaned iid sample-size design.",
        "",
        "The run removes the M74 sample-standardization and demeaning steps. Structural shocks are drawn as population-normalized iid chi-square variables, residual noise is iid Gaussian, residuals are not demeaned, and recovered shocks are not sample-centered. The pointwise weights are analytic iid efficient GMM weights, \\(W=(E[f_t f_t'])^{-1}\\), computed by polynomial expansion from the assumed univariate moments.",
        "",
        "This output reports truth-at-\\(B_0\\) pointwise inclusion only. It does not report accepted projection shares or empty-set rates.",
        "",
        "## Configuration",
        "",
        f"- Machine-readable output: `{display_path(json_output)}`.",
        f"- Replications per scenario: `{reps}`.",
        f"- Structural shock: `(chi2_{fig.STRUCTURAL_CHI2_DF:g} - {fig.STRUCTURAL_CHI2_DF:g}) / sqrt(2*{fig.STRUCTURAL_CHI2_DF:g})`.",
        "- Residual noise: iid Gaussian.",
        "- Weighting: analytic \\(W=(E[f_t f_t'])^{-1}\\), no auxiliary large-sample weight simulation.",
        "- Diagnostic scope: truth-at-\\(B_0\\) pointwise size only.",
        "",
        "## Analytic Weight Formula",
        "",
        "Let \\(q_t=(\\varepsilon_{1t},\\varepsilon_{2t},\\zeta_{1t},\\zeta_{2t})\\), where the first two entries are independent population-normalized chi-square variables and the last two entries are independent standard normals. For each tested candidate, the script writes every moment row as a polynomial \\(f_j(q_t)\\). It computes",
        "",
        "\\[",
        "\\Omega_f=E[f(q_t)f(q_t)']-E[f(q_t)]E[f(q_t)]',",
        "\\qquad",
        "W=\\Omega_f^{-1}.",
        "\\]",
        "",
        "The expectations are evaluated from exact univariate raw moments up to order eight. No auxiliary sample is used to estimate \\(W\\).",
        "",
        "## Truth-Inclusion Table",
        "",
        "| T | Sign truth | DW truth | nrDW truth | Warning | Sign J q90 | DW J q90 | nrDW J q90 |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in summaries:
        lines.append(
            "| {label} | {sign} | {dw} | {rdw} | {warning} | {sign_j} | {dw_j} | {rdw_j} |".format(
                label=item["label"].replace("T=", ""),
                sign=fmt_rate(item["truth_inclusion"]["sign"]),
                dw=fmt_rate(item["truth_inclusion"]["standard_dw"]),
                rdw=fmt_rate(item["truth_inclusion"]["robust_dw"]),
                warning=fmt_rate(item["warning"]),
                sign_j=fmt(item["truth_j"]["sign_second"]["q90"]),
                dw_j=fmt(item["truth_j"]["standard_higher"]["q90"]),
                rdw_j=fmt(item["truth_j"]["robust_full"]["q90"]),
            )
        )
    lines.extend(
        [
            "",
            "## Weight Diagnostics",
            "",
            "| Weight | Dimension | Min eigenvalue | Max eigenvalue | Condition number | Max absolute moment mean |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for name, bundle in weights.items():
        eigenvalues = bundle.eigenvalues
        max_abs_mean = max(abs(value) for value in bundle.moment_means)
        lines.append(
            f"| {name} | {len(eigenvalues)} | {min(eigenvalues):.6g} | {max(eigenvalues):.6g} | {max(eigenvalues) / min(eigenvalues):.6g} | {max_abs_mean:.3g} |"
        )
    lines.extend(
        [
            "",
            "## Claim Audit",
            "",
            "| Claim | Status | Evidence | Confidence | Action |",
            "|---|---|---|---|---|",
            "| With iid per-period moments and \\(E[f_t]=0\\), \\(W=(E[f_t f_t'])^{-1}\\) is the pointwise efficient GMM weight. | `derived`, `user-decision` | GMM variance of the sample mean under iid moments; M77 task prompt. | high | promote as cleaned MC design |",
            "| The cleaned MC is a simplification of the M74 weighting route. | `code-implemented`, `derived`, `user-decision` | This script removes sample-specific covariance weights and computes analytic population weights. | high | promote with DGP-change caveat |",
            "| This output replaces M74 Table 2 set-size evidence. | `conjectural` | M77 is truth-at-B0 only and reports no accepted projection shares. | high | quarantine; supplement M74 unless full-grid cleaned MC is run |",
            "",
        ]
    )
    note_output.parent.mkdir(parents=True, exist_ok=True)
    note_output.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def run(
    reps: int = 500,
    json_output: Path = JSON_OUTPUT,
    note_output: Path = NOTE_OUTPUT,
) -> Path:
    second_weight = standard_second_weight()
    dw_weight = standard_dw_weight()
    lambda_pair = true_lambda((0.2, 0.2))
    robust_truth = robust_weight(
        fig.TRUE_B11,
        fig.TRUE_B12,
        fig.TRUE_B21,
        fig.TRUE_B22,
        lambda_pair,
    )
    weights = {
        "sign_second": second_weight,
        "standard_dw_higher": dw_weight,
        "robust_full_truth": robust_truth,
    }

    records: list[dict[str, Any]] = []
    for scenario_index, scenario in enumerate(SAMPLE_SCENARIOS):
        for rep in range(reps):
            seed = m69.seed_for(fig.RANDOM_SEED, 2, scenario_index, rep)
            metrics = truth_metrics(scenario, seed, second_weight, dw_weight, robust_truth)
            records.append(
                {
                    "scenario": scenario.name,
                    "label": scenario.label,
                    "rep": rep,
                    "seed": seed,
                    "metrics": metrics,
                }
            )
    summaries = summarize(records)
    write_outputs(records, summaries, reps, weights, json_output, note_output)
    return json_output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reps", type=int, default=500)
    parser.add_argument("--json-output", type=Path, default=JSON_OUTPUT)
    parser.add_argument("--note-output", type=Path, default=NOTE_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    path = run(args.reps, args.json_output, args.note_output)
    print(f"Wrote {display_path(path)}")


if __name__ == "__main__":
    main()
