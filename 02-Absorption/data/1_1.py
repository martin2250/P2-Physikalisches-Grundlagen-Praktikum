#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import sys

U, NL, NR = np.loadtxt('source/1.1.dat', unpack=True)

#30 second average
NL = NL / 30
NR = NR / 30

matplotlib.rc('text', usetex = True)
plt.xlabel('operating voltage $U$ in V')
plt.ylabel('Activity in Events / s')

plt.plot(U, NL, 'o', label='left setup')
plt.plot(U, NR, 'o', label='right setup')

plt.legend()

if len(sys.argv) == 1:
	plt.show()
else:
	plt.savefig(sys.argv[1], format='pdf')
