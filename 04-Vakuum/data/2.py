#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats

(t, T1, T2) = np.loadtxt('source/2.dat', unpack=True)

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

#plt.xkcd()

ax = plt.gca()
ax.set_yscale('log')

a1, b1, r, p, stderr = scipy.stats.linregress(t, np.log(T1))
a2, b2, r, p, stderr = scipy.stats.linregress(t, np.log(T2))

plt.plot(t, np.exp(a1*t+b1), label=('fit of T1, $a_1=%.4f\\si{\\second}^{-1}$' % a1))
plt.plot(t, np.exp(a2*t+b2), label=('fit of T2, $a_2=%.4f\\si{\\second}^{-1}$' % a2))

plt.plot(t, T1, 'bo', label='$T_1$')
plt.plot(t, T2, 'ro', label='$T_2$')

plt.xlabel('Time in \\si{\\second}')
plt.ylabel('Pressure in \\si{\\milli\\bar}')

plt.legend()

if len(sys.argv) == 1:
	plt.show()
else:
	plt.savefig(sys.argv[1])
