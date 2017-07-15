#!/usr/bin/python
from __future__ import division, print_function
import scipy.optimize
import numpy as np

(R, U) = np.loadtxt('source/2.dat', unpack=True)

def u(R, rref, U0):
	return U0 * rref/(rref + R)

popt, pconv = scipy.optimize.curve_fit(u, R, U)

print('internal resistance: %e'%popt[0])
print('U0:', popt[1])
