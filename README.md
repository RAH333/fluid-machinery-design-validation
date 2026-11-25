# fluid-machinery-design-validation
End-to-end R&amp;D Mechanical Design &amp; Validation toolkit for high-pressure fluid machinery (centrifugal pump/pressure exchanger): Solid mechanics stress solver, GD&amp;T tolerance stack-up, DFMEA, and Python experimental test-data validation.

# Fluid Machinery R&D Design & Validation Suite

An engineering design, structural verification, and test-data validation toolkit tailored for high-pressure fluid machinery (centrifugal pumps, turbines, and pressure exchangers used in desalination and industrial processes).

## Engineering Objectives
1. **Mechanics of Solids & Fatigue Validation (`src/structural_stress_solver.py`):** Evaluates radial stress, hoop stress, Von Mises equivalent stress, and Goodman fatigue safety factors for rotating impeller discs under hydrodynamic pressure and centrifugal loads.
2. **GD&T & Tolerance Stack-Up (`src/tolerance_stackup.py` & `docs/GDT_Tolerance_Stackup_Report.md`):** Computes Worst-Case and Root Sum Square (RSS) radial clearance between impeller shroud and volute wear ring to ensure manufacturability and prevent mechanical interference.
3. **Experimental Test-Data Processing (`src/test_data_validator.py`):** Processes raw pressure-transducer and flowmeter CSV logs, applies signal filtering, computes hydraulic efficiency, and validates analytical predictions against test data.
4. **Risk & Quality Engineering (`docs/DFMEA_Fluid_Machinery.md`):** Design Failure Mode and Effects Analysis (DFMEA) aligned with ASME/ISO fluid machinery standards.

## Quick Start
```bash
git clone https://github.com<your-username>/fluid-machinery-design-validation.git
cd fluid-machinery-design-validation
pip install -r requirements.txt
python src/structural_stress_solver.py
python src/tolerance_stackup.py
python src/test_data_validator.py
```

## Key Engineering Outputs
- **Design Operating Point:** 3,600 RPM | Differential Pressure: 65 bar (6.5 MPa) | Material: Duplex Stainless Steel (SAF 2205)
- **Peak Von Mises Stress:** ~184.6 MPa (Factor of Safety > 2.4 against Yield)
- **Radial Clearance Stack-Up:** Nominal 0.35 mm | RSS Range: [0.278 mm, 0.422 mm] (Zero interference confirmed)
- 
```
fluid-machinery-design-validation/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── raw_pump_test_log.csv
├── docs/
│   ├── DFMEA_Fluid_Machinery.md
│   └── GDT_Tolerance_Stackup_Report.md
└── src/
    ├── __init__.py
    ├── structural_stress_solver.py
    ├── tolerance_stackup.py
    └── test_data_validator.py
```
