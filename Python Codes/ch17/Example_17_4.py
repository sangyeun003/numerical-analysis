import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,6)
y = np.array([0.5, 1.7, 3.4, 5.7, 8.4])

logx = np.log(x)
logy = np.log(y)

# https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
# numpy 자체 least square method
A = np.vstack([logx, np.ones(len(logx))]).T	# 첫 행을 logx 벡터로, 두 번째 행을 전부 1로 logx의 길이만큼해서 배열 만들고, transpose

beta, log_alpha = np.linalg.lstsq(A, logy, rcond=None)[0]
print(beta, log_alpha)
alpha = np.exp(log_alpha)

fig, ax = plt.subplots(2)

xx = np.linspace(0,5,100)

ax[0].set_xlim([0,9]) # To make the graph look similar to Figure 17.10(a).
_ = ax[0].plot(x, y, 'o', label='Original data', markersize=10)
_ = ax[0].plot(xx, alpha*np.power(xx, beta), 'r', label='Fitted power function')
_ = ax[0].legend()


plt.xscale('log')
plt.yscale('log')
xx = np.linspace(1,7,100)
_ = ax[1].plot(x, y, 'o', label='Original data (logscale)', markersize=10)
_ = ax[1].plot(xx, alpha*np.power(xx, beta), 'r', label='Fitted line')
_ = ax[1].legend()


plt.show()

