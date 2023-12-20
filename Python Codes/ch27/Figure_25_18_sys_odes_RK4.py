import numpy as np


def Integrator(x, y, h, xend, Derivs):
    # Integrate from x to xend with stepsize h.
    # The return values are
    # xend, (an approximate) y(xend).
    while True:
        if xend-x < h:
            h = xend-x
        x,y = RK4(x, y, h, Derivs)
        if x >= xend:
            return xend, y

def RK4(x, y, h, Derivs):
    k1 = Derivs(x, y)
    ym = y + k1*h/2
    k2 = Derivs(x + h/2, ym)
    ym = y + k2*h/2
    k3 = Derivs(x + h/2, ym)
    ye = y + k3*h
    k4 = Derivs(x + h, ye)
    slope = (k1 + 2*(k2 + k3) + k4)/6
    y = y + slope*h
    x = x + h
    return x,y


def solve_system_of_odes(xi, yi, xf, dx, xout, Derivs):
    # n = number of equations
    # yi = initial values of dependent variables (n-vector)
    # xi = initial value independent variable (scalar value)
    # xf = final value independent variable (scalar value)
    # dx = calculation step size
    # xout = output interval

    # NOTE #1
    # The output values of y(x) are evaluated at
    # xi, xi+xout, xi+2*xout, ..., xf
    # and stored in "yp".

    # NOTE #2
    # In each interval [xi + i*xout, xi + (i+1)*xout],
    # the output values of y are evaluated at
    # xi + i*xout, xi + i*xout + dx, xi + i*xout + 2*dx, ..., xi + (i+1)*xout]
    # and stored in "y".

    # Assuming "xf-xi = 4*xout" and "xout=3*dx",
    #
    # xi     xi+xout  xi+2xout xi+3xout    xf
    #  |  xout  |  xout  |  xout  |  xout  |
    #  +--+--+--+--+--+--+--+--+--+--+--+--+
    #  |dx|dx|dx|dx|dx|dx|dx|dx|dx|dx|dx|dx|

    x = xi
    m = 0   # index of yp[i]
    xp = [x]    # x to be returned

    # NOTE: To leverage the vector operations, we switch the two indices of yp
    # from (i,m) to (m,i).

    yp = [yi]   # the vector where the (approximate) values
                # [y(xi), y(xi+xout), y(xi+2*xout),...,y(xf)] are to be stored.
    y = np.array(yi)    # the vector where the (approximate) values
              # [y(xi+m*xout, xi+m*xout+dx, xi+m*xout+2*dx,...,xi+(m+1)*xout]
              # are to be stored.
              # Note that the last value (xi+(m+1)*xout) might be "xf" at the end.
    while True:
        # At this point, 
        # x = xi + m*xout
        xend = x + xout
        if xend > xf:   # If |xf-xi| is not a multiple of xout.
            xend = xf
        h = dx
        x,y = Integrator(x, y, h, xend, Derivs)   
        m = m + 1
        xp.append(x)
        yp.append(y)
        if x >= xf:
            return xp,np.array(yp)



