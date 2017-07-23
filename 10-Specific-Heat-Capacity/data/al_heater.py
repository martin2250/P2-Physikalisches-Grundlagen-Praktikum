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
t, U1, T = np.loadtxt('source/al-warm-up-no-shitty-encoding-errors.dat', unpack=True)

t = t[90:] #began warming up at 90th data point #no workout tho
t = t - t[0] #get rid of the time offset

#transform voltage into temperature using calcTemp defined above
T = calcTemp(U1)
T = T[90:]
#curve fit
def warmUpFunc(t, a, b, c):
	return a*(t**b)+c

popt, pconv = scipy.optimize.curve_fit(warmUpFunc, t, T)
t_lin=np.linspace(t[0], t[-1], 1000)
plt.plot(t_lin, warmUpFunc(t_lin, popt[0], popt[1], popt[2]), label='fit\n$T(t)=a\cdot t^b + c$\n$a = %.2f°C\ s^{-1}, b = %.2f, c = %.2f°C$' %(popt[0], popt[1], popt[2]), zorder=2)

#data points
plt.plot(t, T, '+', zorder=1, label='data')

plt.title("With heater")
plt.xlabel("time in s")
plt.ylabel("temperature in °C")
plt.legend()
plt.grid()
#------------- ACTUAL DATA ANALYSIS END----------------------------

if len(sys.argv) == 2:
	plt.savefig(sys.argv[1])
else:
	plt.show()
