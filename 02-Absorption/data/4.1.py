#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import scipy.optimize
import matplotlib
from matplotlib import pyplot as plt
import sys

d, N, t = np.loadtxt('source/4.1.dat', unpack=True)

def expon(x, a, b):
	return a*np.exp(-b*x)

#left setup: mean 0.352941176471 cps, std: 0.578148817661 cps

#correction constants
l_br=0.3529
#corrections
N = N/t		#average
N=N-l_br	#background radiation

matplotlib.rc('text', usetex = True)
plt.xlabel('distance in mm')
plt.ylabel('Activity in Events / s')

popt, pconv = scipy.optimize.curve_fit(expon, d, N)

plt.plot(d, expon(d, popt[0], popt[1]))
plt.plot(d, N, 'o')
plt.text(18, 4.15, ('N(d)=a*exp(-b*d)\na=%.2f, b=%.2f' %(popt[0], popt[1])))


if len(sys.argv) == 1:
	print("fit parameters: a=" + str(popt[0]) + ", b=" + str(popt[1]))
	plt.show()
else:
	plt.savefig(sys.argv[1], format='pdf')
	print("fit parameters: a=" + str(popt[0]) + ", b=" + str(popt[1]))
