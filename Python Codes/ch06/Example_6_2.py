import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,6)
y1 = x
y2 = np.exp(-x)


print(' x   y1   y2')
print('--- --- -----')
for i in range(0,x.size):
    print(f'{x[i]:2.1f} {y1[i]:2.1f} {y2[i]:4.3f}')

xx = np.linspace(0,1,100)

fig, axes = plt.subplots(2,1)

for i in range(2):
    axes[i].spines.left.set_position('zero')
    axes[i].spines.right.set_color('none')
    axes[i].spines.bottom.set_position('zero')
    axes[i].spines.top.set_color('none')
    axes[i].xaxis.set_ticks_position('bottom')
    axes[i].yaxis.set_ticks_position('left')

axes[0].plot(xx, np.exp(-xx) - xx, 'k', label='$f(x)=e^{-x}-x$')
axes[0].legend()

axes[1].plot(xx, xx, 'b', label='$f_1(x)=x$')
axes[1].plot(xx, np.exp(-xx), 'r', label='$f_2(x)=e^{-x}$')
axes[1].legend()

plt.show()

