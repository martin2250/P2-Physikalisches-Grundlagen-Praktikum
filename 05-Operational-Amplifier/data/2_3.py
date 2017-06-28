#!/usr/bin/python
from __future__ import print_function
from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats

(f, Vout) = np.loadtxt('source/2_3.dat', unpack=True)
Ve=496e-3

#f_lin=np.exp(np.linspace(np.log(2.8), np.log(100e3), 50))

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

#plt.xkcd()
ax=plt.gca()
ax.grid()
ax.set_xscale('log')
#ax.set_yscale('log')

def amp(Va):
    return 20*np.log10(Va/Ve)

#def high_from_a_spliff(f, tau, A0):
#    return A0 / np.sqrt( 1 + 1/(2*np.pi*f*tau)**2 )

#popt, pconv = scipy.optimize.curve_fit(high_from_a_spliff, f, amp(Vinc, Voutc), p0=[1e-3, 250])
a, b, r, p, stderr = scipy.stats.linregress(f[5:], amp(Vout[5:]))

plt.plot(f*1e3, amp(Vout), 'bo', label='$A$')
#plt.plot(f[5:], a*f[5:]+b, zorder=2)

plt.xlabel('Frequency in \\si{\\hertz}')
plt.ylabel('Amplification in \\si{\decibel}')

plt.legend(loc=1)

if len(sys.argv) == 1:
	#print("tau = ", popt[0]*1e6, "e-6")
	print("f_cut = ", ((18-b)/a))
	plt.show()
else:
    plt.savefig(sys.argv[1])
