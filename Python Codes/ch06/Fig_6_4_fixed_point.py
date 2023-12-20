import numpy as np

def Fixpt(x0, es, imax):
    xr = x0
    iter = 0
    while(True):
        xrold = xr
        xr = g(xrold)
        iter = iter + 1
        if xr != 0:
            ea = np.abs((xr-xrold)/xr)*100
        # print(ea, es)
        if ea<es or iter>=imax:
            break
    return xr

def g(x):
    return np.exp(-x)

x = Fixpt(1, 1e-5, 100)

print(f'root = {x}, f(x) = g(x)-x = {g(x)-x}')

    
