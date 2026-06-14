"""Full-grid cleaned iid sample-size MC with analytic GMM weights.

M78 extends the M77 truth-at-B0 audit to the full sample-size projection table.
It keeps the M74 sample-size scenarios and grid, but uses the cleaned iid DGP:
population-normalized chi-square structural shocks, iid Gaussian residual
noise, no sample standardization, no residual demeaning, and no recovered-shock
demeaning. Sign and DW use analytic no-noise weights for their moment stacks.
nrDW uses candidate-specific analytic iid weights W=(E[f_t f_t'])^{-1}.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import traceback
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np

try:
    from . import m69_extended_three_block_mc as m69
    from . import m77_clean_iid_mc_efficient_weight as m77
    from . import sign_dw_unit_variance_noise_grid_figure as fig
except ImportError:
    import m69_extended_three_block_mc as m69
    import m77_clean_iid_mc_efficient_weight as m77
    import sign_dw_unit_variance_noise_grid_figure as fig


ROOT = Path(__file__).resolve().parents[2]
SIM_DIR = ROOT / "manuscript" / "simulations"
OUTPUT_DIR = SIM_DIR / "output"
JSON_OUTPUT = OUTPUT_DIR / "m78_clean_iid_full_sample_size_mc.json"
NOTE_OUTPUT = SIM_DIR / "m78_clean_iid_full_sample_size_mc.md"

SAMPLE_SCENARIOS = m77.SAMPLE_SCENARIOS

Exponent = tuple[int, int, int, int]
VectorPolynomial = dict[Exponent, np.ndarray]


@dataclass
class RobustWeightCache:
    grid: fig.CandidateGrid
    lambda_pairs: np.ndarray
    cache: dict[int, np.ndarray]
    stats: dict[str, Any]

    @classmethod
    def create(cls, grid: fig.CandidateGrid, lambda_pairs: np.ndarray) -> "RobustWeightCache":
        return cls(
            grid=grid,
            lambda_pairs=lambda_pairs,
            cache={},
            stats={
                "computed_b_candidates": 0,
                "computed_candidate_lambda_pairs": 0,
                "regularization": empty_regularization_stats(),
                "max_abs_moment_mean": 0.0,
            },
        )

    def get(self, indices: np.ndarray) -> np.ndarray:
        missing = [int(index) for index in indices if int(index) not in self.cache]
        if missing:
            missing_array = np.asarray(missing, dtype=int)
            pair_count = self.lambda_pairs.shape[0]
            b11 = np.repeat(self.grid.b11[missing_array], pair_count)
            b12 = np.repeat(self.grid.b12[missing_array], pair_count)
            b21 = np.repeat(self.grid.b21[missing_array], pair_count)
            b22 = np.repeat(self.grid.b22[missing_array], pair_count)
            lambda_1 = np.tile(self.lambda_pairs[:, 0], missing_array.size)
            lambda_2 = np.tile(self.lambda_pairs[:, 1], missing_array.size)
            inverse, stats, max_abs_mean = robust_inverse_weight_stack(
                b11,
                b12,
                b21,
                b22,
                lambda_1,
                lambda_2,
            )
            inverse = inverse.reshape(missing_array.size, pair_count, 8, 8)
            for local, index in enumerate(missing):
                self.cache[index] = inverse[local]
            self.stats["computed_b_candidates"] += int(missing_array.size)
            self.stats["computed_candidate_lambda_pairs"] += int(missing_array.size * pair_count)
            merge_regularization_stats(self.stats["regularization"], stats)
            self.stats["max_abs_moment_mean"] = max(
                float(self.stats["max_abs_moment_mean"]),
                float(max_abs_mean),
            )
        return np.concatenate([self.cache[int(index)] for index in indices], axis=0)


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def coefficient(value: float | np.ndarray, size: int) -> np.ndarray:
    array = np.asarray(value, dtype=float)
    if array.ndim == 0:
        return np.full(size, float(array), dtype=float)
    if array.shape != (size,):
        raise ValueError(f"expected coefficient shape {(size,)}, got {array.shape}")
    return array.astype(float, copy=False)


def vpoly_constant(value: float | np.ndarray, size: int) -> VectorPolynomial:
    array = coefficient(value, size)
    if not np.any(np.abs(array) > 1e-14):
        return {}
    return {(0, 0, 0, 0): array}


def vpoly_variable(index: int, size: int, value: float | np.ndarray = 1.0) -> VectorPolynomial:
    exponent = [0, 0, 0, 0]
    exponent[index] = 1
    return {tuple(exponent): coefficient(value, size)}


def vpoly_add(size: int, *polys: VectorPolynomial) -> VectorPolynomial:
    result: VectorPolynomial = {}
    for poly in polys:
        for exponent, value in poly.items():
            if exponent not in result:
                result[exponent] = np.zeros(size, dtype=float)
            result[exponent] = result[exponent] + value
    return {
        exponent: value
        for exponent, value in result.items()
        if np.any(np.abs(value) > 1e-14)
    }


def vpoly_scale(poly: VectorPolynomial, scale: float | np.ndarray, size: int) -> VectorPolynomial:
    scale_array = coefficient(scale, size)
    if not np.any(np.abs(scale_array) > 1e-14):
        return {}
    return {
        exponent: value * scale_array
        for exponent, value in poly.items()
        if np.any(np.abs(value * scale_array) > 1e-14)
    }


def vpoly_sub(left: VectorPolynomial, right: VectorPolynomial, size: int) -> VectorPolynomial:
    return vpoly_add(size, left, vpoly_scale(right, -1.0, size))


def vpoly_mul(left: VectorPolynomial, right: VectorPolynomial, size: int) -> VectorPolynomial:
    result: VectorPolynomial = {}
    for exp_left, coef_left in left.items():
        for exp_right, coef_right in right.items():
            exponent = tuple(a + b for a, b in zip(exp_left, exp_right))
            if exponent not in result:
                result[exponent] = np.zeros(size, dtype=float)
            result[exponent] = result[exponent] + coef_left * coef_right
    return {
        exponent: value
        for exponent, value in result.items()
        if np.any(np.abs(value) > 1e-14)
    }


def vpoly_pow(poly: VectorPolynomial, power: int, size: int) -> VectorPolynomial:
    result = vpoly_constant(1.0, size)
    for _ in range(power):
        result = vpoly_mul(result, poly, size)
    return result


def vpoly_expectation(poly: VectorPolynomial, size: int) -> np.ndarray:
    total = np.zeros(size, dtype=float)
    for exponent, value in poly.items():
        moment = (
            m77.STRUCTURAL_MOMENTS[exponent[0]]
            * m77.STRUCTURAL_MOMENTS[exponent[1]]
            * m77.GAUSSIAN_MOMENTS[exponent[2]]
            * m77.GAUSSIAN_MOMENTS[exponent[3]]
        )
        total = total + value * moment
    return total


def covariance_from_vpolynomials(
    moments: list[VectorPolynomial],
    size: int,
) -> tuple[np.ndarray, dict[str, Any], float]:
    means = np.stack([vpoly_expectation(poly, size) for poly in moments], axis=1)
    k = len(moments)
    covariance = np.empty((size, k, k), dtype=float)
    for i, left in enumerate(moments):
        for j, right in enumerate(moments):
            product = vpoly_mul(left, right, size)
            covariance[:, i, j] = vpoly_expectation(product, size) - means[:, i] * means[:, j]
    covariance = 0.5 * (covariance + np.swapaxes(covariance, 1, 2))
    inverse, stats = fig.regularized_inverse_stack(covariance)
    return inverse, stats, float(np.max(np.abs(means))) if means.size else 0.0


def robust_inverse_weight_stack(
    b11: np.ndarray,
    b12: np.ndarray,
    b21: np.ndarray,
    b22: np.ndarray,
    lambda_1: np.ndarray,
    lambda_2: np.ndarray,
) -> tuple[np.ndarray, dict[str, Any], float]:
    size = int(np.asarray(b11).size)
    b11 = np.asarray(b11, dtype=float)
    b12 = np.asarray(b12, dtype=float)
    b21 = np.asarray(b21, dtype=float)
    b22 = np.asarray(b22, dtype=float)
    lambda_1 = np.asarray(lambda_1, dtype=float)
    lambda_2 = np.asarray(lambda_2, dtype=float)

    signal_11 = b11 * b11 + b12 * b12
    signal_12 = b11 * b21 + b12 * b22
    signal_22 = b21 * b21 + b22 * b22
    nu1 = signal_11 * lambda_1
    nu2 = signal_22 * lambda_2

    eps1 = vpoly_variable(0, size)
    eps2 = vpoly_variable(1, size)
    eta1 = vpoly_variable(2, size, np.sqrt(np.maximum(nu1, 0.0)))
    eta2 = vpoly_variable(3, size, np.sqrt(np.maximum(nu2, 0.0)))
    u1 = vpoly_add(size, vpoly_scale(eps1, b11, size), vpoly_scale(eps2, b12, size), eta1)
    u2 = vpoly_add(size, vpoly_scale(eps1, b21, size), vpoly_scale(eps2, b22, size), eta2)

    determinant = b11 * b22 - b12 * b21
    inv11 = b22 / determinant
    inv12 = -b12 / determinant
    inv21 = -b21 / determinant
    inv22 = b11 / determinant
    e1 = vpoly_add(size, vpoly_scale(u1, inv11, size), vpoly_scale(u2, inv12, size))
    e2 = vpoly_add(size, vpoly_scale(u1, inv21, size), vpoly_scale(u2, inv22, size))

    omega11 = 1.0 + inv11 * inv11 * nu1 + inv12 * inv12 * nu2
    omega12 = inv11 * inv21 * nu1 + inv12 * inv22 * nu2
    omega22 = 1.0 + inv21 * inv21 * nu1 + inv22 * inv22 * nu2

    moments = [
        vpoly_sub(vpoly_pow(u1, 2, size), vpoly_constant(signal_11 + nu1, size), size),
        vpoly_sub(vpoly_mul(u1, u2, size), vpoly_constant(signal_12, size), size),
        vpoly_sub(vpoly_pow(u2, 2, size), vpoly_constant(signal_22 + nu2, size), size),
        vpoly_mul(vpoly_pow(e1, 2, size), e2, size),
        vpoly_mul(e1, vpoly_pow(e2, 2, size), size),
        vpoly_sub(
            vpoly_mul(vpoly_pow(e1, 3, size), e2, size),
            vpoly_constant(3.0 * omega11 * omega12, size),
            size,
        ),
        vpoly_sub(
            vpoly_mul(vpoly_pow(e1, 2, size), vpoly_pow(e2, 2, size), size),
            vpoly_constant(omega11 * omega22 + 2.0 * omega12 * omega12, size),
            size,
        ),
        vpoly_sub(
            vpoly_mul(e1, vpoly_pow(e2, 3, size), size),
            vpoly_constant(3.0 * omega22 * omega12, size),
            size,
        ),
    ]
    return covariance_from_vpolynomials(moments, size)


def empty_regularization_stats() -> dict[str, Any]:
    return {
        "matrix_count": 0,
        "regularized_matrix_count": 0,
        "regularized_eigenvalue_count": 0,
        "min_eigenvalue_before_floor": None,
        "max_eigenvalue_floor": None,
    }


def merge_regularization_stats(target: dict[str, Any], update: dict[str, Any]) -> None:
    target["matrix_count"] += int(update["matrix_count"])
    target["regularized_matrix_count"] += int(update["regularized_matrix_count"])
    target["regularized_eigenvalue_count"] += int(update["regularized_eigenvalue_count"])
    for key, reducer in (
        ("min_eigenvalue_before_floor", min),
        ("max_eigenvalue_floor", max),
    ):
        value = update[key]
        if value is None:
            continue
        if target[key] is None:
            target[key] = float(value)
        else:
            target[key] = float(reducer(float(target[key]), float(value)))


def fixed_quadratic_stat(observations: np.ndarray, inverse_weight: np.ndarray) -> np.ndarray:
    mean = observations.mean(axis=0)
    return observations.shape[0] * np.einsum("bi,ij,bj->b", mean, inverse_weight, mean)


def stacked_quadratic_stat(observations: np.ndarray, inverse_weight: np.ndarray) -> np.ndarray:
    mean = observations.mean(axis=0)
    return observations.shape[0] * np.einsum("bi,bij,bj->b", mean, inverse_weight, mean)


def fixed_quadratic_from_mean(mean: np.ndarray, inverse_weight: np.ndarray, sample_size: int) -> np.ndarray:
    return sample_size * np.einsum("bi,ij,bj->b", mean, inverse_weight, mean)


def stacked_quadratic_from_mean(mean: np.ndarray, inverse_weight: np.ndarray, sample_size: int) -> np.ndarray:
    return sample_size * np.einsum("bi,bij,bj->b", mean, inverse_weight, mean)


def raw_second_moment_matrix(residuals: np.ndarray) -> np.ndarray:
    return residuals.T @ residuals / residuals.shape[0]


def sample_raw_moments(residuals: np.ndarray, max_order: int = 4) -> np.ndarray:
    u1 = residuals[:, 0]
    u2 = residuals[:, 1]
    powers_1 = [np.ones_like(u1)]
    powers_2 = [np.ones_like(u2)]
    for power in range(1, max_order + 1):
        powers_1.append(powers_1[-1] * u1)
        powers_2.append(powers_2[-1] * u2)
    moments = np.zeros((max_order + 1, max_order + 1), dtype=float)
    for p in range(max_order + 1):
        for q in range(max_order + 1 - p):
            moments[p, q] = float(np.mean(powers_1[p] * powers_2[q]))
    return moments


def linear_product_mean(
    moments: np.ndarray,
    a: np.ndarray,
    b: np.ndarray,
    c: np.ndarray,
    d: np.ndarray,
    power_1: int,
    power_2: int,
) -> np.ndarray:
    result = np.zeros_like(a, dtype=float)
    for i in range(power_1 + 1):
        coef_1 = math.comb(power_1, i) * (a**i) * (b ** (power_1 - i))
        for j in range(power_2 + 1):
            coef_2 = math.comb(power_2, j) * (c**j) * (d ** (power_2 - j))
            u1_power = i + j
            u2_power = (power_1 - i) + (power_2 - j)
            result = result + coef_1 * coef_2 * moments[u1_power, u2_power]
    return result


def inverse_arrays(
    b11: np.ndarray,
    b12: np.ndarray,
    b21: np.ndarray,
    b22: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    _det, inv11, inv12, inv21, inv22 = fig.inverse_elements(b11, b12, b21, b22)
    return inv11, inv12, inv21, inv22


def standard_moment_means_from_raw(
    moments: np.ndarray,
    b11: np.ndarray,
    b12: np.ndarray,
    b21: np.ndarray,
    b22: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    inv11, inv12, inv21, inv22 = inverse_arrays(b11, b12, b21, b22)
    e20 = linear_product_mean(moments, inv11, inv12, inv21, inv22, 2, 0)
    e11 = linear_product_mean(moments, inv11, inv12, inv21, inv22, 1, 1)
    e02 = linear_product_mean(moments, inv11, inv12, inv21, inv22, 0, 2)
    second = np.stack([e20 - 1.0, e11, e02 - 1.0], axis=1)
    higher = np.stack(
        [
            linear_product_mean(moments, inv11, inv12, inv21, inv22, 2, 1),
            linear_product_mean(moments, inv11, inv12, inv21, inv22, 1, 2),
            linear_product_mean(moments, inv11, inv12, inv21, inv22, 3, 1),
            linear_product_mean(moments, inv11, inv12, inv21, inv22, 2, 2) - 1.0,
            linear_product_mean(moments, inv11, inv12, inv21, inv22, 1, 3),
        ],
        axis=1,
    )
    return second, higher


def robust_moment_means_from_raw(
    moments: np.ndarray,
    b11: np.ndarray,
    b12: np.ndarray,
    b21: np.ndarray,
    b22: np.ndarray,
    lambda_pairs: np.ndarray,
) -> np.ndarray:
    batch = b11.size
    pair_count = lambda_pairs.shape[0]
    b11_r = np.repeat(b11, pair_count)
    b12_r = np.repeat(b12, pair_count)
    b21_r = np.repeat(b21, pair_count)
    b22_r = np.repeat(b22, pair_count)
    lambda_1 = np.tile(lambda_pairs[:, 0], batch)
    lambda_2 = np.tile(lambda_pairs[:, 1], batch)

    signal_11 = b11_r * b11_r + b12_r * b12_r
    signal_12 = b11_r * b21_r + b12_r * b22_r
    signal_22 = b21_r * b21_r + b22_r * b22_r
    nu1 = signal_11 * lambda_1
    nu2 = signal_22 * lambda_2

    inv11, inv12, inv21, inv22 = inverse_arrays(b11_r, b12_r, b21_r, b22_r)
    omega11 = 1.0 + inv11 * inv11 * nu1 + inv12 * inv12 * nu2
    omega12 = inv11 * inv21 * nu1 + inv12 * inv22 * nu2
    omega22 = 1.0 + inv21 * inv21 * nu1 + inv22 * inv22 * nu2

    return np.stack(
        [
            moments[2, 0] - (signal_11 + nu1),
            moments[1, 1] - signal_12,
            moments[0, 2] - (signal_22 + nu2),
            linear_product_mean(moments, inv11, inv12, inv21, inv22, 2, 1),
            linear_product_mean(moments, inv11, inv12, inv21, inv22, 1, 2),
            linear_product_mean(moments, inv11, inv12, inv21, inv22, 3, 1) - 3.0 * omega11 * omega12,
            linear_product_mean(moments, inv11, inv12, inv21, inv22, 2, 2)
            - omega11 * omega22
            - 2.0 * omega12 * omega12,
            linear_product_mean(moments, inv11, inv12, inv21, inv22, 1, 3) - 3.0 * omega22 * omega12,
        ],
        axis=1,
    )


def rough_covariance_prefilter_raw(
    residuals: np.ndarray,
    b11: np.ndarray,
    b12: np.ndarray,
    b21: np.ndarray,
    b22: np.ndarray,
    tolerance: float = 0.65,
) -> np.ndarray:
    covariance = raw_second_moment_matrix(residuals)
    signal_11 = b11 * b11 + b12 * b12
    signal_12 = b11 * b21 + b12 * b22
    signal_22 = b21 * b21 + b22 * b22
    lower_11 = signal_11
    upper_11 = (1.0 + fig.RELATIVE_NOISE_RATIO) * signal_11
    lower_22 = signal_22
    upper_22 = (1.0 + fig.RELATIVE_NOISE_RATIO) * signal_22
    feasible_11 = (covariance[0, 0] >= lower_11 - tolerance) & (covariance[0, 0] <= upper_11 + tolerance)
    feasible_22 = (covariance[1, 1] >= lower_22 - tolerance) & (covariance[1, 1] <= upper_22 + tolerance)
    feasible_12 = np.abs(covariance[0, 1] - signal_12) <= tolerance
    return feasible_11 & feasible_22 & feasible_12


def mask_metrics(mask: np.ndarray) -> dict[str, Any]:
    return {
        "accepted_count": int(np.count_nonzero(mask)),
        "accepted_share": fig.mask_share(mask),
        "empty": not bool(mask.any()),
    }


def evaluate_standard_projection_clean(
    residuals: np.ndarray,
    grid: fig.CandidateGrid,
    spec: fig.GridSpec,
    second_weight: m77.WeightBundle,
    dw_weight: m77.WeightBundle,
) -> dict[str, Any]:
    shape = (grid.b21_values.size, grid.b11_values.size)
    sign_mask = np.zeros(shape, dtype=bool)
    standard_mask = np.zeros(shape, dtype=bool)
    best_second = np.full(shape, np.nan)
    best_standard = np.full(shape, np.nan)
    moments = sample_raw_moments(residuals)

    for start in range(0, grid.b11.size, spec.standard_batch_size):
        end = min(start + spec.standard_batch_size, grid.b11.size)
        second_mean, higher_mean = standard_moment_means_from_raw(
            moments,
            grid.b11[start:end],
            grid.b12[start:end],
            grid.b21[start:end],
            grid.b22[start:end],
        )
        second_j = fixed_quadratic_from_mean(second_mean, second_weight.inverse, residuals.shape[0])
        standard_j = fixed_quadratic_from_mean(higher_mean, dw_weight.inverse, residuals.shape[0])
        sign_accept = second_j <= fig.CHI2_90_DF3
        standard_accept = sign_accept & (standard_j <= fig.CHI2_90_DF5)
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
    }


def evaluate_robust_projection_clean(
    residuals: np.ndarray,
    grid: fig.CandidateGrid,
    spec: fig.GridSpec,
    cache: RobustWeightCache,
) -> dict[str, Any]:
    shape = (grid.b21_values.size, grid.b11_values.size)
    robust_mask = np.zeros(shape, dtype=bool)
    best_robust = np.full(shape, np.nan)
    best_lambda_1 = np.full(shape, np.nan)
    best_lambda_2 = np.full(shape, np.nan)
    pair_count = cache.lambda_pairs.shape[0]
    moments = sample_raw_moments(residuals)

    prefilter = rough_covariance_prefilter_raw(residuals, grid.b11, grid.b12, grid.b21, grid.b22)
    candidate_indices = np.flatnonzero(prefilter)
    for start in range(0, candidate_indices.size, spec.robust_batch_size):
        selected = candidate_indices[start : start + spec.robust_batch_size]
        b11 = grid.b11[selected]
        b12 = grid.b12[selected]
        b21 = grid.b21[selected]
        b22 = grid.b22[selected]
        mean = robust_moment_means_from_raw(moments, b11, b12, b21, b22, cache.lambda_pairs)
        inverse = cache.get(selected)
        robust_j = stacked_quadratic_from_mean(mean, inverse, residuals.shape[0]).reshape(selected.size, pair_count)
        lambda_min_index = np.nanargmin(robust_j, axis=1)
        min_j = robust_j[np.arange(selected.size), lambda_min_index]
        rows = grid.b21_index[selected]
        cols = grid.b11_index[selected]
        for local, (row, col) in enumerate(zip(rows, cols)):
            value = float(min_j[local])
            if not np.isfinite(best_robust[row, col]) or value < best_robust[row, col]:
                best_robust[row, col] = value
                pair = cache.lambda_pairs[int(lambda_min_index[local])]
                best_lambda_1[row, col] = float(pair[0])
                best_lambda_2[row, col] = float(pair[1])
            if value <= fig.CHI2_90_DF8:
                robust_mask[row, col] = True

    return {
        "robust_mask": robust_mask,
        "best_robust": best_robust,
        "best_lambda_1": best_lambda_1,
        "best_lambda_2": best_lambda_2,
        "prefilter_count": int(candidate_indices.size),
    }


def standard_truth_j_clean(
    residuals: np.ndarray,
    second_weight: m77.WeightBundle,
    dw_weight: m77.WeightBundle,
) -> tuple[float, float]:
    moments = sample_raw_moments(residuals)
    second_mean, higher_mean = standard_moment_means_from_raw(
        moments,
        np.array([fig.TRUE_B11]),
        np.array([fig.TRUE_B12]),
        np.array([fig.TRUE_B21]),
        np.array([fig.TRUE_B22]),
    )
    second_j = float(fixed_quadratic_from_mean(second_mean, second_weight.inverse, residuals.shape[0])[0])
    standard_j = float(fixed_quadratic_from_mean(higher_mean, dw_weight.inverse, residuals.shape[0])[0])
    return second_j, standard_j


def robust_truth_j_clean(residuals: np.ndarray, noise: tuple[float, float]) -> tuple[float, tuple[float, float]]:
    lambda_pair = m77.true_lambda(noise)
    moments = sample_raw_moments(residuals)
    mean = robust_moment_means_from_raw(
        moments,
        np.array([fig.TRUE_B11]),
        np.array([fig.TRUE_B12]),
        np.array([fig.TRUE_B21]),
        np.array([fig.TRUE_B22]),
        np.array(lambda_pair, dtype=float)[None, :],
    )
    inverse, _stats, _max_abs_mean = robust_inverse_weight_stack(
        np.array([fig.TRUE_B11]),
        np.array([fig.TRUE_B12]),
        np.array([fig.TRUE_B21]),
        np.array([fig.TRUE_B22]),
        np.array([lambda_pair[0]]),
        np.array([lambda_pair[1]]),
    )
    robust_j = float(stacked_quadratic_from_mean(mean, inverse, residuals.shape[0])[0])
    return robust_j, lambda_pair


def evaluate_one(
    scenario: m69.MCScenario,
    seed: int,
    grid: fig.CandidateGrid,
    spec: fig.GridSpec,
    second_weight: m77.WeightBundle,
    dw_weight: m77.WeightBundle,
    cache: RobustWeightCache,
) -> dict[str, Any]:
    if abs(scenario.non_gaussian_weight - 1.0) > 1e-12:
        raise ValueError("M78 sample-size MC currently supports strong non-Gaussianity only")
    residuals = m77.cleaned_residuals(
        scenario.noise,
        scenario.sample_size,
        seed,
        scenario.residual_noise,
    )
    standard = evaluate_standard_projection_clean(residuals, grid, spec, second_weight, dw_weight)
    robust = evaluate_robust_projection_clean(residuals, grid, spec, cache)
    second_truth, standard_truth = standard_truth_j_clean(residuals, second_weight, dw_weight)
    robust_truth, true_lambda = robust_truth_j_clean(residuals, scenario.noise)

    sign_mask = standard["sign_mask"]
    standard_mask = standard["standard_mask"]
    robust_mask = robust["robust_mask"]
    intersection = standard_mask & robust_mask
    union = standard_mask | robust_mask
    standard_count = int(np.count_nonzero(standard_mask))
    intersection_count = int(np.count_nonzero(intersection))
    union_count = int(np.count_nonzero(union))
    standard_contained = intersection_count / standard_count if standard_count else None

    sign_truth_in = bool(second_truth <= fig.CHI2_90_DF3)
    standard_truth_in = bool(sign_truth_in and standard_truth <= fig.CHI2_90_DF5)
    robust_truth_in = bool(
        true_lambda[0] <= fig.RELATIVE_NOISE_RATIO
        and true_lambda[1] <= fig.RELATIVE_NOISE_RATIO
        and robust_truth <= fig.CHI2_90_DF8
    )
    return {
        "seed": int(seed),
        "sign": {
            **mask_metrics(sign_mask),
            "truth_in": sign_truth_in,
            "truth_second_j": float(second_truth),
            "distance_to_truth_projection": fig.truth_distance(sign_mask, grid),
        },
        "standard_dw": {
            **mask_metrics(standard_mask),
            "truth_in": standard_truth_in,
            "truth_second_j": float(second_truth),
            "truth_higher_j": float(standard_truth),
            "distance_to_truth_projection": fig.truth_distance(standard_mask, grid),
        },
        "robust_dw": {
            **mask_metrics(robust_mask),
            "truth_in": robust_truth_in,
            "truth_j": float(robust_truth),
            "true_lambda": [float(true_lambda[0]), float(true_lambda[1])],
            "distance_to_truth_projection": fig.truth_distance(robust_mask, grid),
            "prefilter_count": int(robust["prefilter_count"]),
        },
        "overlap": {
            "intersection_count": intersection_count,
            "union_count": union_count,
            "jaccard": intersection_count / union_count if union_count else None,
            "d_standard_not_subset_robust": None if standard_contained is None else 1.0 - standard_contained,
        },
        "warning": bool((not standard_truth_in) and robust_truth_in),
    }


def finite_values(values: list[Any]) -> list[float]:
    finite: list[float] = []
    for value in values:
        if value is None:
            continue
        numeric = float(value)
        if math.isfinite(numeric):
            finite.append(numeric)
    return finite


def numeric_summary(values: list[Any]) -> dict[str, Any]:
    finite = finite_values(values)
    if not finite:
        return {
            "n": 0,
            "mean": None,
            "median": None,
            "se": None,
            "min": None,
            "q90": None,
            "max": None,
        }
    array = np.asarray(finite, dtype=float)
    return {
        "n": int(array.size),
        "mean": float(np.mean(array)),
        "median": float(np.median(array)),
        "se": None if array.size <= 1 else float(np.std(array, ddof=1) / math.sqrt(array.size)),
        "min": float(np.min(array)),
        "q90": float(np.quantile(array, 0.90)),
        "max": float(np.max(array)),
    }


def count_rate(values: list[Any]) -> dict[str, Any]:
    finite = finite_values(values)
    count = int(sum(1 for value in finite if value >= 0.5))
    total = int(len(finite))
    rate = count / total if total else None
    se = None if not total else float(math.sqrt(rate * (1.0 - rate) / total))
    return {"count": count, "total": total, "rate": rate, "se": se}


def summarize(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for scenario in SAMPLE_SCENARIOS:
        subset = [record for record in records if record["scenario"] == scenario.name]
        metrics = [record["metrics"] for record in subset]
        summaries.append(
            {
                "scenario": scenario.name,
                "label": scenario.label,
                "reps": len(subset),
                "noise": list(scenario.noise),
                "non_gaussian_weight": scenario.non_gaussian_weight,
                "sample_size": scenario.sample_size,
                "residual_noise": scenario.residual_noise,
                "truth_inclusion": {
                    "sign": count_rate([m["sign"]["truth_in"] for m in metrics]),
                    "standard_dw": count_rate([m["standard_dw"]["truth_in"] for m in metrics]),
                    "robust_dw": count_rate([m["robust_dw"]["truth_in"] for m in metrics]),
                },
                "warning": count_rate([m["warning"] for m in metrics]),
                "size": {
                    "measure": "accepted projection share on the displayed (B11,B21) grid",
                    "sign": numeric_summary([m["sign"]["accepted_share"] for m in metrics]),
                    "standard_dw": numeric_summary([m["standard_dw"]["accepted_share"] for m in metrics]),
                    "robust_dw": numeric_summary([m["robust_dw"]["accepted_share"] for m in metrics]),
                },
                "empty": {
                    "sign": count_rate([m["sign"]["empty"] for m in metrics]),
                    "standard_dw": count_rate([m["standard_dw"]["empty"] for m in metrics]),
                    "robust_dw": count_rate([m["robust_dw"]["empty"] for m in metrics]),
                },
                "truth_j": {
                    "sign_second": numeric_summary([m["sign"]["truth_second_j"] for m in metrics]),
                    "standard_higher": numeric_summary([m["standard_dw"]["truth_higher_j"] for m in metrics]),
                    "robust_full": numeric_summary([m["robust_dw"]["truth_j"] for m in metrics]),
                },
                "overlap": {
                    "jaccard": numeric_summary([m["overlap"]["jaccard"] for m in metrics]),
                    "d_standard_not_subset_robust": numeric_summary(
                        [m["overlap"]["d_standard_not_subset_robust"] for m in metrics]
                    ),
                },
                "distance_to_truth_projection": {
                    "sign": numeric_summary([m["sign"]["distance_to_truth_projection"] for m in metrics]),
                    "standard_dw": numeric_summary(
                        [m["standard_dw"]["distance_to_truth_projection"] for m in metrics]
                    ),
                    "robust_dw": numeric_summary(
                        [m["robust_dw"]["distance_to_truth_projection"] for m in metrics]
                    ),
                },
                "prefilter_count": numeric_summary([m["robust_dw"]["prefilter_count"] for m in metrics]),
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
    return f"{fmt(item['rate'])} ({item['count']}/{item['total']})"


def fmt_mean_median(item: dict[str, Any]) -> str:
    return f"{fmt(item['mean'])} ({fmt(item['median'])})"


def weight_metadata(bundle: m77.WeightBundle) -> dict[str, Any]:
    return {
        "eigenvalues": bundle.eigenvalues,
        "condition_number": float(max(bundle.eigenvalues) / min(bundle.eigenvalues)),
        "max_abs_moment_mean": float(max(abs(value) for value in bundle.moment_means)),
        "regularization": bundle.regularization,
    }


def write_progress(progress_output: Path | None, payload: dict[str, Any]) -> None:
    if progress_output is None:
        return
    progress_output.parent.mkdir(parents=True, exist_ok=True)
    temp_path = progress_output.with_suffix(progress_output.suffix + ".tmp")
    temp_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    temp_path.replace(progress_output)


def append_progress_log(progress_log_output: Path | None, line: str) -> None:
    if progress_log_output is None:
        return
    progress_log_output.parent.mkdir(parents=True, exist_ok=True)
    with progress_log_output.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line.rstrip() + "\n")


def emit_progress(line: str, progress_log_output: Path | None) -> None:
    append_progress_log(progress_log_output, line)
    stream = getattr(sys, "stdout", None)
    if stream is not None:
        print(line, flush=True)


def write_outputs(
    records: list[dict[str, Any]],
    summaries: list[dict[str, Any]],
    spec: fig.GridSpec,
    reps: int,
    second_weight: m77.WeightBundle,
    dw_weight: m77.WeightBundle,
    robust_cache: RobustWeightCache,
    json_output: Path,
    note_output: Path,
    quick: bool,
) -> None:
    payload = {
        "schema_version": 1,
        "task": "M78 clean iid full sample-size MC",
        "description": "Full-grid sample-size MC using population-normalized iid shocks/noise and analytic iid GMM weights W=(E[f_t f_t'])^{-1}.",
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
            "dgp": "population-normalized iid chi-square structural shocks and iid Gaussian residual noise; no sample standardization; no residual or recovered-shock demeaning",
            "structural_shock": f"(chi2_{fig.STRUCTURAL_CHI2_DF:g} - {fig.STRUCTURAL_CHI2_DF:g}) / sqrt(2*{fig.STRUCTURAL_CHI2_DF:g})",
            "set_size_measure": "accepted projection share on the displayed (B11,B21) grid",
            "weighting": {
                "sign": "analytic no-noise second-moment W=(E[f_S f_S'])^{-1}",
                "standard_dw": "analytic no-noise higher-moment W=(E[f_DW f_DW'])^{-1}, combined with the sign screen",
                "robust_dw": "candidate-specific analytic iid W(B,lambda)=(E[f_t(B,lambda)f_t(B,lambda)'])^{-1}",
            },
            "weight_regularization": "symmetric covariance eigensystem with eigenvalue floor max(max_eigenvalue, 1) * 1e-10",
            "critical_values": {
                "second_moment_chi2_90_df3": fig.CHI2_90_DF3,
                "standard_dw_chi2_90_df5": fig.CHI2_90_DF5,
                "robust_full_moment_chi2_90_df8": fig.CHI2_90_DF8,
            },
            "inference_caveat": "Pointwise chi-square diagnostics only; final projected critical values remain M65 follow-up.",
            "weights": {
                "sign_second": weight_metadata(second_weight),
                "standard_dw_higher": weight_metadata(dw_weight),
                "robust_cache": robust_cache.stats,
            },
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
                for scenario in SAMPLE_SCENARIOS
            ],
        },
        "summaries": summaries,
        "records": records,
    }
    json_output.parent.mkdir(parents=True, exist_ok=True)
    json_output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# M78 Clean IID Full Sample-Size MC",
        "",
        "Status: generated full-grid sample-size Monte Carlo output for the cleaned iid analytic-weight design.",
        "",
        "This run extends M77 from a truth-at-B0 pointwise audit to the full accepted-set table. It keeps the M74 sample-size scenarios and intermediate grid, but removes sample standardization, residual demeaning, recovered-shock demeaning, and sample-specific covariance weights.",
        "",
        "## Configuration",
        "",
        f"- Machine-readable output: `{display_path(json_output)}`.",
        f"- Quick run: `{quick}`.",
        f"- Replications per scenario: `{reps}`.",
        f"- Projection grid: `{spec.projection_points} x {spec.projection_points}` plus exact true coordinates when needed.",
        f"- Profile grid: `{spec.profile_points} x {spec.profile_points}` plus exact true profiled coordinates when needed.",
        f"- Lambda grid: `{spec.lambda_points} x {spec.lambda_points}` plus true lambda values.",
        "- Structural shocks: population-normalized iid chi-square.",
        "- Residual noise: iid Gaussian.",
        "- No sample standardization, no residual demeaning, no recovered-shock demeaning.",
        "- Sign screen: `B11>0`, `B22>0`, `B12<=0`; `B21` is not sign-restricted.",
        "- Sign weight: analytic no-noise three-moment weight.",
        "- DW weight: analytic no-noise five-moment weight, after the sign screen.",
        "- nrDW weight: candidate-specific analytic iid eight-moment weight.",
        "",
        "## Sample-Size Table",
        "",
        "| T | Sign truth | DW truth | nrDW truth | Sign size | DW size | nrDW size | Sign empty | DW empty | nrDW empty | Warning |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in summaries:
        lines.append(
            "| {label} | {sign_truth} | {dw_truth} | {rdw_truth} | {sign_size} | {dw_size} | {rdw_size} | {sign_empty} | {dw_empty} | {rdw_empty} | {warning} |".format(
                label=item["label"].replace("T=", ""),
                sign_truth=fmt_rate(item["truth_inclusion"]["sign"]),
                dw_truth=fmt_rate(item["truth_inclusion"]["standard_dw"]),
                rdw_truth=fmt_rate(item["truth_inclusion"]["robust_dw"]),
                sign_size=fmt_mean_median(item["size"]["sign"]),
                dw_size=fmt_mean_median(item["size"]["standard_dw"]),
                rdw_size=fmt_mean_median(item["size"]["robust_dw"]),
                sign_empty=fmt_rate(item["empty"]["sign"]),
                dw_empty=fmt_rate(item["empty"]["standard_dw"]),
                rdw_empty=fmt_rate(item["empty"]["robust_dw"]),
                warning=fmt_rate(item["warning"]),
            )
        )
    lines.extend(
        [
            "",
            "## Truth-Statistic Quantiles",
            "",
            "| T | Sign J q90 | DW J q90 | nrDW J q90 | nrDW prefilter mean |",
            "|---:|---:|---:|---:|---:|",
        ]
    )
    for item in summaries:
        lines.append(
            "| {label} | {sign_j} | {dw_j} | {rdw_j} | {prefilter} |".format(
                label=item["label"].replace("T=", ""),
                sign_j=fmt(item["truth_j"]["sign_second"]["q90"]),
                dw_j=fmt(item["truth_j"]["standard_higher"]["q90"]),
                rdw_j=fmt(item["truth_j"]["robust_full"]["q90"]),
                prefilter=fmt(item["prefilter_count"]["mean"], 1),
            )
        )
    lines.extend(
        [
            "",
            "## Weight Diagnostics",
            "",
            "| Weight | Detail | Value |",
            "|---|---|---:|",
            f"| Sign | condition number | {weight_metadata(second_weight)['condition_number']:.6g} |",
            f"| DW | condition number | {weight_metadata(dw_weight)['condition_number']:.6g} |",
            f"| nrDW cache | computed B candidates | {robust_cache.stats['computed_b_candidates']} |",
            f"| nrDW cache | computed candidate-lambda pairs | {robust_cache.stats['computed_candidate_lambda_pairs']} |",
            f"| nrDW cache | max absolute analytic moment mean | {robust_cache.stats['max_abs_moment_mean']:.3g} |",
            f"| nrDW cache | regularized matrices | {robust_cache.stats['regularization']['regularized_matrix_count']} |",
            "",
            "## Claim Audit",
            "",
            "| Claim | Status | Evidence | Confidence | Action |",
            "|---|---|---|---|---|",
            "| The cleaned full MC uses population-normalized iid shocks/noise and no demeaning. | `code-implemented`, `user-decision` | This script and JSON configuration. | high | promote |",
            "| The nrDW full-grid statistic uses candidate-specific analytic W(B,lambda). | `code-implemented`, `derived`, `user-decision` | Vectorized polynomial weight computation in this script. | high | promote as M78 design |",
            "| Sign and DW use analytic no-noise weights for their own moment stacks. | `code-implemented`, `derived` | M77 standard weight functions reused here. | high | promote |",
            "| M78 replaces M77 as a full-grid table. | `conjectural` | M77 is pointwise only; M78 is full-grid, but M77 remains the clean size audit. | high | revise: M78 replaces M74 for full-grid cleaned design and complements M77 |",
            "| Pointwise chi-square cutoffs are final projected confidence-set critical values. | `conjectural` | M65 remains open. | medium | quarantine |",
            "",
        ]
    )
    note_output.parent.mkdir(parents=True, exist_ok=True)
    note_output.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def run(
    json_output: Path = JSON_OUTPUT,
    note_output: Path = NOTE_OUTPUT,
    reps: int = 500,
    spec: fig.GridSpec = fig.GridSpec(projection_points=27, profile_points=7, lambda_points=5, robust_batch_size=36),
    quick: bool = False,
    progress_output: Path | None = None,
    progress_log_output: Path | None = None,
) -> Path:
    grid = fig.make_candidate_grid(spec)
    lambda_1, lambda_2 = fig.lambda_grid_for_noise((0.2, 0.2), spec)
    lambda_pairs = np.array(np.meshgrid(lambda_1, lambda_2, indexing="ij")).reshape(2, -1).T
    robust_cache = RobustWeightCache.create(grid, lambda_pairs)
    second_weight = m77.standard_second_weight()
    dw_weight = m77.standard_dw_weight()

    records: list[dict[str, Any]] = []
    total = len(SAMPLE_SCENARIOS) * reps
    completed = 0
    started = time.perf_counter()

    def publish_progress(
        status: str,
        scenario: m69.MCScenario | None = None,
        rep: int | None = None,
        seed: int | None = None,
        metrics: dict[str, Any] | None = None,
    ) -> None:
        elapsed = time.perf_counter() - started
        average = elapsed / completed if completed else None
        eta = average * (total - completed) if average is not None else None
        latest = None
        if metrics is not None:
            latest = {
                "sign_share": metrics["sign"]["accepted_share"],
                "standard_share": metrics["standard_dw"]["accepted_share"],
                "robust_share": metrics["robust_dw"]["accepted_share"],
                "sign_truth_in": metrics["sign"]["truth_in"],
                "standard_truth_in": metrics["standard_dw"]["truth_in"],
                "robust_truth_in": metrics["robust_dw"]["truth_in"],
                "robust_prefilter_count": metrics["robust_dw"]["prefilter_count"],
            }
        payload = {
            "schema_version": 1,
            "status": status,
            "updated_at": now_iso(),
            "pid": os.getpid(),
            "completed": completed,
            "total": total,
            "remaining": total - completed,
            "elapsed_seconds": elapsed,
            "average_seconds_per_rep": average,
            "eta_seconds": eta,
            "grid": {
                "projection_points": spec.projection_points,
                "profile_points": spec.profile_points,
                "lambda_points": spec.lambda_points,
            },
            "reps_per_scenario": reps,
            "current": None
            if scenario is None
            else {
                "scenario": scenario.name,
                "label": scenario.label,
                "sample_size": scenario.sample_size,
                "rep": rep,
                "seed": seed,
            },
            "latest_metrics": latest,
            "robust_weight_cache": robust_cache.stats,
            "outputs": {
                "json": display_path(json_output),
                "note": display_path(note_output),
            },
        }
        write_progress(progress_output, payload)
        if status == "completed":
            emit_progress(f"[progress] completed {completed}/{total} reps in {elapsed:.1f}s", progress_log_output)
        elif scenario is not None and rep is not None:
            eta_text = "n/a" if eta is None else f"{eta / 3600:.2f}h"
            emit_progress(
                f"[progress] {completed}/{total} scenario={scenario.name} "
                f"rep={rep + 1}/{reps} elapsed={elapsed / 3600:.2f}h eta={eta_text}",
                progress_log_output,
            )
        else:
            emit_progress(f"[progress] started total={total}", progress_log_output)

    publish_progress("running")
    for scenario_index, scenario in enumerate(SAMPLE_SCENARIOS):
        for rep in range(reps):
            seed = m69.seed_for(fig.RANDOM_SEED, 2, scenario_index, rep)
            metrics = evaluate_one(scenario, seed, grid, spec, second_weight, dw_weight, robust_cache)
            completed += 1
            records.append(
                {
                    "scenario": scenario.name,
                    "label": scenario.label,
                    "rep": rep,
                    "seed": seed,
                    "metrics": metrics,
                }
            )
            publish_progress("running", scenario, rep, seed, metrics)
    summaries = summarize(records)
    write_outputs(records, summaries, spec, reps, second_weight, dw_weight, robust_cache, json_output, note_output, quick)
    publish_progress("completed")
    return note_output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-output", default="", help="Optional JSON output path.")
    parser.add_argument("--note-output", default="", help="Optional Markdown note output path.")
    parser.add_argument("--evaluation-reps", type=int, default=500)
    parser.add_argument("--projection-points", type=int, default=27)
    parser.add_argument("--profile-points", type=int, default=7)
    parser.add_argument("--lambda-points", type=int, default=5)
    parser.add_argument("--robust-batch-size", type=int, default=36)
    parser.add_argument("--standard-batch-size", type=int, default=240)
    parser.add_argument("--progress-output", default="", help="Optional JSON progress file updated after each replication.")
    parser.add_argument("--progress-log-output", default="", help="Optional text progress log appended after each replication.")
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Use a small smoke-test grid and limit replications.",
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
    progress_output = Path(args.progress_output) if args.progress_output else None
    progress_log_output = Path(args.progress_log_output) if args.progress_log_output else None
    try:
        path = run(
            json_output=Path(args.json_output) if args.json_output else JSON_OUTPUT,
            note_output=Path(args.note_output) if args.note_output else NOTE_OUTPUT,
            reps=reps,
            spec=spec,
            quick=args.quick,
            progress_output=progress_output,
            progress_log_output=progress_log_output,
        )
    except Exception:
        error = traceback.format_exc()
        write_progress(
            progress_output,
            {
                "schema_version": 1,
                "status": "failed",
                "updated_at": now_iso(),
                "pid": os.getpid(),
                "error": error,
            },
        )
        append_progress_log(progress_log_output, "[progress] failed")
        append_progress_log(progress_log_output, error)
        raise
    print(f"Wrote {display_path(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
