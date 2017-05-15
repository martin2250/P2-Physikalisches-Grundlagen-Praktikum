#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import scipy.optimize
import matplotlib
from matplotlib import pyplot as plt
import sys

d, N, t = np.loadtxt('source/4.1.dat', unpack=True)

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

def expon(x, a, b):
	return a*np.exp(-b*x)

#left setup: mean 0.352941176471 cps, std: 0.578148817661 cps

#correction constants
l_br=0.3529
#corrections
N = N/t		#average
N=N-l_br	#background radiation


plt.xlabel('distance in $\si{\milli\meter}$')
plt.ylabel('Activity in Events/$\si{\second}$')

popt, pconv = scipy.optimize.curve_fit(expon, d, N)

plt.plot(d, expon(d, popt[0], popt[1]))
plt.plot(d, N, 'o')
plt.text(18, 3.8, ('$N(d)=ae^{-bd}$\n$a=%.2f, b=%.2f\si{\milli\meter}^{-1}$' %(popt[0], popt[1])))


if len(sys.argv) == 1:
	print("fit parameters: a=" + str(popt[0]) + ", b=" + str(popt[1]))
	plt.show()
else:
	plt.savefig(sys.argv[1], format='pdf')
