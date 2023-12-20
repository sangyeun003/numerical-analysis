import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

def f_0th(x):
    return 1.2*x**0

def f_1st(x):
    return 1.2 -0.25*x

def f_2nd(x):
    return 1.2 -0.25*x -0.5*x**2

delta = 0.1

x = np.linspace(0-delta,1+delta,100)	# 100보다 작은 수 할수록 완만하지 않은 그래프 됨.

fig, ax = plt.subplots()

ax.plot(x, f(x), 'k-', 1, f(1), 'ko')
ax.plot(x, f_0th(x), 'r-', 1, f_0th(1), 'ro')
ax.plot(x, f_1st(x), 'b-', 1, f_1st(1), 'bo')
ax.plot(x, f_2nd(x), 'g-', 1, f_2nd(1), 'go')

plt.show()


