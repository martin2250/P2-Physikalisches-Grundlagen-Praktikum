#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import linregress
import sys

N = 11
means = np.zeros(N)
stdevs = np.zeros(N)

for i in range(0, N):
	n, data = np.loadtxt('source/1_4/R_1.4_%02d.dat'%i, unpack=True)
	means[i] = np.mean(data)
	stdevs[i] = np.std(data)

ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
matplotlib.rc('text', usetex = True)
plt.xlabel('Distance $d$ in inches')
plt.ylabel('Activity in Events / s')
plt.grid(which="both")

d = np.arange(0, N)
d = d * 10 + 28
d = d / 25.4

plt.errorbar(d, means, fmt='o', yerr=stdevs, label='Sr-90 $\\beta$ source')

slope, intercept, r, p, stderr = linregress(np.log(d), np.log(means))
Xfit = np.log(np.array([d[0], d[N-1]]))
Yfit = intercept + Xfit * slope
Xfit = np.exp(Xfit)
Yfit = np.exp(Yfit)
plt.plot(Xfit, Yfit)

plt.legend()

if len(sys.argv) == 1:
	print('slope:', slope)
	plt.show()
else:
	plt.savefig(sys.argv[1])
