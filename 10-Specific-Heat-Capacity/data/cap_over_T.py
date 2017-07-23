#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import sys

def T_func_heater(T, a, b, c):
	return a*b * ((T-c) / a)**((b-1) / b)

def T_func_no_heater(T, a, c):
	return c*(a-T)

def cap(T, P, m):
	return P / (m * (T_func_heater(T, 1.06, 0.67, -197)-T_func_no_heater(T, 22.25, 0.00005)))

T = np.linspace(-150, 50, 1000)

plt.plot(T, cap(T, 2.01*11.1, 338))

plt.grid()
plt.xlabel("temperature in °C")
plt.ylabel("specific heat capacity in $\\mathrm{\\frac{J}{gK}}$")

if len(sys.argv) == 2:
	plt.savefig(sys.argv[1])
else:
	print("c(20)=", cap(20, 2.01*11.1, 338))
	plt.show()
