import numpy as np

def Ludecomp(A, b, tol):
    # The coefficient matrix A is assumed to be square.
    try:
        ovec = Decompose(A, tol)
    except Exception as e:
        print(e.args[0])
        return None

    return Substitute(A, b, ovec)


def Decompose(A, tol):
    n = A.shape[0]

    ovec = np.arange(n) # order of rows
    svec = np.max(np.abs(A), axis=1)   # svec[i]: maximum absolute value in the i-th row

    for k in range(n):
        Pivot(A, ovec, svec, k)
        if np.abs(A[ovec[k],k]/svec[ovec[k]]) < tol:
            raise Exception(f'The pivot value is (almost) zero! {A[ovec[k],k]/svec[ovec[k]]}!')
        for i in range(k+1, n):
            factor = A[ovec[i],k]/A[ovec[k],k]
            A[ovec[i],k] = factor
            A[ovec[i],(k+1):] = A[ovec[i],(k+1):] - factor*A[ovec[k],(k+1):]

    return ovec
    
    
def Pivot(A, ovec, svec, k):
    # "p" is the index of the row in column k, 
    # among the rows on the diagonal or below.
    p = np.argmax(np.abs(A[ovec[k:],k]/svec[ovec[k:]])) + k

    if not p==k:
        ovec[[p,k]] = ovec[[k,p]] # exchange two elements.  (reference: https://www.statology.org/numpy-swap-rows)


def Substitute(A, b, ovec):
    n = A.shape[0]

    # Solve "Ly = b"
    # The result "y" is written over "b"
    for i in range(1,n):
        b[ovec[i]] = b[ovec[i]] - np.dot(A[ovec[i],:i], b[ovec[:i]])

    # Solve "Ux = y"
    x = np.zeros(n)
    x[n-1] = b[ovec[n-1]]/A[ovec[n-1],n-1]
    for i in range(n-2,-1,-1):
        x[i] = (b[ovec[i]] - np.dot(A[ovec[i],(i+1):], x[(i+1):]))/A[ovec[i],i]
    return x



n = 5
A = np.random.rand(n,n)
b = np.random.rand(n)
x_true = np.linalg.solve(A,b)

x = Ludecomp(A, b, 1e-10)
if x is None:
    print('Error while solving the linear system.')
else:
    print(np.linalg.norm(x - x_true))

   

