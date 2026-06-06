"""Build the sign/DW/robust-DW B-plane noise grid figure.

This figure reproduces the KnowledgeVault B-plane layout with three noise
columns and adds a third robust-DW row.  All rows invert pointwise finite-sample
J statistics at the 10 percent level.  The default historical robust-DW row
profiles out diagonal residual-noise variances using the now-superseded
off-diagonal covariance anchor plus mixed higher cumulants of B^{-1}u.

Pass ``--robust-mode pure`` to plot the pure higher-cumulant robust row without
the diagonal-noise off-diagonal covariance anchor.

Pass ``--robust-mode bounded`` to plot the pure row intersected with the
candidate recovered-covariance values attainable from diagonal residual-noise
variances bounded by 0.5.

Pass ``--robust-mode relative`` to plot the pure row intersected with the
candidate covariance decompositions where each diagonal residual-noise variance
is at most half of the corresponding structural shock variance.
"""

from __future__ import annotations

import math
import argparse
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "manuscript" / "figures"
OUTPUT_PATH = OUTPUT_DIR / "fig_sign_dw_robust_noise_grid.png"
PURE_OUTPUT_PATH = OUTPUT_DIR / "fig_sign_dw_pure_robust_noise_grid.png"
BOUNDED_OUTPUT_PATH = OUTPUT_DIR / "fig_sign_dw_bounded_noise_robust_grid.png"
RELATIVE_OUTPUT_PATH = OUTPUT_DIR / "fig_sign_dw_relative_noise_robust_grid.png"

TRUE_B12 = -0.25
TRUE_B21 = 0.80
TRUE_MATRIX = np.array([[1.0, TRUE_B12], [TRUE_B21, 1.0]], dtype=float)

NOISE_LEVELS = ((0.0, 0.0), (0.2, 0.2), (0.5, 0.5))
SAMPLE_SIZE = 500
GRID_POINTS = 121
RANDOM_SEED = 20260605
NOISE_VARIANCE_UPPER_BOUND = 0.5
RELATIVE_NOISE_RATIO = 0.5

CHI2_90_DF1 = 2.705543454095404
CHI2_90_DF4 = 7.779440339734858
CHI2_90_DF5 = 9.236356899781123
CHI2_90_DF6 = 10.644640675668422
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


def sample_residual_covariance(residuals: np.ndarray) -> np.ndarray:
    centered = residuals - residuals.mean(axis=0, keepdims=True)
    return centered.T @ centered / centered.shape[0]


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


def pure_robust_j_statistic(b12: float, b21: float, residuals: np.ndarray) -> float:
    shocks = candidate_shocks(b12, b21, residuals)
    if shocks is None:
        return math.nan
    return robust_j_statistic_from_shocks(shocks)


def recovered_covariance_value(b12: float, b21: float, residuals: np.ndarray) -> float:
    shocks = candidate_shocks(b12, b21, residuals)
    if shocks is None:
        return math.nan
    return float(np.mean(shocks[:, 0] * shocks[:, 1]))


def bounded_noise_recovered_covariance_interval(
    b12: float,
    b21: float,
    variance_upper_bound: float = NOISE_VARIANCE_UPPER_BOUND,
) -> tuple[float, float] | None:
    determinant = 1.0 - b12 * b21
    if abs(determinant) < 1e-10:
        return None

    scale = determinant * determinant
    coefficient_1 = -b21 / scale
    coefficient_2 = -b12 / scale
    lower = variance_upper_bound * (min(coefficient_1, 0.0) + min(coefficient_2, 0.0))
    upper = variance_upper_bound * (max(coefficient_1, 0.0) + max(coefficient_2, 0.0))
    return lower, upper


def bounded_noise_covariance_feasible(b12: float, b21: float, residuals: np.ndarray) -> bool:
    interval = bounded_noise_recovered_covariance_interval(b12, b21)
    if interval is None:
        return False
    recovered_covariance = recovered_covariance_value(b12, b21, residuals)
    if not math.isfinite(recovered_covariance):
        return False
    lower, upper = interval
    return lower <= recovered_covariance <= upper


def update_interval_from_inequality(
    lower: float,
    upper: float,
    coefficient: float,
    bound: float,
    tolerance: float = 1e-10,
) -> tuple[float, float] | None:
    if abs(coefficient) <= tolerance:
        if bound >= -tolerance:
            return lower, upper
        return None
    threshold = bound / coefficient
    if coefficient > 0.0:
        upper = min(upper, threshold)
    else:
        lower = max(lower, threshold)
    if lower <= upper + tolerance:
        return lower, upper
    return None


