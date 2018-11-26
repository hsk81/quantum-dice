# A Quantum Dice: Let's Gamble!

Billions of dollars are at stake! Play now a quantum mechanically enhanced dice to enrich yourself: Roll this brand new kind of a *quantum dice* - which has been built using [Rigetti's](https://www.rigetti.com/) *Forest* API - and beat the odds!

## QDice: Quantum Dice

```python
from pyquil.api import QVMConnection
from pyquil.quil import Program as P
from pyquil.gates import H
```

```python
from functools import reduce
from numpy import average
```

```python
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
```

```python
if __name__ == '__main__':

    qdice = QDice()
    rolls = qdice.roll(trials=1024)
    means = average(rolls, axis=0)

    for i, roll in enumerate(rolls):
        print("#%03d:[ %.3f %.3f %.3f ] => %d" % (
            i+1, *roll, QDice.number(roll)
        ))

    print("⟨H(i)⟩=[ %.3f %.3f %.3f ] => %.3f" % (
        *means, QDice.number(means)
    ))
```

```bash
$ python q-dice.py
#0001:[ 1.000 1.000 0.000 ] => 7
#0002:[ 1.000 1.000 0.000 ] => 7
#0003:[ 1.000 1.000 1.000 ] => 8
#0004:[ 0.000 0.000 1.000 ] => 2
...
#1021:[ 0.000 1.000 1.000 ] => 4
#1022:[ 0.000 0.000 1.000 ] => 2
#1023:[ 1.000 1.000 0.000 ] => 7
#1024:[ 1.000 0.000 1.000 ] => 6
```

```bash
⟨H(i)⟩=[ 0.492 0.519 0.530 ] => 4.536
```

## QColor: Quantum Colors
...

## Copyright

 © 2018 Hasan Karahan, https://github.com/hsk81.
