#!/usr/bin/python
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import sys

if len(sys.argv) == 1:
	print('usage: ./newton.py input.dat <output.pdf>')

D = np.loadtxt(sys.argv[1])

wavelength = D[0, 0] * 1e-9

D = D[1:,:].T

k = D[0]
r = np.abs(D[2] - D[1]) * 1e-3 / 2

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(k, r**2)

R = slope/wavelength

plt.ylabel('$r_k^2$ ($\\mathrm{mm^2}$)')
plt.xlabel('Ring Order $k$')
plt.grid()

x = np.array([k[0], k[-1]])
plt.plot(x, (x*slope + intercept)*1e6, '-r')

plt.plot(k, r**2 * 1e6, 'ob', label='$r_k$')

if len(sys.argv) == 2:
	print('curvature radius R =', R, 'm')
	print('r^2_k/k = ', slope * 1e6, 'mm^2')
	print('intercept = ', intercept, 'mm^2')
	plt.show()
else:
	plt.savefig(sys.argv[2])
