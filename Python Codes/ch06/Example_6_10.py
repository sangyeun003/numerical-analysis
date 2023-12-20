import numpy as np


def f(x):
    return (x-3)*(x-1)**2

def fI(x):
    return 3*x**2 - 10*x + 7

def fII(x):
    return 6*x - 10

def NR(x):
    return x - f(x)/fI(x)

def NR_mod(x):
    return x - f(x)*fI(x)/((fI(x))**2 - f(x)*fII(x))

x_NR = 0        # initial guess
x_true = 1      # true solution

print('1. For the double root x=1 with an initial guess x0=0: Standard method')
print(f'---- --------- ------')
print(f'iter     xi      et  ')
print(f'---- --------- ------')
for i in range(7):
    print(f'{i:4d} {x_NR:8.7f} {np.abs((x_NR-x_true)/x_true):6.1%}')
    x_NR = NR(x_NR)

x_NR_mod = 0    # initial guess
x_true = 1      # true solution

print('')
print('2. For the double root x=1 with an initial guess x0=0: Modified method')
print(f'---- -------- ----------')
print(f'iter     xi       et    ')
print(f'---- -------- ----------')
for i in range(4):
    print(f'{i:4d} {x_NR_mod:8.6f} {np.abs((x_NR_mod-x_true)/x_true):10.5%}')
    x_NR_mod = NR_mod(x_NR_mod)


x_NR = 4        # initial guess
x_NR_mod = 4    # initial guess
x_true = 3      # true solution

print('')
print('3. For the single root x=3 with an initial guess x0=4')
print(f'---- -------- ----------- -------- -----------')
print(f'iter standard     et      modified      et    ')
print(f'---- -------- ----------- -------- -----------')
for i in range(6):
    print(f'{i:4d} {x_NR:8.6f} {np.abs((x_NR-x_true)/x_true):11.7%} {x_NR_mod:8.6f} {np.abs((x_NR_mod-x_true)/x_true):11.7%}')
    x_NR = NR(x_NR)
    x_NR_mod = NR_mod(x_NR_mod)

