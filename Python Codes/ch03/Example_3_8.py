import numpy as np

x1_true = -0.001
x2_true = -3000

a = np.single(1)
b = np.single(3000.001)
c = np.single(3)
d = np.sqrt(b*b - np.single(4)*a*c)
x1 = (-b+d)/(np.single(2)*a)
x2 = (-b-d)/(np.single(2)*a)

print(f'single precision')
print(f'  x1 = {x1:.4e}, et = {abs(100*(x1-x1_true)/x1):.2f}%')
print(f'  x2 = {x2:.4e}, et = {abs(100*(x2-x2_true)/x2):.2f}%')

x1 = np.single(-2)*c/(b+d)
print(f'  x1 (modified formula) = {x1:.4e}, et = {abs(100*(x1-x1_true)/x1):.2f}%')


a = np.double(1)
b = np.double(3000.001)
c = np.double(3)
d = np.sqrt(b*b - np.double(4)*a*c)
x1 = (-b+d)/(np.double(2)*a)
x2 = (-b-d)/(np.double(2)*a)

print(f'double precision')
print(f'  x1 = {x1:.4e}, et = {abs(100*(x1-x1_true)/x1):.2f}%')
print(f'  x2 = {x2:.4e}, et = {abs(100*(x2-x2_true)/x2):.2f}%')
