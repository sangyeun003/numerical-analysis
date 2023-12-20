import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import *

h_prime = 5e-8
Ta = 20
L = 10
T1 = 40
T2 = 200

def f(x,Tz):    
    # Tz = [T, z]
    return np.array([Tz[1], h_prime*(Tz[0] - Ta)**4])

h = .1

x = np.arange(0, L+h, h)

# first guess
z0_1 = 10
ret1 = solve_ivp(f, [0,L], [T1,z0_1], t_eval=x)
T_last_1 = ret1.y[0,-1]

# second guess
z0_2 = 8
ret2 = solve_ivp(f, [0,L], [T1,z0_2], t_eval=x)
T_last_2 = ret2.y[0,-1]

# linearly interpolated guess
z0_new = z0_1 + (z0_2 - z0_1)/(T_last_2 - T_last_1)*(T2 - T_last_1)
ret_new = solve_ivp(f, [0,L], [T1,z0_new], t_eval=x)


plt.plot(x,ret1.y[0,:],"-g", label=f"z(0)={z0_1}")
plt.plot(x,ret2.y[0,:],"-b", label=f"z(0)={z0_2}")
plt.plot(x,ret_new.y[0,:],"-r", label="linearly interpolated z(0)")
plt.plot(L, T2, "ok")
plt.legend()
plt.show()
