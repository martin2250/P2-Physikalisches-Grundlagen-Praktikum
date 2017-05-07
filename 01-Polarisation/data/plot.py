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

deg = deg + rotate

theta = deg * np.pi / 180

matplotlib.rc('xtick', labelsize=11)
matplotlib.rc('ytick', labelsize=9)
matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}']}
plt.rcParams.update(params)


ax = plt.subplot(111, projection='polar')

ax.set_xlabel('Winkel in $\\si{\\degree}$')
ax.set_ylabel('Spannung in $\\si{\\volt}$')

ax.plot(theta, U)

if len(sys.argv)==2:
	plt.show()
else:
	plt.savefig(sys.argv[2], format='pdf')
