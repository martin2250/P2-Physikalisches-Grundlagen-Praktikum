#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys

matplotlib.rcParams.update({'font.size': 12})

v0 = 0.3
dv = 0.4
p0 = 0.3
dp1 = 0.4
dp2 = 0.15
k=1
lw=5

arrowprops=dict(facecolor='black', shrink=0.05)

plt.xlim(0.075, 0.8)
plt.ylim(0.15, 0.75)

plt.xlabel('Volume $V$')
plt.ylabel('Pressure $p(V)$')

plt.axhline(p0, ls='--', lw=0.8)
plt.yticks([p0], ['$p_0$'])

plt.axvline(v0, ls='--', lw=0.8)
plt.xticks([v0], ['$V_0$'])

#pV^k = const
P = np.linspace(p0+dp1, p0, 20)
V = ((p0+dp1)/P)**(1/k)*v0
plt.plot(V, P, lw=lw)
plt.annotate('venting\n$pV^k=const$', xy=(V[10], P[10]), xytext=(0.54, 0.54), arrowprops=arrowprops)


plt.text(v0 + 0.0125, p0+dp1, '$(V_0, p_0+dp_1, T_0)$')

#clsong valve
plt.plot([V[-1], v0], [p0, p0], lw=lw)
plt.annotate('closing valve', xy=(np.mean([V[-1], v0]), p0), xytext=(0.4, 0.175), arrowprops=arrowprops)

plt.text(V[-1] - 0.025, p0 - 0.05, '$(V_0 + dV, p_0, T_0 - dT)$', ha='center')

#heating up
plt.plot([v0, v0], [p0, p0+dp2], lw=lw)
plt.annotate('re-heating', xy=(v0, p0+dp2/2), xytext=(0.4, 0.33), arrowprops=arrowprops)

plt.text(v0 - 0.0125, p0 + 0.01, '$(V_0, p_0, T_0 - dT)$', ha='right')

plt.plot([v0, V[-1], v0, v0], [p0+dp1, p0, p0, p0+dp2], 'ok')

plt.text(v0 - 0.0125, p0 + dp2, '$(V_0, p_0 + dp_2, T_0)$', ha='right')

if len(sys.argv) == 1:
	plt.show()
else:
	plt.savefig(sys.argv[1])
