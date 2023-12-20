import numpy as np

def Bisect(xl, xu, es, imax, xr):
# The parameters `iter' and `ea' are removed
# since they the local variables.
    iter = 0
    while True:
        xrold = xr
        xr = (xl + xu)/2
        # print(iter)
        iter = iter + 1
        if xr != 0:
            ea = np.abs((xr - xrold) / xr)*100
        test = f(xl) * f(xr)
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0
        if (ea < es) or (iter >= imax):
            break
    # modified to return three values
    # xr: approtimate root
    # iter: number of iterations
    # ea: estimated relative error (%)
    return (xr, iter, ea)

t = 10
g = 9.81
v = 40
m = 68.1
def f(c):
   return (g*m/c)*(1-np.exp(-(c/m)*t)) - v # (PT2.4) on p.119


xl = 12
xu = 16
es = 0.001
imax = 100
xr = xl

x, iter, ea = Bisect(xl, xu, es, imax, xr)

print(f'Number of iterations = {iter}')
print(f'Estimated relative error = {ea:.4f}%')

print(f'Root = {x:.4f}')
print(f'f(x) = {f(x):.2e}')

