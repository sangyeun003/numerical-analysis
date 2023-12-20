import numpy as np
from functools import reduce

def polynomial_regression(dataset, degree):
    # input parameters
    # - dataset: n x 2 matrix (numpy.array) containing the dataset
    #  * dataset[:,0]: x-coordinates
    #  * dataset[:,1]: y-coordinates
    # - degree: polynomial degree for regression

    # return value:
    # - An array of coefficients of the fitting polynomial. (size degree+1)
    # - The array should contain the polynomial coefficients in the ascending order.
    #    [a_0,a_1,a_2,...a_d] ( d = degree ) 


    # NOTE: You can use "np.linalg.solve" to solve a linear system.
	
	n = dataset.shape[0]	# data 수

	x = dataset[:, 0]
	y = dataset[:, 1]
	A = np.zeros((degree + 1, degree + 1))
	B = np.zeros(degree + 1)
	for i in range (degree + 1):
		for j in range (i + 1):
			k = i + j
			sum = 0
			for l in range (0, n):
				sum += pow(x[l], k)
			A[i, j] = sum
			A[j, i] = sum
		sum = 0
		for j in range (n):
			sum += pow(x[j], i) * y[j]
		B[i] = sum
	return np.linalg.solve(A, B)