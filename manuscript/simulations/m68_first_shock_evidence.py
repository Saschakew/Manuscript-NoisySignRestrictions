"""Monte Carlo evidence for the M68 first-shock unit-variance chart."""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

try:
    from . import sign_dw_unit_variance_noise_grid_figure as fig
except ImportError:
    import sign_dw_unit_variance_noise_grid_figure as fig


ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = ROOT / "manuscript" / "simulations"
OUTPUT_DIR = SIM_DIR / "output"
JSON_OUTPUT = OUTPUT_DIR / "m68_first_shock_evidence.json"
NOTE_OUTPUT = SIM_DIR / "m68_first_shock_evidence.md"


@dataclass(frozen=True)
class MCScenario:
    name: str
    label: str
    noise: tuple[float, float]
    non_gaussian_weight: float
    sample_size: int
    residual_noise: str
    note: str


SCENARIOS = (
    MCScenario("no_noise", "No noise, strong moments", (0.0, 0.0), 1.0, 500, "gaussian", "Sanity case."),
    MCScenario("moderate_noise", "Moderate Gaussian noise", (0.2, 0.2), 1.0, 500, "gaussian", "Main moderate-noise case."),
    MCScenario("high_noise", "High Gaussian noise", (0.5, 0.5), 1.0, 500, "gaussian", "Main high-noise stress case."),
    MCScenario("weak_moments", "Weak structural higher moments", (0.2, 0.2), 0.25, 500, "gaussian", "Higher-moment limitation case."),
    MCScenario("gaussian_shocks", "Gaussian structural shocks", (0.2, 0.2), 0.0, 500, "gaussian", "All-null higher-cumulant limit."),
    MCScenario("skewed_residual_noise", "Skewed residual noise", (0.2, 0.2), 1.0, 500, "skewed", "Maintained-assumption stress case."),
)


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def seed_for(base_seed: int, scenario_index: int, rep: int) -> int:
    return int(base_seed + 100_000 + scenario_index * 10_000 + rep)


def mask_metrics(mask: np.ndarray) -> dict[str, Any]:
    return {
        "accepted_count": int(np.count_nonzero(mask)),
        "accepted_share": fig.mask_share(mask),
        "empty": not bool(mask.any()),
    }


def evaluate_one(
    scenario: MCScenario,
    seed: int,
    grid: fig.CandidateGrid,
    spec: fig.GridSpec,
) -> dict[str, Any]:
    residuals = fig.simulate_residuals(
        *scenario.noise,
        sample_size=scenario.sample_size,
        seed=seed,
        non_gaussian_weight=scenario.non_gaussian_weight,
        residual_noise=scenario.residual_noise,
    )
    second_weight, standard_weight, robust_weight = fig.scenario_weights(residuals, scenario.noise)
    standard = fig.evaluate_standard_projection(residuals, grid, spec, second_weight, standard_weight)
    robust = fig.evaluate_robust_projection(residuals, scenario.noise, grid, spec, robust_weight)
    second_truth, standard_truth = fig.standard_truth_j(residuals, second_weight, standard_weight)
    robust_truth, true_lambda = fig.robust_truth_j(residuals, scenario.noise, robust_weight)

    sign_mask = standard["sign_mask"]
    standard_mask = standard["standard_mask"]
    robust_mask = robust["robust_mask"]
    intersection = standard_mask & robust_mask
    union = standard_mask | robust_mask
    standard_count = int(np.count_nonzero(standard_mask))
    intersection_count = int(np.count_nonzero(intersection))
    union_count = int(np.count_nonzero(union))
    standard_contained = intersection_count / standard_count if standard_count else None

    standard_truth_in = bool(second_truth <= fig.CHI2_90_DF3 and standard_truth <= fig.CHI2_90_DF5)
    robust_truth_in = bool(
        true_lambda[0] <= fig.RELATIVE_NOISE_RATIO
        and true_lambda[1] <= fig.RELATIVE_NOISE_RATIO
        and robust_truth <= fig.CHI2_90_DF8
    )
    return {
        "seed": seed,
        "sign": mask_metrics(sign_mask),
        "standard_dw": {
            **mask_metrics(standard_mask),
            "truth_in": standard_truth_in,
            "truth_second_j": float(second_truth),
            "truth_higher_j": float(standard_truth),
            "distance_to_truth_projection": fig.truth_distance(standard_mask, grid),
        },
        "robust_dw": {
            **mask_metrics(robust_mask),
            "truth_in": robust_truth_in,
            "truth_j": float(robust_truth),
            "true_lambda": [float(true_lambda[0]), float(true_lambda[1])],
            "distance_to_truth_projection": fig.truth_distance(robust_mask, grid),
            "prefilter_count": int(robust["prefilter_count"]),
        },
        "overlap": {
            "intersection_count": intersection_count,
            "union_count": union_count,
            "jaccard": intersection_count / union_count if union_count else None,
            "d_standard_not_subset_robust": None if standard_contained is None else 1.0 - standard_contained,
        },
        "warning": bool((not standard_truth_in) and robust_truth_in),
    }


