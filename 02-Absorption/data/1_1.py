#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import linregress
import sys

U, NL, NR = np.loadtxt('source/1.1.dat', unpack=True)

#30 second average
NL = NL / 30
NR = NR / 30

matplotlib.rc('text', usetex = True)
plt.xlabel('operating voltage $U$ in V')
plt.ylabel('count rate in events / s')

plt.plot(U, NL, 'o', label='left setup')
plt.plot(U, NR, 'o', label='right setup')
plt.legend()

#determine plateau slope
UL = U[4:]
UR = U[2:]

NL = NL[4:]
NR = NR[2:]

slopeL, interceptL, r, p, stderr = linregress(UL, NL)
slopeR, interceptR, r, p, stderr = linregress(UR, NR)

XL = np.array([320, 450])
XR = np.array([310, 450])

plt.plot(XL, XL * slopeL + interceptL)
plt.plot(XR, XR * slopeR + interceptR)

if len(sys.argv) == 1:
	print('left slope:', slopeL, 'cps/V')
	print('right slope:', slopeR, 'cps/V')
	plt.show()
else:
	plt.savefig(sys.argv[1])
