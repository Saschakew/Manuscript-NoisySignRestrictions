"""Build a sign/DW/robust-DW grid varying structural non-Gaussianity.

This companion to sign_dw_robust_noise_grid_figure.py fixes moderate residual
noise and changes only the strength of structural-shock higher moments. All
rows invert pointwise finite-sample J statistics at the 10 percent level. The
bottom row is the diagonal-noise robust-DW J test: it uses the off-diagonal
covariance restriction that survives diagonal residual noise, plus mixed
higher cumulants of transformed residuals.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np

try:
    from . import sign_dw_robust_noise_grid_figure as base
except ImportError:
    import sign_dw_robust_noise_grid_figure as base


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "manuscript" / "figures"
OUTPUT_PATH = OUTPUT_DIR / "fig_sign_dw_robust_nongaussianity_grid.png"

FIXED_NOISE = (0.2, 0.2)
NON_GAUSSIANITY_LEVELS = (
    ("Strong non-Gaussianity", 1.00),
    ("Weak non-Gaussianity", 0.25),
    ("Gaussian shocks", 0.00),
)


def structural_and_noise_draws(non_gaussian_weight: float) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(base.RANDOM_SEED)
    skewed = base.standardize_columns(rng.chisquare(df=base.STRUCTURAL_CHI2_DF, size=(base.SAMPLE_SIZE, 2)))
    gaussian = base.standardize_columns(rng.normal(size=(base.SAMPLE_SIZE, 2)))
    structural = math.sqrt(non_gaussian_weight) * skewed + math.sqrt(1.0 - non_gaussian_weight) * gaussian
    structural = base.standardize_columns(structural)
    noise = base.standardize_columns(rng.normal(size=(base.SAMPLE_SIZE, 2)))
    return structural, noise


def simulate_residuals(non_gaussian_weight: float) -> np.ndarray:
    structural, noise = structural_and_noise_draws(non_gaussian_weight)
    nu1, nu2 = FIXED_NOISE
    residuals = structural @ base.TRUE_MATRIX.T
    residuals[:, 0] += math.sqrt(nu1) * noise[:, 0]
    residuals[:, 1] += math.sqrt(nu2) * noise[:, 1]
    return residuals - residuals.mean(axis=0, keepdims=True)


def excess_kurtosis(values: np.ndarray) -> np.ndarray:
    standardized = base.standardize_columns(values)
    return np.mean(standardized**4, axis=0) - 3.0


def plot() -> Path:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

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

    for col, (label, non_gaussian_weight) in enumerate(NON_GAUSSIANITY_LEVELS):
        structural, noise = structural_and_noise_draws(non_gaussian_weight)
        nu1, nu2 = FIXED_NOISE
        residuals = structural @ base.TRUE_MATRIX.T
        residuals[:, 0] += math.sqrt(nu1) * noise[:, 0]
        residuals[:, 1] += math.sqrt(nu2) * noise[:, 1]
        residuals = residuals - residuals.mean(axis=0, keepdims=True)
        kurtosis = excess_kurtosis(structural)

        (
            b12_mesh,
            b21_mesh,
            correlation,
            covariance_j,
            covariance_accepted,
            dw_j,
            dw_accepted,
        ) = base.evaluate_standard_grid(residuals, nu1, nu2, b12_grid, b21_grid)
        _, _, robust_j, robust_accepted = base.evaluate_robust_grid(residuals, b12_grid, b21_grid)

        true_shocks = base.standardized_candidate_shocks(base.TRUE_B12, base.TRUE_B21, residuals)
        true_covariance_j = math.nan
        true_dw_j = math.nan
        if true_shocks is not None:
            true_covariance_j = base.j_statistic(true_shocks, base.MOMENTS_COVARIANCE)
            true_dw_j = base.j_statistic(true_shocks, base.MOMENTS_DW)
        true_robust_j = base.robust_j_statistic(base.TRUE_B12, base.TRUE_B21, residuals)

        column_title = f"{label}\nw={non_gaussian_weight:g}; sample excess kurt=({kurtosis[0]:.2f},{kurtosis[1]:.2f})"

        ax = axes[0, col]
        base.shade(ax, b12_mesh, b21_mesh, covariance_accepted, "#9bc9a6", 0.9)
        base.draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title(f"{column_title}\nSign/covariance J-test")
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
        ax.set_title("Standard DW J-test")
        ax.text(
            -1.22,
            1.16,
            f"{base.min_label(dw_j)}\n{base.truth_label(true_dw_j, base.CHI2_90_DF4)}",
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
                levels=[base.CHI2_90_DF6],
                colors=["#2166ac"],
                linewidths=1.2,
            )
        base.draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title("Robust DW J-test")
        robust_label_lines = [
            base.min_label(robust_j),
            base.truth_label(true_robust_j, base.CHI2_90_DF6),
        ]
        if non_gaussian_weight == 0.0:
            robust_label_lines.insert(0, "cumulants all-null")
        ax.text(-1.22, 1.16, "\n".join(robust_label_lines), color="#2166ac", fontsize=9)

    for ax in axes.flat:
        base.add_common_panel_style(ax, b12_grid, b21_grid)

    for ax in axes[2, :]:
        ax.set_xlabel("b12")
    for ax in axes[:, 0]:
        ax.set_ylabel("b21")
    axes[0, 0].legend(loc="lower left", frameon=True, framealpha=0.9, fontsize=8)

    fig.suptitle(
        (
            f"Same B-plane and fixed residual noise V=({FIXED_NOISE[0]:g},{FIXED_NOISE[1]:g}); "
            "columns weaken structural non-Gaussianity\n"
            f"N={base.SAMPLE_SIZE}; all rows invert pointwise 10% J tests; "
            "robust DW profiles diagonal noise and adds mixed higher cumulants"
        ),
        fontsize=13,
    )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=180)
    plt.close(fig)
    return OUTPUT_PATH


if __name__ == "__main__":
    path = plot()
    print(f"Wrote {path.relative_to(ROOT)}")
