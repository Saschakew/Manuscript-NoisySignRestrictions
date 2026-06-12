"""Build unit-variance first-shock impact grid figures.

The figures replace the historical diagonal-normalized B-plane figures and
the M67 ``(B12, B21)`` projection. They use the M64/M66 route: structural
shocks have unit variance, residual-noise variances are nuisance parameters,
and the robust row projects accepted ``(B, lambda)`` pairs onto displayed
impact coordinates.

The active M71 chart reports the impact vector of the first shock,
``(B11, B21)``. For each plotted ``(B11, B21)`` point, the script profiles
``B12`` and ``B22`` while imposing the maintained sign screen
``B11 > 0``, ``B22 > 0``, and ``B12 <= 0``. The robust row then searches over
``lambda in [0, rho]^2`` and evaluates the Section 4 moment vector at
``nu_i(B, lambda) = lambda_i (B B')_ii``. Every statistic uses a
candidate-specific pointwise covariance estimate.
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
B12_MAX = 0.0
B21_MIN = -1.45
B21_MAX = 1.90
B11_MIN = 0.35
B11_MAX = 1.65
B22_MIN = 0.55
B22_MAX = 1.45


@dataclass(frozen=True)
class GridSpec:
    projection_points: int = 31
    profile_points: int = 9
    lambda_points: int = 5
    robust_batch_size: int = 48
    standard_batch_size: int = 240


@dataclass(frozen=True)
class FigureScenario:
    label: str
    noise: tuple[float, float]
    sample_size: int = SAMPLE_SIZE
    non_gaussian_weight: float = 1.0
    seed: int = RANDOM_SEED
    residual_noise: str = "gaussian"


@dataclass(frozen=True)
class CandidateGrid:
    b11: np.ndarray
    b12: np.ndarray
    b21: np.ndarray
    b22: np.ndarray
    b11_index: np.ndarray
    b21_index: np.ndarray
    b11_values: np.ndarray
    b21_values: np.ndarray


FIGURE_SCENARIOS = {
    "noise": (
        FigureScenario("V=(0,0)", (0.0, 0.0)),
        FigureScenario("V=(0.2,0.2)", (0.2, 0.2)),
        FigureScenario("V=(0.5,0.5)", (0.5, 0.5)),
    ),
    "nongaussianity": (
        FigureScenario("w=1", (0.2, 0.2), non_gaussian_weight=1.0),
        FigureScenario("w=0.25", (0.2, 0.2), non_gaussian_weight=0.25),
        FigureScenario("w=0", (0.2, 0.2), non_gaussian_weight=0.0),
    ),
    "sample_size": (
        FigureScenario("T=500", (0.2, 0.2), sample_size=500),
        FigureScenario("T=1000", (0.2, 0.2), sample_size=1000),
        FigureScenario("T=2000", (0.2, 0.2), sample_size=2000),
    ),
}


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


def primitive_draws(
    sample_size: int = SAMPLE_SIZE,
    seed: int = RANDOM_SEED,
    non_gaussian_weight: float = 1.0,
    residual_noise: str = "gaussian",
) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    skewed = standardize_columns(rng.chisquare(df=STRUCTURAL_CHI2_DF, size=(sample_size, 2)))
    if non_gaussian_weight >= 1.0 - 1e-12:
        structural = skewed
    elif non_gaussian_weight <= 1e-12:
        structural = standardize_columns(rng.normal(size=(sample_size, 2)))
    else:
        gaussian = standardize_columns(rng.normal(size=(sample_size, 2)))
        structural = math.sqrt(non_gaussian_weight) * skewed
        structural += math.sqrt(max(0.0, 1.0 - non_gaussian_weight)) * gaussian
        structural = standardize_columns(structural)
    if residual_noise == "gaussian":
        noise = standardize_columns(rng.normal(size=(sample_size, 2)))
    elif residual_noise == "skewed":
        noise = standardize_columns(rng.chisquare(df=STRUCTURAL_CHI2_DF, size=(sample_size, 2)))
    else:
        raise ValueError(f"unknown residual-noise type: {residual_noise}")
    return structural, noise


def simulate_residuals(
    nu1: float,
    nu2: float,
    sample_size: int = SAMPLE_SIZE,
    seed: int = RANDOM_SEED,
    non_gaussian_weight: float = 1.0,
    residual_noise: str = "gaussian",
) -> np.ndarray:
    structural, noise = primitive_draws(sample_size, seed, non_gaussian_weight, residual_noise)
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
    b11_values = unique_grid(B11_MIN, B11_MAX, spec.projection_points, TRUE_B11)
    b21_values = unique_grid(B21_MIN, B21_MAX, spec.projection_points, TRUE_B21)
    b12_values = unique_grid(B12_MIN, B12_MAX, spec.profile_points, TRUE_B12)
    b22_values = unique_grid(B22_MIN, B22_MAX, spec.profile_points, TRUE_B22)

    b11_index, b21_index, b12_index, b22_index = np.meshgrid(
        np.arange(b11_values.size),
        np.arange(b21_values.size),
        np.arange(b12_values.size),
        np.arange(b22_values.size),
        indexing="ij",
    )
    b11 = b11_values[b11_index].ravel()
    b21 = b21_values[b21_index].ravel()
    b12 = b12_values[b12_index].ravel()
    b22 = b22_values[b22_index].ravel()

    sign_and_orientation = (b11 > 0.0) & (b22 > 0.0) & (b12 <= 0.0)
    determinant = b11 * b22 - b12 * b21
    nonsingular = np.abs(determinant) > 1e-8
    keep = sign_and_orientation & nonsingular
    return CandidateGrid(
        b11=b11[keep],
        b12=b12[keep],
        b21=b21[keep],
        b22=b22[keep],
        b11_index=b11_index.ravel()[keep],
        b21_index=b21_index.ravel()[keep],
        b11_values=b11_values,
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


def empty_regularization_stats() -> dict[str, Any]:
    return {
        "matrix_count": 0,
        "regularized_matrix_count": 0,
        "regularized_eigenvalue_count": 0,
        "min_eigenvalue_before_floor": None,
        "max_eigenvalue_floor": None,
    }


def merge_regularization_stats(target: dict[str, Any], label: str, update: dict[str, Any]) -> None:
    entry = target.setdefault(label, empty_regularization_stats())
    entry["matrix_count"] += int(update["matrix_count"])
    entry["regularized_matrix_count"] += int(update["regularized_matrix_count"])
    entry["regularized_eigenvalue_count"] += int(update["regularized_eigenvalue_count"])
    for key, reducer in (
        ("min_eigenvalue_before_floor", min),
        ("max_eigenvalue_floor", max),
    ):
        value = update[key]
        if value is None:
            continue
        if entry[key] is None:
            entry[key] = float(value)
        else:
            entry[key] = float(reducer(float(entry[key]), float(value)))


def regularized_inverse_stack(covariance: np.ndarray) -> tuple[np.ndarray, dict[str, Any]]:
    covariance = 0.5 * (covariance + np.swapaxes(covariance, -1, -2))
    values, vectors = np.linalg.eigh(covariance)
    raw_values = values.copy()
    max_values = np.maximum(np.max(values, axis=1), 1.0)
    floors = max_values[:, None] * 1e-10
    regularized = values < floors
    values = np.maximum(values, floors)
    stats = {
        "matrix_count": int(values.shape[0]),
        "regularized_matrix_count": int(np.count_nonzero(np.any(regularized, axis=1))),
        "regularized_eigenvalue_count": int(np.count_nonzero(regularized)),
        "min_eigenvalue_before_floor": float(np.min(raw_values)) if raw_values.size else None,
        "max_eigenvalue_floor": float(np.max(floors)) if floors.size else None,
    }
    return np.einsum("bij,bj,bkj->bik", vectors, 1.0 / values, vectors), stats


def j_from_observations(
    observations: np.ndarray,
    regularization: dict[str, Any] | None = None,
    label: str = "criterion",
) -> np.ndarray:
    mean = observations.mean(axis=0)
    centered = observations - mean[None, :, :]
    covariance = np.einsum("tbi,tbj->bij", centered, centered) / observations.shape[0]
    inverse, stats = regularized_inverse_stack(covariance)
    if regularization is not None:
        merge_regularization_stats(regularization, label, stats)
    return observations.shape[0] * np.einsum("bi,bij,bj->b", mean, inverse, mean)


def second_moment_observations(shocks: np.ndarray) -> np.ndarray:
    e1 = shocks[:, :, 0]
    e2 = shocks[:, :, 1]
    return np.stack([e1 * e1 - 1.0, e1 * e2, e2 * e2 - 1.0], axis=2)


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


def evaluate_standard_projection(
    residuals: np.ndarray,
    grid: CandidateGrid,
    spec: GridSpec,
) -> dict[str, Any]:
    shape = (grid.b21_values.size, grid.b11_values.size)
    sign_mask = np.zeros(shape, dtype=bool)
    standard_mask = np.zeros(shape, dtype=bool)
    best_second = np.full(shape, np.nan)
    best_standard = np.full(shape, np.nan)
    regularization: dict[str, Any] = {}

    for start in range(0, grid.b11.size, spec.standard_batch_size):
        end = min(start + spec.standard_batch_size, grid.b11.size)
        shocks = recovered_shocks(
            residuals,
            grid.b11[start:end],
            grid.b12[start:end],
            grid.b21[start:end],
            grid.b22[start:end],
        )
        second_j = j_from_observations(
            second_moment_observations(shocks),
            regularization,
            "second_moment",
        )
        standard_j = j_from_observations(
            standard_dw_observations(shocks),
            regularization,
            "standard_dw",
        )
        sign_accept = second_j <= CHI2_90_DF3
        standard_accept = sign_accept & (standard_j <= CHI2_90_DF5)
        rows = grid.b21_index[start:end]
        cols = grid.b11_index[start:end]
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
        "regularization": regularization,
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
) -> dict[str, Any]:
    shape = (grid.b21_values.size, grid.b11_values.size)
    robust_mask = np.zeros(shape, dtype=bool)
    best_robust = np.full(shape, np.nan)
    best_lambda_1 = np.full(shape, np.nan)
    best_lambda_2 = np.full(shape, np.nan)
    regularization: dict[str, Any] = {}

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
        observations = robust_observations(residuals, shocks, b11, b12, b21, b22, lambda_pairs)
        robust_j = j_from_observations(observations, regularization, "robust_full").reshape(
            selected.size,
            lambda_pairs.shape[0],
        )
        lambda_min_index = np.nanargmin(robust_j, axis=1)
        min_j = robust_j[np.arange(selected.size), lambda_min_index]
        rows = grid.b21_index[selected]
        cols = grid.b11_index[selected]
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
        "regularization": regularization,
    }


def robust_truth_j(
    residuals: np.ndarray,
    noise: tuple[float, float],
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
    observations = robust_observations(
        residuals,
        shocks,
        np.array([TRUE_B11]),
        np.array([TRUE_B12]),
        np.array([TRUE_B21]),
        np.array([TRUE_B22]),
        np.array(lambda_pair, dtype=float)[None, :],
    )
    return float(j_from_observations(observations)[0]), lambda_pair


def standard_truth_j(residuals: np.ndarray) -> tuple[float, float]:
    shocks = recovered_shocks(
        residuals,
        np.array([TRUE_B11]),
        np.array([TRUE_B12]),
        np.array([TRUE_B21]),
        np.array([TRUE_B22]),
    )
    second_j = float(j_from_observations(second_moment_observations(shocks))[0])
    standard_j = float(j_from_observations(standard_dw_observations(shocks))[0])
    return second_j, standard_j


def mask_share(mask: np.ndarray) -> float:
    return float(np.count_nonzero(mask) / mask.size)


def truth_distance(mask: np.ndarray, grid: CandidateGrid) -> float | None:
    if not mask.any():
        return None
    b11_mesh, b21_mesh = np.meshgrid(grid.b11_values, grid.b21_values)
    distances = np.hypot(b11_mesh[mask] - TRUE_B11, b21_mesh[mask] - TRUE_B21)
    return float(np.min(distances))


def boundary_flags(mask: np.ndarray) -> dict[str, bool]:
    return {
        "touches_b11_min": bool(mask[:, 0].any()),
        "touches_b11_max": bool(mask[:, -1].any()),
        "touches_b21_min": bool(mask[0, :].any()),
        "touches_b21_max": bool(mask[-1, :].any()),
    }


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
    scenario_set: str,
) -> None:
    payload = {
        "schema_version": 1,
        "task": "M71 remove B21 sign and pointwise weighting",
        "figure": display_path(output_path),
        "description": "Projected unit-variance first-shock grid over (B11,B21), with B12/B22 and lambda profiled, no B21 sign restriction, and candidate-specific pointwise covariance weighting.",
        "configuration": {
            "scenario_set": scenario_set,
            "rho": RELATIVE_NOISE_RATIO,
            "projection_points": spec.projection_points,
            "profile_points": spec.profile_points,
            "lambda_points": spec.lambda_points,
            "true_B0": TRUE_MATRIX.tolist(),
            "critical_values": {
                "second_moment_chi2_90_df3": CHI2_90_DF3,
                "standard_dw_chi2_90_df5": CHI2_90_DF5,
                "robust_full_moment_chi2_90_df8": CHI2_90_DF8,
            },
            "displayed_projection": ["B11", "B21"],
            "profiled_coordinates": ["B12", "B22", "lambda1", "lambda2"],
            "sign_restrictions": ["B11 > 0", "B22 > 0", "B12 <= 0"],
            "weighting": "candidate-specific pointwise covariance estimates for each tested B or (B,lambda) candidate",
            "weight_regularization": "symmetric covariance eigensystem with eigenvalue floor max(max_eigenvalue, 1) * 1e-10",
        },
        "diagnostics": diagnostics,
    }
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# M71 Unit-Variance First-Shock Figure Diagnostics",
        "",
        "Status: generated corrected first-shock impact figure for the M64/M66 unit-variance route after M71.",
        "",
        "The chart displays the projection of accepted matrices onto `(B11, B21)`, the impact vector of the first shock. It does not impose `diag(B)=1`: for every displayed projection point the script searches over `B12` and `B22`. The maintained sign screen is `B11>0`, `B22>0`, and `B12<=0`; `B21` is displayed but not sign-restricted. The robust row also searches over `lambda in [0,rho]^2` and sets `nu_i=lambda_i (B B')_ii` before evaluating the Section 4 moment vector.",
        "",
        "Truth markers refer to the full true matrix, not merely to whether the true `(B11,B21)` projection cell contains some other accepted profiled pair: a star means the full true `B0` passes that row's test, and an x means it does not.",
        "",
        "The plotted statistics use candidate-specific pointwise covariance estimates: for each tested `B` or `(B,lambda)` candidate, the script estimates the covariance of that candidate's moment observations and computes `T g' W g`. The robust cutoff is a pointwise diagnostic chi-square cutoff for the eight displayed moment rows. The final projection-critical-value choice remains part of the broader M65 evidence task.",
        "",
        "## Configuration",
        "",
        f"- Output figure: `{display_path(output_path)}`.",
        f"- Machine-readable diagnostics: `{display_path(json_path)}`.",
        f"- Noise ratio bound: `rho={RELATIVE_NOISE_RATIO}`.",
        f"- Projection grid: `{spec.projection_points} x {spec.projection_points}` plus true coordinates.",
        f"- Profile grid: `{spec.profile_points} x {spec.profile_points}` plus true profiled coordinates.",
        f"- Lambda grid: `{spec.lambda_points} x {spec.lambda_points}` plus the true lambda values for each scenario.",
        "- Weighting: candidate-specific pointwise covariance estimates for each tested candidate.",
        "- Weight regularization: symmetric covariance eigensystem with eigenvalue floor `max(max_eigenvalue, 1) * 1e-10`.",
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
            "| The displayed chart is a projection to `(B11,B21)`, with `B12`, `B22`, and `lambda` profiled. | `code-implemented`, `user-decision` | Candidate grid construction and diagnostics JSON; M71 task. | high | promote |",
            "| The maintained sign screen is `B11>0`, `B22>0`, and `B12<=0`; `B21` is unrestricted. | `code-implemented`, `user-decision` | Candidate grid construction and diagnostics JSON; M71 task. | high | promote |",
            "| The plotted statistics use candidate-specific pointwise covariance weights. | `code-implemented`, `user-decision` | `j_from_observations` calls in the evaluator. | high | promote as diagnostic implementation detail |",
            "| The robust cutoff is final for projected inference. | `conjectural` | M65 still lists projection critical values as unresolved. | medium | quarantine as diagnostic |",
            "",
        ]
    )
    note_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def draw_mask(ax: Any, grid: CandidateGrid, mask: np.ndarray, color: str, alpha: float) -> None:
    b11_mesh, b21_mesh = np.meshgrid(grid.b11_values, grid.b21_values)
    if mask.any():
        ax.contourf(
            b11_mesh,
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
    ax.set_xlim(float(grid.b11_values.min()), float(grid.b11_values.max()))
    ax.set_ylim(float(grid.b21_values.min()), float(grid.b21_values.max()))
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.18)


def draw_truth_marker(ax: Any, accepted: bool) -> None:
    if accepted:
        ax.scatter(
            [TRUE_B11],
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
            [TRUE_B11],
            [TRUE_B21],
            marker="x",
            color="#b2182b",
            linewidth=2.0,
            s=90,
            zorder=6,
        )


def nearest_truth_cell(grid: CandidateGrid) -> tuple[int, int]:
    col = int(np.argmin(np.abs(grid.b11_values - TRUE_B11)))
    row = int(np.argmin(np.abs(grid.b21_values - TRUE_B21)))
    return row, col


def plot(
    output_path: Path = OUTPUT_PATH,
    note_path: Path = NOTE_PATH,
    json_path: Path = JSON_PATH,
    spec: GridSpec = GridSpec(),
    scenarios: tuple[FigureScenario, ...] = FIGURE_SCENARIOS["noise"],
    scenario_set: str = "noise",
) -> Path:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    grid = make_candidate_grid(spec)
    fig, axes = plt.subplots(
        3,
        len(scenarios),
        figsize=(15.6, 11.4),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )
    diagnostics: list[dict[str, Any]] = []
    truth_row, truth_col = nearest_truth_cell(grid)

    for col, scenario in enumerate(scenarios):
        noise = scenario.noise
        residuals = simulate_residuals(
            *noise,
            sample_size=scenario.sample_size,
            seed=scenario.seed,
            non_gaussian_weight=scenario.non_gaussian_weight,
            residual_noise=scenario.residual_noise,
        )
        standard = evaluate_standard_projection(
            residuals,
            grid,
            spec,
        )
        robust = evaluate_robust_projection(residuals, noise, grid, spec)
        second_truth, standard_truth = standard_truth_j(residuals)
        robust_truth, true_lambda = robust_truth_j(residuals, noise)

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

        label = scenario.label
        diagnostics.append(
            {
                "label": label,
                "noise": list(noise),
                "sample_size": scenario.sample_size,
                "seed": scenario.seed,
                "non_gaussian_weight": scenario.non_gaussian_weight,
                "residual_noise": scenario.residual_noise,
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
                "boundary": {
                    "sign": boundary_flags(sign_mask),
                    "standard_dw": boundary_flags(standard_mask),
                    "robust_dw": boundary_flags(robust_mask),
                },
                "best_truth_cell_lambda": list(robust_lambda_cell),
                "robust_prefilter_count": robust["prefilter_count"],
                "regularization": {
                    "standard": standard["regularization"],
                    "robust": robust["regularization"],
                },
            }
        )

        ax = axes[0, col]
        draw_mask(ax, grid, sign_mask, "#9bc9a6", 0.92)
        ax.set_title(f"No-noise sign/covariance, {label}")
        sign_truth_in = second_truth <= CHI2_90_DF3
        draw_truth_marker(ax, sign_truth_in)
        ax.text(
            B11_MIN + 0.08,
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
            B11_MIN + 0.08,
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
            B11_MIN + 0.08,
            B21_MAX - 0.25,
            f"share {mask_share(robust_mask):.3f}\nB0 {robust_status}; J {robust_truth:.2f}",
            color="#2166ac",
            fontsize=9,
        )

    for ax in axes.flat:
        draw_panel_style(ax, grid)
    for ax in axes[2, :]:
        ax.set_xlabel("B11")
    for ax in axes[:, 0]:
        ax.set_ylabel("B21")

    fig.suptitle(
        (
            f"Unit-variance {scenario_set.replace('_', '-')} projection to (B11,B21); "
            "B12/B22 profiled, signs B11>0, B22>0, B12<=0\n"
            f"rho={RELATIVE_NOISE_RATIO}; pointwise diagnostic cutoffs "
            f"chi2_3={CHI2_90_DF3:.2f}, chi2_5={CHI2_90_DF5:.2f}, chi2_8={CHI2_90_DF8:.2f}"
        ),
        fontsize=12,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    write_outputs(diagnostics, spec, output_path, note_path, json_path, scenario_set)
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="", help="Optional figure output path.")
    parser.add_argument("--note-output", default="", help="Optional Markdown note output path.")
    parser.add_argument("--json-output", default="", help="Optional JSON diagnostics output path.")
    parser.add_argument("--projection-points", type=int, default=GridSpec.projection_points)
    parser.add_argument("--profile-points", type=int, default=GridSpec.profile_points)
    parser.add_argument("--lambda-points", type=int, default=GridSpec.lambda_points)
    parser.add_argument("--robust-batch-size", type=int, default=GridSpec.robust_batch_size)
    parser.add_argument("--standard-batch-size", type=int, default=GridSpec.standard_batch_size)
    parser.add_argument(
        "--scenario-set",
        choices=tuple(FIGURE_SCENARIOS.keys()),
        default="noise",
        help="Which three-column figure scenario set to render.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    spec = GridSpec(
        projection_points=args.projection_points,
        profile_points=args.profile_points,
        lambda_points=args.lambda_points,
        robust_batch_size=args.robust_batch_size,
        standard_batch_size=args.standard_batch_size,
    )
    path = plot(
        output_path=Path(args.output) if args.output else OUTPUT_PATH,
        note_path=Path(args.note_output) if args.note_output else NOTE_PATH,
        json_path=Path(args.json_output) if args.json_output else JSON_PATH,
        spec=spec,
        scenarios=FIGURE_SCENARIOS[args.scenario_set],
        scenario_set=args.scenario_set,
    )
    print(f"Wrote {display_path(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
