import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return np.polyval([-2,12,-20,8.5],x)

def f_I(x,y):
    return np.polyval([-6,24,-20],x)

def f_II(x,y):
    return np.polyval([-12,24],x)

def f_III(x,y):
    return -12

def y_exact(x):
    return np.polyval([-0.5,4,-10,8.5,1],x)

x1 = np.linspace(0,4,8+1)
h1 = 0.5
x2 = np.linspace(0,4,16+1)
h2 = 0.25

y_Euler1 = [1]   # y(0) = 1
y_Euler2 = [1]

for i in range(0,len(x1)-1):
    y_Euler1.append(y_Euler1[i] + f(x1[i], y_Euler1[i])*h1)

for i in range(0,len(x2)-1):
    y_Euler2.append(y_Euler2[i] + f(x2[i], y_Euler2[i])*h2)

LTE_true = []
LTE_est = []

for i in range(0,len(x1)-1):
    LTE = (h1**2)*f_I(x1[i],y_Euler1[i])/2 + (h1**3)*f_II(x1[i],y_Euler1[i])/6 + (h1**4)*f_III(x1[i],y_Euler1[i])/24
    LTE_est.append(LTE/y_Euler1[i+1])
    LTE_true.append(LTE/y_exact(x1[i+1]))


fig, ax = plt.subplots(nrows=2, ncols=1)

ax[0].plot(x1, y_Euler1, 'o-b', label='h=0.5')
ax[0].plot(x2, y_Euler2, 'o-g', label='h=0.25')
xx = np.linspace(0,4,100)
ax[0].plot(xx, y_exact(xx), '-k', label='true solution')

ax[1].plot(x1[1:], LTE_true)
ax[1].plot(x1[1:], LTE_est)
plt.show()
