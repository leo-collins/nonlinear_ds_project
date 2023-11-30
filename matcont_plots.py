import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat

origin_branch = loadmat("matcont/origin_branch.mat")
limit_cycle_from_hopf = loadmat("matcont/limit_cycle_from_hopf_origin.mat")
first_period_doubling = loadmat("matcont/first_period_doubling.mat")
second_period_doubling = loadmat("matcont/second_period_doubling.mat")
third_period_doubling = loadmat("matcont/third_period_doubling.mat")

origin_branch_x_stable = origin_branch["x"][0][:5]
origin_branch_x_unstable = origin_branch["x"][0][5:13]
origin_branch_A_stable = origin_branch["x"][3][:5]
origin_branch_A_unstable = origin_branch["x"][3][5:13]

limit_cycle_max_x_stable = np.max(limit_cycle_from_hopf["x"][:-2:3], axis=0)[:720]
limit_cycle_max_x_unstable = np.max(limit_cycle_from_hopf["x"][:-2:3], axis=0)[720:]
limit_cycle_A_stable = limit_cycle_from_hopf["x"][-1][:720]
limit_cycle_A_unstable = limit_cycle_from_hopf["x"][-1][720:]

first_period_doubling_max_x_stable = np.max(first_period_doubling["x"][:-2:3], axis=0)[
    :197
]
first_period_doubling_max_x_unstable = np.max(
    first_period_doubling["x"][:-2:3], axis=0
)[197:]
first_period_doubling_A_stable = first_period_doubling["x"][-1][:197]
first_period_doubling_A_unstable = first_period_doubling["x"][-1][197:]

second_period_doubling_max_x_stable = np.max(
    second_period_doubling["x"][:-2:3], axis=0
)[:95]
second_period_doubling_max_x_unstable = np.max(
    second_period_doubling["x"][:-2:3], axis=0
)[95:]
second_period_doubling_A_stable = second_period_doubling["x"][-1][:95]
second_period_doubling_A_unstable = second_period_doubling["x"][-1][95:]

third_period_doubling_max_x_stable = np.max(third_period_doubling["x"][:-2:3], axis=0)[
    :45
]
third_period_doubling_max_x_unstable = np.max(
    third_period_doubling["x"][:-2:3], axis=0
)[45:]
third_period_doubling_A_stable = third_period_doubling["x"][-1][:45]
third_period_doubling_A_unstable = third_period_doubling["x"][-1][45:]

plt.plot(
    origin_branch_A_stable,
    origin_branch_x_stable,
    linestyle="solid",
    c="black",
    zorder=0,
)
plt.plot(
    origin_branch_A_unstable,
    origin_branch_x_unstable,
    linestyle="dashed",
    c="black",
    zorder=1,
)
plt.plot(
    limit_cycle_A_stable,
    limit_cycle_max_x_stable,
    linestyle="solid",
    c="green",
    zorder=2,
)
plt.plot(
    limit_cycle_A_unstable,
    limit_cycle_max_x_unstable,
    linestyle="dashed",
    c="green",
    zorder=3,
)
plt.plot(
    first_period_doubling_A_stable,
    first_period_doubling_max_x_stable,
    linestyle="solid",
    c="blue",
    zorder=4,
)
plt.plot(
    first_period_doubling_A_unstable,
    first_period_doubling_max_x_unstable,
    linestyle="dashed",
    c="blue",
    zorder=5,
)
plt.plot(
    second_period_doubling_A_stable,
    second_period_doubling_max_x_stable,
    linestyle="solid",
    c="red",
    zorder=6,
)
plt.plot(
    second_period_doubling_A_unstable,
    second_period_doubling_max_x_unstable,
    linestyle="dashed",
    c="red",
    zorder=7,
)
plt.plot(
    third_period_doubling_A_stable,
    third_period_doubling_max_x_stable,
    linestyle="solid",
    c="green",
    zorder=8,
)
plt.plot(
    third_period_doubling_A_unstable,
    third_period_doubling_max_x_unstable,
    linestyle="dashed",
    c="green",
    zorder=9,
)
plt.scatter([0.0595], [0], c="black", zorder=10, s=20)
plt.scatter([0.2301], [5.78414], c="black", zorder=11, s=20)
plt.scatter([0.26749154], [6.68178963], c="black", zorder=12, s=20)
plt.scatter([0.27599168], [6.87807003], c="black", zorder=13, s=20)
# plt.ylim(5.5, 7.5)
# plt.xlim(0.22, 0.3)
plt.xlabel("A")
plt.ylabel("max x")
plt.show()
