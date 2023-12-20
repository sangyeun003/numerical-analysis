import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,4,6,5])
f = np.log(x)   # natural logarithm

f10 = (f[1]-f[0])/(x[1]-x[0])
f21 = (f[2]-f[1])/(x[2]-x[1])
f32 = (f[3]-f[2])/(x[3]-x[2])

f210 = (f21 - f10)/(x[2]-x[0])
f321 = (f32 - f21)/(x[3]-x[1])

f3210 = (f321 - f210)/(x[3]-x[0])


x_test = 2
f_estimate = f[0] + f10*(x_test-x[0]) + f210*(x_test-x[0])*(x_test-x[1]) + f3210*(x_test-x[0])*(x_test-x[1])*(x_test-x[2])
f_true = np.log(x_test)

print(f'estimated value = {f_estimate}')
print(f'relative error = {np.abs((f_estimate - f_true)/f_true):.1%}')

plt.plot(x, f, 'ko')
xx = np.linspace(np.min(x),np.max(x),100)
plt.plot(xx, f[0] + f10*(xx-x[0]) + f210*(xx-x[0])*(xx-x[1]) + f3210*(xx-x[0])*(xx-x[1])*(xx-x[2]), 'r-', label='interpolating cubic polynomial')
plt.plot(xx, np.log(xx), 'b-', label='natural logarithm')
plt.legend()

plt.show()


