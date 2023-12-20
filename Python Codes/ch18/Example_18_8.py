import numpy as np
import matplotlib.pyplot as plt

x = np.array([3, 4.5, 7, 9])
f = np.array([2.5, 1, 2.5, 0.5])

# linear spline
def s0_linear(xx):
    return f[0]*(xx-x[1])/(x[0]-x[1]) + f[1]*(xx-x[0])/(x[1]-x[0])

def s1_linear(xx):
    return f[1]*(xx-x[2])/(x[1]-x[2]) + f[2]*(xx-x[1])/(x[2]-x[1])

def s2_linear(xx):
    return f[2]*(xx-x[3])/(x[2]-x[3]) + f[3]*(xx-x[2])/(x[3]-x[2])

# quadratic spline (Example 18.9)
def s0_quadratic(xx):
    return 2.5 - (xx-x[0])

def s1_quadratic(xx):
    return 1.0 - (xx-x[1]) + 0.64*(xx-x[1])**2

def s2_quadratic(xx):
    return 2.5 + 2.2*(xx-x[2]) - 1.6*(xx-x[2])**2

# cubic spline (Example 18.10)
def s0_cubic(xx):
    return 2.5 - 1.419771863*(xx-x[0]) + 0.186565272*(xx-x[0])**3

def s1_cubic(xx):
    return 1.0 - 0.160456274*(xx-x[1]) + 0.839543726*(xx-x[1])**2 - 0.214144487*(xx-x[1])**3

def s2_cubic(xx):
    return 2.5 + 0.022053232*(xx-x[2]) - 0.766539924*(xx-x[2])**2 + 0.127756654*(xx-x[2])**3

# interpolating cubic polynomial
def p3(xx):
    return (f[0]*np.prod([xx-x[1],xx-x[2],xx-x[3]],axis=0)/np.prod([x[0]-x[1],x[0]-x[2],x[0]-x[3]])
          + f[1]*np.prod([xx-x[0],xx-x[2],xx-x[3]],axis=0)/np.prod([x[1]-x[0],x[1]-x[2],x[1]-x[3]])
          + f[2]*np.prod([xx-x[0],xx-x[1],xx-x[3]],axis=0)/np.prod([x[2]-x[0],x[2]-x[1],x[2]-x[3]])
          + f[3]*np.prod([xx-x[0],xx-x[1],xx-x[2]],axis=0)/np.prod([x[3]-x[0],x[3]-x[1],x[3]-x[2]]))

fig, ax = plt.subplots(3,1)

xx = np.linspace(np.min(x), np.max(x), 100)
xx0 = np.linspace(x[0], x[1], 100)
xx1 = np.linspace(x[1], x[2], 100)
xx2 = np.linspace(x[2], x[3], 100)

ax[0].plot(x,f,'ok')
ax[0].plot(xx0, s0_linear(xx0), 'r-')
ax[0].plot(xx1, s1_linear(xx1), 'g-')
ax[0].plot(xx2, s2_linear(xx2), 'b-')

ax[1].plot(x,f,'ok')
ax[1].plot(xx0, s0_quadratic(xx0), 'r-')
ax[1].plot(xx1, s1_quadratic(xx1), 'g-')
ax[1].plot(xx2, s2_quadratic(xx2), 'b-')

ax[2].plot(x,f,'ok')
ax[2].plot(xx0, s0_cubic(xx0), 'r-', label='cubic spline')
ax[2].plot(xx1, s1_cubic(xx1), 'g-', label='cubic spline')
ax[2].plot(xx2, s2_cubic(xx2), 'b-', label='cubic spline')
ax[2].plot(xx, p3(xx), 'k:', label='interpolating cubic')
ax[2].legend()



plt.show()
