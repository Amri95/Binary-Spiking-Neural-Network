"""
Daniel Maidment

Tue Oct 22 10:42:33 2019
"""
########################################################################

import numpy as np

########################################################################


class InputNeuron:

    def __init__(self):
        self.reg = False
        self.p = 0.5

    def __add__(self, p):
        if(isinstance(p, tuple) or
           isinstance(p, list) or
           isinstance(p, np.ndarray)):
            s = "Attempeted to pass a list, tupple or array to"
            s += "input neuron seed"
            raise Exception(s)
        elif(p >= 1.0 or p < 0.0):
            s = "Input neuron seed value was not within [0, 1)"
            raise Exception(s)
        else:
            self.p = p
            self.reg = bool(np.random.binomial(1, self.p, 1))
            return self.reg

    def __repr__(self):
        str_val = "Input Neuron: "
        str_val += f"x={int(self.reg)}, P={self.p:.3}"
        return str_val

    def __str__(self):
        str_val = f"{int(self.reg)}"
        return str_val

        return self.reg

    @property
    def state(self):
        return self.reg
