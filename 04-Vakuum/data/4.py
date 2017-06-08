#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats

(t, IM) = np.loadtxt('source/4.dat', unpack=True)

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

#plt.xkcd()

ax = plt.gca()
ax.set_yscale('log')
extraticks=[0.5, 5]
ax.set_yticks(list(ax.get_yticks()) + extraticks)

a2, b2, r, p, stderr = scipy.stats.linregress(t[:6], np.log(IM[:6]))

plt.plot(t[:6], np.exp(a2*t[:6]+b2), zorder=2, label=('fit, $a=%.4f\\si{\\second}^{-1}$' % a2))

plt.plot(t, IM, 'bo', label='$T_1$', zorder=1)

plt.xlabel('Time in \\si{\\second}')
plt.ylabel('Pressure in \\si{\\milli\\bar}')

plt.text(-29.5,0.48, "$0.5$")
plt.text(-25,4.8, "$5$")
plt.legend()

if len(sys.argv) == 1:
	plt.show()
else:
	plt.savefig(sys.argv[1])
