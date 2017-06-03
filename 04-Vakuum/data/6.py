#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats

(P, Ui, Uh) = np.loadtxt('source/6.dat', unpack=True)

#plt.xkcd()

ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')

plt.grid(which='both')

plt.plot(P, Ui, 'bo')
plt.plot(P, Uh, 'ro')

plt.xlabel('Pressure')
plt.ylabel('Voltage')

if len(sys.argv) == 1:
	plt.show()
else:
	plt.savefig(sys.argv[1])
