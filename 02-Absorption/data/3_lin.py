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

d1 = d[:9]
r1 = r[:9]

d2 = d[9:-1]
r2 = r[9:-1]

slope1, intercept1, rr, p, stderr = linregress(d1, r1)
slope2, intercept2, rr, p, stderr = linregress(d2, r2)

X1 = np.linspace(d1[0], d1[len(d1)-1], 30)
X2 = np.linspace(d2[0], d2[len(d2)-1], 30)

plt.plot(d, r, 'o', label='Sr-90 beta source')

plt.plot(X1, intercept1 + X1 * slope1, 'r')
plt.plot(X2, intercept2 + X2 * slope2, 'r')

matplotlib.rc('text', usetex = True)
plt.xlabel('Thickness $d$ in microns')
plt.ylabel('Activity in Events / s')
plt.grid(which="both")

ax = plt.gca()
#ax.set_yscale('log')
#ax.set_xscale('log')


if len(sys.argv) == 1:
	plt.show()
else:
	plt.savefig(sys.argv[1])
