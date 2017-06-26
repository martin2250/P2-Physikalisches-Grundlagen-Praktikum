#!/usr/bin/python
from __future__ import print_function, division
import numpy as np

(h1, h2) = np.loadtxt('source/2.dat', unpack=True)

dh = 0.2	#because someone used cm

k = h1 / (h1 - h2)

#http://www.wolframalpha.com/input/?i=d%2Fdx+x%2F(x-y)
dk1 = h2/(h1-h2)**2
dk2 = h1/(h1-h2)**2
dk = np.sqrt(dk1**2 + dk2**2)*dh

print('kappa', k)
print('dkappa', dk)
print('mean', np.average(k, weights=dk**-2))
print('dmean', np.sqrt(1./np.sum(dk**-2)))
