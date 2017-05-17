#!/usr/bin/python
from __future__ import print_function, division
import numpy as np
import sys

n, R = np.loadtxt(sys.argv[1], unpack=True)

N=R*2 #calculate events

sum= np.sum(N)

print(sum)
