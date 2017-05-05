#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

if len(sys.argv)==1:
	print('Specify a file, dimwit.')
	sys.exit()

elif len(sys.argv)==2:
	print(sys.argv[1])
	(deg, U) = np.loadtxt(sys.argv[1], unpack=True)

N = 36
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
ax.plot(theta, U, color='#ee8d18')

matplotlib.rc('text', usetex = True)
params = {'text.latex.preamble' : ['\\usepackage{amsmath}', '\\usepackage{siunitx}', '\\sisetup{per-mode=fraction}', '\\sisetup{separate-uncertainty=true}']}
plt.rcParams.update(params)

if len(sys.argv)==2:
	plt.show()

elif len(sys.argv)==3 and sys.argv[2]=='save':
	plt.savefig('plots/' + sys.argv[1][:-3] + 'pdf', format='pdf')
