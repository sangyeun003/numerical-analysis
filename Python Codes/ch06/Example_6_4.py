import numpy as np

def f(x):
    return np.exp(-x)-x

def fI(x):
    return -np.exp(-x)-1

def fII(x):
    return np.exp(-x)

xr = 0.56714329

c = -fII(xr)/(2*fI(xr))

print(c)

xi = 0
x_true = 0.56714329
print(' i      xi         et(%)         Et     E_{i+1}/E_i^2  c*Et_old^2')
print('-- ----------- ----------- ------------ ------------- ------------')
for i in range(5):
    et = np.abs(100*(xi-x_true)/x_true)
    if i>0:
        Et_old = Et
    Et = np.abs(xi-x_true)
    if i>0:
        print(f'{i:>2d} {xi:.9f} {et:11.7f} {Et:12.10f}   {(Et)/(Et_old**2):9.3f}   {c*Et_old**2:12.10f}')
    else:
        print(f'{i:>2d} {xi:.9f} {et:11.7f} {Et:12.10f}')
    xi_old = xi
    xi = xi - (np.exp(-xi) - xi)/(-np.exp(-xi)-1)


