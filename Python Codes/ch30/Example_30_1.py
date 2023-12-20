import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation


L = 10
k_prime = 0.49
#delta_x = 2
#delta_x = 0.5
delta_x = 0.4
delta_t = 0.1
#delta_t = 0.2
#t_end = 12
t_end = 30
x0 = 100
xL = 50
C = 0.2174
rho = 2.7
k = k_prime/(rho * C)
_lambda = k*delta_t/(delta_x**2)

t = np.arange(0,t_end+delta_t,delta_t)
x = np.arange(0,L+delta_x, delta_x)

T = np.zeros((len(t), len(x)))

T[:,0] = x0
T[:,-1] = xL

for l in range(len(t)-1):
    T[l+1,1:-1] = T[l,1:-1] + _lambda*(T[l,2:] - 2*T[l,1:-1] + T[l,:-2])

xx,tt = np.meshgrid(x,t)

# 2D surface plot
ax = plt.axes(projection ='3d') 
ax.plot_surface(tt, xx, T, cmap=cm.coolwarm)
plt.show()


