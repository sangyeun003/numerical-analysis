import numpy as np

def f(x):
    return np.polyval([-0.1, -0.15, -0.5, -0.25, 1.2], x)

D_exact = -0.9125

x = 0.5

D = {}
et = {}

for h in [0.5, 0.25]:
    D[h] = (f(x+h) - f(x-h))/(2*h)
    et[h] = (D_exact - D[h])/D_exact*100
    print(f'derivative computed using the central difference with h={h}: {D[h]:.4f} (relative error(%) = {et[h]:.1f})')

D_extra = (4/3)*D[0.25] - (1/3)*D[0.5]

print(f'derivative computed by Richardson extrapolation = {D_extra:.4f} (relative error(%) = {(D_exact-D_extra)/D_exact:.1f})')

