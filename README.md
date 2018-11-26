# A Quantum Dice: Let's Gamble!

Billions of dollars are at stake! Play now a quantum mechanically enhanced dice to enrich yourself: Roll this brand new kind of a *quantum dice* - which has been built using [Rigetti's](https://www.rigetti.com/) *Forest* API - and beat the odds!

## Installation

```bash
pipenv install
```

## Run: QVM Server

Requires a 64-bit Linux environment:

```bash
$ ./bin/forest-sdk-2.0.2/qvm --server
[2018-11-26 12:24:19] Starting server on port 5000.
```

with the following run-time dependencies:

```bash
$ ldd ./bin/forest-sdk-2.0.2/qvm
linux-vdso.so.1 (0x00007ffc05919000)
libdl.so.2=> /usr/lib/libdl.so.2 (0x00007f8aaaea9000)
libpthread.so.0 => /usr/lib/libpthread.so.0 (0x00007f8aaae88000)
libz.so.1 => /usr/lib/libz.so.1 (0x00007f8aaac71000)
libm.so.6 => /usr/lib/libm.so.6 (0x00007f8aaaaec000)
libc.so.6 => /usr/lib/libc.so.6 (0x00007f8aaa928000)
/lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2(0x00007f8aaaed8000)
```

## Run: `q-dice.py`

Simulates `1024` throws of a `9`-sided quantum dice, which has been implemented using `3` Hadamard gates: Sampling those gates results in `3` classical bits, which are then togheter interpreted as the binary representation of a single number in the range `[1..9]`.

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

The result of the `1024` throws is averaged for each bit and the corresponding number, providing a simple statistical check w.r.t. to the expected uniform distribution:

```bash
⟨H(i)⟩=[ 0.492 0.519 0.530 ] => 4.536
```

## QColor: Quantum Colors
...

## Copyright

 © 2018 Hasan Karahan, https://github.com/hsk81.
