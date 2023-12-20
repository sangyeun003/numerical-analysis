import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def solve_ex30_3(T0, TL, delta_x, delta_t, t_end):
	# input parameters
	# - T0      : fixed temperature at x=0
	# - TL      : fixed temperature at x=L
	# - delta_x : step size along x (location)
	# - delta_t : step size along t (time)
	# - t_end   : ending time

	# return value: T
	# i-th row of T: temperature distribution at time i
	# j-th column of T: temperature change at node j

	L = 10
	_lambda = 0.020875

	# TODO: Compute T
	x = np.arange(0, L + delta_x, delta_x)
	t = np.arange(0, t_end + delta_t, delta_t)

	M = len(x) - 2

	T = np.zeros((len(t), len(x)))

	T[:, 0] = T0
	T[:, -1] = TL

	A = np.zeros((M, M))
	b = np.zeros(M)

	A[0, : 2] = np.array([[2 * (1 + _lambda), -_lambda]])
	for i in range(1, M - 1):
		A[i, (i - 1) : (i + 2)] = np.array([-_lambda, 2 * (1 + _lambda), -_lambda]) 
	A[M - 1, -2 : ] = np.array([-_lambda, 2 * (1 + _lambda)])

	for l in range(len(t) - 1):
		b[0] = _lambda * T0 + 2 * (1 - _lambda) * T[l, 1] + _lambda * T[l, 2] + _lambda * T0
		b[1 : M - 1] = _lambda * T[l, 1 : M - 1] + 2 * (1 - _lambda) * T[l, 2 : M] + _lambda * T[l, 3 : M + 1]
		b[M - 1] = _lambda * TL + 2 * (1 - _lambda) * T[l, M] + _lambda * T[l, M - 1] + _lambda * TL
		T[l + 1, 1 : -1] = np.linalg.solve(A, b)

	return T


