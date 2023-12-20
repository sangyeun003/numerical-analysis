import numpy as np
import math

def IterMeth(x,es,maxit):
    # initialization
    iter = 1
    sol = 1
    ea = 100

    # iterative calculation
    while True:
        solold = sol

        sol = sol + x**iter/math.factorial(iter)
        iter = iter + 1
        if sol != 0:
            ea = abs((sol - solold)/sol)*100
        if ea<=es or iter>=maxit:
            break
    return (sol,ea,iter)

val, ea, iter = IterMeth(1, 1e-6, 100)

print(f'computed value (val) = {val}')
print(f'approximate percent relative error (ea) = {ea}')
print(f'number of iterations (iter) = {iter}')

trueval = np.exp(1)

print(f'true value (trueval) = {trueval}')

et = abs((trueval-val)/trueval)*100

print(f'true percent relative error (et) = {et}')

