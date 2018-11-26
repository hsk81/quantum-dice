#!/usr/bin/env python

from pyquil.api import QVMConnection
from pyquil.quil import Program as P
from pyquil.gates import H

from functools import reduce
from numpy import average
from numpy import ceil
from numpy import log
from numpy import std

import argparse

class QDice:

    def __init__(self):
        self.qvm = QVMConnection()

    def roll(self, hadamards=3, trials=1):
        return self.qvm.run(
            self.magic(hadamards=hadamards).measure_all(), trials=trials)

    def magic(self, hadamards=3):
        return P(*list(map(lambda i: H(i), range(hadamards))))

    @staticmethod
    def number(roll):
        return 1 + reduce(lambda i, j: 2*i+j, roll)

def digits(n: int) -> int:

    return ceil(log(n)/log(10))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Produces statistics of a quantum dice.')
    parser.add_argument(
        '-H', '--hadamards', type=int, default=3)
    parser.add_argument(
        '-n', '--trials', type=int, default=1024)
    args = parser.parse_args()

    qdice = QDice()
    rolls = qdice.roll(hadamards=args.hadamards, trials=args.trials)
    gamma = average(rolls, axis=0)
    sigma = std(rolls, axis=0)

    string = "#%0{0}d:[{1} ] => %0{2}d;".format(
        digits(args.trials), args.hadamards*' %.2f', digits(2**args.hadamards))
    for i, roll in enumerate(rolls):
        print(string % (i+1, *roll, QDice.number(roll)))

    print("")
    print("μ{{⟨H(i)⟩}}=[{0} ], μ{{∑H(i)*2^i}}=%.2f;".format(
        args.hadamards*' %.2f') % (*gamma, QDice.number(gamma)))
    print("σ{{⟨H(i)⟩}}=[{0} ], σ{{∑H(i)*2^i}}=%.2f.".format(
        args.hadamards*' %.2f') % (*sigma, QDice.number(sigma)))
