# A Quantum Dice: Let's Gamble!

Billions of dollars are at stake! Play now a quantum mechanically enhanced dice to enrich yourself: Roll this brand new kind of a *quantum dice* - which has been built using [Rigetti's](https://www.rigetti.com/) *Forest* API - and beat the odds!

## Installation

To install the dependencies run:

```bash
pipenv install
```

To enable the virtual environment run:

```bash
pipenv shell
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

## Run: `qdice.py`

Simulates `1024` throws of a `8`-sided quantum dice, which has been implemented using `3` Hadamard gates: Sampling those gates results in `3` classical bits, which are then togheter interpreted as the binary representation of a single number in the range `[1..9]`.

```bash
$ python ./qdice.py --trials=1024 --hadamards=3
#0001:[ 0 1 0 ] => 3;
#0002:[ 1 0 1 ] => 6;
#0003:[ 0 0 0 ] => 1;
#0004:[ 0 0 0 ] => 1;
...
#1021:[ 0 1 1 ] => 4;
#1022:[ 1 1 0 ] => 7;
#1023:[ 0 1 1 ] => 4;
#1024:[ 0 1 0 ] => 3;
```

The result of the `1024` throws is averaged for each bit and the corresponding number, providing a simple statistics, where the expected distribution is uniform:

```bash
μ{⟨H(i)⟩}=[ 0.48 0.52 0.41 ], μ{∑H(i)*2^i}=4.46;
```
```bash
σ{⟨H(i)⟩}=[ 0.50 0.50 0.50 ], σ{∑H(i)*2^i}=4.50.
```

## Run: `qcolor.py`

Transforms the results of the random throws of a quantum dice into an RGB colored image, where the square root of the number of `trials` defines the height and width of the square image; hence `trials` should be a square number. The `simulate` flag controls whether a regular pseudo-random generator should be used to produce the throws.

```bash
$ python ./qcolor.py --trials=65536 [--simulate]
```

![Quantum Image](./img/qcolor-qvm.png)

## Copyright

 © 2018 Hasan Karahan, https://github.com/hsk81.
