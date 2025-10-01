
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

## Modification

Fork this repo and add/remove whatever modules you want from `/src/pypad/__init__.py`.

I've added a brief argparser bit as I often want access to a dictionary of English words, but you could just as easily add a dummy dataframe or NumPy array generator for running experiments on.

It's also easy to modify the script to keep any plots inline, however I like them to be temporary and interactive.

You could even remove the orange lad ASCII art if you don't have a heart.
