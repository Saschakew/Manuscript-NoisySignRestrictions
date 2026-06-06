"""Build the sign/DW/pure-robust-DW B-plane noise grid figure.

This figure reproduces the KnowledgeVault B-plane layout with three noise
columns and adds a third robust-DW row.  All rows invert pointwise finite-sample
J statistics at the 10 percent level.  The robust-DW row uses mixed higher
cumulants only; second moments enter fourth-cumulant estimation as nuisance
terms, not as restrictions.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "manuscript" / "figures"
OUTPUT_PATH = OUTPUT_DIR / "fig_sign_dw_robust_noise_grid.png"

TRUE_B12 = -0.45
TRUE_B21 = 0.70
TRUE_MATRIX = np.array([[1.0, TRUE_B12], [TRUE_B21, 1.0]], dtype=float)

NOISE_LEVELS = ((0.0, 0.0), (0.3, 0.3), (2.0, 2.0))
SAMPLE_SIZE = 500
GRID_POINTS = 121
RANDOM_SEED = 20260605

CHI2_90_DF1 = 2.705543454095404
CHI2_90_DF4 = 7.779440339734858
CHI2_90_DF5 = 9.236356899781123
TEST_LEVEL = 0.10
STRUCTURAL_CHI2_DF = 5.0
STRUCTURAL_THIRD_CUMULANT = math.sqrt(8.0 / STRUCTURAL_CHI2_DF)
STRUCTURAL_FOURTH_CUMULANT = 12.0 / STRUCTURAL_CHI2_DF

MOMENTS_COVARIANCE = ((1, 1),)
MOMENTS_DW = ((1, 1), (2, 1), (1, 2), (2, 2))


def standardize_columns(values: np.ndarray) -> np.ndarray:
    values = values - values.mean(axis=0, keepdims=True)
    scale = values.std(axis=0, keepdims=True)
    if np.any(scale <= 1e-12):
        raise ValueError("cannot standardize a degenerate column")
    return values / scale


def primitive_draws(sample_size: int = SAMPLE_SIZE, seed: int = RANDOM_SEED) -> tuple[np.ndarray, np.ndarray]:
    """Use skewed structural shocks and Gaussian residual noise."""
    rng = np.random.default_rng(seed)
    structural = standardize_columns(rng.chisquare(df=STRUCTURAL_CHI2_DF, size=(sample_size, 2)))
    noise = standardize_columns(rng.normal(size=(sample_size, 2)))
    return structural, noise


def simulate_residuals(nu1: float, nu2: float) -> np.ndarray:
    structural, noise = primitive_draws()
    residuals = structural @ TRUE_MATRIX.T
    residuals[:, 0] += math.sqrt(nu1) * noise[:, 0]
    residuals[:, 1] += math.sqrt(nu2) * noise[:, 1]
    return residuals - residuals.mean(axis=0, keepdims=True)


def b_plane_covariance(nu1: float, nu2: float) -> np.ndarray:
    return TRUE_MATRIX @ TRUE_MATRIX.T + np.diag([nu1, nu2])


def b_plane_correlation_grid(
    b12_mesh: np.ndarray,
    b21_mesh: np.ndarray,
    reduced_covariance: np.ndarray,
) -> np.ndarray:
    s11 = reduced_covariance[0, 0]
    s12 = reduced_covariance[0, 1]
    s22 = reduced_covariance[1, 1]
    determinant = 1.0 - b12_mesh * b21_mesh
    omega11_scaled = s11 - 2.0 * b12_mesh * s12 + b12_mesh * b12_mesh * s22
    omega22_scaled = b21_mesh * b21_mesh * s11 - 2.0 * b21_mesh * s12 + s22
    omega12_scaled = (
        -b21_mesh * s11
        + (1.0 + b12_mesh * b21_mesh) * s12
        - b12_mesh * s22
    )
    valid = (np.abs(determinant) > 1e-10) & (omega11_scaled > 0.0) & (omega22_scaled > 0.0)
    correlation = np.full_like(b12_mesh, np.nan, dtype=float)
    correlation[valid] = omega12_scaled[valid] / np.sqrt(
        omega11_scaled[valid] * omega22_scaled[valid]
    )
    return correlation


def standardized_candidate_shocks(b12: float, b21: float, residuals: np.ndarray) -> np.ndarray | None:
    determinant = 1.0 - b12 * b21
    if abs(determinant) < 1e-10:
        return None
    inv_b = np.array([[1.0, -b12], [-b21, 1.0]], dtype=float) / determinant
    shocks = residuals @ inv_b.T
    shocks = shocks - shocks.mean(axis=0, keepdims=True)
    scale = shocks.std(axis=0, keepdims=True)
    if np.any(scale <= 1e-12):
        return None
    return shocks / scale


def candidate_shocks(b12: float, b21: float, residuals: np.ndarray) -> np.ndarray | None:
    determinant = 1.0 - b12 * b21
    if abs(determinant) < 1e-10:
        return None
    inv_b = np.array([[1.0, -b12], [-b21, 1.0]], dtype=float) / determinant
    shocks = residuals @ inv_b.T
    return shocks - shocks.mean(axis=0, keepdims=True)


def moment_target(power_pair: tuple[int, int]) -> float:
    return 1.0 if power_pair == (2, 2) else 0.0


def moment_observations(shocks: np.ndarray, powers: tuple[tuple[int, int], ...]) -> np.ndarray:
    first = shocks[:, 0]
    second = shocks[:, 1]
    return np.column_stack(
        [
            (first**power_1) * (second**power_2) - moment_target((power_1, power_2))
            for power_1, power_2 in powers
        ]
    )


def sample_moment_covariance(moment_values: np.ndarray) -> np.ndarray:
    centered = moment_values - moment_values.mean(axis=0, keepdims=True)
    return centered.T @ centered / moment_values.shape[0]


def regularized_inverse(covariance: np.ndarray) -> np.ndarray:
    covariance = np.atleast_2d(np.asarray(covariance, dtype=float))
    covariance = 0.5 * (covariance + covariance.T)
    if not np.all(np.isfinite(covariance)):
        return np.full_like(covariance, math.nan)
    values, vectors = np.linalg.eigh(covariance)
    floor = max(float(np.max(values)), 1.0) * 1e-10
    values = np.maximum(values, floor)
    return (vectors / values) @ vectors.T


def j_statistic(shocks: np.ndarray, powers: tuple[tuple[int, int], ...]) -> float:
    moment_values = moment_observations(shocks, powers)
    sample_mean = moment_values.mean(axis=0)
    inverse = regularized_inverse(sample_moment_covariance(moment_values))
    if not np.all(np.isfinite(inverse)):
        return math.nan
    return float(shocks.shape[0] * sample_mean @ inverse @ sample_mean)


def robust_higher_cumulant_values(shocks: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return mixed higher-cumulant estimates and influence observations."""
    centered = shocks - shocks.mean(axis=0, keepdims=True)
    x = centered[:, 0]
    y = centered[:, 1]

    m11 = float(np.mean(x * y))
    m20 = float(np.mean(x * x))
    m02 = float(np.mean(y * y))
    m31 = float(np.mean((x**3) * y))
    m22 = float(np.mean((x**2) * (y**2)))
    m13 = float(np.mean(x * (y**3)))

    moments = np.array(
        [
            float(np.mean((x**2) * y)),
            float(np.mean(x * (y**2))),
            m31 - 3.0 * m20 * m11,
            m22 - m20 * m02 - 2.0 * m11 * m11,
            m13 - 3.0 * m02 * m11,
        ],
        dtype=float,
    )
    influence = np.column_stack(
        [
            (x**2) * y,
            x * (y**2),
            (x**3) * y - 3.0 * (m11 * x**2 + m20 * x * y),
            (x**2) * (y**2) - m02 * x**2 - m20 * y**2 - 4.0 * m11 * x * y,
            x * (y**3) - 3.0 * (m11 * y**2 + m02 * x * y),
        ]
    )
    return moments, influence


