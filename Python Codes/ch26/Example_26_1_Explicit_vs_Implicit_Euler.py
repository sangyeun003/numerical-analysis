import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return -1000*y + 3000 - 2000*np.exp(-t)

def y_exact(t):
    return 3 - 0.998*np.exp(-1000*t) - 2.002*np.exp(-t)


h_explicit_1 = 0.0005 # for Euler's method
h_explicit_2 = 0.0015 # for Euler's method
t_start_explicit = 0
t_end_explicit = 0.006

y_explicit_1 = [0] # initial condition: y(0)=0
t_explicit_1 = np.linspace(t_start_explicit, t_end_explicit, int((t_end_explicit-t_start_explicit)/h_explicit_1)+1)
for i in range(len(t_explicit_1)-1):
    y_explicit_1.append(y_explicit_1[i] + f(t_explicit_1[i], y_explicit_1[i])*h_explicit_1)

y_explicit_2 = [0] # initial condition: y(0)=0
t_explicit_2 = np.linspace(t_start_explicit, t_end_explicit, int((t_end_explicit-t_start_explicit)/h_explicit_2)+1)
for i in range(len(t_explicit_2)-1):
    y_explicit_2.append(y_explicit_2[i] + f(t_explicit_2[i], y_explicit_2[i])*h_explicit_2)



h_implicit = 0.05   # for implicit Euler's method
t_start_implicit = 0
t_end_implicit = 0.4
y_implicit = [0] # initial condition: y(0)=0
t_implicit = np.linspace(t_start_implicit, t_end_implicit, int((t_end_implicit-t_start_implicit)/h_implicit)+1)
for i in range(len(t_implicit)-1):
    y_implicit.append((y_implicit[i] + 3000*h_implicit - 2000*h_implicit*np.exp(-(t_implicit[i]+h_implicit)))/(1 + 1000*h_implicit))



fig,ax = plt.subplots(2,1)

ax[0].set_title("Euler's explicit method")
ax[0].plot(t_explicit_1, y_explicit_1,'o-g',label=f"step size {h_explicit_1}")
ax[0].plot(t_explicit_2, y_explicit_2,'o-b',label=f"step size {h_explicit_2}")
tt_explicit = np.linspace(t_start_explicit, t_end_explicit, 1000)
ax[0].plot(tt_explicit, y_exact(tt_explicit), '-k')
ax[0].legend()

ax[1].set_title("Euler's implicit method")
ax[1].plot(t_implicit, y_implicit, 'o-r', label=f"step size {h_implicit}")
tt_implicit = np.linspace(t_start_implicit, t_end_implicit, 1000)
ax[1].plot(tt_implicit, y_exact(tt_implicit), '-k')
ax[1].legend()

plt.show()


