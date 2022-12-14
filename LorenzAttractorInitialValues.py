import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def lorenz(t, xyz):
    x, y, z = xyz
    s, r, b = 10, 28, 8 / 3.  # parameters Lorentz used
    return [s * (y - x), x * (r - z) - y, x * y - b * z]


a, b = 0, 40
t = np.linspace(a, b, 4000)

sol1 = solve_ivp(lorenz, [a, b], [1, 1, 1], t_eval=t)
sol2 = solve_ivp(lorenz, [a, b], [1, 1, 1.00001], t_eval=t)

plt.style.use('seaborn')
plt.plot(sol1.y[0], sol1.y[2])
plt.plot(sol2.y[0], sol2.y[2])
plt.plot(sol1.y[0][-1], sol1.y[2][-1], 'o', color="blue")
plt.plot(sol2.y[0][-1], sol2.y[2][-1], 'o', color="green")
plt.xlabel("$x$")
plt.ylabel("$z$")
plt.style.use('seaborn')
plt.show()
plt.savefig("lorenz_xz.png")
plt.close()

plt.subplot(211)
plt.plot(sol1.t, sol1.y[0])
plt.plot(sol2.t, sol2.y[0])
plt.xlabel("$t$")
plt.ylabel("$x_1(t)$")
plt.subplot(212)
plt.plot(sol1.t, sol1.y[0] - sol2.y[0])
plt.ylabel("$x_1(t) - x_2(t)$")
plt.xlabel("$t$")
plt.style.use('seaborn')

plt.show()
plt.savefig("lorenz_x.png")
