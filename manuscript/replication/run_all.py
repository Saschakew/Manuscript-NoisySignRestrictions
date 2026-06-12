"""Rebuild the active manuscript figures and Monte Carlo evidence.

This is the M33 manuscript-local replication wrapper. It calls the
manuscript-local simulation scripts that produced the active M52 figures and
table, without depending on a local KnowledgeVault checkout.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPLICATION_DIR = Path(__file__).resolve().parent
SIM_DIR = ROOT / "manuscript" / "simulations"
FIGURE_DIR = ROOT / "manuscript" / "figures"
QUICK_OUTPUT_DIR = REPLICATION_DIR / "output" / "quick"


@dataclass(frozen=True)
class Step:
    name: str
    command: list[str]


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def output_dir_from_args(args: argparse.Namespace) -> Path | None:
    if args.output_dir:
        requested = Path(args.output_dir)
        return requested if requested.is_absolute() else REPLICATION_DIR / requested
    if args.quick:
        return QUICK_OUTPUT_DIR
    return None


def figure_output(output_dir: Path | None, filename: str) -> Path:
    if output_dir is not None:
        return output_dir / filename
    return FIGURE_DIR / filename


def evidence_outputs(output_dir: Path | None) -> tuple[Path, Path]:
    if output_dir is not None:
        return (
            output_dir / "m52_source_correct_evidence.json",
            output_dir / "m52_source_correct_evidence.md",
        )
    return (
        SIM_DIR / "output" / "m52_source_correct_evidence.json",
        SIM_DIR / "m52_source_correct_evidence.md",
    )


def build_steps(args: argparse.Namespace) -> list[Step]:
    output_dir = output_dir_from_args(args)
    steps: list[Step] = []

    figure_commands = {
        "figure1": [
            sys.executable,
            str(SIM_DIR / "sign_dw_robust_noise_grid_figure.py"),
            "--robust-mode",
            "relative",
            "--output",
            str(figure_output(output_dir, "fig_sign_dw_relative_noise_robust_grid.png")),
        ],
        "figure2": [
            sys.executable,
            str(SIM_DIR / "sign_dw_robust_nongaussianity_grid_figure.py"),
            "--output",
            str(figure_output(output_dir, "fig_sign_dw_robust_nongaussianity_grid.png")),
        ],
        "figure3": [
            sys.executable,
            str(SIM_DIR / "sign_dw_sample_size_robust_grid_figure.py"),
            "--output",
            str(figure_output(output_dir, "fig_sign_dw_sample_size_robust_grid.png")),
        ],
    }

    if args.stage in {"all", "figures", "figure1"}:
        steps.append(Step("Figure 1 residual-noise grid", figure_commands["figure1"]))
    if args.stage in {"all", "figures", "figure2"}:
        steps.append(Step("Figure 2 non-Gaussianity grid", figure_commands["figure2"]))
    if args.stage in {"all", "figures", "figure3"}:
        steps.append(Step("Figure 3 sample-size grid", figure_commands["figure3"]))

    if args.stage in {"all", "evidence"}:
        json_output, note_output = evidence_outputs(output_dir)
        command = [
            sys.executable,
            str(SIM_DIR / "m45_variance_ratio_evidence.py"),
            "--json-output",
            str(json_output),
            "--note-output",
            str(note_output),
        ]
        if args.quick:
            command.extend(
                [
                    "--diagnostic-grid-points",
                    "11",
                    "--calibration-reps",
                    "2",
                    "--evaluation-reps",
                    "1",
                    "--grid-points",
                    "9",
                ]
            )
        steps.append(Step("M52 Monte Carlo evidence", command))

    return steps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--stage",
        choices=("all", "figures", "figure1", "figure2", "figure3", "evidence"),
        default="all",
        help="Replication stage to run.",
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Use small Monte Carlo settings and write outputs under replication/output/quick.",
    )
    parser.add_argument(
        "--output-dir",
        default="",
        help="Optional output directory, resolved relative to manuscript/replication.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print commands without running them.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    steps = build_steps(args)
    if not steps:
        raise SystemExit("No replication steps selected.")

    for step in steps:
        print(f"[{step.name}]", flush=True)
        print("> " + subprocess.list2cmdline(step.command), flush=True)
        if args.dry_run:
            continue
        subprocess.run(step.command, cwd=ROOT, check=True)

    if args.quick and not args.output_dir:
        print(f"Quick outputs: {display_path(QUICK_OUTPUT_DIR)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
