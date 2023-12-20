import numpy as np
import math

def compute_exponential(x):
    term = np.single(0)
    sum = np.single(0)
    test = None
    i = 0
    print(f'   i      term           sum')
    print(f'  --- ------------  ------------')
    while True:
        if sum == test:
            break
        i = i+1
        test = sum
#        term = (x**i)/math.factorial(i)
#        term = np.single(np.power(x,i))/np.single(math.factorial(i))
#        term = np.single(np.single(x**i)/np.single(math.factorial(i)))
        term = np.single((x**i)/math.factorial(i))
        sum = sum + term
        print(f' {i:>3d}  {term:+.6e}  {sum:+.6e} ')


print(f'\n\ncomputing exp(10)')
compute_exponential(10)
print(f'\n\ncomputing exp(-10)')
compute_exponential(-10)
        
