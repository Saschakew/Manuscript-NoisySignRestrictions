"""Full-grid cleaned iid residual-noise MC with analytic GMM weights.

M79 extends the M78 cleaned iid full-grid Monte Carlo to the Figure 1
residual-noise DGPs. It holds T=500 and strong structural non-Gaussianity
fixed, varies V=(0,0),(0.2,0.2),(0.5,0.5), and reports Sign, DW, and nrDW on
the active first-shock projection grid. The statistic uses population-normalized
iid chi-square structural shocks, iid Gaussian residual noise, no demeaning or
sample standardization, and analytic iid weights.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np

try:
    from . import m69_extended_three_block_mc as m69
    from . import m77_clean_iid_mc_efficient_weight as m77
    from . import m78_clean_iid_full_sample_size_mc as m78
    from . import sign_dw_unit_variance_noise_grid_figure as fig
except ImportError:
    import m69_extended_three_block_mc as m69
    import m77_clean_iid_mc_efficient_weight as m77
    import m78_clean_iid_full_sample_size_mc as m78
    import sign_dw_unit_variance_noise_grid_figure as fig


ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = ROOT / "manuscript" / "simulations"
OUTPUT_DIR = SIM_DIR / "output"
JSON_OUTPUT = OUTPUT_DIR / "m79_clean_iid_full_residual_noise_mc.json"
NOTE_OUTPUT = SIM_DIR / "m79_clean_iid_full_residual_noise_mc.md"

NOISE_SCENARIOS = (
    m69.MCScenario("noise_v0", "V=(0,0)", (0.0, 0.0), 1.0, 500, "gaussian", "No residual noise."),
    m69.MCScenario(
        "noise_v02",
        "V=(0.2,0.2)",
        (0.2, 0.2),
        1.0,
        500,
        "gaussian",
        "Moderate Gaussian residual noise.",
    ),
    m69.MCScenario(
        "noise_v05",
        "V=(0.5,0.5)",
        (0.5, 0.5),
        1.0,
        500,
        "gaussian",
        "High Gaussian residual noise.",
    ),
)


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def lambda_grid_for_scenarios(
    spec: fig.GridSpec,
    scenarios: tuple[m69.MCScenario, ...] = NOISE_SCENARIOS,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    lambda_1_values: list[float] = []
    lambda_2_values: list[float] = []
    for scenario in scenarios:
        lambda_1, lambda_2 = fig.lambda_grid_for_noise(scenario.noise, spec)
        lambda_1_values.extend(float(value) for value in lambda_1)
        lambda_2_values.extend(float(value) for value in lambda_2)
    lambda_1 = np.asarray(sorted(set(lambda_1_values)), dtype=float)
    lambda_2 = np.asarray(sorted(set(lambda_2_values)), dtype=float)
    lambda_pairs = np.array(np.meshgrid(lambda_1, lambda_2, indexing="ij")).reshape(2, -1).T
    return lambda_1, lambda_2, lambda_pairs


def validate_lambda_grid(
    lambda_1: np.ndarray,
    lambda_2: np.ndarray,
    scenarios: tuple[m69.MCScenario, ...] = NOISE_SCENARIOS,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if not np.any(np.isclose(lambda_1, 0.0)) or not np.any(np.isclose(lambda_2, 0.0)):
        raise ValueError("lambda grid must contain zero for the no-noise scenario")
    for scenario in scenarios:
        true_lambda = m77.true_lambda(scenario.noise)
        contains = (
            bool(np.any(np.isclose(lambda_1, true_lambda[0]))),
            bool(np.any(np.isclose(lambda_2, true_lambda[1]))),
        )
        if not all(contains):
            raise ValueError(f"lambda grid does not contain true lambda for {scenario.name}: {true_lambda}")
        records.append(
            {
                "scenario": scenario.name,
                "label": scenario.label,
                "noise": list(scenario.noise),
                "true_lambda": [float(true_lambda[0]), float(true_lambda[1])],
                "true_lambda_in_grid": list(contains),
                "inside_rho_bound": bool(
                    true_lambda[0] <= fig.RELATIVE_NOISE_RATIO
                    and true_lambda[1] <= fig.RELATIVE_NOISE_RATIO
                ),
            }
        )
    return records


def summarize(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for scenario in NOISE_SCENARIOS:
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
                    "sign": m78.count_rate([m["sign"]["truth_in"] for m in metrics]),
                    "standard_dw": m78.count_rate([m["standard_dw"]["truth_in"] for m in metrics]),
                    "robust_dw": m78.count_rate([m["robust_dw"]["truth_in"] for m in metrics]),
                },
                "warning": m78.count_rate([m["warning"] for m in metrics]),
                "size": {
                    "measure": "accepted projection share on the displayed (B11,B21) grid",
                    "sign": m78.numeric_summary([m["sign"]["accepted_share"] for m in metrics]),
                    "standard_dw": m78.numeric_summary([m["standard_dw"]["accepted_share"] for m in metrics]),
                    "robust_dw": m78.numeric_summary([m["robust_dw"]["accepted_share"] for m in metrics]),
                },
                "empty": {
                    "sign": m78.count_rate([m["sign"]["empty"] for m in metrics]),
                    "standard_dw": m78.count_rate([m["standard_dw"]["empty"] for m in metrics]),
                    "robust_dw": m78.count_rate([m["robust_dw"]["empty"] for m in metrics]),
                },
                "truth_j": {
                    "sign_second": m78.numeric_summary([m["sign"]["truth_second_j"] for m in metrics]),
                    "standard_higher": m78.numeric_summary([m["standard_dw"]["truth_higher_j"] for m in metrics]),
                    "robust_full": m78.numeric_summary([m["robust_dw"]["truth_j"] for m in metrics]),
                },
                "overlap": {
                    "jaccard": m78.numeric_summary([m["overlap"]["jaccard"] for m in metrics]),
                    "d_standard_not_subset_robust": m78.numeric_summary(
                        [m["overlap"]["d_standard_not_subset_robust"] for m in metrics]
                    ),
                },
                "distance_to_truth_projection": {
                    "sign": m78.numeric_summary([m["sign"]["distance_to_truth_projection"] for m in metrics]),
                    "standard_dw": m78.numeric_summary(
                        [m["standard_dw"]["distance_to_truth_projection"] for m in metrics]
                    ),
                    "robust_dw": m78.numeric_summary(
                        [m["robust_dw"]["distance_to_truth_projection"] for m in metrics]
                    ),
                },
                "prefilter_count": m78.numeric_summary([m["robust_dw"]["prefilter_count"] for m in metrics]),
                "note": scenario.note,
            }
        )
    return summaries


def scenario_metadata() -> list[dict[str, Any]]:
    return [
        {
            "name": scenario.name,
            "label": scenario.label,
            "noise": list(scenario.noise),
            "non_gaussian_weight": scenario.non_gaussian_weight,
            "sample_size": scenario.sample_size,
            "residual_noise": scenario.residual_noise,
            "note": scenario.note,
        }
        for scenario in NOISE_SCENARIOS
    ]


def write_progress(progress_output: Path | None, payload: dict[str, Any]) -> None:
    if progress_output is None:
        return
    progress_output.parent.mkdir(parents=True, exist_ok=True)
    temp_path = progress_output.with_suffix(progress_output.suffix + ".tmp")
    temp_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    temp_path.replace(progress_output)


def append_progress_log(progress_log_output: Path | None, line: str) -> None:
    if progress_log_output is None:
        return
    progress_log_output.parent.mkdir(parents=True, exist_ok=True)
    with progress_log_output.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line.rstrip() + "\n")


def emit_progress(line: str, progress_log_output: Path | None) -> None:
    append_progress_log(progress_log_output, line)
    stream = getattr(sys, "stdout", None)
    if stream is not None:
        print(line, flush=True)


def weight_metadata(bundle: m77.WeightBundle) -> dict[str, Any]:
    return {
        "eigenvalues": bundle.eigenvalues,
        "condition_number": float(max(bundle.eigenvalues) / min(bundle.eigenvalues)),
        "max_abs_moment_mean": float(max(abs(value) for value in bundle.moment_means)),
        "regularization": bundle.regularization,
    }


def fmt(value: Any, digits: int = 3) -> str:
    return m78.fmt(value, digits)


def fmt_rate(item: dict[str, Any]) -> str:
    return m78.fmt_rate(item)


def fmt_mean_median(item: dict[str, Any]) -> str:
    return m78.fmt_mean_median(item)


def write_outputs(
    records: list[dict[str, Any]],
    summaries: list[dict[str, Any]],
    spec: fig.GridSpec,
    reps: int,
    second_weight: m77.WeightBundle,
    dw_weight: m77.WeightBundle,
    robust_cache: m78.RobustWeightCache,
    lambda_1: np.ndarray,
    lambda_2: np.ndarray,
    lambda_checks: list[dict[str, Any]],
    json_output: Path,
    note_output: Path,
    quick: bool,
) -> None:
    payload = {
        "schema_version": 1,
        "task": "M79 clean iid full residual-noise MC",
        "description": "Full-grid residual-noise MC for the Figure 1 DGPs using population-normalized iid shocks/noise and analytic iid GMM weights W=(E[f_t f_t'])^{-1}.",
        "configuration": {
            "quick": quick,
            "reps_per_scenario": reps,
            "base_seed": fig.RANDOM_SEED,
            "seed_block_index": 0,
            "rho": fig.RELATIVE_NOISE_RATIO,
            "projection_points": spec.projection_points,
            "profile_points": spec.profile_points,
            "lambda_points_nominal": spec.lambda_points,
            "lambda_1_grid": [float(value) for value in lambda_1],
            "lambda_2_grid": [float(value) for value in lambda_2],
            "displayed_projection": ["B11", "B21"],
            "profiled_coordinates": ["B12", "B22", "lambda1", "lambda2"],
            "sign_restrictions": ["B11 > 0", "B22 > 0", "B12 <= 0"],
            "dgp": "population-normalized iid chi-square structural shocks and iid Gaussian residual noise; no sample standardization; no residual or recovered-shock demeaning",
            "structural_shock": f"(chi2_{fig.STRUCTURAL_CHI2_DF:g} - {fig.STRUCTURAL_CHI2_DF:g}) / sqrt(2*{fig.STRUCTURAL_CHI2_DF:g})",
            "set_size_measure": "accepted projection share on the displayed (B11,B21) grid",
            "weighting": {
                "sign": "analytic no-noise second-moment W=(E[f_S f_S'])^{-1}",
                "standard_dw": "analytic no-noise higher-moment W=(E[f_DW f_DW'])^{-1}, combined with the sign screen",
                "robust_dw": "candidate-specific analytic iid W(B,lambda)=(E[f_t(B,lambda)f_t(B,lambda)'])^{-1}",
            },
            "weight_regularization": "symmetric covariance eigensystem with eigenvalue floor max(max_eigenvalue, 1) * 1e-10",
            "critical_values": {
                "second_moment_chi2_90_df3": fig.CHI2_90_DF3,
                "standard_dw_chi2_90_df5": fig.CHI2_90_DF5,
                "robust_full_moment_chi2_90_df8": fig.CHI2_90_DF8,
            },
            "inference_caveat": "Pointwise chi-square diagnostics only; final projected critical values remain M65 follow-up.",
            "weights": {
                "sign_second": weight_metadata(second_weight),
                "standard_dw_higher": weight_metadata(dw_weight),
                "robust_cache": robust_cache.stats,
            },
            "lambda_checks": lambda_checks,
            "scenarios": scenario_metadata(),
        },
        "summaries": summaries,
        "records": records,
    }
    json_output.parent.mkdir(parents=True, exist_ok=True)
    json_output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# M79 Clean IID Full Residual-Noise MC",
        "",
        "Status: generated full-grid residual-noise Monte Carlo output for the cleaned iid analytic-weight design.",
        "",
        "This run extends the M78 cleaned iid full-grid logic to the Figure 1 residual-noise scenarios. It fixes `T=500` and strong structural non-Gaussianity, varies residual noise across `V=(0,0)`, `V=(0.2,0.2)`, and `V=(0.5,0.5)`, and keeps the active Sign/DW/nrDW reporting surface.",
        "",
        "## Configuration",
        "",
        f"- Machine-readable output: `{display_path(json_output)}`.",
        f"- Quick run: `{quick}`.",
        f"- Replications per scenario: `{reps}`.",
        f"- Projection grid: `{spec.projection_points} x {spec.projection_points}` plus exact true coordinates when needed.",
        f"- Profile grid: `{spec.profile_points} x {spec.profile_points}` plus exact true profiled coordinates when needed.",
        f"- Nominal lambda grid: `{spec.lambda_points} x {spec.lambda_points}` plus true lambda values for all residual-noise scenarios.",
        "- Structural shocks: population-normalized iid chi-square.",
        "- Residual noise: iid Gaussian.",
        "- No sample standardization, no residual demeaning, no recovered-shock demeaning.",
        "- Sign screen: `B11>0`, `B22>0`, `B12<=0`; `B21` is not sign-restricted.",
        "- Sign weight: analytic no-noise three-moment weight.",
        "- DW weight: analytic no-noise five-moment weight, after the sign screen.",
        "- nrDW weight: candidate-specific analytic iid eight-moment weight.",
        "",
        "## Residual-Noise Table",
        "",
        "| V | Sign truth | DW truth | nrDW truth | Sign size | DW size | nrDW size | Sign empty | DW empty | nrDW empty | Warning |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in summaries:
        lines.append(
            "| {label} | {sign_truth} | {dw_truth} | {rdw_truth} | {sign_size} | {dw_size} | {rdw_size} | {sign_empty} | {dw_empty} | {rdw_empty} | {warning} |".format(
                label=item["label"].replace("V=", ""),
                sign_truth=fmt_rate(item["truth_inclusion"]["sign"]),
                dw_truth=fmt_rate(item["truth_inclusion"]["standard_dw"]),
                rdw_truth=fmt_rate(item["truth_inclusion"]["robust_dw"]),
                sign_size=fmt_mean_median(item["size"]["sign"]),
                dw_size=fmt_mean_median(item["size"]["standard_dw"]),
                rdw_size=fmt_mean_median(item["size"]["robust_dw"]),
                sign_empty=fmt_rate(item["empty"]["sign"]),
                dw_empty=fmt_rate(item["empty"]["standard_dw"]),
                rdw_empty=fmt_rate(item["empty"]["robust_dw"]),
                warning=fmt_rate(item["warning"]),
            )
        )
    lines.extend(
        [
            "",
            "## Truth-Statistic Quantiles",
            "",
            "| V | True lambda | Sign J q90 | DW J q90 | nrDW J q90 | nrDW prefilter mean |",
            "|---:|---:|---:|---:|---:|---:|",
        ]
    )
    lambda_by_name = {item["scenario"]: item for item in lambda_checks}
    for item in summaries:
        true_lambda = lambda_by_name[item["scenario"]]["true_lambda"]
        lines.append(
            "| {label} | ({lambda1}, {lambda2}) | {sign_j} | {dw_j} | {rdw_j} | {prefilter} |".format(
                label=item["label"].replace("V=", ""),
                lambda1=fmt(true_lambda[0]),
                lambda2=fmt(true_lambda[1]),
                sign_j=fmt(item["truth_j"]["sign_second"]["q90"]),
                dw_j=fmt(item["truth_j"]["standard_higher"]["q90"]),
                rdw_j=fmt(item["truth_j"]["robust_full"]["q90"]),
                prefilter=fmt(item["prefilter_count"]["mean"], 1),
            )
        )
    lines.extend(
        [
            "",
            "## Weight Diagnostics",
            "",
            "| Weight | Detail | Value |",
            "|---|---|---:|",
            f"| Sign | condition number | {weight_metadata(second_weight)['condition_number']:.6g} |",
            f"| DW | condition number | {weight_metadata(dw_weight)['condition_number']:.6g} |",
            f"| nrDW cache | computed B candidates | {robust_cache.stats['computed_b_candidates']} |",
            f"| nrDW cache | computed candidate-lambda pairs | {robust_cache.stats['computed_candidate_lambda_pairs']} |",
            f"| nrDW cache | max absolute analytic moment mean | {robust_cache.stats['max_abs_moment_mean']:.3g} |",
            f"| nrDW cache | regularized matrices | {robust_cache.stats['regularization']['regularized_matrix_count']} |",
            "",
            "## Claim Audit",
            "",
            "| Claim | Status | Evidence | Confidence | Action |",
            "|---|---|---|---|---|",
            "| M79 uses the Figure 1 DGPs: `T=500`, strong structural non-Gaussianity, Gaussian residual noise, and `V=(0,0),(0.2,0.2),(0.5,0.5)`. | `code-implemented`, `user-decision` | Scenario configuration in this script and JSON. | high | promote as M79 design |",
            "| The cleaned full MC uses population-normalized iid shocks/noise and no demeaning. | `code-implemented`, `user-decision` | This script and JSON configuration. | high | promote |",
            "| The nrDW full-grid statistic uses candidate-specific analytic W(B,lambda). | `code-implemented`, `derived`, `user-decision` | M78 vectorized polynomial weight computation reused here. | high | promote as M79 design |",
            "| The no-noise truth is evaluated with lambda zero on the lambda grid. | `code-implemented` | Lambda-grid checks in JSON configuration. | high | promote |",
            "| Pointwise chi-square cutoffs are final projected confidence-set critical values. | `conjectural` | M65 remains open. | medium | quarantine |",
            "",
        ]
    )
    note_output.parent.mkdir(parents=True, exist_ok=True)
    note_output.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def run(
    json_output: Path = JSON_OUTPUT,
    note_output: Path = NOTE_OUTPUT,
    reps: int = 500,
    spec: fig.GridSpec = fig.GridSpec(projection_points=27, profile_points=7, lambda_points=5, robust_batch_size=36),
    quick: bool = False,
    progress_output: Path | None = None,
    progress_log_output: Path | None = None,
) -> Path:
    grid = fig.make_candidate_grid(spec)
    lambda_1, lambda_2, lambda_pairs = lambda_grid_for_scenarios(spec)
    lambda_checks = validate_lambda_grid(lambda_1, lambda_2)
    robust_cache = m78.RobustWeightCache.create(grid, lambda_pairs)
    second_weight = m77.standard_second_weight()
    dw_weight = m77.standard_dw_weight()

    records: list[dict[str, Any]] = []
    total = len(NOISE_SCENARIOS) * reps
    completed = 0
    started = time.perf_counter()

    def publish_progress(
        status: str,
        scenario: m69.MCScenario | None = None,
        rep: int | None = None,
        seed: int | None = None,
        metrics: dict[str, Any] | None = None,
    ) -> None:
        elapsed = time.perf_counter() - started
        average = elapsed / completed if completed else None
        eta = average * (total - completed) if average is not None else None
        latest = None
        if metrics is not None:
            latest = {
                "sign_share": metrics["sign"]["accepted_share"],
                "standard_share": metrics["standard_dw"]["accepted_share"],
                "robust_share": metrics["robust_dw"]["accepted_share"],
                "sign_truth_in": metrics["sign"]["truth_in"],
                "standard_truth_in": metrics["standard_dw"]["truth_in"],
                "robust_truth_in": metrics["robust_dw"]["truth_in"],
                "robust_prefilter_count": metrics["robust_dw"]["prefilter_count"],
            }
        payload = {
            "schema_version": 1,
            "status": status,
            "updated_at": now_iso(),
            "pid": os.getpid(),
            "completed": completed,
            "total": total,
            "remaining": total - completed,
            "elapsed_seconds": elapsed,
            "average_seconds_per_rep": average,
            "eta_seconds": eta,
            "grid": {
                "projection_points": spec.projection_points,
                "profile_points": spec.profile_points,
                "lambda_points_nominal": spec.lambda_points,
                "lambda_1_points_actual": int(lambda_1.size),
                "lambda_2_points_actual": int(lambda_2.size),
            },
            "reps_per_scenario": reps,
            "current": None
            if scenario is None
            else {
                "scenario": scenario.name,
                "label": scenario.label,
                "noise": list(scenario.noise),
                "sample_size": scenario.sample_size,
                "rep": rep,
                "seed": seed,
            },
            "latest_metrics": latest,
            "robust_weight_cache": robust_cache.stats,
            "outputs": {
                "json": display_path(json_output),
                "note": display_path(note_output),
            },
        }
        write_progress(progress_output, payload)
        if status == "completed":
            emit_progress(f"[progress] completed {completed}/{total} reps in {elapsed:.1f}s", progress_log_output)
        elif scenario is not None and rep is not None:
            eta_text = "n/a" if eta is None else f"{eta / 3600:.2f}h"
            emit_progress(
                f"[progress] {completed}/{total} scenario={scenario.name} "
                f"rep={rep + 1}/{reps} elapsed={elapsed / 3600:.2f}h eta={eta_text}",
                progress_log_output,
            )
        else:
            emit_progress(f"[progress] started total={total}", progress_log_output)

    publish_progress("running")
    for scenario_index, scenario in enumerate(NOISE_SCENARIOS):
        for rep in range(reps):
            seed = m69.seed_for(fig.RANDOM_SEED, 0, scenario_index, rep)
            metrics = m78.evaluate_one(
                scenario,
                seed,
                grid,
                spec,
                second_weight,
                dw_weight,
                robust_cache,
            )
            completed += 1
            records.append(
                {
                    "scenario": scenario.name,
                    "label": scenario.label,
                    "rep": rep,
                    "seed": seed,
                    "metrics": metrics,
                }
            )
            publish_progress("running", scenario, rep, seed, metrics)
    summaries = summarize(records)
    write_outputs(
        records,
        summaries,
        spec,
        reps,
        second_weight,
        dw_weight,
        robust_cache,
        lambda_1,
        lambda_2,
        lambda_checks,
        json_output,
        note_output,
        quick,
    )
    publish_progress("completed")
    return note_output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-output", default="", help="Optional JSON output path.")
    parser.add_argument("--note-output", default="", help="Optional Markdown note output path.")
    parser.add_argument("--evaluation-reps", type=int, default=500)
    parser.add_argument("--projection-points", type=int, default=27)
    parser.add_argument("--profile-points", type=int, default=7)
    parser.add_argument("--lambda-points", type=int, default=5)
    parser.add_argument("--robust-batch-size", type=int, default=36)
    parser.add_argument("--standard-batch-size", type=int, default=240)
    parser.add_argument("--progress-output", default="", help="Optional JSON progress file updated after each replication.")
    parser.add_argument("--progress-log-output", default="", help="Optional text progress log appended after each replication.")
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Use a small smoke-test grid and limit replications.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    reps = args.evaluation_reps
    projection_points = args.projection_points
    profile_points = args.profile_points
    lambda_points = args.lambda_points
    if args.quick:
        reps = min(reps, 2)
        projection_points = min(projection_points, 7)
        profile_points = min(profile_points, 5)
        lambda_points = min(lambda_points, 3)
    spec = fig.GridSpec(
        projection_points=projection_points,
        profile_points=profile_points,
        lambda_points=lambda_points,
        robust_batch_size=args.robust_batch_size,
        standard_batch_size=args.standard_batch_size,
    )
    progress_output = Path(args.progress_output) if args.progress_output else None
    progress_log_output = Path(args.progress_log_output) if args.progress_log_output else None
    try:
        path = run(
            json_output=Path(args.json_output) if args.json_output else JSON_OUTPUT,
            note_output=Path(args.note_output) if args.note_output else NOTE_OUTPUT,
            reps=reps,
            spec=spec,
            quick=args.quick,
            progress_output=progress_output,
            progress_log_output=progress_log_output,
        )
    except Exception:
        error = traceback.format_exc()
        write_progress(
            progress_output,
            {
                "schema_version": 1,
                "status": "failed",
                "updated_at": now_iso(),
                "pid": os.getpid(),
                "error": error,
            },
        )
        append_progress_log(progress_log_output, "[progress] failed")
        append_progress_log(progress_log_output, error)
        raise
    print(f"Wrote {display_path(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
