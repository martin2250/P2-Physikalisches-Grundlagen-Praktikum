#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats

(P, Ui, Uh) = np.loadtxt('source/6.dat', unpack=True)

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

#plt.xkcd()

ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')

plt.grid(which='both')

plt.plot(P, Ui, 'bo', label='$U_\\text{br}$')
plt.plot(P, Uh, 'ro', label='$U_\\text{hold}$')

plt.xlabel('Pressure')
plt.ylabel('Voltage')

plt.legend()

if len(sys.argv) == 1:
	plt.show()
else:
	plt.savefig(sys.argv[1])
