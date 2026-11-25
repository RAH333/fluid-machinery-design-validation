"""
Mechanics of Solids Solver for Rotating Fluid Machinery Impeller Disc.
Calculates radial stress, tangential (hoop) stress, Von Mises stress,
and Goodman fatigue safety factor for Duplex Stainless Steel (SAF 2205).
"""

import numpy as np


def analyze_rotating_impeller(
    inner_radius_m: float = 0.035,
    outer_radius_m: float = 0.145,
    rpm: float = 3600.0,
    density_kg_m3: float = 7800.0,
    poissons_ratio: float = 0.30,
    yield_strength_mpa: float = 450.0,
    ultimate_strength_mpa: float = 655.0,
    endurance_limit_mpa: float = 260.0,
    pressure_fluctuation_ratio: float = 0.15,
) -> dict:
    """Computes radial stress distribution and fatigue safety factors."""
    omega = (2.0 * np.pi * rpm) / 60.0  # Angular velocity (rad/s)
    r = np.linspace(inner_radius_m, outer_radius_m, 200)

    ri2 = inner_radius_m**2
    ro2 = outer_radius_m**2
    factor = ((3.0 + poissons_ratio) / 8.0) * density_kg_m3 * (omega**2)

    # Analytical rotating annular disc stress equations (Pa -> MPa)
    sigma_r = factor * (ri2 + ro2 - (ri2 * ro2) / (r**2) - r**2) / 1e6
    sigma_theta = (
        factor
        * (
            ri2
            + ro2
            + (ri2 * ro2) / (r**2)
            - ((1.0 + 3.0 * poissons_ratio) / (3.0 + poissons_ratio)) * (r**2)
        )
        / 1e6
    )

    # Von Mises equivalent stress (plane stress assumption)
    von_mises = np.sqrt(sigma_r**2 - sigma_r * sigma_theta + sigma_theta**2)
    max_vm_mpa = float(np.max(von_mises))
    critical_radius_mm = float(r[np.argmax(von_mises)] * 1000.0)

    # Static Yield Factor of Safety
    fos_yield = yield_strength_mpa / max_vm_mpa

    # Modified Goodman Fatigue Analysis (accounting for hydraulic pressure pulsations)
    sigma_mean = max_vm_mpa
    sigma_alt = max_vm_mpa * pressure_fluctuation_ratio
    fos_goodman = 1.0 / (
        (sigma_alt / endurance_limit_mpa) + (sigma_mean / ultimate_strength_mpa)
    )

    return {
        "rpm": rpm,
        "max_radial_stress_mpa": round(float(np.max(sigma_r)), 2),
        "max_hoop_stress_mpa": round(float(np.max(sigma_theta)), 2),
        "max_von_mises_mpa": round(max_vm_mpa, 2),
        "critical_radius_mm": round(critical_radius_mm, 2),
        "static_fos_yield": round(float(fos_yield), 2),
        "fatigue_fos_goodman": round(float(fos_goodman), 2),
    }


if __name__ == "__main__":
    results = analyze_rotating_impeller()
    print("=== Impeller Structural & Fatigue Analysis Summary ===")
    for key, value in results.items():
        print(f"{key}: {value}")
      
