"""
Daniel Maidment

Wed Oct  9 10:27:23 2019
"""
########################################################################

#import spyder_utilities as su
import numpy as np
from spnetwork.neuron import DelayFBNeuron2 as Neuron
from spnetwork.synapse import Synapse
########################################################################
########################## Internal Functions ###########analysis:ignore
########################################################################


def _genNeurons(self):
    for l in range(self.L):
        self.nLs.append(np.empty(shape=self.shape[l],
                                 dtype=object))
    for l in range(self.L):
        for j in range(self.shape[l]):
            self.nLs[l][j] = Neuron(self.nN)
    return None


def _genSynapses(self):
    for l in range(self.L-1):
        self.sLs.append(np.empty(shape=(self.shape[l+1],
                                        self.shape[l]),
                                 dtype=object))
    for l in range(self.L-1):
        for j in range(self.shape[l+1]):  # rows
            for k in range(self.shape[l]):  # cols
                self.sLs[l][j, k] = Synapse(self.sN)
    return None


def __str__(self):
    str_val = ""
    for l in range(self.L-1):
        for j in range(self.shape[l]):
            str_val += str(self.nLs[l][j])
            str_val += f" {l},{j}"
            str_val += "\n"
        str_val += "\n"
        for i in range(self.shape[l+1]):
            for k in range(self.shape[l]):
                str_val += str(self.sLs[l][i, k])
                str_val += f" {l},{i},{k}"
                str_val += "\n"
            str_val += "\n"
    for j in range(self.shape[self.L-1]):
        str_val += str(self.nLs[self.L-1][j])
        str_val += f" {self.L-1},{j}"

    return str_val
