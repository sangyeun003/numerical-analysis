import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

m = 50
n = 50

map_index_solution = np.reshape(np.arange(m*(n+1)), (m,(n+1)), order="F")
map_index = -np.ones((m+2,n+2), dtype=np.int32)
map_index[1:-1,0:-1] = map_index_solution

#print(map_index)

b = np.zeros((m*(n+1),))
A = np.zeros((m*(n+1),m*(n+1)))

# boundary conditions
X0 = 75
X1 = 50
#Y0 = 0
Y1 = 100


for x in range(1,m+1):
    for y in range(0,n+1):
        r = map_index[x,y]

        if x-1==0:
            b[r] = b[r] + X0
        else:
            A[r,map_index[x-1,y]] = -1
        if x+1==m+1:
            b[r] = b[r] + X1
        else:
            A[r,map_index[x+1,y]] = -1
 
        if y==0:    # lower edge
            A[r,map_index[x,1]] = -2
        else:
            A[r,map_index[x,y-1]] = -1
            if y+1==n+1:
                b[r] = b[r] + Y1
            else:
                A[r,map_index[x,y+1]] = -1
        A[r,r] = 4

print(A)
print(b)

T_solution = np.linalg.solve(A,b)

T = np.zeros((m+2,n+2))

for x in range(m+2):
    for y in range(n+2):
        if x==0:
            T[x,y] = X0
        elif x==m+1:
            T[x,y] = X1
#        elif y==0:
#            T[x,y] = Y0
        elif y==n+1:
            T[x,y] = Y1
        else:
            T[x,y] = T_solution[map_index[x,y]]

T = T.T

x,y = np.meshgrid(np.arange(m+2),np.arange(n+2))


#plt.contour(T,np.linspace(0,100,10))
#plt.show()


ax = plt.axes(projection ='3d') 
ax.plot_surface(x, y, T, cmap=cm.coolwarm)
plt.show()