def mean_optional(values: list[Any]) -> float | None:
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


def summarize(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for scenario in SCENARIOS:
        subset = [record for record in records if record["scenario"] == scenario.name]
        summaries.append(
            {
                "scenario": scenario.name,
                "label": scenario.label,
                "reps": len(subset),
                "noise": list(scenario.noise),
                "non_gaussian_weight": scenario.non_gaussian_weight,
                "sample_size": scenario.sample_size,
                "residual_noise": scenario.residual_noise,
                "standard_truth_rate": mean_optional([r["metrics"]["standard_dw"]["truth_in"] for r in subset]),
                "robust_truth_rate": mean_optional([r["metrics"]["robust_dw"]["truth_in"] for r in subset]),
                "warning_rate": mean_optional([r["metrics"]["warning"] for r in subset]),
                "sign_share": mean_optional([r["metrics"]["sign"]["accepted_share"] for r in subset]),
                "standard_share": mean_optional([r["metrics"]["standard_dw"]["accepted_share"] for r in subset]),
                "robust_share": mean_optional([r["metrics"]["robust_dw"]["accepted_share"] for r in subset]),
                "standard_empty_rate": mean_optional([r["metrics"]["standard_dw"]["empty"] for r in subset]),
                "robust_empty_rate": mean_optional([r["metrics"]["robust_dw"]["empty"] for r in subset]),
                "d_standard_not_subset_robust": mean_optional(
                    [r["metrics"]["overlap"]["d_standard_not_subset_robust"] for r in subset]
                ),
                "standard_distance_to_truth": mean_optional(
                    [r["metrics"]["standard_dw"]["distance_to_truth_projection"] for r in subset]
                ),
                "robust_distance_to_truth": mean_optional(
                    [r["metrics"]["robust_dw"]["distance_to_truth_projection"] for r in subset]
                ),
                "note": scenario.note,
            }
        )
    return summaries


def fmt(value: Any, digits: int = 3) -> str:
    if value is None:
        return "n/a"
    numeric = float(value)
    if not math.isfinite(numeric):
        return "n/a"
    return f"{numeric:.{digits}f}"


def write_outputs(
    records: list[dict[str, Any]],
    summaries: list[dict[str, Any]],
    spec: fig.GridSpec,
    reps: int,
    json_output: Path,
    note_output: Path,
) -> None:
    payload = {
        "schema_version": 1,
        "task": "M68 first-shock impact evidence rebuild",
        "description": "Monte Carlo table using the same first-shock chart and M66 unit-variance GMM criterion as Figures 1-3.",
        "configuration": {
            "reps": reps,
            "base_seed": fig.RANDOM_SEED,
            "rho": fig.RELATIVE_NOISE_RATIO,
            "projection_points": spec.projection_points,
            "profile_points": spec.profile_points,
            "lambda_points": spec.lambda_points,
            "displayed_projection": ["B11", "B21"],
            "profiled_coordinates": ["B12", "B22", "lambda1", "lambda2"],
            "sign_restrictions": ["B11 > 0", "B22 > 0", "B12 <= 0", "B21 >= 0"],
            "critical_values": {
                "second_moment_chi2_90_df3": fig.CHI2_90_DF3,
                "standard_dw_chi2_90_df5": fig.CHI2_90_DF5,
                "robust_full_moment_chi2_90_df8": fig.CHI2_90_DF8,
            },
        },
        "summaries": summaries,
        "records": records,
    }
    json_output.parent.mkdir(parents=True, exist_ok=True)
    json_output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# M68 First-Shock Monte Carlo Evidence",
        "",
        "Status: generated Monte Carlo table for the M68 first-shock impact chart.",
        "",
        "The table uses the same sign screen as Figures 1-3: `B11>0`, `B22>0`, `B12<=0`, and `B21>=0`. The displayed coordinates are `(B11,B21)`, while `B12`, `B22`, and `lambda` are profiled. The robust row evaluates the M66 moment vector at `nu_i=lambda_i(BB')_ii`.",
        "",
        "The cutoffs are pointwise chi-square diagnostics for the displayed moment rows. The final projected critical-value route remains an inference follow-up.",
        "",
        "## Configuration",
        "",
        f"- Machine-readable output: `{display_path(json_output)}`.",
        f"- Replications per scenario: `{reps}`.",
        f"- Projection grid: `{spec.projection_points} x {spec.projection_points}`.",
        f"- Profile grid: `{spec.profile_points} x {spec.profile_points}`.",
        f"- Lambda grid: `{spec.lambda_points} x {spec.lambda_points}`.",
        "",
        "## Chi-Square Diagnostic Table",
        "",
        "| Scenario | S truth | R truth | Warning | Sign share | S share | R share | d_S_not_subset_R | S dist | R dist |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in summaries:
        lines.append(
            "| {label} | {s_truth} | {r_truth} | {warning} | {sign} | {standard} | {robust} | {outside} | {s_dist} | {r_dist} |".format(
                label=item["label"],
                s_truth=fmt(item["standard_truth_rate"]),
                r_truth=fmt(item["robust_truth_rate"]),
                warning=fmt(item["warning_rate"]),
                sign=fmt(item["sign_share"]),
                standard=fmt(item["standard_share"]),
                robust=fmt(item["robust_share"]),
                outside=fmt(item["d_standard_not_subset_robust"]),
                s_dist=fmt(item["standard_distance_to_truth"]),
                r_dist=fmt(item["robust_distance_to_truth"]),
            )
        )
    lines.extend(
        [
            "",
            "## Claim Audit",
            "",
            "| Claim | Status | Evidence | Confidence | Action |",
            "|---|---|---|---|---|",
            "| Monte Carlo uses the M68 sign screen and first-shock chart. | `code-implemented`, `user-decision` | This script and JSON configuration. | high | promote for Table 1 diagnostics |",
            "| Robust MC uses `nu_i=lambda_i(BB')_ii` and profiles `lambda in [0,rho]^2`. | `code-implemented`, `derived` | M66 derivation and evaluator calls. | high | promote |",
            "| The chi-square cutoffs are final projected confidence-set critical values. | `conjectural` | M65/M68 still leave projection-critical-value inference as follow-up. | medium | quarantine as diagnostic |",
            "",
        ]
    )
    note_output.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def run(
    json_output: Path = JSON_OUTPUT,
    note_output: Path = NOTE_OUTPUT,
    reps: int = 12,
    spec: fig.GridSpec = fig.GridSpec(projection_points=17, profile_points=7, lambda_points=5),
) -> Path:
    grid = fig.make_candidate_grid(spec)
    records: list[dict[str, Any]] = []
    for scenario_index, scenario in enumerate(SCENARIOS):
        for rep in range(reps):
            seed = seed_for(fig.RANDOM_SEED, scenario_index, rep)
            metrics = evaluate_one(scenario, seed, grid, spec)
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
    write_outputs(records, summaries, spec, reps, json_output, note_output)
    return note_output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-output", default="", help="Optional JSON output path.")
    parser.add_argument("--note-output", default="", help="Optional Markdown note output path.")
    parser.add_argument("--evaluation-reps", type=int, default=12)
    parser.add_argument("--projection-points", type=int, default=17)
    parser.add_argument("--profile-points", type=int, default=7)
    parser.add_argument("--lambda-points", type=int, default=5)
    parser.add_argument("--robust-batch-size", type=int, default=36)
    parser.add_argument("--standard-batch-size", type=int, default=240)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    spec = fig.GridSpec(
        projection_points=args.projection_points,
        profile_points=args.profile_points,
        lambda_points=args.lambda_points,
        robust_batch_size=args.robust_batch_size,
        standard_batch_size=args.standard_batch_size,
    )
    path = run(
        json_output=Path(args.json_output) if args.json_output else JSON_OUTPUT,
        note_output=Path(args.note_output) if args.note_output else NOTE_OUTPUT,
        reps=args.evaluation_reps,
        spec=spec,
    )
    print(f"Wrote {display_path(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
