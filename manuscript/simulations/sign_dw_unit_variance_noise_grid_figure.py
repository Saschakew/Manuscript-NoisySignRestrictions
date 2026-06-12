"""Build the M67 unit-variance residual-noise Figure 1.

The figure replaces the historical diagonal-normalized B-plane Figure 1.  It
uses the M64/M66 route: structural shocks have unit variance, residual-noise
variances are nuisance parameters, and the robust row projects accepted
``(B, lambda)`` pairs onto the displayed ``(B12, B21)`` coordinates.

The displayed chart is a projection, not a normalization.  For each plotted
``(B12, B21)`` point, the script searches over positive diagonal entries
``B11`` and ``B22``.  The robust row then searches over
``lambda in [0, rho]^2`` and evaluates the Section 4 moment vector at
``nu_i(B, lambda) = lambda_i (B B')_ii``.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
FIGURE_DIR = ROOT / "manuscript" / "figures"
SIM_DIR = ROOT / "manuscript" / "simulations"
OUTPUT_DIR = SIM_DIR / "output"

OUTPUT_PATH = FIGURE_DIR / "fig_sign_dw_unit_variance_noise_grid.png"
NOTE_PATH = SIM_DIR / "sign_dw_unit_variance_noise_grid_figure.md"
JSON_PATH = OUTPUT_DIR / "sign_dw_unit_variance_noise_grid_figure.json"

TRUE_MATRIX = np.array([[1.0, -0.25], [0.80, 1.0]], dtype=float)
TRUE_B11 = float(TRUE_MATRIX[0, 0])
TRUE_B12 = float(TRUE_MATRIX[0, 1])
TRUE_B21 = float(TRUE_MATRIX[1, 0])
TRUE_B22 = float(TRUE_MATRIX[1, 1])

NOISE_LEVELS = ((0.0, 0.0), (0.2, 0.2), (0.5, 0.5))
SAMPLE_SIZE = 500
RANDOM_SEED = 20260605
RELATIVE_NOISE_RATIO = 0.5
STRUCTURAL_CHI2_DF = 5.0

CHI2_90_DF3 = 6.251388631170325
CHI2_90_DF5 = 9.236356899781123
CHI2_90_DF8 = 13.36156613651173

B12_MIN = -1.10
B12_MAX = 0.45
B21_MIN = -0.10
B21_MAX = 1.45
B11_MIN = 0.55
B11_MAX = 1.45
B22_MIN = 0.55
B22_MAX = 1.45


@dataclass(frozen=True)
class GridSpec:
    projection_points: int = 47
    diagonal_points: int = 11
    lambda_points: int = 7
    robust_batch_size: int = 36
    standard_batch_size: int = 240


@dataclass(frozen=True)
class CandidateGrid:
    b11: np.ndarray
    b12: np.ndarray
    b21: np.ndarray
    b22: np.ndarray
    b12_index: np.ndarray
    b21_index: np.ndarray
    b12_values: np.ndarray
    b21_values: np.ndarray


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def standardize_columns(values: np.ndarray) -> np.ndarray:
    values = values - values.mean(axis=0, keepdims=True)
    scale = values.std(axis=0, keepdims=True)
    if np.any(scale <= 1e-12):
        raise ValueError("cannot standardize a degenerate column")
    return values / scale


def primitive_draws(sample_size: int = SAMPLE_SIZE, seed: int = RANDOM_SEED) -> tuple[np.ndarray, np.ndarray]:
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


def sample_covariance(values: np.ndarray) -> np.ndarray:
    centered = values - values.mean(axis=0, keepdims=True)
    return centered.T @ centered / centered.shape[0]


def unique_grid(start: float, stop: float, points: int, include: float) -> np.ndarray:
    values = np.linspace(start, stop, points)
    values = np.unique(np.append(values, include))
    values.sort()
    return values


def make_candidate_grid(spec: GridSpec) -> CandidateGrid:
    b12_values = unique_grid(B12_MIN, B12_MAX, spec.projection_points, TRUE_B12)
    b21_values = unique_grid(B21_MIN, B21_MAX, spec.projection_points, TRUE_B21)
    b11_values = unique_grid(B11_MIN, B11_MAX, spec.diagonal_points, TRUE_B11)
    b22_values = unique_grid(B22_MIN, B22_MAX, spec.diagonal_points, TRUE_B22)

    b12_index, b21_index, b11_index, b22_index = np.meshgrid(
        np.arange(b12_values.size),
        np.arange(b21_values.size),
        np.arange(b11_values.size),
        np.arange(b22_values.size),
        indexing="ij",
    )
    b12 = b12_values[b12_index].ravel()
    b21 = b21_values[b21_index].ravel()
    b11 = b11_values[b11_index].ravel()
    b22 = b22_values[b22_index].ravel()

    sign_and_orientation = (b11 > 0.0) & (b22 > 0.0) & (b21 >= 0.0)
    determinant = b11 * b22 - b12 * b21
    nonsingular = np.abs(determinant) > 1e-8
    keep = sign_and_orientation & nonsingular
    return CandidateGrid(
        b11=b11[keep],
        b12=b12[keep],
        b21=b21[keep],
        b22=b22[keep],
        b12_index=b12_index.ravel()[keep],
        b21_index=b21_index.ravel()[keep],
        b12_values=b12_values,
        b21_values=b21_values,
    )


def lambda_grid_for_noise(noise: tuple[float, float], spec: GridSpec) -> tuple[np.ndarray, np.ndarray]:
    base = np.linspace(0.0, RELATIVE_NOISE_RATIO, spec.lambda_points)
    signal = TRUE_MATRIX @ TRUE_MATRIX.T
    true_lambda_1 = 0.0 if signal[0, 0] <= 0.0 else noise[0] / signal[0, 0]
    true_lambda_2 = 0.0 if signal[1, 1] <= 0.0 else noise[1] / signal[1, 1]
    lambda_1 = np.unique(np.append(base, np.clip(true_lambda_1, 0.0, RELATIVE_NOISE_RATIO)))
    lambda_2 = np.unique(np.append(base, np.clip(true_lambda_2, 0.0, RELATIVE_NOISE_RATIO)))
    lambda_1.sort()
    lambda_2.sort()
    return lambda_1, lambda_2


def inverse_elements(
    b11: np.ndarray,
    b12: np.ndarray,
    b21: np.ndarray,
    b22: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    determinant = b11 * b22 - b12 * b21
    inv11 = b22 / determinant
    inv12 = -b12 / determinant
    inv21 = -b21 / determinant
    inv22 = b11 / determinant
    return determinant, inv11, inv12, inv21, inv22


def recovered_shocks(
    residuals: np.ndarray,
    b11: np.ndarray,
    b12: np.ndarray,
    b21: np.ndarray,
    b22: np.ndarray,
) -> np.ndarray:
    _det, inv11, inv12, inv21, inv22 = inverse_elements(b11, b12, b21, b22)
    u1 = residuals[:, 0:1]
    u2 = residuals[:, 1:2]
    e1 = u1 * inv11[None, :] + u2 * inv12[None, :]
    e2 = u1 * inv21[None, :] + u2 * inv22[None, :]
    shocks = np.stack([e1, e2], axis=2)
    return shocks - shocks.mean(axis=0, keepdims=True)


def regularized_inverse_stack(covariance: np.ndarray) -> np.ndarray:
    covariance = 0.5 * (covariance + np.swapaxes(covariance, -1, -2))
    values, vectors = np.linalg.eigh(covariance)
    max_values = np.maximum(np.max(values, axis=1), 1.0)
    floors = max_values[:, None] * 1e-10
    values = np.maximum(values, floors)
    return np.einsum("bij,bj,bkj->bik", vectors, 1.0 / values, vectors)


def j_from_observations(observations: np.ndarray) -> np.ndarray:
    mean = observations.mean(axis=0)
    centered = observations - mean[None, :, :]
    covariance = np.einsum("tbi,tbj->bij", centered, centered) / observations.shape[0]
    inverse = regularized_inverse_stack(covariance)
    return observations.shape[0] * np.einsum("bi,bij,bj->b", mean, inverse, mean)


def weight_from_observations(observations: np.ndarray) -> np.ndarray:
    if observations.ndim != 3 or observations.shape[1] != 1:
        raise ValueError("weight observations must have shape (T, 1, k)")
    single = observations[:, 0, :]
    centered = single - single.mean(axis=0, keepdims=True)
    covariance = centered.T @ centered / single.shape[0]
    covariance = 0.5 * (covariance + covariance.T)
    values, vectors = np.linalg.eigh(covariance)
    floor = max(float(np.max(values)), 1.0) * 1e-10
    values = np.maximum(values, floor)
    return (vectors / values) @ vectors.T


def j_with_weight(mean: np.ndarray, weight: np.ndarray, sample_size: int) -> np.ndarray:
    return sample_size * np.einsum("bi,ij,bj->b", mean, weight, mean)


def second_moment_observations(shocks: np.ndarray) -> np.ndarray:
    e1 = shocks[:, :, 0]
    e2 = shocks[:, :, 1]
    return np.stack([e1 * e1 - 1.0, e1 * e2, e2 * e2 - 1.0], axis=2)


def second_moment_means(shocks: np.ndarray) -> np.ndarray:
    return second_moment_observations(shocks).mean(axis=0)


def standard_dw_observations(shocks: np.ndarray) -> np.ndarray:
    e1 = shocks[:, :, 0]
    e2 = shocks[:, :, 1]
    return np.stack(
        [
            e1 * e1 * e2,
            e1 * e2 * e2,
            e1 * e1 * e1 * e2,
            e1 * e1 * e2 * e2 - 1.0,
            e1 * e2 * e2 * e2,
        ],
        axis=2,
    )


def standard_dw_means(shocks: np.ndarray) -> np.ndarray:
    return standard_dw_observations(shocks).mean(axis=0)


def robust_observations(
    residuals: np.ndarray,
    shocks: np.ndarray,
    b11: np.ndarray,
    b12: np.ndarray,
    b21: np.ndarray,
    b22: np.ndarray,
    lambda_pairs: np.ndarray,
) -> np.ndarray:
    batch = b11.size
    pair_count = lambda_pairs.shape[0]
    repeated = batch * pair_count
    e1 = shocks[:, :, 0]
    e2 = shocks[:, :, 1]

    signal_11 = b11 * b11 + b12 * b12
    signal_12 = b11 * b21 + b12 * b22
    signal_22 = b21 * b21 + b22 * b22

    lambda_1 = lambda_pairs[:, 0]
    lambda_2 = lambda_pairs[:, 1]
    nu1 = signal_11[:, None] * lambda_1[None, :]
    nu2 = signal_22[:, None] * lambda_2[None, :]

    model_11 = signal_11[:, None] + nu1
    model_12 = signal_12[:, None] + np.zeros_like(nu1)
    model_22 = signal_22[:, None] + nu2

    u1 = residuals[:, 0:1]
    u2 = residuals[:, 1:2]
    second = np.stack(
        [
            u1 * u1 - model_11.reshape(1, repeated),
            u1 * u2 - model_12.reshape(1, repeated),
            u2 * u2 - model_22.reshape(1, repeated),
        ],
        axis=2,
    )

    _det, inv11, inv12, inv21, inv22 = inverse_elements(b11, b12, b21, b22)
    omega11 = 1.0 + (inv11[:, None] ** 2) * nu1 + (inv12[:, None] ** 2) * nu2
    omega12 = (inv11[:, None] * inv21[:, None]) * nu1 + (inv12[:, None] * inv22[:, None]) * nu2
    omega22 = 1.0 + (inv21[:, None] ** 2) * nu1 + (inv22[:, None] ** 2) * nu2

    e1_repeated = np.repeat(e1, pair_count, axis=1)
    e2_repeated = np.repeat(e2, pair_count, axis=1)
    omega11 = omega11.reshape(1, repeated)
    omega12 = omega12.reshape(1, repeated)
    omega22 = omega22.reshape(1, repeated)
    higher = np.stack(
        [
            e1_repeated * e1_repeated * e2_repeated,
            e1_repeated * e2_repeated * e2_repeated,
            e1_repeated * e1_repeated * e1_repeated * e2_repeated - 3.0 * omega11 * omega12,
            e1_repeated * e1_repeated * e2_repeated * e2_repeated
            - omega11 * omega22
            - 2.0 * omega12 * omega12,
            e1_repeated * e2_repeated * e2_repeated * e2_repeated - 3.0 * omega22 * omega12,
        ],
        axis=2,
    )
    return np.concatenate([second, higher], axis=2)


def robust_means(
    residuals: np.ndarray,
    shocks: np.ndarray,
    b11: np.ndarray,
    b12: np.ndarray,
    b21: np.ndarray,
    b22: np.ndarray,
    lambda_pairs: np.ndarray,
) -> np.ndarray:
    batch = b11.size
    pair_count = lambda_pairs.shape[0]
    repeated = batch * pair_count
    e1 = shocks[:, :, 0]
    e2 = shocks[:, :, 1]
    covariance = sample_covariance(residuals)

    signal_11 = b11 * b11 + b12 * b12
    signal_12 = b11 * b21 + b12 * b22
    signal_22 = b21 * b21 + b22 * b22

    lambda_1 = lambda_pairs[:, 0]
    lambda_2 = lambda_pairs[:, 1]
    nu1 = signal_11[:, None] * lambda_1[None, :]
    nu2 = signal_22[:, None] * lambda_2[None, :]
    model_11 = signal_11[:, None] + nu1
    model_12 = signal_12[:, None] + np.zeros_like(nu1)
    model_22 = signal_22[:, None] + nu2

    second = np.stack(
        [
            covariance[0, 0] - model_11.reshape(repeated),
            covariance[0, 1] - model_12.reshape(repeated),
            covariance[1, 1] - model_22.reshape(repeated),
        ],
        axis=1,
    )

    _det, inv11, inv12, inv21, inv22 = inverse_elements(b11, b12, b21, b22)
    omega11 = 1.0 + (inv11[:, None] ** 2) * nu1 + (inv12[:, None] ** 2) * nu2
    omega12 = (inv11[:, None] * inv21[:, None]) * nu1 + (inv12[:, None] * inv22[:, None]) * nu2
    omega22 = 1.0 + (inv21[:, None] ** 2) * nu1 + (inv22[:, None] ** 2) * nu2

    e21 = np.mean(e1 * e1 * e2, axis=0)[:, None]
    e12 = np.mean(e1 * e2 * e2, axis=0)[:, None]
    e31 = np.mean(e1 * e1 * e1 * e2, axis=0)[:, None]
    e22 = np.mean(e1 * e1 * e2 * e2, axis=0)[:, None]
    e13 = np.mean(e1 * e2 * e2 * e2, axis=0)[:, None]

    higher = np.stack(
        [
            np.broadcast_to(e21, omega11.shape).reshape(repeated),
            np.broadcast_to(e12, omega11.shape).reshape(repeated),
            (e31 - 3.0 * omega11 * omega12).reshape(repeated),
            (e22 - omega11 * omega22 - 2.0 * omega12 * omega12).reshape(repeated),
            (e13 - 3.0 * omega22 * omega12).reshape(repeated),
        ],
        axis=1,
    )
    return np.concatenate([second, higher], axis=1)


def scenario_weights(residuals: np.ndarray, noise: tuple[float, float]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    true_shocks = recovered_shocks(
        residuals,
        np.array([TRUE_B11]),
        np.array([TRUE_B12]),
        np.array([TRUE_B21]),
        np.array([TRUE_B22]),
    )
    signal = TRUE_MATRIX @ TRUE_MATRIX.T
    lambda_pair = np.array(
        [
            0.0 if signal[0, 0] <= 0.0 else noise[0] / signal[0, 0],
            0.0 if signal[1, 1] <= 0.0 else noise[1] / signal[1, 1],
        ],
        dtype=float,
    )[None, :]
    second_weight = weight_from_observations(second_moment_observations(true_shocks))
    standard_weight = weight_from_observations(standard_dw_observations(true_shocks))
    robust_weight = weight_from_observations(
        robust_observations(
            residuals,
            true_shocks,
            np.array([TRUE_B11]),
            np.array([TRUE_B12]),
            np.array([TRUE_B21]),
            np.array([TRUE_B22]),
            lambda_pair,
        )
    )
    return second_weight, standard_weight, robust_weight


def evaluate_standard_projection(
    residuals: np.ndarray,
    grid: CandidateGrid,
    spec: GridSpec,
    second_weight: np.ndarray,
    standard_weight: np.ndarray,
) -> dict[str, Any]:
    shape = (grid.b21_values.size, grid.b12_values.size)
    sign_mask = np.zeros(shape, dtype=bool)
    standard_mask = np.zeros(shape, dtype=bool)
    best_second = np.full(shape, np.nan)
    best_standard = np.full(shape, np.nan)

    for start in range(0, grid.b11.size, spec.standard_batch_size):
        end = min(start + spec.standard_batch_size, grid.b11.size)
        shocks = recovered_shocks(
            residuals,
            grid.b11[start:end],
            grid.b12[start:end],
            grid.b21[start:end],
            grid.b22[start:end],
        )
        second_j = j_with_weight(second_moment_means(shocks), second_weight, residuals.shape[0])
        standard_j = j_with_weight(standard_dw_means(shocks), standard_weight, residuals.shape[0])
        sign_accept = second_j <= CHI2_90_DF3
        standard_accept = sign_accept & (standard_j <= CHI2_90_DF5)
        rows = grid.b21_index[start:end]
        cols = grid.b12_index[start:end]
        for local, (row, col) in enumerate(zip(rows, cols)):
            value_2 = float(second_j[local])
            value_s = float(standard_j[local])
            if not np.isfinite(best_second[row, col]) or value_2 < best_second[row, col]:
                best_second[row, col] = value_2
            if sign_accept[local]:
                sign_mask[row, col] = True
                if not np.isfinite(best_standard[row, col]) or value_s < best_standard[row, col]:
                    best_standard[row, col] = value_s
            if standard_accept[local]:
                standard_mask[row, col] = True

    return {
        "sign_mask": sign_mask,
        "standard_mask": standard_mask,
        "best_second": best_second,
        "best_standard": best_standard,
    }


def rough_covariance_prefilter(
    residuals: np.ndarray,
    b11: np.ndarray,
    b12: np.ndarray,
    b21: np.ndarray,
    b22: np.ndarray,
    tolerance: float = 0.65,
) -> np.ndarray:
    covariance = sample_covariance(residuals)
    signal_11 = b11 * b11 + b12 * b12
    signal_12 = b11 * b21 + b12 * b22
    signal_22 = b21 * b21 + b22 * b22
    lower_11 = signal_11
    upper_11 = (1.0 + RELATIVE_NOISE_RATIO) * signal_11
    lower_22 = signal_22
    upper_22 = (1.0 + RELATIVE_NOISE_RATIO) * signal_22
    feasible_11 = (covariance[0, 0] >= lower_11 - tolerance) & (covariance[0, 0] <= upper_11 + tolerance)
    feasible_22 = (covariance[1, 1] >= lower_22 - tolerance) & (covariance[1, 1] <= upper_22 + tolerance)
    feasible_12 = np.abs(covariance[0, 1] - signal_12) <= tolerance
    return feasible_11 & feasible_22 & feasible_12


def evaluate_robust_projection(
    residuals: np.ndarray,
    noise: tuple[float, float],
    grid: CandidateGrid,
    spec: GridSpec,
    robust_weight: np.ndarray,
) -> dict[str, Any]:
    shape = (grid.b21_values.size, grid.b12_values.size)
    robust_mask = np.zeros(shape, dtype=bool)
    best_robust = np.full(shape, np.nan)
    best_lambda_1 = np.full(shape, np.nan)
    best_lambda_2 = np.full(shape, np.nan)

    lambda_1, lambda_2 = lambda_grid_for_noise(noise, spec)
    lambda_pairs = np.array(np.meshgrid(lambda_1, lambda_2, indexing="ij")).reshape(2, -1).T

    prefilter = rough_covariance_prefilter(residuals, grid.b11, grid.b12, grid.b21, grid.b22)
    candidate_indices = np.flatnonzero(prefilter)
    for start in range(0, candidate_indices.size, spec.robust_batch_size):
        selected = candidate_indices[start : start + spec.robust_batch_size]
        b11 = grid.b11[selected]
        b12 = grid.b12[selected]
        b21 = grid.b21[selected]
        b22 = grid.b22[selected]
        shocks = recovered_shocks(residuals, b11, b12, b21, b22)
        means = robust_means(residuals, shocks, b11, b12, b21, b22, lambda_pairs)
        robust_j = j_with_weight(means, robust_weight, residuals.shape[0]).reshape(
            selected.size,
            lambda_pairs.shape[0],
        )
        lambda_min_index = np.nanargmin(robust_j, axis=1)
        min_j = robust_j[np.arange(selected.size), lambda_min_index]
        rows = grid.b21_index[selected]
        cols = grid.b12_index[selected]
        for local, (row, col) in enumerate(zip(rows, cols)):
            value = float(min_j[local])
            if not np.isfinite(best_robust[row, col]) or value < best_robust[row, col]:
                best_robust[row, col] = value
                pair = lambda_pairs[int(lambda_min_index[local])]
                best_lambda_1[row, col] = float(pair[0])
                best_lambda_2[row, col] = float(pair[1])
            if value <= CHI2_90_DF8:
                robust_mask[row, col] = True

    return {
        "robust_mask": robust_mask,
        "best_robust": best_robust,
        "best_lambda_1": best_lambda_1,
        "best_lambda_2": best_lambda_2,
        "lambda_1_grid": lambda_1,
        "lambda_2_grid": lambda_2,
        "prefilter_count": int(candidate_indices.size),
    }


def robust_truth_j(
    residuals: np.ndarray,
    noise: tuple[float, float],
    robust_weight: np.ndarray,
) -> tuple[float, tuple[float, float]]:
    signal = TRUE_MATRIX @ TRUE_MATRIX.T
    lambda_pair = (
        0.0 if signal[0, 0] <= 0.0 else noise[0] / signal[0, 0],
        0.0 if signal[1, 1] <= 0.0 else noise[1] / signal[1, 1],
    )
    shocks = recovered_shocks(
        residuals,
        np.array([TRUE_B11]),
        np.array([TRUE_B12]),
        np.array([TRUE_B21]),
        np.array([TRUE_B22]),
    )
    means = robust_means(
        residuals,
        shocks,
        np.array([TRUE_B11]),
        np.array([TRUE_B12]),
        np.array([TRUE_B21]),
        np.array([TRUE_B22]),
        np.array(lambda_pair, dtype=float)[None, :],
    )
    return float(j_with_weight(means, robust_weight, residuals.shape[0])[0]), lambda_pair


def standard_truth_j(
    residuals: np.ndarray,
    second_weight: np.ndarray,
    standard_weight: np.ndarray,
) -> tuple[float, float]:
    shocks = recovered_shocks(
        residuals,
        np.array([TRUE_B11]),
        np.array([TRUE_B12]),
        np.array([TRUE_B21]),
        np.array([TRUE_B22]),
    )
    second_j = float(j_with_weight(second_moment_means(shocks), second_weight, residuals.shape[0])[0])
    standard_j = float(j_with_weight(standard_dw_means(shocks), standard_weight, residuals.shape[0])[0])
    return second_j, standard_j


def mask_share(mask: np.ndarray) -> float:
    return float(np.count_nonzero(mask) / mask.size)


def truth_distance(mask: np.ndarray, grid: CandidateGrid) -> float | None:
    if not mask.any():
        return None
    b12_mesh, b21_mesh = np.meshgrid(grid.b12_values, grid.b21_values)
    distances = np.hypot(b12_mesh[mask] - TRUE_B12, b21_mesh[mask] - TRUE_B21)
    return float(np.min(distances))


def fmt(value: Any, digits: int = 3) -> str:
    if value is None:
        return "n/a"
    numeric = float(value)
    if not math.isfinite(numeric):
        return "n/a"
    return f"{numeric:.{digits}f}"


def write_outputs(
    diagnostics: list[dict[str, Any]],
    spec: GridSpec,
    output_path: Path,
    note_path: Path,
    json_path: Path,
) -> None:
    payload = {
        "schema_version": 1,
        "task": "M67 unit-variance Figure 1 rebuild",
        "figure": display_path(output_path),
        "description": "Projected unit-variance residual-noise grid over (B12,B21), with B11/B22 and lambda profiled.",
        "configuration": {
            "sample_size": SAMPLE_SIZE,
            "seed": RANDOM_SEED,
            "rho": RELATIVE_NOISE_RATIO,
            "projection_points": spec.projection_points,
            "diagonal_points": spec.diagonal_points,
            "lambda_points": spec.lambda_points,
            "true_B0": TRUE_MATRIX.tolist(),
            "critical_values": {
                "second_moment_chi2_90_df3": CHI2_90_DF3,
                "standard_dw_chi2_90_df5": CHI2_90_DF5,
                "robust_full_moment_chi2_90_df8": CHI2_90_DF8,
            },
            "displayed_projection": ["B12", "B21"],
            "profiled_coordinates": ["B11", "B22", "lambda1", "lambda2"],
            "orientation": "B11 > 0 and B22 > 0",
            "sign_restriction": "B21 >= 0",
            "weighting": "fixed one-step GMM weights by scenario, evaluated at the fixed-draw true parameter",
        },
        "diagnostics": diagnostics,
    }
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# M67 Unit-Variance Figure 1 Diagnostics",
        "",
        "Status: generated corrected Figure 1 for the M64/M66 unit-variance route.",
        "",
        "The chart displays the projection of accepted matrices onto `(B12, B21)`. It does not impose `diag(B)=1`: for every displayed projection point the script searches over positive `B11` and `B22`. The robust row also searches over `lambda in [0,rho]^2` and sets `nu_i=lambda_i (B B')_ii` before evaluating the Section 4 moment vector.",
        "",
        "Truth markers refer to the full true matrix, not merely to whether the true `(B12,B21)` projection cell contains some other accepted diagonal pair: a star means the full true `B0` passes that row's test, and an x means it does not.",
        "",
        "The plotted J statistics use a fixed one-step GMM weight for each scenario, estimated from the fixed draw at the true parameter. The robust cutoff is a pointwise diagnostic chi-square cutoff for the eight displayed moment rows. The final projection-critical-value choice remains part of the broader M65 evidence task.",
        "",
        "## Configuration",
        "",
        f"- Output figure: `{display_path(output_path)}`.",
        f"- Machine-readable diagnostics: `{display_path(json_path)}`.",
        f"- Sample size: `{SAMPLE_SIZE}`.",
        f"- Seed: `{RANDOM_SEED}`.",
        f"- Noise ratio bound: `rho={RELATIVE_NOISE_RATIO}`.",
        f"- Projection grid: `{spec.projection_points} x {spec.projection_points}` plus true coordinates.",
        f"- Diagonal grid: `{spec.diagonal_points} x {spec.diagonal_points}` plus true diagonal entries.",
        f"- Lambda grid: `{spec.lambda_points} x {spec.lambda_points}` plus the true lambda values for each scenario.",
        "- Weighting: fixed one-step GMM weights by scenario, evaluated at the fixed-draw true parameter for this diagnostic figure.",
        "",
        "## Fixed-Draw Diagnostics",
        "",
        "| Noise | Sign share | Standard DW share | Robust share | B0 standard | B0 robust | Robust distance | Best lambda at nearest accepted cell |",
        "|---|---:|---:|---:|---|---|---:|---|",
    ]
    for record in diagnostics:
        standard_truth = "in" if record["truth"]["standard_in"] else "out"
        robust_truth = "in" if record["truth"]["robust_in"] else "out"
        lines.append(
            "| {noise} | {sign} | {standard} | {robust} | {standard_truth} | {robust_truth} | {distance} | ({lambda1}, {lambda2}) |".format(
                noise=record["label"],
                sign=fmt(record["shares"]["sign"]),
                standard=fmt(record["shares"]["standard_dw"]),
                robust=fmt(record["shares"]["robust_dw"]),
                standard_truth=standard_truth,
                robust_truth=robust_truth,
                distance=fmt(record["distances"]["robust_to_truth"]),
                lambda1=fmt(record["best_truth_cell_lambda"][0]),
                lambda2=fmt(record["best_truth_cell_lambda"][1]),
            )
        )
    lines.extend(
        [
            "",
            "## Claim Audit",
            "",
            "| Claim | Status | Evidence | Confidence | Action |",
            "|---|---|---|---|---|",
            "| The robust row uses `nu_i=lambda_i (B B')_ii` with `lambda in [0,rho]^2`. | `code-implemented`, `derived` | `sign_dw_unit_variance_noise_grid_figure.py`; M66 derivation note. | high | promote for Figure 1 |",
            "| The displayed chart is a projection to `(B12,B21)`, with diagonal entries profiled. | `code-implemented` | Candidate grid construction and diagnostics JSON. | high | promote |",
            "| The plotted J statistics use fixed one-step GMM weights for tractability and visual stability. | `code-implemented` | Scenario weight construction in the script. | high | promote as diagnostic implementation detail |",
            "| The robust cutoff is final for projected inference. | `conjectural` | M65 still lists projection critical values as unresolved. | medium | quarantine as diagnostic |",
            "",
        ]
    )
    note_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def draw_mask(ax: Any, grid: CandidateGrid, mask: np.ndarray, color: str, alpha: float) -> None:
    b12_mesh, b21_mesh = np.meshgrid(grid.b12_values, grid.b21_values)
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


def draw_panel_style(ax: Any, grid: CandidateGrid) -> None:
    ax.axvline(0.0, color="0.35", lw=0.8)
    ax.axhline(0.0, color="0.35", lw=0.8)
    ax.set_xlim(float(grid.b12_values.min()), float(grid.b12_values.max()))
    ax.set_ylim(float(grid.b21_values.min()), float(grid.b21_values.max()))
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.18)


def draw_truth_marker(ax: Any, accepted: bool) -> None:
    if accepted:
        ax.scatter(
            [TRUE_B12],
            [TRUE_B21],
            marker="*",
            color="#b2182b",
            edgecolor="white",
            linewidth=0.7,
            s=125,
            zorder=6,
        )
    else:
        ax.scatter(
            [TRUE_B12],
            [TRUE_B21],
            marker="x",
            color="#b2182b",
            linewidth=2.0,
            s=90,
            zorder=6,
        )


def nearest_truth_cell(grid: CandidateGrid) -> tuple[int, int]:
    col = int(np.argmin(np.abs(grid.b12_values - TRUE_B12)))
    row = int(np.argmin(np.abs(grid.b21_values - TRUE_B21)))
    return row, col


def plot(
    output_path: Path = OUTPUT_PATH,
    note_path: Path = NOTE_PATH,
    json_path: Path = JSON_PATH,
    spec: GridSpec = GridSpec(),
) -> Path:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    grid = make_candidate_grid(spec)
    fig, axes = plt.subplots(
        3,
        3,
        figsize=(15.6, 11.4),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )
    diagnostics: list[dict[str, Any]] = []
    truth_row, truth_col = nearest_truth_cell(grid)

    for col, noise in enumerate(NOISE_LEVELS):
        residuals = simulate_residuals(*noise)
        second_weight, standard_weight, robust_weight = scenario_weights(residuals, noise)
        standard = evaluate_standard_projection(
            residuals,
            grid,
            spec,
            second_weight,
            standard_weight,
        )
        robust = evaluate_robust_projection(residuals, noise, grid, spec, robust_weight)
        second_truth, standard_truth = standard_truth_j(
            residuals,
            second_weight,
            standard_weight,
        )
        robust_truth, true_lambda = robust_truth_j(residuals, noise, robust_weight)

        sign_mask = standard["sign_mask"]
        standard_mask = standard["standard_mask"]
        robust_mask = robust["robust_mask"]
        robust_lambda_cell = (
            float(robust["best_lambda_1"][truth_row, truth_col])
            if np.isfinite(robust["best_lambda_1"][truth_row, truth_col])
            else math.nan,
            float(robust["best_lambda_2"][truth_row, truth_col])
            if np.isfinite(robust["best_lambda_2"][truth_row, truth_col])
            else math.nan,
        )

        label = f"V=({noise[0]:g},{noise[1]:g})"
        diagnostics.append(
            {
                "label": label,
                "noise": list(noise),
                "shares": {
                    "sign": mask_share(sign_mask),
                    "standard_dw": mask_share(standard_mask),
                    "robust_dw": mask_share(robust_mask),
                },
                "truth": {
                    "second_j": second_truth,
                    "standard_j": standard_truth,
                    "standard_in": bool(second_truth <= CHI2_90_DF3 and standard_truth <= CHI2_90_DF5),
                    "robust_j": robust_truth,
                    "robust_in": bool(
                        true_lambda[0] <= RELATIVE_NOISE_RATIO
                        and true_lambda[1] <= RELATIVE_NOISE_RATIO
                        and robust_truth <= CHI2_90_DF8
                    ),
                    "true_lambda": list(true_lambda),
                },
                "distances": {
                    "sign_to_truth": truth_distance(sign_mask, grid),
                    "standard_to_truth": truth_distance(standard_mask, grid),
                    "robust_to_truth": truth_distance(robust_mask, grid),
                },
                "best_truth_cell_lambda": list(robust_lambda_cell),
                "robust_prefilter_count": robust["prefilter_count"],
            }
        )

        ax = axes[0, col]
        draw_mask(ax, grid, sign_mask, "#9bc9a6", 0.92)
        ax.set_title(f"No-noise sign/covariance, {label}")
        sign_truth_in = second_truth <= CHI2_90_DF3
        draw_truth_marker(ax, sign_truth_in)
        ax.text(
            B12_MIN + 0.08,
            B21_MAX - 0.22,
            f"share {mask_share(sign_mask):.3f}\nB0 {'in' if sign_truth_in else 'out'}; J2 {second_truth:.2f}",
            color="#11623a",
            fontsize=9,
        )

        ax = axes[1, col]
        draw_mask(ax, grid, sign_mask, "#d9d9d9", 0.45)
        draw_mask(ax, grid, standard_mask, "#6a51a3", 0.90)
        ax.set_title(f"Standard DW GMM1, {label}")
        standard_status = "in" if second_truth <= CHI2_90_DF3 and standard_truth <= CHI2_90_DF5 else "out"
        draw_truth_marker(ax, standard_status == "in")
        ax.text(
            B12_MIN + 0.08,
            B21_MAX - 0.25,
            f"share {mask_share(standard_mask):.3f}\nB0 {standard_status}; JH {standard_truth:.2f}",
            color="#542788",
            fontsize=9,
        )

        ax = axes[2, col]
        draw_mask(ax, grid, robust_mask, "#67a9cf", 0.90)
        ax.set_title(f"Robust projected GMM, {label}")
        robust_status = "in" if diagnostics[-1]["truth"]["robust_in"] else "out"
        draw_truth_marker(ax, robust_status == "in")
        ax.text(
            B12_MIN + 0.08,
            B21_MAX - 0.25,
            f"share {mask_share(robust_mask):.3f}\nB0 {robust_status}; J {robust_truth:.2f}",
            color="#2166ac",
            fontsize=9,
        )

    for ax in axes.flat:
        draw_panel_style(ax, grid)
    for ax in axes[2, :]:
        ax.set_xlabel("B12")
    for ax in axes[:, 0]:
        ax.set_ylabel("B21")

    fig.suptitle(
        (
            "Figure 1: unit-variance projection to (B12,B21); "
            "B11/B22 profiled, B11>0, B22>0, sign B21>=0\n"
            f"T={SAMPLE_SIZE}; rho={RELATIVE_NOISE_RATIO}; pointwise diagnostic cutoffs "
            f"chi2_3={CHI2_90_DF3:.2f}, chi2_5={CHI2_90_DF5:.2f}, chi2_8={CHI2_90_DF8:.2f}"
        ),
        fontsize=12,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    write_outputs(diagnostics, spec, output_path, note_path, json_path)
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="", help="Optional figure output path.")
    parser.add_argument("--note-output", default="", help="Optional Markdown note output path.")
    parser.add_argument("--json-output", default="", help="Optional JSON diagnostics output path.")
    parser.add_argument("--projection-points", type=int, default=GridSpec.projection_points)
    parser.add_argument("--diagonal-points", type=int, default=GridSpec.diagonal_points)
    parser.add_argument("--lambda-points", type=int, default=GridSpec.lambda_points)
    parser.add_argument("--robust-batch-size", type=int, default=GridSpec.robust_batch_size)
    parser.add_argument("--standard-batch-size", type=int, default=GridSpec.standard_batch_size)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    spec = GridSpec(
        projection_points=args.projection_points,
        diagonal_points=args.diagonal_points,
        lambda_points=args.lambda_points,
        robust_batch_size=args.robust_batch_size,
        standard_batch_size=args.standard_batch_size,
    )
    path = plot(
        output_path=Path(args.output) if args.output else OUTPUT_PATH,
        note_path=Path(args.note_output) if args.note_output else NOTE_PATH,
        json_path=Path(args.json_output) if args.json_output else JSON_PATH,
        spec=spec,
    )
    print(f"Wrote {display_path(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
