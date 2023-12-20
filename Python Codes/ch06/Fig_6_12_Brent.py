import numpy as np

def fzerosimp(xl,xu,f):
    eps = 2.22044604925031e-16
    tol = 0.000001
    a = xl
    b = xu
    fa = f(a)
    fb = f(b)
    c = a
    fc = fa
    d = b-c
    e = d
    while True:
        if fb == 0:
            break
        if np.sign(fa) == np.sign(fb):  # If necessary, rearrange points
            a = c
            fa = fc
            d = b-c
            e = d
        if np.abs(fa) < np.abs(fb):
            c = b
            b = a
            a = c
            fc = fb
            fb = fa
            fa = fc
        m = 0.5*(a-b)   # Termination test and possible exit
        tol = 2*eps*max(np.abs(b),1)
        if (np.abs(m) <= tol) or (fb == 0.0):
            break
        # Choose open methods or bisection
        if (np.abs(e) >= tol) and (np.abs(fc) > np.abs(fb)):
            s = fb/fc
            if a==c:    # Secant method
                p = 2*m*s
                q = 1-s
            else:   # Inverse quadratic interpolation
                q = fc/fa
                r = fb/fa
                p = s*(2*m*q*(q-r) - (b-c)*(r-1))
                q = (q-1)*(r-1)*(s-1)
            if p>0:
                q = -q
            else:
                p = -p
            if (2*p<3*m*q - np.abs(tol*1)) and (p < np.abs(0.5*e*q)):
                e = d
                d = p/q
            else:
                d = m
                e = m
        else:   # Bisection
            d = m
            e = m
        c = b
        fc = fb
        if np.abs(d) > tol:
            b = b + d
        else:
            b = b - np.sign(b-a)*tol
        fb = f(b)
    return b



# Example 6.1, 6.2, 6.3, 6.4, 6.6, 6.8
# f(x) = exp(-x) - x
print(fzerosimp(0,1,lambda x:np.exp(-x) - x))

# Example 6.7
# f(x) = ln(x)
print(fzerosimp(0.5,5.0,np.log))

