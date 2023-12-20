import numpy as np
import matplotlib.pyplot as plt

x = np.array([2,9])
y = np.array([1,6])
f = np.array([[60, 55], [57.5, 70]])    # [[f(x0,y0), f(x0,y1)], [f(x1,y0), f(x1,y1)]]

def bilinear_interpolation(xx,yy):
    fi0 = f[0,0]*(xx-x[1])/(x[0]-x[1]) + f[1,0]*(xx-x[0])/(x[1]-x[0])
    fi1 = f[0,1]*(xx-x[1])/(x[0]-x[1]) + f[1,1]*(xx-x[0])/(x[1]-x[0])
    return fi0*(yy-y[1])/(y[0]-y[1]) + fi1*(yy-y[0])/(y[1]-y[0])

xx,yy = np.meshgrid(np.linspace(np.min(x), np.max(x), 100),
                    np.linspace(np.min(y), np.max(y), 100))

zz = bilinear_interpolation(xx.flatten(), yy.flatten()).reshape(xx.shape)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(xx, yy, zz)

ax.scatter([x[0],x[0],x[1],x[1]], [y[0], y[1],y[0],y[1]], f.flatten(), c='red')
plt.show()


