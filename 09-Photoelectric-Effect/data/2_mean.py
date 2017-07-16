#!/usr/bin/python
from __future__ import division, print_function
import scipy.optimize
import numpy as np

(R, U) = np.loadtxt('source/2.dat', unpack=True)

R=R[1:]
U=U[1:]
U_0=5

Ri= R * (U / (U_0-U))

print('internal resistance with mean: %e'%np.mean(Ri), '+/- %e' %np.std(Ri))
