import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

def f(x,y):
    return 0.1*(x**2 + y**2 - 25)

def g(x,y):
    return 0.1*((2/3)*x**2 - y - 2)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

X = np.arange(-6, 6, 0.25)
Y = np.arange(-6, 6, 0.25)
X, Y = np.meshgrid(X, Y)
Zf = f(X,Y)
Zg = g(X,Y)

surf = ax.plot_surface(X,Y,Zf,cmap=cm.coolwarm, linewidth=0, antialiased=False, zorder=0.1)
ax.contour(X,Y,Zf, 0, zdir='z', offset=-4, colors = ['red'])

surf = ax.plot_surface(X,Y,Zg,cmap=cm.coolwarm, linewidth=0, antialiased=False, zorder=0.1)
ax.contour(X,Y,Zg, 0, zdir='z', offset=-4, colors = ['blue'])

ax.set_zlim(-4, 4)

plt.show()


