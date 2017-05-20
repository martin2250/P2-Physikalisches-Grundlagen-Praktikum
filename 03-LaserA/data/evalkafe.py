#!/usr/bin/python
import kafe
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys
from kafe.function_library import linear_2par

wavelength = 633e-6 #in mm

if len(sys.argv) < 2:
	print('specify an input file')
	exit(1)

I = np.loadtxt(sys.argv[1]).T

L = I[0]*1e3	#distance to screen in mm
D = I[1:].T		#distance between mins in mm

sort = np.argsort(-L)
L = L[sort]
D = D[sort]

O = np.arange(0, D.shape[1])	#order

A = D.copy()	#angles
for i in range(0, len(L)):
	A[i] = D[i] / L[i]

#throw out second line for datasets with two equal lines
#this makes dealing with single line files easier, since the arrays would not only have different sizes, but also different shapes
if np.array_equal(A[0], A[1]):
	A = A[:1]
	L = L[:1]

d_err = 1					#assume 1mm error on d
a_err = [d_err / l for l in L]

Fits = []
AoverO = np.zeros(len(L))
Aoffset = np.zeros(len(L))
AoverOerr = np.zeros(len(L))

for i in range(0, len(L)):
	dataset = kafe.Dataset(data=(O, A[i]))
	dataset.add_error_source('y', 'simple', a_err[i])

	fit = kafe.Fit(dataset, linear_2par)
	fit.do_fit(quiet=True)
	Fits = Fits + [fit]

	AoverO[i] = fit.final_parameter_values[0]
	Aoffset[i] = fit.final_parameter_values[1]
	AoverOerr[i] = fit.final_parameter_errors[1]


if len(sys.argv) == 3:

	if sys.argv[2] != 'data':


		matplotlib.rc('text', usetex = True)
		params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
		plt.rcParams.update(params)

		for i in range(0, len(L)):
			plt.errorbar(O, D[i],fmt='.', yerr=d_err, label='$D_\\text{screen} = \\SI{%0.2f}{\\meter}$'%(L[i]*1e-3))

			X = np.array([0, O[-1]])
			plt.plot(X, L[i]*linear_2par(X, AoverO[i], Aoffset[i]), color='#999999', ls='--', lw=1., label='Linear Fit' if i==0 else None)

		plt.legend() #only for fixing datasets with missing orders
		plt.xlabel('Order')
		plt.ylabel('Distance between Features (\\si{\\mm})')

		if sys.argv[2] == 'show':
			plt.show()
		else:
			plt.savefig(sys.argv[2])


	else:
		print('Fit Slopes:', AoverO)
		print('Slope Errors:', AoverOerr)
		print('in rad/order')

		print('latex table:')
		print('(angle/order)	(error on #0)	(feature size [um])	(error on #2)')

		fmt = '\\num{%0.2e}&	\\num{%0.2e}&	\\num{%0.0f}&	\\num{%0.2f}\\\\'

		for i in range(0, len(L)):
			featuresize = 2 * wavelength / AoverO[i]
			fserror = AoverOerr[i] * featuresize / AoverO[i]

			print(fmt%(AoverO[i], AoverOerr[i], featuresize*1e3, fserror * 1e3))
