import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt

# Example 25.1 (p.722)
x1_domain = [0,4]
y0_1 = 1
def f1(x,y): 
    return np.polyval([-2, 12, -20, 8.5], x)
def y1_analytic(x): 
    return np.polyval([-0.5, 4, -10, 8.5, 1], x)

# Example 1.1 (p.14) and 25.4 (p.732)
g = 9.81
c = 12.5
m = 68.1
x2_domain = [0, 15]
y0_2 = 0
def f2(x,y): 
    return g - c*y/m
def y2_analytic(x): 
    return (g*m/c)*(1 - np.exp(-c*x/m))

# Example 25.5 (p.736)
x3_domain = [0,4]
y0_3 = 2
def f3(x,y): 
    return 4*np.exp(0.8*x) - 0.5*y
def y3_analytic(x): 
    return (4/1.3)*(np.exp(0.8*x) - np.exp(-0.5*x)) + 2*np.exp(-0.5*x)

fig,ax = plt.subplots(3,1)

method = "RK23"

x1 = np.linspace(x1_domain[0], x1_domain[1], 10)
ret1 = solve_ivp(f1, x1_domain, [y0_1], method=method, t_eval=x1)
xx = np.linspace(x1_domain[0], x1_domain[1], 100)

ax[0].plot(xx, y1_analytic(xx), "-k", label="analytic solution")
ax[0].plot(ret1.t, ret1.y[0,:], "o-r", label="numerical solution")
ax[0].legend()
ax[0].set_title("Example 25.1")

x2 = np.linspace(x2_domain[0], x2_domain[1], 10)
ret2 = solve_ivp(f2, x2_domain, [y0_2], method=method, t_eval=x2)
xx = np.linspace(x2_domain[0], x2_domain[1], 100)

ax[1].plot(xx, y2_analytic(xx), "-k", label="analytic solution")
ax[1].plot(ret2.t, ret2.y[0,:], "o-r", label="numerical solution")
ax[1].legend()
ax[1].set_title("Example 1.1 / Example 25.4")

x3 = np.linspace(x3_domain[0], x3_domain[1], 10)
ret3 = solve_ivp(f3, x3_domain, [y0_3], method=method, t_eval=x3)
xx = np.linspace(x3_domain[0], x3_domain[1], 100)

ax[2].plot(xx, y3_analytic(xx), "-k", label="analytic solution")
ax[2].plot(ret3.t, ret3.y[0,:], "o-r", label="numerical solution")
ax[2].legend()
ax[2].set_title("Example 25.5")


plt.show()

