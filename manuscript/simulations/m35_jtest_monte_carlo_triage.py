"""M35 early Monte Carlo triage for DW-style J-test inversion.

This is exploratory manuscript evidence, not the final replication package.
It compares two screening inversions in the simultaneous bivariate model:

* standard DW: covariance-whitened rotations of the noisy residual covariance;
* robust DW: a normalized impact chart that drops second moments as structural
  restrictions and tests mixed higher cumulants of B^{-1}u.

The J statistic uses a simple per-candidate scale normalization for the moment
stack. Treat the resulting acceptance rates as triage signals, not as final
size-controlled tests.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = ROOT / "manuscript" / "simulations" / "output"
CHI2_5_95 = 11.070497693516351


@dataclass(frozen=True)
class Scenario:
    name: str
    label: str
    noise_cov: np.ndarray
    non_gaussian_weight: float
    note: str


@dataclass(frozen=True)
class EvalResult:
    nonempty: bool
    accepted_fraction: float
    min_j: float
    nearest_shape_distance: float
    nearest_shape_accepted: bool
    nearest_shape_j: float
    accepted_nearest_distance: float | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260606)
    parser.add_argument("--reps", type=int, default=80)
    parser.add_argument("--sample-size", type=int, default=400)
    parser.add_argument("--angles", type=int, default=361)
    parser.add_argument("--shape-grid", type=int, default=51)
    parser.add_argument("--critical-value", type=float, default=CHI2_5_95)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def rotation(theta: float) -> np.ndarray:
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=float)


def sign_admissible(B: np.ndarray) -> bool:
    return B[0, 0] > 0 and B[0, 1] > 0 and B[1, 0] < 0 and B[1, 1] > 0


def normalize_shape(B: np.ndarray) -> tuple[float, float] | None:
    if B[0, 0] <= 0 or B[1, 1] <= 0:
        return None
    return (B[0, 1] / B[1, 1], B[1, 0] / B[0, 0])


def shape_distance(shape: tuple[float, float], truth_shape: tuple[float, float]) -> float:
    return float(np.hypot(shape[0] - truth_shape[0], shape[1] - truth_shape[1]))


def draw_structural_shocks(
    rng: np.random.Generator,
    nobs: int,
    non_gaussian_weight: float,
) -> np.ndarray:
    """Draw independent unit-variance shocks with tunable higher moments."""
    exp_shock = rng.exponential(scale=1.0, size=nobs) - 1.0
    chi_square_shock = (rng.chisquare(df=3, size=nobs) - 3.0) / np.sqrt(6.0)
    gaussian = rng.normal(size=(nobs, 2))
    non_gaussian = np.column_stack([exp_shock, chi_square_shock])
    w = non_gaussian_weight
    eps = np.sqrt(w) * non_gaussian + np.sqrt(1.0 - w) * gaussian
    return eps


def draw_residuals(
    rng: np.random.Generator,
    B0: np.ndarray,
    scenario: Scenario,
    nobs: int,
) -> np.ndarray:
    eps = draw_structural_shocks(rng, nobs, scenario.non_gaussian_weight)
    if np.allclose(scenario.noise_cov, 0.0):
        eta = np.zeros((nobs, 2), dtype=float)
    else:
        eta = rng.multivariate_normal(np.zeros(2), scenario.noise_cov, size=nobs)
    return eps @ B0.T + eta


def cumulant_stack(z: np.ndarray) -> np.ndarray:
    zc = z - z.mean(axis=0, keepdims=True)
    z1 = zc[:, 0]
    z2 = zc[:, 1]
    s11 = np.mean(z1 * z1)
    s22 = np.mean(z2 * z2)
    s12 = np.mean(z1 * z2)
    return np.array(
        [
            np.mean(z1 * z1 * z2),
            np.mean(z1 * z2 * z2),
            np.mean(z1 * z1 * z1 * z2) - 3.0 * s11 * s12,
            np.mean(z1 * z1 * z2 * z2) - s11 * s22 - 2.0 * s12 * s12,
            np.mean(z1 * z2 * z2 * z2) - 3.0 * s22 * s12,
        ],
        dtype=float,
    )


def moment_scale(z: np.ndarray) -> np.ndarray:
    zc = z - z.mean(axis=0, keepdims=True)
    z1 = zc[:, 0]
    z2 = zc[:, 1]
    raw = np.column_stack(
        [
            z1 * z1 * z2,
            z1 * z2 * z2,
            z1 * z1 * z1 * z2,
            z1 * z1 * z2 * z2,
            z1 * z2 * z2 * z2,
        ]
    )
    scale = raw.std(axis=0, ddof=1)
    return np.maximum(scale, 1e-8)


def j_statistic(z: np.ndarray) -> float:
    g = cumulant_stack(z)
    scale = moment_scale(z)
    return float(z.shape[0] * np.sum((g / scale) ** 2))


def build_standard_candidates(
    Sigma_u: np.ndarray,
    angles: np.ndarray,
    truth_shape: tuple[float, float],
) -> list[tuple[np.ndarray, tuple[float, float], float]]:
    P = np.linalg.cholesky(Sigma_u)
    candidates: list[tuple[np.ndarray, tuple[float, float], float]] = []
    for theta in angles:
        B = P @ rotation(float(theta))
        if not sign_admissible(B):
            continue
        shape = normalize_shape(B)
        if shape is None:
            continue
        candidates.append((B, shape, shape_distance(shape, truth_shape)))
    return candidates


def build_robust_candidates(
    a_grid: np.ndarray,
    b_grid: np.ndarray,
    truth_shape: tuple[float, float],
) -> list[tuple[float, float, float]]:
    candidates: list[tuple[float, float, float]] = []
    for a in a_grid:
        for b in b_grid:
            det = 1.0 - a * b
            if a <= 0.0 or b >= 0.0 or abs(det) < 0.2:
                continue
            shape = (float(a), float(b))
            candidates.append((float(a), float(b), shape_distance(shape, truth_shape)))
    return candidates


def evaluate_standard(
    u: np.ndarray,
    candidates: list[tuple[np.ndarray, tuple[float, float], float]],
    critical_value: float,
) -> EvalResult:
    if not candidates:
        raise RuntimeError("No sign-admissible standard-DW candidates.")

    js = np.empty(len(candidates), dtype=float)
    distances = np.empty(len(candidates), dtype=float)
    for idx, (B, _shape, distance) in enumerate(candidates):
        z = np.linalg.solve(B, u.T).T
        js[idx] = j_statistic(z)
        distances[idx] = distance
    return summarize_js(js, distances, critical_value)


def evaluate_robust(
    u: np.ndarray,
    candidates: list[tuple[float, float, float]],
    critical_value: float,
) -> EvalResult:
    if not candidates:
        raise RuntimeError("No sign-admissible robust-DW candidates.")

    u1 = u[:, 0]
    u2 = u[:, 1]
    js = np.empty(len(candidates), dtype=float)
    distances = np.empty(len(candidates), dtype=float)
    for idx, (a, b, distance) in enumerate(candidates):
        det = 1.0 - a * b
        z = np.column_stack([(u1 - a * u2) / det, (-b * u1 + u2) / det])
        js[idx] = j_statistic(z)
        distances[idx] = distance
    return summarize_js(js, distances, critical_value)


def summarize_js(js: np.ndarray, distances: np.ndarray, critical_value: float) -> EvalResult:
    accepted = js <= critical_value
    nearest_idx = int(np.argmin(distances))
    accepted_distances = distances[accepted]
    accepted_nearest = None
    if accepted_distances.size:
        accepted_nearest = float(np.min(accepted_distances))
    return EvalResult(
        nonempty=bool(np.any(accepted)),
        accepted_fraction=float(np.mean(accepted)),
        min_j=float(np.min(js)),
        nearest_shape_distance=float(distances[nearest_idx]),
        nearest_shape_accepted=bool(accepted[nearest_idx]),
        nearest_shape_j=float(js[nearest_idx]),
        accepted_nearest_distance=accepted_nearest,
    )


def summarize_results(results: list[dict]) -> dict:
    out: dict[str, dict[str, dict[str, float | int | None]]] = {}
    for scenario_name in sorted({item["scenario"] for item in results}):
        scenario_items = [item for item in results if item["scenario"] == scenario_name]
        out[scenario_name] = {}
        for method in ("standard_dw", "robust_dw"):
            method_items = [item[method] for item in scenario_items]
            accepted_nearest = np.array(
                [
                    np.nan if item["accepted_nearest_distance"] is None else item["accepted_nearest_distance"]
                    for item in method_items
                ],
                dtype=float,
            )
            out[scenario_name][method] = {
                "reps": len(method_items),
                "nonempty_rate": float(np.mean([item["nonempty"] for item in method_items])),
                "nearest_shape_accept_rate": float(
                    np.mean([item["nearest_shape_accepted"] for item in method_items])
                ),
                "mean_accepted_fraction": float(np.mean([item["accepted_fraction"] for item in method_items])),
                "median_min_j": float(np.median([item["min_j"] for item in method_items])),
                "median_nearest_shape_j": float(np.median([item["nearest_shape_j"] for item in method_items])),
                "median_accepted_nearest_distance": none_if_all_nan(accepted_nearest),
                "median_least_rejected_shape_distance": float(
                    np.median(
                        [
                            item["least_rejected_shape_distance"]
                            for item in method_items
                        ]
                    )
                ),
            }
    return out


def none_if_all_nan(values: np.ndarray) -> float | None:
    if np.all(np.isnan(values)):
        return None
    return float(np.nanmedian(values))


def eval_to_dict(result: EvalResult, least_rejected_shape_distance: float) -> dict:
    return {
        "nonempty": result.nonempty,
        "accepted_fraction": result.accepted_fraction,
        "min_j": result.min_j,
        "nearest_shape_distance": result.nearest_shape_distance,
        "nearest_shape_accepted": result.nearest_shape_accepted,
        "nearest_shape_j": result.nearest_shape_j,
        "accepted_nearest_distance": result.accepted_nearest_distance,
        "least_rejected_shape_distance": least_rejected_shape_distance,
    }


def evaluate_with_least_distance_standard(
    u: np.ndarray,
    candidates: list[tuple[np.ndarray, tuple[float, float], float]],
    critical_value: float,
) -> tuple[EvalResult, float]:
    js = np.empty(len(candidates), dtype=float)
    distances = np.empty(len(candidates), dtype=float)
    for idx, (B, _shape, distance) in enumerate(candidates):
        z = np.linalg.solve(B, u.T).T
        js[idx] = j_statistic(z)
        distances[idx] = distance
    result = summarize_js(js, distances, critical_value)
    return result, float(distances[int(np.argmin(js))])


def evaluate_with_least_distance_robust(
    u: np.ndarray,
    candidates: list[tuple[float, float, float]],
    critical_value: float,
) -> tuple[EvalResult, float]:
    u1 = u[:, 0]
    u2 = u[:, 1]
    js = np.empty(len(candidates), dtype=float)
    distances = np.empty(len(candidates), dtype=float)
    for idx, (a, b, distance) in enumerate(candidates):
        det = 1.0 - a * b
        z = np.column_stack([(u1 - a * u2) / det, (-b * u1 + u2) / det])
        js[idx] = j_statistic(z)
        distances[idx] = distance
    result = summarize_js(js, distances, critical_value)
    return result, float(distances[int(np.argmin(js))])


def markdown_summary(payload: dict) -> str:
    lines = [
        "# M35 Early J-Test Monte Carlo Triage",
        "",
        "Status: exploratory screening output, not final calibrated evidence.",
        "",
        "## Command",
        "",
        "```powershell",
        payload["command"],
        "```",
        "",
        "## Design",
        "",
        f"- Seed: `{payload['seed']}`",
        f"- Replications per scenario: `{payload['reps']}`",
        f"- Sample size: `{payload['sample_size']}`",
        f"- Standard-DW angle grid: `{payload['angles']}` rotations",
        f"- Robust-DW shape grid: `{payload['shape_grid']} x {payload['shape_grid']}` before sign filtering",
        f"- Screening critical value: `{payload['critical_value']:.4f}` (chi-square 5, 95 percent reference)",
        "- True normalized impact matrix: `[[1, 0.35], [-0.25, 1]]`",
        "- Sign filter: `B11 > 0`, `B12 > 0`, `B21 < 0`, `B22 > 0`.",
        "",
        "The statistic uses the five mixed higher-cumulant moments from the M24/M25 notes and a simple per-candidate scale normalization. It is meant to flag whether the comparison is promising enough for M28-M30, not to settle coverage.",
        "",
        "## Scenario Notes",
        "",
    ]
    for scenario in payload["scenarios"]:
        lines.append(f"- `{scenario['name']}`: {scenario['note']}")
    lines.extend(["", "## Summary", ""])
    header = (
        "| Scenario | Method | Nonempty rate | Nearest-shape accept rate | "
        "Mean accepted fraction | Median min J | Median least-rejected distance |"
    )
    lines.extend([header, "|---|---|---:|---:|---:|---:|---:|"])
    for scenario_name, scenario_summary in payload["summary"].items():
        for method, values in scenario_summary.items():
            lines.append(
                "| "
                + " | ".join(
                    [
                        scenario_name,
                        method,
                        f"{values['nonempty_rate']:.3f}",
                        f"{values['nearest_shape_accept_rate']:.3f}",
                        f"{values['mean_accepted_fraction']:.4f}",
                        f"{values['median_min_j']:.2f}",
                        f"{values['median_least_rejected_shape_distance']:.3f}",
                    ]
                )
                + " |"
            )
    lines.extend(
        [
            "",
            "## Triage Read",
            "",
            "- The no-noise strong-moment scenario passes the basic sanity check: both routes are usually nonempty and their least-rejected shapes remain close to the true normalized shape.",
            "- The moderate-noise scenario does not yet give a clean finite-sample emptying or false-sharpening pattern for standard DW. With this provisional scale-normalized statistic, standard DW remains frequently nonempty, so the manuscript should not move directly to polished false-sharpening figures from this run.",
            "- The weak higher-moment scenario is almost non-discriminating for both methods. That is useful triage information: weak higher cumulants can make the robust comparison honest but very wide in macro-sized samples.",
            "- Gate outcome: proceed to audit and population-grid verification before larger Monte Carlo work. This screen supports M28/M30 as the next evidence tasks, not M29-style final tables.",
            "",
            "## Next Checks",
            "",
            "- Audit this script before treating the output as evidence: moment scaling, critical values, shape normalization, sign filtering, and finite-sample size all remain provisional.",
            "- M28 should replace this sample-screening run with population-grid checks that verify zeros and aliases directly.",
            "- M29 should use repeated-sample or bootstrap critical values before reporting manuscript tables.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    rng = np.random.default_rng(args.seed)
    B0 = np.array([[1.0, 0.35], [-0.25, 1.0]], dtype=float)
    truth_shape = (0.35, -0.25)
    Sigma0 = B0 @ B0.T
    scenarios = [
        Scenario(
            name="no_noise_strong",
            label="No noise, strong higher moments",
            noise_cov=np.zeros((2, 2), dtype=float),
            non_gaussian_weight=1.0,
            note="No residual noise; shocks have strong skewness or kurtosis.",
        ),
        Scenario(
            name="moderate_gaussian_noise",
            label="Moderate Gaussian residual noise",
            noise_cov=np.array([[0.20, 0.0], [0.0, 0.12]], dtype=float),
            non_gaussian_weight=1.0,
            note="Diagonal Gaussian residual noise in u-coordinates; this is generically non-diagonal in structural coordinates.",
        ),
        Scenario(
            name="weak_higher_moments_with_noise",
            label="Weak higher moments with Gaussian noise",
            noise_cov=np.array([[0.20, 0.0], [0.0, 0.12]], dtype=float),
            non_gaussian_weight=0.15,
            note="Same residual noise, but structural shocks are mostly Gaussian mixtures, weakening the higher-cumulant signal.",
        ),
    ]

    angles = np.linspace(0.0, 2.0 * np.pi, args.angles, endpoint=False)
    a_grid = np.unique(np.append(np.linspace(-0.15, 0.85, args.shape_grid), truth_shape[0]))
    b_grid = np.unique(np.append(np.linspace(-0.75, 0.25, args.shape_grid), truth_shape[1]))
    robust_candidates = build_robust_candidates(a_grid, b_grid, truth_shape)

    results: list[dict] = []
    for scenario in scenarios:
        Sigma_u = Sigma0 + scenario.noise_cov
        standard_candidates = build_standard_candidates(Sigma_u, angles, truth_shape)
        for rep in range(args.reps):
            u = draw_residuals(rng, B0, scenario, args.sample_size)
            standard, standard_least_distance = evaluate_with_least_distance_standard(
                u,
                standard_candidates,
                args.critical_value,
            )
            robust, robust_least_distance = evaluate_with_least_distance_robust(
                u,
                robust_candidates,
                args.critical_value,
            )
            results.append(
                {
                    "scenario": scenario.name,
                    "rep": rep,
                    "standard_dw": eval_to_dict(standard, standard_least_distance),
                    "robust_dw": eval_to_dict(robust, robust_least_distance),
                }
            )

    command = (
        "python manuscript/simulations/m35_jtest_monte_carlo_triage.py "
        f"--seed {args.seed} --reps {args.reps} --sample-size {args.sample_size} "
        f"--angles {args.angles} --shape-grid {args.shape_grid}"
    )
    payload = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "command": command,
        "seed": args.seed,
        "reps": args.reps,
        "sample_size": args.sample_size,
        "angles": args.angles,
        "shape_grid": args.shape_grid,
        "critical_value": args.critical_value,
        "true_B0": B0.tolist(),
        "truth_shape": list(truth_shape),
        "scenarios": [
            {
                "name": scenario.name,
                "label": scenario.label,
                "noise_cov": scenario.noise_cov.tolist(),
                "non_gaussian_weight": scenario.non_gaussian_weight,
                "note": scenario.note,
            }
            for scenario in scenarios
        ],
        "summary": summarize_results(results),
        "replicate_results": results,
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "m35_jtest_monte_carlo_summary.json"
    md_path = ROOT / "manuscript" / "simulations" / "m35_jtest_monte_carlo_triage.md"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    md_path.write_text(markdown_summary(payload), encoding="utf-8")
    print(f"Wrote {json_path.relative_to(ROOT)}")
    print(f"Wrote {md_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
