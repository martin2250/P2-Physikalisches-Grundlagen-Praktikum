#!/usr/bin/python
from __future__ import division, print_function
import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt

(Us, Unf, Uf) = np.loadtxt('source/33.dat', unpack=True)

Rshunt = 100e6

Inf = Unf/Rshunt
If = Uf/Rshunt

plt.plot(Us, Inf)
plt.plot(Us, If)

ax = plt.gca()
ax.set_yscale('log')

plt.show()
