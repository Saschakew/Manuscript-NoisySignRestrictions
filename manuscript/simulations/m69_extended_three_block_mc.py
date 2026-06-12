"""Extended Monte Carlo for the three corrected active figure blocks.

This script reuses the corrected first-shock evaluator. It does not change the
moment criterion: the active chart displays (B11, B21), profiles B12, B22, and
lambda, imposes B11>0, B22>0, and B12<=0, and evaluates the M66 route
nu_i=lambda_i(BB')_ii with candidate-specific pointwise covariance weights.
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
    from . import m68_first_shock_evidence as m68
    from . import sign_dw_unit_variance_noise_grid_figure as fig
except ImportError:
    import m68_first_shock_evidence as m68
    import sign_dw_unit_variance_noise_grid_figure as fig


ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = ROOT / "manuscript" / "simulations"
OUTPUT_DIR = SIM_DIR / "output"
REPLICATION_DIR = ROOT / "manuscript" / "replication"
QUICK_OUTPUT_DIR = REPLICATION_DIR / "output" / "quick"
JSON_OUTPUT = OUTPUT_DIR / "m69_extended_three_block_mc.json"
NOTE_OUTPUT = SIM_DIR / "m69_extended_three_block_mc.md"


@dataclass(frozen=True)
class MCScenario:
    name: str
    label: str
    noise: tuple[float, float]
    non_gaussian_weight: float
    sample_size: int
    residual_noise: str
    note: str


@dataclass(frozen=True)
class MCBlock:
    name: str
    label: str
    figure_matched: str
    note: str
    scenarios: tuple[MCScenario, ...]


BLOCKS = (
    MCBlock(
        name="noise_grid",
        label="Residual-noise grid",
        figure_matched="Figure 1",
        note="Matches Figure 1: residual-noise variance varies while T=500 and structural non-Gaussianity is strong.",
        scenarios=(
            MCScenario("noise_v0", "V=(0,0)", (0.0, 0.0), 1.0, 500, "gaussian", "No residual noise."),
            MCScenario("noise_v02", "V=(0.2,0.2)", (0.2, 0.2), 1.0, 500, "gaussian", "Moderate Gaussian residual noise."),
            MCScenario("noise_v05", "V=(0.5,0.5)", (0.5, 0.5), 1.0, 500, "gaussian", "High Gaussian residual noise."),
        ),
    ),
    MCBlock(
        name="nongaussianity_grid",
        label="Structural non-Gaussianity grid",
        figure_matched="Figure 2",
        note="Matches Figure 2: residual noise is fixed and structural higher moments weaken.",
        scenarios=(
            MCScenario("nongaussian_w1", "w=1", (0.2, 0.2), 1.0, 500, "gaussian", "Strong structural non-Gaussianity."),
            MCScenario("nongaussian_w025", "w=0.25", (0.2, 0.2), 0.25, 500, "gaussian", "Weak structural non-Gaussianity."),
            MCScenario("nongaussian_w0", "w=0", (0.2, 0.2), 0.0, 500, "gaussian", "Gaussian structural-shock limit."),
        ),
    ),
    MCBlock(
        name="sample_size_grid",
        label="Sample-size grid",
        figure_matched="Figure 3",
        note="Matches Figure 3: residual noise and structural non-Gaussianity are fixed while T varies.",
        scenarios=(
            MCScenario("sample_t500", "T=500", (0.2, 0.2), 1.0, 500, "gaussian", "Baseline sample size."),
            MCScenario("sample_t1000", "T=1000", (0.2, 0.2), 1.0, 1000, "gaussian", "Medium sample size."),
            MCScenario("sample_t2000", "T=2000", (0.2, 0.2), 1.0, 2000, "gaussian", "Large sample size."),
        ),
    ),
)


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def block_map() -> dict[str, MCBlock]:
    return {block.name: block for block in BLOCKS}


def selected_blocks(name: str) -> tuple[MCBlock, ...]:
    if name == "all":
        return BLOCKS
    return (block_map()[name],)


def seed_for(base_seed: int, block_index: int, scenario_index: int, rep: int) -> int:
    return int(base_seed + 200_000 + block_index * 100_000 + scenario_index * 10_000 + rep)


def finite_values(values: list[Any]) -> list[float]:
    out: list[float] = []
    for value in values:
        if value is None:
            continue
        numeric = float(value)
        if math.isfinite(numeric):
            out.append(numeric)
    return out


def numeric_summary(values: list[Any]) -> dict[str, Any]:
    finite = finite_values(values)
    if not finite:
        return {
            "n": 0,
            "mean": None,
            "median": None,
            "se": None,
            "min": None,
            "max": None,
        }
    array = np.asarray(finite, dtype=float)
    se = None if array.size <= 1 else float(np.std(array, ddof=1) / math.sqrt(array.size))
    return {
        "n": int(array.size),
        "mean": float(np.mean(array)),
        "median": float(np.median(array)),
        "se": se,
        "min": float(np.min(array)),
        "max": float(np.max(array)),
    }


def count_rate(values: list[Any]) -> dict[str, Any]:
    finite = finite_values(values)
    count = int(sum(1 for value in finite if value >= 0.5))
    total = int(len(finite))
    summary = numeric_summary(finite)
    return {
        "count": count,
        "total": total,
        "rate": summary["mean"],
        "se": summary["se"],
    }


def summarize(records: list[dict[str, Any]], blocks: tuple[MCBlock, ...]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for block in blocks:
        for scenario in block.scenarios:
            subset = [
                record
                for record in records
                if record["block"] == block.name and record["scenario"] == scenario.name
            ]
            metrics = [record["metrics"] for record in subset]
            summaries.append(
                {
                    "block": block.name,
                    "block_label": block.label,
                    "figure_matched": block.figure_matched,
                    "scenario": scenario.name,
                    "label": scenario.label,
                    "reps": len(subset),
                    "noise": list(scenario.noise),
                    "non_gaussian_weight": scenario.non_gaussian_weight,
                    "sample_size": scenario.sample_size,
                    "residual_noise": scenario.residual_noise,
                    "truth_inclusion": {
                        "standard_dw": count_rate([m["standard_dw"]["truth_in"] for m in metrics]),
                        "robust_dw": count_rate([m["robust_dw"]["truth_in"] for m in metrics]),
                    },
                    "warning": count_rate([m["warning"] for m in metrics]),
                    "size": {
                        "measure": "accepted projection share on the displayed (B11,B21) grid",
                        "sign": numeric_summary([m["sign"]["accepted_share"] for m in metrics]),
                        "standard_dw": numeric_summary([m["standard_dw"]["accepted_share"] for m in metrics]),
                        "robust_dw": numeric_summary([m["robust_dw"]["accepted_share"] for m in metrics]),
                        "standard_count": numeric_summary([m["standard_dw"]["accepted_count"] for m in metrics]),
                        "robust_count": numeric_summary([m["robust_dw"]["accepted_count"] for m in metrics]),
                    },
                    "empty": {
                        "standard_dw": count_rate([m["standard_dw"]["empty"] for m in metrics]),
                        "robust_dw": count_rate([m["robust_dw"]["empty"] for m in metrics]),
                    },
                    "overlap": {
                        "jaccard": numeric_summary([m["overlap"]["jaccard"] for m in metrics]),
                        "d_standard_not_subset_robust": numeric_summary(
                            [m["overlap"]["d_standard_not_subset_robust"] for m in metrics]
                        ),
                    },
                    "distance_to_truth_projection": {
                        "standard_dw": numeric_summary(
                            [m["standard_dw"]["distance_to_truth_projection"] for m in metrics]
                        ),
                        "robust_dw": numeric_summary(
                            [m["robust_dw"]["distance_to_truth_projection"] for m in metrics]
                        ),
                    },
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


def fmt_rate(item: dict[str, Any]) -> str:
    return f"{item['count']}/{item['total']} ({fmt(item['rate'])}; se {fmt(item['se'])})"


def fmt_mean(item: dict[str, Any]) -> str:
    return f"{fmt(item['mean'])} (se {fmt(item['se'])})"


def fmt_median(item: dict[str, Any]) -> str:
    return fmt(item["median"])


def write_outputs(
    records: list[dict[str, Any]],
    summaries: list[dict[str, Any]],
    blocks: tuple[MCBlock, ...],
    spec: fig.GridSpec,
    reps: int,
    json_output: Path,
    note_output: Path,
    quick: bool,
) -> None:
    payload = {
        "schema_version": 1,
        "task": "M71 corrected extended three-block Monte Carlo",
        "description": "Extended MC aligned with the three active figure blocks after M71. Uses the same M66 unit-variance projected GMM evaluator with no B21 sign restriction and candidate-specific pointwise weights.",
        "configuration": {
            "quick": quick,
            "reps_per_scenario": reps,
            "base_seed": fig.RANDOM_SEED,
            "rho": fig.RELATIVE_NOISE_RATIO,
            "projection_points": spec.projection_points,
            "profile_points": spec.profile_points,
            "lambda_points": spec.lambda_points,
            "displayed_projection": ["B11", "B21"],
            "profiled_coordinates": ["B12", "B22", "lambda1", "lambda2"],
            "sign_restrictions": ["B11 > 0", "B22 > 0", "B12 <= 0"],
            "set_size_measure": "accepted projection share on the displayed (B11,B21) grid",
            "weighting": "candidate-specific pointwise covariance estimates for each tested B or (B,lambda) candidate",
            "weight_regularization": "symmetric covariance eigensystem with eigenvalue floor max(max_eigenvalue, 1) * 1e-10",
            "critical_values": {
                "second_moment_chi2_90_df3": fig.CHI2_90_DF3,
                "standard_dw_chi2_90_df5": fig.CHI2_90_DF5,
                "robust_full_moment_chi2_90_df8": fig.CHI2_90_DF8,
            },
            "inference_caveat": "Pointwise chi-square diagnostics only; final projected critical values remain M65 follow-up.",
            "blocks": [
                {
                    "name": block.name,
                    "label": block.label,
                    "figure_matched": block.figure_matched,
                    "note": block.note,
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
                        for scenario in block.scenarios
                    ],
                }
                for block in blocks
            ],
        },
        "summaries": summaries,
        "records": records,
    }
    json_output.parent.mkdir(parents=True, exist_ok=True)
    json_output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# M71 Corrected Extended Three-Block Monte Carlo",
        "",
        "Status: generated corrected extended MC output aligned with the three active figure blocks.",
        "",
        "The set-size measure is the accepted share of the displayed `(B11,B21)` projection grid. The table reports both mean and median set size for the standard-DW and robust-DW inverted sets. Truth inclusion is reported as counts and rates.",
        "",
        "The statistics use candidate-specific pointwise covariance estimates for each tested candidate. The cutoffs are pointwise chi-square diagnostics for the displayed moment rows. Final projected confidence-set critical values remain M65 follow-up.",
        "",
        "## Configuration",
        "",
        f"- Machine-readable output: `{display_path(json_output)}`.",
        f"- Quick run: `{quick}`.",
        f"- Replications per scenario: `{reps}`.",
        f"- Projection grid: `{spec.projection_points} x {spec.projection_points}`.",
        f"- Profile grid: `{spec.profile_points} x {spec.profile_points}`.",
        f"- Lambda grid: `{spec.lambda_points} x {spec.lambda_points}`.",
        "- Sign screen: `B11>0`, `B22>0`, `B12<=0`; `B21` is not sign-restricted.",
        "- Robust route: `nu_i=lambda_i(BB')_ii`, `lambda in [0,rho]^2`.",
        "",
    ]
    for block in blocks:
        lines.extend(
            [
                f"## {block.label}",
                "",
                f"Matched figure: {block.figure_matched}. {block.note}",
                "",
                "| Scenario | S truth | R truth | Warning | S size mean | S size median | R size mean | R size median | S empty | R empty |",
                "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for item in summaries:
            if item["block"] != block.name:
                continue
            lines.append(
                "| {label} | {s_truth} | {r_truth} | {warning} | {s_mean} | {s_median} | {r_mean} | {r_median} | {s_empty} | {r_empty} |".format(
                    label=item["label"],
                    s_truth=fmt_rate(item["truth_inclusion"]["standard_dw"]),
                    r_truth=fmt_rate(item["truth_inclusion"]["robust_dw"]),
                    warning=fmt_rate(item["warning"]),
                    s_mean=fmt_mean(item["size"]["standard_dw"]),
                    s_median=fmt_median(item["size"]["standard_dw"]),
                    r_mean=fmt_mean(item["size"]["robust_dw"]),
                    r_median=fmt_median(item["size"]["robust_dw"]),
                    s_empty=fmt_rate(item["empty"]["standard_dw"]),
                    r_empty=fmt_rate(item["empty"]["robust_dw"]),
                )
            )
        lines.append("")
    lines.extend(
        [
            "## Claim Audit",
            "",
            "| Claim | Status | Evidence | Confidence | Action |",
            "|---|---|---|---|---|",
            "| Extended MC mirrors the three active figure blocks. | `code-implemented`, `user-decision` | Scenario block configuration in this script and JSON. | high | promote as M69 setup result |",
            "| Inverted-set size is measured by accepted projection share on `(B11,B21)`. | `code-implemented`, `user-decision` | `size` summaries in JSON and table. | high | promote as diagnostic size metric |",
            "| Truth inclusion is counted for standard-DW and robust-DW sets. | `code-implemented`, `user-decision` | `truth_inclusion` count/rate summaries in JSON and table. | high | promote as MC diagnostic |",
            "| M71 removes the `B21>=0` sign restriction from the extended MC. | `code-implemented`, `user-decision` | Scenario block configuration and shared evaluator. | high | promote |",
            "| M71 uses candidate-specific pointwise covariance weights. | `code-implemented`, `user-decision` | Shared evaluator calls through `j_from_observations`. | high | promote |",
            "| Robust MC uses `nu_i=lambda_i(BB')_ii` and profiles `lambda in [0,rho]^2`. | `code-implemented`, `derived` | M66 route reused through M68 evaluator calls. | high | promote |",
            "| The chi-square cutoffs are final projected confidence-set critical values. | `conjectural` | M65 remains open for projected critical values. | medium | quarantine as diagnostic |",
            "",
        ]
    )
    note_output.parent.mkdir(parents=True, exist_ok=True)
    note_output.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def run(
    blocks: tuple[MCBlock, ...],
    json_output: Path = JSON_OUTPUT,
    note_output: Path = NOTE_OUTPUT,
    reps: int = 8,
    spec: fig.GridSpec = fig.GridSpec(projection_points=13, profile_points=5, lambda_points=3),
    quick: bool = False,
) -> Path:
    grid = fig.make_candidate_grid(spec)
    records: list[dict[str, Any]] = []
    all_blocks = block_map()
    for block in blocks:
        block_index = list(all_blocks).index(block.name)
        for scenario_index, scenario in enumerate(block.scenarios):
            for rep in range(reps):
                seed = seed_for(fig.RANDOM_SEED, block_index, scenario_index, rep)
                metrics = m68.evaluate_one(scenario, seed, grid, spec)
                records.append(
                    {
                        "block": block.name,
                        "block_label": block.label,
                        "figure_matched": block.figure_matched,
                        "scenario": scenario.name,
                        "label": scenario.label,
                        "rep": rep,
                        "seed": seed,
                        "metrics": metrics,
                    }
                )
    summaries = summarize(records, blocks)
    write_outputs(records, summaries, blocks, spec, reps, json_output, note_output, quick)
    return note_output


def parse_args() -> argparse.Namespace:
    choices = ("all",) + tuple(block.name for block in BLOCKS)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--block", choices=choices, default="all", help="Which MC block to run.")
    parser.add_argument("--json-output", default="", help="Optional JSON output path.")
    parser.add_argument("--note-output", default="", help="Optional Markdown note output path.")
    parser.add_argument("--evaluation-reps", type=int, default=8)
    parser.add_argument("--projection-points", type=int, default=13)
    parser.add_argument("--profile-points", type=int, default=5)
    parser.add_argument("--lambda-points", type=int, default=3)
    parser.add_argument("--robust-batch-size", type=int, default=36)
    parser.add_argument("--standard-batch-size", type=int, default=240)
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Use a small smoke-test grid and write default outputs under replication/output/quick.",
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
    if args.quick and not args.json_output:
        json_output = QUICK_OUTPUT_DIR / "m69_extended_three_block_mc.json"
    else:
        json_output = Path(args.json_output) if args.json_output else JSON_OUTPUT
    if args.quick and not args.note_output:
        note_output = QUICK_OUTPUT_DIR / "m69_extended_three_block_mc.md"
    else:
        note_output = Path(args.note_output) if args.note_output else NOTE_OUTPUT

    path = run(
        blocks=selected_blocks(args.block),
        json_output=json_output,
        note_output=note_output,
        reps=reps,
        spec=spec,
        quick=args.quick,
    )
    print(f"Wrote {display_path(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
