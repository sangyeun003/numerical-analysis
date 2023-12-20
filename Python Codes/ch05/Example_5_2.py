import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(10*x) + np.cos(3*x)

x = np.arange(0, 5, 0.001)
y = f(x)

fig, (ax_a, ax_b, ax_c) = plt.subplots(nrows=1, ncols=3, figsize=(18,6))

ax_a.plot(x, y)
ax_a.set_xlim([0,5])
ax_a.set_ylim([-2,2])
ax_a.axhline(0, color='red', linewidth=.5)   # x-axis

ax_b.plot(x, y)
ax_b.set_xlim([3,5])
ax_b.set_ylim([-2,2])
ax_b.axhline(0, color='red', linewidth=.5)   # x-axis

ax_c.plot(x, y)
ax_c.set_xlim([4.2,4.3])
ax_c.set_ylim([-0.15,0.15])
ax_c.axhline(0, color='red', linewidth=.5)   # x-axis

plt.show()



