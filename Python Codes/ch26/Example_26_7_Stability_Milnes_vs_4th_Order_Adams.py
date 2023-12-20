import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return -y

def y_analytic(x):
    return np.exp(-x)

h = 0.5
x = np.arange(-h*3,10+h,h)

y_Milne = np.empty(len(x))
y_Milne[:5] = y_analytic(x[:5])
y_4thAdam = np.empty(len(x))
y_4thAdam[:5] = y_analytic(x[:5])

for i in range(4,len(x)-1):
    y_Milne[i+1] = y_Milne[i-3] + (4*h/3)*(2*f(x[i],y_Milne[i]) - f(x[i-1],y_Milne[i-1]) + 2*f(x[i-2],y_Milne[i-2]))
    for j in range(10):
        y_Milne[i+1] = y_Milne[i-1] + (h/3)*(f(x[i-1],y_Milne[i-1]) + 4*f(x[i],y_Milne[i]) + f(x[i+1],y_Milne[i+1]))

    y_4thAdam[i+1] = y_4thAdam[i] + h*((55/24)*f(x[i],y_4thAdam[i]) - (59/24)*f(x[i-1],y_4thAdam[i-1]) + (37/24)*f(x[i-2],y_4thAdam[i-2]) -(9/24)*f(x[i-3],y_4thAdam[i-3]))

    for j in range(10):
        y_4thAdam[i+1] = y_4thAdam[i] + h*( (9/24)*f(x[i+1],y_4thAdam[i+1])+(19/24)*f(x[i],y_4thAdam[i])-(5/24)*f(x[i-1],y_4thAdam[i-1]) + (1/24)*f(x[i-2],y_4thAdam[i-2]))

print(y_analytic(x))

xx = np.linspace(0,10,100)
plt.plot(xx,y_analytic(xx),'-k')
plt.plot(x,y_Milne,'o-r', label="Milne's method")
plt.plot(x,y_4thAdam,'o:b', label="4th-order Adams method")
plt.ylim([-0.002,0.007])
plt.xlim([5,10])
plt.legend()
plt.show()




