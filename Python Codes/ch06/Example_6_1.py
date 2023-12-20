import numpy as np

xi = 0
x_true = 0.56714329
print(' i    xi     ea(%)  et(%)  et_{i+1}/et_i')
print('-- -------- ------ ------- -------------')
for i in range(11):
    if i>0:
        ea = np.abs(100*(xi-xi_old)/xi)
        et_old = et
    et = np.abs(100*(xi-x_true)/x_true)
    if i>0:
        print(f'{i:>2d} {xi:.6f} {ea:6.2f} {et:7.3f} {et/et_old:7.3f}')
    else:
        print(f'{i:>2d} {xi:.6f}        {et:7.3f}')
    xi_old = xi
    xi = np.exp(-xi)

    
