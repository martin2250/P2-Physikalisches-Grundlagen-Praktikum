#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys
import scipy.signal

T, U = np.loadtxt('source/superconductor.dat', unpack=True)

T=T+273.15	#to kelvin
R=U/0.063

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

plt.grid()
plt.plot(T, R, 'ro')
plt.xlabel("T in \\si{\\kelvin}")
plt.ylabel("R in \\si{\\ohm}")

maxdiff=0
maxindex=None
valueatmax=None

for i in range(0, len(U)-1):
	
	diff=np.abs(R[i]-R[i+1])
	if maxdiff<diff:
		maxdiff=diff
		maxindex = i
		valueatmax=T[i]



if len(sys.argv) == 1:
	plt.show()
	print("edge of dR= ", maxdiff, "at T[",maxindex, "]= ",valueatmax)
else:
	plt.savefig(sys.argv[1])
