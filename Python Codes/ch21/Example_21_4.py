import numpy as np
from scipy import integrate
import math

def f(x):
    # 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
    return np.polyval([400, -900, 675, -200, 25, 0.2], x)

def f_IV(x): # 4-th derivative of f(x)
    return np.polyval([math.factorial(5)*400, -math.factorial(4)*900], x)

I_exact = 1.640533

a = 0
b = 0.8
x = np.linspace(a,b,3)
h = (b-a)/2

w = np.array([1,4,1])*h/3
I = np.dot(w, f(x))
f_IV_average = integrate.quad(f_IV, a, b)[0]/(b-a)  # [PT6.4] on p.604

Et = I_exact - I
et = (I_exact - I)/I_exact
Ea = -(1/90)*f_IV_average*h**5

print('+--------------------------------------------------------+')
print("| Example 21.4: Single Application of Simpson's 1/3 Rule |")
print('+--------------------------------------------------------+')
print(f'I = {I:8.6f}, Et = {Et:9.7f}, et = {et:4.1%} Ea = {Ea:9.7f}')
