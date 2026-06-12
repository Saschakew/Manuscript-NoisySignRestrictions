"""Rebuild the active manuscript figures and Monte Carlo evidence.

This is the M33 manuscript-local replication wrapper, updated in M71. The
active stages use the unit-variance first-shock chart: display ``(B11,B21)``,
profile ``B12``, ``B22``, and ``lambda``, impose ``B11>0``, ``B22>0``, and
``B12<=0``, and evaluate the M66 ``nu_i=lambda_i(BB')_ii`` route with
candidate-specific pointwise covariance weights.
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
            output_dir / "m68_first_shock_evidence.json",
            output_dir / "m68_first_shock_evidence.md",
        )
    return (
        SIM_DIR / "output" / "m68_first_shock_evidence.json",
        SIM_DIR / "m68_first_shock_evidence.md",
    )


def extended_mc_outputs(output_dir: Path | None) -> tuple[Path, Path]:
    if output_dir is not None:
        return (
            output_dir / "m69_extended_three_block_mc.json",
            output_dir / "m69_extended_three_block_mc.md",
        )
    return (
        SIM_DIR / "output" / "m69_extended_three_block_mc.json",
        SIM_DIR / "m69_extended_three_block_mc.md",
    )


def build_steps(args: argparse.Namespace) -> list[Step]:
    output_dir = output_dir_from_args(args)
    steps: list[Step] = []

    figure_commands = {
        "figure1": [
            sys.executable,
            str(SIM_DIR / "sign_dw_unit_variance_noise_grid_figure.py"),
            "--scenario-set",
            "noise",
            "--output",
            str(figure_output(output_dir, "fig_sign_dw_unit_variance_noise_grid.png")),
            "--note-output",
            str((output_dir or SIM_DIR) / "sign_dw_unit_variance_noise_grid_figure.md"),
            "--json-output",
            str((output_dir or (SIM_DIR / "output")) / "sign_dw_unit_variance_noise_grid_figure.json"),
        ],
        "figure2": [
            sys.executable,
            str(SIM_DIR / "sign_dw_unit_variance_noise_grid_figure.py"),
            "--scenario-set",
            "nongaussianity",
            "--output",
            str(figure_output(output_dir, "fig_sign_dw_unit_variance_nongaussianity_grid.png")),
            "--note-output",
            str((output_dir or SIM_DIR) / "sign_dw_unit_variance_nongaussianity_grid_figure.md"),
            "--json-output",
            str((output_dir or (SIM_DIR / "output")) / "sign_dw_unit_variance_nongaussianity_grid_figure.json"),
        ],
        "figure3": [
            sys.executable,
            str(SIM_DIR / "sign_dw_unit_variance_noise_grid_figure.py"),
            "--scenario-set",
            "sample_size",
            "--output",
            str(figure_output(output_dir, "fig_sign_dw_unit_variance_sample_size_grid.png")),
            "--note-output",
            str((output_dir or SIM_DIR) / "sign_dw_unit_variance_sample_size_grid_figure.md"),
            "--json-output",
            str((output_dir or (SIM_DIR / "output")) / "sign_dw_unit_variance_sample_size_grid_figure.json"),
        ],
    }

    if args.quick:
        for command in figure_commands.values():
            command.extend(
                [
                    "--projection-points",
                    "9",
                    "--profile-points",
                    "5",
                    "--lambda-points",
                    "3",
                ]
            )

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
            str(SIM_DIR / "m68_first_shock_evidence.py"),
            "--json-output",
            str(json_output),
            "--note-output",
            str(note_output),
        ]
        if args.quick:
            command.extend(
                [
                    "--evaluation-reps",
                    "1",
                    "--projection-points",
                    "7",
                    "--profile-points",
                    "5",
                    "--lambda-points",
                    "3",
                ]
            )
        steps.append(Step("M68 Monte Carlo evidence", command))

    if args.stage == "extended-mc":
        json_output, note_output = extended_mc_outputs(output_dir)
        command = [
            sys.executable,
            str(SIM_DIR / "m69_extended_three_block_mc.py"),
            "--json-output",
            str(json_output),
            "--note-output",
            str(note_output),
        ]
        if args.quick:
            command.append("--quick")
        steps.append(Step("M69 extended three-block Monte Carlo", command))

    return steps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--stage",
        choices=("all", "figures", "figure1", "figure2", "figure3", "evidence", "extended-mc"),
        default="all",
        help="Replication stage to run.",
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Use small figure/Monte Carlo settings and write outputs under replication/output/quick.",
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
