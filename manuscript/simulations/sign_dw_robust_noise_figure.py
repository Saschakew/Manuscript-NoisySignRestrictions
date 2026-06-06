"""Replicate the sign/DW noise visualization and add robust DW.

This is a deterministic population figure adapted from the KnowledgeVault
visualization lab:

  C:/Users/smsakewe/Documents/GitHub/KnowledgeVault/
  replications/svar-noise-recursive-sign-visualization/noisy_svar_visuals.py

The standard-DW panels use the recursive bivariate calibration from the vault
note. The robust-DW panel uses the same normalized shape and Gaussian residual
noise, because the current robust route is a Gaussian-noise higher-cumulant
construction that deliberately drops second moments as structural restrictions.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from matplotlib.lines import Line2D


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "manuscript" / "figures"
OUTPUT_PATH = OUTPUT_DIR / "fig_sign_dw_robust_noise_comparison.png"

BETA = 0.7
TRUE_A = 0.0
TRUE_B = BETA
SKEWNESS = np.array([2.0, 2.0, 0.0, 0.0])
EXCESS_KURTOSIS = np.array([6.0, 6.0, 0.0, 0.0])
STANDARD_DW_TOLERANCE = 0.01
ROBUST_DW_TOLERANCE = 0.01


def recursive_cholesky(nu1: float, nu2: float) -> np.ndarray:
    return np.array(
        [
            [math.sqrt(1.0 + nu1), 0.0],
            [
                BETA / math.sqrt(1.0 + nu1),
                math.sqrt(1.0 + nu2 + BETA * BETA * nu1 / (1.0 + nu1)),
            ],
        ],
        dtype=float,
    )


def rotation(theta: float) -> np.ndarray:
    c = math.cos(theta)
    s = math.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=float)


def rotation_column(theta: float) -> np.ndarray:
    return np.array([math.cos(theta), math.sin(theta)], dtype=float)


def primitive_mixing(nu1: float, nu2: float) -> np.ndarray:
    return np.array(
        [
            [1.0, 0.0, math.sqrt(nu1), 0.0],
            [BETA, 1.0, 0.0, math.sqrt(nu2)],
        ],
        dtype=float,
    )


def sign_response(theta: float, nu1: float, nu2: float) -> float:
    return float((recursive_cholesky(nu1, nu2) @ rotation_column(theta))[1])


def sign_ok(theta: float, nu1: float, nu2: float) -> bool:
    return sign_response(theta, nu1, nu2) >= 0.0


def boundary_angle(nu1: float, nu2: float) -> float:
    denominator = math.sqrt((1.0 + nu1) * (1.0 + nu2) + BETA * BETA * nu1)
    return -math.atan(BETA / denominator)


def recovered_primitive_loadings(theta: float, nu1: float, nu2: float) -> np.ndarray:
    return (
        rotation(theta).T
        @ np.linalg.inv(recursive_cholesky(nu1, nu2))
        @ primitive_mixing(nu1, nu2)
    )


def standard_dw_moments(theta: float, nu1: float, nu2: float) -> np.ndarray:
    loadings = recovered_primitive_loadings(theta, nu1, nu2)
    first = loadings[0]
    second = loadings[1]
    return np.array(
        [
            np.sum(SKEWNESS * first * first * second),
            np.sum(SKEWNESS * first * second * second),
            np.sum(EXCESS_KURTOSIS * first * first * second * second),
        ],
        dtype=float,
    )


def standard_dw_score(theta: float, nu1: float, nu2: float) -> float:
    moments = standard_dw_moments(theta, nu1, nu2)
    return float(moments @ moments)


def robust_dw_score(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Higher-cumulant score for B(a,b)^{-1}B0 epsilon.

    Gaussian residual noise is intentionally absent from this score because its
    cumulants above order two are zero after every linear transformation.
    """
    determinant = 1.0 - a * b
    valid = np.abs(determinant) > 1e-8
    alpha = np.full_like(a, np.nan, dtype=float)
    beta = np.full_like(a, np.nan, dtype=float)
    c = np.full_like(a, np.nan, dtype=float)
    d = np.full_like(a, np.nan, dtype=float)
    alpha[valid] = (1.0 - a[valid] * TRUE_B) / determinant[valid]
    beta[valid] = (TRUE_A - a[valid]) / determinant[valid]
    c[valid] = (TRUE_B - b[valid]) / determinant[valid]
    d[valid] = (1.0 - b[valid] * TRUE_A) / determinant[valid]

    gamma1 = gamma2 = 2.0
    kappa1 = kappa2 = 6.0
    c112 = alpha * alpha * c * gamma1 + beta * beta * d * gamma2
    c122 = alpha * c * c * gamma1 + beta * d * d * gamma2
    c1112 = alpha**3 * c * kappa1 + beta**3 * d * kappa2
    c1122 = alpha * alpha * c * c * kappa1 + beta * beta * d * d * kappa2
    c1222 = alpha * c**3 * kappa1 + beta * d**3 * kappa2

    scaled = np.stack(
        [c112 / 2.0, c122 / 2.0, c1112 / 6.0, c1122 / 6.0, c1222 / 6.0],
        axis=0,
    )
    return np.sum(scaled * scaled, axis=0)


