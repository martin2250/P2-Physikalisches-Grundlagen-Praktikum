#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import sys

N = 11
means = np.zeros(N)
stdevs = np.zeros(N)

for i in range(0, N):
#	n, data = np.laodtxt("filename", unpack=True)
	#means[i] = np.mean(data)
	#stdevs[i] = np.std(data)
	pass

matplotlib.rc('text', usetex = True)
plt.xlabel('Distance $d$ in inches')
plt.ylabel('Activity in Events / s')

d = np.arange(0, N)
d = d * 10 + 50
d = d / 25.4

plt.plot(d, means)
plt.plot(d, stdevs)

if len(sys.argv) == 1:
	plt.show()
else:
	plt.savefig(sys.argv[2], format='pdf')
