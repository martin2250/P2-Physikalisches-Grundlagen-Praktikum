#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import linregress
import scipy
import sys

d, e, t = np.loadtxt('source/3.dat', unpack=True)

r = e/t
r = r - 0.3235	#background rate
r = r/(1-r*211e-6)	#dead time

def expon(x, a, b, c, d):
	return a*np.exp(-b*x) + c*np.exp(-d*x)

X = np.linspace(d[0], d[len(d)-1], 60)
popt, pconv = scipy.optimize.curve_fit(expon, d, r, bounds=([0, 0, 0, 0], [1000, 1, 1000, 1]))

plt.plot(X/25.4, expon(X, popt[0], popt[1], popt[2], popt[3]))

matplotlib.rc('text', usetex = True)
plt.xlabel('Thickness $d$ in thou')
plt.ylabel('Activity in Events / s')
plt.grid(which="both")

ax = plt.gca()
#ax.set_yscale('log')
#ax.set_xscale('log')

plt.plot(d/25.4, r, 'o')

if len(sys.argv) == 1:
	plt.show()
else:
	plt.savefig(sys.argv[1])
