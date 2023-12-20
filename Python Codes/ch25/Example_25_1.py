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

x = np.linspace(0,4,9)
h = 0.5

y_true = y_exact(x)

y_Euler = [1]   # y(0) = 1

for i in range(0,len(x)-1):
    y_next = y_Euler[i] + f(x[i], y_Euler[i])*h
    y_Euler.append(y_next)

print('------------------------------------------')
print('                    Percent Relative Error')
print('                    ----------------------')
print(' x   y_true y_Euler   Global       Local')
print('--- ------- ------- ----------  ----------')
for i in range(len(x)):
    if i==0:
        print(f'{x[i]:.1f} {y_true[i]:.5f} {y_Euler[i]:.5f}')
    else:
        E_local = (h**2)*f_I(x[i-1],y_Euler[i-1])/2 + (h**3)*f_II(x[i-1],y_Euler[i-1])/6 + (h**4)*f_III(x[i-1],y_Euler[i-1])/24
        E_global = y_true[i] - y_Euler[i]
        print(f'{x[i]:.1f} {y_true[i]:.5f} {y_Euler[i]:.5f}  {E_global/y_true[i]:7.1%}     {E_local/y_true[i]:7.1%}')

print('--- ------- ------- ----------  ----------')

plt.plot(x, y_Euler, 'o-b', label='h=0.5')
xx = np.linspace(0,4,100)
plt.plot(xx, y_exact(xx), '-k', label='true solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
