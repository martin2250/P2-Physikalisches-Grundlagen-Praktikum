#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import linregress
import scipy
import sys
import matplotlib.ticker as ticker

lamb, u1, u2, u3 = np.loadtxt('source/31.dat', unpack=True)

#conclude into one voltage array
U = np.mean(np.array([u1, u2, u3]), axis=0)

#inverse wavelength for fit
lamb = 1/lamb

#fit
a, b, r, p, std = linregress(lamb, U)
lamb_space = np.linspace(lamb[0], lamb[-1], 500)

#plot
plt.plot(lamb, U, 'ro', label='data')
plt.plot(lamb_space, a*lamb_space+b, label='fit: $U(\lambda)=a\cdot\lambda^{-1}+b$\n$a = %.3f$ Vnm\n$b = %.3f$ V' %(a,b))

plt.xlabel('Inverse wavelength in $\\frac{1}{\mu m}$')
plt.ylabel('Terminal voltage in V')
ax = plt.gca()
ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x*1e3))
ax.xaxis.set_major_formatter(ticks_x)
plt.grid()
plt.legend()

if len(sys.argv) == 1:
	print('a=', a, 'b=', b, 'r_squared=', r)
	plt.show()
else:
	plt.savefig(sys.argv[1])
