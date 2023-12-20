import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt

# Example 25.9 (p.752)
x1_domain = [0,2]
y0_1 = [4,6]
def f1(x,y):
    return np.array([-0.5*y[0], 4-0.3*y[1] - 0.1*y[0]])

# Example 25.11 (p.754)
x2_domain = [0,4]
def f2_linear(x,y):
    return np.array([y[1], -16.1*y[0]])

def f2_nonlinear(x,y):
    return np.array([y[1], -16.1*np.sin(y[0])])

y0_2_small = [0.1, 0]
y0_2_large = [np.pi/4, 0]

fig,ax = plt.subplots(3,1)

x1 = np.linspace(x1_domain[0],x1_domain[1],10)
ret1 = solve_ivp(f1,x1_domain,y0_1,method="RK23", t_eval=x1)
ax[0].plot(ret1.t, ret1.y[0,:], "o-r")
ax[0].set_title("Example 25.9")

# Example 25.11 with a small initial displacement
x2 = np.linspace(x2_domain[0],x2_domain[1],100)

ret2_small_linear = solve_ivp(f2_linear,x2_domain,y0_2_small,method="RK23", t_eval=x2)
ret2_small_nonlinear = solve_ivp(f2_nonlinear,x2_domain,y0_2_small,method="RK23", t_eval=x2)
ax[1].plot(ret2_small_nonlinear.t, ret2_small_nonlinear.y[0,:], "-r", label="nonlineaar")
ax[1].plot(ret2_small_linear.t, ret2_small_linear.y[0,:], ":b", label="linear")
ax[1].set_title("Example 25.11 with a small initial displacement")
ax[1].legend()

# Example 25.11 with a large initial displacement
ret2_large_linear = solve_ivp(f2_linear,x2_domain,y0_2_large,method="RK23", t_eval=x2)
ret2_large_nonlinear = solve_ivp(f2_nonlinear,x2_domain,y0_2_large,method="RK23", t_eval=x2)
ax[2].plot(ret2_large_nonlinear.t, ret2_large_nonlinear.y[0,:], "-r", label="nonlinear")
ax[2].plot(ret2_large_linear.t, ret2_large_linear.y[0,:], ":b", label="linear")
ax[2].set_title("Example 25.11 with a large initial displacement")
ax[2].legend()

plt.show()

