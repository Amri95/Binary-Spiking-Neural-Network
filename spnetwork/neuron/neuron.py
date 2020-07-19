"""
Daniel Maidment

Fri Oct  4 13:16:52 2019
"""
########################################################################

import numpy as np

########################################################################


class Neuron:

    def __init__(self, N=8):
        self.N = N
        self.reg = np.zeros(shape=self.N, dtype=bool)
        self._state = False

    def __repr__(self):
        str_val = "Neuron\n"
        str_val += np.array2string(np.array(self.reg, dtype=int),
                                   separator=', ',
                                   suppress_small=True)
        str_val += f", {int(self._state)}"
        return str_val

    def __str__(self):
        str_val = np.array2string(np.array(self.reg, dtype=int),
                                  separator=', ',
                                  suppress_small=True)
        str_val += f", {int(self._state)}"
        return str_val

    def __add__(self, other):
        nIn = False

        if(isinstance(other, tuple)
           or isinstance(other, list)
           or isinstance(other, np.ndarray)):
            for arg in other:
                nIn = np.logical_or(nIn, bool(arg))
        else:
            nIn = np.logical_or(nIn, bool(other))

        if(nIn):
            self.reg = np.roll(self.reg, shift=1)
            self.reg[0] = 1

        self._state = self.reg[-1]
        if(self._state):
            self.reset()

        return self._state

    def __len__(self):
        return len(self.reg)

    def reset(self):
        self.reg = np.zeros(shape=self.N, dtype=bool)
        return None

    @property
    def state(self):
        return self._state


def periodseries(T, N):
    s = np.empty(N, int)
    bit = False
    for i in range(N):
        s[i] = bit
        if(i % (N/T) == 0):
            bit = not bit
    return s
