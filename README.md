
# PyPad

PyPad is an Ipython based Read Evaluate Print Loop (REPL) with commonly used modules already loaded, as I found myself forever typing `import numpy as np` etc... when trying to test out methods.

## Installation

I got this idea from a great [article](https://www.bitecode.dev/p/uv-tricks) on UV tips by [bitecode](https://www.bitecode.dev/)

1. Make sure you have [UV](https://docs.astral.sh/uv/getting-started/installation/) installed
2. Clone this repo and `cd` into it
3. Run `Run uv tool install . -e`

It should now be globally available by invoking `pypad` in the command line.

## Usage

Call `pypad` in the command line and it should start up. Type `exit()` or ctrl-d to exit.

The imported modules are:

#### Builtins

- `re`: This module provides regular expression matching operations similar to those found in Perl
- `Pathlib`'s `Path`: PurePath subclass that can make system calls.
- `os`: OS routines for NT or Posix depending on what system we're on
 
#### Third Party

- `Numpy` as `np`: Provides an array object of arbitrary homogeneous items,fast mathematical operations over arrays and Linear Algebra, Fourier Transforms, Random Number Generation
- `Pandas` as `pd`: A package providing fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive
- `Matplotlib` as `plt`: A state-based interface to matplotlib. It provides an implicit, MATLAB-like, way of plotting. It also opens figures on your screen, and acts as the figure GUI manager

#### Optional

- `-w` or `--wordlist` will read from `clean_dictionary.txt` and store the list of words in a list called `words`.

## Modification

Fork this repo and add/remove whatever modules you want from `/src/pypad/__init__.py`.

I've added a brief argparser bit as I often want access to a dictionary of English words, but you could just as easily add a dummy dataframe or NumPy array generator for running experiments on.

It's also easy to modify the script to keep any plots inline, however I like them to be temporary and interactive.

You could even remove the orange lad ASCII art if you don't have a heart.
