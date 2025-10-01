import re
from pathlib import Path
import os
import argparse

from IPython import embed

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pypad

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)


def print_lad():
    print(r"""


                                    =-=
                              -::-=====++=-:-
                           ::-=====+++++++++++=:
                         ::-========+==+++++++*+=--
                        :-=============+++++++****=-
                       :-===============+++++*******-
                      :-==-========+=====+++*********-
                      :==%*-=====++=*#+-+=+***********:
                     :===**======+++*%*=+=++**********+:
                    :-========++===+++++===++**********-
                  :::======+=+++++========+++**********=-:
               :::--======++=+*++*+======++***********+++=---
             ::-----=+====+++**++**++===+++**********+++===++=:
           ::-----===+====++******+++++++++***********+++++==++-
          :--====-----====+++======+++====+***********++==++==+=
        ::-====-:-   --=+*###**********++++********##=:   --=+*=
      ::--==-:        :=+++++********+++++*******###*:   ::=+++:
     ::==-=:          --+++++++===++++++++*******###==  ::==+*-
    .-=--.=:           :+++++++++*******+*********##=  :+===:+-
    :--: :--           :=+++************************- :=-:=- --=
    -:                 :==++***************+++++****= :- :-: :-
                       :===+****+===========++++++**=
                       :===+***--          :=+=++++*=
                      -:=-=+**-             :===+++*=
                      :-=-=+*==             --==+++*=
                      :===+**:              :===++**==
                -:::--=+++***-          ::--=++++****-
           :::--==+**********+-   :::--=+***####*###*+:
       :---===+++===+####*****=:--==++++=++*########**-
      --==++=+****++++-------:+++++=+*#*++==*#*+**++=--
            -------::         ----=:-====+==-


    """)


def main():
    parser = argparse.ArgumentParser(
        description="Launch IPython REPL with NumPy, Matplolib and Pandas imported."
    )
    # Accept both -w and -wordlist (the user asked for single-dash -wordlist)
    parser.add_argument(
        "-w",
        "-wordlist",
        action="store_true",
        dest="wordlist",
        help="Load words from src/assets/clean_dictionary.txt into the REPL as `words`",
    )
    args = parser.parse_args()

    if args.wordlist:
        try:
            word_path = (
                Path(pypad.__file__).parent.parent / "assets/clean_dictionary.txt"
            )
            with open(word_path, "r", encoding="utf-8") as f:
                words = f.read().split()
            print(f"Loaded {len(words)} words into `words`.")
        except FileNotFoundError:
            print(f"Wordlist file not found at {word_path} — starting without `words`.")
            words = []
        except Exception as e:
            print(f"Error loading wordlist: {e} — starting without `words`.")
            words = []

    # keep existing behavior (assumes print_lad is defined elsewhere)
    print_lad()
    print(
        f"Launching IPython with numpy {np.__version__}, pandas {pd.__version__}, matplotlib"
    )

    # Pass the current locals() so `words` (if defined) is available inside the REPL
    embed(user_ns=locals())


if __name__ == "__main__":
    main()
