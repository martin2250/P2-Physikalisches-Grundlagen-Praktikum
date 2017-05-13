#!/usr/bin/python
from __future__ import print_function, division
import numpy as np

n, RL = np.loadtxt('source/1.2_L.dat', unpack=True)
n, RR = np.loadtxt('source/1.2_R.dat', unpack=True)

ml = np.mean(RL)
mr = np.mean(RR)
sdl = np.std(RL)
sdr = np.std(RR)

print('left setup: mean', ml, 'cps, std:', sdl, 'cps')
print('right setup: mean', mr, 'cps, std:', sdr, 'cps')
