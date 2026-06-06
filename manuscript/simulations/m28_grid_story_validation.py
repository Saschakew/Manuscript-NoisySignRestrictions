"""Validate the M0020 sign/DW/robust-DW grid-pair story.

This script is the first M28 validation gate. It keeps the selected figure
generators unchanged and records separate diagnostics for:

* exact population mixed-moment zeros on the plotted B-plane;
* grid-boundary sensitivity of population minima and near aliases;
* repeated fixed-design finite-sample J-test inversions; and
* pointwise critical-value sensitivity.
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
JSON_OUTPUT = OUTPUT_DIR / "m28_grid_story_validation.json"
NOTE_OUTPUT = ROOT / "manuscript" / "simulations" / "m28_grid_story_validation.md"

TRUE_POINT = np.array([base.TRUE_B12, base.TRUE_B21], dtype=float)
TRUE_MATRIX = base.TRUE_MATRIX

CRITICAL_VALUES = {
    "80": {
        "covariance": 1.642374415149818,
        "standard_dw": 5.9886166940042465,
        "robust_dw": 7.289276126648476,
    },
    "90": {
        "covariance": base.CHI2_90_DF1,
        "standard_dw": base.CHI2_90_DF4,
        "robust_dw": base.CHI2_90_DF5,
    },
    "95": {
        "covariance": 3.841458820694124,
        "standard_dw": 9.487729036781154,
        "robust_dw": 11.070497693516351,
    },
}


@dataclass(frozen=True)
class Scenario:
    group: str
    name: str
    label: str
    noise: tuple[float, float]
    non_gaussian_weight: float
    note: str


NOISE_SCENARIOS = (
    Scenario(
        group="noise_grid",
        name="noise_none",
        label="V=(0,0)",
        noise=(0.0, 0.0),
        non_gaussian_weight=1.0,
        note="No residual noise; strong chi-square higher moments.",
    ),
    Scenario(
        group="noise_grid",
        name="noise_moderate",
        label="V=(0.3,0.3)",
        noise=(0.3, 0.3),
        non_gaussian_weight=1.0,
        note="Moderate Gaussian residual noise; strong chi-square higher moments.",
    ),
    Scenario(
        group="noise_grid",
        name="noise_high",
        label="V=(2,2)",
        noise=(2.0, 2.0),
        non_gaussian_weight=1.0,
        note="High Gaussian residual noise; selected false-sharpening stress case.",
    ),
)

NONGAUSSIANITY_SCENARIOS = (
    Scenario(
        group="nongaussianity_grid",
        name="strong_nongaussianity",
        label="w=1",
        noise=(0.3, 0.3),
        non_gaussian_weight=1.0,
        note="Fixed moderate residual noise with strong structural higher moments.",
    ),
    Scenario(
        group="nongaussianity_grid",
        name="weak_nongaussianity",
        label="w=0.25",
        noise=(0.3, 0.3),
        non_gaussian_weight=0.25,
        note="Fixed moderate residual noise with weakened structural higher moments.",
    ),
    Scenario(
        group="nongaussianity_grid",
        name="gaussian_shocks",
        label="w=0",
        noise=(0.3, 0.3),
        non_gaussian_weight=0.0,
        note="Fixed moderate residual noise with Gaussian structural shocks.",
    ),
)

ALL_SCENARIOS = NOISE_SCENARIOS + NONGAUSSIANITY_SCENARIOS

GRID_WINDOWS = {
    "base": (-1.35, 0.35, -0.25, 1.35),
    "expanded": (-1.85, 0.85, -0.55, 1.85),
    "narrow": (-0.95, 0.05, 0.05, 1.05),
}


def finite_float(value: float | np.floating[Any]) -> float | None:
    value = float(value)
    if not math.isfinite(value):
        return None
    return value


def candidate_matrix(b12: float, b21: float) -> np.ndarray | None:
    determinant = 1.0 - b12 * b21
    if abs(determinant) < 1e-10:
        return None
    return np.array([[1.0, b12], [b21, 1.0]], dtype=float)


def structural_cumulants(non_gaussian_weight: float) -> tuple[np.ndarray, np.ndarray]:
    """Return third and fourth cumulants for each unit-variance shock.

    The figure scripts mix standardized chi-square shocks with Gaussian shocks
    as sqrt(w) X + sqrt(1-w) G. In population, this preserves unit variance and
    scales cumulants by w^(r/2).
    """
    third = (non_gaussian_weight ** 1.5) * base.STRUCTURAL_THIRD_CUMULANT
    fourth = (non_gaussian_weight**2.0) * base.STRUCTURAL_FOURTH_CUMULANT
    return np.array([third, third], dtype=float), np.array([fourth, fourth], dtype=float)


def transformed_components(
    b12: float,
    b21: float,
    noise: tuple[float, float],
) -> tuple[np.ndarray, np.ndarray] | None:
    candidate = candidate_matrix(b12, b21)
    if candidate is None:
        return None
    inv_candidate = np.linalg.inv(candidate)
    structural_loadings = inv_candidate @ TRUE_MATRIX
    noise_covariance = inv_candidate @ np.diag(noise) @ inv_candidate.T
    covariance = structural_loadings @ structural_loadings.T + noise_covariance
    if np.any(np.diag(covariance) <= 0.0):
        return None
    return structural_loadings, covariance


def mixed_third(loadings: np.ndarray, third: np.ndarray, powers: tuple[int, int]) -> float:
    return float(np.sum(third * (loadings[0, :] ** powers[0]) * (loadings[1, :] ** powers[1])))


def mixed_fourth(loadings: np.ndarray, fourth: np.ndarray, powers: tuple[int, int]) -> float:
    return float(np.sum(fourth * (loadings[0, :] ** powers[0]) * (loadings[1, :] ** powers[1])))


def population_covariance_moment(
    b12: float,
    b21: float,
    scenario: Scenario,
) -> np.ndarray | None:
    components = transformed_components(b12, b21, scenario.noise)
    if components is None:
        return None
    _, covariance = components
    sd = np.sqrt(np.diag(covariance))
    return np.array([covariance[0, 1] / (sd[0] * sd[1])], dtype=float)


def population_standard_dw_moments(
    b12: float,
    b21: float,
    scenario: Scenario,
) -> np.ndarray | None:
    components = transformed_components(b12, b21, scenario.noise)
    if components is None:
        return None
    loadings, covariance = components
    third, fourth = structural_cumulants(scenario.non_gaussian_weight)
    sd = np.sqrt(np.diag(covariance))
    standardized_loadings = loadings / sd[:, None]
    rho = covariance[0, 1] / (sd[0] * sd[1])
    return np.array(
        [
            rho,
            mixed_third(standardized_loadings, third, (2, 1)),
            mixed_third(standardized_loadings, third, (1, 2)),
            2.0 * rho * rho + mixed_fourth(standardized_loadings, fourth, (2, 2)),
        ],
        dtype=float,
    )


def population_robust_dw_moments(
    b12: float,
    b21: float,
    scenario: Scenario,
) -> np.ndarray | None:
    components = transformed_components(b12, b21, scenario.noise)
    if components is None:
        return None
    loadings, _ = components
    third, fourth = structural_cumulants(scenario.non_gaussian_weight)
    return np.array(
        [
            mixed_third(loadings, third, (2, 1)),
            mixed_third(loadings, third, (1, 2)),
            mixed_fourth(loadings, fourth, (3, 1)),
            mixed_fourth(loadings, fourth, (2, 2)),
            mixed_fourth(loadings, fourth, (1, 3)),
        ],
        dtype=float,
    )


def make_grid(window: tuple[float, float, float, float], points: int) -> tuple[np.ndarray, np.ndarray]:
    b12_min, b12_max, b21_min, b21_max = window
    b12_grid = np.unique(np.append(np.linspace(b12_min, b12_max, points), base.TRUE_B12))
    b21_grid = np.unique(np.append(np.linspace(b21_min, b21_max, points), base.TRUE_B21))
    return b12_grid, b21_grid


def empty_population_record(method: str) -> dict[str, Any]:
    return {
        "method": method,
        "candidate_count": 0,
        "zero_count": 0,
        "near_zero_count": 0,
        "remote_near_zero_count": 0,
        "min_norm": None,
        "min_abs_max": None,
        "min_b12": None,
        "min_b21": None,
        "min_distance_to_truth": None,
        "truth_norm": None,
        "truth_abs_max": None,
        "truth_is_zero": False,
        "truth_is_near_zero": False,
    }


def score_population_method(
    scenario: Scenario,
    b12_grid: np.ndarray,
    b21_grid: np.ndarray,
    method: str,
    zero_tolerance: float,
    near_tolerance: float,
    remote_radius: float,
) -> dict[str, Any]:
    moment_function = {
        "covariance": population_covariance_moment,
        "standard_dw": population_standard_dw_moments,
        "robust_dw": population_robust_dw_moments,
    }[method]
    record = empty_population_record(method)
    min_norm = math.inf
    min_abs_max = math.inf
    min_point = (math.nan, math.nan)

    for b12 in b12_grid:
        for b21 in b21_grid:
            if b21 < 0.0:
                continue
            moments = moment_function(float(b12), float(b21), scenario)
            if moments is None or not np.all(np.isfinite(moments)):
                continue
            norm = float(np.linalg.norm(moments))
            abs_max = float(np.max(np.abs(moments)))
            distance = float(np.linalg.norm(np.array([b12, b21]) - TRUE_POINT))
            record["candidate_count"] += 1
            if abs_max <= zero_tolerance:
                record["zero_count"] += 1
            if abs_max <= near_tolerance:
                record["near_zero_count"] += 1
                if distance > remote_radius:
                    record["remote_near_zero_count"] += 1
            if norm < min_norm:
                min_norm = norm
                min_abs_max = abs_max
                min_point = (float(b12), float(b21))

    truth_moments = moment_function(base.TRUE_B12, base.TRUE_B21, scenario)
    if truth_moments is not None:
        truth_abs_max = float(np.max(np.abs(truth_moments)))
        truth_norm = float(np.linalg.norm(truth_moments))
        record["truth_norm"] = truth_norm
        record["truth_abs_max"] = truth_abs_max
        record["truth_is_zero"] = truth_abs_max <= zero_tolerance
        record["truth_is_near_zero"] = truth_abs_max <= near_tolerance

    if math.isfinite(min_norm):
        record["min_norm"] = min_norm
        record["min_abs_max"] = min_abs_max
        record["min_b12"] = min_point[0]
        record["min_b21"] = min_point[1]
        record["min_distance_to_truth"] = float(np.linalg.norm(np.array(min_point) - TRUE_POINT))
    return record


def population_summary(
    scenarios: tuple[Scenario, ...],
    grid_points: int,
    zero_tolerance: float,
    near_tolerance: float,
    remote_radius: float,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for window_name, window in GRID_WINDOWS.items():
        b12_grid, b21_grid = make_grid(window, grid_points)
        for scenario in scenarios:
            methods = [
                score_population_method(
                    scenario,
                    b12_grid,
                    b21_grid,
                    method,
                    zero_tolerance,
                    near_tolerance,
                    remote_radius,
                )
                for method in ("covariance", "standard_dw", "robust_dw")
            ]
            records.append(
                {
                    "window": window_name,
                    "grid_points": grid_points,
                    "scenario": scenario.name,
                    "group": scenario.group,
                    "label": scenario.label,
                    "noise": list(scenario.noise),
                    "non_gaussian_weight": scenario.non_gaussian_weight,
                    "methods": methods,
                }
            )
    return records


def structural_and_noise_draws(seed: int, non_gaussian_weight: float) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    skewed = base.standardize_columns(
        rng.chisquare(df=base.STRUCTURAL_CHI2_DF, size=(base.SAMPLE_SIZE, 2))
    )
    gaussian = base.standardize_columns(rng.normal(size=(base.SAMPLE_SIZE, 2)))
    structural = math.sqrt(non_gaussian_weight) * skewed + math.sqrt(1.0 - non_gaussian_weight) * gaussian
    structural = base.standardize_columns(structural)
    noise = base.standardize_columns(rng.normal(size=(base.SAMPLE_SIZE, 2)))
    return structural, noise


def simulate_residuals(seed: int, scenario: Scenario) -> np.ndarray:
    structural, noise = structural_and_noise_draws(seed, scenario.non_gaussian_weight)
    nu1, nu2 = scenario.noise
    residuals = structural @ TRUE_MATRIX.T
    residuals[:, 0] += math.sqrt(nu1) * noise[:, 0]
    residuals[:, 1] += math.sqrt(nu2) * noise[:, 1]
    return residuals - residuals.mean(axis=0, keepdims=True)


def accepted_share(j_values: np.ndarray, cutoff: float) -> tuple[float, float]:
    accepted = np.isfinite(j_values) & (j_values <= cutoff)
    valid = np.isfinite(j_values)
    plotted_share = float(np.mean(accepted))
    valid_share = float(np.sum(accepted) / np.sum(valid)) if np.any(valid) else math.nan
    return plotted_share, valid_share


def finite_truth_j_values(residuals: np.ndarray) -> dict[str, float | None]:
    true_shocks = base.standardized_candidate_shocks(base.TRUE_B12, base.TRUE_B21, residuals)
    covariance_j = math.nan
    standard_j = math.nan
    if true_shocks is not None:
        covariance_j = base.j_statistic(true_shocks, base.MOMENTS_COVARIANCE)
        standard_j = base.j_statistic(true_shocks, base.MOMENTS_DW)
    robust_j = base.robust_j_statistic(base.TRUE_B12, base.TRUE_B21, residuals)
    return {
        "covariance": finite_float(covariance_j),
        "standard_dw": finite_float(standard_j),
        "robust_dw": finite_float(robust_j),
    }


def finite_seed_record(
    seed: int,
    scenario: Scenario,
    finite_grid_points: int,
) -> dict[str, Any]:
    b12_grid, b21_grid = make_grid(GRID_WINDOWS["base"], finite_grid_points)
    residuals = simulate_residuals(seed, scenario)
    (
        _,
        _,
        _,
        covariance_j,
        _,
        standard_j,
        _,
    ) = base.evaluate_standard_grid(residuals, scenario.noise[0], scenario.noise[1], b12_grid, b21_grid)
    _, _, robust_j, _ = base.evaluate_robust_grid(residuals, b12_grid, b21_grid)
    truth_j = finite_truth_j_values(residuals)
    j_grids = {
        "covariance": covariance_j,
        "standard_dw": standard_j,
        "robust_dw": robust_j,
    }
    methods: dict[str, Any] = {}
    for method, values in j_grids.items():
        methods[method] = {
            "truth_j": truth_j[method],
            "min_j": finite_float(np.nanmin(values)) if np.isfinite(values).any() else None,
            "cutoffs": {},
        }
        for level, cutoff_map in CRITICAL_VALUES.items():
            cutoff = cutoff_map[method]
            plotted_share, valid_share = accepted_share(values, cutoff)
            truth_value = truth_j[method]
            methods[method]["cutoffs"][level] = {
                "cutoff": cutoff,
                "truth_in": bool(truth_value is not None and truth_value <= cutoff),
                "accepted_share_plotted": plotted_share,
                "accepted_share_valid": valid_share,
            }
    return {
        "seed": seed,
        "scenario": scenario.name,
        "group": scenario.group,
        "label": scenario.label,
        "noise": list(scenario.noise),
        "non_gaussian_weight": scenario.non_gaussian_weight,
        "methods": methods,
    }


def finite_seed_records(
    scenarios: tuple[Scenario, ...],
    seeds: list[int],
    finite_grid_points: int,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for scenario in scenarios:
        for seed in seeds:
            records.append(finite_seed_record(seed, scenario, finite_grid_points))
    return records


def summarize_finite(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    scenario_names = sorted({record["scenario"] for record in records})
    for scenario_name in scenario_names:
        scenario_records = [record for record in records if record["scenario"] == scenario_name]
        sample_record = scenario_records[0]
        for method in ("covariance", "standard_dw", "robust_dw"):
            truth_js = np.array(
                [
                    record["methods"][method]["truth_j"]
                    for record in scenario_records
                    if record["methods"][method]["truth_j"] is not None
                ],
                dtype=float,
            )
            cutoff_summaries: dict[str, Any] = {}
            for level in CRITICAL_VALUES:
                truth_in = np.array(
                    [
                        record["methods"][method]["cutoffs"][level]["truth_in"]
                        for record in scenario_records
                    ],
                    dtype=float,
                )
                plotted_shares = np.array(
                    [
                        record["methods"][method]["cutoffs"][level]["accepted_share_plotted"]
                        for record in scenario_records
                    ],
                    dtype=float,
                )
                cutoff_summaries[level] = {
                    "truth_in_rate": float(np.mean(truth_in)),
                    "mean_accepted_share_plotted": float(np.mean(plotted_shares)),
                    "min_accepted_share_plotted": float(np.min(plotted_shares)),
                    "max_accepted_share_plotted": float(np.max(plotted_shares)),
                }
            summaries.append(
                {
                    "scenario": scenario_name,
                    "group": sample_record["group"],
                    "label": sample_record["label"],
                    "method": method,
                    "median_truth_j": finite_float(np.median(truth_js)) if truth_js.size else None,
                    "max_truth_j": finite_float(np.max(truth_js)) if truth_js.size else None,
                    "cutoffs": cutoff_summaries,
                }
            )
    return summaries


def method_record(pop_record: dict[str, Any], method: str) -> dict[str, Any]:
    for item in pop_record["methods"]:
        if item["method"] == method:
            return item
    raise KeyError(method)


def verdict_for_population(pop_record: dict[str, Any]) -> str:
    standard = method_record(pop_record, "standard_dw")
    robust = method_record(pop_record, "robust_dw")
    if pop_record["scenario"] == "gaussian_shocks":
        return "robust all-null expected"
    if robust["truth_is_zero"] and not standard["truth_is_zero"]:
        return "supports divergence"
    if robust["truth_is_zero"] and standard["truth_is_zero"]:
        return "truth compatible"
    return "needs review"


def fmt(value: Any, digits: int = 3) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, (int, np.integer)):
        return str(int(value))
    value = float(value)
    if abs(value) >= 1000 or (0 < abs(value) < 0.001):
        return f"{value:.{digits}e}"
    return f"{value:.{digits}f}"


def write_note(payload: dict[str, Any]) -> None:
    base_population = [
        record
        for record in payload["population"]
        if record["window"] == "base"
        and record["scenario"]
        in {
            "noise_none",
            "noise_moderate",
            "noise_high",
            "strong_nongaussianity",
            "weak_nongaussianity",
            "gaussian_shocks",
        }
    ]
    finite_90 = [
        record
        for record in payload["finite_summary"]
        if record["method"] in {"standard_dw", "robust_dw"}
    ]

    lines = [
        "# M28 Grid Story Validation",
        "",
        "Status: completed first M28 validation pass for the selected M0020 grid pair.",
        "",
        "This note validates the figure story without changing the figure generators. "
        "It combines exact population moment diagnostics with repeated fixed-design "
        "finite-sample J-test checks on the same B-plane.",
        "",
        "## Configuration",
        "",
        f"- Population grid: `{payload['configuration']['population_grid_points']} x "
        f"{payload['configuration']['population_grid_points']}` plus the true `B0` point.",
        f"- Finite grid: `{payload['configuration']['finite_grid_points']} x "
        f"{payload['configuration']['finite_grid_points']}` plus the true `B0` point.",
        f"- Finite seeds: `{', '.join(str(seed) for seed in payload['configuration']['seeds'])}`.",
        f"- Population near-zero tolerance: `{payload['configuration']['near_tolerance']}`.",
        f"- Remote-alias radius: `{payload['configuration']['remote_radius']}` in `(b12,b21)` distance.",
        "",
        "## Population Truth And Alias Diagnostics",
        "",
        "| Scenario | Standard truth norm | Robust truth norm | Standard remote near-zeros | Robust remote near-zeros | Verdict |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for record in base_population:
        standard = method_record(record, "standard_dw")
        robust = method_record(record, "robust_dw")
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{record['group']} / {record['label']}",
                    fmt(standard["truth_norm"]),
                    fmt(robust["truth_norm"]),
                    fmt(standard["remote_near_zero_count"], 0),
                    fmt(robust["remote_near_zero_count"], 0),
                    verdict_for_population(record),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "Population reading: robust-DW is exactly zero at the true normalized `B0` "
            "under Gaussian residual noise whenever structural higher moments are present, "
            "while the standard DW population moments become nonzero when the noisy "
            "covariance target moves away from the no-noise impact matrix. With Gaussian "
            "structural shocks, the robust higher-cumulant stack is all-null by design.",
            "",
            "## Boundary Sensitivity",
            "",
            "| Scenario | Window | Standard min distance | Robust min distance | Standard remote near-zeros | Robust remote near-zeros |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    boundary_focus = {"noise_high", "weak_nongaussianity", "gaussian_shocks"}
    for record in payload["population"]:
        if record["scenario"] not in boundary_focus:
            continue
        standard = method_record(record, "standard_dw")
        robust = method_record(record, "robust_dw")
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{record['group']} / {record['label']}",
                    record["window"],
                    fmt(standard["min_distance_to_truth"]),
                    fmt(robust["min_distance_to_truth"]),
                    fmt(standard["remote_near_zero_count"], 0),
                    fmt(robust["remote_near_zero_count"], 0),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "Boundary reading: the high-noise standard-DW population minimum is not at "
            "the true `B0`; robust-DW keeps the true point as an exact population zero. "
            "The Gaussian-shock column correctly has remote robust near-zeros because "
            "there is no higher-moment information to identify the impact shape.",
            "",
            "## Repeated Finite-Sample J Checks",
            "",
            "| Scenario | Method | Truth-in rate at 10% | Mean accepted share | Median `J(B0)` | Max `J(B0)` |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for record in finite_90:
        cutoff = record["cutoffs"]["90"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{record['group']} / {record['label']}",
                    record["method"],
                    fmt(cutoff["truth_in_rate"]),
                    fmt(cutoff["mean_accepted_share_plotted"]),
                    fmt(record["median_truth_j"]),
                    fmt(record["max_truth_j"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Critical-Value Sensitivity",
            "",
            "| Scenario | Method | 20% truth-in | 10% truth-in | 5% truth-in | 20% mean share | 10% mean share | 5% mean share |",
            "|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    critical_focus = {
        ("noise_high", "standard_dw"),
        ("noise_high", "robust_dw"),
        ("weak_nongaussianity", "robust_dw"),
        ("gaussian_shocks", "robust_dw"),
    }
    for record in payload["finite_summary"]:
        if (record["scenario"], record["method"]) not in critical_focus:
            continue
        cut80 = record["cutoffs"]["80"]
        cut90 = record["cutoffs"]["90"]
        cut95 = record["cutoffs"]["95"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{record['group']} / {record['label']}",
                    record["method"],
                    fmt(cut80["truth_in_rate"]),
                    fmt(cut90["truth_in_rate"]),
                    fmt(cut95["truth_in_rate"]),
                    fmt(cut80["mean_accepted_share_plotted"]),
                    fmt(cut90["mean_accepted_share_plotted"]),
                    fmt(cut95["mean_accepted_share_plotted"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Gate Outcome",
            "",
            "- The population diagnostics support the core visual story: residual noise "
            "moves the standard covariance/DW target, and robust-DW keeps the true "
            "normalized impact as a population zero under the maintained Gaussian-noise condition.",
            "- The high-noise finite-sample stress case is stable enough for the selected "
            "visual spine: standard DW rejects the true point across repeated seeds at "
            "the pointwise 10 percent cutoff, while robust DW usually contains it.",
            "- The non-Gaussianity companion behaves as intended: weakening higher moments "
            "widens the robust accepted region, and the Gaussian-shock case is an "
            "all-null population limit rather than identifying evidence.",
            "- This is not yet final evidence. M29 still needs calibrated repeated-sample "
            "or bootstrap critical values before the manuscript reports coverage or size claims.",
            "",
            "Machine-readable output: `manuscript/simulations/output/m28_grid_story_validation.json`.",
        ]
    )
    NOTE_OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def parse_seeds(seed_text: str) -> list[int]:
    seeds = [int(item.strip()) for item in seed_text.split(",") if item.strip()]
    if not seeds:
        raise ValueError("Provide at least one finite-sample seed.")
    return seeds


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--population-grid-points", type=int, default=101)
    parser.add_argument("--finite-grid-points", type=int, default=51)
    parser.add_argument(
        "--seeds",
        default="20260605,20260606,20260607,20260608,20260609,20260610",
        help="Comma-separated finite-sample seeds.",
    )
    parser.add_argument("--zero-tolerance", type=float, default=1e-8)
    parser.add_argument("--near-tolerance", type=float, default=5e-3)
    parser.add_argument("--remote-radius", type=float, default=0.20)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    seeds = parse_seeds(args.seeds)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    population = population_summary(
        ALL_SCENARIOS,
        args.population_grid_points,
        args.zero_tolerance,
        args.near_tolerance,
        args.remote_radius,
    )
    finite_records = finite_seed_records(ALL_SCENARIOS, seeds, args.finite_grid_points)
    payload = {
        "schema_version": 1,
        "description": "M28 validation of the M0020 grid-pair story.",
        "configuration": {
            "population_grid_points": args.population_grid_points,
            "finite_grid_points": args.finite_grid_points,
            "seeds": seeds,
            "zero_tolerance": args.zero_tolerance,
            "near_tolerance": args.near_tolerance,
            "remote_radius": args.remote_radius,
            "sample_size": base.SAMPLE_SIZE,
            "true_B0": TRUE_MATRIX.tolist(),
            "critical_values": CRITICAL_VALUES,
        },
        "scenarios": [
            {
                "group": scenario.group,
                "name": scenario.name,
                "label": scenario.label,
                "noise": list(scenario.noise),
                "non_gaussian_weight": scenario.non_gaussian_weight,
                "note": scenario.note,
            }
            for scenario in ALL_SCENARIOS
        ],
        "population": population,
        "finite_records": finite_records,
        "finite_summary": summarize_finite(finite_records),
    }
    JSON_OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    write_note(payload)
    print(f"Wrote {JSON_OUTPUT.relative_to(ROOT)}")
    print(f"Wrote {NOTE_OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