def robust_j_statistic_from_shocks(shocks: np.ndarray) -> float:
    moments, influence = robust_higher_cumulant_values(shocks)
    inverse = regularized_inverse(sample_moment_covariance(influence))
    if not np.all(np.isfinite(inverse)):
        return math.nan
    return float(shocks.shape[0] * moments @ inverse @ moments)


def robust_j_statistic(b12: float, b21: float, residuals: np.ndarray) -> float:
    shocks = candidate_shocks(b12, b21, residuals)
    if shocks is None:
        return math.nan
    return robust_j_statistic_from_shocks(shocks)


def evaluate_standard_grid(
    residuals: np.ndarray,
    nu1: float,
    nu2: float,
    b12_grid: np.ndarray,
    b21_grid: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    b12_mesh, b21_mesh = np.meshgrid(b12_grid, b21_grid)
    correlation = b_plane_correlation_grid(b12_mesh, b21_mesh, b_plane_covariance(nu1, nu2))
    covariance_j = np.full_like(correlation, np.nan, dtype=float)
    dw_j = np.full_like(correlation, np.nan, dtype=float)

    rows, cols = np.where((b21_mesh >= 0.0) & np.isfinite(correlation))
    for row, col in zip(rows, cols):
        shocks = standardized_candidate_shocks(
            float(b12_mesh[row, col]),
            float(b21_mesh[row, col]),
            residuals,
        )
        if shocks is None:
            continue
        covariance_j[row, col] = j_statistic(shocks, MOMENTS_COVARIANCE)
        dw_j[row, col] = j_statistic(shocks, MOMENTS_DW)

    covariance_accepted = np.isfinite(covariance_j) & (covariance_j <= CHI2_90_DF1)
    dw_accepted = np.isfinite(dw_j) & (dw_j <= CHI2_90_DF4)
    return (
        b12_mesh,
        b21_mesh,
        correlation,
        covariance_j,
        covariance_accepted,
        dw_j,
        dw_accepted,
    )


def evaluate_robust_grid(
    residuals: np.ndarray,
    b12_grid: np.ndarray,
    b21_grid: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    b12_mesh, b21_mesh = np.meshgrid(b12_grid, b21_grid)
    robust_j = np.full_like(b12_mesh, np.nan, dtype=float)
    rows, cols = np.where((b21_mesh >= 0.0) & (np.abs(1.0 - b12_mesh * b21_mesh) > 1e-10))
    for row, col in zip(rows, cols):
        robust_j[row, col] = robust_j_statistic(
            float(b12_mesh[row, col]),
            float(b21_mesh[row, col]),
            residuals,
        )
    robust_accepted = np.isfinite(robust_j) & (robust_j <= CHI2_90_DF5)
    return b12_mesh, b21_mesh, robust_j, robust_accepted


def shade(ax, b12_mesh: np.ndarray, b21_mesh: np.ndarray, mask: np.ndarray, color: str, alpha: float) -> None:
    if mask.any():
        ax.contourf(
            b12_mesh,
            b21_mesh,
            mask.astype(float),
            levels=[0.5, 1.5],
            colors=[color],
            alpha=alpha,
            antialiased=False,
        )


def draw_covariance_contour(ax, b12_mesh: np.ndarray, b21_mesh: np.ndarray, correlation: np.ndarray) -> None:
    if not np.isfinite(correlation).any():
        return
    corr_min = float(np.nanmin(correlation))
    corr_max = float(np.nanmax(correlation))
    if corr_min <= 0.0 <= corr_max:
        ax.contour(
            b12_mesh,
            b21_mesh,
            correlation,
            levels=[0.0],
            colors=["#1b1b1b"],
            linewidths=1.35,
        )


def add_common_panel_style(ax, b12_grid: np.ndarray, b21_grid: np.ndarray) -> None:
    ax.axvline(0.0, color="0.25", lw=0.9)
    ax.axhline(0.0, color="0.25", lw=0.9)
    ax.scatter(
        [TRUE_B12],
        [TRUE_B21],
        marker="*",
        color="#b2182b",
        edgecolor="white",
        linewidth=0.7,
        s=125,
        zorder=5,
        label="true B0",
    )
    ax.set_xlim(float(b12_grid.min()), float(b12_grid.max()))
    ax.set_ylim(float(b21_grid.min()), float(b21_grid.max()))
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.18)


def min_label(j_values: np.ndarray, fallback: str = "empty") -> str:
    if not np.isfinite(j_values).any():
        return fallback
    return f"min J {np.nanmin(j_values):.3g}"


def truth_label(j_value: float, cutoff: float) -> str:
    if not math.isfinite(j_value):
        return "B0 n/a"
    status = "in" if j_value <= cutoff else "out"
    return f"B0 {status}; J0 {j_value:.3g}"


def plot() -> Path:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    b12_grid = np.linspace(-1.35, 0.35, GRID_POINTS)
    b21_grid = np.linspace(-0.25, 1.35, GRID_POINTS)
    fig, axes = plt.subplots(
        3,
        3,
        figsize=(15.4, 11.2),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    for col, (nu1, nu2) in enumerate(NOISE_LEVELS):
        residuals = simulate_residuals(nu1, nu2)
        (
            b12_mesh,
            b21_mesh,
            correlation,
            covariance_j,
            covariance_accepted,
            dw_j,
            dw_accepted,
        ) = evaluate_standard_grid(residuals, nu1, nu2, b12_grid, b21_grid)
        _, _, robust_j, robust_accepted = evaluate_robust_grid(residuals, b12_grid, b21_grid)

        true_shocks = standardized_candidate_shocks(TRUE_B12, TRUE_B21, residuals)
        true_covariance_j = math.nan
        true_dw_j = math.nan
        if true_shocks is not None:
            true_covariance_j = j_statistic(true_shocks, MOMENTS_COVARIANCE)
            true_dw_j = j_statistic(true_shocks, MOMENTS_DW)
        true_robust_j = robust_j_statistic(TRUE_B12, TRUE_B21, residuals)

        ax = axes[0, col]
        shade(ax, b12_mesh, b21_mesh, covariance_accepted, "#9bc9a6", 0.9)
        draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title(f"Sign/covariance J-test, V=({nu1:g},{nu2:g})")
        ax.text(
            -1.22,
            1.16,
            f"{min_label(covariance_j)}\n{truth_label(true_covariance_j, CHI2_90_DF1)}",
            color="#11623a",
            fontsize=9,
        )

        ax = axes[1, col]
        shade(ax, b12_mesh, b21_mesh, covariance_accepted, "#d9d9d9", 0.55)
        shade(ax, b12_mesh, b21_mesh, dw_accepted, "#6a51a3", 0.9)
        draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title(f"Standard DW J-test, V=({nu1:g},{nu2:g})")
        ax.text(
            -1.22,
            1.16,
            f"{min_label(dw_j)}\n{truth_label(true_dw_j, CHI2_90_DF4)}",
            color="#542788",
            fontsize=9,
        )

        ax = axes[2, col]
        shade(ax, b12_mesh, b21_mesh, robust_accepted, "#67a9cf", 0.88)
        if np.isfinite(robust_j).any() and robust_accepted.any():
            ax.contour(
                b12_mesh,
                b21_mesh,
                robust_j,
                levels=[CHI2_90_DF5],
                colors=["#2166ac"],
                linewidths=1.2,
            )
        draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title(f"Robust DW J-test, V=({nu1:g},{nu2:g})")
        ax.text(
            -1.22,
            1.16,
            f"{min_label(robust_j)}\n{truth_label(true_robust_j, CHI2_90_DF5)}",
            color="#2166ac",
            fontsize=9,
        )

    for ax in axes.flat:
        add_common_panel_style(ax, b12_grid, b21_grid)

    for ax in axes[2, :]:
        ax.set_xlabel("b12")
    for row_label, ax in zip(["b21", "b21", "b21"], axes[:, 0]):
        ax.set_ylabel(row_label)
    axes[0, 0].legend(loc="lower left", frameon=True, framealpha=0.9, fontsize=8)

    fig.suptitle(
        (
            "Diagonal normalization: B = [[1, b12], [b21, 1]]; sign restriction b21 >= 0\n"
            f"N={SAMPLE_SIZE}; all rows invert pointwise 10% J tests; "
            "robust DW uses mixed higher cumulants only"
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
