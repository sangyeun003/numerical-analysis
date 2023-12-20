import numpy as np
import sys
import traceback

def Gauss(A, b, tol):
    # A: coefficient matrix (assumed to be a square matrix)
    # b: constant vector
    # tol: tolerance to determine the zero value
    #      (A value is considered zero if its absolute value
    #       is smaller than "tol.")

	# 각 행의 절대 최댓값 구함
    s = np.max(np.abs(A), axis=1)
    # Now, s contains the absolute maximum value in each row.

    # step 1: elimination
    try:
        Eliminate(A, s, b, tol)
    except Exception as e:
        print(e.args[0])
        return None

    # step 2: back substitution
    return Substitute(A, b)

def Eliminate(A, s, b, tol):

    n = A.shape[0]  # number of rows/columns

    for k in range(n): # for each column

        Pivot(A, b, s, k)

        if np.abs(A[k,k]/s[k]) < tol:
            raise Exception(f'The pivot value is (almost) zero!')

        for i in range(k+1,n): # for the elements below the current pivot
            factor = A[i,k]/A[k,k]  
            A[i,:] = A[i,:] - factor*A[k,:]
            b[i] = b[i] - factor*b[k]

def Pivot(A, b, s, k):

	# "p" is the index of the row in column k, 
	# among the rows on the diagonal or below.
	# 최대값의 index를 저장
	p = np.argmax(np.abs(A[k:,k])) + k

	if not p==k:    
		# There is a large (absolute) value below the diagonal
		# So we need to exchange the rows A[k,:] and A[p,:].

		# exchanging rows (reference: https://www.statology.org/numpy-swap-rows)
		# p행과 k행 교환
		A[[p,k]] = A[[k,p]] 
		b[[p,k]] = b[[k,p]]
		s[[p,k]] = s[[k,p]]

def Substitute(A, b):
    n = A.shape[0]
    x = np.zeros(n) # solution (initialized to the zero vector)
    x[n-1] = b[n-1]/A[n-1,n-1]  # compute the last element of x
    for i in range(n-2,-1,-1):
        # np.dot(A[i,i+1:n], x[i+1:n])
        #
        # is the same as "summation" computed as below.
        #
        # summation = 0
        # for j in range(i+1,n):
        #     summation = summation + A[i,j]*x[j]
        x[i] = (b[i] - np.dot(A[i,i+1:n], x[i+1:n]))/A[i,i]
    return x


n = 5
A = np.random.rand(n,n)
b = np.random.rand(n)
x_true = np.linalg.solve(A,b)

#A = np.array([[1, 0, 1], [0, -3, 1], [2, 1, 3]], dtype=np.float64)
#b = np.array([6, 7, 15], dtype=np.float64)
#x_true = np.array([2, -1, 4], dtype=np.float64)

x = Gauss(A, b, 1e-10)
if x is None:
    print('Error while solving the linear system.')
else:
    print(f"The 2-norm of 'x-x_true' = {np.linalg.norm(x - x_true)}")
    print("The value of 'x_true' is found using numpy.linalg.solve().")

