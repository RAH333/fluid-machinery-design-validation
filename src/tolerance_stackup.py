"""
1D GD&T Radial Clearance Tolerance Stack-Up Analysis
Evaluates Worst-Case and Root Sum Square (RSS) radial clearance between
a centrifugal impeller wear-ring OD and stationary casing bore ID.
"""

import numpy as np


def run_radial_clearance_stackup() -> dict:
    """
    Loop equation: Radial Clearance C = R_casing_bore - R_impeller_ring + Concentricity_offset
    All values in millimeters (mm).
    """
    components = [
        {"name": "Casing Wear-Ring Bore Radius (+)", "nominal": 85.350, "tol": 0.025, "sign": 1},
        {"name": "Impeller Hub Wear-Ring Radius (-)", "nominal": 85.000, "tol": 0.020, "sign": -1},
        {"name": "Bearing Housing Runout / Concentricity", "nominal": 0.000, "tol": 0.030, "sign": 1},
        {"name": "Shaft-to-Impeller Keyway Fit Play", "nominal": 0.000, "tol": 0.015, "sign": 1},
    ]

    nominal_clearance = sum(c["nominal"] * c["sign"] for c in components)
    worst_case_tol = sum(c["tol"] for c in components)
    rss_tol = float(np.sqrt(sum(c["tol"] ** 2 for c in components)))

    return {
        "nominal_radial_clearance_mm": round(nominal_clearance, 4),
        "worst_case_min_mm": round(nominal_clearance - worst_case_tol, 4),
        "worst_case_max_mm": round(nominal_clearance + worst_case_tol, 4),
        "rss_min_mm": round(nominal_clearance - rss_tol, 4),
        "rss_max_mm": round(nominal_clearance + rss_tol, 4),
        "design_status": "PASS - Zero Rubbing Risk" if (nominal_clearance - worst_case_tol) > 0.15 else "REVIEW",
    }


if __name__ == "__main__":
    summary = run_radial_clearance_stackup()
    print("=== GD&T Radial Clearance Stack-Up Results ===")
    for k, v in summary.items():
        print(f"{k}: {v}")
      
