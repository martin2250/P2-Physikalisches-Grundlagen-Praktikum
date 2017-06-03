#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats

(P) = np.loadtxt('source/5.dat', unpack=True)

N = np.arange(len(P))
X = np.array([N[0], N[-1]])

slope, intercept, r, p, stderr = scipy.stats.linregress(N, P)

plt.xkcd()

plt.plot(X, X * slope + intercept)
plt.plot(N, P, 'or')

plt.xlabel('Times Vented')
plt.ylabel('Pressure')

if len(sys.argv) == 1:
	print('slope:', slope, 'mBar/vent')
	print('intercept:', intercept, 'mBar')
	plt.show()
else:
	plt.savefig(sys.argv[1])
