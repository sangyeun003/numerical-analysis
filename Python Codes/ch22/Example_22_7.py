import numpy as np
import scipy

def MonteCarloDartDummy(func, n, a, b):
    def ymx(x):
        return -func(x)
    xopt = scipy.optimize.fminbound(ymx,a,b)
    ymax = -ymx(xopt)   # find the maximum y value in the interval [a,b]
    TotalArea = ymax*(b-a)
    count = 0
# original, slow version using a loop
#    for i in range(n):
#        x = a + (b-a)*np.random.rand()
#        y = ymax*np.random.rand()
#        if y<func(x):
#            count = count+1

# faster version
    x = a + (b-a)*np.random.rand(n)
    y = ymax*np.random.rand(n)
    count = np.count_nonzero(y < func(x))
   
    return (count/n)*TotalArea


points = 10**5
def f(x):
    return np.polyval([400,-900,675,-200,25,0.2],x)

a = 0
b = 0.8
Q = MonteCarloDartDummy(f, points, a, b)

I_exact = 1.640533

print(f'integral = {Q:6.4f}, relative error = {np.abs((I_exact-Q)/I_exact):.4%}')

