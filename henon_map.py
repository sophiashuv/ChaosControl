# python3
import numpy as np
import matplotlib.pyplot as plt


def henon_attractor(x, y, a=1.4, b=0.3):
    x_next = 1 - a * x ** 2 + y
    y_next = b * x
    return x_next, y_next


steps = 100000
X = np.zeros(steps + 1)
Y = np.zeros(steps + 1)

X[0], Y[0] = 0, -1

for i in range(steps):
    x_next, y_next = henon_attractor(X[i], Y[i])
    X[i + 1] = x_next
    Y[i + 1] = y_next


plt.style.use('seaborn')
plt.plot(X, Y, '^', markersize=0.8)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()
plt.close()

# for i in range(steps):
#     x_dot, y_dot = henon_attractor(X[i], Y[i])
#     X[i+1] = x_dot
#     Y[i+1] = y_dot
#     plt.xlim(-1.5, 1.5)
#     plt.ylim(-0.5, 0.5)
#
#     plt.plot(X, Y, '^', color='white', alpha = 0.8, markersize=0.3)
#     plt.axis('off')
#     plt.savefig('{}.png'.format(i), dpi=300)
#     plt.close()