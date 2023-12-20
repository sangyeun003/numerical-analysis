import numpy as np


def build_linear_system(N):
	# input parameters:
	# N: number of segments. Therefore, there are (N+1) nodes.
	# return value: tuple (A,b) for the linear system of the "interior nodes"
	# - A: coefficient matrix
	# - b: constant column vector

	# below is the list of constants in Example 27.1 (p.795)
	h_prime = 0.01  # = h' 
	Ta = 20         
	T1 = 40         # = T(0): boundary condition
	T2 = 200        # = T(10): boundary condition
	L = 10          # length of the rod
	# TODO: build A and b
	del_x = L / N	# segment length
	c = 2 + h_prime * del_x * del_x
	val_b = h_prime * del_x * del_x * Ta
	
	# A
	A = np.zeros((N - 1, N - 1))
	A[0, 0] = c
	A[0, 1] = -1
	for i in range(1, N - 2):
		A[i, i - 1] = -1
		A[i, i] = c
		A[i, i + 1] = -1
	A[N - 2, N - 3] = -1
	A[N - 2, N - 2] = c
	
	# b
	b = np.zeros(N - 1)
	b[0] = val_b + T1
	b[1: N - 2] = val_b
	b[N - 2] = val_b + T2
	return (A, b)

