#!/usr/bin/env python

from pyquil.api import QVMConnection
from pyquil.quil import Program
from pyquil.gates import H

from matplotlib import pyplot as pp
from numpy import array, random

import argparse

class QColor:

    def __init__(self, simulate=False):

        self.qvm = QVMConnection()
        self.sim = simulate

    def run(self, trials=1, simulate=False):

        if self.sim:
            return random.random((65536, 3)).round()
        else:
            return self.qvm.run(
                self.rgb.measure_all(), trials=trials)

    @property
    def rgb(self):
        return Program(H(0), H(1), H(2))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Produces a quantum image.')
    parser.add_argument(
        '-s', '--simulate', action='store_true')
    args = parser.parse_args()

    qcolor = QColor(simulate=args.simulate)
    trials = qcolor.run(trials=65536)
    r, g, b = array(trials).transpose()
    rgb = array([r,g,b]).reshape((256, 256, 3))

    pp.subplot(121)
    pp.title('Quantum Image')
    pp.imshow(rgb*255)

    pp.subplot(333)
    pp.title('Color Channels')
    pp.hist(r.cumsum(), color='r', bins=64)
    pp.subplot(336)
    pp.hist(g.cumsum(), color='g', bins=64)
    pp.subplot(339)
    pp.hist(b.cumsum(), color='b', bins=64)

    pp.show()
