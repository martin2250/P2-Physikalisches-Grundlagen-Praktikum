#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
from scipy.stats import linregress
import matplotlib
from matplotlib import pyplot as plt
import sys

rho, N, t = np.loadtxt('source/4.3.dat', unpack=True, usecols=[1,2,3])
materials=np.array(['acrylic glass', 'iron', 'brass', 'aluminium', 'trovidur', 'wood', 'concrete'])

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

#left setup: mean 0.352941176471 cps, std: 0.578148817661 cps

#correction constants
l_br=0.3529
t_dead=263.4e-6
#corrections
N = N/t		#average
N=N/(1-N*t_dead)	#dead time
N=N-l_br	#background radiation


plt.xlabel('rho in $\si{\gram\per\cubic\centi\meter}$')
plt.ylabel('Activity in Events/$\si{\second}$')

slope, intercept, r, p, stderr = linregress(rho, N)

plt.plot(rho, intercept+rho*slope, label='Linear Fit $N(\\rho)=a\\cdot\\rho+b$\n$a=%.2f\\si{\centi\meter}^{-1}, b=%2.f$' %(slope, intercept))

for i in range(0, len(rho)):
	plt.plot(rho[i], N[i], 'o', label=materials[i])

#plt.text(17.5, 3.4, ('$N(d)=ae^{-bd}$\n$a=%.2f, b=%.3f\si{\milli\meter}^{-1}$' %(popt[0], popt[1])))

plt.legend()
plt.grid()

if len(sys.argv) == 1:
	#print("fit parameters: a=" + str(popt[0]) + ", b=" + str(popt[1]))
	plt.show()
else:
	plt.savefig(sys.argv[1], format='pdf')
