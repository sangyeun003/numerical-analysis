import numpy as np

# 25.1 Euler's explicit method (p.722)
def Euler_explicit(f, a, b, hs, y0):
    ys = np.empty((len(hs),))
    # ys[j] contains y(b) computed with the step size hs[j].
    for j in range(len(hs)):
        h = hs[j]
        x = np.arange(a, b + h, h)	# a부터 b까지 h 간격으로..
        n = len(x)
        y = np.zeros((n,))
        y[0] = y0
        for i in range(n - 1):
            slope = f(x[i], y[i])
            y[i + 1] = y[i] + slope * h
        ys[j] = y[-1]
    return ys

# 25.2.1. Heun's method (p.734)
def Heun(f, a, b, hs, y0):
	ys = np.zeros((len(hs),))
	# TODO: Fill ys. ys[j] contains y(b) computed with the step size hs[j].
	for j in range(len(hs)):
		h = hs[j]
		x = np.arange(a, b + h, h)
		n = len(x)
		y = np.zeros((n,))
		y[0] = y0
		for i in range(n - 1):
			temp_new_y = y[i] + f(x[i], y[i]) * h
			slope = (f(x[i], y[i]) + f(x[i + 1], temp_new_y)) / 2
			y[i + 1] = y[i] + slope * h
		ys[j] = y[-1]
	return ys

# 25.2.2. Midpoint method (p.738)
def midpoint(f, a, b, hs, y0):
	ys = np.zeros((len(hs),))
	# TODO: Fill ys. ys[j] contains y(b) computed with the step size hs[j].
	for j in range(len(hs)):
		h = hs[j]
		x = np.arange(a, b + h, h)	# a부터 b까지 h 간격으로..
		n = len(x)
		y = np.zeros((n,))
		y[0] = y0
		for i in range(n - 1):
			y_05= y[i] + f(x[i], y[i]) * h / 2
			slope = f(x[i] + 0.5 * h, y_05)
			y[i + 1] = y[i] + slope * h
		ys[j] = y[-1]
	return ys

# Ralston's method (p.744)
def Ralston(f, a, b, hs, y0):
	ys = np.zeros((len(hs),))
	# TODO: Fill ys. ys[j] contains y(b) computed with the step size hs[j].
	for j in range(len(hs)):
		h = hs[j]
		x = np.arange(a, b + h, h)	# a부터 b까지 h 간격으로..
		n = len(x)
		y = np.zeros((n,))
		y[0] = y0
		for i in range(n - 1):
			k1 = f(x[i], y[i])
			k2 = f(x[i] + 0.75 * h, y[i] + 0.75 * k1 * h)
			slope = 1 / 3 * k1 + 2 / 3 * k2
			y[i + 1] = y[i] + slope * h
		ys[j] = y[-1]
	return ys

# 3rd order Runge-Kutta method (classical, p.746-747)
def RK3_classical(f, a, b, hs, y0):
	ys = np.zeros((len(hs),))
	# TODO: Fill ys. ys[j] contains y(b) computed with the step size hs[j].
	for j in range(len(hs)):
		h = hs[j]
		x = np.arange(a, b + h, h)	# a부터 b까지 h 간격으로..
		n = len(x)
		y = np.zeros((n,))
		y[0] = y0
		for i in range(n - 1):
			k1 = f(x[i], y[i])
			k2 = f(x[i] + 0.5 * h, y[i] + 0.5 * k1 * h)
			k3 = f(x[i] + h, y[i] - k1 * h + 2 * k2 * h)
			slope = (k1 + 4 * k2 + k3) / 6
			y[i + 1] = y[i] + slope * h
		ys[j] = y[-1]
	return ys

# 3rd order Runge-Kutta method (Nystrom's): See the slide
def RK3_Nystrom(f, a, b, hs, y0):
	ys = np.zeros((len(hs),))
	# TODO: Fill ys. ys[j] contains y(b) computed with the step size hs[j].
	for j in range(len(hs)):
		h = hs[j]
		x = np.arange(a, b + h, h)	# a부터 b까지 h 간격으로..
		n = len(x)
		y = np.zeros((n,))
		y[0] = y0
		for i in range(n - 1):
			k1 = f(x[i], y[i])
			k2 = f(x[i] + 2 / 3 * h, y[i] + 2 / 3 * k1 * h)
			k3 = f(x[i] + 2 / 3 * h, y[i] + 2 / 3 * k2 * h)
			slope = 2 / 8 * k1 + 3 / 8 * k2 + 3 / 8 * k3
			y[i + 1] = y[i] + slope * h
		ys[j] = y[-1]
	return ys

# 25.3.3. 4th order Runge-Kutta method (classical) (p.747)
def RK4_classical(f, a, b, hs, y0):
	ys = np.zeros((len(hs),))
	# TODO: Fill ys. ys[j] contains y(b) computed with the step size hs[j].
	for j in range(len(hs)):
		h = hs[j]
		x = np.arange(a, b + h, h)	# a부터 b까지 h 간격으로..
		n = len(x)
		y = np.zeros((n,))
		y[0] = y0
		for i in range(n - 1):
			k1 = f(x[i], y[i])
			k2 = f(x[i] + 0.5 * h, y[i] + 0.5 * k1 * h)
			k3 = f(x[i] + 0.5 * h, y[i] + 0.5 * k2 * h)
			k4 = f(x[i] + h, y[i] + k3 * h)
			slope = (k1 + 2 * k2 + 2 * k3 + k4) / 6
			y[i + 1] = y[i] + slope * h
		ys[j] = y[-1]
	return ys