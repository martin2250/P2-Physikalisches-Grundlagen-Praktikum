#!/usr/bin/python
from __future__ import print_function
from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats

(L, I) = np.loadtxt('source/phototranny.dat', unpack=True)

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

plt.plot(L, I, 'ro')

plt.grid()
plt.xlabel('Luminosity in \\si{\\lux}')
plt.ylabel('Reverse current in \\si{\\milli\\ampere}')

if len(sys.argv) == 1:
	plt.show()
else:
    plt.savefig(sys.argv[1])
