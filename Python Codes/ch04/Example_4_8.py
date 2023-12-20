import numpy as np
import matplotlib.pyplot as plt

def diffex(func, dfunc, x, n):
    dftrue = dfunc(x)
    h = 1
    H = [h]
    D = [(func(x+h) - func(x-h))/(2*h)]
    E = [np.abs(dftrue - D[0])]
    for i in range(1,n):
        h = h/10
        H.append(h)
        D.append((func(x+h) - func(x-h))/(2*h))
        E.append(np.abs(dftrue - D[i]))

    L = np.array([H,D,E]).transpose()
    print('    step size  finite difference     true error')
    print('  ------------ -----------------  ---------------')
    for i in range(L.shape[0]):
        print(f'{L[i,0]:14.10f} {L[i,1]:16.14f} {L[i,2]:16.13f}')

    fig, ax = plt.subplots()
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Step Size')
    plt.ylabel('Error')
    plt.title('Plot of Error Versus Step Size')
    ax.plot(H, E)
    plt.show()

   

def ff(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

def df(x):
    return -0.4*x**3 - 0.45*x**2 - x - 0.25

diffex(ff,df,0.5,11)


