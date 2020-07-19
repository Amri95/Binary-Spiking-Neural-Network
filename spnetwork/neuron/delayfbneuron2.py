"""
Daniel Maidment

Wed Oct 23 13:03:10 2019
"""
########################################################################


import numpy as np
from spnetwork.neuron.neuron import Neuron
from spnetwork.neuron.neuron import periodseries

########################################################################


class DelayFBNeuron2(Neuron):

    def __init__(self, N=4, Nfb=2):
        super().__init__(N)
        self.Nfb = Nfb
        self.fbreg = np.zeros(shape=self.Nfb, dtype=bool)

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
        nIn = np.logical_xor(nIn, self.fbreg[-1])

        self.reg = np.roll(self.reg, shift=1)
        self.reg[0] = nIn

        self._state = self.reg[-1]
#        if(self._state or self.fbreg[-1]):
        if(self.fbreg[-1]):
            self.fbreg[:] = False
        self.fbreg = np.roll(self.fbreg, shift=1)
        self.fbreg[0] = self._state

        return self.state

    def reset(self):
        self.reg = np.zeros(shape=self.N, dtype=bool)
        self.fbreg = np.zeros(shape=self.Nfb, dtype=bool)
        return None

    def __repr__(self):
        str_val = "Delay Feedback Neuron\n"
        str_val += "Main:\t\t"
        str_val += np.array2string(np.array(self.reg, dtype=int),
                                   separator=', ',
                                   suppress_small=True)
        str_val += f", {int(self._state)}\n"
        str_val += "Feedback:\t"
        str_val += np.array2string(np.array(self.fbreg, dtype=int),
                                   separator=', ',
                                   suppress_small=True)

        return str_val


if __name__ == "__main__":
    import spyder_utilities as su
    import matplotlib.pyplot as plt

    np.random.seed(100)
    N = 100
    t = np.arange(0, N, 1)


    s = np.zeros(N, bool)
    s[int(N/3)] = True
#    s[int(N/2)+1] = True
#    s = periodseries(100, 100)
    s = np.random.binomial(1, 0.1, (2,N))
    nn = 4
    tnls = [Neuron(nn),
            DelayFBNeuron2(nn, 3)]
    nN = len(tnls)
    p = 0.5
    nS = 2
    tnout = np.zeros((nN, N), dtype=int)
    for i in range(N):
        for k in range(len(tnls)):
            tnls[k]+s[:, i]
            tnout[k, i] = int(tnls[k].state)

    fig0, axarr = plt.subplots(nS+nN, 1, figsize=(14, 1.5*(nS+nN)),
                               sharex=True, sharey=True)
    for i in range(nS):
        lbl = "Input {}\nmean={:.3}".format(i, np.mean(s))
        axarr[i] = su.binary_ax_config(N=N, ax=axarr[i])
        axarr[i].step(t, s[i, :], where='post', linewidth=1)
        axarr[i].text(1.01, 0.5, s=lbl,
                      horizontalalignment='left',
                      verticalalignment='center',
                      transform=axarr[i].transAxes)

    for j in range(nS, nN+nS):
        lbl = tnls[j-nS].__repr__()
        lbl += "\nmean={:.3}".format(np.mean(tnout[j-nS]))
        axarr[j] = su.binary_ax_config(N=N, ax=axarr[j])
        axarr[j].step(t, tnout[j-nS], where='post', linewidth=1,
                      label=lbl)
        axarr[j].text(1.01, 0.5, s=lbl,
                      horizontalalignment='left',
                      verticalalignment='center',
                      transform=axarr[j].transAxes)

    axarr[-1].set_xlabel("Number of clock cycles")
    plt.show()
    [n.reset() for n in tnls]

#su.save_fig(fig=fig0, path = "\\images\\neuron\\delayFB", image_nm=f"timeseries_model", eps=True)
