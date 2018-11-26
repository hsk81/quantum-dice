#!/usr/bin/env python

from pyquil.api import QVMConnection
from pyquil.quil import Program as P
from pyquil.gates import H

from functools import reduce
from numpy import average

class QDice:

    def __init__(self):
        self.qvm = QVMConnection()
    
    def roll(self, trials=1):
        return self.qvm.run(
            self.magic.measure_all(), trials=trials)

    @property
    def magic(self):
        return P(H(0), H(1), H(2))

    @staticmethod
    def number(roll):
        return 1 + reduce(lambda i, j: 2*i+j, roll)

if __name__ == '__main__':

    qdice = QDice()
    rolls = qdice.roll(trials=1024)
    means = average(rolls, axis=0)

    for i, roll in enumerate(rolls):
        print("#%04d: [ %.3f %.3f %.3f ] => %d" % (
            i+1, *roll, QDice.number(roll)
        ))

    print("⟨H(i)⟩=[ %.3f %.3f %.3f ] => %.3f" % (
        *means, QDice.number(means)
    ))
