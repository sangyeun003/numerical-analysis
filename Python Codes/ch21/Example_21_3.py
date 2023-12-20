import numpy as np
from scipy import integrate
#import scipy.integrate as integrate

def Trapm(h,f):
    w = np.ones(len(f), dtype=np.double)
    w[[0,-1]] = [1/2, 1/2]  # replace the 1st and last elements with 1/2
    return h*np.dot(f, w)

def v(t):
    g = 9.8
    m = 68.1
    c = 12.5
    return (g*m/c)*(1 - np.exp(-(c/m)*t))

t_start = 0
t_end = 10
# Compute the exact value using the Gauss quadrature
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html
#d_exact,_ = integrate.quad(v, t_start, t_end)  
d_exact = 289.43515

print(f'exact valeu = {d_exact}')

segments = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

print('-------- ------------ -------------  -------')
print('Segments Segment size Estimated d,m   et(%)')
print('-------- ------------ -------------  -------')
for n in segments:
    t = np.linspace(t_start, t_end, n+1, dtype=np.double)
    f = v(t)
    h = (t_end-t_start)/n
    d = Trapm(h,f)
    et = np.abs((d - d_exact)/d_exact)
    print(f'{n:>8,d}     {h:4.3f}       {d:8.4f}    {et:5.4%}')
print('-------- ------------ -------------  -------')
