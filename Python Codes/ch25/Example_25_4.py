import numpy as np
import matplotlib.pyplot as plt

g = 9.81
c = 12.5
m = 68.1
a = 8.3
b = 2.2
vmax = 46

def f_linear(t,v):
    return g - c*v/m

def f_nonlinear(t,v):
    return g - (c/m)*(v + a*((v/vmax)**b))

h = 0.1
t = np.arange(0,15,h)
v_linear = [0] # initial condition: v(0) = 0
v_nonlinear = [0]

for i in range(0,len(t)-1):
    v_linear.append(v_linear[i] + h*f_linear(t[i],v_linear[i]))
    v_nonlinear.append(v_nonlinear[i] + h*f_nonlinear(t[i],v_nonlinear[i]))


plt.plot(t,v_linear,'-k', label='linear')
plt.plot(t,v_nonlinear, '-b', label='nonlinear')
plt.legend()
plt.show()
