#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import scipy.optimize
import matplotlib
from matplotlib import pyplot as plt
import sys

d, N, t = np.loadtxt('source/4.2.dat', unpack=True)

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

def expon(x, a, b):
	return a*np.exp(-b*x)

#left setup: mean 0.352941176471 cps, std: 0.578148817661 cps

#correction constants
l_br=0.3529
t_dead=263.4e-6
#corrections
N = N/t		#average
N=N/(1-N*t_dead)	#dead time
N=N-l_br	#background radiation


plt.xlabel('thickness in $\si{\milli\meter}$')
plt.ylabel('Activity in Events/$\si{\second}$')

popt, pconv = scipy.optimize.curve_fit(expon, d, N)

plt.plot(d, expon(d, popt[0], popt[1]))
plt.plot(d, N, 'o', label='Cs-137 source')
plt.text(17.5, 3.4, ('$N(d)=ae^{-bd}$\n$a=%.2f, b=%.3f\si{\milli\meter}^{-1}$' %(popt[0], popt[1])))

plt.legend()
plt.grid()

if len(sys.argv) == 1:
	print("fit parameters: a=" + str(popt[0]) + ", b=" + str(popt[1]))
	plt.show()
else:
	plt.savefig(sys.argv[1], format='pdf')