def relative_noise_covariance_feasible(
    b12: float,
    b21: float,
    residuals: np.ndarray,
    ratio: float = RELATIVE_NOISE_RATIO,
    tolerance: float = 1e-8,
) -> bool:
    covariance = sample_residual_covariance(residuals)
    s11 = float(covariance[0, 0])
    s12 = float(covariance[0, 1])
    s22 = float(covariance[1, 1])

    equality = np.array([b21, b12], dtype=float)
    norm_squared = float(equality @ equality)
    if norm_squared <= tolerance:
        return abs(s12) <= tolerance and s11 > 0.0 and s22 > 0.0

    point = equality * (s12 / norm_squared)
    direction = np.array([-b12, b21], dtype=float)
    lower = -math.inf
    upper = math.inf
    eps = 1e-10

    inequalities = [
        (np.array([-1.0, 0.0]), -eps),
        (np.array([0.0, -1.0]), -eps),
        (np.array([1.0, b12 * b12]), s11),
        (np.array([-(1.0 + ratio), -(b12 * b12)]), -s11),
        (np.array([b21 * b21, 1.0]), s22),
        (np.array([-(b21 * b21), -(1.0 + ratio)]), -s22),
    ]
    for normal, bound in inequalities:
        interval = update_interval_from_inequality(
            lower,
            upper,
            float(normal @ direction),
            float(bound - normal @ point),
            tolerance=tolerance,
        )
        if interval is None:
            return False
        lower, upper = interval
    return True


