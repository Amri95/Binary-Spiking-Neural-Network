"""
Daniel Maidment

Tue Oct 22 10:47:21 2019
"""
########################################################################

import numpy as np
from spnetwork.neuron.neuron import Neuron

########################################################################


class XORFBNeuron(Neuron):

    def __init__(self, N=4):
        super().__init__(N)

    def __add__(self, other):
        nIn = False

        if(isinstance(other, tuple)
           or isinstance(other, list)
           or isinstance(other, np.ndarray)):
            for arg in other:
                nIn = np.logical_or(nIn, bool(arg))
        else:
            nIn = np.logical_or(nIn, bool(other))

        # Feedback instruction
        nIn = np.logical_xor(nIn, self.state)

        if(nIn):
            self.reg = np.roll(self.reg, shift=1)
            self.reg[0] = 1

        self._state = self.reg[-1]
        if(self._state):
            self.reset()

        return self._state

    def __repr__(self):
        str_val = "XOR\nFeedback Neuron\n"
        str_val += np.array2string(np.array(self.reg, dtype=int),
                                   separator=', ',
                                   suppress_small=True)
        str_val += f", {int(self._state)}"
        return str_val
