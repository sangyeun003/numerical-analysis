import numpy as np

def f(x,y):
    return 4*np.exp(0.8*x) - 0.5*y

def y_analytic(x):    # p.736 Example 25.5
    return (4/1.3)*(np.exp(0.8*x) - np.exp(-0.5*x)) + 2*np.exp(-0.5*x)

h = 1
x = np.arange(-1,3)
y_true = y_analytic(x)

y = [y_true[0], y_true[1]]
yp = [None, None]

for i in range(1,3):
    yp.append(y[i-1] + f(x[i], y[i])*2*h)
    if i>1:
        yp[i+1] = yp[i+1] + (4/5)*(y[i] - yp[i])    # predictor modifier
    yc = yp[i+1]
    for j in range(5):
        yc = y[i] + (f(x[i],y[i]) + f(x[i+1],yc))*h/2
    yc = yc - (yc - yp[i+1])/5   # corrector modifier
    y.append(yc)

    Et = y_true[i+1] - yc
    et = np.abs(Et/y_true[i+1])
    print(f"at x={x[i+1]}: true error = {Et:.7f}, true relative error = {et:.3%}")


