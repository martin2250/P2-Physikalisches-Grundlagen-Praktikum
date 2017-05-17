#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import scipy.optimize
import matplotlib
from matplotlib import pyplot as plt
import sys

d, N, t = np.loadtxt('source/2.dat', unpack=True)

def expon(x, a, b):
	return a*np.exp(-b*x)

#left setup: mean 0.352941176471 cps, std: 0.578148817661 cps

#correction constants
r=12e-3
d_mm=d*1e-3
omega=4*(r**2/d_mm**2)
l_br=0.3529
t_dead=263.4e-6

#corrections
N = N/t		#average
N=0.98*N 	#parasitic gamma radiation
N=N/(1-N*t_dead)	#dead time
N=N*omega	#solid angle
N=N-l_br	#background radiation

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

plt.xlabel('distance in \si{\milli\meter}')
plt.ylabel('Activity in Events / s')

#popt, pconv = scipy.optimize.curve_fit(expon, d_mm, N)

#plt.plot(d_mm, expon(d_mm, popt[0], popt[1]))
plt.plot(d, N, 'o', label='Am-241 source')
plt.grid()
plt.legend()
#plt.text(0.025, 300, ('N(d)=a*exp(-b*d)\na=%.2f, b=%.2f' %(popt[0], popt[1])))


if len(sys.argv) == 1:
	#print("fit parameters: a=" + str(popt[0]) + ", b=" + str(popt[1]))
	plt.show()
else:
	plt.savefig(sys.argv[1], format='pdf')
