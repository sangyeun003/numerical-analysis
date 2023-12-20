import numpy as np

xi = 0
x_true = 0.56714329
print(' i      xi         et(%)        Et     E_{i+1}/E_i^2')
print('-- ----------- ----------- ----------- -------------')
for i in range(5):
    et = np.abs(100*(xi-x_true)/x_true)
    if i>0:
        Et_old = Et
    Et = np.abs(xi-x_true)
    if i>0:
        print(f'{i:>2d} {xi:.9f} {et:11.7f} {Et:11.9f} {(Et)/(Et_old**2):9.3f}')
    else:
        print(f'{i:>2d} {xi:.9f} {et:11.7f} {Et:11.9f}')
    xi_old = xi
    xi = xi - (np.exp(-xi) - xi)/(-np.exp(-xi)-1)

 
