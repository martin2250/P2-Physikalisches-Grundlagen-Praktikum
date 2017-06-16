#!/usr/bin/python
from __future__ import print_function
from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats

(f, Vin, Vout, Vinc, Voutc) = np.loadtxt('source/1_4.dat', unpack=True)

f_lin=np.exp(np.linspace(np.log(2.8), np.log(100e3), 50))

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

#plt.xkcd()
ax=plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')	#aaalways use log-log for frequency responses

def amp(A, B):
    return (B*1e3)/A

def high_from_a_spliff(f, tau, A0):
    return A0 / np.sqrt( 1 + 1/(2*np.pi*f*tau)**2 )

popt, pconv = scipy.optimize.curve_fit(high_from_a_spliff, f, amp(Vinc, Voutc), p0=[1e-3, 250])

plt.plot(f, amp(Vin, Vout), 'bo', label='$A$ without $C_\\text{E}$')
plt.plot(f, amp(Vinc, Voutc), 'ro', label='$A$ with $C_\\text{E}$')

plt.plot(f_lin, high_from_a_spliff(f_lin, popt[0], popt[1]), label='$A_\\text{highpass}$')

plt.xlabel('Frequency in \\si{\\hertz}')
plt.ylabel('Amplification')

plt.legend(loc=2)

if len(sys.argv) == 1:
	print("tau = ", popt[0]*1e6, "e-6")
	print("A0 = ", popt[1])
	plt.show()
else:
    plt.savefig(sys.argv[1])
