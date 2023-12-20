import numpy as np
import matplotlib.pyplot as plt

x = 0.5
xs = []
imax = 40
for i in range(imax):
    x = x - (x**10 - 1)/(10*x**9)
    xs.append(x)

print(np.array(xs))

fig, ax = plt.subplots()
plt.axhline(1, color='red', linewidth=.5)   # true solution

ax.plot(np.arange(imax), xs)

plt.show()

