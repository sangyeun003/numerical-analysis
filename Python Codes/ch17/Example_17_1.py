import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,8)
y = np.array([0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5])
n = x.shape[0]

Sx = np.sum(x)
Sy = np.sum(y)
Sxy = np.dot(x,y)
Sxx = np.dot(x,x)

a1 = (n*Sxy - Sx*Sy)/(n*Sxx - (Sx)**2)
a0 = (Sy - a1*Sx)/n

print(f'a1={a1}, a0={a0}')

plt.plot(x,y,'o')
xx = np.linspace(1,7,2)
plt.plot(xx,a1*xx+a0,'-r')
plt.show()


