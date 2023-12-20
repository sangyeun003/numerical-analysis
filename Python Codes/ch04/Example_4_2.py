import numpy as np
import matplotlib.pyplot as plt
import math

xi = np.pi/4
h = np.pi/12
f_true = np.cos(xi+h)

f = 0
et = []
print(f' i   f(pi/3)       et')
print(f' - ----------- ----------')
n_max = 7
for n in range(n_max+1):
    if n%2==0:  # even n
        f = f + (-1)**(n/2)*np.cos(xi)*(h**n)/math.factorial(n)
    else:   # odd n
        f = f + (-1)**((n+1)/2)*np.sin(xi)*(h**n)/math.factorial(n)
    et.append((f_true-f)*100/f_true)
    print(f' {n} {f:.9} {et[n]:+.3e}')


fig, ax = plt.subplots()
plt.yscale('log')
plt.xlabel('order')
plt.ylabel('true percent error')
ax.plot(np.arange(0,n_max+1), np.abs(et), '-o')
plt.show()


