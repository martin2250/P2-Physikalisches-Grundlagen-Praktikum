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

dP = P[1:] - P[:-1]
barX = np.arange(len(dP)) + 0.5

plt.xkcd()

ax1 = plt.gca()
ax2 = ax1.twinx()

ax2.plot(X, X * slope + intercept)
ax2.plot(N, P, 'or')
ax1.bar(barX, dP, alpha=0.2, color='g')

plt.xlabel('Times Vented')
ax2.set_ylabel('PresSure P (mBar)')
ax1.set_ylabel('PreSsure DiFferEnce dP (mBar)')

if len(sys.argv) == 1:
	print('slope:', slope, 'mBar/vent')
	print('intercept:', intercept, 'mBar')
	plt.show()
else:
	plt.savefig(sys.argv[1])
