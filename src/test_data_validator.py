"""
Experimental Test-Rig Data Processing & Model Validation Script.
Parses pressure-transducer and torque sensor logs, computes hydraulic power,
shaft power, and overall pump efficiency, and checks against target specs.
"""

import os
import numpy as np
import pandas as pd


def validate_test_data(csv_path: str, target_efficiency_pct: float = 82.0) -> dict:
    df = pd.read_csv(csv_path)

    # Convert units to SI
    flow_m3s = df["flow_rate_m3h"] / 3600.0
    delta_p_pa = (df["discharge_pressure_bar"] - df["suction_pressure_bar"]) * 1e5
    omega = (2.0 * np.pi * df["rpm"]) / 60.0

    # Hydraulic Power (W) = Q * dP
    df["hydraulic_power_kw"] = (flow_m3s * delta_p_pa) / 1000.0

    # Shaft Mechanical Power (W) = Torque * omega
    df["shaft_power_kw"] = (df["shaft_torque_nm"] * omega) / 1000.0

    # Overall Efficiency (%)
    df["efficiency_pct"] = (df["hydraulic_power_kw"] / df["shaft_power_kw"]) * 100.0

    mean_eff = float(df["efficiency_pct"].mean())
    std_eff = float(df["efficiency_pct"].std())
    mean_dp_bar = float((df["discharge_pressure_bar"] - df["suction_pressure_bar"]).mean())

    return {
        "samples_processed": len(df),
        "mean_differential_pressure_bar": round(mean_dp_bar, 2),
        "mean_hydraulic_power_kw": round(float(df["hydraulic_power_kw"].mean()), 2),
        "mean_shaft_power_kw": round(float(df["shaft_power_kw"].mean()), 2),
        "mean_efficiency_pct": round(mean_eff, 2),
        "efficiency_std_dev_pct": round(std_eff, 3),
        "meets_design_spec": mean_eff >= target_efficiency_pct,
    }


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_file = os.path.join(base_dir, "data", "raw_pump_test_log.csv")
    report = validate_test_data(data_file)
    print("=== Experimental Test Validation Report ===")
    for key, val in report.items():
        print(f"{key}: {val}")
      
