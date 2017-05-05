#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

if not 1 < len(sys.argv) < 4:
	print('usage: %s source.dat [target.pdf]\n\t\t...dickhead.'%sys.argv[0])
	sys.exit()

(deg, U) = np.loadtxt(sys.argv[1], unpack=True)

N = 37
theta = np.linspace(0.0, 2 * np.pi, N)

ax = plt.subplot(111, projection='polar')
ax.plot(theta, U, color='#ee8d18')

for i in range(0,37):
	print(i, theta[i], U[i])

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

if len(sys.argv)==2:
	plt.show()
else:
	plt.savefig(sys.argv[2], format='pdf')
