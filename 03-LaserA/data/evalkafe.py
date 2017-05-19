#!/usr/bin/python
import kafe
import numpy as np
import matplotlib.pyplot as plt
import sys
from kafe.function_library import linear_2par

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


d_err = 0.5						#assume 0.5mm error on d
a_err = [d_err / l for l in L]

for i in range(0, len(L)):
	dataset = kafe.Dataset(data=(O, A[i]))
	dataset.add_error_source('y', 'simple', a_err[i])
	fit = kafe.Fit(dataset, linear_2par)
	fit.do_fit(quiet=True)
	print(fit.final_parameter_values)
	print(fit.final_parameter_errors)
