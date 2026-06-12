"""Rebuild validation and Monte Carlo evidence for variance-ratio robust DW.

This script now writes the M52 source-correct rebuild of the earlier M45-style
evidence gate. It treats the standard-DW row as the source-correct bivariate
DW GMM1 higher-moment menu intersected with a separate no-noise covariance
screen in the common B-plane chart. It treats the robust set as the pure mixed
higher-cumulant J inversion, with full central-moment delta weighting,
intersected with the relative covariance-decomposition screen:

    0 <= nu_i <= 0.5 * Var(epsilon_i).

The script intentionally writes new M45 outputs instead of replacing the
historical M28/M29 files, because those older files document the superseded
diagonal-anchor robust row.
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
    from . import sign_dw_robust_noise_grid_figure as base
except ImportError:
    import sign_dw_robust_noise_grid_figure as base


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "manuscript" / "simulations" / "output"
JSON_OUTPUT = OUTPUT_DIR / "m52_source_correct_evidence.json"
NOTE_OUTPUT = ROOT / "manuscript" / "simulations" / "m52_source_correct_evidence.md"

ROBUST_MODE = "relative"
GRID_WINDOW = (-1.35, 0.35, -0.25, 1.35)


@dataclass(frozen=True)
class Scenario:
    group: str
    name: str
    label: str
    noise: tuple[float, float]
    non_gaussian_weight: float
    sample_size: int
    residual_noise: str
    note: str


FIGURE_SCENARIOS = (
    Scenario("figure1_noise", "noise_none", "V=(0,0)", (0.0, 0.0), 1.0, 500, "gaussian", "Figure 1 no-noise column."),
    Scenario("figure1_noise", "noise_moderate", "V=(0.2,0.2)", (0.2, 0.2), 1.0, 500, "gaussian", "Figure 1 moderate-noise column."),
    Scenario("figure1_noise", "noise_high", "V=(0.5,0.5)", (0.5, 0.5), 1.0, 500, "gaussian", "Figure 1 high-noise column."),
    Scenario("figure2_nongaussianity", "strong_nongaussianity", "w=1", (0.2, 0.2), 1.0, 500, "gaussian", "Figure 2 strong higher moments."),
    Scenario("figure2_nongaussianity", "weak_nongaussianity", "w=0.25", (0.2, 0.2), 0.25, 500, "gaussian", "Figure 2 weak higher moments."),
    Scenario("figure2_nongaussianity", "gaussian_shocks", "w=0", (0.2, 0.2), 0.0, 500, "gaussian", "Figure 2 all-null higher-cumulant limit."),
    Scenario("figure3_sample_size", "sample_500", "T=500", (0.2, 0.2), 1.0, 500, "gaussian", "Figure 3 first sample-size column."),
    Scenario("figure3_sample_size", "sample_1000", "T=1000", (0.2, 0.2), 1.0, 1000, "gaussian", "Figure 3 middle sample-size column."),
    Scenario("figure3_sample_size", "sample_2000", "T=2000", (0.2, 0.2), 1.0, 2000, "gaussian", "Figure 3 large sample-size column."),
)

MC_SCENARIOS = (
    Scenario("monte_carlo", "no_noise", "No noise, strong moments", (0.0, 0.0), 1.0, 500, "gaussian", "Sanity case."),
    Scenario("monte_carlo", "moderate_noise", "Moderate Gaussian noise", (0.2, 0.2), 1.0, 500, "gaussian", "Figure 1/Figure 2 fixed-noise calibration."),
    Scenario("monte_carlo", "high_noise", "High Gaussian noise", (0.5, 0.5), 1.0, 500, "gaussian", "Main residual-noise stress case."),
    Scenario("monte_carlo", "weak_moments", "Weak structural higher moments", (0.2, 0.2), 0.25, 500, "gaussian", "Higher-moment limitation case."),
    Scenario("monte_carlo", "gaussian_shocks", "Gaussian structural shocks", (0.2, 0.2), 0.0, 500, "gaussian", "All-null higher-cumulant limit."),
    Scenario("monte_carlo", "skewed_residual_noise", "Skewed residual noise", (0.2, 0.2), 1.0, 500, "skewed", "Maintained-assumption stress case."),
)


def finite_float(value: float | np.floating[Any]) -> float | None:
    value = float(value)
    return value if math.isfinite(value) else None


def seed_for(base_seed: int, block: int, scenario_index: int, rep: int) -> int:
    return int(base_seed + block * 1_000_000 + scenario_index * 10_000 + rep)


def standardize_mixture(seed: int, scenario: Scenario) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    sample_size = scenario.sample_size
    skewed = base.standardize_columns(
        rng.chisquare(df=base.STRUCTURAL_CHI2_DF, size=(sample_size, 2))
    )
    gaussian = base.standardize_columns(rng.normal(size=(sample_size, 2)))
    structural = math.sqrt(scenario.non_gaussian_weight) * skewed
    structural += math.sqrt(max(0.0, 1.0 - scenario.non_gaussian_weight)) * gaussian
    structural = base.standardize_columns(structural)

    if scenario.residual_noise == "gaussian":
        noise = rng.normal(size=(sample_size, 2))
    elif scenario.residual_noise == "skewed":
        noise = rng.chisquare(df=base.STRUCTURAL_CHI2_DF, size=(sample_size, 2))
    else:
        raise ValueError(f"unknown residual-noise type: {scenario.residual_noise}")
    return structural, base.standardize_columns(noise)


def simulate_residuals(seed: int, scenario: Scenario) -> np.ndarray:
    structural, noise = standardize_mixture(seed, scenario)
    residuals = structural @ base.TRUE_MATRIX.T
    residuals[:, 0] += math.sqrt(scenario.noise[0]) * noise[:, 0]
    residuals[:, 1] += math.sqrt(scenario.noise[1]) * noise[:, 1]
    return residuals - residuals.mean(axis=0, keepdims=True)


def simulate_figure_residuals(seed: int, scenario: Scenario) -> np.ndarray:
    """Match the exact draw streams used by the rendered figure scripts."""
    rng = np.random.default_rng(seed)
    if scenario.group == "figure2_nongaussianity":
        skewed = base.standardize_columns(
            rng.chisquare(df=base.STRUCTURAL_CHI2_DF, size=(scenario.sample_size, 2))
        )
        gaussian = base.standardize_columns(rng.normal(size=(scenario.sample_size, 2)))
        structural = math.sqrt(scenario.non_gaussian_weight) * skewed
        structural += math.sqrt(max(0.0, 1.0 - scenario.non_gaussian_weight)) * gaussian
        structural = base.standardize_columns(structural)
    else:
        structural = base.standardize_columns(
            rng.chisquare(df=base.STRUCTURAL_CHI2_DF, size=(scenario.sample_size, 2))
        )
    noise = base.standardize_columns(rng.normal(size=(scenario.sample_size, 2)))
    residuals = structural @ base.TRUE_MATRIX.T
    residuals[:, 0] += math.sqrt(scenario.noise[0]) * noise[:, 0]
    residuals[:, 1] += math.sqrt(scenario.noise[1]) * noise[:, 1]
    return residuals - residuals.mean(axis=0, keepdims=True)


def make_grid(points: int) -> tuple[np.ndarray, np.ndarray]:
    b12_min, b12_max, b21_min, b21_max = GRID_WINDOW
    b12_grid = np.unique(np.append(np.linspace(b12_min, b12_max, points), base.TRUE_B12))
    b21_grid = np.unique(np.append(np.linspace(b21_min, b21_max, points), base.TRUE_B21))
    return b12_grid, b21_grid


def robust_feasible_grid(
    residuals: np.ndarray,
    b12_mesh: np.ndarray,
    b21_mesh: np.ndarray,
) -> np.ndarray:
    feasible = np.zeros_like(b12_mesh, dtype=bool)
    rows, cols = np.where(
        (b21_mesh >= 0.0) & (np.abs(1.0 - b12_mesh * b21_mesh) > 1e-10)
    )
    for row, col in zip(rows, cols):
        feasible[row, col] = base.relative_noise_covariance_feasible(
            float(b12_mesh[row, col]),
            float(b21_mesh[row, col]),
            residuals,
        )
    return feasible


def truth_values(residuals: np.ndarray) -> dict[str, Any]:
    standard_shocks = base.standardized_candidate_shocks(base.TRUE_B12, base.TRUE_B21, residuals)
    standard_j = math.nan
    covariance_j = math.nan
    if standard_shocks is not None:
        covariance_j = base.j_statistic(standard_shocks, base.MOMENTS_COVARIANCE)
        standard_j = base.j_statistic(standard_shocks, base.MOMENTS_DW)
    robust_j = base.robust_mode_statistic(
        base.TRUE_B12,
        base.TRUE_B21,
        residuals,
        ROBUST_MODE,
    )
    robust_feasible = base.relative_noise_covariance_feasible(
        base.TRUE_B12,
        base.TRUE_B21,
        residuals,
    )
    return {
        "standard_dw": finite_float(standard_j),
        "standard_covariance": finite_float(covariance_j),
        "standard_covariance_in": bool(
            math.isfinite(covariance_j) and covariance_j <= base.CHI2_90_DF1
        ),
        "robust_dw": finite_float(robust_j),
        "robust_feasible": bool(robust_feasible),
    }


def grid_statistics(
    residuals: np.ndarray,
    scenario: Scenario,
    grid_points: int,
) -> dict[str, Any]:
    b12_grid, b21_grid = make_grid(grid_points)
    (
        b12_mesh,
        b21_mesh,
        _correlation,
        covariance_j,
        covariance_accepted,
        standard_j,
        _standard_accepted,
    ) = base.evaluate_standard_grid(
        residuals,
        scenario.noise[0],
        scenario.noise[1],
        b12_grid,
        b21_grid,
    )
    _, _, robust_j, _robust_accepted = base.evaluate_robust_grid(
        residuals,
        b12_grid,
        b21_grid,
        ROBUST_MODE,
    )
    robust_feasible = robust_feasible_grid(residuals, b12_mesh, b21_mesh)
    return {
        "b12_mesh": b12_mesh,
        "b21_mesh": b21_mesh,
        "standard_covariance_j": covariance_j,
        "standard_covariance_accepted": covariance_accepted,
        "standard_j": standard_j,
        "robust_j": robust_j,
        "robust_feasible": robust_feasible,
    }


def least_rejected(
    j_values: np.ndarray,
    b12_mesh: np.ndarray,
    b21_mesh: np.ndarray,
    mask: np.ndarray,
) -> dict[str, float | None]:
    candidates = np.where(mask & np.isfinite(j_values), j_values, np.nan)
    if not np.isfinite(candidates).any():
        return {"j": None, "b12": None, "b21": None, "distance": None}
    row, col = np.unravel_index(int(np.nanargmin(candidates)), candidates.shape)
    distance = math.hypot(
        float(b12_mesh[row, col]) - base.TRUE_B12,
        float(b21_mesh[row, col]) - base.TRUE_B21,
    )
    return {
        "j": float(candidates[row, col]),
        "b12": float(b12_mesh[row, col]),
        "b21": float(b21_mesh[row, col]),
        "distance": float(distance),
    }


def distance_to_set(accepted: np.ndarray, b12_mesh: np.ndarray, b21_mesh: np.ndarray) -> float | None:
    if not accepted.any():
        return None
    distances = np.hypot(b12_mesh[accepted] - base.TRUE_B12, b21_mesh[accepted] - base.TRUE_B21)
    return float(np.min(distances))


def set_metrics(
    stats: dict[str, Any],
    truth: dict[str, Any],
    standard_cutoff: float,
    robust_cutoff: float,
) -> dict[str, Any]:
    b12_mesh = stats["b12_mesh"]
    b21_mesh = stats["b21_mesh"]
    standard_j = stats["standard_j"]
    standard_covariance_accepted = stats["standard_covariance_accepted"]
    robust_j = stats["robust_j"]
    robust_feasible = stats["robust_feasible"]
    chart = np.isfinite(robust_j)
    chart_count = int(np.count_nonzero(chart))

    standard = (
        chart
        & standard_covariance_accepted
        & np.isfinite(standard_j)
        & (standard_j <= standard_cutoff)
    )
    robust = chart & robust_feasible & np.isfinite(robust_j) & (robust_j <= robust_cutoff)
    intersection = standard & robust
    union = standard | robust

    standard_count = int(np.count_nonzero(standard))
    robust_count = int(np.count_nonzero(robust))
    intersection_count = int(np.count_nonzero(intersection))
    union_count = int(np.count_nonzero(union))
    standard_contained = intersection_count / standard_count if standard_count else None
    robust_contained = intersection_count / robust_count if robust_count else None

    standard_truth_j = truth["standard_dw"]
    standard_covariance_j = truth["standard_covariance"]
    standard_covariance_in = bool(truth["standard_covariance_in"])
    robust_truth_j = truth["robust_dw"]
    standard_truth_in = (
        standard_truth_j is not None
        and standard_truth_j <= standard_cutoff
        and standard_covariance_in
    )
    robust_truth_in = (
        robust_truth_j is not None
        and robust_truth_j <= robust_cutoff
        and bool(truth["robust_feasible"])
    )

    return {
        "grid_count": chart_count,
        "standard_dw": {
            "accepted_count": standard_count,
            "accepted_share": standard_count / chart_count if chart_count else None,
            "empty": standard_count == 0,
            "truth_in": bool(standard_truth_in),
            "truth_j": standard_truth_j,
            "covariance_truth_j": standard_covariance_j,
            "covariance_screen_in": standard_covariance_in,
            "distance_to_accepted_set": distance_to_set(standard, b12_mesh, b21_mesh),
            "least_rejected": least_rejected(
                standard_j,
                b12_mesh,
                b21_mesh,
                chart & standard_covariance_accepted,
            ),
        },
        "robust_dw": {
            "accepted_count": robust_count,
            "accepted_share": robust_count / chart_count if chart_count else None,
            "empty": robust_count == 0,
            "truth_in": bool(robust_truth_in),
            "truth_j": robust_truth_j,
            "truth_feasible": bool(truth["robust_feasible"]),
            "distance_to_accepted_set": distance_to_set(robust, b12_mesh, b21_mesh),
            "least_rejected": least_rejected(robust_j, b12_mesh, b21_mesh, chart & robust_feasible),
        },
        "overlap": {
            "intersection_count": intersection_count,
            "union_count": union_count,
            "jaccard": intersection_count / union_count if union_count else None,
            "q_standard_given_robust": standard_contained,
            "q_robust_given_standard": robust_contained,
            "d_standard_not_subset_robust": None
            if standard_contained is None
            else 1.0 - standard_contained,
        },
    }


def calibrate_truth_cutoffs(
    scenarios: tuple[Scenario, ...],
    base_seed: int,
    reps: int,
) -> tuple[dict[str, dict[str, float]], list[dict[str, Any]]]:
    cutoffs: dict[str, dict[str, float]] = {}
    records: list[dict[str, Any]] = []
    for scenario_index, scenario in enumerate(scenarios):
        truth_js: dict[str, list[float | None]] = {"standard_dw": [], "robust_dw": []}
        feasible_values: list[bool] = []
        for rep in range(reps):
            seed = seed_for(base_seed, 1, scenario_index, rep)
            residuals = simulate_residuals(seed, scenario)
            truth = truth_values(residuals)
            truth_js["standard_dw"].append(truth["standard_dw"])
            truth_js["robust_dw"].append(truth["robust_dw"])
            feasible_values.append(bool(truth["robust_feasible"]))
            records.append({"scenario": scenario.name, "rep": rep, "seed": seed, "truth": truth})
        cutoffs[scenario.name] = {
            "standard_dw": quantile_or_nan(truth_js["standard_dw"], 0.90),
            "robust_dw": quantile_or_nan(truth_js["robust_dw"], 0.90),
            "robust_truth_feasible_rate": float(np.mean(feasible_values)),
        }
    return cutoffs, records


def quantile_or_nan(values: list[float | None], probability: float) -> float:
    finite = np.array([value for value in values if value is not None], dtype=float)
    if finite.size == 0:
        return math.nan
    return float(np.quantile(finite, probability))


def cutoff_catalog(
    truth_cutoffs: dict[str, dict[str, float]],
    scenario_name: str,
) -> list[dict[str, Any]]:
    no_noise = truth_cutoffs["no_noise"]
    scenario = truth_cutoffs[scenario_name]
    return [
        {
            "name": "chi_square_90",
            "label": "Chi-square 90%",
            "standard_dw": base.standard_dw_cutoff(),
            "robust_dw": base.robust_mode_cutoff(ROBUST_MODE),
        },
        {
            "name": "no_noise_repeated_90",
            "label": "No-noise repeated 90%",
            "standard_dw": no_noise["standard_dw"],
            "robust_dw": no_noise["robust_dw"],
        },
        {
            "name": "scenario_truth_repeated_90",
            "label": "Scenario truth repeated 90%",
            "standard_dw": scenario["standard_dw"],
            "robust_dw": scenario["robust_dw"],
        },
    ]


def fixed_grid_diagnostics(grid_points: int) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for scenario in FIGURE_SCENARIOS:
        figure_seed = base.RANDOM_SEED
        residuals = simulate_figure_residuals(figure_seed, scenario)
        stats = grid_statistics(residuals, scenario, grid_points)
        truth = truth_values(residuals)
        metrics = set_metrics(
            stats,
            truth,
            base.standard_dw_cutoff(),
            base.robust_mode_cutoff(ROBUST_MODE),
        )
        records.append(
            {
                "group": scenario.group,
                "scenario": scenario.name,
                "label": scenario.label,
                "noise": list(scenario.noise),
                "non_gaussian_weight": scenario.non_gaussian_weight,
                "sample_size": scenario.sample_size,
                "seed": figure_seed,
                "metrics": metrics,
                "note": scenario.note,
            }
        )
    return records


def evaluate_records(
    scenarios: tuple[Scenario, ...],
    truth_cutoffs: dict[str, dict[str, float]],
    base_seed: int,
    reps: int,
    grid_points: int,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for scenario_index, scenario in enumerate(scenarios):
        for rep in range(reps):
            seed = seed_for(base_seed, 2, scenario_index, rep)
            residuals = simulate_residuals(seed, scenario)
            stats = grid_statistics(residuals, scenario, grid_points)
            truth = truth_values(residuals)
            for cutoff in cutoff_catalog(truth_cutoffs, scenario.name):
                records.append(
                    {
                        "scenario": scenario.name,
                        "label": scenario.label,
                        "cutoff_convention": cutoff["name"],
                        "rep": rep,
                        "seed": seed,
                        "cutoffs": {
                            "standard_dw": finite_float(cutoff["standard_dw"]),
                            "robust_dw": finite_float(cutoff["robust_dw"]),
                        },
                        "metrics": set_metrics(
                            stats,
                            truth,
                            cutoff["standard_dw"],
                            cutoff["robust_dw"],
                        ),
                    }
                )
    return records


def mean_optional(values: list[float | int | bool | None]) -> float | None:
    finite: list[float] = []
    for value in values:
        if value is None:
            continue
        numeric = float(value)
        if math.isfinite(numeric):
            finite.append(numeric)
    if not finite:
        return None
    return float(np.mean(finite))


def median_optional(values: list[float | int | bool | None]) -> float | None:
    finite: list[float] = []
    for value in values:
        if value is None:
            continue
        numeric = float(value)
        if math.isfinite(numeric):
            finite.append(numeric)
    if not finite:
        return None
    return float(np.median(finite))


def summarize(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    scenario_order = [scenario.name for scenario in MC_SCENARIOS]
    cutoff_order = ["chi_square_90", "no_noise_repeated_90", "scenario_truth_repeated_90"]
    for scenario_name in scenario_order:
        for cutoff_name in cutoff_order:
            subset = [
                record
                for record in records
                if record["scenario"] == scenario_name
                and record["cutoff_convention"] == cutoff_name
            ]
            if not subset:
                continue
            standard = [record["metrics"]["standard_dw"] for record in subset]
            robust = [record["metrics"]["robust_dw"] for record in subset]
            overlap = [record["metrics"]["overlap"] for record in subset]
            warning_values = [
                (
                    (not record["metrics"]["standard_dw"]["truth_in"])
                    and record["metrics"]["robust_dw"]["truth_in"]
                )
                or (
                    record["metrics"]["overlap"]["d_standard_not_subset_robust"] is not None
                    and record["metrics"]["overlap"]["d_standard_not_subset_robust"] >= 0.25
                    and record["metrics"]["standard_dw"]["accepted_share"] is not None
                    and record["metrics"]["standard_dw"]["accepted_share"] > 0.01
                )
                for record in subset
            ]
            rows.append(
                {
                    "scenario": scenario_name,
                    "label": subset[0]["label"],
                    "cutoff_convention": cutoff_name,
                    "cutoffs": subset[0]["cutoffs"],
                    "standard_dw": {
                        "truth_in_rate": mean_optional([item["truth_in"] for item in standard]),
                        "empty_rate": mean_optional([item["empty"] for item in standard]),
                        "mean_accepted_share": mean_optional([item["accepted_share"] for item in standard]),
                        "median_truth_j": median_optional([item["truth_j"] for item in standard]),
                        "mean_distance_to_set": mean_optional([item["distance_to_accepted_set"] for item in standard]),
                        "mean_least_rejected_distance": mean_optional(
                            [item["least_rejected"]["distance"] for item in standard]
                        ),
                    },
                    "robust_dw": {
                        "truth_in_rate": mean_optional([item["truth_in"] for item in robust]),
                        "truth_feasible_rate": mean_optional([item["truth_feasible"] for item in robust]),
                        "empty_rate": mean_optional([item["empty"] for item in robust]),
                        "mean_accepted_share": mean_optional([item["accepted_share"] for item in robust]),
                        "median_truth_j": median_optional([item["truth_j"] for item in robust]),
                        "mean_distance_to_set": mean_optional([item["distance_to_accepted_set"] for item in robust]),
                        "mean_least_rejected_distance": mean_optional(
                            [item["least_rejected"]["distance"] for item in robust]
                        ),
                    },
                    "overlap": {
                        "mean_jaccard": mean_optional([item["jaccard"] for item in overlap]),
                        "mean_d_standard_not_subset_robust": mean_optional(
                            [item["d_standard_not_subset_robust"] for item in overlap]
                        ),
                        "warning_rate": mean_optional(warning_values),
                    },
                }
            )
    return rows


def fmt(value: Any, digits: int = 3) -> str:
    if value is None:
        return "n/a"
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        return str(value)
    if not math.isfinite(numeric):
        return "n/a"
    return f"{numeric:.{digits}f}"


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def write_note(payload: dict[str, Any], note_output: Path, json_output: Path) -> None:
    convention_labels = {
        "chi_square_90": "chi-square",
        "no_noise_repeated_90": "no-noise repeated",
        "scenario_truth_repeated_90": "scenario truth",
    }
    summary_lookup = {
        (row["scenario"], row["cutoff_convention"]): row
        for row in payload["monte_carlo_summary"]
    }
    lines = [
        "# M52 Source-Correct Variance-Ratio Robust DW Evidence",
        "",
        "Status: completed M52 source-correct rebuild for the variance-ratio robust DW proposal.",
        "",
        "The standard-DW set in this pass is the source-correct bivariate DW GMM1 higher-moment menu, `112`, `122`, `1112`, `1122`, and `1222`, intersected with a separate no-noise covariance screen in the common diagonal-normalized B-plane chart.",
        "",
        "The robust set is the pure five-moment higher-cumulant J inversion with full central-moment delta weighting for generated fourth cumulants, intersected with the relative covariance-decomposition screen. The screen is applied in every grid and every truth-inclusion calculation.",
        "",
        "## Configuration",
        "",
        f"- Base seed: `{payload['configuration']['seed']}`.",
        f"- Fixed-grid diagnostic grid: `{payload['configuration']['diagnostic_grid_points']} x {payload['configuration']['diagnostic_grid_points']}` plus the true point.",
        f"- Monte Carlo calibration replications per scenario: `{payload['configuration']['calibration_reps']}`.",
        f"- Monte Carlo evaluation replications per scenario: `{payload['configuration']['evaluation_reps']}`.",
        f"- Monte Carlo grid: `{payload['configuration']['grid_points']} x {payload['configuration']['grid_points']}` plus the true point.",
        f"- Standard-DW primary cutoff: `{fmt(base.standard_dw_cutoff())}` for source-correct `{base.STANDARD_DW_MENU}` higher moments, plus a separate covariance-screen cutoff `{fmt(base.CHI2_90_DF1)}`.",
        f"- Robust cutoff under the primary chi-square convention: `{fmt(base.robust_mode_cutoff(ROBUST_MODE))}` with five generated higher-cumulant moments.",
        "",
        "## Fixed-Grid Diagnostics",
        "",
        "| Group | Scenario | S truth | R truth | R feasible | S share | R share | d_S_not_subset_R |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for record in payload["fixed_grid_diagnostics"]:
        metrics = record["metrics"]
        lines.append(
            "| {group} | {label} | {s_truth} | {r_truth} | {r_feas} | {s_share} | {r_share} | {div} |".format(
                group=record["group"],
                label=record["label"],
                s_truth="yes" if metrics["standard_dw"]["truth_in"] else "no",
                r_truth="yes" if metrics["robust_dw"]["truth_in"] else "no",
                r_feas="yes" if metrics["robust_dw"]["truth_feasible"] else "no",
                s_share=fmt(metrics["standard_dw"]["accepted_share"]),
                r_share=fmt(metrics["robust_dw"]["accepted_share"]),
                div=fmt(metrics["overlap"]["d_standard_not_subset_robust"]),
            )
        )

    lines.extend(
        [
            "",
            "## Monte Carlo Summary",
            "",
            "| Scenario | Cutoff | S truth | R truth | R feasible | S share | R share | Empty S | Empty R | Jaccard | d_S_not_subset_R | Warning |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in payload["monte_carlo_summary"]:
        lines.append(
            "| {scenario} | {cutoff} | {s_truth} | {r_truth} | {r_feas} | {s_share} | {r_share} | {s_empty} | {r_empty} | {jac} | {div} | {warn} |".format(
                scenario=row["label"],
                cutoff=convention_labels[row["cutoff_convention"]],
                s_truth=fmt(row["standard_dw"]["truth_in_rate"]),
                r_truth=fmt(row["robust_dw"]["truth_in_rate"]),
                r_feas=fmt(row["robust_dw"]["truth_feasible_rate"]),
                s_share=fmt(row["standard_dw"]["mean_accepted_share"]),
                r_share=fmt(row["robust_dw"]["mean_accepted_share"]),
                s_empty=fmt(row["standard_dw"]["empty_rate"]),
                r_empty=fmt(row["robust_dw"]["empty_rate"]),
                jac=fmt(row["overlap"]["mean_jaccard"]),
                div=fmt(row["overlap"]["mean_d_standard_not_subset_robust"]),
                warn=fmt(row["overlap"]["warning_rate"]),
            )
        )

    high_chi = summary_lookup[("high_noise", "chi_square_90")]
    weak_chi = summary_lookup[("weak_moments", "chi_square_90")]
    gaussian_chi = summary_lookup[("gaussian_shocks", "chi_square_90")]
    high_oracle = summary_lookup[("high_noise", "scenario_truth_repeated_90")]
    lines.extend(
        [
            "",
            "## Reading",
            "",
            "- Under the primary chi-square convention, high Gaussian noise keeps the standard-DW truth-in rate at "
            f"{fmt(high_chi['standard_dw']['truth_in_rate'])} and the variance-ratio robust truth-in rate at "
            f"{fmt(high_chi['robust_dw']['truth_in_rate'])}.",
            "- The high-noise robust truth-feasible rate is "
            f"{fmt(high_chi['robust_dw']['truth_feasible_rate'])}. This records the finite-sample cost of the hard covariance-decomposition screen separately from the higher-cumulant J cutoff.",
            "- With scenario-truth calibration, the high-noise standard-DW accepted share rises to "
            f"{fmt(high_oracle['standard_dw']['mean_accepted_share'])}. That is a calibration-cost diagnostic, not an application-ready correction.",
            "- Weak and Gaussian structural-shock scenarios remain limitation cases. Under the primary chi-square convention, robust accepted shares are "
            f"{fmt(weak_chi['robust_dw']['mean_accepted_share'])} and "
            f"{fmt(gaussian_chi['robust_dw']['mean_accepted_share'])}, respectively.",
            "- The skewed-residual-noise row violates the maintained Gaussian-noise route, so it remains a stress case even when finite-sample truth inclusion is high.",
            "",
            f"Machine-readable output: `{display_path(json_output)}`.",
        ]
    )
    note_output.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260607)
    parser.add_argument("--diagnostic-grid-points", type=int, default=61)
    parser.add_argument("--calibration-reps", type=int, default=60)
    parser.add_argument("--evaluation-reps", type=int, default=24)
    parser.add_argument("--grid-points", type=int, default=41)
    parser.add_argument("--json-output", default="", help="Optional JSON output path.")
    parser.add_argument("--note-output", default="", help="Optional Markdown note output path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    json_output = Path(args.json_output) if args.json_output else JSON_OUTPUT
    note_output = Path(args.note_output) if args.note_output else NOTE_OUTPUT
    json_output.parent.mkdir(parents=True, exist_ok=True)
    note_output.parent.mkdir(parents=True, exist_ok=True)
    fixed = fixed_grid_diagnostics(args.diagnostic_grid_points)
    truth_cutoffs, calibration_records = calibrate_truth_cutoffs(
        MC_SCENARIOS,
        args.seed,
        args.calibration_reps,
    )
    evaluation_records = evaluate_records(
        MC_SCENARIOS,
        truth_cutoffs,
        args.seed,
        args.evaluation_reps,
        args.grid_points,
    )
    payload = {
        "schema_version": 1,
        "description": "M52 source-correct validation and Monte Carlo evidence for the variance-ratio robust DW proposal.",
        "configuration": {
            "seed": args.seed,
            "diagnostic_grid_points": args.diagnostic_grid_points,
            "calibration_reps": args.calibration_reps,
            "evaluation_reps": args.evaluation_reps,
            "grid_points": args.grid_points,
            "grid_window": list(GRID_WINDOW),
            "true_B0": base.TRUE_MATRIX.tolist(),
            "true_b12": base.TRUE_B12,
            "true_b21": base.TRUE_B21,
            "robust_mode": ROBUST_MODE,
            "standard_dw_menu": base.STANDARD_DW_MENU,
            "standard_dw_moments": [list(moment) for moment in base.MOMENTS_DW],
            "primary_cutoff_convention": "chi_square_90",
            "chi_square_cutoffs": {
                "standard_dw": base.standard_dw_cutoff(),
                "standard_covariance": base.CHI2_90_DF1,
                "robust_dw": base.robust_mode_cutoff(ROBUST_MODE),
            },
        },
        "figure_scenarios": [scenario.__dict__ for scenario in FIGURE_SCENARIOS],
        "monte_carlo_scenarios": [scenario.__dict__ for scenario in MC_SCENARIOS],
        "fixed_grid_diagnostics": fixed,
        "truth_cutoffs": truth_cutoffs,
        "calibration_records": calibration_records,
        "evaluation_records": evaluation_records,
        "monte_carlo_summary": summarize(evaluation_records),
    }
    json_output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    write_note(payload, note_output, json_output)
    print(f"Wrote {display_path(json_output)}")
    print(f"Wrote {display_path(note_output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
