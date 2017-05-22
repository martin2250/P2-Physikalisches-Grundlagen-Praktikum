#!/usr/bin/python
import kafe
import numpy as np
import sys
from kafe.function_library import linear_2par

def frexp10(x):
	exp = int(np.log10(x)) - 1
	return x / 10**exp, exp

def formatUC(x, err, sig=2):
	fmt = '%%0.%df(%%%d.0f)e%%d'%(sig, sig)
	man, exp = frexp10(x)
	errman = err*10**(sig-exp)
	return fmt%(man, errman, exp)

def mixcase(s):
	return ''.join([c.upper() if np.random.randint(0,2) else c.lower() for c in s])

XKCD = True

wavelength = 632.816e-6 #in mm

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
L_err = 10

Fits = []
AoverO = np.zeros(len(L))
Aoffset = np.zeros(len(L))
AoverOerr = np.zeros(len(L))

for i in range(0, len(L)):
	dataset = kafe.Dataset(data=(O, A[i]))

	a_err = np.sqrt((A[i] * L_err/L[i])**2 + (d_err / L[i])**2)
	dataset.add_error_source('y', 'simple', a_err)

	fit = kafe.Fit(dataset, linear_2par)
	fit.do_fit(quiet=True)
	Fits = Fits + [fit]

	AoverO[i] = fit.final_parameter_values[0]/2
	Aoffset[i] = fit.final_parameter_values[1]
	AoverOerr[i] = fit.final_parameter_errors[1]/2


if len(sys.argv) >= 3:

	if sys.argv[2] != 'data':
		import matplotlib.pyplot as plt
		import matplotlib

		if XKCD:
			plt.xkcd()
			pointlabel = lambda: mixcase('D = %0.2f m')
		else:
			print('boring!')
			matplotlib.rc('text', usetex = True)
			params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
			plt.rcParams.update(params)
			pointlabel = lambda: '$D_\\text{screen} = \\SI{%0.2f}{\\meter}$'

		for i in range(0, len(L)):
			plt.errorbar(O, D[i],fmt='.', yerr=d_err, label=pointlabel()%(L[i]*1e-3))

			X = np.array([0, O[-1]])
			plt.plot(X, L[i]*linear_2par(X, AoverO[i]*2, Aoffset[i]), color='#999999', ls='--', lw=1., label='Linear Fit' if i==0 else None)

		plt.legend() #only for fixing datasets with missing orders
		plt.xlabel('Order')
		if XKCD:
			plt.ylabel('Distance bEtweEn FeaturEs (mM)')
		else:
			plt.ylabel('Distance between Features (\\si{\\mm})')


		if sys.argv[2] == 'show':
			plt.show()
		else:
			plt.savefig(sys.argv[2])


	else:
		print('latex table:')
		print('(D_screen)	(angle/order)	(feature size [um])')

		for i in range(0, len(L)):
			featuresize = wavelength / AoverO[i]
			fserror = AoverOerr[i] * featuresize / AoverO[i]

			fmt = '%0.2f&	%s&	%s\\\\'
			print(fmt%(L[i]*1e-3, formatUC(AoverO[i], AoverOerr[i]), formatUC(featuresize*1e-3, fserror*1e-3)))

		print('\\midrule')

		meanAoO = np.average(AoverO, weights=AoverOerr**-2)
		merr = np.sqrt(1./np.sum(AoverOerr**-2))
		meanfeaturesize = wavelength / meanAoO
		meanfeatureerror = merr * meanfeaturesize / meanAoO

		fmt = '{mean}&	%s&	%s\\\\'
		print(fmt%(formatUC(meanAoO, merr), formatUC(meanfeaturesize*1e-3, meanfeatureerror*1e-3)))
