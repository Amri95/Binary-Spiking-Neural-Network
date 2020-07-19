"""
Daniel Maidment

Tue Oct  8 16:14:08 2019
"""
########################################################################

import spyder_utilities as su
import numpy as np
import matplotlib.pyplot as plt
import spnetwork.neuron
import spnetwork.synapse

########################################################################


class Network:

    def __init__(self, shape=(2, 3, 1),
                 nN=8,
                 sN=16, sSeed=0.5,
                 debug=False):

        self.shape = shape
        self.L = len(self.shape)
        self.nN = nN
        self.sN = sN
        self.sSeed = sSeed
        self.nLs = []
        self.sLs = []
        self._genNeurons()
        self._genSynapses()

        return None
########################### Imported methods ############analysis:ignore

    # _spnetworkinternal.py methods
    from spnetwork._nnutilities import _genNeurons
    from spnetwork._nnutilities import _genSynapses
    from spnetwork._nnutilities import __str__


if __name__ == "__main__":
    testNet = Network()
    print(testNet)
