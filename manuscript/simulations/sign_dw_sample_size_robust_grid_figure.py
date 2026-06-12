"""Build the historical sign/DW/relative-robust-DW sample-size grid.

This companion to the residual-noise and non-Gaussianity grids fixes the
structural-shock calibration and residual-noise variance, then varies only the
finite-sample size.  The bottom row uses the M0036 variance-ratio robust-DW
proposal: pure mixed higher-cumulant J inversion intersected with the
covariance-decomposition screen in which each diagonal residual-noise variance
is at most half of the corresponding structural-shock variance.

After M64/M66 this script is historical. It reuses the pre-M64
diagonal-normalized B-plane implementation and does not implement the active
unit-variance projected GMM algorithm over B and lambda.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np

try:
    from . import sign_dw_robust_noise_grid_figure as base
except ImportError:
    import sign_dw_robust_noise_grid_figure as base


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "manuscript" / "figures"
OUTPUT_PATH = OUTPUT_DIR / "fig_sign_dw_sample_size_robust_grid.png"

FIXED_NOISE = (0.2, 0.2)
SAMPLE_SIZE_LEVELS = (
    ("T=500", 500),
    ("T=1000", 1000),
    ("T=2000", 2000),
)
ROBUST_MODE = "relative"
ROBUST_CUTOFF = base.robust_mode_cutoff(ROBUST_MODE)


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def structural_and_noise_draws(sample_size: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(base.RANDOM_SEED)
    structural = base.standardize_columns(
        rng.chisquare(df=base.STRUCTURAL_CHI2_DF, size=(sample_size, 2))
    )
    noise = base.standardize_columns(rng.normal(size=(sample_size, 2)))
    return structural, noise


def simulate_residuals(sample_size: int) -> np.ndarray:
    structural, noise = structural_and_noise_draws(sample_size)
    residuals = structural @ base.TRUE_MATRIX.T
    residuals[:, 0] += math.sqrt(FIXED_NOISE[0]) * noise[:, 0]
    residuals[:, 1] += math.sqrt(FIXED_NOISE[1]) * noise[:, 1]
    return residuals - residuals.mean(axis=0, keepdims=True)


def plot(output_path: Path | None = None) -> Path:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    if output_path is None:
        output_path = OUTPUT_PATH

    b12_grid = np.linspace(-1.35, 0.35, base.GRID_POINTS)
    b21_grid = np.linspace(-0.25, 1.35, base.GRID_POINTS)
    fig, axes = plt.subplots(
        3,
        3,
        figsize=(15.4, 11.2),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    for col, (label, sample_size) in enumerate(SAMPLE_SIZE_LEVELS):
        residuals = simulate_residuals(sample_size)
        nu1, nu2 = FIXED_NOISE
        (
            b12_mesh,
            b21_mesh,
            correlation,
            covariance_j,
            covariance_accepted,
            dw_j,
            dw_accepted,
        ) = base.evaluate_standard_grid(residuals, nu1, nu2, b12_grid, b21_grid)
        _, _, robust_j, robust_accepted = base.evaluate_robust_grid(
            residuals,
            b12_grid,
            b21_grid,
            ROBUST_MODE,
        )

        true_shocks = base.standardized_candidate_shocks(base.TRUE_B12, base.TRUE_B21, residuals)
        true_covariance_j = math.nan
        true_dw_j = math.nan
        if true_shocks is not None:
            true_covariance_j = base.j_statistic(true_shocks, base.MOMENTS_COVARIANCE)
            true_dw_j = base.j_statistic(true_shocks, base.MOMENTS_DW)
        true_robust_j = base.robust_mode_statistic(
            base.TRUE_B12,
            base.TRUE_B21,
            residuals,
            ROBUST_MODE,
        )
        true_robust_accepted = base.robust_mode_accepts(
            base.TRUE_B12,
            base.TRUE_B21,
            residuals,
            ROBUST_MODE,
            true_robust_j,
        )

        ax = axes[0, col]
        base.shade(ax, b12_mesh, b21_mesh, covariance_accepted, "#9bc9a6", 0.9)
        base.draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title(f"{label}\nSign/covariance J-test")
        ax.text(
            -1.22,
            1.16,
            f"{base.min_label(covariance_j)}\n{base.truth_label(true_covariance_j, base.CHI2_90_DF1)}",
            color="#11623a",
            fontsize=9,
        )

        ax = axes[1, col]
        base.shade(ax, b12_mesh, b21_mesh, covariance_accepted, "#d9d9d9", 0.55)
        base.shade(ax, b12_mesh, b21_mesh, dw_accepted, "#6a51a3", 0.9)
        base.draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title(base.standard_dw_title())
        ax.text(
            -1.22,
            1.16,
            f"{base.min_label(dw_j)}\n{base.standard_dw_truth_label(true_dw_j, true_covariance_j)}",
            color="#542788",
            fontsize=9,
        )

        ax = axes[2, col]
        base.shade(ax, b12_mesh, b21_mesh, robust_accepted, "#67a9cf", 0.88)
        if np.isfinite(robust_j).any() and robust_accepted.any():
            ax.contour(
                b12_mesh,
                b21_mesh,
                robust_j,
                levels=[ROBUST_CUTOFF],
                colors=["#2166ac"],
                linewidths=1.2,
            )
        base.draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title("Relative-noise robust DW")
        ax.text(
            -1.22,
            1.16,
            f"{base.min_label(robust_j)}\n{base.truth_label_with_status(true_robust_j, true_robust_accepted)}",
            color="#2166ac",
            fontsize=9,
        )

    for ax in axes.flat:
        base.add_common_panel_style(ax, b12_grid, b21_grid)

    for ax in axes[2, :]:
        ax.set_xlabel("b12")
    for ax in axes[:, 0]:
        ax.set_ylabel("b21")
    axes[0, 0].legend(loc="lower left", frameon=True, framealpha=0.9, fontsize=8)

    fig.suptitle(
        (
            f"Strong structural non-Gaussianity; fixed residual noise V=({FIXED_NOISE[0]:g},{FIXED_NOISE[1]:g}); "
            "columns vary sample size\n"
            + base.standard_dw_summary()
            + "; "
            + base.robust_mode_summary(ROBUST_MODE)
        ),
        fontsize=12,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="", help="Optional output path.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    path = plot(Path(args.output) if args.output else None)
    print(f"Wrote {display_path(path)}")
