"""
Daniel Maidment

Thu Oct 10 09:56:42 2019
"""
########################################################################

import spyder_utilities as su
import numpy as np
import matplotlib.pyplot as plt
from SpNetwork import SpNeuron
########################################################################
np.random.seed(100)

size = 100
N = 6

fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax = su.config_axis(ax, x_lim=(0, 1), y_lim=(0, 1), Eng=False)
P = np.arange(0.01, 1, 0.05)

s = f"Synaptic inputs per point: {size[0]}{size[1]}"

for n in np.arange(5, N, 1):
    tNeuron = SpNeuron.SpNeuron(n)
    p_x = np.empty(np.shape(P), dtype=float)
    p_y = np.empty(np.shape(P), dtype=float)

    for i in range(len(P)):
        in_ar_1 = np.array(np.random.binomial(1, P[i], size), dtype=bool)
        in_ar_2 = np.array(np.random.binomial(1, P[i], size), dtype=bool)
        p_x[i] = np.mean(in_ar_1)

        out_ar = np.zeros(size[0], bool)

        for j in range(size[0]):
            out_ar[j] = tNeuron + in_ar[j]

        p_y[i] = np.mean(out_ar)
        tNeuron.reset()

    slope = np.mean(np.gradient(p_y, p_x))
    label = f"N = {n:2d}, m"
    label += r"$\approx$" + "{:4.3}".format(slope)
    ax.scatter(p_x, p_y, label=label)
#    s += f"\nN={n}: m" + r"$\approx$" + "{:4.3}".format(slope)

plt.legend()
ax.text(0, 1.01, s,
        horizontalalignment='left',
        verticalalignment='bottom',
        transform=ax.transAxes)
plt.show()
#su.save_fig(fig=fig, image_nm="neuron_frequency_model", eps=True)