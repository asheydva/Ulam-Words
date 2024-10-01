# Ulam Words
A repository for data on Ulam words and Python code for computing terms

Ulam words were originally defined by Bade et al. in a 2020 paper (Ulam Sets in New Settings).
This repository contains code for an algorithm to compute all Ulam words up to a fixed length. We were able to use it to compute words up to length 30. However, since this produced a file over 4GB in size, we have only included all Ulam words up to length 20 in this repository.

There are two files in this repository:
  1. UlamWords_20_sorted.txt: this contains all Ulam words up to length 30.
  2. Ulam Words v5.py: this is a Python file containing functions needed to compute Ulam words. The primary algorithm is the last one, next_Ulam_words. Given the name of a file containing Ulam words up to some length k, it produces a file containing Ulam words up to length k + 1.

Ulam words are always stored in the following general format:
  1. A line "Length X" at the beginning denotes that below it are words of length X.
  2. Each word is represented by the corresponding integer, using binary. (E.g. the word '100' would be represented as 4; the word '001' would be represented as 1.)
