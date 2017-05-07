#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

if not 1 < len(sys.argv) < 4:
	print('usage: %s source.dat [target.pdf]\n\t\t...dickhead.'%sys.argv[0])
	sys.exit()

(deg, U) = np.loadtxt(sys.argv[1], unpack=True)

rotate = 0

with open(sys.argv[1]) as file:
	firstline = file.readlines()[0]
	if firstline.startswith('#rotate='):
		rotate = int(firstline[8:])
		print(rotate)

deg = np.roll(deg, rotate)
U = np.roll(U, rotate)

theta = deg * np.pi / 180

matplotlib.rc('xtick', labelsize=11)
matplotlib.rc('ytick', labelsize=9)

#This isn't fucking working
#plt.xlabel('Winkel in $\si{\degree}$')
#plt.ylabel('Spannung in $\si{\volt}$')

ax = plt.subplot(111, projection='polar')
ax.plot(theta, U)

if len(sys.argv)==2:
	for i in range(0,37):
		print(i, theta[i], U[i])
	plt.show()
else:
	plt.savefig(sys.argv[2], format='pdf')
