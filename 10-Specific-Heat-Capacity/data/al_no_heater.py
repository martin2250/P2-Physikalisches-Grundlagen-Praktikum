#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import linregress
import scipy
import sys

#--------------- CONVERSION OF TEMP <--> VOLTAGE ------------------
temp, U = np.loadtxt('source/type-K-ref.dat', unpack=True)

#fit of temp-volt curve
degree = 15	#might be overkill
p = np.polyfit(U, temp, degree)

def calcTemp(u):

	poly = 0
	for i in range(0, degree):
		poly = poly + p[i]*(u**(degree-i))

	return poly
#--------------- CONVERSION OF TEMP <--> VOLTAGE END---------------

#------------- ACTUAL DATA ANALYSIS -------------------------------
t, U = np.loadtxt('source/al-warm-up-no-heater-and-no-shitty-encoding-errors.dat', unpack=True)

#transform voltage into temperature using calcTemp defined above
T = calcTemp(U)

#curve fit
def warmUpFunc(t, a, b, c):
	return a - (a - b)*np.exp(-c*t)

p0 = np.array([20, calcTemp(-5.785), 0.0001])
popt, pconv = scipy.optimize.curve_fit(warmUpFunc, t, T, p0=p0)
t_lin=np.linspace(t[0], t[-1], 1000)
plt.plot(t_lin, warmUpFunc(t_lin, popt[0], popt[1], popt[2]), label='fit\n$T(t)=a-(a-b)e^{-ct}$\n$a = %.2f°C, b = %.2f°C, c = %.2f\cdot 10^{-6}\ s^{-1}$' %(popt[0], popt[1], popt[2]*1e6), zorder=2)

#data points
plt.plot(t, T, '+', zorder=1, label='data')

plt.title("Without heater")
plt.xlabel("time in s")
plt.ylabel("temperature in °C")
plt.legend()
plt.grid()
#------------- ACTUAL DATA ANALYSIS END----------------------------

if len(sys.argv) == 2:
	plt.savefig(sys.argv[1])
else:
	plt.show()
