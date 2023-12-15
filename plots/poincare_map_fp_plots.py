import matplotlib.pyplot as plt
import numpy as np


def func(x, p):
    e, mu, x_bar, beta, nu, xi, phi = p
    return (e * mu + x_bar) * beta * (x**nu) * np.cos(xi * np.log(x) + phi)


mu = 0.01
nu = 1
pars = [0.5, mu, 1, 0.1, nu, 10, 0]

z = np.linspace(0, 0.1, num=10000)

fig, ax = plt.subplots()
ax.plot(z, func(z, pars), color="black")
ax.plot(z, z - mu, color="red")
ax.set_xlabel(r"$z$")
ax.set_ylim([-0.06, 0.08])
ax.set_title(r"$\mu>0$")
