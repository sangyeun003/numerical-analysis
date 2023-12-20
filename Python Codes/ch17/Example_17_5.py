import numpy as np
from functools import reduce
import matplotlib.pyplot as plt

x = np.arange(6)
y = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

n = len(x)
m = 2   # Quadratic polynomial (degreee 2)

Sx0 = n
Sx1 = np.sum(x)
Sx2 = reduce(lambda x,y: x + y**2, x, 0)	# 위에거랑 다른 y, Sx2 = np.sum(x**2)랑 같음
Sx3 = reduce(lambda x,y: x + y**3, x, 0)
Sx4 = reduce(lambda x,y: x + y**4, x, 0)
Sy = np.sum(y)
Sxy = np.dot(x,y)
Sxxy = np.dot(x**2,y)

A = np.array([[Sx0, Sx1, Sx2],
              [Sx1, Sx2, Sx3],
              [Sx2, Sx3, Sx4]])
b = np.array([Sy,Sxy,Sxxy])

a = np.linalg.solve(A,b)    # a = [a0,a1,a2]

plt.plot(x,y,'o')
xx = np.linspace(0,5,100)
# We have to "flip" a to make it [a2,a2,a0]
# See https://numpy.org/doc/stable/reference/generated/numpy.polyval.html
# polyval(): polynomial을 evaluate 해줌
plt.plot(xx,np.polyval(np.flip(a),xx),'-r')	# coefficient를 내림차순으로 해줘야함(flip) 
plt.show()



