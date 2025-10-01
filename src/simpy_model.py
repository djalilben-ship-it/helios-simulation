"""
Discrete-event simulation of helium production chain.
Scenario 1: Baseline (GNL2Z only)
Scenario 2: Improved (GNL2Z + GNL1 + GNL3)
"""

import simpy
import random


def supplier_process(env, tank, supplier_name, failure_rate=0.1):
    while True:
        yield env.timeout(5)  # supply every 5 time units
        if random.random() < failure_rate:
            yield env.timeout(10)  # downtime
        else:
            yield tank.put(1)
            print(f"{supplier_name} supplied helium unit at t={env.now}")


def run_simulation(suppliers, until=100):
    env = simpy.Environment()
    tank = simpy.Container(env, capacity=200, init=0)
    for name in suppliers:
        env.process(supplier_process(env, tank, name))
    env.run(until=until)
    return tank.level


if __name__ == "__main__":
    # Baseline: only GNL2Z
    baseline_stock = run_simulation(["GNL2Z"])
    print("Baseline helium stock:", baseline_stock)

    # Improved: GNL2Z + GNL1 + GNL3
    improved_stock = run_simulation(["GNL2Z", "GNL1", "GNL3"])
    print("Improved helium stock:", improved_stock)
