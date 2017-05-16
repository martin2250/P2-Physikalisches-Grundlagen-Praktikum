#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import linregress
import scipy
import sys

d, e, t = np.loadtxt('source/3.dat', unpack=True)

#d in um
d = d + 12	#tube window

r = e/t
r = r/(1-r*211e-6)	#dead time
r = r - 0.3235	#background rate

def expon(x, a, b, c, d):
	return a*np.exp(-b*x) + c*np.exp(-d*x)

#discard last two values for curve fitting, since exponential model only works up to ~50 percent
popt, pconv = scipy.optimize.curve_fit(expon, d[:-2], r[:-2], bounds=([0, 0, 0, 0], [1000, 1, 1000, 1]))

X = np.exp(np.linspace(np.log(d[0]), np.log(d[len(d)-1]), 60))
plt.plot(X, expon(X, popt[0], popt[1], popt[2], popt[3]))

matplotlib.rc('text', usetex = True)
plt.xlabel('Thickness $d$ in microns')
plt.ylabel('Activity in Events / s')
plt.grid(which="both")

ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')

plt.plot(d, r, 'o', label='Sr-90 beta source')

if len(sys.argv) == 1:
	print('activities:', popt[0], popt[2])
	print('CoA:', popt[1]*1e6, popt[3]*1e6)
	densityAl = 2710
	print('MCoA:', popt[1]*1e6/densityAl, popt[3]*1e6/densityAl)
	plt.show()
else:
	plt.savefig(sys.argv[1])
