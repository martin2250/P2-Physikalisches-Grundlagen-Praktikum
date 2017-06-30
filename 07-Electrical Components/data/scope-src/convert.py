#!/usr/bin/python
import numpy as np
import sys

inp = np.load(sys.argv[1])
np.savez_compressed(sys.argv[2], inp)
