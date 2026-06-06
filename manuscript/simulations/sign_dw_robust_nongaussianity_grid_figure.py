"""Build a sign/DW/robust-DW grid varying structural non-Gaussianity.

This companion to sign_dw_robust_noise_grid_figure.py fixes moderate residual
noise and changes only the strength of structural-shock higher moments. The
bottom row is the pure robust-DW higher-cumulant population set: it deliberately
does not use the covariance moment or any other second-moment restriction.
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

FIXED_NOISE = (0.3, 0.3)
NON_GAUSSIANITY_LEVELS = (
    ("Strong non-Gaussianity", 1.00),
    ("Weak non-Gaussianity", 0.25),
    ("Gaussian shocks", 0.00),
)
CHI2_95_DF5 = 11.070497693516351
ROBUST_POPULATION_CUTOFF = CHI2_95_DF5 / base.SAMPLE_SIZE


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


def structural_cumulants(non_gaussian_weight: float) -> tuple[float, float]:
    """Population cumulants for sqrt(w) * skewed + sqrt(1-w) * Gaussian.

    The base skewed component is the same standardized chi-square(df)
    calibration used by the noise-grid script.  The Gaussian component
    contributes no cumulants above order two.
    """
    gamma = base.STRUCTURAL_THIRD_CUMULANT * non_gaussian_weight ** 1.5
    kappa = base.STRUCTURAL_FOURTH_CUMULANT * non_gaussian_weight**2
    return gamma, kappa


def pure_robust_population_score(
    b12_mesh: np.ndarray,
    b21_mesh: np.ndarray,
    non_gaussian_weight: float,
) -> np.ndarray:
    gamma, kappa = structural_cumulants(non_gaussian_weight)
    determinant = 1.0 - b12_mesh * b21_mesh
    valid = np.abs(determinant) > 1e-10
    alpha = np.full_like(b12_mesh, np.nan, dtype=float)
    beta = np.full_like(b12_mesh, np.nan, dtype=float)
    c = np.full_like(b12_mesh, np.nan, dtype=float)
    d = np.full_like(b12_mesh, np.nan, dtype=float)
    alpha[valid] = (1.0 - b12_mesh[valid] * base.TRUE_B21) / determinant[valid]
    beta[valid] = (base.TRUE_B12 - b12_mesh[valid]) / determinant[valid]
    c[valid] = (base.TRUE_B21 - b21_mesh[valid]) / determinant[valid]
    d[valid] = (1.0 - b21_mesh[valid] * base.TRUE_B12) / determinant[valid]

    c112 = gamma * (alpha * alpha * c + beta * beta * d)
    c122 = gamma * (alpha * c * c + beta * d * d)
    c1112 = kappa * (alpha**3 * c + beta**3 * d)
    c1122 = kappa * (alpha * alpha * c * c + beta * beta * d * d)
    c1222 = kappa * (alpha * c**3 + beta * d**3)
    return (
        (c112 / 2.0) ** 2
        + (c122 / 2.0) ** 2
        + (c1112 / 6.0) ** 2
        + (c1122 / 6.0) ** 2
        + (c1222 / 6.0) ** 2
    )


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
        robust_score = pure_robust_population_score(b12_mesh, b21_mesh, non_gaussian_weight)
        robust_accepted = (
            (b21_mesh >= 0.0)
            & (np.abs(1.0 - b12_mesh * b21_mesh) > 1e-10)
            & np.isfinite(robust_score)
            & (robust_score <= ROBUST_POPULATION_CUTOFF)
        )

        column_title = f"{label}\nw={non_gaussian_weight:g}; sample excess kurt=({kurtosis[0]:.2f},{kurtosis[1]:.2f})"

        ax = axes[0, col]
        base.shade(ax, b12_mesh, b21_mesh, covariance_accepted, "#9bc9a6", 0.9)
        base.draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title(f"{column_title}\nSign/covariance N-test")
        ax.text(-1.22, 1.16, base.min_label(covariance_j), color="#11623a", fontsize=9)

        ax = axes[1, col]
        base.shade(ax, b12_mesh, b21_mesh, covariance_accepted, "#d9d9d9", 0.55)
        base.shade(ax, b12_mesh, b21_mesh, dw_accepted, "#6a51a3", 0.9)
        base.draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title("Standard DW N-test")
        ax.text(-1.22, 1.16, base.min_label(dw_j), color="#542788", fontsize=9)

        ax = axes[2, col]
        base.shade(ax, b12_mesh, b21_mesh, robust_accepted, "#67a9cf", 0.88)
        if np.isfinite(robust_score).any() and robust_accepted.any() and non_gaussian_weight > 0.0:
            ax.contour(
                b12_mesh,
                b21_mesh,
                robust_score,
                levels=[ROBUST_POPULATION_CUTOFF],
                colors=["#2166ac"],
                linewidths=1.2,
            )
        base.draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title("Robust DW: higher cumulants only")
        if non_gaussian_weight == 0.0:
            label_text = "all admissible B accepted"
        else:
            label_text = f"min score {np.nanmin(robust_score):.3g}"
        ax.text(-1.22, 1.16, label_text, color="#2166ac", fontsize=9)

    for ax in axes.flat:
        base.add_common_panel_style(ax, b12_grid, b21_grid)

    for ax in axes[2, :]:
        ax.set_xlabel("b12")
    for ax in axes[:, 0]:
        ax.set_ylabel("b21")
    axes[0, 0].legend(loc="lower left", frameon=True, framealpha=0.9, fontsize=8)

    fig.suptitle(
        (
            "Same B-plane and fixed residual noise V=(0.3,0.3); columns weaken structural non-Gaussianity\n"
            f"Top/middle: N={base.SAMPLE_SIZE} pointwise tests. Bottom: population higher-cumulant robust DW, no second moments."
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
