#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys
import scipy.signal

# usage:
# ./curve-plotter.py <output file> ([data file] [legend label])xN
# will show or save plot based on even/odd number of args
# to specify a color use a label like "<r>LED red"

def load(path):
	A = np.load(path)['arr_0'][:,1:]
	#remove all (x y) where x or y is infinite
	A = np.array([x for x in A if (np.isfinite(x[0]) and np.isfinite(x[1]))])
	A = A.T
	return A[1], A[0]	#U(voltage, volt), I(current, mA)


args = sys.argv[1:]
outputfile = None

if len(args) % 2:
	outputfile = args[0]
	args = args[1:]

for num in range(int(len(args)/2)):
	U, I = load(args[2*num])
	#i = np.argsort(U)
	#U = U[i]
	#I = I[i]

	lbl = args[2*num + 1]
	color = None
	if lbl[0] == '<':
		lbl = lbl[1:]
		s = lbl.rsplit('>', 1)
		color = s[0]
		lbl = s[1]
		print(color, lbl)

	plt.plot(U, I, label=lbl, color=color)

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

plt.grid()
plt.legend(loc=2, ncol=2, title="Luminosity in \\si{\\lux}")

ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.annotate('Voltage $U$ (V)', xy=(0.5, -.05), ha='center', va='top', xycoords='axes fraction', fontsize=12)
ax.annotate('Current $I$ (mA)', xy=(0, 0.5), ha='right', va='center', rotation='vertical', xycoords='axes fraction', fontsize=12)

if outputfile != None:
	plt.savefig(outputfile)
else:
	plt.show()
