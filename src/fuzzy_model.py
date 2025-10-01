"""
Fuzzy logic evaluation of HELIOS project.
Inputs: project duration, budget
Outputs: control level, yield
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def build_fuzzy_system():
    # Inputs
    duration = ctrl.Antecedent(np.arange(0, 25, 1), 'duration')
    budget = ctrl.Antecedent(np.arange(0, 50, 1), 'budget')

    # Outputs
    control = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'control')
    yield_out = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'yield')

    # Membership functions for duration
    duration['short'] = fuzz.trimf(duration.universe, [0, 0, 12])
    duration['medium'] = fuzz.trimf(duration.universe, [6, 12, 18])
    duration['long'] = fuzz.trimf(duration.universe, [12, 24, 24])

    # Membership functions for budget
    budget['low'] = fuzz.trimf(budget.universe, [0, 0, 15])
    budget['medium'] = fuzz.trimf(budget.universe, [10, 25, 40])
    budget['high'] = fuzz.trimf(budget.universe, [30, 50, 50])

    # Membership functions for control
    control['low'] = fuzz.trimf(control.universe, [0, 0, 0.5])
    control['medium'] = fuzz.trimf(control.universe, [0.3, 0.6, 0.8])
    control['high'] = fuzz.trimf(control.universe, [0.7, 0.9, 1])

    # Membership functions for yield
    yield_out['poor'] = fuzz.trimf(yield_out.universe, [0, 0, 0.5])
    yield_out['average'] = fuzz.trimf(yield_out.universe, [0.4, 0.7, 0.9])
    yield_out['optimal'] = fuzz.trimf(yield_out.universe, [0.8, 1, 1])

    # Rules (can be expanded if needed)
    rules = [
        ctrl.Rule(duration['short'] & budget['high'], (control['high'], yield_out['optimal'])),
        ctrl.Rule(duration['medium'] & budget['medium'], (control['medium'], yield_out['average'])),
        ctrl.Rule(duration['long'] & budget['low'], (control['low'], yield_out['poor']))
    ]

    system = ctrl.ControlSystem(rules)
    return ctrl.ControlSystemSimulation(system)


if __name__ == "__main__":
    sim = build_fuzzy_system()
    # Real project inputs
    sim.input['duration'] = 12   # months
    sim.input['budget'] = 30     # M USD

    sim.compute()
    print("Control Level:", round(sim.output.get('control', -1), 2))
    print("Project Yield:", round(sim.output.get('yield', -1), 2))
