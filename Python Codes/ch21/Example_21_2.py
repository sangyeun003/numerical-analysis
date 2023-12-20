import numpy as np

I_exact = 3076/1875 # 1.640533...  Example 21.5 on p.628

a = 0
b = 0.8

print('-------------------------')
print(' n     h       I    et(%)')
print('--  ------  ------  -----')
for n in range(2,11):
    x = np.linspace(a,b,n+1)
    w = np.ones(len(x))
    w[[0,-1]] = [1/2, 1/2]  # replace the 1st and last elements with 1/2
    # Now, w = [1/2, 1, 1, ..., 1, 1, 1/2]

    I = np.dot( np.polyval([400, -900, 675, -200, 25, 0.2], x) ,w)*(b-a)/n # (21.10) on p.620
    Et = np.abs(100*(I_exact - I)/I_exact)    # relative percent error
    print(f'{n:>2}  {(b-a)/n:>.4f}  {I:>.4f}  {Et:4.1f}')
print('-------------------------')

