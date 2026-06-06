"""First calibrated Monte Carlo pass for the M29 evidence gate.

This script keeps the M0020/M28 B-plane design and reports the M27 metric
bundle under three pointwise critical-value conventions:

* the chi-square 90 percent guide used in the figures;
* a no-noise repeated-sample 90 percent calibration applied to all scenarios;
* an oracle scenario-specific truth calibration, used only as a diagnostic
  for how much the cutoff must move to keep the true B0 in repeated samples.

The output is a first evidence pass, not the final replication package.
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
JSON_OUTPUT = OUTPUT_DIR / "m29_calibrated_monte_carlo.json"
NOTE_OUTPUT = ROOT / "manuscript" / "simulations" / "m29_calibrated_monte_carlo.md"

GRID_WINDOW = (-1.35, 0.35, -0.25, 1.35)


@dataclass(frozen=True)
class Scenario:
    name: str
    label: str
    noise: tuple[float, float]
    non_gaussian_weight: float
    residual_noise: str
    note: str


SCENARIOS = (
    Scenario(
        name="no_noise",
        label="No noise, strong moments",
        noise=(0.0, 0.0),
        non_gaussian_weight=1.0,
        residual_noise="gaussian",
        note="Sanity case for standard-DW and robust-DW agreement.",
    ),
    Scenario(
        name="moderate_noise",
        label="Moderate Gaussian noise",
        noise=(0.3, 0.3),
        non_gaussian_weight=1.0,
        residual_noise="gaussian",
        note="The M0020 moderate-noise column with informative higher moments.",
    ),
    Scenario(
        name="high_noise",
        label="High Gaussian noise",
        noise=(2.0, 2.0),
        non_gaussian_weight=1.0,
        residual_noise="gaussian",
        note="The M0020 stress column where standard DW rejects true B0 under chi-square guides.",
    ),
    Scenario(
        name="weak_moments",
        label="Weak structural higher moments",
        noise=(0.3, 0.3),
        non_gaussian_weight=0.25,
        residual_noise="gaussian",
        note="Companion-grid limitation case: robust DW should widen as higher moments weaken.",
    ),
    Scenario(
        name="gaussian_shocks",
        label="Gaussian structural shocks",
        noise=(0.3, 0.3),
        non_gaussian_weight=0.0,
        residual_noise="gaussian",
        note="All-null robust higher-cumulant population limit.",
    ),
    Scenario(
        name="skewed_residual_noise",
        label="Skewed residual noise",
        noise=(0.3, 0.3),
        non_gaussian_weight=1.0,
        residual_noise="skewed",
        note="Misspecified-noise stress case that violates the maintained Gaussian-noise route.",
    ),
)


def finite_float(value: float | np.floating[Any]) -> float | None:
    value = float(value)
    return value if math.isfinite(value) else None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260606)
    parser.add_argument("--sample-size", type=int, default=base.SAMPLE_SIZE)
    parser.add_argument("--calibration-reps", type=int, default=80)
    parser.add_argument("--evaluation-reps", type=int, default=24)
    parser.add_argument("--grid-points", type=int, default=41)
    return parser.parse_args()


def make_grid(points: int) -> tuple[np.ndarray, np.ndarray]:
    b12_min, b12_max, b21_min, b21_max = GRID_WINDOW
    b12_grid = np.unique(np.append(np.linspace(b12_min, b12_max, points), base.TRUE_B12))
    b21_grid = np.unique(np.append(np.linspace(b21_min, b21_max, points), base.TRUE_B21))
    return b12_grid, b21_grid


def seed_for(base_seed: int, block: int, scenario_index: int, rep: int) -> int:
    return int(base_seed + block * 1_000_000 + scenario_index * 10_000 + rep)


def structural_and_noise_draws(
    seed: int,
    sample_size: int,
    non_gaussian_weight: float,
    residual_noise: str,
) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    skewed = base.standardize_columns(
        rng.chisquare(df=base.STRUCTURAL_CHI2_DF, size=(sample_size, 2))
    )
    gaussian = base.standardize_columns(rng.normal(size=(sample_size, 2)))
    structural = math.sqrt(non_gaussian_weight) * skewed
    structural += math.sqrt(max(0.0, 1.0 - non_gaussian_weight)) * gaussian
    structural = base.standardize_columns(structural)

    if residual_noise == "gaussian":
        noise = rng.normal(size=(sample_size, 2))
    elif residual_noise == "skewed":
        noise = rng.chisquare(df=base.STRUCTURAL_CHI2_DF, size=(sample_size, 2))
    else:
        raise ValueError(f"unknown residual noise kind: {residual_noise}")
    return structural, base.standardize_columns(noise)


def simulate_residuals(seed: int, scenario: Scenario, sample_size: int) -> np.ndarray:
    structural, noise = structural_and_noise_draws(
        seed,
        sample_size,
        scenario.non_gaussian_weight,
        scenario.residual_noise,
    )
    residuals = structural @ base.TRUE_MATRIX.T
    residuals[:, 0] += math.sqrt(scenario.noise[0]) * noise[:, 0]
    residuals[:, 1] += math.sqrt(scenario.noise[1]) * noise[:, 1]
    return residuals - residuals.mean(axis=0, keepdims=True)


def truth_j_values(residuals: np.ndarray) -> dict[str, float | None]:
    standard_shocks = base.standardized_candidate_shocks(
        base.TRUE_B12,
        base.TRUE_B21,
        residuals,
    )
    standard = math.nan
    if standard_shocks is not None:
        standard = base.j_statistic(standard_shocks, base.MOMENTS_DW)
    robust = base.robust_j_statistic(base.TRUE_B12, base.TRUE_B21, residuals)
    return {"standard_dw": finite_float(standard), "robust_dw": finite_float(robust)}


def quantile_or_nan(values: list[float | None], probability: float) -> float:
    finite = np.array([value for value in values if value is not None], dtype=float)
    if finite.size == 0:
        return math.nan
    return float(np.quantile(finite, probability))


def calibrate_truth_cutoffs(
    scenarios: tuple[Scenario, ...],
    base_seed: int,
    sample_size: int,
    reps: int,
) -> tuple[dict[str, dict[str, float]], list[dict[str, Any]]]:
    cutoffs: dict[str, dict[str, float]] = {}
    records: list[dict[str, Any]] = []
    for scenario_index, scenario in enumerate(scenarios):
        truth_js: dict[str, list[float | None]] = {"standard_dw": [], "robust_dw": []}
        for rep in range(reps):
            seed = seed_for(base_seed, 1, scenario_index, rep)
            residuals = simulate_residuals(seed, scenario, sample_size)
            values = truth_j_values(residuals)
            for method, value in values.items():
                truth_js[method].append(value)
            records.append(
                {
                    "scenario": scenario.name,
                    "rep": rep,
                    "seed": seed,
                    "truth_j": values,
                }
            )
        cutoffs[scenario.name] = {
            method: quantile_or_nan(values, 0.90)
            for method, values in truth_js.items()
        }
    return cutoffs, records


def least_rejected_record(
    j_values: np.ndarray,
    b12_mesh: np.ndarray,
    b21_mesh: np.ndarray,
    chart_mask: np.ndarray,
) -> dict[str, float | None]:
    candidates = np.where(chart_mask & np.isfinite(j_values), j_values, np.nan)
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


def distance_to_set(
    accepted: np.ndarray,
    b12_mesh: np.ndarray,
    b21_mesh: np.ndarray,
) -> float | None:
    if not accepted.any():
        return None
    distances = np.hypot(b12_mesh[accepted] - base.TRUE_B12, b21_mesh[accepted] - base.TRUE_B21)
    return float(np.min(distances))


def set_metrics(
    standard_j: np.ndarray,
    robust_j: np.ndarray,
    b12_mesh: np.ndarray,
    b21_mesh: np.ndarray,
    standard_cutoff: float,
    robust_cutoff: float,
    truth_j: dict[str, float | None],
) -> dict[str, Any]:
    chart = np.isfinite(robust_j)
    chart_count = int(np.count_nonzero(chart))
    standard = chart & np.isfinite(standard_j) & (standard_j <= standard_cutoff)
    robust = chart & np.isfinite(robust_j) & (robust_j <= robust_cutoff)
    intersection = standard & robust
    union = standard | robust

    standard_count = int(np.count_nonzero(standard))
    robust_count = int(np.count_nonzero(robust))
    intersection_count = int(np.count_nonzero(intersection))
    union_count = int(np.count_nonzero(union))
    jaccard = intersection_count / union_count if union_count else None
    standard_contained = intersection_count / standard_count if standard_count else None
    robust_contained = intersection_count / robust_count if robust_count else None

    standard_truth_j = truth_j["standard_dw"]
    robust_truth_j = truth_j["robust_dw"]
    standard_truth_in = (
        standard_truth_j is not None and math.isfinite(standard_cutoff) and standard_truth_j <= standard_cutoff
    )
    robust_truth_in = (
        robust_truth_j is not None and math.isfinite(robust_cutoff) and robust_truth_j <= robust_cutoff
    )

    return {
        "grid_count": chart_count,
        "standard_dw": {
            "accepted_count": standard_count,
            "accepted_share": standard_count / chart_count if chart_count else None,
            "empty": standard_count == 0,
            "truth_in": standard_truth_in,
            "truth_j": standard_truth_j,
            "distance_to_accepted_set": distance_to_set(standard, b12_mesh, b21_mesh),
            "least_rejected": least_rejected_record(standard_j, b12_mesh, b21_mesh, chart),
        },
        "robust_dw": {
            "accepted_count": robust_count,
            "accepted_share": robust_count / chart_count if chart_count else None,
            "empty": robust_count == 0,
            "truth_in": robust_truth_in,
            "truth_j": robust_truth_j,
            "distance_to_accepted_set": distance_to_set(robust, b12_mesh, b21_mesh),
            "least_rejected": least_rejected_record(robust_j, b12_mesh, b21_mesh, chart),
        },
        "overlap": {
            "intersection_count": intersection_count,
            "union_count": union_count,
            "jaccard": jaccard,
            "q_standard_given_robust": standard_contained,
            "q_robust_given_standard": robust_contained,
            "d_standard_not_subset_robust": None
            if standard_contained is None
            else 1.0 - standard_contained,
        },
    }


def cutoff_catalog(
    truth_cutoffs: dict[str, dict[str, float]],
    scenario_name: str,
) -> list[dict[str, Any]]:
    no_noise_cutoffs = truth_cutoffs["no_noise"]
    scenario_cutoffs = truth_cutoffs[scenario_name]
    return [
        {
            "name": "chi_square_90",
            "label": "Chi-square 90%",
            "standard_dw": base.CHI2_90_DF4,
            "robust_dw": base.CHI2_90_DF5,
            "description": "Same pointwise guide used in the M0020 grid figures.",
        },
        {
            "name": "no_noise_repeated_90",
            "label": "No-noise repeated 90%",
            "standard_dw": no_noise_cutoffs["standard_dw"],
            "robust_dw": no_noise_cutoffs["robust_dw"],
            "description": "Finite-sample cutoff calibrated at true B0 in the no-noise strong-moment DGP and applied to every scenario.",
        },
        {
            "name": "scenario_truth_repeated_90",
            "label": "Scenario truth repeated 90%",
            "standard_dw": scenario_cutoffs["standard_dw"],
            "robust_dw": scenario_cutoffs["robust_dw"],
            "description": "Oracle scenario-specific true-B0 cutoff; diagnostic only, not application-feasible.",
        },
    ]


def evaluate_records(
    scenarios: tuple[Scenario, ...],
    truth_cutoffs: dict[str, dict[str, float]],
    base_seed: int,
    sample_size: int,
    reps: int,
    grid_points: int,
) -> list[dict[str, Any]]:
    b12_grid, b21_grid = make_grid(grid_points)
    records: list[dict[str, Any]] = []
    for scenario_index, scenario in enumerate(scenarios):
        for rep in range(reps):
            seed = seed_for(base_seed, 2, scenario_index, rep)
            residuals = simulate_residuals(seed, scenario, sample_size)
            (
                b12_mesh,
                b21_mesh,
                _correlation,
                _covariance_j,
                _covariance_accepted,
                standard_j,
                _standard_accepted,
            ) = base.evaluate_standard_grid(
                residuals,
                scenario.noise[0],
                scenario.noise[1],
                b12_grid,
                b21_grid,
            )
            _, _, robust_j, _ = base.evaluate_robust_grid(residuals, b12_grid, b21_grid)
            truth_j = truth_j_values(residuals)
            for convention in cutoff_catalog(truth_cutoffs, scenario.name):
                metrics = set_metrics(
                    standard_j,
                    robust_j,
                    b12_mesh,
                    b21_mesh,
                    convention["standard_dw"],
                    convention["robust_dw"],
                    truth_j,
                )
                records.append(
                    {
                        "scenario": scenario.name,
                        "cutoff_convention": convention["name"],
                        "rep": rep,
                        "seed": seed,
                        "cutoffs": {
                            "standard_dw": finite_float(convention["standard_dw"]),
                            "robust_dw": finite_float(convention["robust_dw"]),
                        },
                        "metrics": metrics,
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
    scenario_names = [scenario.name for scenario in SCENARIOS]
    convention_names = ["chi_square_90", "no_noise_repeated_90", "scenario_truth_repeated_90"]
    for scenario_name in scenario_names:
        for convention_name in convention_names:
            subset = [
                record
                for record in records
                if record["scenario"] == scenario_name
                and record["cutoff_convention"] == convention_name
            ]
            if not subset:
                continue
            first = subset[0]
            standard = [record["metrics"]["standard_dw"] for record in subset]
            robust = [record["metrics"]["robust_dw"] for record in subset]
            overlap = [record["metrics"]["overlap"] for record in subset]
            warning_values = [
                (
                    (not item["metrics"]["standard_dw"]["truth_in"])
                    and item["metrics"]["robust_dw"]["truth_in"]
                )
                or (
                    item["metrics"]["overlap"]["d_standard_not_subset_robust"] is not None
                    and item["metrics"]["overlap"]["d_standard_not_subset_robust"] >= 0.25
                    and item["metrics"]["standard_dw"]["accepted_share"] is not None
                    and item["metrics"]["standard_dw"]["accepted_share"] > 0.01
                )
                for item in subset
            ]
            rows.append(
                {
                    "scenario": scenario_name,
                    "cutoff_convention": convention_name,
                    "cutoffs": first["cutoffs"],
                    "standard_dw": {
                        "truth_in_rate": mean_optional([item["truth_in"] for item in standard]),
                        "empty_rate": mean_optional([item["empty"] for item in standard]),
                        "mean_accepted_share": mean_optional(
                            [item["accepted_share"] for item in standard]
                        ),
                        "median_truth_j": median_optional([item["truth_j"] for item in standard]),
                        "mean_distance_to_set": mean_optional(
                            [item["distance_to_accepted_set"] for item in standard]
                        ),
                        "mean_least_rejected_distance": mean_optional(
                            [item["least_rejected"]["distance"] for item in standard]
                        ),
                    },
                    "robust_dw": {
                        "truth_in_rate": mean_optional([item["truth_in"] for item in robust]),
                        "empty_rate": mean_optional([item["empty"] for item in robust]),
                        "mean_accepted_share": mean_optional(
                            [item["accepted_share"] for item in robust]
                        ),
                        "median_truth_j": median_optional([item["truth_j"] for item in robust]),
                        "mean_distance_to_set": mean_optional(
                            [item["distance_to_accepted_set"] for item in robust]
                        ),
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


def write_note(payload: dict[str, Any]) -> None:
    scenario_lookup = {scenario.name: scenario for scenario in SCENARIOS}
    convention_labels = {
        "chi_square_90": "chi-square",
        "no_noise_repeated_90": "no-noise repeated",
        "scenario_truth_repeated_90": "scenario truth",
    }
    summary_lookup = {
        (row["scenario"], row["cutoff_convention"]): row
        for row in payload["summary"]
    }
    lines: list[str] = [
        "# M29 Calibrated Monte Carlo First Pass",
        "",
        "Status: first calibrated finite-sample evidence pass for M29, not the final replication table.",
        "",
        "This pass keeps the M0020/M28 normalized B-plane and reports the M27 metric bundle under three critical-value conventions.",
        "",
        "## Configuration",
        "",
        f"- Calibration replications per scenario: `{payload['configuration']['calibration_reps']}`",
        f"- Evaluation replications per scenario: `{payload['configuration']['evaluation_reps']}`",
        f"- Sample size: `{payload['configuration']['sample_size']}`",
        f"- Evaluation grid: `{payload['configuration']['grid_points']} x {payload['configuration']['grid_points']}` plus the true `B0` point.",
        f"- True normalized B0: `b12={base.TRUE_B12:g}`, `b21={base.TRUE_B21:g}`.",
        "",
        "Critical-value conventions:",
        "",
        "- `chi_square_90`: the pointwise 90 percent chi-square guide used in the M0020 figures.",
        "- `no_noise_repeated_90`: repeated-sample true-`B0` calibration in the no-noise strong-moment DGP, then applied to every scenario.",
        "- `scenario_truth_repeated_90`: oracle repeated-sample true-`B0` calibration inside each scenario. This is diagnostic only because applications do not know the true `B0` or DGP.",
        "",
        "## Scenario Cutoffs",
        "",
        "| Scenario | Standard scenario cutoff | Robust scenario cutoff | Note |",
        "|---|---:|---:|---|",
    ]
    for scenario in SCENARIOS:
        cutoffs = payload["truth_cutoffs"][scenario.name]
        lines.append(
            "| {label} | {std} | {rob} | {note} |".format(
                label=scenario.label,
                std=fmt(cutoffs["standard_dw"]),
                rob=fmt(cutoffs["robust_dw"]),
                note=scenario.note,
            )
        )

    lines.extend(
        [
            "",
            "## Monte Carlo Summary",
            "",
            "| Scenario | Cutoff | S truth | R truth | S share | R share | Empty S | Empty R | Jaccard | d_S_not_subset_R | Warning |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in payload["summary"]:
        scenario = scenario_lookup[row["scenario"]]
        lines.append(
            "| {scenario} | {cutoff} | {s_truth} | {r_truth} | {s_share} | {r_share} | {s_empty} | {r_empty} | {jaccard} | {divergence} | {warning} |".format(
                scenario=scenario.label,
                cutoff=convention_labels[row["cutoff_convention"]],
                s_truth=fmt(row["standard_dw"]["truth_in_rate"]),
                r_truth=fmt(row["robust_dw"]["truth_in_rate"]),
                s_share=fmt(row["standard_dw"]["mean_accepted_share"]),
                r_share=fmt(row["robust_dw"]["mean_accepted_share"]),
                s_empty=fmt(row["standard_dw"]["empty_rate"]),
                r_empty=fmt(row["robust_dw"]["empty_rate"]),
                jaccard=fmt(row["overlap"]["mean_jaccard"]),
                divergence=fmt(row["overlap"]["mean_d_standard_not_subset_robust"]),
                warning=fmt(row["overlap"]["warning_rate"]),
            )
        )

    high_chi = summary_lookup[("high_noise", "chi_square_90")]
    high_null = summary_lookup[("high_noise", "no_noise_repeated_90")]
    high_oracle = summary_lookup[("high_noise", "scenario_truth_repeated_90")]
    weak_null = summary_lookup[("weak_moments", "no_noise_repeated_90")]
    gaussian_null = summary_lookup[("gaussian_shocks", "no_noise_repeated_90")]
    skewed_null = summary_lookup[("skewed_residual_noise", "no_noise_repeated_90")]

    lines.extend(
        [
            "",
            "## First-Pass Outcome",
            "",
            "- In the high Gaussian-noise stress case, standard DW includes true `B0` in only "
            f"{fmt(high_chi['standard_dw']['truth_in_rate'])} of evaluation samples under the "
            "chi-square guide and "
            f"{fmt(high_null['standard_dw']['truth_in_rate'])} under the no-noise repeated calibration; "
            "robust DW includes true `B0` in "
            f"{fmt(high_chi['robust_dw']['truth_in_rate'])} and "
            f"{fmt(high_null['robust_dw']['truth_in_rate'])}, respectively.",
            "- The high-noise oracle standard-DW cutoff is "
            f"`{fmt(payload['truth_cutoffs']['high_noise']['standard_dw'])}`, compared with "
            f"`{fmt(payload['truth_cutoffs']['no_noise']['standard_dw'])}` under no noise. "
            "That is the calibration cost of forcing the misspecified standard-DW statistic to cover the truth.",
            "- The same high-noise oracle cutoff raises the standard-DW accepted share to "
            f"{fmt(high_oracle['standard_dw']['mean_accepted_share'])}, so the apparent precision is not free once the cutoff is truth-calibrated.",
            "- Weak and Gaussian structural-shock cases keep robust DW wide under the no-noise repeated cutoff: mean robust shares are "
            f"{fmt(weak_null['robust_dw']['mean_accepted_share'])} and "
            f"{fmt(gaussian_null['robust_dw']['mean_accepted_share'])}. This supports the limitation story rather than a sharp identification claim.",
            "- The skewed-residual-noise stress case has high robust truth inclusion in this first pass, but the maintained Gaussian-noise interpretation is invalid there; it remains a stress case, not a robustness guarantee.",
            "",
            "## Reading",
            "",
            "- The no-noise repeated calibration is the cleanest first size check for the maintained no-noise benchmark. It should preserve the no-noise sanity case while still exposing residual-noise divergence.",
            "- The high-noise Gaussian case is the main stress case from the visual spine. Under the figure-style and no-noise-calibrated cutoffs, standard DW should reject true `B0` more often than robust DW.",
            "- The scenario-specific truth calibration is an oracle diagnostic. When its standard-DW cutoff is much larger than the no-noise cutoff, the standard DW statistic is paying a calibration cost under residual noise rather than delivering free precision.",
            "- The Gaussian-shock case is expected to make robust DW wide or weak because the higher-cumulant signal disappears.",
            "- The skewed-residual-noise case is a maintained-assumption stress test. Robust DW is not expected to retain the clean Gaussian-noise interpretation there.",
            "",
            "Machine-readable output: `manuscript/simulations/output/m29_calibrated_monte_carlo.json`.",
        ]
    )
    NOTE_OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    args = parse_args()
    truth_cutoffs, calibration_records = calibrate_truth_cutoffs(
        SCENARIOS,
        args.seed,
        args.sample_size,
        args.calibration_reps,
    )
    evaluation_records = evaluate_records(
        SCENARIOS,
        truth_cutoffs,
        args.seed,
        args.sample_size,
        args.evaluation_reps,
        args.grid_points,
    )
    payload = {
        "description": "M29 first calibrated Monte Carlo pass for standard-DW versus robust-DW comparison.",
        "configuration": {
            "seed": args.seed,
            "sample_size": args.sample_size,
            "calibration_reps": args.calibration_reps,
            "evaluation_reps": args.evaluation_reps,
            "grid_points": args.grid_points,
            "grid_window": list(GRID_WINDOW),
            "true_B0": base.TRUE_MATRIX.tolist(),
            "true_b12": base.TRUE_B12,
            "true_b21": base.TRUE_B21,
            "chi_square_cutoffs": {
                "standard_dw": base.CHI2_90_DF4,
                "robust_dw": base.CHI2_90_DF5,
            },
        },
        "scenarios": [
            {
                "name": scenario.name,
                "label": scenario.label,
                "noise": list(scenario.noise),
                "non_gaussian_weight": scenario.non_gaussian_weight,
                "residual_noise": scenario.residual_noise,
                "note": scenario.note,
            }
            for scenario in SCENARIOS
        ],
        "truth_cutoffs": truth_cutoffs,
        "summary": summarize(evaluation_records),
        "calibration_records": calibration_records,
        "evaluation_records": evaluation_records,
    }
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    write_note(payload)
    print(f"Wrote {JSON_OUTPUT.relative_to(ROOT)}")
    print(f"Wrote {NOTE_OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
