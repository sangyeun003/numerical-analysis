import numpy as np

def quadapt(a,b):
    tol = 1e-6
    c = (a + b)/2
    fa = f(a)
    fc = f(c)
    fb = f(b)
    return qstep(a, b, tol, fa, fc, fb)

def qstep(a, b, tol, fa, fc, fb):
    h1 = b - a
    h2 = h1/2
    c = (a + b)/2
    fd = f((a + c)/2)
    fe = f((c + b)/2)
    I1 = (h1/6)*(fa + 4*fc + fb)    # Simpson's 1/3 rule
    I2 = (h2/6)*(fa + 4*fd + 2*fc + 4*fe + fb)
    if np.abs(I2 - I1) < tol:   # terminate after Boole's rule
        return I2 + (I2 - I1)/15
    else:
        Ia = qstep(a, c, tol, fa, fd, fc)
        Ib = qstep(c, b, tol, fc, fe, fb)
        return Ia + Ib

def f(x):
    return np.polyval([400, -900, 675, -200, 25, 0.2], x)


a = 0
b = 0.8

I_exact = 3076/1875 # 1.640533...  Example 21.5 on p.628
I = quadapt(a, b)

print(f'I = {I:8.6}, relative percent error = {(I-I_exact)/I_exact:.2%}')


