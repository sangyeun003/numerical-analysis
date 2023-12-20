import numpy as np

#sum1 = np.half(0)
#sum2 = np.half(0)
#sum3 = np.single(0)
#x1 = np.half(1)
#x2 = np.half(1e-5)
#x3 = np.single(1e-5)
sum1 = np.single(0)
sum2 = np.single(0)
sum3 = np.double(0)
x1 = np.single(1)
x2 = np.single(0.00001)
x3 = np.double(0.00001)

for i in range(100000):
    sum1 = sum1 + x1
    sum2 = sum3 + x2
    sum3 = sum3 + x3

print(f'sum1 = {sum1}')
print(f'sum2 = {sum2}')
print(f'sum3 = {sum3}')
