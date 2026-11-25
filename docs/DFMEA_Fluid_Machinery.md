# Design Failure Mode and Effects Analysis (DFMEA)
**System:** High-Pressure Desalination Centrifugal Pump / Pressure Recovery Rotor  
**Standard Alignment:** ASME PTC 8.2 / ISO 5199  

| Item / Function | Potential Failure Mode | Potential Effect of Failure | Severity (S) | Potential Cause | Occurrence (O) | Current Design Controls | Detection (D) | RPN | Recommended Action |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| **Impeller Shroud & Vanes** | High-cycle fatigue cracking at vane root | Sudden loss of discharge pressure & rotor imbalance | 9 | Cyclic hydraulic pressure pulsations & stress concentration | 3 | FEA harmonic & Goodman fatigue safety factor > 2.0 | 4 | **108** | Increase fillet radius at vane-to-hub junction; shot-peen surface |
| **Wear-Ring Clearance Interface** | Radial galling / mechanical seizure | Seized shaft, motor overload, emergency shutdown | 9 | Excessive tolerance stack-up or shaft deflection | 2 | GD&T concentricity datum callout & RSS tolerance stack-up | 3 | **54** | Specify non-galling PEEK or Nitronic 60 wear-ring material |
| **Mechanical Seal Housing** | High-pressure brine leakage | Environmental hazard, bearing contamination | 8 | O-ring extrusion under 65 bar differential pressure | 3 | ASME groove dimensioning & hydro-test at 1.5x MAWP | 2 | **48** | Add PTFE anti-extrusion backup ring |
