#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import sys

wavelength = 633e-6 #in mm

if len(sys.argv) < 2:
	print('specify an input file')
	exit(1)

I = np.loadtxt(sys.argv[1]).T

L = I[0]*1e3	#distance to screen in mm
D = I[1:].T		#distance between mins in mm

O = np.arange(0, D.shape[1])	#order

A = D.copy()	#angles
for i in range(0, len(L)):
	A[i] = A[i] / L[i]

S = L.copy()	#slopes (angle over order)
for i in range(0, len(L)):
	S[i], intercept, r, p, stderr = linregress(O, A[i])

W = [2 * wavelength / s for s in S]	#slit width
print(W)

if len(sys.argv) == 3:
	for i in range(0, len(L)):
		plt.plot(O, D[i], label='%d'%i)
	plt.legend()

	if sys.argv[2] == 'show':
		plt.show()
	else:
		plt.savefig(sys.argv[2])
