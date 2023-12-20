import numpy as np

# input parameters
# - f: function to integrate
# - a,b: integration interval
# - Ns: array of number of segments

# return value
# - I: integral values (of type numpy.array)
#      I[i] is the integral values using Ns[i] number of segments

# Composite Rectangle Method with left point
def composite_rectangle_left(f, a, b, Ns):
	I = np.zeros((len(Ns),))
	# TODO: Fill this part
	n = len(Ns)
	h = (b - a) / Ns				# x들의 간격(밑변)
	for i in range(n):
		x = np.linspace(a, b, Ns[i] + 1)	# a부터 b까지 등간격으로 나눈 (Ns[i] + 1)개 x값(index: 0 ~ Ns[i]) -> Ns[i]개의 사다리꼴
		sum = 0
		for j in range(Ns[i]):				# 0 ~ Ns[i - 1]까지 총 Ns[i]번
			sum += f(x[j]) * h[i]
		I[i] = sum
	return I

# Composite Midpoint Method
def composite_midpoint(f, a, b, Ns):
	I = np.zeros((len(Ns),))
	# TODO: Fill this part
	n = len(Ns)
	h = (b - a) / Ns				# x들의 간격(밑변)
	for i in range(n):
		x = np.linspace(a, b, Ns[i] + 1)	# a부터 b까지 등간격으로 나눈 (Ns[i] + 1)개 x값(index: 0 ~ Ns[i]) -> Ns[i]개의 사다리꼴
		sum = 0
		for j in range(Ns[i]):				# 0 ~ Ns[i - 1]까지 총 Ns[i]번
			sum += f((x[j] + x[j + 1]) / 2) * h[i]
		I[i] = sum
	return I

# Composite Trapezoidal Method
def composite_trapezoidal(f, a, b, Ns):
	I = np.zeros((len(Ns),))
	# TODO: Fill this part
	n = len(Ns)
	h = (b - a) / Ns				# x들의 간격(밑변)
	for i in range(n):
		x = np.linspace(a, b, Ns[i] + 1)	# a부터 b까지 등간격으로 나눈 (Ns[i] + 1)개 x값(index: 0 ~ Ns[i]) -> Ns[i]개의 사다리꼴
		sum = 0
		for j in range(Ns[i]):				# 0 ~ Ns[i - 1]까지 총 Ns[i]번
			sum += (f(x[j]) + f(x[j + 1])) / 2 * h[i]
		I[i] = sum
	return I

# Composite Simpson's 1/3 Method
def composite_Simpson_1_3rd(f, a, b, Ns):
	I = np.zeros((len(Ns),))
	# TODO: Fill this part
	# n = len(Ns)
	# h = (b - a) / Ns				# x들의 간격(밑변)
	# for i in range(n):
	# 	x = np.linspace(a, b, Ns[i] + 1)	# a부터 b까지 등간격으로 나눈 (Ns[i] + 1)개 x값(index: 0 ~ Ns[i]) -> Ns[i]개의 사다리꼴
	# 	sum = 0
	# 	for j in range(0, Ns[i], 2):				# 0 ~ Ns[i - 1]까지 총 Ns[i]번
	# 		sum += (f(x[j]) + 4 * f(x[j + 1]) + f(x[j + 2])) / 3 * h[i]
	# 	I[i] = sum
	# 공식 이용
	n = len(Ns)
	for i in range(n):
		x = np.linspace(a, b, Ns[i] + 1)	# Ns[i] = segment 개수 = n
		h = (b - a) / Ns[i]
		first = f(a)
		second = 4 * np.sum(f(x[1: -1: 2]))
		third = 2 * np.sum(f(x[2: -2: 2]))
		fourth = f(b)
		I[i] = (first + second + third + fourth) * h / 3
	return I

# Composite Simpson's 3/8 Method
def composite_Simpson_3_8th(f, a, b, Ns):
	I = np.zeros((len(Ns),))
	# TODO: Fill this part
	# n = len(Ns)
	# h = (b - a) / Ns				# x들의 간격(밑변)
	# for i in range(n):
	# 	x = np.linspace(a, b, Ns[i] + 1)	# a부터 b까지 등간격으로 나눈 (Ns[i] + 1)개 x값(index: 0 ~ Ns[i]) -> Ns[i]개의 사다리꼴
	# 	sum = 0
	# 	for j in range(0, Ns[i], 3):				# 0 ~ Ns[i - 1]까지 총 Ns[i]번
	# 		sum += (f(x[j]) + 3 * f(x[j + 1]) + 3 * f(x[j + 2]) + f(x[j + 3])) * 3 / 8 * h[i]
	# 	I[i] = sum
	# 공식 이용
	n = len(Ns)
	for i in range(n):
		x = np.linspace(a, b, Ns[i] + 1)	# Ns[i] = segment 개수 = n
		h = (b - a) / Ns[i]
		first = f(a)
		second = 3 * np.sum(f(x[1: -2: 3]) + f(x[2: -1: 3]))
		third = 2 * np.sum(f(x[3: -3: 3]))
		fourth = f(b)
		I[i] = (first + second + third + fourth) * h * 3 / 8
	return I


