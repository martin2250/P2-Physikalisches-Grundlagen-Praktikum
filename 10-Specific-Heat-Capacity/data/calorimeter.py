#!/usr/bin/python
from __future__ import print_function, division
import numpy as np

#	units:
#	temperature: degree celsius
#	mass: grams

m0 = 240.15		#	mass empty, grams
Ccal = 44.25	#	calorimeter total heat capacity, J/K
cw = 4.187		#	water heat capacity, J/(g*K)

materials = ['aluminium', 'copper   ']
lit = np.array([0.897, 0.385])	#	literature values, J/(g*K)

(mi, mc, mh, Tc, Th, Tmix) = np.loadtxt('source/calorimeter.dat',  unpack=True)

mi = mi.astype(int)	#	material index
lit = lit[mi]

mc -= m0		#	cold mass
mh -= m0 + mc	#	hot mass

c = (cw * mc + Ccal) * (Tmix - Tc) / (mh * (Th - Tmix))

dev = (c / lit - 1) * 100

for i in range(len(mc)):
	print(materials[mi[i]], end=' &')

	print('\t%0.1f'%mc[i], end=' &')
	print('\t%0.1f'%mh[i], end=' &')

	print('\t%0.1f'%Tc[i], end=' &')
	print('\t%0.1f'%Th[i], end=' &')
	print('\t%0.1f'%Tmix[i], end=' &')

	print('\t%0.3f'%c[i], end=' &')

	if dev[i] >= 10:
		print('\t%+0.0f'%dev[i], end=' \\\\')
	else:
		print('\t%+0.1f'%dev[i], end=' \\\\')

	print()
