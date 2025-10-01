"""
Failure Mode and Effects Analysis (AMDEC/FMEA).
Calculates Risk Priority Numbers (RPN).
"""

import pandas as pd

def calculate_rpn(df: pd.DataFrame):
    df["RPN"] = df["Severity"] * df["Occurrence"] * df["Detection"]
    return df.sort_values("RPN", ascending=False)


if __name__ == "__main__":
    # Example failure modes from HELIOS PSA & compressors
    fmea_data = pd.DataFrame({
        "FailureMode": ["Compressor stop", "Valve stuck", "PSA leakage"],
        "Severity": [9, 7, 8],
        "Occurrence": [3, 4, 2],
        "Detection": [2, 3, 2]
    })
    result = calculate_rpn(fmea_data)
    print(result)
