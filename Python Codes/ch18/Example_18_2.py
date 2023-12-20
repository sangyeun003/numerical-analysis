import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,4,6])
f = np.log(x)   # natural logarithm
print(f)

b0 = f[0]
b1 = (f[1]-f[0])/(x[1]-x[0])
b2 = ((f[2]-f[1])/(x[2]-x[1]) - (f[1]-f[0])/(x[1]-x[0]))/(x[2]-x[0])

plt.plot(x, f, 'ko')
xx = np.linspace(x[0],x[2],100)
plt.plot(xx, b0 + b1*(xx - x[0]) + b2*(xx - x[0])*(xx - x[1]), 'r-', label='interpolating quadratic polynomial')
plt.plot(xx, np.log(xx), 'b-', label='natural logarithm')
plt.legend()

plt.show()

