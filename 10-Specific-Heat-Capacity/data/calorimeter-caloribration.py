#!/usr/bin/python
from __future__ import print_function, division
import numpy as np

#	units:
#	temperature: degree celsius
#	mass: grams

T0 = 27.66		#	cold water temp
T1 = 88			#	hot water temp
Tmix = 51.4		#	mix temp

m0 = 240.15		#	mass of empty calorimeter
m1 = 291.05
m2 = 330.92

m1 -= m0		#	cold water mass
m2 -= m0 + m1	#	hot water mass

cw = 4.187		#	water heat capacity, J/(g*K)

C = cw * (m2 * (T1 - Tmix) / (Tmix - T0) - m1)

print('m-cold', m1)
print('m-hot', m2)
print('calorimeter total heat capacity:', C, 'J/K')
