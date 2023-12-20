import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([0, 2, 2.5, 1, 4, 7])
x2 = np.array([0, 1, 2, 3, 6, 2])
y = np.array([5, 10, 9, 0, 3, 27])

n = len(y)

A = np.array([[     n,     np.sum(x1),    np.sum(x2)],
              [np.sum(x1), np.dot(x1,x2), np.dot(x1,x2)],
              [np.sum(x2), np.dot(x1,x2), np.dot(x2,x2)]])
b = np.array([np.sum(y), np.dot(x1,y), np.dot(x2,y)])

a = np.linalg.solve(A,b)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x1,x2,y, c='red', alpha=1)
xx1,xx2 = np.meshgrid([0,7],[0,6])
yy = a[0] + a[1]*xx1 + a[2]*xx2
ax.plot_surface(xx1,xx2,yy)
plt.show()

