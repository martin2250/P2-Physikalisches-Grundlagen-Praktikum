#!/usr/bin/python
from __future__ import print_function, division
import numpy as np

f_mmhg_pa = 133.322365

pa = 99600

dp_boil = 231 * f_mmhg_pa
p_boil = pa + dp_boil
Dp_boil = 1 * f_mmhg_pa

dp_freeze = -33 * f_mmhg_pa
p_freeze = pa + dp_freeze
Dp_freeze = 1 * f_mmhg_pa

t_boil = 99.49
Dt_boil = 2

gamma = 2.5e-5

alpha_1 = (p_boil - p_freeze)/(p_freeze * t_boil)
Dalpha_1 = np.zeros(3)
Dalpha_1[0] = 1/(p_freeze * t_boil) * Dp_boil
Dalpha_1[1] = p_boil/(p_freeze**2 * t_boil) * Dp_freeze
Dalpha_1[2] = (p_boil - p_freeze)/(p_freeze * t_boil**2) * Dt_boil
Dalpha_1 = np.sqrt(np.sum(Dalpha_1**2))

alpha = alpha_1 + p_boil/p_freeze * gamma
Dalpha = np.zeros(3)
Dalpha[0] = Dalpha_1
Dalpha[1] = gamma/p_freeze * Dp_boil
Dalpha[2] = p_boil * gamma / (p_freeze ** 2) * dp_freeze
Dalpha = np.sqrt(np.sum(Dalpha**2))

T_o = -1/alpha
DT_o = 1/(alpha**2) * Dalpha

print('alpha_1:', alpha_1, 'pm', Dalpha_1)
print('alpha:', alpha, 'pm', Dalpha)
print('T_o:', T_o, 'pm', DT_o)
print('error from -273.15:', np.abs(T_o + 273.15))
