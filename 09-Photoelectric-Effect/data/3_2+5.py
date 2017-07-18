#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import linregress
import scipy
import sys
import matplotlib.ticker as ticker

if len(sys.argv) == 1:
	print('usage: ./3_2+5.py input.dat <output.pdf>')

lamb, U= np.loadtxt(sys.argv[1], unpack=True)

#inverse wavelength for fit
lamb = 1/lamb

#fit
a, b, r, p, std = linregress(lamb, U)
lamb_space = np.linspace(lamb[0], lamb[-1], 500)

#plot
plt.plot(lamb, U, '+')
plt.plot(lamb_space, a*lamb_space+b, label='fit: $U(\lambda)=a\cdot\lambda^{-1}+b$\n$a = %.3f$ Vnm\n$b = %.3f$ V' %(a,b))

plt.xlabel('Wavelength in nm')
plt.ylabel('Terminal voltage in V')
ax = plt.gca()
ticks_x = ticker.FuncFormatter(lambda x, pos: '{:0.1f}'.format(1/x))
ax.xaxis.set_major_formatter(ticks_x)
plt.grid()
plt.legend()

if len(sys.argv) == 2:
	print('a=', a, 'b=', b, 'r_squared=', r)
	plt.show()
else:
	plt.savefig(sys.argv[2])
