import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

WIDTH, HEIGHT, DPI = 1000, 750, 100


def lorenz(t, xyz):
    x, y, z = xyz
    s, r, b = 10, 28, 8 / 3.  # parameters Lorentz used
    return [s * (y - x), x * (r - z) - y, x * y - b * z]


a, b, n = 0, 150, 10000
t = np.linspace(a, b, n)

sol1 = solve_ivp(lorenz, [a, b], [1, 1, 1], t_eval=t, dense_output=True)

x, y, z = sol1.sol(t)


fig = plt.figure(facecolor='k', figsize=(WIDTH/DPI, HEIGHT/DPI))
ax = fig.gca(projection='3d')
ax.set_facecolor('k')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

s = 10
cmap = plt.cm.winter
for i in range(0,n-s,s):
    ax.plot(x[i:i+s+1], y[i:i+s+1], z[i:i+s+1], color=cmap(i/n), alpha=0.4)

ax.set_axis_off()
plt.savefig('lorenz.png', dpi=DPI)
plt.show()