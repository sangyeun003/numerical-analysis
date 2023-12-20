import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return 4*np.exp(0.8*x) - 0.5*y

def y_true(x):    # p.736 Example 25.5
    return (4/1.3)*(np.exp(0.8*x) - np.exp(-0.5*x)) + 2*np.exp(-0.5*x)

h = 1
x = np.arange(-1,5)
y = [-0.3929953, 2]
y_Heun = [-0.3929953, 2]
m = 10

for i in range(1,len(x)-1):
    # Original Heun's method
    y_temp = y_Heun[i] + f(x[i], y_Heun[i])*h
#    print(f'predicted y[{i+1}] = {y_temp:.6f} {(y_true(x[i+1]) - y_temp)/y_true(x[i+1]):.2%}')
    for _ in range(1):
        y_temp = y[i] + (f(x[i],y[i]) + f(x[i+1],y_temp))*h/2
    y_Heun.append(y_temp)
#    print(f'corrected y[{i+1}] = {y_Heun[i+1]:.6f} {(y_true(x[i+1]) - y_temp)/y_true(x[i+1]):.2%}')

    # Non-self-starting Heun's method
    y_temp = y[i-1] + f(x[i], y[i])*2*h
#    print(f'predicted y[{i+1}] = {y_temp:.6f}')
    for _ in range(m):
        y_temp = y[i] + (f(x[i],y[i]) + f(x[i+1],y_temp))*h/2
    y.append(y_temp)
#    print(f'corrected y[{i+1}] = {y[i+1]:.6f}')

plt.plot(x,y,'o-r', label="Non-self-starting Heun's method")
plt.plot(x,y_Heun,'o-b', label="Self-starting Heun's method")
xx = np.linspace(0,4,100)
plt.plot(xx,y_true(xx),'-k')
plt.legend()
plt.show()
