import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return 4*np.exp(0.8*x) - 0.5*y

def y_analytic(x):    # p.736 Example 25.5
    return (4/1.3)*(np.exp(0.8*x) - np.exp(-0.5*x)) + 2*np.exp(-0.5*x)

x = np.arange(-3,5)
y = np.empty(x.shape)
y[:4] = y_analytic(x[:4])
h = 1

for i in range(3,7):
    y[i+1] = y[i] + h*((55/24)*f(x[i],y[i]) - (59/24)*f(x[i-1],y[i-1]) + (37/24)*f(x[i-2],y[i-2]) -(9/24)*f(x[i-3],y[i-3]))
    for j in range(10):
        y[i+1] = y[i] + h*( (9/24)*f(x[i+1],y[i+1])+(19/24)*f(x[i],y[i])-(5/24)*f(x[i-1],y[i-1]) + (1/24)*f(x[i-2],y[i-2]))

print(y)

xx = np.linspace(0,4,100)
plt.plot(xx,y_analytic(xx),'-k')
plt.plot(x,y,'o-r')
plt.show()

