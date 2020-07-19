"""
Daniel Maidment

Tue Oct 22 10:44:17 2019
"""
########################################################################

import numpy as np
from spnetwork.neuron.neuron import Neuron
########################################################################


class OutputNeuron(Neuron):

    def __init__(self, N=8):
        super().__init__(N)
        self._state = 0.0

    def __add__(self, other):
        nIn = False

        if(isinstance(other, tuple)
           or isinstance(other, list)
           or isinstance(other, np.ndarray)):
            for arg in other:
                nIn = np.logical_or(nIn, bool(arg))
        else:
            nIn = np.logical_or(nIn, bool(other))

        self.reg = np.roll(self.reg, shift=1)
        self.reg[0] = nIn

        self._state = np.mean(self.reg)

        return self._state

    def __str__(self):
        str_val = "{:.3}".format(self._state)
        return str_val

    def __repr__(self):
        str_val = "Output Neuron: "
        str_val += np.array2string(np.array(self.reg, dtype=int),
                                   separator=', ',
                                   suppress_small=True)
        str_val += f", p = {self._state:.3}"
        return str_val

    @property
    def state(self):
        self._state = np.mean(self.reg)
        return self._state
