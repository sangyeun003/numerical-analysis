import numpy as np
import matplotlib.pyplot as plt

t = np.array([1,3,5,7,13])
v = np.array([800, 2310, 3090, 3940, 4755])

# quartic polynomial interpolating (t0,v0),...,(t4,v4)
def p4(x):
    return (v[0]*np.prod([x-t[1],x-t[2],x-t[3],x-t[4]],axis=0)/np.prod([t[0]-t[1],t[0]-t[2],t[0]-t[3],t[0]-t[4]])
          + v[1]*np.prod([x-t[0],x-t[2],x-t[3],x-t[4]],axis=0)/np.prod([t[1]-t[0],t[1]-t[2],t[1]-t[3],t[1]-t[4]])
          + v[2]*np.prod([x-t[0],x-t[1],x-t[3],x-t[4]],axis=0)/np.prod([t[2]-t[0],t[2]-t[1],t[2]-t[3],t[2]-t[4]])
          + v[3]*np.prod([x-t[0],x-t[1],x-t[2],x-t[4]],axis=0)/np.prod([t[3]-t[0],t[3]-t[1],t[3]-t[2],t[3]-t[4]])
          + v[4]*np.prod([x-t[0],x-t[1],x-t[2],x-t[3]],axis=0)/np.prod([t[4]-t[0],t[4]-t[1],t[4]-t[2],t[4]-t[3]]))

# cubic polynomial interpolating (t1,v1),(t2,v2),(t3,v3),(t4,v4)
def p3(x):
    return (v[1]*np.prod([x-t[2],x-t[3],x-t[4]],axis=0)/np.prod([t[1]-t[2],t[1]-t[3],t[1]-t[4]])
          + v[2]*np.prod([x-t[1],x-t[3],x-t[4]],axis=0)/np.prod([t[2]-t[1],t[2]-t[3],t[2]-t[4]])
          + v[3]*np.prod([x-t[1],x-t[2],x-t[4]],axis=0)/np.prod([t[3]-t[1],t[3]-t[2],t[3]-t[4]])
          + v[4]*np.prod([x-t[1],x-t[2],x-t[3]],axis=0)/np.prod([t[4]-t[1],t[4]-t[2],t[4]-t[3]]))

# quadratic polynomial interpolating (t2,v2),(t3,v3),(t4,v4)
def p2(x):
    return (v[2]*np.prod([x-t[3],x-t[4]],axis=0)/np.prod([t[2]-t[3],t[2]-t[4]])
          + v[3]*np.prod([x-t[2],x-t[4]],axis=0)/np.prod([t[3]-t[2],t[3]-t[4]])
          + v[4]*np.prod([x-t[2],x-t[3]],axis=0)/np.prod([t[4]-t[2],t[4]-t[3]]))

# linear polynomial interpolating (t3,v3),(t4,v4)
def p1(x):
    return (v[3]*(x-t[4])/(t[3]-t[4])
          + v[4]*(x-t[3])/(t[4]-t[3]))



tt = np.linspace(0, 15, 100)

fig, ax = plt.subplots(2,2)

ax[0,0].plot(t, v, 'ob')
ax[0,0].plot(tt, p4(tt), 'k-')
ax[0,0].set_ylim(0,6000)

ax[0,1].plot(t, v, 'ob')
ax[0,1].plot(tt, p3(tt), 'k-')
ax[0,1].set_ylim(0,6000)

ax[1,0].plot(t, v, 'ob')
ax[1,0].plot(tt, p2(tt), 'k-')
ax[1,0].set_ylim(0,6000)

ax[1,1].plot(t, v, 'ob')
ax[1,1].plot(tt, p1(tt), 'k-')
ax[1,1].set_ylim(0,6000)

plt.show()
