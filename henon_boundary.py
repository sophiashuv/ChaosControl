import numpy as np
import matplotlib.pyplot as plt
import copy


def henon_boundary(max_iterations, a, b):
    x_range = 2000
    y_range = 2000

    x_list = np.arange(-5, 5, 10 / x_range)
    y_list = np.arange(5, -5, -10 / y_range)
    array = np.meshgrid(x_list, y_list)

    x2 = np.zeros(x_range)
    y2 = np.zeros(y_range)
    iterations_until_divergence = np.meshgrid(x2, y2)

    for i in iterations_until_divergence:
        for j in i:
            j += max_iterations

    not_already_diverged = array[0] < 1000
    for k in range(max_iterations):
        array_copied = copy.deepcopy(array[0])

        array[0] = 1 - a * array[0] ** 2 + array[1]
        array[1] = b * array_copied

        r = (array[0] ** 2 + array[1] ** 2) ** 0.5
        diverging = r > 10
        diverging_now = diverging & not_already_diverged
        iterations_until_divergence[0][diverging_now] = k
        not_already_diverged = np.invert(diverging_now) & not_already_diverged

        array[0][diverging] = 0
        array[1][diverging] = 0

    return iterations_until_divergence[0]


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

plt.plot(X, Y, ',', alpha = 0.8, markersize=0.3)
henon_boundary = henon_boundary(70, a=1.4, b=0.3)
plt.imshow(henon_boundary, extent=[-5, 5, -5, 5], alpha=1)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.plot(-1.1314, -0.3394, 'o', color="red")
plt.plot(0.6314, 0.1894, 'o', color="red")
plt.show()
plt.savefig('Henon_boundary.png', dpi=300)
plt.close()
