import numpy as np

def f(x):
    return np.polyval([400, -900, 675, -200, 25, 0.2], x)

I = {}
a = 0
b = 0.8

max_level = 4


print(' --------------- --------------- --------------- ---------------')
print('      O(h^2)          O(h^4)          O(h^6)          O(h^8)')
print(' --------------- --------------- --------------- ---------------')

for levels in range(2,max_level+1):
    print(f' number of levels = {levels}\n')
    for j in range(1,levels+1):
        n = 2**(j-1)
        x = np.linspace(a,b,n+1)
        w = np.ones(n+1)
        w[[0,-1]] = 1/2
        I[(j,1)] = np.dot(f(x), w)*(b-a)/n
    
    
    for k in range(2,levels+1):
        for j in range(1,levels - k+2):
            # (22.8) on p.647
            I[(j,k)] = (4**(k-1)*I[(j+1,k-1)] - I[(j,k-1)])/(4**(k-1)-1)
    
    for j in range(1,levels+2):
        row = ''
        for k in range(1,levels - j+2):
            row = row + f' I({j},{k})={I[(j,k)]:8.6f}'
        print(row)

    print(f' ea = {(I[(1,levels)] - I[(2,levels-1)])/I[(1,levels)]:.1%}')
    print(' ---------------------------------------------------------------')