def build_standard_panels(theta_grid: np.ndarray, nu_grid_heat: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    score = np.full((nu_grid_heat.size, theta_grid.size), np.nan)
    sign_mask = np.zeros_like(score, dtype=bool)
    for i, nu1 in enumerate(nu_grid_heat):
        for j, theta in enumerate(theta_grid):
            if sign_ok(float(theta), float(nu1), 0.0):
                sign_mask[i, j] = True
                score[i, j] = standard_dw_score(float(theta), float(nu1), 0.0)
    accepted = np.isfinite(score) & (score <= STANDARD_DW_TOLERANCE)
    return score, accepted


def standard_widths(theta_grid: np.ndarray, nu_grid: np.ndarray) -> tuple[list[float], list[float], list[float]]:
    sign_width = []
    dw_width = []
    min_score = []
    for nu1 in nu_grid:
        sign_angles = np.array([theta for theta in theta_grid if sign_ok(float(theta), float(nu1), 0.0)])
        if sign_angles.size:
            sign_width.append(float(np.degrees(sign_angles.max() - sign_angles.min())))
        else:
            sign_width.append(0.0)
        scores = np.array(
            [
                standard_dw_score(float(theta), float(nu1), 0.0)
                for theta in theta_grid
                if sign_ok(float(theta), float(nu1), 0.0)
            ],
            dtype=float,
        )
        min_score.append(float(np.min(scores)) if scores.size else math.nan)
        dw_angles = np.array(
            [
                theta
                for theta in theta_grid
                if sign_ok(float(theta), float(nu1), 0.0)
                and standard_dw_score(float(theta), float(nu1), 0.0) <= STANDARD_DW_TOLERANCE
            ]
        )
        if dw_angles.size:
            dw_width.append(float(np.degrees(dw_angles.max() - dw_angles.min())))
        else:
            dw_width.append(0.0)
    return sign_width, dw_width, min_score


def plot() -> Path:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    theta_grid = np.linspace(math.radians(-80.0), math.radians(110.0), 420)
    nu_grid_heat = np.linspace(0.0, 8.0, 240)
    nu_grid_curve = np.linspace(0.0, 60.0, 300)
    score, accepted = build_standard_panels(theta_grid, nu_grid_heat)
    sign_width, dw_width, min_score = standard_widths(theta_grid, nu_grid_curve)

    a_grid = np.linspace(-0.65, 0.65, 260)
    b_grid = np.linspace(-0.10, 1.35, 260)
    a_mesh, b_mesh = np.meshgrid(a_grid, b_grid)
    robust_score = robust_dw_score(a_mesh, b_mesh)
    robust_accepted = np.isfinite(robust_score) & (b_mesh >= 0.0) & (robust_score <= ROBUST_DW_TOLERANCE)

    fig = plt.figure(figsize=(15.5, 4.9), constrained_layout=True)
    gs = fig.add_gridspec(1, 3, width_ratios=[1.28, 1.0, 1.0])

    ax = fig.add_subplot(gs[0, 0])
    im = ax.pcolormesh(
        np.degrees(theta_grid),
        nu_grid_heat,
        np.log10(np.where(np.isfinite(score), score, np.nan) + 1e-8),
        cmap="magma_r",
        shading="auto",
        vmin=-8,
        vmax=0.25,
    )
    ax.contour(
        np.degrees(theta_grid),
        nu_grid_heat,
        accepted.astype(float),
        levels=[0.5],
        colors=["#00bcd4"],
        linewidths=1.8,
    )
    boundary = [math.degrees(boundary_angle(float(nu), 0.0)) for nu in nu_grid_heat]
    ax.plot(boundary, nu_grid_heat, color="white", lw=1.5, ls="--", label="sign boundary")
    ax.set_title("Standard DW inside sign set")
    ax.set_xlabel("rotation angle theta, degrees")
    ax.set_ylabel("noise variance in first residual")
    ax.text(-76, 7.25, "blank = sign rejected", color="white")
    ax.text(18, 0.45, "cyan = DW accepted", color="#00e5ff")
    ax.legend(loc="upper right", frameon=True, framealpha=0.9, fontsize=8)
    cbar = fig.colorbar(im, ax=ax, fraction=0.045, pad=0.02)
    cbar.set_label("log10 higher-moment score")

    ax = fig.add_subplot(gs[0, 1])
    ax.plot(nu_grid_curve, sign_width, color="#4d4d4d", lw=2.1, label="sign-only angle width")
    ax.plot(nu_grid_curve, dw_width, color="#b2182b", lw=2.4, label="sign + standard DW")
    ax.set_title("Standard DW can empty and reopen")
    ax.set_xlabel("noise variance in first residual")
    ax.set_ylabel("accepted angle width, degrees")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="upper right", fontsize=8, frameon=True, framealpha=0.9)
    ax2 = ax.twinx()
    ax2.plot(nu_grid_curve, min_score, color="#2166ac", lw=1.4, ls="--", label="best DW score")
    ax2.axhline(STANDARD_DW_TOLERANCE, color="#2166ac", lw=1.0, ls=":")
    ax2.set_yscale("log")
    ax2.set_ylim(1e-5, 3.0)
    ax2.set_ylabel("best higher-moment score", color="#2166ac")
    ax2.tick_params(axis="y", labelcolor="#2166ac")

    ax = fig.add_subplot(gs[0, 2])
    ax.contourf(
        a_mesh,
        b_mesh,
        robust_accepted.astype(float),
        levels=[0.5, 1.5],
        colors=["#c7e9c0"],
        alpha=0.92,
    )
    ax.contour(
        a_mesh,
        b_mesh,
        robust_score,
        levels=[ROBUST_DW_TOLERANCE],
        colors=["#1b7837"],
        linewidths=2.0,
    )
    ax.scatter([TRUE_A], [TRUE_B], marker="*", s=155, color="#b2182b", edgecolor="white", zorder=5, label="true B0")
    ax.axhline(0.0, color="0.5", lw=1.0, ls="--", label="sign boundary b >= 0")
    ax.set_title("Robust DW ignores Gaussian noise variance")
    ax.set_xlabel("a in B(a,b)")
    ax.set_ylabel("b in B(a,b)")
    ax.set_xlim(a_grid.min(), a_grid.max())
    ax.set_ylim(b_grid.min(), b_grid.max())
    ax.grid(True, alpha=0.25)
    robust_handle = Line2D([0], [0], color="#1b7837", lw=2.0, label="robust DW accepted")
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles + [robust_handle], labels + ["robust DW accepted"], loc="upper right", fontsize=8, frameon=True, framealpha=0.9)
    ax.text(
        -0.60,
        0.05,
        "same region for all Gaussian noise levels\nbecause only higher cumulants are used",
        fontsize=8,
        color="#1b7837",
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=200)
    plt.close(fig)
    return OUTPUT_PATH


if __name__ == "__main__":
    path = plot()
    print(f"Wrote {path.relative_to(ROOT)}")
