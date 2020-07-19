"""
Daniel Maidment

Sat Oct  5 14:50:24 2019
"""
########################################################################

import numpy as np

########################################################################


class Synapse:

    def __init__(self, N=8, p=0.5, lr=0.1):
        self.N = N
        self._p = p
        self.reg = np.zeros(shape=8, dtype=bool)
        self.seed(self._p)
        self._state = False

    def getMean(self):
        return np.mean(self.reg)

    def seed(self, p):
        self._p = p
        self.reg = np.array(np.random.binomial(1, self._p, self.N),
                            dtype=bool)

        return None
    
    def load(self, shift_reg):
        self.reg = np.array(shift_reg, dtype=bool)
        
        return None

    def __mul__(self, sIn=False):
        if(not isinstance(sIn, bool)):
            sIn = bool(sIn)
        self._state = np.bitwise_and(self.reg[-1], sIn, dtype=bool)
        self.reg = np.roll(self.reg, shift=1)

        return self._state

    def __add__(self, up):
        self._freq_shift(fs=up)
        return np.mean(self.reg)

    def __sub__(self, down):
        self._freq_shift(fs=-1*down)
        return np.mean(self.reg)

    def __repr__(self):
        str_val = "Synapse: "
        str_val += np.array2string(np.array(self.reg,
                                            dtype=int),
                                   separator=', ',
                                   suppress_small=True)
        str_val += ", f = " + str(np.mean(self.reg))
        str_val += ", N = " + str(self.N)
        return str_val

    def __str__(self):
        str_val = np.array2string(np.array(self.reg[0:2], dtype=int),
                                  separator=', ',
                                  suppress_small=True)[:-1]
        str_val += ", ..., "
        str_val += np.array2string(np.array(self.reg[-2:],
                                            dtype=int),
                                   separator=', ',
                                   suppress_small=True)[1:]
        str_val += ", f = " + str(np.mean(self.reg))
        return str_val

    def _f_recurse_up(self, fd, L=1, fi=0.1, debug=False):
        if(debug):
            print("up")

        idx = np.where(self.reg == 0)[0]
        ridx = np.random.randint(0, high=len(idx), size=L)

        for r in ridx:
            self.reg[idx[r]] = 1

        fc = np.mean(self.reg)
        L = int(np.round(abs(fc-fd), 4)/fi)
        if(fc < fd):
            self._f_recurse_up(fd, L, fi, debug)
        return True

    def _f_recurse_down(self, fd, L=1, fi=0.1, debug=False):
        if(debug):
            print("down")

        idx = np.where(self.reg == 1)[0]
        ridx = np.random.randint(0, high=len(idx), size=L)
        for r in ridx:
            self.reg[idx[r]] = 0
        fc = np.mean(self.reg)
        L = int(np.round(abs(fc-fd), 4)/fi)
        if(fc > fd):
            self._f_recurse_down(fd, L, fi, debug)
        return None

    def _freq_shift(self, fs=0.1, debug=False):
        fi = 1/self.N
        f_pos = np.arange(0, 1, fi)
        fc = np.mean(self.reg)
        fd = fc+fs
        fd = np.round(self._find_val(f_pos[1:], fd), 3)
        dist = int(np.round(abs(fc-fd), 4)/fi)

        if(fd > fc):
            self._f_recurse_up(fd, dist, fi)
        elif(fd < fc):
            self._f_recurse_down(fd, dist, fi)

        return None

    def _find_val(self, arr, val):
        idx = (np.abs(arr-val)).argmin()
        return arr[idx]

    @property
    def state(self):
        return self._state


if __name__ == "__main__":
    from spnetwork.neuron import Neuron
    preSyn = Neuron(N=2)
    postSyn = Neuron(N=4)
    ts = Synapse(p=0.9)

    for i in range(10):
        nIn = np.random.binomial(1, 0.5, 2)
        print("Input:\t\t", nIn)
        preOut = preSyn+nIn
        print("Layer 1:\t", preSyn)
        print("Layer 1 out:\t", int(preOut))
        print("Synapse:\t", ts)
        ts*preOut
#        p = ts-0.1
#        print("new frequency:\t", p)
        print("Synapse out:\t", int(ts.state))
        postOut = postSyn+ts.state
        print("Layer 2:\t", postSyn)
        print("Layer 2 out:\t", int(postOut))
        print("______________________________________________\n")

    print(ts.__repr__())
