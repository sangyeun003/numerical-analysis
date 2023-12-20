import numpy as np
import matplotlib.pyplot as plt

t = 10
g = 9.81
v = 40
m = 68.1

# (PT2.4) on p.191
def f(c):
    return (g*m/c)*(1 - np.exp(-(c/m)*t)) - v

c = np.array([4,8,12,16,20])
fc = f(c)

print(f'f(14.75) = {f(14.75)}')

fig, ax = plt.subplots()
plt.axhline(0, color='red', linewidth=.5)   # x-axis
plt.axvline(0, color='green', linewidth=.5) # y-axis

ax.plot(c, fc)

plt.show()

