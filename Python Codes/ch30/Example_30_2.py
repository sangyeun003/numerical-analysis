import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

L = 10
k_prime = 0.49
#delta_x = 2
#delta_x = 1
#delta_x = .5
#delta_x = .1
delta_x = .1
delta_t = 0.1
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

m = len(x)-2

T = np.zeros((len(t), len(x)))

T[:,0] = x0
T[:,-1] = xL

A = np.zeros((m,m))
b = np.zeros((m,))

np.set_printoptions(precision=5)

A[0,:2] = np.array([[1 + 2 *_lambda, -_lambda]])
for i in range(1,m-1):
    A[i, (i-1):(i+2)] = np.array([-_lambda, 1+2*_lambda, -_lambda]) 
A[m-1,-2:] = np.array([-_lambda, 1 + 2*_lambda])


for l in range(len(t)-1):
    b[0] = T[l,1] + _lambda*x0
    b[1:m-1] = T[l,2:m]
    b[m-1] = T[l,m] + _lambda*xL
    T[l+1,1:-1] = np.linalg.solve(A, b)


xx,tt = np.meshgrid(x,t)

ax = plt.axes(projection ='3d') 
ax.plot_surface(tt, xx, T, cmap=cm.coolwarm)
plt.show()



