import numpy as np

# A biquadratic function is a bi-variate polynomial of x & y
# which interpolates 3x3 data points c.
# How to find the biquadratic function f(x,y)?
# (1) Find the quadratic polynomial c0(x) interpolating c[0,0], c[0,1], c[0,2] along the x-axis.
# (2) Find the quadratic polynomial c1(x) interpolating c[1,0], c[1,1], c[1,2] along the x-axis.
# (3) Find the quadratic polynomial c2(x) interpolating c[2,0], c[2,1], c[2,2] along the x-axis.
# (4) Find the quadratic polynomial f(x,y) interpolating c0(x), c1(x), c2(x) along the y-axis.

def quadratic_interpolation(x, x0, x1, x2, y0, y1, y2):
	b0 = y0
	b1 = (y1 - y0) / (x1 - x0)
	b2 = ((y2 - y1) / (x2 - x1) - (y1 - y0) / (x1 - x0)) / (x2 - x0)
	return b0 + b1 * (x - x0) + b2 * (x - x0) * (x - x1)

def biquadratic(c, x, y):
    # Let n be the number of points to be evaluated.
    #
    # x: n-dimensional array containing the x-coordinates of the points to be evaluated
    # y: n-dimensional array containing the y-coordinates of the points to be evaluated
    # c: 3x3 array containing the points to be evaluated. c[i,j] is the value at (i,j).

    # return value: the n-dimensional array (in type numpy.array) 
    #               composed of the value of the bi-quadratic function at (x,y)
    #               If "v" is the return value, "v[i]" is the bi-quadratic function value of (x[i],y[i])
	n = len(x)
	# c0_y = quadratic_interpolation(y, 0, 1, 2, c[0, 0], c[0, 1], c[0, 2])
	# c1_y = quadratic_interpolation(y, 0, 1, 2, c[1, 0], c[1, 1], c[1, 2])
	# c2_y = quadratic_interpolation(y, 0, 1, 2, c[2, 0], c[2, 1], c[2, 2])

	# f = quadratic_interpolation(x, 0, 1, 2, c0_y, c1_y, c2_y)

	c0_x = quadratic_interpolation(x, 0, 1, 2, c[0, 0], c[1, 0], c[2, 0])
	c1_x = quadratic_interpolation(x, 0, 1, 2, c[0, 1], c[1, 1], c[2, 1])
	c2_x = quadratic_interpolation(x, 0, 1, 2, c[0, 2], c[1, 2], c[2, 2])

	f = quadratic_interpolation(y, 0, 1, 2, c0_x, c1_x, c2_x)
	return f