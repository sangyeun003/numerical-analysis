import numpy as np

# The codes are to be tested with Python version 3.9
# 2022920027 컴퓨터과학부 박상윤

def FalsePosition(f, xl, xu, maxiter, epsilon):
    # f: function defined in the equation "f(x)=0"
    # xl, xu: initial lower/upper bound (defined on p.136)
    # maxiter: maximum iterations
    # epsilon: termination criterion ("percent relative error" defined in (3.5) on p.62)

    # return values
    # * If the solution is found, return (x,i,ea) (a 3-tuple) where
    # - x: computed approximate solution 
    # - i: number of iterations, starting with zero (first iteration)
    # - ea: percent relative error
    # * If the solution is not found within the maximum iterations, return None

    # NOTE: To compute the percent relative error, you need the "previous approximation"
    #       value in the formula (3.5) but we don't have any for the bracketing methods.
    #       So skip computing it in the first iteration and compute them from 
    #       the second iterations.

    # TODO: Implement the false-position method based on the formula (5.7) on p.136.
	f_l = f(xl)
	f_u = f(xu)
	x_r_old = 0
	for i in range(maxiter):
		x = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
		f_r = f(x)
		if x != 0:
			ea = np.abs((x - x_r_old) / x) * 100
		else:	# devision by zero
			return None
		if ea <= epsilon:
			break
		if f_l * f_r < 0:
			xu = x
		elif f_r * f_u < 0:
			xl = x
		x_r_old = x
	if ea > epsilon:
		return None
	return x, i, ea 

           

def NewtonRaphson(f, df, x0, maxiter, epsilon):
    # f: function defined in the equation "f(x)=0"
    # df: derivative of f(x)
    # x0: initial estimate/guess (defined on p.152)
    # maxiter: maximum iterations
    # epsilon: termination criterion ("percent relative error" defined in (3.5) on p.62)

    # return values
    # * If the solution is found, return (x,i,ea) (a 3-tuple) where
    # - x: computed approximate solution 
    # - i: number of iterations, starting with zero (first iteration)
    # - ea: percent relative error
    # * If the solution is not found within the maximum iterations, return None

    # TODO: Implement the Newton-Raphson method based ob the formula (6.6) on p.153.
	for i in range(maxiter):
		f_x0 = f(x0)
		df_x0 = df(x0)
		x = x0 - f_x0 / df_x0
		if x != 0:
			ea = np.abs((x - x0) / x) * 100
		else:
			return None
		if ea <= epsilon:
			break
		x0 = x
	if ea > epsilon:
		return None
	return x, i, ea



def NewtonRaphson_2x2(u, dudx, dudy, v, dvdx, dvdy, x0, y0, maxiter, epsilon):
    # u,v: functions defined in the system of nonlinear equation (p.170)
    #       u(x,y) = 0
    #       v(x,y) = 0
    # dudx, dudy: first derivatives of u(x,y) (p.173)
    # dvdx, dvdy: first derivatives of v(x,y) (p.173)
    # x0, y0: initial estimates/guesses (defined on p.152)
    # maxiter: maximum iterations
    # epsilon: termination criterion ("percent relative error" defined in (3.5) on p.62)
    #          both x and y should meet the termination criterion.


    # return values 
    # * If the solution is found, return (x,y,i,ea) (a 4-tuple) where
    # - x,y: computed approximate solutions ("None" if no solution is found within the maximum iterations)
    # - i: number of iterations, starting with zero (first iteration)
    # - ea: largest percent relative error among x and y
    # * If the solution is not found within the maximum iterations, return None

    # TODO: Implement the Newton-Raphson method to solve a 2x2 system of nonlinear equations
    #       based on the formulas in (6.24a) and (6.24b) on p.173.
	for i in range(maxiter):
		u0 = u(x0, y0)
		v0 = v(x0, y0)
		dudx0 = dudx(x0, y0)
		dudy0 = dudy(x0, y0)
		dvdx0 = dvdx(x0, y0)
		dvdy0 = dvdy(x0, y0)
		x = x0 - (u0 * dvdy0 - v0 * dudy0) / (dudx0 * dvdy0 - dudy0 * dvdx0)
		y = y0 - (v0 * dudx0 - u0 * dvdx0) / (dudx0 * dvdy0 - dudy0 * dvdx0)
		if x != 0:
			ea_x = np.abs((x - x0) / x) * 100
		else:
			return None
		if y != 0:
			ea_y = np.abs((y - y0) / y) * 100
		else:
			return None
		if ea_x > ea_y:
			ea = ea_x
		else:
			ea = ea_y
		if ea <= epsilon:
			break
		x0 = x
		y0 = y
	if ea > epsilon:
		return None
	return x, y, i, ea


