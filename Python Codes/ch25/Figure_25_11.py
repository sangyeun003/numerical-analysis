import numpy as np
import matplotlib.pyplot as plt


def f(x,y):
    return np.polyval([-2,12,-20,8.5],x)

def y_exact(x):
    return np.polyval([-0.5,4,-10,8.5,1],x)

x = np.linspace(0,4,8+1)
y_Euler = [1] # initial condition: y[0]=0
y_Heun = [1]
h = 0.5


for i in range(0,len(x)-1):
    y_Euler.append(y_Euler[i] + f(x[i],y_Euler[i])*h)
    y_next = y_Euler[i+1]
    y_Heun.append(y_Heun[i] + (f(x[i],y_Heun[i]) + f(x[i+1],y_next))*h/2)


plt.plot(x,y_Euler,'o-k', label="Euler's method")
plt.plot(x,y_Heun,'o-b', label="Heun's method")
xx = np.linspace(0,4,100)
plt.plot(xx,y_exact(xx),'-r', label="true solution")
plt.legend()
plt.show()

