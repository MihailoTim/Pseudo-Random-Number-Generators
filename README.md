# Pseudo-Random-Number-Generators
Implementation of some basic pseudo-random number generators that were used in the early days of computing. Compared the density and sparsity of each algorithm
between themselves and against a random number generator from NumPy.

## Linear congruential generator (LCG)
An algorithm based on a linear recurrent equation. More about this algorithm can be found here: https://en.wikipedia.org/wiki/Linear_congruential_generator

## Blum Blum Shub (BBS)
An algorithm based on extracting bits from a sequence of pseudo-random numbers and assembling a result number from them. More about this algorithm: https://en.wikipedia.org/wiki/Blum_Blum_Shub

## Linear feedback shift register (LFSR)
An algorithm based on performing a XOR (or XNOR) operation on certain bit positions of a seed number. More about this algorithm: https://en.wikipedia.org/wiki/Linear-feedback_shift_register

## How to run the script
These random generators are implemented as modules so they can be used separately or from an already existing `plot.py` script. Plot script plots 100000 pseudo-randomized numbers from 
all three of these generators as well as 100000 from NumPy random generator. To check out the results run the `plot.py` script.  
For the script to run following things are needeed:
1. Python
2. Matplotlib
3. Numpy   
  
Install python, then get needed libraries using `pip` package installer with `pip install matplotlib numpy` 

## Results
