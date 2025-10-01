"""
Statistical analysis tools for helium production data.
Replicates thesis methods: mean, std, CI, control charts.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st


def basic_stats(data: pd.Series):
    mean = data.mean()
    std = data.std()
    ci_low, ci_high = st.t.interval(alpha=0.95, df=len(data)-1,
                                    loc=mean, scale=st.sem(data))
    return {"mean": mean, "std": std, "95%_CI": (ci_low, ci_high)}


def plot_control_chart(data: pd.Series, title="Helium Production Control Chart"):
    mean = data.mean()
    std = data.std()
    plt.figure(figsize=(10,5))
    plt.plot(data.index, data.values, marker="o", label="Production")
    plt.axhline(mean, color="red", linestyle="--", label="Mean")
    plt.axhline(mean+3*std, color="green", linestyle="--", label="+3σ")
    plt.axhline(mean-3*std, color="green", linestyle="--", label="-3σ")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()
