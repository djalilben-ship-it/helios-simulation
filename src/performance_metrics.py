"""
Performance metrics for HELIOS production system.
Includes Availability, MTBF, MTTR, TRG (global efficiency).
"""

def availability(uptime, downtime):
    return uptime / (uptime + downtime)


def mtbf(uptime, failures):
    return uptime / failures if failures > 0 else float("inf")


def mttr(downtime, failures):
    return downtime / failures if failures > 0 else 0


def trg(availability, performance, quality):
    return availability * performance * quality


if __name__ == "__main__":
    # Real project values (baseline vs after new suppliers)
    baseline = {
        "availability": 0.82,
        "mtbf": 68,
        "mttr": 15,
        "trg": 0.72,
    }
    improved = {
        "availability": 0.93,
        "mtbf": 85,  # +25%
        "mttr": 12.7, # -15%
        "trg": 0.88,
    }
    print("Baseline:", baseline)
    print("Improved:", improved)
