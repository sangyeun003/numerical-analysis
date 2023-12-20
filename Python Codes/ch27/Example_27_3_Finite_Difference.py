import numpy as np

h_prime = 0.01
Ta = 20
T1 = 40
T2 = 200
h = 2   # delta x
c = 2 + h_prime*h**2
b = h_prime*h**2*Ta

A = np.array([
        [ c,-1, 0, 0],
        [-1, c,-1, 0],
        [ 0,-1, c,-1],
        [ 0, 0,-1, c]])
b = np.array([b + T1,b,b,b + T2])

T = np.linalg.solve(A,b)

np.set_printoptions(precision=4)    # to print 4 decimal places

print(np.array([T1, T[0], T[1], T[2], T[3], T2]))
            
