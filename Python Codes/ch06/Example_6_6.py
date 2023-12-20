import numpy as np

x_curr = 1  # current solution
x_prev = 0  # previous solution
x_true = 0.56714329 # true solution

def f(x):
    return np.exp(-x) - x

print(f'iteration    et  ')
print(f'--------- -------')
for i in range(3):
    x = x_curr - (f(x_curr)*(x_prev - x_curr))/(f(x_prev) - f(x_curr))
    x_prev = x_curr
    x_curr = x
    print(f'{i+1:9d} {np.abs(100*(x_curr - x_true)/x_true):5.4f}%')
