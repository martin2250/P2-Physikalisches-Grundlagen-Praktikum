#!/usr/bin/python
from __future__ import print_function, division
import kafe
import numpy as np
import matplotlib.pyplot as plt
import sys

#T: temperature, Rp: potentiometer resistance, Rr: reference resistance
(Tn, Rpn, Rrn) = np.loadtxt('source/ntc.dat', unpack=True)
(Tp, Rpp, Rrp) = np.loadtxt('source/pt100.dat', unpack=True)

Rn = 1e3*Rrn*(10-Rpn)/Rpn	#because f*** consistency
Rp = Rrp*(10-Rpp)/Rpp

@kafe.FitFunction
def pt100_fit(T, R0=100.0, alpha=4e-3):
    return R0 * (1 + T * alpha)

@kafe.FitFunction
def ntc_fit(T, R0=0.03, alpha=3.6e3):
    return R0 * np.exp(alpha/(T + 273.15))

# temperror = 5.
# reserror = 0.05

datan = kafe.Dataset(data=(Tn, Rn))
# datan.add_error_source('x', 'simple', temperror)
# datan.add_error_source('y', 'simple', reserror, relative=True)
datap = kafe.Dataset(data=(Tp, Rp))
# datap.add_error_source('x', 'simple', temperror)
# datap.add_error_source('y', 'simple', reserror, relative=True)

fitp = kafe.Fit(datap, pt100_fit)
fitp.do_fit(quiet=True)
fitn = kafe.Fit(datan, ntc_fit)
fitn.do_fit(quiet=True)

(R0n, alphan) = fitn.final_parameter_values
(R0en, alphaen) = fitn.final_parameter_errors
(R0p, alphap) = fitp.final_parameter_values
(R0ep, alphaep) = fitp.final_parameter_errors

Xp = np.linspace(60, 210, 70)
Xn = np.linspace(75, 210, 70)

plt.plot(Xn, ntc_fit(Xn, R0n, alphan), color='#78D6F5')
plt.plot(Xp, pt100_fit(Xp, R0p, alphap), color='#E3D72D')

plt.plot(Tn, Rn, 'ob', label='NTC')
plt.plot(Tp, Rp, 'or', label='PT100')

plt.legend()
plt.grid()
plt.xlabel(u'Temperature $T$ (in \u00B0C)')
plt.ylabel(u'Resistance $R$ (in \u03A9)')

if len(sys.argv) == 1:
	print('PT100:')
	print(u'R\u2080:', R0p, u'\n    \u00B1', R0ep)
	print(u'\u03B1: %e\n \u00B1 %e'%(alphap, alphaep))
	print('')
	print('NTC:')
	print(u'R\u2080:', R0n, u'\n  \u00B1', R0en)
	print(u'\u03B1:', alphan, u'\n    \u00B1', alphaen)
	plt.show()
else:
	plt.savefig(sys.argv[1])
