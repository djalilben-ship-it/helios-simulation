"""
PSA process cycle modeled as a state machine.
Steps: adsorption → equalization → purge → recompression
"""

from transitions import Machine


class PSAProcess:
    states = ["adsorption", "equalization_hp", "equalization_lp",
              "purge", "recompression"]

    transitions = [
        {"trigger": "next", "source": "adsorption", "dest": "equalization_hp"},
        {"trigger": "next", "source": "equalization_hp", "dest": "equalization_lp"},
        {"trigger": "next", "source": "equalization_lp", "dest": "purge"},
        {"trigger": "next", "source": "purge", "dest": "recompression"},
        {"trigger": "next", "source": "recompression", "dest": "adsorption"},
    ]

    def __init__(self):
        self.machine = Machine(model=self, states=PSAProcess.states,
                               transitions=PSAProcess.transitions,
                               initial="adsorption")


if __name__ == "__main__":
    psa = PSAProcess()
    for _ in range(7):
        print("Current state:", psa.state)
        psa.next()