def Muller(f, xr, h, eps, maxit):
    # f: polynomial function defined in the equation "f(x)=0"
    # xr: initial guess
    # h: value to be used to perturb xr to obtain two more initial guesses (explained on p.187)
    # eps: termination criterion
    # maxit: maximum number of iterations

    # return values
    # * If the solution is found, return (x,i,ea) (a 3-tuple) where
    # - x: computed approximate solution 
    # - i: number of iterations, starting with zero (first iteration)
    # - ea: percent relative error
    # * If the solution is not found within the maximum iterations, return None


    # TODO: Implement the pseudocode in Figure 7.4 in python3.

    # NOTE:
    # - On the 23th line in the pseudocode, 
    #   "IF(|dxr| < eps*xr OR iter>=maxit) EXIT"
    #   both successful and failed cases are handled.
    #   (1) |dxr|<eps*xr  --> successful case
    #                         When exiting (returning) the function, 
    #                         the solution is stored in "xr".
    #   (2) iter>=maxit   --> failed case
    #   When you implement the Muller's method, you have to handle the cases separately.
	x2 = xr
	x1 = xr + h * xr
	x0 = xr - h * xr
	for i in range(maxit):
		h0 = x1 - x0
		h1 = x2 - x1
		d0 = (f(x1) - f(x0)) / h0
		d1 = (f(x2) - f(x1)) / h1
		a = (d1 - d0) / (h1 + h0)
		b = a * h1 + d1
		c = f(x2)
		rad = np.sqrt(b * b - 4 * a * c)
		if np.abs(b + rad) > np.abs(b - rad):
			den = b + rad
		else:
			den = b - rad
		if den != 0:
			dxr = -2 * c / den
		xr = x2 + dxr
		if xr != 0:
			ea = np.abs(dxr / xr) * 100
		if ea <= eps:
			break
		x0 = x1
		x1 = x2
		x2 = xr
	if ea > eps:
		return None
	return xr, i, ea
   

def GaussJordan(A,b):
	# Solve the linear system "Ax=b"

	# The following two lines are pre-implemented to provide you
	# the corresponding values in the pseudocode.

	# A = square matrix
	aug = np.hstack((A,b.reshape((b.shape[0], 1))))
	m,n = aug.shape

	# aug: The augmented matrix [A|b]
	# m: number of rows of "aug"
	# n: number of columns of "aug"

	# TODO: Implement the pseudocode in Figure 9.10 on p.279.

	# NOTE: 
	# (1) Assume that there exists a unique solution.
	#     You don't have to handle singular cases. (Non-invertible matrix "A")
	# (2) Whenever possible, remove a loop and replace it with numpy indexing syntax.
	#     (Refer to "Fig_9_6_Gauss.py".)
	for i in range(m):
		aug[i] = aug[i] / aug[i, i]
		for j in range(m):
			if i != j:
				factor = aug[j, i] / aug[i][i]
				aug[j] = aug[j] - factor * aug[i]
	x = aug[:, -1]
	return x

def Jacobi(A, b, x0, maxiter, epsilon):
    # Solve the linear system "Ax=b"
    # x0: initial guess
    # maxiter: number of maximum iterations
    # epsilon: termination criterion
    
    # TODO: Implement the Jacobi method.
    # Whenever possible, remove a loop and replace it with numpy indexing syntax.
    # (Refer to "Fig_9_6_Gauss.py".)
    # https://numpy.org/doc/stable/user/basics.indexing.html

    # Bonus points: If you use ONLY ONE loop (for iterations), you can get extra points!
	for iter in range(maxiter):
		x_new = (b - A @ x0 + A.diagonal() * x0) / A.diagonal()
		if (np.linalg.norm(x_new) != 0):
			ea = np.linalg.norm(x_new - x0) / np.linalg.norm(x_new) * 100
		if (ea <= epsilon):
			break
		x0 = x_new
	if ea > epsilon:
		return None
	return x_new, iter, ea

