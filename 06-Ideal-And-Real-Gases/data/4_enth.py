#!/usr/bin/python
from __future__ import print_function
from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats

(T_heat, h_heat) = np.loadtxt('source/4_b.dat', unpack=True)
(T_cool, h_cool) = np.loadtxt('source/4_a.dat', unpack=True)

#22.12 shift
h_cool = h_cool - 22.12
h_heat = h_heat - 22.12
h_cool = h_cool*1e-2
h_heat = h_heat*1e-2

#SI rocks
T_heat = T_heat+273.15
T_cool = T_cool+273.15

#calculate pressure
p_cool = h_cool*1.3332e5+996	#hPa
p_heat = h_heat*1.3332e5+996	#hPa

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

a_cool, b_cool, r_cool, pv_cool, stderr_cool = scipy.stats.linregress(np.reciprocal(T_cool), np.log(p_cool))
a_heat, b_heat, r_heat, pv_heat, stderr_heat = scipy.stats.linregress(np.reciprocal(T_heat), np.log(p_heat))

plt.plot(np.reciprocal(T_cool), p_cool, 'bo', label='Cooling')
plt.plot(np.reciprocal(T_heat), p_heat, 'ro', label='Heating')


T=np.linspace(np.reciprocal(T_cool)[-1], np.reciprocal(T_cool)[0], 1000)
plt.plot(T, np.exp(a_cool*T+b_cool), label='Fit for cooling')
plt.plot(T, np.exp(a_heat*T+b_heat), label='Fit for heating')

mT_cool = np.mean(np.reciprocal(T_cool))
mT_heat = np.mean(np.reciprocal(T_heat))

#plt.xkcd()
ax=plt.gca()
ax.grid()
#ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel('Inverse temperature in \\si{\\per\\kelvin}')
plt.ylabel('Logarithmic pressure in \\si{\\hecto\\pascal}')

plt.legend(loc=1)

if len(sys.argv) == 1:
	plt.show()
	print("a_cool= (", a_cool, "+/-", stderr_cool, "), b_cool= ", b_cool, ", r_cool= ", r_cool)
	print("a_heat= (", a_heat, "+/-", stderr_heat, "), b_heat= ", b_heat, ", r_heat= ", r_heat)
else:
    plt.savefig(sys.argv[1])
 
