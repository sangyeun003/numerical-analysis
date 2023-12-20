import numpy as np

def f(x,y):
    return 4*np.exp(0.8*x) - 0.5*y

def y_true(x):
    return (4/1.3)*(np.exp(0.8*x) - np.exp(-0.5*x)) + 2*np.exp(-0.5*x)

x = np.arange(0,5)
y_Heun_1 = [2]    # initial condition: y[0] = 2
y_Heun_15 = [2]    # initial condition: y[0] = 2
y_true = y_true(x)
h = 1

for i in range(0,len(x)-1):
    slope_1 = f(x[i],y_Heun_1[i])
    y_next = y_Heun_1[i] + slope_1*h
    slope_2 = f(x[i+1],y_next)
    y_Heun_1.append(y_Heun_1[i] + h*(slope_1+slope_2)/2)

for i in range(0,len(x)-1):
    slope_1 = f(x[i],y_Heun_15[i])
    y_Heun_15.append(y_Heun_15[i] + slope_1*h)   # predictor
    for j in range(15):
        slope_2 = f(x[i+1],y_Heun_15[i+1])
        y_Heun_15[i+1] = y_Heun_15[i] + h*(slope_1+slope_2)/2   # corrector


print('--------------------------------------------------')
print("                  Iterations of Heun's Method")
print('             -------------------------------------')
print('                       1                 15')
print('             ------------------ ------------------')
print('x   y_true     y_Heun   |et|(%)   y_Heun   |et|(%)')
print('- ---------- ---------- ------- ---------- -------')
for i in range(len(x)):
    et_1 = np.abs((y_true[i] - y_Heun_1[i])/y_true[i])
    et_15 = np.abs((y_true[i] - y_Heun_15[i])/y_true[i])
    print(f'{x[i]} {y_true[i]:10.7f} {y_Heun_1[i]:10.7f}  {et_1:6.2%} {y_Heun_15[i]:10.7f}  {et_15:6.2%}')
print('--------------------------------------------------')



