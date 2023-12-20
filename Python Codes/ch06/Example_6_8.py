import numpy as np

def f(x):
    return np.exp(-x) - x

x = 1
delta = 0.01
x_true = 0.56714329
print(f'iter     x         et')
print(f'---- -------- -----------')
for i in range(3):
    x = x - (delta*x*f(x))/(f(x+delta*x) - f(x))
    print(f'{i+1:4d} {x:7.6f} {100*np.abs((x-x_true)/x_true):9.8f}%')
