#!/usr/bin/python
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import sys

order, angleL, arcL, angleR, arcR = np.loadtxt('source/2-4-140mm.dat', unpack=True)

#constants
wavelength = 589.3e-9

#decimalization
arc_dez_L = arcL / 60
arc_dez_R = arcR / 60

angle_dez_L = angleL + arc_dez_L
angle_dez_R = angleR + arc_dez_R

#offset
angle_dez_L = angle_dez_L - 180
angle_dez_R = 180 - angle_dez_R

#in radian
angle_L = angle_dez_L * (np.pi / 180)
angle_R = angle_dez_R * (np.pi / 180)

#mean
angle = (angle_L + angle_R) / 2	#mean in radian
angle_deg = (angle_dez_L + angle_dez_R) / 2
angle_deg_mean = np.floor(angle_deg) + (angle_deg - np.floor(angle_deg)) * (60 / 100)	#mean in degree,arc minutes

#==> grating constant
b = np.sin(angle) / (order*wavelength)

for i in range(0, len(b)):
	print("phi=", angle_deg_mean[i], "1/g=", b[i])
print("mean 1/g=", np.mean(b), "std=", np.std(b))
