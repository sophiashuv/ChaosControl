import numpy as np
import matplotlib.pyplot as plt


def henon_attractor(x, y, a=1.4, b=0.03):
    dx = 1 - a * x ** 2 + y
    dy = b * x
    return dx, dy


def logistic_eq(r, x, y):
    dx, dy = henon_attractor(x, y, a=1.4, b=r)
    return dx


def bifurcation_diagram(seed, n_skip, n_iter, step=0.0001, r_min=0):
    print("Starting with x0 seed {0}, skip plotting first {1} iterations, "
          "then plot next {2} iterations.".format(seed, n_skip, n_iter))
    R, X, Y = [], [], []
    r_range = np.linspace(r_min, 4, int(1 / step))

    for r in r_range:
        x = seed
        y = seed
        for i in range(n_iter + n_skip + 1):
            if i >= n_skip:
                R.append(r)
                X.append(x)
                Y.append(y)

            x, y = henon_attractor(x, y, a=r, b=0.3)
    plt.style.use('seaborn')
    plt.figure(figsize=(10, 5))
    plt.plot(R, X, ls='', marker=',')

    plt.ylim(-1.5, 1.5)
    plt.xlim(r_min, 1.5)
    plt.xlabel('a')
    plt.ylabel('X')
    plt.show()


bifurcation_diagram(1.5, 100, 200)
