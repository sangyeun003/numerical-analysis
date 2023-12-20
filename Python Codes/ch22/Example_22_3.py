import numpy as np

def f(x):
    return np.polyval([400, -900, 675, -200, 25, 0.2], x)

a = 0
b = 0.8

c0 = 1
c1 = 1
x0 = -1/np.sqrt(3)
x1 = 1/np.sqrt(3)

I = ((b-a)/2)*( c0*f(((b+a)+(b-a)*x0)/2) + c1*f(((b+a)+(b-a)*x1)/2) )

I_exact = 3076/1875 # 1.640533...  Example 21.5 on p.628

print(f'I = {I:8.6f}, relative percent error = {(I_exact - I)/I_exact:.2%}')
