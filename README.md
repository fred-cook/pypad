
# PyPad

PyPad is a python scratch pad to quickly write and test python functions/classes with useful modules already imported and ready for use, as I found myself forever typing `import numpy as np` etc...

It uses Ipython which has excellent autocomplete tooling built in, along with many other cool/useful [features](https://ipython.readthedocs.io/en/stable/interactive/reference.html#)

## Installation

I got this idea from a great [article](https://www.bitecode.dev/p/uv-tricks) on UV tips by [bitecode](https://www.bitecode.dev/)

1. Make sure you have [UV](https://docs.astral.sh/uv/getting-started/installation/) installed
2. Clone this repo and `cd` into it
3. Run `uv tool install . -e`

It should now be globally available by invoking `pypad` in the command line.

## Usage

Call `pypad` in the command line and it should start up. Type `exit()` or ctrl-d to exit.

The imported modules are:

#### Builtins

- `re`: Regular expression operations.
- `pathlib.Path` as `Path`: Object-oriented filesystem paths.
- `os`: Operating system routines for file and environment management.
 
#### Third Party

- `numpy` as `np`: Fast array operations, linear algebra, random number generation, and more.
- `pandas` as `pd`: High-performance data structures for labeled or relational data.
- `matplotlib.pyplot` as `plt`: MATLAB-like plotting interface; opens interactive figures.

#### Optional

- `-w` or `--wordlist` will read from `clean_dictionary.txt` and store the list of words in a list called `words`.

## Modification

Fork this repo and add/remove whatever modules you want from `/src/pypad/__init__.py`.

I've added a brief argparser bit as I often want access to a dictionary of English words, but you could just as easily add a dummy dataframe or NumPy array generator for running experiments on.

It's also easy to modify the script to keep any plots inline, however I like them to be temporary and interactive.

You could even remove the orange lad ASCII art if you don't have a heart.