def offdiagonal_covariance_values(
    residuals: np.ndarray,
    b12: float,
    b21: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Return the diagonal-noise-robust off-diagonal covariance moment."""
    centered = residuals - residuals.mean(axis=0, keepdims=True)
    observations = centered[:, 0] * centered[:, 1] - (b12 + b21)
    return np.array([float(np.mean(observations))], dtype=float), observations[:, None]


def diagonal_noise_robust_values(
    b12: float,
    b21: float,
    residuals: np.ndarray,
) -> tuple[np.ndarray, np.ndarray] | None:
    shocks = candidate_shocks(b12, b21, residuals)
    if shocks is None:
        return None
    covariance_moment, covariance_influence = offdiagonal_covariance_values(
        residuals,
        b12,
        b21,
    )
    cumulant_moments, cumulant_influence = robust_higher_cumulant_values(shocks)
    return (
        np.concatenate([covariance_moment, cumulant_moments]),
        np.column_stack([covariance_influence[:, 0], cumulant_influence]),
    )


def robust_j_statistic(b12: float, b21: float, residuals: np.ndarray) -> float:
    values = diagonal_noise_robust_values(b12, b21, residuals)
    if values is None:
        return math.nan
    moments, influence = values
    inverse = regularized_inverse(sample_moment_covariance(influence))
    if not np.all(np.isfinite(inverse)):
        return math.nan
    return float(residuals.shape[0] * moments @ inverse @ moments)


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


def robust_mode_cutoff(robust_mode: str) -> float:
    if robust_mode == "diagonal":
        return CHI2_90_DF6
    if robust_mode in {"pure", "bounded", "relative"}:
        return CHI2_90_DF5
    raise ValueError(f"unknown robust mode: {robust_mode}")


def robust_mode_title(robust_mode: str) -> str:
    if robust_mode == "diagonal":
        return "Robust DW J-test"
    if robust_mode == "pure":
        return "Pure robust DW J-test"
    if robust_mode == "bounded":
        return "Bounded-noise robust DW"
    if robust_mode == "relative":
        return "Relative-noise robust DW"
    raise ValueError(f"unknown robust mode: {robust_mode}")


def robust_mode_summary(robust_mode: str) -> str:
    if robust_mode == "diagonal":
        return "robust DW profiles diagonal noise and adds mixed higher cumulants"
    if robust_mode == "pure":
        return "pure robust DW uses only mixed higher cumulants"
    if robust_mode == "bounded":
        return "bounded robust DW uses pure cumulants plus 0 <= noise variances <= 0.5"
    if robust_mode == "relative":
        return "relative robust DW uses pure cumulants plus noise variances <= 0.5 shock variances"
    raise ValueError(f"unknown robust mode: {robust_mode}")


def robust_mode_statistic(b12: float, b21: float, residuals: np.ndarray, robust_mode: str) -> float:
    if robust_mode == "diagonal":
        return robust_j_statistic(b12, b21, residuals)
    if robust_mode in {"pure", "bounded", "relative"}:
        return pure_robust_j_statistic(b12, b21, residuals)
    raise ValueError(f"unknown robust mode: {robust_mode}")


def robust_mode_accepts(
    b12: float,
    b21: float,
    residuals: np.ndarray,
    robust_mode: str,
    j_value: float | None = None,
) -> bool:
    if j_value is None:
        j_value = robust_mode_statistic(b12, b21, residuals, robust_mode)
    if not math.isfinite(j_value) or j_value > robust_mode_cutoff(robust_mode):
        return False
    if robust_mode == "bounded":
        return bounded_noise_covariance_feasible(b12, b21, residuals)
    if robust_mode == "relative":
        return relative_noise_covariance_feasible(b12, b21, residuals)
    return True


def evaluate_robust_grid(
    residuals: np.ndarray,
    b12_grid: np.ndarray,
    b21_grid: np.ndarray,
    robust_mode: str,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    b12_mesh, b21_mesh = np.meshgrid(b12_grid, b21_grid)
    robust_j = np.full_like(b12_mesh, np.nan, dtype=float)
    rows, cols = np.where((b21_mesh >= 0.0) & (np.abs(1.0 - b12_mesh * b21_mesh) > 1e-10))
    for row, col in zip(rows, cols):
        robust_j[row, col] = robust_mode_statistic(
            float(b12_mesh[row, col]),
            float(b21_mesh[row, col]),
            residuals,
            robust_mode,
        )
    robust_accepted = np.zeros_like(robust_j, dtype=bool)
    for row, col in zip(rows, cols):
        robust_accepted[row, col] = robust_mode_accepts(
            float(b12_mesh[row, col]),
            float(b21_mesh[row, col]),
            residuals,
            robust_mode,
            float(robust_j[row, col]),
        )
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


def truth_label_with_status(j_value: float, accepted: bool) -> str:
    if not math.isfinite(j_value):
        return "B0 n/a"
    status = "in" if accepted else "out"
    return f"B0 {status}; J0 {j_value:.3g}"


def plot(robust_mode: str = "diagonal", output_path: Path | None = None) -> Path:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    robust_cutoff = robust_mode_cutoff(robust_mode)
    if output_path is None:
        if robust_mode == "pure":
            output_path = PURE_OUTPUT_PATH
        elif robust_mode == "bounded":
            output_path = BOUNDED_OUTPUT_PATH
        elif robust_mode == "relative":
            output_path = RELATIVE_OUTPUT_PATH
        else:
            output_path = OUTPUT_PATH

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
        _, _, robust_j, robust_accepted = evaluate_robust_grid(
            residuals,
            b12_grid,
            b21_grid,
            robust_mode,
        )

        true_shocks = standardized_candidate_shocks(TRUE_B12, TRUE_B21, residuals)
        true_covariance_j = math.nan
        true_dw_j = math.nan
        if true_shocks is not None:
            true_covariance_j = j_statistic(true_shocks, MOMENTS_COVARIANCE)
            true_dw_j = j_statistic(true_shocks, MOMENTS_DW)
        true_robust_j = robust_mode_statistic(TRUE_B12, TRUE_B21, residuals, robust_mode)
        true_robust_accepted = robust_mode_accepts(
            TRUE_B12,
            TRUE_B21,
            residuals,
            robust_mode,
            true_robust_j,
        )

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
                levels=[robust_cutoff],
                colors=["#2166ac"],
                linewidths=1.2,
            )
        draw_covariance_contour(ax, b12_mesh, b21_mesh, correlation)
        ax.set_title(f"{robust_mode_title(robust_mode)}, V=({nu1:g},{nu2:g})")
        ax.text(
            -1.22,
            1.16,
            f"{min_label(robust_j)}\n{truth_label_with_status(true_robust_j, true_robust_accepted)}",
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
            f"N={SAMPLE_SIZE}; all rows invert pointwise 10% J tests; " +
            robust_mode_summary(robust_mode)
        ),
        fontsize=13,
    )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--robust-mode",
        choices=["diagonal", "pure", "bounded", "relative"],
        default="diagonal",
        help="Bottom-row robust statistic to plot.",
    )
    parser.add_argument("--output", default="", help="Optional output path.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    path = plot(
        robust_mode=args.robust_mode,
        output_path=Path(args.output) if args.output else None,
    )
    print(f"Wrote {path.relative_to(ROOT)}")
