#!/usr/bin/python
from __future__ import print_function
from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats

if len(sys.argv) < 3:
	print('motherfucker')
	print('./piezo-shitty-file-name.py [input file] [y-axis unit] <output file>')
	exit(1)

data  = np.load(sys.argv[1])['arr_0']
data = data.T

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

plt.plot(data[0], data[1], color='red')
plt.grid()

plt.xlabel("time in \\si{\\milli\\second}")
plt.ylabel("voltage in \\si{\\%s}"%sys.argv[2])

if len(sys.argv) == 3:
	plt.show()
else:
    plt.savefig(sys.argv[3])
