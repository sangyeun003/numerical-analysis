import numpy as np

def GaussSeidel(A, b, imax, es, w):
    n = A.shape[0]
    x = np.zeros(n)
    for i in range(n):
        A[i,:] = A[i,:]/A[i,i]
        b[i] = b[i]/A[i,i]
    for i in range(n):
        x[i] = b[i] - np.dot(A[i,:i],x[:i]) - np.dot(A[i,i+1:],x[i+1:])

    print(x)

    for iter in range(imax+1):
        sentinel = 1
        for i in range(n):
            old_xi = x[i]
            x[i] = w*(b[i] - np.dot(A[i,:i],x[:i]) - np.dot(A[i,i+1:],x[i+1:])) + (1-w)*old_xi
            if sentinel == 1 and not x[i] == 0:
                ea = np.abs((x[i]-old_xi)/x[i])*100
                if ea > es:
                    sentinel = 0
        if sentinel==1:
            return (x,iter)
        print(x)
    return (None,iter)


n = 5
A = np.random.rand(n,n)
np.fill_diagonal(A, 10.0*np.diagonal(A))    # Scale the diagonal entries to make the algorithm converge...
b = np.random.rand(n)

#A = np.array([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]], dtype=np.float64)
#b = np.array([7.85, -19.3, 71.4], dtype=np.float64)

x,iter = GaussSeidel(A, b, 100, 1e-5, 1)

print(iter)

print(np.dot(A, x) - b)
