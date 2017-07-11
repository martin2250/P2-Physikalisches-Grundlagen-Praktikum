#!/usr/bin/python
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import sys

order, vb_l, vb_l_arcs, b_l, b_l_arcs, bg_l, bg_l_arcs, r_l, r_l_arcs, vb_r, vb_r_arcs, b_r, b_r_arcs, bg_r, bg_r_arcs, r_r, r_r_arcs= np.loadtxt('source/2-5.dat', unpack=True)

#combine left and right sides
vb = np.vstack((vb_l, vb_r))
vb_arcs = np.vstack((vb_l_arcs, vb_r_arcs))
b = np.vstack((b_l, b_r))
b_arcs = np.vstack((b_l_arcs, b_r_arcs))
bg = np.vstack((bg_l, bg_r))
bg_arcs = np.vstack((bg_l_arcs, bg_r_arcs))
r = np.vstack((r_l, r_r))
r_arcs = np.vstack((r_l_arcs, r_r_arcs))

#constants
g=616.2e3	#grating constant

#decimalization
vb_dez_arcs = vb_arcs / 60
b_dez_arcs = b_arcs / 60
bg_dez_arcs = bg_arcs / 60
r_dez_arcs = r_arcs / 60

vb_dez = vb + vb_dez_arcs
b_dez = b + b_dez_arcs
bg_dez = bg + bg_dez_arcs
r_dez = r + r_dez_arcs

#offset
vb_dez[0] = vb_dez[0] - 180
vb_dez[1] = 180 - vb_dez[1]
b_dez[0] = b_dez[0] - 180
b_dez[1] = 180 - b_dez[1]
bg_dez[0] = bg_dez[0] - 180
bg_dez[1] = 180 - bg_dez[1]
r_dez[0] = r_dez[0] - 180
r_dez[1] = 180 - r_dez[1]

#in radian
vb_rad = (vb_dez * (np.pi / 180))
b_rad = (b_dez * (np.pi / 180))
bg_rad = (bg_dez * (np.pi / 180))
r_rad = (r_dez * (np.pi / 180))

#mean in radian
vb_mean_angle = np.mean(vb_rad, axis=0)
b_mean_angle = np.mean(b_rad, axis=0)
bg_mean_angle = np.mean(bg_rad, axis=0)
r_mean_angle = np.mean(r_rad, axis=0)

#mean in degrees
# vb_dez = vb_dez.T
# b_dez = b_dez.T
# bg_dez = bg_dez.T
# r_dez = r_dez.T
vb_mean_deg = (vb_dez[0]+vb_dez[1]) / 2
b_mean_deg = (b_dez[0]+b_dez[1]) / 2
bg_mean_deg = (bg_dez[0]+bg_dez[1]) / 2
r_mean_deg = (r_dez[0]+r_dez[1]) / 2

#mean in degrees, formatted to degree,arc minutes
vb_mean_for = np.floor(vb_mean_deg) + (vb_mean_deg - np.floor(vb_mean_deg)) * (60 / 100)
b_mean_for = np.floor(b_mean_deg) + (b_mean_deg - np.floor(b_mean_deg)) * (60 / 100)
bg_mean_for = np.floor(bg_mean_deg) + (bg_mean_deg - np.floor(bg_mean_deg)) * (60 / 100)
r_mean_for = np.floor(r_mean_deg) + (r_mean_deg - np.floor(r_mean_deg)) * (60 / 100)

#==> grating constant
lamb_vb = np.sin(vb_mean_angle) / (order*g)
#print(np.sin(vb_mean_angle) / (order*g))
lamb_b = np.sin(b_mean_angle) / (order*g)
lamb_bg = np.sin(bg_mean_angle) / (order*g)
lamb_r = np.sin(r_mean_angle) / (order*g)

print("\nlambda vb=", lamb_vb)
print("mean of phi for vb=", vb_mean_for)
print("mean of lambda vb=", np.mean(lamb_vb), "+/-", np.std(lamb_vb), "\n")
print("lambda b=", lamb_b)
print("mean of phi for b=", b_mean_for)
print("mean of lambda b=", np.mean(lamb_b), "+/-", np.std(lamb_b), "\n")
print("lambda bg=", lamb_bg)
print("mean of phi for bg=", bg_mean_for)
print("mean of lambda bg=", np.mean(lamb_bg), "+/-", np.std(lamb_bg), "\n")
print("lambda r=", lamb_r)
print("mean of phi for r=", r_mean_for)
print("mean of lambda r=", np.mean(lamb_r), "+/-", np.std(lamb_r), "\n")
