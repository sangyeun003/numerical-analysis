import numpy as np
import math


b = 1
A = -2

# computing \int_{-\infty}^{-2} exp(-x**2/2) dx
# using the extended midpoint rule with 4 segments
def f1(t):
    return (1/t**2)*np.exp(-1/(2*t**2))
n = 4
h = (0 - (1/A))/n
x = (1/A) + (h/2)*np.array([1, 3, 5, 7])
w = np.array([1, 1, 1, 1])
I1 = ((0 - (1/A))/n)*np.dot(w,f1(x))

# computing \int_{-2}^1 exp(-x**2/2) dx
# using the Simpson's 1/3 rule
def f2(x):
    return np.exp(-x**2/2)

n = 6
x = np.linspace(A,b,n+1)
w = np.array([1,4,2,4,2,4,1])
I2 = ((b-A)/(3*n))*np.dot(w,f2(x))

I_approx = (I1+I2)/np.sqrt(2*math.pi)

I_exact = 0.8413


et = (I_exact - I_approx)/I_exact

print(f'approximate integral = {I_approx:6.4f}, et = {et:.4%}')
