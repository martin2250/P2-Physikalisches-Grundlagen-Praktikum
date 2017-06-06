#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats

(t, T1) = np.loadtxt('source/3.dat', unpack=True)

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

#plt.xkcd()

ax = plt.gca()
ax.set_yscale('log')

a1, b1, r, p, stderr = scipy.stats.linregress(t[:8], np.log(T1[:8]))
a2, b2, r, p, stderr = scipy.stats.linregress(t[10:20], np.log(T1[10:20]))
a3, b3, r, p, stderr = scipy.stats.linregress(t[27:], np.log(T1[27:]))

plt.plot(t[:8], np.exp(a1*t[:8]+b1), zorder=2, label=('first fit, $a_1=%.4f\\si{\\second}^{-1}$' % a1))
plt.plot(t[10:20], np.exp(a2*t[10:20]+b2), zorder=2, label=('second fit, $a_2=%.4f\\si{\\second}^{-1}$' % a2))
plt.plot(t[27:], np.exp(a3*t[27:]+b3), zorder=2, label=('third fit, $a_3=%.4f\\si{\\second}^{-1}$' % a3))

plt.plot(t, T1, 'bo', label='$T_1$', zorder=1)

plt.xlabel('Time in \\si{\\second}')
plt.ylabel('Pressure in \\si{\\milli\\bar}')

plt.legend()

if len(sys.argv) == 1:
	plt.show()
else:
	plt.savefig(sys.argv[1])
