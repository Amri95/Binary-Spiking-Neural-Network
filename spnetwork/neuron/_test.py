"""
Daniel Maidment

Tue Oct 22 10:56:31 2019
"""
########################################################################

import spyder_utilities as su
import numpy as np
import matplotlib.pyplot as plt

from neuron.delayfbneuron import DelayFBNeuron
#  from neuron.inputneuron import InputNeuron
from neuron.nandfbneuron import NANDFBNeuron
from neuron.neuron import Neuron
#  from neuron.outputneuron import OutputNeuron
from neuron.xorfbneuron import XORFBNeuron
from neuron.delayfbneuron2 import DelayFBNeuron2

########################################################################

np.random.seed(100)
nn = 4
tnls = [Neuron(nn),
        XORFBNeuron(nn),
        DelayFBNeuron(nn),
        NANDFBNeuron(nn)]
print(tnls[2].__repr__())
nN = len(tnls)
N = 200
p = 0.5
nS = 2
t = np.arange(0, N, 1)
s = np.random.binomial(1, p, (N, nS))
tnout = np.zeros((nN, N), dtype=int)
for i in range(N):
    for k in range(len(tnls)):
        tnls[k]+s[i]
        tnout[k, i] = int(tnls[k].state)

fig0, axarr = plt.subplots(nS+nN, 1, figsize=(14, 1.5*(nS+nN)),
                           sharex=True, sharey=True)
for i in range(nS):
    lbl = "Input {}\nmean={:.3}".format(i, np.mean(s[:, i]))
    axarr[i] = su.binary_ax_config(N=N, ax=axarr[i])
    axarr[i].step(t, s[:, i], where='post', linewidth=1)
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