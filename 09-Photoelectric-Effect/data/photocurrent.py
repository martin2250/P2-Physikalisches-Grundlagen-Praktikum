#!/usr/bin/python
from __future__ import division, print_function
import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import sys

interactive = len(sys.argv) == 1


##########################################	data
(Us, Unf, Uf) = np.loadtxt('source/33.dat', unpack=True)

Rshunt = 100e6

Inf = Unf/Rshunt * 1e9
If = Uf/Rshunt *1e9
Usnf = Us - Unf
Usf = Us - Uf

##########################################	main plot
plt.plot(Usnf, Inf, '+')
plt.plot(Usf, If, '+')

plt.axis([-2, 5.7, -2.5, 60])
plt.xlabel('Stopping Potential (V)')
plt.ylabel('Photocurrent (nA)')
plt.grid()

ax = plt.gca()
ax.add_patch(Rectangle((-1.65, -0.5), 1.6, 3.8, transform=ax.transData, alpha=1, fill=None))

##########################################	fit function

def fitfunc(x, x0, A, B):
	return A/(1+np.exp(B*(x-x0)))

def makefit(X, Y):
	fit, garbage = scipy.optimize.curve_fit(fitfunc, X, Y, [2, 25, -2])

	x = np.linspace(X[0], X[-1], 60)
	y = fitfunc(x, *fit)
	plt.plot(x, y, zorder=-10, alpha=0.6)

	if interactive:
		print('Plateau Current:', fit[1], 'nA')

makefit(Usnf, Inf)
makefit(Usf, If)
import sys
##########################################	subplot

ax.add_patch(Rectangle((-1.8, 25), 4, 32, transform=ax.transData, alpha=1, facecolor='w', zorder=10))
subax = plt.axes([0.15, 0.5, .35, .35], alpha=1)
subax.yaxis.tick_right()
plt.xlim(-1.65, 0)
maxn = 17
plt.grid()
plt.plot(Usnf[:maxn], Inf[:maxn], '+')
plt.plot(Usf[:maxn], If[:maxn], '+')

##########################################

if interactive:
	plt.show()
else:
	plt.savefig(sys.argv[1])
