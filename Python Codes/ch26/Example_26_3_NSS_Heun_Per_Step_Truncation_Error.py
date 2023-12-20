import numpy as np

def f(x,y):
    return 4*np.exp(0.8*x) - 0.5*y

def y_analytic(x):    # p.736 Example 25.5
    return (4/1.3)*(np.exp(0.8*x) - np.exp(-0.5*x)) + 2*np.exp(-0.5*x)

h = 1
x = np.arange(-1,3)
y_true = y_analytic(x)

y = [y_true[0], y_true[1]]



for i in range(1,3):
    yp = y[i-1] + f(x[i], y[i])*2*h
    yc = yp
    for j in range(10):
        yc = y[i] + (f(x[i],y[i]) + f(x[i+1],yc))*h/2
    y.append(yc)
    
    Ec = -(yc - yp)/5
    Et = y_true[i+1] - yc
    print(f"at x={x[i+1]}: predicted value = {yp:.7f}, corrected value = {yc:.7f}, estimated error = {Ec:.7f}, true error = {Et:.7f}")


