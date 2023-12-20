import numpy as np
from mayavi import mlab

s = 0.01
c = 7

def u(x,y):
    return s*(x**2 + x*y - 10)

def v(x,y):
    return s*(y + 3*x*y**2 - 57)

def ux(x,y):
    return s*(2*x + y)

def uy(x,y):
    return s*x

def vx(x,y):
    return s*(3*y**2)

def vy(x,y):
    return s*(1 + 6*x*y)

def tangent_plane_u(x0,y0,x,y):
    return (u(x0,y0) + (x-x0)*ux(x0,y0) + (y-y0)*uy(x0,y0))

def tangent_plane_v(x0,y0,x,y):
    return (v(x0,y0) + (x-x0)*vx(x0,y0) + (y-y0)*vy(x0,y0))

def compute_approx(x0,y0):
    A = np.array([[ux(x0,y0), uy(x0,y0)],[vx(x0,y0),vy(x0,y0)]])
    b = np.array([-u(x0,y0) + x0*ux(x0,y0) + y0*uy(x0,y0),
                  -v(x0,y0) + x0*vx(x0,y0) + y0*vy(x0,y0)])
    return np.linalg.solve(A,b)
#x0=1.5
#y0=3.5
x0=2.5
y0=4.5

X,Y=np.mgrid[-c:c:0.025,-c:c:0.025] 
Zu = u(X,Y)
Zv = v(X,Y)
Zu_tangent = tangent_plane_u(x0,y0,X,Y)
Zv_tangent = tangent_plane_v(x0,y0,X,Y)

# x-y plane
mlab.surf(X,Y,np.zeros(X.shape),color=(1,1,1))  


# u(x,y) related ------------------------------------
# surface u(x,y)
mlab.surf(X,Y,Zu,colormap='summer') 
# tangent plane of u at (x0,y0) (pink plane)
mlab.surf(X,Y,Zu_tangent,color=(1,.5,.5))   
# level set of "u(x,y)=0"   (red curve)
mlab.contour_surf(X,Y,Zu,contours=[0],color=(1,0,0),line_width=5)   
# intersection of the tangent plane with the x-y plane  (dark red line)
mlab.contour_surf(X,Y,Zu_tangent,contours=[0],color=(.5,0,0),line_width=5)  
# (x0,y0,u(x0,y0))  (pink sphere)
mlab.points3d([x0],[y0],[u(x0,y0)],[1],line_width=1,color=(1,.5,.5),scale_factor=.5)    


# v(x,y) related ------------------------------------
# surface v(x,y)
mlab.surf(X,Y,Zv,colormap='autumn') 
# tangent plane of v at (x0,y0) (light blue plane)
mlab.surf(X,Y,Zv_tangent,color=(.5,.5,1))   
# level set of "v(x,y)=0" (blue curve)
mlab.contour_surf(X,Y,Zv,contours=[0],color=(0,0,1),line_width=5)   
# intersection of the tangent plane with the x-y plane (dark blue line)
mlab.contour_surf(X,Y,Zv_tangent,contours=[0],color=(0,0,.5),line_width=5)  
#  (x0,y0,v(x0,y0)) (light blue sphere)
mlab.points3d([x0],[y0],[v(x0,y0)],[1],line_width=1,color=(.5,.5,1),scale_factor=.5)    


# true solution (gray sphere)
mlab.points3d([2],[3],[0],[1],line_width=1,color=(.5,.5,.5),scale_factor=.5)

# approximate solution (green sphere)
x = compute_approx(x0,y0)   # intersection of the red & blue lines
mlab.points3d([x[0]],[x[1]],[0],[1],line_width=1,color=(0,1,0),scale_factor=.5)

mlab.show()



